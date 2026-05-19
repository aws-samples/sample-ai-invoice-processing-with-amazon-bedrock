"""
Textract vs LLM Invoice Extraction Comparison Page

Allows users to upload an invoice PDF and compare extraction results from:
1. Amazon Textract (AnalyzeExpense API)
2. Amazon Bedrock LLM (Claude Sonnet)

Displays header-level and line-item-level extraction side by side.
"""

import streamlit as st
import boto3
import json
import base64
import time
import pandas as pd
from typing import Dict, Any, List

st.set_page_config(page_title="Textract vs LLM Comparison", page_icon="🔬", layout="wide")

# --- Configuration ---
AWS_REGION = "us-east-1"
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB

AVAILABLE_MODELS = {
    "Claude Sonnet 4.6": "us.anthropic.claude-sonnet-4-6",
    "Claude Opus 4.5": "us.anthropic.claude-opus-4-5-20251101-v1:0",
}


# --- AWS Client Initialization ---
@st.cache_resource
def get_aws_clients():
    """Initialize AWS clients (cached across reruns)."""
    session = boto3.Session(region_name=AWS_REGION)
    return {
        "textract": session.client("textract"),
        "bedrock": session.client("bedrock-runtime"),
    }


# --- Textract Extraction ---
def extract_with_textract(file_bytes: bytes) -> Dict[str, Any]:
    """Extract invoice data using Amazon Textract AnalyzeExpense API."""
    clients = get_aws_clients()
    textract = clients["textract"]

    response = textract.analyze_expense(
        Document={"Bytes": file_bytes}
    )

    header_fields = {}
    other_fields = []
    line_items = []

    for doc in response.get("ExpenseDocuments", []):
        # Extract summary/header fields — separate OTHER into its own list
        for field in doc.get("SummaryFields", []):
            field_type = field.get("Type", {}).get("Text", "")
            value = field.get("ValueDetection", {}).get("Text", "")
            confidence = field.get("ValueDetection", {}).get("Confidence", 0)
            if field_type and value:
                if field_type == "OTHER":
                    other_fields.append({"value": value, "confidence": round(confidence, 2)})
                else:
                    header_fields[field_type] = {
                        "value": value,
                        "confidence": round(confidence, 2),
                    }

        # Extract line item groups (skip OTHER and EXPENSE_ROW)
        for group in doc.get("LineItemGroups", []):
            for line_item in group.get("LineItems", []):
                item = {}
                for field in line_item.get("LineItemExpenseFields", []):
                    field_type = field.get("Type", {}).get("Text", "")
                    value = field.get("ValueDetection", {}).get("Text", "")
                    confidence = field.get("ValueDetection", {}).get("Confidence", 0)
                    if field_type and field_type not in ("OTHER", "EXPENSE_ROW"):
                        item[field_type] = {
                            "value": value,
                            "confidence": round(confidence, 2),
                        }
                if item:
                    line_items.append(item)

    return {"header": header_fields, "line_items": line_items, "other": other_fields}


# --- LLM Extraction ---
def extract_with_llm(file_bytes: bytes, model_id: str) -> Dict[str, Any]:
    """Extract invoice data using Amazon Bedrock Claude."""
    clients = get_aws_clients()
    bedrock = clients["bedrock"]

    encoded = base64.b64encode(file_bytes).decode("utf-8")

    prompt = """You are an invoice data extraction system. Extract ALL data from this invoice document.

You MUST return a JSON object with exactly two keys: "header" and "line_items".

For "header", extract these EXACT fields (use empty string if not found):
- VENDOR_NAME: Company name of the vendor/seller
- VENDOR_ADDRESS: Full vendor address as one string
- VENDOR_STREET: Street portion of vendor address
- VENDOR_CITY: City of vendor
- VENDOR_STATE: State/province of vendor
- VENDOR_ZIP_CODE: Postal/zip code of vendor
- VENDOR_COUNTRY: Country of vendor
- VENDOR_PHONE: Vendor phone number
- VENDOR_EMAIL: Vendor email address
- TAX_PAYER_ID: Tax ID / GST / ABN number of vendor
- INVOICE_RECEIPT_ID: Invoice number
- INVOICE_RECEIPT_DATE: Invoice date
- DUE_DATE: Payment due date
- PO_NUMBER: Purchase order number
- PAYMENT_TERMS: Payment terms (e.g., Net 30)
- RECEIVER_NAME: Bill-to company/person name
- RECEIVER_ADDRESS: Full bill-to address
- SUBTOTAL: Subtotal before tax
- TAX: Tax amount
- DISCOUNT: Discount amount (include negative sign if shown)
- TOTAL: Total amount due
- AMOUNT_DUE: Final amount due (same as TOTAL if no other adjustments)
- BANK_NAME: Bank name for payment
- ACCOUNT_NUMBER: Bank account number
- ROUTING_NUMBER: Bank routing/IFSC code
- SWIFT_CODE: SWIFT/BIC code

For "line_items", extract an array where each item has:
- ITEM: Item description/service name
- QUANTITY: Quantity or hours
- UNIT_PRICE: Rate per unit/hour
- PRICE: Line total amount (quantity x unit_price)

Return ONLY valid JSON. No explanation or markdown."""

    body = json.dumps({
        "anthropic_version": "bedrock-2023-05-31",
        "max_tokens": 4000,
        "messages": [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt},
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": encoded,
                        },
                    },
                ],
            }
        ],
    })

    response = bedrock.invoke_model(
        modelId=model_id,
        body=body,
    )

    result = json.loads(response["body"].read())
    text = result["content"][0]["text"]

    # Parse JSON from response
    start = text.find("{")
    end = text.rfind("}") + 1
    if start != -1 and end > start:
        return json.loads(text[start:end])

    return {"header": {}, "line_items": [], "error": "Could not parse LLM response"}


# --- Display Helpers ---
def normalize_textract_header(header: Dict) -> Dict[str, str]:
    """Extract values from Textract header, keeping original field names."""
    normalized = {}
    for key, data in header.items():
        normalized[key] = data["value"]
    return normalized


def normalize_textract_line_items(items: List[Dict]) -> List[Dict[str, str]]:
    """Normalize Textract line items keeping original field names."""
    normalized = []
    for item in items:
        row = {}
        for key, data in item.items():
            row[key] = data["value"]
        normalized.append(row)
    return normalized


def fuzzy_match(val_a: str, val_b: str) -> str:
    """Compare two values with fuzzy logic. Returns ✅, ⚠️, or ❌."""
    a = val_a.strip().lower().rstrip(",.")
    b = val_b.strip().lower().rstrip(",.")
    if not a or not b:
        return "—"
    if a == b:
        return "✅"
    # Check if one contains the other
    if a in b or b in a:
        return "🟡"
    return "❌"


# Fields we actually want to compare (common between both engines)
COMPARISON_FIELDS = [
    "VENDOR_NAME", "VENDOR_ADDRESS", "VENDOR_STREET", "VENDOR_CITY",
    "VENDOR_STATE", "VENDOR_ZIP_CODE", "VENDOR_COUNTRY", "VENDOR_PHONE",
    "TAX_PAYER_ID", "INVOICE_RECEIPT_ID", "INVOICE_RECEIPT_DATE",
    "DUE_DATE", "PO_NUMBER", "PAYMENT_TERMS",
    "RECEIVER_NAME", "RECEIVER_ADDRESS",
    "SUBTOTAL", "TAX", "DISCOUNT", "TOTAL", "AMOUNT_DUE",
]


def display_header_comparison(textract_header: Dict, llm_header: Dict, textract_other: List = None):
    """Display header fields side by side with fuzzy matching."""
    st.subheader("📋 Header-Level Extraction")

    # Show comparison for key fields first, then extras
    all_fields = sorted(set(list(textract_header.keys()) + list(llm_header.keys())))
    key_fields = [f for f in COMPARISON_FIELDS if f in textract_header or f in llm_header]
    extra_fields = [f for f in all_fields if f not in COMPARISON_FIELDS]

    rows = []
    for field in key_fields + extra_fields:
        t_val = textract_header.get(field, "")
        l_val = llm_header.get(field, "")
        match = fuzzy_match(t_val, l_val)
        rows.append({
            "Field": field,
            "Textract": t_val if t_val else "—",
            "LLM (Claude)": l_val if l_val else "—",
            "Match": match,
        })

    df = pd.DataFrame(rows)
    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True,
        column_config={
            "Field": st.column_config.TextColumn(width="medium"),
            "Textract": st.column_config.TextColumn(width="large"),
            "LLM (Claude)": st.column_config.TextColumn(width="large"),
            "Match": st.column_config.TextColumn(width="small"),
        },
    )

    # Unbiased scorecard
    st.markdown("---")
    st.markdown("#### 📊 Extraction Scorecard")

    # Count what each engine found
    t_extracted = len([r for r in rows if r["Textract"] != "—"])
    l_extracted = len([r for r in rows if r["LLM (Claude)"] != "—"])
    t_other_count = len(textract_other) if textract_other else 0

    comparable = [r for r in rows if r["Textract"] != "—" and r["LLM (Claude)"] != "—"]
    exact = len([r for r in comparable if r["Match"] == "✅"])
    partial = len([r for r in comparable if r["Match"] == "🟡"])
    total_comparable = len(comparable)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("**Amazon Textract**")
        st.metric("Named Fields Extracted", t_extracted)
        st.metric("Unclassified (OTHER) Fields", t_other_count)
        st.metric("Total Data Points", t_extracted + t_other_count)

    with col2:
        st.markdown("**LLM (Claude)**")
        st.metric("Named Fields Extracted", l_extracted)
        st.metric("Unclassified Fields", "0")
        st.metric("Total Data Points", l_extracted)

    with col3:
        st.markdown("**Agreement (where both extracted)**")
        if total_comparable > 0:
            st.metric("Fields Both Found", total_comparable)
            st.metric("Exact Match", f"{exact} ({100*exact//total_comparable}%)")
            st.metric("Partial Match", f"{partial} ({100*partial//total_comparable}%)")
        else:
            st.info("No overlapping fields to compare")

    # Show what each found that the other missed
    t_only = [r["Field"] for r in rows if r["Textract"] != "—" and r["LLM (Claude)"] == "—"]
    l_only = [r["Field"] for r in rows if r["LLM (Claude)"] != "—" and r["Textract"] == "—"]

    if t_only or l_only:
        st.markdown("#### 🔎 Coverage Gaps")
        gc1, gc2 = st.columns(2)
        with gc1:
            if t_only:
                st.markdown(f"**Textract found, LLM missed** ({len(t_only)}):")
                st.code("\n".join(t_only))
            else:
                st.success("LLM covered all Textract named fields")
        with gc2:
            if l_only:
                st.markdown(f"**LLM found, Textract missed** ({len(l_only)}):")
                st.code("\n".join(l_only))
            else:
                st.success("Textract covered all LLM fields")

    # Show Textract OTHER fields transparently
    if textract_other:
        with st.expander(f"📎 Textract unclassified data ({t_other_count} items) — detected but not labeled"):
            for i, o in enumerate(textract_other, 1):
                st.text(f"{i}. {o['value']}")


def display_line_items_comparison(textract_items: List[Dict], llm_items: List[Dict]):
    """Display line items from both sources."""
    st.subheader("📦 Line-Item Extraction")

    col1, col2 = st.columns(2)

    with col1:
        st.markdown("**Amazon Textract**")
        if textract_items:
            df_t = pd.DataFrame(textract_items)
            st.dataframe(df_t, use_container_width=True, hide_index=True)
        else:
            st.info("No line items extracted by Textract.")
        st.caption(f"{len(textract_items)} line items detected")

    with col2:
        st.markdown("**LLM (Claude Sonnet)**")
        if llm_items:
            df_l = pd.DataFrame(llm_items)
            st.dataframe(df_l, use_container_width=True, hide_index=True)
        else:
            st.info("No line items extracted by LLM.")
        st.caption(f"{len(llm_items)} line items detected")


def display_raw_json(textract_result: Dict, llm_result: Dict):
    """Show raw JSON output in expandable sections."""
    st.subheader("🔍 Raw Extraction Output")
    col1, col2 = st.columns(2)
    with col1:
        with st.expander("Textract Raw JSON", expanded=False):
            st.json(textract_result)
        # Show OTHER fields separately
        other = textract_result.get("other", [])
        if other:
            with st.expander(f"Textract 'OTHER' fields ({len(other)} unlabeled)", expanded=False):
                st.caption("These are fields Textract detected but couldn't classify into a named type:")
                for i, o in enumerate(other, 1):
                    st.text(f"{i}. {o['value']}")
    with col2:
        with st.expander("LLM Raw JSON", expanded=False):
            st.json(llm_result)


# --- Main Page ---
st.title("🔬 Textract vs LLM — Invoice Extraction Comparison")
st.markdown(
    "Upload an invoice PDF to compare extraction accuracy between "
    "**Amazon Textract** (AnalyzeExpense) and **Amazon Bedrock LLM** (Claude Sonnet)."
)

st.divider()

# Model selection
selected_model_name = st.selectbox(
    "🤖 Select LLM Model",
    options=list(AVAILABLE_MODELS.keys()),
    help="Choose which Claude model to use for extraction comparison",
)
selected_model_id = AVAILABLE_MODELS[selected_model_name]

# File upload
uploaded_file = st.file_uploader(
    "Upload Invoice PDF",
    type=["pdf"],
    help="Max 10 MB. Supported: PDF invoices.",
)

if uploaded_file:
    if uploaded_file.size > MAX_FILE_SIZE:
        st.error(f"File too large ({uploaded_file.size / 1024 / 1024:.1f} MB). Max is 10 MB.")
    else:
        st.success(f"📄 **{uploaded_file.name}** ({uploaded_file.size / 1024:.1f} KB)")

        if st.button("🚀 Extract & Compare", type="primary"):
            file_bytes = uploaded_file.read()

            col_t, col_l = st.columns(2)

            # Run both extractions
            textract_result = None
            llm_result = None

            with col_t:
                st.markdown("#### ⚙️ Amazon Textract")
                with st.spinner("Running Textract AnalyzeExpense..."):
                    t_start = time.time()
                    try:
                        textract_result = extract_with_textract(file_bytes)
                        t_time = time.time() - t_start
                        st.success(f"Done in {t_time:.1f}s")
                    except Exception as e:
                        st.error(f"Textract error: {e}")

            with col_l:
                st.markdown(f"#### 🤖 {selected_model_name}")
                with st.spinner(f"Running {selected_model_name}..."):
                    l_start = time.time()
                    try:
                        llm_result = extract_with_llm(file_bytes, selected_model_id)
                        l_time = time.time() - l_start
                        st.success(f"Done in {l_time:.1f}s")
                    except Exception as e:
                        st.error(f"LLM error: {e}")

            st.divider()

            # Display comparison if both succeeded
            if textract_result and llm_result:
                # Normalize Textract output (keep original field names)
                norm_t_header = normalize_textract_header(textract_result["header"])
                norm_t_items = normalize_textract_line_items(textract_result["line_items"])
                textract_other = textract_result.get("other", [])

                # LLM already uses same field names now
                llm_header = llm_result.get("header", {})
                # Remove empty string values from LLM output
                llm_header = {k: v for k, v in llm_header.items() if v}
                llm_items = llm_result.get("line_items", [])

                # Header comparison
                display_header_comparison(norm_t_header, llm_header, textract_other)

                st.divider()

                # Line items comparison
                display_line_items_comparison(norm_t_items, llm_items)

                st.divider()

                # Raw JSON
                display_raw_json(textract_result, llm_result)

            elif textract_result:
                st.warning("Only Textract results available.")
                norm_t_header = normalize_textract_header(textract_result["header"])
                norm_t_items = normalize_textract_line_items(textract_result["line_items"])
                display_header_comparison(norm_t_header, {})
                display_line_items_comparison(norm_t_items, [])

            elif llm_result:
                st.warning("Only LLM results available.")
                display_header_comparison({}, llm_result.get("header", {}))
                display_line_items_comparison([], llm_result.get("line_items", []))

else:
    st.info("👆 Upload an invoice PDF to get started.")

    # Show sample invoices available
    with st.expander("📂 Sample invoices available in docs/ folder"):
        st.markdown("""
        - `Sample_Invoice_CloudNova_CN-INV-2026-0042.pdf` — US corporate layout (USD)
        - `Sample_Invoice_Meridian_MDS-2026-1187.pdf` — Indian vendor layout (INR + GST)
        """)
