# Project Structure

## Directory Organization

```
├── .kiro/                          # Kiro IDE configuration and steering rules
├── .venv/                          # Python virtual environment (isolated dependencies)
├── docs/                           # Documentation and document generation utilities
│   ├── create_prfaq.py            # Basic PRFAQ document generator
│   ├── create_formatted_prfaq.py  # Formatted PRFAQ with proper styling
│   ├── extract_word_formatting.py # Utility to analyze Word document formatting
│   ├── solution.txt               # Project solution description and pitch
│   ├── InvoiceFlow_AI_PRFAQ.docx  # Generated PRFAQ document
│   ├── InvoiceFlow_AI_PRFAQ_Formatted.docx # Formatted PRFAQ document
│   └── Nexus PRFAQ P&S Final.docx # Reference document for formatting
├── sample_invoice.py              # Sample invoice document generator
├── vendor_contract.py             # Vendor contract document generator
├── Sample_Invoice_TechCorp_INV-2024-1215.docx # Generated sample invoice
└── Vendor_Contract_TechCorp_Solutions.docx    # Generated vendor contract
```

## File Naming Conventions

### Generated Documents
- **Invoices**: `Sample_Invoice_[Company]_[InvoiceNumber].docx`
- **Contracts**: `Vendor_Contract_[Company]_[Type].docx`
- **PRFAQs**: `[Product]_[Type]_PRFAQ[_Variant].docx`

### Python Scripts
- **Document generators**: `[document_type].py` (e.g., `sample_invoice.py`)
- **Utilities**: `[action]_[target].py` (e.g., `extract_word_formatting.py`)
- **Documentation scripts**: Located in `docs/` directory

## Code Organization Patterns

### Document Generator Structure
1. **Imports**: Standard libraries first, then third-party (python-docx)
2. **Helper Functions**: Reusable formatting functions at the top
3. **Document Creation**: Main document generation logic
4. **Content Sections**: Organized by document sections (header, body, footer)
5. **Save and Validation**: Document saving with success confirmation

### Common Helper Functions
- `set_font(paragraph, font_name, font_size)`: Standardize font formatting
- `set_paragraph_spacing(paragraph, space_after)`: Control paragraph spacing
- `create_custom_style()`: Define reusable document styles

### Document Structure Standards
- **Margins**: Consistent margin settings (typically 1" all around)
- **Fonts**: Document-type specific fonts (Arial for invoices, Times New Roman for contracts, Calibri for PRFAQs)
- **Spacing**: Proper paragraph spacing and alignment
- **Sections**: Clear separation between document sections

## Development Workflow

1. **Environment Setup**: Activate `.venv` before development
2. **Document Generation**: Run appropriate Python script to generate documents
3. **Validation**: Each generator includes validation output and success confirmation
4. **Documentation**: Keep `docs/` folder for all documentation-related files and utilities