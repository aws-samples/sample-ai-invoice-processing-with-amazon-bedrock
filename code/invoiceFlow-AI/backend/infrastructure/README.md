# InvoiceFlow AI - Infrastructure Deployment

## Overview

This infrastructure deploys the InvoiceFlow AI backend services including S3 storage, Bedrock Knowledge Base, Cognito authentication, and IAM roles for secure local application access.

## Architecture

```
Local Streamlit App → AWS Services
    ├── S3 Document Storage (invoiceflow-ai-bucket-ACCOUNT_ID)
    ├── S3 Vectors Storage (invoiceflow-ai-vectors-ACCOUNT_ID)
    ├── Bedrock Knowledge Base (S3 Vectors)
    ├── Bedrock Claude Sonnet 4
    └── Cognito User Pool
```

## Components

1. **Amazon S3**: Document storage with account-specific bucket naming
2. **Bedrock Knowledge Base**: S3 Vectors for contract storage and search
3. **Amazon Cognito**: User authentication and authorization
4. **IAM Roles**: Deployment and application roles with least privilege

## Deployment Steps

### Prerequisites
- AWS CLI configured
- Python 3.10+
- Bedrock service access in us-east-1

### 1. Create Deployment Role (Recommended)

```bash
cd code/invoiceFlow-AI/backend/infrastructure
./create_deployment_role.sh
```

This creates:
- IAM role with deployment permissions
- Trust policy with external ID for security
- Returns role ARN for use in deployment

### 2. Deploy Infrastructure

```bash
# Set deployment role ARN (from step 1 output)
export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT_ID:role/InvoiceFlowDeploymentRole'

# Deploy all infrastructure
python cognito_deployment.py
```

This creates:
- S3 buckets for documents and vectors (with account ID suffix)
- Bedrock Knowledge Base with S3 Vectors storage
- Cognito User Pool with default user
- IAM application role for Streamlit app
- All necessary IAM policies with least privilege

### 3. Run Application

```bash
cd ../
export APP_ROLE_ARN='arn:aws:iam::ACCOUNT_ID:role/invoiceflow-ai-app-role'
streamlit run simplified_app.py
```

Access at: `http://localhost:8501`

## Default User

**Email**: admin@invoiceflow.ai  
**Temporary Password**: TempPass123!

⚠️ Password must be changed on first login through Cognito interface.

## Configuration Files

### infrastructure_outputs.json

Generated after deployment, contains:
```json
{
  "S3BucketName": "invoiceflow-ai-bucket-EXAMPLE123",
  "VectorsBucketName": "invoiceflow-ai-vectors-EXAMPLE123",
  "KnowledgeBaseId": "YOUR-KNOWLEDGE-BASE-ID-HERE",
  "DataSourceId": "YOUR-DATA-SOURCE-ID-HERE",
  "CognitoUserPoolId": "us-east-1_EXAMPLE123",
  "CognitoClientId": "your-cognito-client-id-here",
  "AppRoleArn": "arn:aws:iam::123456789012:role/invoiceflow-ai-app-role"
}
```

## Security Configuration

### Authentication
- Default user is created with secure temporary password (configurable via environment variable)
- Password policy enforces 12-character minimum with alphanumeric and symbol requirements
- **MFA is not enabled by default but can be enabled by users if required for additional security**

### IAM Policies
- Least privilege principles applied where possible
- Specific resource permissions rather than broad wildcards

- ✅ IAM roles with least privilege permissions
- ✅ External ID for role assumption security
- ✅ S3 buckets with server-side encryption
- ✅ Private S3 buckets (no public access)
- ✅ Cognito authentication with password complexity
- ✅ Cross-region Bedrock inference access
- ✅ Account-specific resource naming

## IAM Roles

### Deployment Role
- **Purpose**: Deploy and manage AWS infrastructure
- **Permissions**: CloudFormation, S3, Bedrock, Cognito, IAM
- **External ID**: `invoiceflow-deployment`

### Application Role  
- **Purpose**: Runtime access for Streamlit application
- **Permissions**: S3 read/write, Bedrock inference, Knowledge Base access
- **External ID**: `invoiceflow-app`

## Environment Variables

The application uses these environment variables:

```bash
# AWS Configuration
AWS_REGION=us-east-1
S3_BUCKET=invoiceflow-ai-bucket-ACCOUNT_ID

# Bedrock Configuration
BEDROCK_MODEL_ID=us.anthropic.claude-sonnet-4-20250514-v1:0
EMBEDDINGS_MODEL=amazon.titan-embed-text-v1

# Knowledge Base (auto-populated from deployment)
KNOWLEDGE_BASE_ID=auto-generated
DATA_SOURCE_ID=auto-generated

# IAM Role for application
APP_ROLE_ARN=arn:aws:iam::ACCOUNT_ID:role/invoiceflow-ai-app-role
```

## Troubleshooting

### Deployment Issues

```bash
# Check deployment role assumption
aws sts get-caller-identity

# Verify Bedrock service access
aws bedrock list-foundation-models --region us-east-1

# Check CloudFormation stack
aws cloudformation describe-stacks --stack-name invoiceflow-ai-stack
```

### Application Issues

```bash
# Test S3 access
aws s3 ls s3://invoiceflow-ai-bucket-ACCOUNT_ID/

# Check Knowledge Base
aws bedrock-agent list-knowledge-bases --region us-east-1

# Verify Cognito user pool
aws cognito-idp list-users --user-pool-id USER_POOL_ID
```

### Role Assumption Issues

```bash
# Test deployment role assumption
aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT_ID:role/InvoiceFlowDeploymentRole \
  --role-session-name test-session \
  --external-id invoiceflow-deployment

# Test application role assumption  
aws sts assume-role \
  --role-arn arn:aws:iam::ACCOUNT_ID:role/invoiceflow-ai-app-role \
  --role-session-name app-session \
  --external-id invoiceflow-app
```

## Cleanup

To remove all infrastructure:

```bash
# Set deployment role
export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT_ID:role/InvoiceFlowDeploymentRole'

# Delete CloudFormation stack
aws cloudformation delete-stack --stack-name invoiceflow-ai-stack

# Clean up S3 buckets (if needed)
aws s3 rm s3://invoiceflow-ai-bucket-ACCOUNT_ID/ --recursive
aws s3 rm s3://invoiceflow-ai-vectors-ACCOUNT_ID/ --recursive
aws s3 rb s3://invoiceflow-ai-bucket-ACCOUNT_ID/
aws s3 rb s3://invoiceflow-ai-vectors-ACCOUNT_ID/
```

## Cost Estimation

Monthly AWS costs (approximate):
- **Bedrock Claude Sonnet 4**: $0.003/1K input tokens, $0.015/1K output tokens
- **Bedrock Knowledge Base**: S3 Vectors storage and retrieval
- **S3 Storage**: $0.023/GB storage + $0.005/1K requests
- **Cognito**: Free tier: 50K MAUs, then $0.0055/MAU

**Total**: $22-45/month for typical usage (500 invoices/month)

## Additional Configuration

### Adding More Users

```bash
# Create additional Cognito user
aws cognito-idp admin-create-user \
  --user-pool-id USER_POOL_ID \
  --username user@example.com \
  --temporary-password TempPass123! \
  --message-action SUPPRESS
```

### Updating Knowledge Base

```bash
# Trigger data source sync after uploading new contracts
aws bedrock-agent start-ingestion-job \
  --knowledge-base-id KNOWLEDGE_BASE_ID \
  --data-source-id DATA_SOURCE_ID
```

## Support

For issues or questions:
1. Check application logs in Streamlit interface
2. Review AWS CloudWatch logs
3. Verify IAM role permissions
4. Check Bedrock service availability
5. Consult the main [DEPLOYMENT_GUIDE.md](../DEPLOYMENT_GUIDE.md)

---

**Built with Amazon Bedrock and Claude Sonnet 4**