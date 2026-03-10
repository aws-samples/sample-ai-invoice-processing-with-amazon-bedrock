# Technology Stack

## Core Technologies

### AWS Services
- **Amazon Bedrock**: Multimodal AI processing and knowledge bases for document understanding
- **Amazon S3**: Secure document storage and file management
- **AWS Lambda**: Serverless processing and scalability
- **Additional AWS services**: For integration and enterprise connectivity

### Programming Language
- **Python**: Primary development language for all components
- **python-docx**: Library for Word document generation and manipulation

### Document Processing
- **Microsoft Word (.docx)**: Primary document format for invoices, contracts, and reports
- **Document formatting**: Consistent styling with Calibri font, proper spacing, and structured layouts

### Development Environment
- **Virtual Environment**: `.venv` directory for Python dependency isolation
- **Package Management**: Standard Python package management practices

## Common Commands

### Environment Setup
```bash
# Activate virtual environment
source .venv/bin/activate

# Install dependencies
pip install python-docx

# Deactivate environment
deactivate
```

### Document Generation
```bash
# Generate sample invoice
python sample_invoice.py

# Generate vendor contract
python vendor_contract.py

# Create PRFAQ documents
python docs/create_prfaq.py
python docs/create_formatted_prfaq.py

# Extract Word document formatting
python docs/extract_word_formatting.py
```

## Architecture Patterns

### Document Generation Pattern
- Consistent font usage (Arial for invoices, Times New Roman for contracts, Calibri for PRFAQs)
- Standardized spacing and margin settings
- Reusable formatting functions (`set_font`, `set_paragraph_spacing`)
- Structured document creation with clear sections

### File Organization
- Sample documents in root directory
- Documentation and utilities in `docs/` folder
- Generated documents follow naming convention: `[Type]_[Entity]_[Identifier].docx`