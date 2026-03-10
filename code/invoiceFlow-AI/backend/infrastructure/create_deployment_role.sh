#!/bin/bash

# InvoiceFlow AI - Automated Deployment Role Creation
# This script creates the IAM role required for deploying InvoiceFlow AI infrastructure

set -e  # Exit on any error

echo "🚀 InvoiceFlow AI - Deployment Role Setup"
echo "========================================"
echo

# Check if AWS CLI is installed and configured
if ! command -v aws &> /dev/null; then
    echo "❌ AWS CLI is not installed. Please install it first."
    echo "   https://docs.aws.amazon.com/cli/latest/userguide/getting-started-install.html"
    exit 1
fi

# Test AWS credentials
echo "🔍 Checking AWS credentials..."
if ! aws sts get-caller-identity &> /dev/null; then
    echo "❌ AWS credentials not configured or invalid."
    echo "   Please run: aws configure"
    exit 1
fi

# Get account information
ACCOUNT_ID=$(aws sts get-caller-identity --query Account --output text)
CURRENT_USER=$(aws sts get-caller-identity --query Arn --output text)
echo "✅ AWS credentials found"
echo "   Account: $ACCOUNT_ID"
echo "   User/Role: $CURRENT_USER"
echo

# Define role and policy names
ROLE_NAME="InvoiceFlowDeploymentRole"
POLICY_NAME="InvoiceFlowDeploymentPolicy"
ROLE_ARN="arn:aws:iam::${ACCOUNT_ID}:role/${ROLE_NAME}"
POLICY_ARN="arn:aws:iam::${ACCOUNT_ID}:policy/${POLICY_NAME}"

# Create trust policy for the role
echo "📝 Creating trust policy..."
cat > trust-policy.json << EOF
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Allow",
      "Principal": {
        "AWS": "arn:aws:iam::${ACCOUNT_ID}:root"
      },
      "Action": "sts:AssumeRole",
      "Condition": {
        "StringEquals": {
          "sts:ExternalId": "invoiceflow-deployment"
        }
      }
    }
  ]
}
EOF

# Create inline policy for the role
echo "🔐 Creating inline policy..."

# Create the IAM role if it doesn't exist
echo "👤 Creating IAM role..."
if aws iam get-role --role-name "$ROLE_NAME" &> /dev/null; then
    echo "ℹ️  Role $ROLE_NAME already exists"
else
    aws iam create-role \
        --role-name "$ROLE_NAME" \
        --assume-role-policy-document file://trust-policy.json \
        --description "Deployment role for InvoiceFlow AI"
    echo "✅ Created role: $ROLE_NAME"
fi

# Attach inline policy to role (substitute account and region placeholders)
echo "🔗 Attaching inline policy to role..."
REGION="${AWS_REGION:-us-east-1}"
sed -e "s/\${AWS::AccountId}/${ACCOUNT_ID}/g" -e "s/\${AWS::Region}/${REGION}/g" deployment-policy.json > /tmp/deployment-policy-resolved.json
aws iam put-role-policy \
    --role-name "$ROLE_NAME" \
    --policy-name "$POLICY_NAME" \
    --policy-document file:///tmp/deployment-policy-resolved.json
rm -f /tmp/deployment-policy-resolved.json
echo "✅ Inline policy attached to role"

# Clean up temporary files
rm -f trust-policy.json

echo
echo "🎉 Deployment role setup completed!"
echo "=================================="
echo
echo "Role ARN: $ROLE_ARN"
echo
echo "Next steps:"
echo "1. Export the role ARN:"
echo "   export DEPLOYMENT_ROLE_ARN='$ROLE_ARN'"
echo
echo "2. Run the deployment:"
echo "   python cognito_deployment.py"
echo
echo "Note: The role uses an external ID 'invoiceflow-deployment' for additional security."