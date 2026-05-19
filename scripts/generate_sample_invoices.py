#!/usr/bin/env python3
"""Generate sample invoices with two different layouts for Textract vs LLM comparison."""

from fpdf import FPDF
from pathlib import Path

DOCS_DIR = Path(__file__).parent.parent / "docs"


def create_invoice_layout_1():
    """Layout 1: Standard corporate invoice - CloudNova Technologies."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Header
    pdf.set_font("Helvetica", "B", 20)
    pdf.cell(0, 12, "INVOICE", ln=True, align="R")
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(0, 6, "CloudNova Technologies Inc.", ln=True)
    pdf.cell(0, 5, "1200 Innovation Drive, Suite 400", ln=True)
    pdf.cell(0, 5, "Seattle, WA 98101, USA", ln=True)
    pdf.cell(0, 5, "Tax ID: 91-7834521", ln=True)
    pdf.cell(0, 5, "Phone: (206) 555-0147 | Email: billing@cloudnova.com", ln=True)
    pdf.ln(8)

    # Invoice details box
    pdf.set_fill_color(240, 240, 240)
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(95, 7, "Bill To:", ln=False)
    pdf.cell(95, 7, "Invoice Details:", ln=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(95, 5, "Amazon Web Services LLC", ln=False)
    pdf.cell(40, 5, "Invoice Number:", ln=False)
    pdf.cell(55, 5, "CN-INV-2026-0042", ln=True)
    pdf.cell(95, 5, "410 Terry Avenue North", ln=False)
    pdf.cell(40, 5, "Invoice Date:", ln=False)
    pdf.cell(55, 5, "April 15, 2026", ln=True)
    pdf.cell(95, 5, "Seattle, WA 98109", ln=False)
    pdf.cell(40, 5, "Due Date:", ln=False)
    pdf.cell(55, 5, "May 15, 2026", ln=True)
    pdf.cell(95, 5, "Attn: Accounts Payable", ln=False)
    pdf.cell(40, 5, "PO Number:", ln=False)
    pdf.cell(55, 5, "AWS-PO-2026-8891", ln=True)
    pdf.cell(95, 5, "", ln=False)
    pdf.cell(40, 5, "Payment Terms:", ln=False)
    pdf.cell(55, 5, "Net 30", ln=True)
    pdf.ln(8)

    # Line items table header
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(50, 50, 80)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(10, 7, "#", fill=True, align="C")
    pdf.cell(70, 7, "Description", fill=True)
    pdf.cell(25, 7, "Qty", fill=True, align="C")
    pdf.cell(30, 7, "Unit Price", fill=True, align="R")
    pdf.cell(20, 7, "Tax %", fill=True, align="C")
    pdf.cell(35, 7, "Amount (USD)", fill=True, align="R")
    pdf.ln()
    pdf.set_text_color(0, 0, 0)

    # Line items
    items = [
        ("1", "Cloud Infrastructure Consulting - Senior Architect (160 hrs)", "160", "$185.00", "0%", "$29,600.00"),
        ("2", "Data Migration Services - ETL Pipeline Development", "1", "$12,500.00", "0%", "$12,500.00"),
        ("3", "Security Audit & Compliance Assessment (SOC2)", "1", "$8,750.00", "0%", "$8,750.00"),
        ("4", "DevOps Automation - CI/CD Pipeline Setup", "40", "$195.00", "0%", "$7,800.00"),
        ("5", "Training & Knowledge Transfer Sessions (8 sessions)", "8", "$1,200.00", "0%", "$9,600.00"),
        ("6", "24/7 Premium Support - Monthly Retainer (April)", "1", "$4,500.00", "10.25%", "$4,961.25"),
    ]

    pdf.set_font("Helvetica", "", 9)
    for i, item in enumerate(items):
        fill = i % 2 == 0
        if fill:
            pdf.set_fill_color(248, 248, 252)
        pdf.cell(10, 6, item[0], fill=fill, align="C")
        pdf.cell(70, 6, item[1], fill=fill)
        pdf.cell(25, 6, item[2], fill=fill, align="C")
        pdf.cell(30, 6, item[3], fill=fill, align="R")
        pdf.cell(20, 6, item[4], fill=fill, align="C")
        pdf.cell(35, 6, item[5], fill=fill, align="R")
        pdf.ln()

    pdf.ln(5)

    # Totals
    pdf.set_font("Helvetica", "", 10)
    pdf.cell(135, 6, "", ln=False)
    pdf.cell(25, 6, "Subtotal:", ln=False, align="R")
    pdf.cell(30, 6, "$73,211.25", ln=True, align="R")
    pdf.cell(135, 6, "", ln=False)
    pdf.cell(25, 6, "Tax (10.25%):", ln=False, align="R")
    pdf.cell(30, 6, "$461.25", ln=True, align="R")
    pdf.cell(135, 6, "", ln=False)
    pdf.cell(25, 6, "Discount:", ln=False, align="R")
    pdf.cell(30, 6, "-$1,500.00", ln=True, align="R")
    pdf.set_font("Helvetica", "B", 11)
    pdf.cell(135, 8, "", ln=False)
    pdf.cell(25, 8, "TOTAL DUE:", ln=False, align="R")
    pdf.cell(30, 8, "$72,172.50", ln=True, align="R")
    pdf.ln(8)

    # Payment info
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(0, 6, "Payment Information:", ln=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, "Bank: First National Bank | Account: 7823-4561-9900 | Routing: 021000021", ln=True)
    pdf.cell(0, 5, "Wire Reference: CN-INV-2026-0042 | SWIFT: FNBKUS33", ln=True)
    pdf.ln(5)
    pdf.set_font("Helvetica", "I", 8)
    pdf.cell(0, 5, "Thank you for your business. Late payments subject to 1.5% monthly interest.", ln=True)

    output_path = DOCS_DIR / "Sample_Invoice_CloudNova_CN-INV-2026-0042.pdf"
    pdf.output(str(output_path))
    print(f"Created: {output_path}")


def create_invoice_layout_2():
    """Layout 2: Detailed services invoice - Meridian Data Systems (different layout)."""
    pdf = FPDF()
    pdf.add_page()
    pdf.set_auto_page_break(auto=True, margin=15)

    # Top banner style header
    pdf.set_fill_color(20, 60, 120)
    pdf.rect(10, 10, 190, 25, "F")
    pdf.set_text_color(255, 255, 255)
    pdf.set_font("Helvetica", "B", 18)
    pdf.set_y(14)
    pdf.cell(100, 10, "  Meridian Data Systems", ln=False)
    pdf.set_font("Helvetica", "B", 14)
    pdf.cell(90, 10, "TAX INVOICE", ln=True, align="R")
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(0, 5, "  Enterprise Solutions | Cloud Architecture | Managed Services", ln=True)
    pdf.set_text_color(0, 0, 0)
    pdf.ln(10)

    # Two-column header: Vendor left, Invoice right
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(95, 5, "FROM:", ln=False)
    pdf.cell(95, 5, "INVOICE TO:", ln=True)
    pdf.set_font("Helvetica", "", 9)
    pdf.cell(95, 5, "Meridian Data Systems Pvt. Ltd.", ln=False)
    pdf.cell(95, 5, "Amazon Development Center", ln=True)
    pdf.cell(95, 5, "45 Tech Park, Whitefield", ln=False)
    pdf.cell(95, 5, "Bagmane World Technology Center", ln=True)
    pdf.cell(95, 5, "Bangalore, Karnataka 560066, India", ln=False)
    pdf.cell(95, 5, "Marathahalli, Bangalore 560048", ln=True)
    pdf.cell(95, 5, "GSTIN: 29AABCM1234F1Z5", ln=False)
    pdf.cell(95, 5, "GSTIN: 29AABCA5765R1ZP", ln=True)
    pdf.cell(95, 5, "PAN: AABCM1234F", ln=False)
    pdf.cell(95, 5, "", ln=True)
    pdf.cell(95, 5, "Email: invoices@meridiandata.in", ln=False)
    pdf.cell(95, 5, "", ln=True)
    pdf.ln(6)

    # Invoice metadata in a grid
    pdf.set_fill_color(230, 240, 250)
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(32, 6, " Invoice No.", fill=True)
    pdf.cell(45, 6, " MDS/2026/INV-1187", fill=True)
    pdf.cell(5, 6, "")
    pdf.cell(32, 6, " Invoice Date", fill=True)
    pdf.cell(45, 6, " 01-Apr-2026", fill=True)
    pdf.ln()
    pdf.cell(32, 6, " PO Number", fill=True)
    pdf.cell(45, 6, " AMZN-PO-IND-44521", fill=True)
    pdf.cell(5, 6, "")
    pdf.cell(32, 6, " Due Date", fill=True)
    pdf.cell(45, 6, " 01-May-2026", fill=True)
    pdf.ln()
    pdf.cell(32, 6, " Currency", fill=True)
    pdf.cell(45, 6, " INR (Indian Rupees)", fill=True)
    pdf.cell(5, 6, "")
    pdf.cell(32, 6, " Terms", fill=True)
    pdf.cell(45, 6, " Net 30 Days", fill=True)
    pdf.ln(10)

    # Line items
    pdf.set_font("Helvetica", "B", 9)
    pdf.set_fill_color(20, 60, 120)
    pdf.set_text_color(255, 255, 255)
    pdf.cell(8, 7, "SL", fill=True, align="C")
    pdf.cell(55, 7, "Service Description", fill=True)
    pdf.cell(20, 7, "SAC Code", fill=True, align="C")
    pdf.cell(15, 7, "Hrs/Qty", fill=True, align="C")
    pdf.cell(25, 7, "Rate (INR)", fill=True, align="R")
    pdf.cell(30, 7, "Amount (INR)", fill=True, align="R")
    pdf.cell(25, 7, "GST 18%", fill=True, align="R")
    pdf.ln()
    pdf.set_text_color(0, 0, 0)

    items = [
        ("1", "ML Platform Development - Lead Engineer", "998314", "120", "4,500", "5,40,000", "97,200"),
        ("2", "Data Engineering - Spark/EMR Optimization", "998314", "80", "3,800", "3,04,000", "54,720"),
        ("3", "Cloud Architecture Review & Design", "998312", "40", "5,200", "2,08,000", "37,440"),
        ("4", "Kubernetes Cluster Management (Monthly)", "998315", "1", "1,85,000", "1,85,000", "33,300"),
        ("5", "Automated Testing Framework Development", "998314", "60", "3,500", "2,10,000", "37,800"),
        ("6", "Production Support & Incident Mgmt (Apr)", "998316", "1", "2,50,000", "2,50,000", "45,000"),
        ("7", "Documentation & Runbook Creation", "998312", "20", "2,800", "56,000", "10,080"),
    ]

    pdf.set_font("Helvetica", "", 8)
    for i, item in enumerate(items):
        fill = i % 2 == 0
        if fill:
            pdf.set_fill_color(245, 248, 252)
        pdf.cell(8, 6, item[0], fill=fill, align="C")
        pdf.cell(55, 6, item[1], fill=fill)
        pdf.cell(20, 6, item[2], fill=fill, align="C")
        pdf.cell(15, 6, item[3], fill=fill, align="C")
        pdf.cell(25, 6, item[4], fill=fill, align="R")
        pdf.cell(30, 6, item[5], fill=fill, align="R")
        pdf.cell(25, 6, item[6], fill=fill, align="R")
        pdf.ln()

    pdf.ln(5)

    # Totals section
    pdf.set_font("Helvetica", "", 9)
    x_start = 110
    pdf.cell(x_start, 6, "")
    pdf.cell(40, 6, "Subtotal:", align="R")
    pdf.cell(35, 6, "17,53,000.00", align="R")
    pdf.ln()
    pdf.cell(x_start, 6, "")
    pdf.cell(40, 6, "CGST (9%):", align="R")
    pdf.cell(35, 6, "1,57,770.00", align="R")
    pdf.ln()
    pdf.cell(x_start, 6, "")
    pdf.cell(40, 6, "SGST (9%):", align="R")
    pdf.cell(35, 6, "1,57,770.00", align="R")
    pdf.ln()
    pdf.set_font("Helvetica", "B", 10)
    pdf.cell(x_start, 8, "")
    pdf.cell(40, 8, "Grand Total:", align="R")
    pdf.cell(35, 8, "20,68,540.00", align="R")
    pdf.ln(3)
    pdf.set_font("Helvetica", "I", 8)
    pdf.cell(x_start, 6, "")
    pdf.cell(75, 6, "Amount in words: Twenty Lakh Sixty-Eight Thousand Five Hundred Forty Only", align="R")
    pdf.ln(8)

    # Bank details
    pdf.set_font("Helvetica", "B", 9)
    pdf.cell(0, 6, "Bank Details for Payment:", ln=True)
    pdf.set_font("Helvetica", "", 8)
    pdf.cell(0, 5, "Bank: HDFC Bank Ltd. | Branch: Whitefield, Bangalore", ln=True)
    pdf.cell(0, 5, "Account No: 50200045678901 | IFSC: HDFC0001234 | SWIFT: HDFCINBB", ln=True)
    pdf.ln(5)

    # Footer notes
    pdf.set_font("Helvetica", "I", 8)
    pdf.cell(0, 4, "This is a computer-generated invoice. No signature required.", ln=True)
    pdf.cell(0, 4, "Subject to Bangalore jurisdiction. E&OE.", ln=True)

    output_path = DOCS_DIR / "Sample_Invoice_Meridian_MDS-2026-1187.pdf"
    pdf.output(str(output_path))
    print(f"Created: {output_path}")


if __name__ == "__main__":
    create_invoice_layout_1()
    create_invoice_layout_2()
    print("Done! Sample invoices generated.")
