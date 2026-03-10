# InvoiceFlow AI - User Guide

This guide walks you through testing the InvoiceFlow AI application with sample documents.

## Prerequisites

- Application deployed and running (`streamlit run simplified_app.py`)
- Access to the web interface at `http://localhost:8501`
- Login credentials (check deployment output for admin password)

## Test Documents

The `docs/` folder contains three test files:

| File | Purpose |
|------|---------|
| `Vendor_Contract_TechCorp_Solutions.pdf` | Master Services Agreement with TechCorp |
| `Compliant_Invoice_TechCorp_INV-2025-0109.pdf` | Invoice that passes all contract validations |
| `Complex_Invoice_DataFlow_Systems_INV-2024-3847.pdf` | Invoice with multiple compliance violations |

---

## Step 1: Upload Contract to Knowledge Base

1. Navigate to the **"Knowledge Base"** tab
2. Click **"Browse files"** and select `Vendor_Contract_TechCorp_Solutions.pdf`
3. Click **"Upload Contract"**
4. Wait for confirmation: "Contract uploaded and synced successfully"

This indexes the contract terms for validation:
- Approved vendor: TechCorp Solutions Inc.
- Hourly rates: Senior Consultant $185, Software Developer $145, Technical Support $95, Project Management $165
- Contract period: December 1, 2024 - November 30, 2025
- Payment terms: Net 30 days
- Maximum invoice: $250,000

---

## Step 2: Process Compliant Invoice

1. Navigate to the **"Process Invoice"** tab
2. Upload `Compliant_Invoice_TechCorp_INV-2025-0109.pdf`
3. Click **"Process Invoice"**

**Expected Result: APPROVE**

The invoice should pass validation because:
- ✅ Vendor is authorized (TechCorp Solutions Inc.)
- ✅ Invoice date within contract period
- ✅ All hourly rates match contract terms
- ✅ Only approved service categories
- ✅ Payment terms: Net 30 days

---

## Step 3: Process Non-Compliant Invoice

1. Navigate to the **"Process Invoice"** tab
2. Upload `Complex_Invoice_DataFlow_Systems_INV-2024-3847.pdf`
3. Click **"Process Invoice"**

**Expected Result: REJECT**

The invoice should fail validation due to:
- ❌ Vendor not authorized under contract
- ❌ Hourly rates exceed contracted amounts
- ❌ Unapproved service categories
- ❌ Other compliance violations

---

## Step 4: Review Results Dashboard

1. Navigate to the **"Results Dashboard"** tab
2. View processing history for all invoices
3. Compare compliance scores and recommendations

---

## Understanding Validation Results

| Field | Description |
|-------|-------------|
| **Vendor Approved** | Is the vendor authorized under contract? |
| **Rates Approved** | Do hourly rates match contract terms? |
| **Amount Within Limits** | Is total within contract limits? |
| **Payment Terms Match** | Do payment terms match contract? |
| **Compliance Score** | Overall score (0-100) |
| **Recommendation** | APPROVE, MANUAL REVIEW, or REJECT |

---

## Troubleshooting

**Issue**: "Knowledge Base not configured"
- Ensure deployment completed successfully
- Check `infrastructure/infrastructure_outputs.json` exists

**Issue**: Contract not found during validation
- Verify contract was uploaded to Knowledge Base
- Wait for sync to complete (may take 30-60 seconds)

**Issue**: Processing fails
- Check file size (max 10MB)
- Verify PDF is not corrupted
- Review logs in `logs/invoiceflow_debug.log`
