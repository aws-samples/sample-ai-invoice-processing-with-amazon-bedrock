#!/usr/bin/env python3
"""
InvoiceFlow AI - Bedrock Invoice Processing with Knowledge Base
"""

import streamlit as st
import json
import time
import os
import boto3
import pandas as pd
import base64
import logging
from datetime import datetime
from typing import List, Dict, Any

# Ensure logs directory exists
LOG_DIR = os.path.join(os.path.dirname(__file__), 'logs')
os.makedirs(LOG_DIR, exist_ok=True)

# Configure logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(os.path.join(LOG_DIR, 'invoiceflow_debug.log')),
    ]
)
# Separate handler for console (INFO level only)
console_handler = logging.StreamHandler()
console_handler.setLevel(logging.INFO)
console_handler.setFormatter(logging.Formatter('%(asctime)s - %(levelname)s - %(message)s'))
logging.getLogger().addHandler(console_handler)

logger = logging.getLogger(__name__)

# File upload limits
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10 MB
MAX_UPLOADS_PER_HOUR = 10
SESSION_TIMEOUT_SECONDS = 30 * 60  # 30 minutes

def check_upload_rate_limit() -> bool:
    """Check if user has exceeded upload rate limit."""
    if 'upload_times' not in st.session_state:
        st.session_state.upload_times = []
    
    current_time = time.time()
    # Remove timestamps older than 1 hour
    st.session_state.upload_times = [
        t for t in st.session_state.upload_times 
        if current_time - t < 3600  # 1 hour in seconds
    ]
    
    # Check if under limit
    return len(st.session_state.upload_times) < MAX_UPLOADS_PER_HOUR

def record_upload_attempt():
    """Record an upload attempt for rate limiting."""
    if 'upload_times' not in st.session_state:
        st.session_state.upload_times = []
    st.session_state.upload_times.append(time.time())

def check_session_timeout() -> bool:
    """Check if session has timed out."""
    current_time = time.time()
    if 'last_activity' not in st.session_state:
        st.session_state.last_activity = current_time
        return False
    
    # Check if session has timed out
    if current_time - st.session_state.last_activity > SESSION_TIMEOUT_SECONDS:
        return True
    
    # Update last activity
    st.session_state.last_activity = current_time
    return False

def validate_invoice_data(invoice_data: Dict[str, Any]) -> Dict[str, Any]:
    """Validate and sanitize extracted invoice data."""
    if not isinstance(invoice_data, dict):
        return {"error": "Invalid data format"}
    
    # Return the data as-is since Claude already provides structured data
    # Just add basic validation for security
    validated_data = invoice_data.copy()
    
    # Validate vendor name length for security
    if "vendor" in validated_data and isinstance(validated_data["vendor"], dict):
        if "name" in validated_data["vendor"]:
            validated_data["vendor"]["name"] = str(validated_data["vendor"]["name"])[:100]
        if "address" in validated_data["vendor"]:
            validated_data["vendor"]["address"] = str(validated_data["vendor"]["address"])[:200]
        if "tax_id" in validated_data["vendor"]:
            validated_data["vendor"]["tax_id"] = str(validated_data["vendor"]["tax_id"])[:20]
    
    # Validate line items count for security
    if "line_items" in validated_data and isinstance(validated_data["line_items"], list):
        validated_data["line_items"] = validated_data["line_items"][:50]  # Limit to 50 items
    
    return validated_data

def load_config():
    """Load application configuration from config file."""
    config_file = "config.json"
    if os.path.exists(config_file):
        with open(config_file, 'r', encoding='utf-8') as f:
            return json.load(f)
    return {}

def load_infrastructure_config(retry_count=3, retry_delay=2):
    """Load configuration from infrastructure outputs with retry logic."""
    config_file = "infrastructure/infrastructure_outputs.json"
    
    for attempt in range(retry_count):
        if os.path.exists(config_file):
            try:
                with open(config_file, 'r', encoding='utf-8') as f:
                    config = json.load(f)
                    # Validate that required keys exist
                    required_keys = ['knowledge_base_id', 'data_source_id', 's3_bucket']
                    missing_keys = [key for key in required_keys if not config.get(key)]
                    if missing_keys:
                        if attempt == retry_count - 1:  # Last attempt
                            st.error(f"❌ Configuration file missing required keys: {missing_keys}")
                            st.info("Please run the deployment script to generate complete configuration.")
                        else:
                            time.sleep(retry_delay)
                            continue
                    return config
            except json.JSONDecodeError as e:
                if attempt == retry_count - 1:  # Last attempt
                    st.error(f"❌ Invalid JSON in configuration file: {e}")
                else:
                    time.sleep(retry_delay)
                    continue
            except Exception as e:
                if attempt == retry_count - 1:  # Last attempt
                    st.error(f"❌ Error reading configuration file: {e}")
                else:
                    time.sleep(retry_delay)
                    continue
        else:
            if attempt == retry_count - 1:  # Last attempt
                st.warning("⚠️ Configuration file not found: infrastructure/infrastructure_outputs.json")
                st.info("Please run the deployment script first to create the infrastructure.")
            else:
                time.sleep(retry_delay)
                continue
    
    return {}

# Load infrastructure outputs
infra_config = load_infrastructure_config()

# Load application configuration
app_config = load_config()

def validate_startup_configuration():
    """Validate that all required configuration is present."""
    issues = []
    
    if not infra_config:
        issues.append("Infrastructure configuration file not found or empty")
    
    if not infra_config.get('knowledge_base_id'):
        issues.append("Knowledge Base ID not configured")
    
    if not infra_config.get('data_source_id'):
        issues.append("Data Source ID not configured")
    
    if not infra_config.get('s3_bucket'):
        issues.append("S3 Bucket not configured")
    
    if issues:
        st.error("❌ Configuration Issues Detected:")
        for issue in issues:
            st.write(f"• {issue}")
        
        st.info("""
        **To fix these issues:**
        1. Navigate to the `infrastructure/` directory
        2. Run: `python cognito_deployment.py`
        3. Wait for deployment to complete
        4. Restart this Streamlit app
        
        📖 **For detailed troubleshooting steps, see:** `TROUBLESHOOTING.md`
        """)
        
        st.warning("⚠️ Some features may not work until configuration is complete.")
        return False
    
    return True

# Validate configuration on startup
config_valid = validate_startup_configuration()

def get_aws_session():
    """Get AWS session, using app role if configured."""
    app_role_arn = os.getenv("APP_ROLE_ARN", infra_config.get("app_role_arn"))
    
    if app_role_arn:
        try:
            sts_client = boto3.client('sts')
            response = sts_client.assume_role(
                RoleArn=app_role_arn,
                RoleSessionName='invoiceflow-app',
                ExternalId='invoiceflow-app',
                DurationSeconds=3600
            )
            
            credentials = response['Credentials']
            return boto3.Session(
                aws_access_key_id=credentials['AccessKeyId'],
                aws_secret_access_key=credentials['SecretAccessKey'],
                aws_session_token=credentials['SessionToken']
            )
        except Exception as e:
            return boto3.Session()
    else:
        return boto3.Session()

# Get AWS session
aws_session = get_aws_session()

# Configuration with fallbacks
AWS_REGION = os.getenv("AWS_REGION", app_config.get("aws", {}).get("region", "us-east-1"))
S3_BUCKET = os.getenv("S3_BUCKET", infra_config.get("s3_bucket", "invoiceflow-ai-bucket"))
EMBEDDINGS_MODEL = os.getenv("EMBEDDINGS_MODEL", app_config.get("aws", {}).get("embeddings_model", "amazon.titan-embed-text-v2:0"))
BEDROCK_MODEL_ID = os.getenv("BEDROCK_MODEL_ID", app_config.get("aws", {}).get("bedrock_model_id", "anthropic.claude-sonnet-4-20250514-v1:0"))
KNOWLEDGE_BASE_ID = os.getenv("KNOWLEDGE_BASE_ID", infra_config.get("knowledge_base_id"))
DATA_SOURCE_ID = os.getenv("DATA_SOURCE_ID", infra_config.get("data_source_id"))
GUARDRAIL_ID = os.getenv("GUARDRAIL_ID", infra_config.get("guardrail_id"))
GUARDRAIL_VERSION = os.getenv("GUARDRAIL_VERSION", infra_config.get("guardrail_version", "DRAFT"))

# Set page config
st.set_page_config(
    page_title="InvoiceFlow AI - Simplified",
    page_icon="🧾",
    layout="wide"
)

class InvoiceProcessor:
    """Invoice processor using Bedrock Knowledge Base."""
    
    def __init__(self, knowledge_base_id=None):
        self.s3_client = aws_session.client('s3', region_name=AWS_REGION)
        self.bedrock_client = aws_session.client('bedrock-runtime', region_name=AWS_REGION)
        self.bedrock_agent_client = aws_session.client('bedrock-agent', region_name=AWS_REGION)
        self.bedrock_agent_runtime_client = aws_session.client('bedrock-agent-runtime', region_name=AWS_REGION)
        self.knowledge_base_id = knowledge_base_id or KNOWLEDGE_BASE_ID
        self.data_source_id = DATA_SOURCE_ID
        
        # Get account ID for inference profile ARN
        sts_client = aws_session.client('sts')
        self.account_id = sts_client.get_caller_identity()['Account']
    
    def upload_contract_to_s3(self, file_content, filename):
        """Upload contract to S3 knowledge base."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            key = f"knowledge-base/contracts/{filename}"
            
            self.s3_client.put_object(
                Bucket=S3_BUCKET,
                Key=key,
                Body=file_content,
                ContentType='application/pdf'
            )
            
            return {"success": True, "bucket": S3_BUCKET, "key": key}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def list_contracts(self):
        """List all contracts in knowledge base."""
        try:
            response = self.s3_client.list_objects_v2(
                Bucket=S3_BUCKET,
                Prefix="knowledge-base/contracts/"
            )
            
            contracts = []
            if 'Contents' in response:
                for obj in response['Contents']:
                    if obj['Key'].endswith('.pdf'):
                        contracts.append({
                            'name': obj['Key'].split('/')[-1],
                            'key': obj['Key'],
                            'size': obj['Size'],
                            'last_modified': obj['LastModified']
                        })
            
            return contracts
        except Exception as e:
            st.error(f"Error listing contracts: {e}")
            return []
    
    def delete_contract(self, key):
        """Delete contract from S3 and all associated vectors."""
        try:
            # Delete the contract PDF
            self.s3_client.delete_object(Bucket=S3_BUCKET, Key=key)
            
            # Delete all associated vector store objects
            contract_name = key.split('/')[-1].replace('.pdf', '')
            
            # Delete contract sections
            sections_response = self.s3_client.list_objects_v2(
                Bucket=S3_BUCKET,
                Prefix=f"vector-store/contracts/{contract_name}/"
            )
            
            if 'Contents' in sections_response:
                for obj in sections_response['Contents']:
                    self.s3_client.delete_object(Bucket=S3_BUCKET, Key=obj['Key'])
            
            # Delete embeddings
            embeddings_response = self.s3_client.list_objects_v2(
                Bucket=S3_BUCKET,
                Prefix=f"vector-store/embeddings/{contract_name}/"
            )
            
            if 'Contents' in embeddings_response:
                for obj in embeddings_response['Contents']:
                    self.s3_client.delete_object(Bucket=S3_BUCKET, Key=obj['Key'])
            
            return {"success": True}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def sync_knowledge_base(self):
        """Sync Knowledge Base data source to ingest new contracts."""
        if not self.knowledge_base_id or not self.data_source_id:
            return {"success": False, "error": "Knowledge Base not configured"}
        
        try:
            response = self.bedrock_agent_client.start_ingestion_job(
                knowledgeBaseId=self.knowledge_base_id,
                dataSourceId=self.data_source_id
            )
            
            job_id = response['ingestionJob']['ingestionJobId']
            return {"success": True, "job_id": job_id}
            
        except Exception as e:
            return {"success": False, "error": str(e)}
    

    
    def upload_to_s3(self, file_content, filename):
        """Upload file to S3."""
        try:
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
            key = f"uploaded-invoices/{timestamp}_{filename}"
            
            self.s3_client.put_object(
                Bucket=S3_BUCKET,
                Key=key,
                Body=file_content,
                ContentType='application/pdf'
            )
            
            return {"success": True, "bucket": S3_BUCKET, "key": key}
        except Exception as e:
            return {"success": False, "error": str(e)}
    
    def check_knowledge_base_status(self):
        """Check if Knowledge Base is configured and ready."""
        if not self.knowledge_base_id or not self.data_source_id:
            return False
        
        # Additional validation: check if the knowledge base actually exists
        try:
            response = self.bedrock_agent_client.get_knowledge_base(
                knowledgeBaseId=self.knowledge_base_id
            )
            return response['knowledgeBase']['status'] in ['ACTIVE', 'AVAILABLE']
        except Exception as e:
            st.error(f"❌ Knowledge Base validation failed: {str(e)}")
            return False
    
    def check_file_exists_in_s3(self, key):
        """Check if file exists in S3."""
        try:
            self.s3_client.head_object(Bucket=S3_BUCKET, Key=key)
            return True
        except Exception:
            return False
    
    def upload_local_file_to_s3(self, local_path, s3_key):
        """Upload local file to S3 if it exists."""
        try:
            if os.path.exists(local_path):
                with open(local_path, 'rb') as f:
                    self.s3_client.put_object(
                        Bucket=S3_BUCKET,
                        Key=s3_key,
                        Body=f.read(),
                        ContentType='application/pdf'
                    )
                return True
        except Exception as e:
            print(f"Error uploading {local_path}: {e}")
        return False
    
    def search_contract_knowledge(self, query, top_k=3):
        """Search contract knowledge using Bedrock Knowledge Base."""
        if not self.knowledge_base_id:
            return []
        
        try:
            response = self.bedrock_agent_runtime_client.retrieve(
                knowledgeBaseId=self.knowledge_base_id,
                retrievalQuery={'text': query},
                retrievalConfiguration={
                    'vectorSearchConfiguration': {
                        'numberOfResults': top_k
                    }
                }
            )
            
            results = []
            for item in response.get('retrievalResults', []):
                results.append({
                    'content': item['content']['text'],
                    'similarity': item.get('score', 0),
                    'source': item.get('location', {}).get('s3Location', {}).get('uri', 'Unknown')
                })
            
            return results
            
        except Exception as e:
            st.error(f"❌ Error searching Knowledge Base: {e}")
            return []
    
    def extract_invoice_data(self, file_content):
        """Extract data from invoice PDF using Bedrock."""
        try:
            encoded_content = base64.b64encode(file_content).decode('utf-8')
            
            message = {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": """Extract comprehensive invoice details and return structured JSON data. Include:
                        - Vendor information (name, address, tax ID, contact details)
                        - Invoice details (number, date, due date, PO number)
                        - Line items (description, quantity, rate, amount)
                        - Total amounts and taxes
                        - Payment terms
                        
                        Return ONLY valid JSON in this structure:
                        {
                            "vendor": {"name": "", "tax_id": "", "address": ""},
                            "invoice": {"number": "", "date": "", "due_date": "", "po_number": ""},
                            "line_items": [{"description": "", "quantity": 0, "rate": 0, "amount": 0}],
                            "totals": {"subtotal": 0, "tax": 0, "total": 0},
                            "payment_terms": ""
                        }"""
                    },
                    {
                        "type": "document",
                        "source": {
                            "type": "base64",
                            "media_type": "application/pdf",
                            "data": encoded_content
                        }
                    }
                ]
            }
            
            response = self.bedrock_client.invoke_model(
                modelId=f"us.{BEDROCK_MODEL_ID}",
                body=json.dumps({
                    "anthropic_version": "bedrock-2023-05-31",
                    "max_tokens": 4000,
                    "messages": [message]
                }),
                guardrailIdentifier=GUARDRAIL_ID if GUARDRAIL_ID else None,
                guardrailVersion=GUARDRAIL_VERSION if GUARDRAIL_ID else None
            )
            
            result = json.loads(response['body'].read())
            extracted_text = result['content'][0]['text']
            
            logger.debug(f"Raw extraction response: {extracted_text}")
            
            # Try to parse JSON from the response
            # Find JSON in the response
            start = extracted_text.find('{')
            end = extracted_text.rfind('}') + 1
            if start != -1 and end != 0:
                json_str = extracted_text[start:end]
                logger.debug(f"Extracted JSON string: {json_str}")
                try:
                    parsed_data = json.loads(json_str)
                    logger.debug(f"Parsed data: {parsed_data}")
                    # Validate and sanitize the extracted data
                    return validate_invoice_data(parsed_data)
                except json.JSONDecodeError as e:
                    logger.debug(f"JSON decode error: {e}")
                    pass
        
            return {"error": "Could not parse JSON", "raw_response": extracted_text}
            
        except Exception as e:
            return {"error": str(e)}
    
    def validate_against_contract(self, invoice_data):
        """Validate invoice against contract using LLM with Knowledge Base."""
        if not self.knowledge_base_id:
            return {
                "vendor_approved": False,
                "amount_within_limits": False,
                "rates_approved": False,
                "payment_terms_match": False,
                "po_number_valid": False,
                "line_items_approved": False,
                "overall_compliance": False,
                "issues": ["Knowledge Base not configured"],
                "warnings": [],
                "contract_matches": [],
                "compliance_score": 0
            }
        
        try:
            # Create validation prompt with invoice data
            invoice_summary = f"""
            INVOICE DETAILS TO VALIDATE:
            - Vendor: {invoice_data.get('vendor', {}).get('name', 'Unknown')} (Tax ID: {invoice_data.get('vendor', {}).get('tax_id', 'Unknown')})
            - Invoice Number: {invoice_data.get('invoice', {}).get('number', 'Unknown')}
            - Invoice Date: {invoice_data.get('invoice', {}).get('date', 'Unknown')}
            - Total Amount: ${invoice_data.get('totals', {}).get('total', 0):,.2f}
            - Payment Terms: {invoice_data.get('payment_terms', 'Unknown')}
            - PO Number: {invoice_data.get('invoice', {}).get('po_number', 'Unknown')}
            
            LINE ITEMS:
            """
            
            line_items = invoice_data.get('line_items', [])
            if line_items:
                for i, item in enumerate(line_items, 1):
                    invoice_summary += f"""
            {i}. {item.get('description', 'Unknown')} - Qty: {item.get('quantity', 0)}, Rate: ${item.get('rate', 0)}/hr, Amount: ${item.get('amount', 0):,.2f}"""
            else:
                invoice_summary += "\n(No detailed line items provided)"
            
            validation_prompt = f"""
            You are an AI contract compliance validator. Analyze this invoice against the contract terms in the knowledge base.
            
            {invoice_summary}
            
            VALIDATION REQUIREMENTS:
            1. Vendor Authorization: Is this vendor authorized under existing contracts?
            2. Amount Limits: Does the invoice amount comply with contract limits?
            3. Rate Validation: Do hourly rates match contracted rates for each service type?
            4. Payment Terms: Do payment terms match contract requirements?
            5. PO Number: Is the PO number format valid per contract requirements?
            6. Service Authorization: Are the services/line items covered under contract?
            
            Return your analysis in this EXACT JSON format:
            {{
                "vendor_approved": true/false,
                "amount_within_limits": true/false,
                "rates_approved": true/false,
                "payment_terms_match": true/false,
                "po_number_valid": true/false,
                "line_items_approved": true/false,
                "overall_compliance": true/false,
                "compliance_score": 0-100,
                "issues": ["list of contract violations"],
                "warnings": ["list of warnings/concerns"],
                "contract_matches": ["relevant contract sections found"],
                "detailed_analysis": "comprehensive explanation of findings"
            }}
            
            Base your analysis ONLY on the contract terms found in the knowledge base. Be specific about which contract sections support your findings.
            """
            
            # Use Bedrock retrieve and generate for contract-aware validation
            # For cross-region inference models, use inference profile ARN format with account ID
            model_arn = f"arn:aws:bedrock:{AWS_REGION}:{self.account_id}:inference-profile/us.{BEDROCK_MODEL_ID}"
            
            logger.debug(f"Using model ARN: {model_arn}")
            logger.debug(f"Knowledge Base ID: {self.knowledge_base_id}")
            logger.debug(f"Validation prompt: {validation_prompt[:500]}...")
            
            # Build configuration with optional guardrail
            kb_config = {
                'knowledgeBaseId': self.knowledge_base_id,
                'modelArn': model_arn,
                'retrievalConfiguration': {
                    'vectorSearchConfiguration': {
                        'numberOfResults': 10
                    }
                }
            }
            
            rag_config = {
                'type': 'KNOWLEDGE_BASE',
                'knowledgeBaseConfiguration': kb_config
            }
            
            response = self.bedrock_agent_runtime_client.retrieve_and_generate(
                input={'text': validation_prompt},
                retrieveAndGenerateConfiguration=rag_config
            )
            
            llm_response = response['output']['text']
            logger.debug(f"LLM Response: {llm_response}")
            
            # Also check what citations were retrieved
            if 'citations' in response:
                logger.debug(f"Citations found: {len(response['citations'])}")
                for i, citation in enumerate(response['citations'][:3]):  # Show first 3
                    logger.debug(f"Citation {i+1}: {citation.get('retrievedReferences', [{}])[0].get('content', {}).get('text', '')[:200]}...")
            else:
                logger.debug("No citations in response")
            
            # Extract JSON from LLM response
            try:
                # Try multiple JSON extraction strategies
                json_str = None
                
                # Strategy 1: Find JSON between curly braces
                start = llm_response.find('{')
                end = llm_response.rfind('}') + 1
                if start != -1 and end > start:
                    json_str = llm_response[start:end]
                    try:
                        validation_results = json.loads(json_str)
                    except json.JSONDecodeError:
                        # Strategy 2: Try finding JSON in code blocks
                        import re
                        json_match = re.search(r'```(?:json)?\s*(\{.*?\})\s*```', llm_response, re.DOTALL)
                        if json_match:
                            json_str = json_match.group(1)
                            validation_results = json.loads(json_str)
                        else:
                            raise ValueError("No valid JSON found")
                
                if not json_str:
                    raise ValueError("No JSON structure found in response")
                
                # Ensure all required fields exist with defaults
                default_results = {
                    "vendor_approved": False,
                    "amount_within_limits": False,
                    "rates_approved": False,
                    "payment_terms_match": False,
                    "po_number_valid": False,
                    "line_items_approved": False,
                    "overall_compliance": False,
                    "compliance_score": 0,
                    "issues": [],
                    "warnings": [],
                    "contract_matches": [],
                    "detailed_analysis": ""
                }
                
                # Merge with defaults
                for key, default_value in default_results.items():
                    if key not in validation_results:
                        validation_results[key] = default_value
                
                # Store full LLM response in detailed_analysis if not already present
                if not validation_results.get("detailed_analysis"):
                    validation_results["detailed_analysis"] = llm_response
                
                return validation_results
                    
            except (json.JSONDecodeError, ValueError) as e:
                # Fallback: parse response text to extract key information
                # Look for compliance indicators in the text
                response_lower = llm_response.lower()
                
                # Parse text for compliance indicators
                vendor_approved = "vendor authorization" in response_lower and "failed" not in response_lower.split("vendor authorization")[1][:100]
                amount_ok = "amount limits" in response_lower and "passed" in response_lower.split("amount limits")[1][:100]
                rates_ok = "rate validation" in response_lower and "passed" in response_lower.split("rate validation")[1][:100]
                
                # Extract issues from text
                issues = []
                if "failed" in response_lower or "violation" in response_lower:
                    # Split by common delimiters and extract failure reasons
                    for line in llm_response.split('\n'):
                        if 'failed' in line.lower() or 'violation' in line.lower() or 'exceed' in line.lower():
                            issues.append(line.strip('*- ').strip())
                
                # Calculate basic compliance score
                compliance_score = 0
                if vendor_approved:
                    compliance_score += 20
                if amount_ok:
                    compliance_score += 20
                if rates_ok:
                    compliance_score += 20
                if not issues:
                    compliance_score += 40
                
                return {
                    "vendor_approved": vendor_approved,
                    "amount_within_limits": amount_ok,
                    "rates_approved": rates_ok,
                    "payment_terms_match": False,
                    "po_number_valid": True,
                    "line_items_approved": False,
                    "overall_compliance": compliance_score >= 80,
                    "compliance_score": compliance_score,
                    "issues": issues if issues else ["Unable to parse detailed validation results"],
                    "warnings": [],
                    "contract_matches": [],
                    "detailed_analysis": llm_response
                }
                
        except Exception as e:
            return {
                "vendor_approved": False,
                "amount_within_limits": False,
                "rates_approved": False,
                "payment_terms_match": False,
                "po_number_valid": False,
                "line_items_approved": False,
                "overall_compliance": False,
                "compliance_score": 0,
                "issues": [f"Validation error: {str(e)}"],
                "warnings": [],
                "contract_matches": [],
                "detailed_analysis": ""
            }
    
    def determine_recommendation(self, invoice_data, validation_results):
        """Determine approval recommendation using LLM analysis."""
        compliance_score = validation_results.get("compliance_score", 0)
        issues = validation_results.get("issues", [])
        warnings = validation_results.get("warnings", [])
        detailed_analysis = validation_results.get("detailed_analysis", "")
        
        # Use LLM's overall compliance assessment
        if validation_results.get("overall_compliance", False) and compliance_score >= 80:
            return "AUTO APPROVE", f"Full contract compliance achieved (Score: {compliance_score}/100)"
        
        # Critical violations = reject
        elif not validation_results.get("vendor_approved", False):
            primary_issue = issues[0] if issues else "Vendor authorization required"
            return "REJECT", primary_issue
        
        elif not validation_results.get("amount_within_limits", False):
            amount_issue = next((issue for issue in issues if "amount" in issue.lower() or "limit" in issue.lower()), "Amount exceeds contract limits")
            return "REJECT", amount_issue
        
        elif not validation_results.get("rates_approved", False):
            rate_issue = next((issue for issue in issues if "rate" in issue.lower() or "hour" in issue.lower()), "Service rates exceed contract terms")
            return "REJECT", rate_issue
        
        elif len(issues) >= 3:
            # Extract first meaningful issue
            primary_issue = issues[0] if issues else "Multiple contract violations detected"
            # Clean up issue text (remove markdown, truncate)
            primary_issue = primary_issue.replace('**', '').replace('*', '').strip()
            if len(primary_issue) > 150:
                primary_issue = primary_issue[:150] + "..."
            return "REJECT", f"{primary_issue} (+{len(issues)-1} more violations)"
        
        # Partial compliance = manual review
        elif compliance_score >= 50 or (warnings and not issues):
            if issues:
                reason = issues[0].replace('**', '').replace('*', '').strip()
            elif warnings:
                reason = warnings[0].replace('**', '').replace('*', '').strip()
            else:
                reason = "Requires manual review"
            
            if len(reason) > 100:
                reason = reason[:100] + "..."
            return "MANUAL REVIEW", f"Partial compliance (Score: {compliance_score}/100) - {reason}"
        
        # Low compliance = reject
        else:
            primary_issue = issues[0] if issues else "Contract compliance verification failed"
            primary_issue = primary_issue.replace('**', '').replace('*', '').strip()
            if len(primary_issue) > 150:
                primary_issue = primary_issue[:150] + "..."
            return "REJECT", primary_issue

# Simple authentication check
def check_authentication():
    """Check if user is authenticated. Returns True if authenticated."""
    if 'authenticated' not in st.session_state:
        st.session_state.authenticated = False
    return st.session_state.authenticated

def show_login_form():
    """Display login form and handle authentication."""
    st.title("🔐 InvoiceFlow AI - Login")
    
    # Handle password change flow
    if st.session_state.get('requires_new_password'):
        with st.form("change_password_form"):
            st.warning("⚠️ You must set a new password on first login.")
            new_password = st.text_input("New Password", type="password")
            confirm_password = st.text_input("Confirm Password", type="password")
            submitted = st.form_submit_button("Set New Password")
            
            if submitted:
                if not new_password or len(new_password) < 12:
                    st.error("Password must be at least 12 characters.")
                elif new_password != confirm_password:
                    st.error("Passwords do not match.")
                else:
                    if _respond_to_new_password_challenge(new_password):
                        st.session_state.authenticated = True
                        st.session_state.requires_new_password = False
                        st.rerun()
                    else:
                        st.error("Failed to set new password. Ensure it meets complexity requirements.")
        return
    
    with st.form("login_form"):
        username = st.text_input("Email")
        password = st.text_input("Password", type="password")
        submitted = st.form_submit_button("Login")
        
        if submitted:
            if username and password:
                result = validate_cognito_credentials(username, password)
                if result == 'authenticated':
                    st.session_state.authenticated = True
                    st.session_state.username = username
                    st.session_state.last_activity = time.time()
                    logger.info(f"User authenticated: {username}")
                    st.rerun()
                elif result == 'new_password_required':
                    st.session_state.requires_new_password = True
                    st.session_state.username = username
                    st.rerun()
                else:
                    st.error("Invalid credentials. Please try again.")
            else:
                st.warning("Please enter both email and password.")
    
    st.info("💡 Check your email for the temporary password sent by Cognito during deployment.")

def validate_cognito_credentials(username, password):
    """Validate credentials against Cognito User Pool. Returns 'authenticated', 'new_password_required', or None."""
    try:
        cognito_client = aws_session.client('cognito-idp', region_name=AWS_REGION)
        client_id = infra_config.get('cognito_client_id')
        client_secret = infra_config.get('cognito_client_secret')
        
        if not client_id:
            logger.error("Cognito client ID not configured - authentication denied")
            return None
        
        auth_params = {
            'USERNAME': username,
            'PASSWORD': password
        }
        
        # Compute SECRET_HASH if client secret is configured
        if client_secret:
            import hmac, hashlib
            msg = username + client_id
            secret_hash = base64.b64encode(
                hmac.new(client_secret.encode('utf-8'), msg.encode('utf-8'), hashlib.sha256).digest()
            ).decode('utf-8')
            auth_params['SECRET_HASH'] = secret_hash
        
        # Note: USER_PASSWORD_AUTH is used because SECRET_HASH is only supported with this flow.
        # Credentials are transmitted over HTTPS (TLS 1.2+) to AWS Cognito endpoints.
        # For production, consider using Cognito Hosted UI with OAuth2/OIDC flows instead.
        response = cognito_client.initiate_auth(
            ClientId=client_id,
            AuthFlow='USER_PASSWORD_AUTH',
            AuthParameters=auth_params
        )
        
        if 'AuthenticationResult' in response:
            return 'authenticated'
        elif response.get('ChallengeName') == 'NEW_PASSWORD_REQUIRED':
            st.session_state.auth_challenge_session = response['Session']
            st.session_state.auth_challenge_username = username
            return 'new_password_required'
        return None
    except Exception as e:
        logger.error(f"Authentication error: {e}")
        return None


def _respond_to_new_password_challenge(new_password):
    """Respond to NEW_PASSWORD_REQUIRED challenge."""
    try:
        cognito_client = aws_session.client('cognito-idp', region_name=AWS_REGION)
        client_id = infra_config.get('cognito_client_id')
        client_secret = infra_config.get('cognito_client_secret')
        username = st.session_state.get('auth_challenge_username')
        
        challenge_responses = {
            'USERNAME': username,
            'NEW_PASSWORD': new_password
        }
        
        if client_secret:
            import hmac, hashlib
            msg = username + client_id
            secret_hash = base64.b64encode(
                hmac.new(client_secret.encode('utf-8'), msg.encode('utf-8'), hashlib.sha256).digest()
            ).decode('utf-8')
            challenge_responses['SECRET_HASH'] = secret_hash
        
        response = cognito_client.respond_to_auth_challenge(
            ClientId=client_id,
            ChallengeName='NEW_PASSWORD_REQUIRED',
            Session=st.session_state.auth_challenge_session,
            ChallengeResponses=challenge_responses
        )
        return 'AuthenticationResult' in response
    except Exception as e:
        logger.error(f"Password change error: {e}")
        return False

# Initialize processor
@st.cache_resource
def get_processor():
    return InvoiceProcessor()

processor = get_processor()

# Initialize session state
if 'processing_results' not in st.session_state:
    st.session_state.processing_results = []

# Check authentication first
if not check_authentication():
    show_login_form()
    st.stop()

# Main UI
# Check session timeout
if check_session_timeout():
    logger.warning("Session timeout - User session expired due to inactivity")
    st.session_state.authenticated = False
    st.error("Session timed out due to inactivity. Please refresh the page to continue.")
    st.stop()

st.title("🧾 InvoiceFlow AI - Invoice Processing")
st.markdown("**AI-Powered Invoice Processing with Contract Validation**")


# Sidebar
with st.sidebar:
    st.header("🔧 System Status")
    
    # Check configuration status
    config_status = True
    if not KNOWLEDGE_BASE_ID:
        st.error("❌ Knowledge Base ID not configured")
        config_status = False
    if not DATA_SOURCE_ID:
        st.error("❌ Data Source ID not configured")
        config_status = False
    if not S3_BUCKET:
        st.error("❌ S3 Bucket not configured")
        config_status = False
    
    if config_status and processor.check_knowledge_base_status():
        st.success("✅ Knowledge Base Connected")
        st.write(f"**KB ID:** {processor.knowledge_base_id[:20]}...")
    elif config_status:
        st.warning("⚠️ Knowledge Base configured but not accessible")
        st.info("Check AWS permissions and knowledge base status")
    else:
        st.error("❌ Knowledge Base Not Configured")
        st.info("Run deployment script to configure infrastructure")
    
    st.subheader("Settings")
    st.info(f"**Bucket:** {S3_BUCKET}\n**Region:** {AWS_REGION}")
    
    # Configuration details (expandable)
    with st.expander("🔍 Configuration Details"):
        st.write(f"**Knowledge Base ID:** {KNOWLEDGE_BASE_ID or 'Not set'}")
        st.write(f"**Data Source ID:** {DATA_SOURCE_ID or 'Not set'}")
        st.write(f"**Bedrock Model:** {BEDROCK_MODEL_ID}")
        st.write(f"**Embeddings Model:** {EMBEDDINGS_MODEL}")
        
        # Refresh configuration button
        if st.button("🔄 Refresh Configuration", help="Reload configuration from file"):
            st.rerun()

# Main tabs
tab1, tab2, tab3, tab4 = st.tabs(["📚 Knowledge Base", "📤 Process Invoice", "🔍 Test Vector Search", "📊 Results Dashboard"])

# Tab 1: Knowledge Base Management
with tab1:
    st.header("📚 Contract Knowledge Base Management")
    
    st.markdown("""
    Upload vendor contracts to build your knowledge base. The system will:
    - Extract contract terms and pricing
    - Create vector embeddings for intelligent search
    - Use this information to validate invoices
    """)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.subheader("📤 Upload New Contract")
        
        uploaded_contract = st.file_uploader(
            "Choose a contract PDF",
            type=['pdf'],
            help="Upload vendor contract for knowledge base",
            key="contract_upload"
        )
        
        if uploaded_contract is not None:
            # Check rate limit FIRST to prevent bypass attacks
            if not check_upload_rate_limit():
                logger.warning(f"Rate limit exceeded - Contract upload blocked")
                st.error(f"Rate limit exceeded. Maximum {MAX_UPLOADS_PER_HOUR} uploads per hour allowed.")
                uploaded_contract = None
            # Then check file size limit
            elif uploaded_contract.size > MAX_FILE_SIZE:
                st.error(f"File size exceeds limit of {MAX_FILE_SIZE / (1024*1024):.1f} MB. Please upload a smaller file.")
                uploaded_contract = None
            else:
                st.write(f"**Filename:** {uploaded_contract.name}")
                st.write(f"**Size:** {uploaded_contract.size / 1024:.1f} KB")
            
            if uploaded_contract and st.button("📤 Upload & Sync Contract", type="primary"):
                # Record upload attempt for rate limiting BEFORE processing
                record_upload_attempt()
                
                # Audit log
                logger.info(f"Contract upload initiated - File: {uploaded_contract.name}, Size: {uploaded_contract.size}")
                
                with st.spinner("Uploading contract..."):
                    upload_result = processor.upload_contract_to_s3(
                        uploaded_contract.getvalue(),
                        uploaded_contract.name
                    )
                    
                    if upload_result["success"]:
                        st.success("✅ Contract uploaded!")
                        
                        with st.spinner("Syncing Knowledge Base..."):
                            sync_result = processor.sync_knowledge_base()
                            
                            if sync_result["success"]:
                                st.success(f"✅ Sync started! Job ID: {sync_result['job_id']}")
                                st.info("Contract will be available in ~2-5 minutes")
                                st.rerun()
                            else:
                                st.error(f"❌ Sync failed: {sync_result['error']}")
                    else:
                        st.error(f"❌ Upload failed: {upload_result['error']}")
    
    with col2:
        st.subheader("📋 Existing Contracts")
        
        if st.button("🔄 Refresh List"):
            st.rerun()
        
        contracts = processor.list_contracts()
        
        if contracts:
            st.write(f"**Total Contracts:** {len(contracts)}")
            
            for contract in contracts:
                with st.expander(f"📄 {contract['name']}"):
                    st.write(f"**Size:** {contract['size'] / 1024:.1f} KB")
                    st.write(f"**Last Modified:** {contract['last_modified'].strftime('%Y-%m-%d %H:%M:%S')}")
                    st.write(f"**S3 Key:** `{contract['key']}`")
                    
                    col_a, col_b = st.columns(2)
                    
                    with col_a:
                        if st.button("🔄 Resync", key=f"resync_{contract['key']}"):
                            with st.spinner("Syncing Knowledge Base..."):
                                sync_result = processor.sync_knowledge_base()
                                
                                if sync_result["success"]:
                                    st.success(f"✅ Sync started! Job: {sync_result['job_id']}")
                                else:
                                    st.error(f"❌ Failed: {sync_result['error']}")
                    
                    with col_b:
                        if st.button("🗑️ Delete", key=f"delete_{contract['key']}"):
                            delete_result = processor.delete_contract(contract['key'])
                            
                            if delete_result["success"]:
                                st.success("✅ Contract deleted!")
                                st.rerun()
                            else:
                                st.error(f"❌ Delete failed: {delete_result['error']}")
        else:
            st.info("No contracts uploaded yet. Upload your first contract to get started!")
            st.markdown("""
            **Getting Started:**
            1. Upload a vendor contract PDF
            2. System will extract terms and create embeddings
            3. Use the knowledge base to validate invoices
            """)

# Tab 2: Process Invoice
with tab2:
    st.header("📤 Upload and Process Invoice")
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        uploaded_file = st.file_uploader(
            "Choose an invoice PDF",
            type=['pdf'],
            help="Upload PDF invoice for processing",
            key="invoice_pdf_uploader"
        )
        
        if uploaded_file is not None:
            # Check rate limit FIRST to prevent bypass attacks
            if not check_upload_rate_limit():
                logger.warning(f"Rate limit exceeded - Invoice upload blocked")
                st.error(f"Rate limit exceeded. Maximum {MAX_UPLOADS_PER_HOUR} uploads per hour allowed.")
                uploaded_file = None
            # Then check file size limit
            elif uploaded_file.size > MAX_FILE_SIZE:
                st.error(f"File size exceeds limit of {MAX_FILE_SIZE / (1024*1024):.1f} MB. Please upload a smaller file.")
                uploaded_file = None
            else:
                st.subheader("📄 File Details")
                st.write(f"**Filename:** {uploaded_file.name}")
                st.write(f"**Size:** {uploaded_file.size / 1024:.1f} KB")
            
            if uploaded_file and st.button("🚀 Process Invoice", type="primary"):
                if not processor.check_knowledge_base_status():
                    st.error("❌ Knowledge Base not configured")
                    st.stop()
                
                if processor.check_knowledge_base_status():
                    with st.spinner("Processing invoice..."):
                        # Record upload attempt for rate limiting BEFORE processing
                        record_upload_attempt()
                        
                        # Audit log
                        logger.info(f"Invoice processing initiated - File: {uploaded_file.name}, Size: {uploaded_file.size}")
                        
                        start_time = time.time()
                        
                        # Upload to S3
                        upload_result = processor.upload_to_s3(uploaded_file.getvalue(), uploaded_file.name)
                        
                        if upload_result["success"]:
                            # Extract invoice data
                            invoice_data = processor.extract_invoice_data(uploaded_file.getvalue())
                            
                            if "error" not in invoice_data:
                                # Validate against contract
                                validation_results = processor.validate_against_contract(invoice_data)
                                recommendation, reason = processor.determine_recommendation(invoice_data, validation_results)
                                
                                processing_time = time.time() - start_time
                                
                                # Store results
                                result = {
                                    "filename": uploaded_file.name,
                                    "processed_at": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
                                    "processing_time": processing_time,
                                    "vendor_name": invoice_data.get('vendor', {}).get('name', 'Unknown'),
                                    "invoice_number": invoice_data.get('invoice', {}).get('number', 'Unknown'),
                                    "invoice_date": invoice_data.get('invoice', {}).get('date', 'Unknown'),
                                    "total_amount": f"${invoice_data.get('totals', {}).get('total', 0):,.2f}",
                                    "tax_id": invoice_data.get('vendor', {}).get('tax_id', 'Unknown'),
                                    "po_number": invoice_data.get('invoice', {}).get('po_number', 'Unknown'),
                                    "vendor_approved": "✅" if validation_results["vendor_approved"] else "❌",
                                    "amount_within_limits": "✅" if validation_results["amount_within_limits"] else "❌",
                                    "payment_terms_match": "✅" if validation_results["payment_terms_match"] else "❌",
                                    "rates_approved": "✅" if validation_results["rates_approved"] else "❌",
                                    "compliance_score": f"{validation_results['compliance_score']}/100",
                                    "overall_compliance": "✅" if validation_results["overall_compliance"] else "❌",
                                    "recommendation": recommendation,
                                    "reason": reason,
                                    "issues": validation_results["issues"],
                                    "warnings": validation_results["warnings"],
                                    "contract_matches": validation_results.get("contract_matches", []),
                                    "detailed_analysis": validation_results.get("detailed_analysis", ""),
                                    "s3_location": f"s3://{upload_result['bucket']}/{upload_result['key']}"
                                }
                                
                                st.session_state.processing_results.append(result)
                                
                                # Display results in col2
                                with col2:
                                    st.success("✅ Processing completed!")
                                    st.metric("Processing Time", f"{processing_time:.1f}s")
                                    st.metric("Recommendation", recommendation)
                                    
                                    if validation_results["issues"]:
                                        st.warning("⚠️ Issues Found:")
                                        for issue in validation_results["issues"]:
                                            # Escape $ to prevent LaTeX rendering in Streamlit
                                            formatted_issue = str(issue).replace("$", "\\$")
                                            st.write(f"• {formatted_issue}")
                                    
                                    st.success("📊 Results saved! Switch to 'Results Dashboard' tab to view all processed invoices.")
                            else:
                                st.error(f"❌ Extraction failed: {invoice_data.get('error', 'Unknown error')}")
                        else:
                            st.error(f"❌ Upload failed: {upload_result['error']}")


# Tab 3: Test Vector Search
with tab3:
    st.header("🔍 Test Knowledge Base Search")
    
    if not processor.check_knowledge_base_status():
        st.warning("⚠️ Knowledge Base not configured")
    else:
        st.success("✅ Knowledge Base connected")
        
        search_query = st.text_input("Enter search query:", value="payment terms net 30")
        
        if st.button("🔍 Search"):
            if search_query:
                with st.spinner("Searching..."):
                    results = processor.search_contract_knowledge(search_query)
                    
                    if results:
                        st.subheader(f"📊 Found {len(results)} results:")
                        
                        for i, result in enumerate(results):
                            with st.expander(f"Result {i+1} (Score: {result['similarity']:.3f})"):
                                st.write(f"**Source:** {result['source']}")
                                st.text_area("Content", result['content'], height=150, key=f"content_{i}", label_visibility="collapsed")
                    else:
                        st.info("No results found")

# Tab 4: Results Dashboard
with tab4:
    st.header("📊 Invoice Processing Results Dashboard")
    
    if not st.session_state.processing_results:
        st.info("No processing results yet. Process some invoices to see results here.")
        
        # Load sample results for demo
        if st.button("📋 Load Sample Results"):
            sample_results = [
                {
                    "filename": "TechCorp Simple Invoice",
                    "processed_at": "2024-12-18 14:30:15",
                    "processing_time": 2.3,
                    "vendor_name": "TechCorp Solutions Inc",
                    "invoice_number": "INV-2024-1215",
                    "invoice_date": "2024-12-15",
                    "total_amount": "$20,658.17",
                    "tax_id": "91-1234567",
                    "po_number": "PO-GT-2024-0892",
                    "vendor_approved": "✅",
                    "amount_within_limits": "✅",
                    "payment_terms_match": "✅",
                    "rates_approved": "✅",
                    "compliance_score": "95/100",
                    "overall_compliance": "✅",
                    "recommendation": "AUTO APPROVE",
                    "reason": "Full contract compliance achieved (Score: 95/100)",
                    "issues": [],
                    "warnings": []
                },
                {
                    "filename": "DataFlow Complex Invoice",
                    "processed_at": "2024-12-18 14:32:45", 
                    "processing_time": 4.7,
                    "vendor_name": "DataFlow Systems Corporation",
                    "invoice_number": "INV-2024-3847",
                    "invoice_date": "2024-12-18",
                    "total_amount": "$48,314.74",
                    "tax_id": "74-9876543",
                    "po_number": "PO-GT-2024-1156",
                    "vendor_approved": "❌",
                    "amount_within_limits": "✅",
                    "payment_terms_match": "✅",
                    "rates_approved": "❌",
                    "compliance_score": "35/100",
                    "overall_compliance": "❌",
                    "recommendation": "REJECT",
                    "reason": "Vendor not authorized under MSA-2024-1201 - requires contract amendment",
                    "issues": ["Vendor 'DataFlow Systems Corporation' not authorized under MSA-2024-1201 - requires contract amendment", "ML Engineer rate $225/hr exceeds approved Senior Consultant rate ($185/hr)", "Data Scientist rate $195/hr exceeds approved Senior Consultant rate ($185/hr)", "DevOps Engineer rate $175/hr exceeds approved Project Management rate ($165/hr)"],
                    "warnings": []
                },
                {
                    "filename": "Innovate Solutions Invoice",
                    "processed_at": "2024-12-18 14:35:12",
                    "processing_time": 3.1,
                    "vendor_name": "Innovate Solutions LLC",
                    "invoice_number": "INV-2024-2847",
                    "invoice_date": "2024-12-17",
                    "total_amount": "$125,750.00",
                    "tax_id": "88-7654321",
                    "po_number": "PO-CONS-2024-1847",
                    "vendor_approved": "✅",
                    "amount_within_limits": "✅",
                    "payment_terms_match": "✅",
                    "rates_approved": "✅",
                    "compliance_score": "75/100",
                    "overall_compliance": "❌",
                    "recommendation": "MANUAL REVIEW",
                    "reason": "Requires approval workflow - High-value invoice $125,750.00 requires additional approval workflow",
                    "issues": [],
                    "warnings": ["High-value invoice $125,750.00 requires additional approval workflow", "Tax amount $10,750.00 may be incorrect (expected ~$11,003.13)"]
                }
            ]
            st.session_state.processing_results = sample_results
            st.rerun()
    
    else:
        # Display results
        total_results = len(st.session_state.processing_results)
        approved = len([r for r in st.session_state.processing_results if r["recommendation"] == "AUTO APPROVE"])
        rejected = len([r for r in st.session_state.processing_results if r["recommendation"] == "REJECT"])
        review = len([r for r in st.session_state.processing_results if r["recommendation"] == "MANUAL REVIEW"])
        
        # Summary metrics
        col1, col2, col3, col4 = st.columns(4)
        with col1:
            st.metric("Total Processed", total_results)
        with col2:
            st.metric("Auto Approved", approved)
        with col3:
            st.metric("Manual Review", review)
        with col4:
            st.metric("Rejected", rejected)
        
        # Results table
        st.subheader("📋 Processing Results")
        
        df = pd.DataFrame(st.session_state.processing_results)
        
        # Style the dataframe
        def style_recommendation(val):
            if val == "AUTO APPROVE":
                return "background-color: #d4edda; color: #155724"
            elif val == "REJECT":
                return "background-color: #f8d7da; color: #721c24"
            elif val == "MANUAL REVIEW":
                return "background-color: #fff3cd; color: #856404"
            return ""
        
        # Display columns
        display_columns = [
            "filename", "vendor_name", "invoice_number", "total_amount", "po_number",
            "vendor_approved", "amount_within_limits", "payment_terms_match", "rates_approved",
            "compliance_score", "overall_compliance", "recommendation", "reason", "processed_at"
        ]
        
        available_columns = [col for col in display_columns if col in df.columns]
        df_display = df[available_columns]
        
        styled_df = df_display.style.map(
            style_recommendation, subset=["recommendation"]
        )
        
        st.dataframe(styled_df, width="stretch")
        
        # Detailed issues and warnings view
        st.subheader("🔍 Detailed Analysis")
        
        for idx, result in enumerate(st.session_state.processing_results):
            # Show all results, with different styling based on recommendation
            recommendation_emoji = "✅" if result['recommendation'] == "AUTO APPROVE" else "❌" if result['recommendation'] == "REJECT" else "⚠️"
            
            with st.expander(f"{recommendation_emoji} {result['filename']} - {result['recommendation']}"):
                col1, col2 = st.columns(2)
                
                with col1:
                    st.write(f"**Vendor:** {result['vendor_name']}")
                    st.write(f"**Invoice #:** {result['invoice_number']}")
                    st.write(f"**Amount:** {result['total_amount']}")
                    st.write(f"**PO Number:** {result.get('po_number', 'N/A')}")
                    st.write(f"**Compliance Score:** {result.get('compliance_score', 'N/A')}")
                
                with col2:
                    # Show recommendation with color coding
                    if result['recommendation'] == "AUTO APPROVE":
                        st.success(f"**✅ {result['recommendation']}**")
                    elif result['recommendation'] == "REJECT":
                        st.error(f"**❌ {result['recommendation']}**")
                    else:
                        st.warning(f"**⚠️ {result['recommendation']}**")
                    
                    st.write(f"**Reason:** {result['reason']}")
                
                # Show LLM detailed analysis
                if result.get("detailed_analysis"):
                    st.write("**🤖 AI Analysis:**")
                    st.text_area("", result["detailed_analysis"], height=100, key=f"analysis_{idx}", label_visibility="collapsed")
                
                # Show contract matches
                if result.get("contract_matches"):
                    st.write("**📋 Contract References:**")
                    for match in result["contract_matches"]:
                        st.write(f"• {match}")
                
                # Show issues and warnings if any
                if result.get("issues"):
                    st.write("**❌ Contract Violations:**")
                    for issue in result["issues"]:
                        st.write(f"• {str(issue).replace('$', chr(92) + '$')}")
                
                if result.get("warnings"):
                    st.write("**⚠️ Warnings:**")
                    for warning in result["warnings"]:
                        st.write(f"• {str(warning).replace('$', chr(92) + '$')}")
                
                # Show validation details
                st.write("**Validation Summary:**")
                validation_cols = st.columns(4)
                with validation_cols[0]:
                    st.write(f"Vendor: {result.get('vendor_approved', 'N/A')}")
                with validation_cols[1]:
                    st.write(f"Amount: {result.get('amount_within_limits', 'N/A')}")
                with validation_cols[2]:
                    st.write(f"Terms: {result.get('payment_terms_match', 'N/A')}")
                with validation_cols[3]:
                    st.write(f"Rates: {result.get('rates_approved', 'N/A')}")
        
        # Export
        if st.button("📄 Export Results"):
            csv = df_display.to_csv(index=False)
            st.download_button(
                "Download CSV",
                csv,
                f"invoice_results_{datetime.now().strftime('%Y%m%d_%H%M%S')}.csv",
                "text/csv"
            )

def main():
    """Main function to run the app - called when imported by secure_app."""
    pass  # All the UI code above runs on module import

# Footer
st.markdown("---")
st.markdown("**Built with Amazon Bedrock + Claude sonnet**")

if __name__ == "__main__":
    main()
