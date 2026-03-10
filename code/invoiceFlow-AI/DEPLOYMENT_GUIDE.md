# InvoiceFlow AI - Deployment Guide

## Overview

This guide will help you deploy InvoiceFlow AI to your AWS account. The deployment is **fully automated** via Python script. The system consists of:
- Amazon Bedrock Knowledge Base with S3 Vectors for contract storage (auto-created)
- S3 bucket for document storage (auto-created)
- Cognito authentication (auto-created)
- Streamlit web application with HTTPS (runs locally)

## Prerequisites

- AWS Account
- AWS CLI configured with credentials
- Python 3.10+
- Git

### IAM Permissions Setup

The deployment uses automated IAM role creation with least privilege permissions. Two options are available:

#### Option 1: Automated Role Creation (Recommended)

```bash
cd code/invoiceFlow-AI/backend/infrastructure
./create_deployment_role.sh
```

This script creates:
- IAM policy with deployment permissions
- IAM role with proper trust relationships
- Outputs role ARN for deployment

Follow the script output to export the role ARN:
```bash
export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT_ID:role/InvoiceFlowDeploymentRole'
```

#### Option 2: Manual IAM User Setup

If you prefer using an IAM user instead of a role:

1. Create IAM user: `invoiceflow-deployer`
2. Attach the deployment policy (created by setup script)
3. Generate access keys
4. Configure AWS CLI profile

```bash
aws configure --profile invoiceflow
export AWS_PROFILE=invoiceflow
```

## Quick Start Deployment

### 1. Clone Repository

```bash
git clone https://github.com/aws-samples/invoiceflow-ai
cd invoiceflow-ai
```

### 2. Create Deployment Role (Automated)

```bash
cd code/invoiceFlow-AI/backend/infrastructure
./create_deployment_role.sh
```

Follow the script output to export the role ARN:
```bash
export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT_ID:role/InvoiceFlowDeploymentRole'
```

### 3. Setup Python Environment

```bash
cd code/invoiceFlow-AI/backend
python -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Deploy Infrastructure (Single Command)

```bash
cd infrastructure
python cognito_deployment.py
```

This single script automatically deploys everything:
- **S3 bucket** for document storage (with encryption and public access blocks)
- **S3 vectors bucket** for Knowledge Base vector storage
- **Cognito User Pool** for authentication
- Default user: `admin@invoiceflow.ai` / `TempPass123!`
- **Bedrock Knowledge Base** with S3 Vectors storage
- **IAM roles and policies** with least privilege
- **Data source** connected to S3

The script outputs all resource IDs and saves them to `infrastructure_outputs.json`.

### 4. Run Application with HTTPS

```bash
cd ..
python start_app.py
```

The application launcher will:
- Kill any existing processes on port 8501
- Generate self-signed SSL certificates (first run only)
- Start Streamlit with HTTPS on port 8501

**Access the application at: `https://localhost:8501`**

#### Expected Browser Security Warning

When you first access the application, Chrome will show a security warning:

```
Your connection is not private
Attackers might be trying to steal your information from localhost
NET::ERR_CERT_AUTHORITY_INVALID
```

**This is normal and safe for local development.** To proceed:

1. Click **"Advanced"**
2. Click **"Proceed to localhost (unsafe)"**
3. Your application will load with HTTPS

#### Optional: Add Certificate to System Trust Store (macOS)

To eliminate the browser warning permanently:

```bash
# Add the certificate to macOS keychain (run from backend directory)
sudo security add-trusted-cert -d -r trustRoot -k /Library/Keychains/System.keychain ssl/cert.pem
```

After adding the certificate, restart your browser and the security warning will no longer appear.

## Using the Application

### 1. Upload Contracts (Knowledge Base)

1. Navigate to the **"Knowledge Base"** tab
2. Click **"Upload New Contract"**
3. Select your vendor contract PDF
4. Click **"Upload & Process Contract"**
5. System will upload to S3: `s3://invoiceflow-ai-bucket/knowledge-base/contracts/`

### 2. Sync Knowledge Base

After uploading contracts, the app automatically syncs the Knowledge Base when you click "Upload & Sync Contract".

You can also manually sync via CLI:
```bash
aws bedrock-agent start-ingestion-job \
  --knowledge-base-id $KNOWLEDGE_BASE_ID \
  --data-source-id $DATA_SOURCE_ID
```

### 3. Process Invoices

1. Navigate to the **"Process Invoice"** tab
2. Upload an invoice PDF
3. System will:
   - Extract invoice data using Claude Sonnet 4
   - Search knowledge base for relevant contracts
   - Validate against contract terms
   - Generate approval recommendation

### 4. View Results

Navigate to the **"Results Dashboard"** tab to see:
- Processing history
- Approval recommendations
- Contract matches
- Detailed validation results

## Knowledge Base Management

### Upload New Contract

Contracts are uploaded through the UI:
1. Go to "Knowledge Base" tab
2. Upload PDF file
3. System automatically processes and creates embeddings

### Replace Existing Contract

To update a contract:
1. Delete the old contract
2. Upload the new version
3. System will reprocess automatically

### Delete Contract

1. Find contract in "Existing Contracts" list
2. Click "Delete" button
3. Both contract and vector embeddings are removed

## Configuration

The application automatically reads configuration from the deployment outputs. No manual environment variable setup is required.

Configuration is managed through:
- **Deployment outputs**: `infrastructure_outputs.json` (auto-generated)
- **Environment variables**: Optional overrides for advanced users
- **Application defaults**: Built-in fallback values

### Optional Environment Variable Overrides

```bash
export AWS_REGION="us-east-1"
export BEDROCK_MODEL_ID="us.anthropic.claude-sonnet-4-20250514-v1:0"
export EMBEDDINGS_MODEL="amazon.titan-embed-text-v2:0"
```

The application reads these with sensible defaults from `simplified_app.py`.

## Troubleshooting

### S3 Bucket Already Exists

If bucket name is taken:
1. Change `S3_BUCKET` in `simplified_app.py`
2. Update S3 URI in Knowledge Base data source

### Bedrock Access Denied

Ensure you have:
1. Bedrock service access in your region
2. Model access enabled: Claude Sonnet 4 + Titan Embeddings v2
3. IAM permissions: `bedrock:InvokeModel`, `bedrock-agent-runtime:Retrieve`

### Knowledge Base Creation Fails

The deployment script creates Knowledge Base with S3 Vectors for managed vector storage.

**If deployment fails:**
- Ensure you have `bedrock:CreateKnowledgeBase` permission
- Check IAM role has S3 and Bedrock model access
- Verify region is `us-east-1`
- Re-run `cognito_deployment.py` - it's idempotent

### Contract Upload Fails

Check:
1. S3 bucket exists: `aws s3 ls s3://invoiceflow-ai-bucket/`
2. IAM permissions for S3 write
3. PDF file is valid and not corrupted

### Knowledge Base Returns No Results

1. Verify contracts uploaded to: `s3://invoiceflow-ai-bucket/knowledge-base/contracts/`
2. Sync the data source (see "Sync Knowledge Base" section)
3. Check sync status: Should be "AVAILABLE" not "SYNCING" or "FAILED"
4. Verify Knowledge Base ID is correct in `simplified_app.py`

## Production Deployment

For production, deploy Streamlit app to:
- **AWS ECS Fargate** (recommended)
- **AWS EC2** with Auto Scaling
- **AWS App Runner**

Current setup runs locally for development/testing.

## Cost Estimation

Monthly costs (approximate):
- **S3**: $1-5 (storage + requests)
- **Bedrock Knowledge Base**: $10-20 (S3 Vectors storage)
- **Bedrock Claude Sonnet 4**: $15-50 (based on usage)
- **Bedrock Titan Embeddings**: $1-5 (embedding generation)
- **Cognito**: Free tier (50K MAUs)

**Total**: $25-80/month for typical usage (100-500 invoices/month)

## Security Best Practices

1. **Change default password** immediately after first login
2. **Enable MFA** in Cognito User Pool
3. **Restrict S3 bucket** access to application only
4. **Use VPC endpoints** for Bedrock in production
5. **Enable CloudTrail** for audit logging
6. **Rotate credentials** regularly

## Cleanup

To remove all resources:

```bash
# Get account ID and resource IDs
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
KB_ID=$(jq -r '.knowledge_base_id' infrastructure_outputs.json)

# 1. Delete Knowledge Base and Data Source
aws bedrock-agent delete-knowledge-base --knowledge-base-id $KB_ID

# 2. Delete CloudFormation stack
aws cloudformation delete-stack --stack-name invoiceflow-ai-stack

# 3. Empty and delete S3 buckets
aws s3 rm s3://invoiceflow-ai-bucket-${ACCOUNT_ID}/ --recursive
aws s3 rb s3://invoiceflow-ai-bucket-${ACCOUNT_ID}/
aws s3 rm s3://invoiceflow-ai-vectors-${ACCOUNT_ID}/ --recursive  
aws s3 rb s3://invoiceflow-ai-vectors-${ACCOUNT_ID}/

# 4. Delete IAM roles (if created by deployment script)
aws iam delete-role-policy --role-name invoiceflow-ai-kb-role --policy-name S3DataSourceAccess
aws iam delete-role-policy --role-name invoiceflow-ai-kb-role --policy-name BedrockModelAccess
aws iam delete-role --role-name invoiceflow-ai-kb-role

aws iam delete-role-policy --role-name invoiceflow-ai-app-role --policy-name AppUserPolicy
aws iam delete-role --role-name invoiceflow-ai-app-role
```

## Support

For issues:
1. Check CloudWatch logs
2. Verify AWS credentials
3. Review IAM permissions
4. Check Bedrock model access

## Next Steps

1. Upload your vendor contracts
2. Process sample invoices
3. Review validation results
4. Customize contract validation rules
5. Add more contracts to knowledge base
