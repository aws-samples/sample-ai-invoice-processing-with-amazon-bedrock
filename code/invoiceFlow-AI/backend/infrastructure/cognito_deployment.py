#!/usr/bin/env python3
"""
Cognito + Bedrock Knowledge Base Infrastructure Setup for InvoiceFlow AI
"""

import boto3
import json
import time
import os
import logging
from datetime import datetime
from botocore.exceptions import ClientError, NoCredentialsError

# Configure logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

AWS_REGION = "us-east-1"
APP_NAME = "invoiceflow-ai"
STACK_NAME = f"{APP_NAME}-stack"

def get_session_with_role():
    """Assume IAM role if DEPLOYMENT_ROLE_ARN is set, otherwise use default credentials."""
    role_arn = os.getenv('DEPLOYMENT_ROLE_ARN')
    
    if role_arn:
        print(f"🔐 Assuming role: {role_arn}")
        
        try:
            # Create STS client with secure configuration
            from botocore.config import Config
            sts_config = Config(
                retries={'max_attempts': 3, 'mode': 'adaptive'},
                signature_version='v4'
            )
            
            sts_client = boto3.client('sts', config=sts_config)
            
            response = sts_client.assume_role(
                RoleArn=role_arn,
                RoleSessionName='invoiceflow-deployment',
                ExternalId='invoiceflow-deployment',
                DurationSeconds=3600
            )
            
            credentials = response['Credentials']
            print(f"✅ Successfully assumed role")
            
            return boto3.Session(
                aws_access_key_id=credentials['AccessKeyId'],
                aws_secret_access_key=credentials['SecretAccessKey'],
                aws_session_token=credentials['SessionToken']
            )
            
        except ClientError as e:
            error_code = e.response['Error']['Code']
            error_message = e.response['Error']['Message']
            
            if error_code == 'AccessDenied':
                print(f"❌ Access denied when assuming role {role_arn}")
                print("   Check if the role exists and you have permission to assume it")
            elif error_code == 'InvalidParameterValue':
                print(f"❌ Invalid parameter when assuming role: {error_message}")
            else:
                print(f"❌ Error assuming role: {error_code} - {error_message}")
            
            print("❌ Role assumption failed")
            print("   Please set DEPLOYMENT_ROLE_ARN environment variable:")
            print("   export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT:role/ROLE_NAME'")
            raise SystemExit(1)
            
        except NoCredentialsError:
            print("❌ No AWS credentials found")
            print("   Please configure AWS credentials using one of:")
            print("   • AWS CLI: aws configure")
            print("   • Environment variables: AWS_ACCESS_KEY_ID, AWS_SECRET_ACCESS_KEY")
            print("   • IAM role (if running on EC2)")
            print("   • AWS SSO: aws sso login")
            raise SystemExit(1)
            
        except Exception as e:
            print(f"❌ Unexpected error assuming role: {e}")
            print("   Please set DEPLOYMENT_ROLE_ARN environment variable:")
            print("   export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT:role/ROLE_NAME'")
            raise SystemExit(1)
    else:
        print("❌ DEPLOYMENT_ROLE_ARN environment variable is required")
        print("   Please set the deployment role ARN:")
        print("   export DEPLOYMENT_ROLE_ARN='arn:aws:iam::ACCOUNT:role/ROLE_NAME'")
        print()
        print("   The role should have permissions for:")
        print("   • CloudFormation operations")
        print("   • S3 bucket creation and management")
        print("   • Bedrock Knowledge Base operations")
        print("   • IAM role creation and policy attachment")
        raise SystemExit(1)

class InfrastructureDeployer:
    def __init__(self, region=AWS_REGION, session=None):
        self.region = region
        self.session = session or boto3.Session()
        self.cf_client = self.session.client('cloudformation', region_name=region)
        self.s3_client = self.session.client('s3', region_name=region)
        self.cognito_client = self.session.client('cognito-idp', region_name=region)
        self.cloudfront_client = self.session.client('cloudfront', region_name=region)
        self.bedrock_agent_client = self.session.client('bedrock-agent', region_name=region)
        self.bedrock_client = self.session.client('bedrock', region_name=region)
        self.iam_client = self.session.client('iam', region_name=region)
        
    def create_cloudformation_template(self):
        """Generate minimal CloudFormation template for non-production use."""
        template = {
            "AWSTemplateFormatVersion": "2010-09-09",
            "Description": "InvoiceFlow AI - Minimal Infrastructure for Non-Production Use",
            "Parameters": {
                "AppName": {
                    "Type": "String",
                    "Default": APP_NAME,
                    "Description": "Application name"
                }
            },
            "Resources": {
                
                # S3 Document Bucket
                "DocumentBucket": {
                    "Type": "AWS::S3::Bucket",
                    "Properties": {
                        "BucketName": {"Fn::Sub": "${AppName}-bucket-${AWS::AccountId}"},
                        "VersioningConfiguration": {
                            "Status": "Enabled"
                        },
                        "BucketEncryption": {
                            "ServerSideEncryptionConfiguration": [{
                                "ServerSideEncryptionByDefault": {
                                    "SSEAlgorithm": "AES256"
                                }
                            }]
                        },
                        "PublicAccessBlockConfiguration": {
                            "BlockPublicAcls": True,
                            "BlockPublicPolicy": True,
                            "IgnorePublicAcls": True,
                            "RestrictPublicBuckets": True
                        }
                    }
                },
                
                # S3 Bucket Policy - Enforce TLS
                "DocumentBucketPolicy": {
                    "Type": "AWS::S3::BucketPolicy",
                    "Properties": {
                        "Bucket": {"Ref": "DocumentBucket"},
                        "PolicyDocument": {
                            "Version": "2012-10-17",
                            "Statement": [{
                                "Sid": "EnforceTLS",
                                "Effect": "Deny",
                                "Principal": "*",
                                "Action": "s3:*",
                                "Resource": [
                                    {"Fn::GetAtt": ["DocumentBucket", "Arn"]},
                                    {"Fn::Sub": "${DocumentBucket.Arn}/*"}
                                ],
                                "Condition": {
                                    "Bool": {"aws:SecureTransport": "false"}
                                }
                            }]
                        }
                    }
                },
                
                # Cognito User Pool - Basic Configuration
                "CognitoUserPool": {
                    "Type": "AWS::Cognito::UserPool",
                    "Properties": {
                        "UserPoolName": {"Fn::Sub": "${AppName}-user-pool"},
                        "AdminCreateUserConfig": {
                            "AllowAdminCreateUserOnly": True
                        },
                        "AutoVerifiedAttributes": ["email"],
                        "UsernameAttributes": ["email"],
                        "Policies": {
                            "PasswordPolicy": {
                                "MinimumLength": 12,
                                "RequireUppercase": True,
                                "RequireLowercase": True,
                                "RequireNumbers": True,
                                "RequireSymbols": True
                            }
                        },
                        "Schema": [{
                            "Name": "email",
                            "Required": True,
                            "Mutable": False
                        }]
                    }
                },
                
                # Cognito User Pool Client - Basic Configuration
                "CognitoUserPoolClient": {
                    "Type": "AWS::Cognito::UserPoolClient",
                    "Properties": {
                        "ClientName": {"Fn::Sub": "${AppName}-client"},
                        "UserPoolId": {"Ref": "CognitoUserPool"},
                        "GenerateSecret": True,
                        "ExplicitAuthFlows": [
                            "ALLOW_USER_PASSWORD_AUTH",
                            "ALLOW_REFRESH_TOKEN_AUTH",
                            "ALLOW_USER_SRP_AUTH"
                        ]
                    }
                },
                
                # Cognito User Pool Domain
                "CognitoUserPoolDomain": {
                    "Type": "AWS::Cognito::UserPoolDomain",
                    "Properties": {
                        "Domain": {"Fn::Sub": "${AppName}-${AWS::AccountId}"},
                        "UserPoolId": {"Ref": "CognitoUserPool"}
                    }
                }
            },
            "Outputs": {
                "DocumentBucketName": {
                    "Description": "S3 Document Bucket Name",
                    "Value": {"Ref": "DocumentBucket"},
                    "Export": {"Name": {"Fn::Sub": "${AWS::StackName}-DocumentBucket"}}
                },
                "CognitoUserPoolId": {
                    "Description": "Cognito User Pool ID",
                    "Value": {"Ref": "CognitoUserPool"},
                    "Export": {"Name": {"Fn::Sub": "${AWS::StackName}-UserPoolId"}}
                },
                "CognitoClientId": {
                    "Description": "Cognito User Pool Client ID",
                    "Value": {"Ref": "CognitoUserPoolClient"},
                    "Export": {"Name": {"Fn::Sub": "${AWS::StackName}-ClientId"}}
                },
                "CognitoUserPoolDomain": {
                    "Description": "Cognito User Pool Domain",
                    "Value": {"Ref": "CognitoUserPoolDomain"},
                    "Export": {"Name": {"Fn::Sub": "${AWS::StackName}-UserPoolDomain"}}
                }
            }
        }
        return template
    
    def deploy_stack(self):
        """Deploy CloudFormation stack."""
        print(f"🚀 Deploying {STACK_NAME}...")
        
        template = self.create_cloudformation_template()
        template_json = json.dumps(template, indent=2)
        
        try:
            # Check if stack exists
            try:
                self.cf_client.describe_stacks(StackName=STACK_NAME)
                print(f"📝 Updating existing stack...")
                response = self.cf_client.update_stack(
                    StackName=STACK_NAME,
                    TemplateBody=template_json,
                    Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']
                )
                operation = "UPDATE"
            except self.cf_client.exceptions.ClientError as e:
                if 'does not exist' in str(e):
                    print(f"📝 Creating new stack...")
                    response = self.cf_client.create_stack(
                        StackName=STACK_NAME,
                        TemplateBody=template_json,
                        Capabilities=['CAPABILITY_IAM', 'CAPABILITY_NAMED_IAM']
                    )
                    operation = "CREATE"
                elif 'No updates are to be performed' in str(e):
                    print(f"ℹ️  Stack already up to date")
                    return self.get_stack_outputs()
                else:
                    raise
            
            print(f"⏳ Waiting for stack {operation} to complete...")
            waiter = self.cf_client.get_waiter(f'stack_{operation.lower()}_complete')
            waiter.wait(StackName=STACK_NAME)
            
            print(f"✅ Stack {operation} completed successfully!")
            return self.get_stack_outputs()
            
        except Exception as e:
            print(f"❌ Error deploying stack: {e}")
            raise
    
    def get_stack_outputs(self):
        """Get stack outputs."""
        response = self.cf_client.describe_stacks(StackName=STACK_NAME)
        outputs = {}
        
        if response['Stacks']:
            for output in response['Stacks'][0].get('Outputs', []):
                outputs[output['OutputKey']] = output['OutputValue']
        
        return outputs
    
    def create_default_user(self, user_pool_id, username="admin@invoiceflow.ai"):
        """Create default Cognito user. Cognito sends temporary password via email."""
        print(f"👤 Creating default user: {username}")
        
        try:
            response = self.cognito_client.admin_create_user(
                UserPoolId=user_pool_id,
                Username=username,
                UserAttributes=[
                    {'Name': 'email', 'Value': username},
                    {'Name': 'email_verified', 'Value': 'true'}
                ],
                DesiredDeliveryMediums=['EMAIL']
            )
            
            print(f"✅ Default user created successfully!")
            print(f"   Username: {username}")
            print(f"   📧 Temporary password sent to {username} via email")
            print(f"   ⚠️  User must change password on first login")
            
            return response
            
        except self.cognito_client.exceptions.UsernameExistsException:
            print(f"ℹ️  User {username} already exists")
        except Exception as e:
            print(f"❌ Error creating user: {e}")
            raise
    
    def create_bedrock_guardrail(self):
        """Create Bedrock Guardrail for responsible AI usage."""
        try:
            print("🛡️ Creating Bedrock Guardrail...")
            
            response = self.bedrock_client.create_guardrail(
                name=f"{APP_NAME}-guardrail",
                description="Guardrail for InvoiceFlow AI security",
                blockedInputMessaging="Request blocked for security reasons.",
                blockedOutputsMessaging="Response blocked for security reasons.",
                sensitiveInformationPolicyConfig={
                    'piiEntitiesConfig': [
                        {'type': 'EMAIL', 'action': 'ANONYMIZE'},
                        {'type': 'PHONE', 'action': 'ANONYMIZE'},
                        {'type': 'ADDRESS', 'action': 'ANONYMIZE'},
                        {'type': 'PASSWORD', 'action': 'BLOCK'}
                    ]
                },
                contentPolicyConfig={
                    'filtersConfig': [
                        {'type': 'PROMPT_ATTACK', 'inputStrength': 'HIGH', 'outputStrength': 'NONE'},
                        {'type': 'MISCONDUCT', 'inputStrength': 'MEDIUM', 'outputStrength': 'MEDIUM'}
                    ]
                }
            )
            
            print(f"✅ Guardrail created: {response['guardrailId']}")
            return {'guardrail_id': response['guardrailId'], 'guardrail_version': response['version']}
            
        except Exception as e:
            if "ConflictException" in str(type(e)) or "already has this name" in str(e):
                print(f"ℹ️  Guardrail already exists, looking up...")
                guardrails = self.bedrock_client.list_guardrails()
                for g in guardrails.get('guardrails', []):
                    if g['name'] == f"{APP_NAME}-guardrail":
                        print(f"✅ Found existing guardrail: {g['id']}")
                        return {'guardrail_id': g['id'], 'guardrail_version': 'DRAFT'}
            print(f"⚠️ Guardrail creation failed: {e}")
            return None
            
    def create_knowledge_base(self, bucket_name):
        """Create Bedrock Knowledge Base with S3 Vectors."""
        print("🧠 Creating Bedrock Knowledge Base with S3 Vectors...")
        
        account_id = self.session.client('sts').get_caller_identity()['Account']
        s3vectors_client = self.session.client('s3vectors', region_name=self.region)
        
        kb_name = f"{APP_NAME}-knowledge-base-{account_id}"
        vector_bucket_name = f"{APP_NAME}-vectors-{account_id}"
        index_name = f"{APP_NAME}-index"
        role_name = f"{APP_NAME}-kb-role"
        
        try:
            # Step 1: Create S3 Vector Bucket
            print("1️⃣ Creating S3 Vector Bucket...")
            try:
                s3vectors_client.create_vector_bucket(
                    vectorBucketName=vector_bucket_name
                )
                print(f"✅ Created vector bucket: {vector_bucket_name}")
            except Exception as e:
                if "already exists" in str(e).lower():
                    print(f"ℹ️  Vector bucket already exists: {vector_bucket_name}")
                else:
                    raise
            
            # Step 2: Create Vector Index (MUST exist before KB creation)
            print("2️⃣ Creating Vector Index...")
            try:
                s3vectors_client.create_index(
                    vectorBucketName=vector_bucket_name,
                    indexName=index_name,
                    dataType='float32',
                    dimension=1024,
                    distanceMetric='cosine',
                    metadataConfiguration={
                        'nonFilterableMetadataKeys': [
                            'AMAZON_BEDROCK_TEXT',
                            'AMAZON_BEDROCK_METADATA'
                        ]
                    }
                )
                print(f"✅ Created vector index: {index_name}")
                print("⏳ Waiting for index to be ready...")
                # Poll for index readiness instead of arbitrary sleep
                for _ in range(10):
                    try:
                        s3vectors_client.get_index(
                            vectorBucketName=vector_bucket_name,
                            indexName=index_name
                        )
                        break
                    except Exception:
                        time.sleep(1)
            except Exception as e:
                if "already exists" in str(e).lower():
                    print(f"ℹ️  Vector index already exists: {index_name}")
                else:
                    raise
            
            # Step 3: Create IAM role for Knowledge Base
            print("3️⃣ Creating IAM role for Knowledge Base...")
            account_id = self.session.client('sts').get_caller_identity()['Account']
            
            trust_policy = {
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Principal": {"Service": "bedrock.amazonaws.com"},
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {"aws:SourceAccount": account_id},
                        "ArnLike": {"aws:SourceArn": f"arn:aws:bedrock:{self.region}:{account_id}:knowledge-base/*"}
                    }
                }]
            }
            
            try:
                role_response = self.iam_client.create_role(
                    RoleName=role_name,
                    AssumeRolePolicyDocument=json.dumps(trust_policy),
                    Description="Role for Bedrock Knowledge Base with S3 Vectors"
                )
                role_arn = role_response['Role']['Arn']
                print(f"✅ Created IAM role: {role_arn}")
            except self.iam_client.exceptions.EntityAlreadyExistsException:
                role_arn = f"arn:aws:iam::{account_id}:role/{role_name}"
                print(f"ℹ️  Using existing IAM role: {role_arn}")
            
            # Step 4: Attach IAM policies
            print("4️⃣ Attaching IAM policies...")
            policies = {
                'S3VectorsAccess': {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "S3VectorsBucketAccess",
                            "Effect": "Allow",
                            "Action": [
                                "s3:GetObject",
                                "s3:PutObject",
                                "s3:DeleteObject",
                                "s3:ListBucket"
                            ],
                            "Resource": [
                                f"arn:aws:s3:::{vector_bucket_name}",
                                f"arn:aws:s3:::{vector_bucket_name}/*"
                            ]
                        },
                        {
                            "Sid": "S3VectorsIndexAccess",
                            "Effect": "Allow",
                            "Action": [
                                "s3vectors:GetVectorBucket",
                                "s3vectors:GetIndex",
                                "s3vectors:PutVector", "s3vectors:PutVectors",
                                "s3vectors:GetVector",
                                "s3vectors:GetVectors",
                                "s3vectors:DeleteVector",
                                "s3vectors:QueryVectors",
                                "s3vectors:ListIndexes"
                            ],
                            "Resource": [
                                f"arn:aws:s3vectors:{self.region}:{account_id}:bucket/{vector_bucket_name}",
                                f"arn:aws:s3vectors:{self.region}:{account_id}:bucket/{vector_bucket_name}/index/{index_name}"
                            ]
                        }
                    ]
                },
                'S3DataSourceAccess': {
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Sid": "S3DataSourceRead",
                        "Effect": "Allow",
                        "Action": ["s3:GetObject", "s3:ListBucket"],
                        "Resource": [
                            f"arn:aws:s3:::{bucket_name}",
                            f"arn:aws:s3:::{bucket_name}/*"
                        ]
                    }]
                },
                'BedrockModelAccess': {
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Sid": "BedrockEmbeddingModel",
                        "Effect": "Allow",
                        "Action": ["bedrock:InvokeModel"],
                        "Resource": f"arn:aws:bedrock:{self.region}::foundation-model/amazon.titan-embed-text-v2:0"
                    }]
                },
                'AppUserAccess': {
                    "Version": "2012-10-17",
                    "Statement": [
                        {
                            "Sid": "S3AppBucketList",
                            "Effect": "Allow",
                            "Action": [
                                "s3:ListBucket", 
                                "s3:ListBucketVersions",
                                "s3:GetBucketLocation",
                                "s3:GetBucketVersioning",
                                "s3:ListObjectsV2"
                            ],
                            "Resource": f"arn:aws:s3:::{bucket_name}"
                        },
                        {
                            "Sid": "S3AppObjectAccess",
                            "Effect": "Allow",
                            "Action": [
                                "s3:GetObject",
                                "s3:GetObjectVersion", 
                                "s3:PutObject",
                                "s3:DeleteObject",
                                "s3:DeleteObjectVersion"
                            ],
                            "Resource": f"arn:aws:s3:::{bucket_name}/*"
                        },
                        {
                            "Sid": "BedrockAppAccess",
                            "Effect": "Allow",
                            "Action": [
                                "bedrock:Retrieve",
                                "bedrock:RetrieveAndGenerate",
                                "bedrock:InvokeModel",
                                "bedrock:InvokeModelWithResponseStream",
                                "bedrock-agent:StartIngestionJob",
                                "bedrock-agent:GetIngestionJob"
                            ],
                            "Resource": [
                                "arn:aws:bedrock:*::foundation-model/*",
                                "arn:aws:bedrock:*:*:inference-profile/*",
                                f"arn:aws:bedrock:*:*:knowledge-base/{APP_NAME}-kb"
                            ]
                        }
                    ]
                }
            }
            
            for policy_name, policy_doc in policies.items():
                self.iam_client.put_role_policy(
                    RoleName=role_name,
                    PolicyName=policy_name,
                    PolicyDocument=json.dumps(policy_doc)
                )
            
            # Poll IAM role readiness then wait for eventual consistency
            print("⏳ Waiting for IAM role to propagate...")
            iam_client = self.session.client('iam')
            for attempt in range(15):
                try:
                    iam_client.get_role(RoleName=role_name)
                    break
                except iam_client.exceptions.NoSuchEntityException:
                    time.sleep(1)
            # IAM eventual consistency requires additional wait for cross-service authorization
            time.sleep(10)
            
            # Step 5: Create Bedrock Guardrail
            print("5️⃣ Creating Bedrock Guardrail...")
            guardrail_info = self.create_bedrock_guardrail()
            
            # Step 6: Create Knowledge Base (index now exists!)
            print("6️⃣ Creating Knowledge Base...")
            kb_response = self.bedrock_agent_client.create_knowledge_base(
                name=kb_name,
                roleArn=role_arn,
                knowledgeBaseConfiguration={
                    'type': 'VECTOR',
                    'vectorKnowledgeBaseConfiguration': {
                        'embeddingModelArn': f"arn:aws:bedrock:{self.region}::foundation-model/amazon.titan-embed-text-v2:0",
                        'embeddingModelConfiguration': {
                            'bedrockEmbeddingModelConfiguration': {
                                'dimensions': 1024,
                                'embeddingDataType': 'FLOAT32'
                            }
                        }
                    }
                },
                storageConfiguration={
                    'type': 'S3_VECTORS',
                    's3VectorsConfiguration': {
                        'indexArn': f"arn:aws:s3vectors:{self.region}:{account_id}:bucket/{vector_bucket_name}/index/{index_name}"
                    }
                }
            )
            
            kb_id = kb_response['knowledgeBase']['knowledgeBaseId']
            kb_arn = kb_response['knowledgeBase']['knowledgeBaseArn']
            print(f"✅ Created Knowledge Base: {kb_id}")
            
            # Step 6: Create Data Source
            print("6️⃣ Creating Data Source...")
            ds_response = self.bedrock_agent_client.create_data_source(
                knowledgeBaseId=kb_id,
                name=f"{APP_NAME}-datasource",
                dataSourceConfiguration={
                    'type': 'S3',
                    's3Configuration': {
                        'bucketArn': f"arn:aws:s3:::{bucket_name}",
                        'inclusionPrefixes': ['knowledge-base/contracts/']
                    }
                },
                dataDeletionPolicy='DELETE'
            )
            
            ds_id = ds_response['dataSource']['dataSourceId']
            print(f"✅ Created Data Source: {ds_id}")
            
            return {
                "knowledge_base_id": kb_id,
                "knowledge_base_arn": kb_arn,
                "data_source_id": ds_id,
                "role_arn": role_arn,
                "vector_bucket": vector_bucket_name,
                "index_arn": f"arn:aws:s3vectors:{self.region}:{account_id}:bucket/{vector_bucket_name}/index/{index_name}",
                "guardrail_id": guardrail_info['guardrail_id'] if guardrail_info else None,
                "guardrail_version": guardrail_info['guardrail_version'] if guardrail_info else None
            }
            
        except Exception as e:
            if "ConflictException" in str(type(e)) or "already exists" in str(e).lower():
                print(f"ℹ️  Knowledge Base already exists: {kb_name}")
                kbs = self.bedrock_agent_client.list_knowledge_bases()
                for kb in kbs.get('knowledgeBaseSummaries', []):
                    if kb['name'] == kb_name:
                        kb_id = kb['knowledgeBaseId']
                        kb_arn = f"arn:aws:bedrock:{self.region}:{account_id}:knowledge-base/{kb_id}"
                        print(f"✅ Found existing Knowledge Base: {kb_id}")
                        ds_list = self.bedrock_agent_client.list_data_sources(knowledgeBaseId=kb_id)
                        ds_id = ds_list['dataSourceSummaries'][0]['dataSourceId'] if ds_list.get('dataSourceSummaries') else None
                        if not ds_id:
                            ds_resp = self.bedrock_agent_client.create_data_source(
                                knowledgeBaseId=kb_id, name=f"{APP_NAME}-datasource",
                                dataSourceConfiguration={'type': 'S3', 's3Configuration': {'bucketArn': f"arn:aws:s3:::{bucket_name}", 'inclusionPrefixes': ['knowledge-base/contracts/']}},
                                dataDeletionPolicy='DELETE')
                            ds_id = ds_resp['dataSource']['dataSourceId']
                        return {
                            "knowledge_base_id": kb_id, "knowledge_base_arn": kb_arn, "data_source_id": ds_id,
                            "role_arn": role_arn, "vector_bucket": vector_bucket_name,
                            "index_arn": f"arn:aws:s3vectors:{self.region}:{account_id}:bucket/{vector_bucket_name}/index/{index_name}",
                            "guardrail_id": guardrail_info['guardrail_id'] if guardrail_info else None,
                            "guardrail_version": guardrail_info['guardrail_version'] if guardrail_info else None
                        }
            print(f"❌ Error creating Knowledge Base: {e}")
            import traceback
            traceback.print_exc()
            return None
    
    def create_app_role(self, bucket_name, kb_id=None):
        """Create IAM role for the Streamlit application."""
        print("🔑 Creating application IAM role...")
        
        account_id = self.session.client('sts').get_caller_identity()['Account']
        app_role_name = f"{APP_NAME}-app-role"
        
        try:
            # Trust policy for the app role
            # SECURITY NOTE: This trust policy allows any principal in the account to assume the role.
            # This is acceptable for:
            # - Development/demo environments
            # - Single-user AWS accounts
            # - Non-production workloads
            # 
            # For production environments, restrict the Principal to specific IAM users/roles:
            # "Principal": {"AWS": "arn:aws:iam::{account_id}:user/specific-username"}
            # 
            # Trust policy restricts role assumption to the current user only
            # The ExternalId condition provides additional security by requiring a secret value
            # to assume the role, preventing confused deputy attacks.
            current_user_arn = self.session.client('sts').get_caller_identity()['Arn']
            
            trust_policy = {
                "Version": "2012-10-17",
                "Statement": [{
                    "Effect": "Allow",
                    "Principal": {"AWS": current_user_arn},
                    "Action": "sts:AssumeRole",
                    "Condition": {
                        "StringEquals": {"sts:ExternalId": "invoiceflow-app"}
                    }
                }]
            }
            
            # Create the role
            try:
                role_response = self.iam_client.create_role(
                    RoleName=app_role_name,
                    AssumeRolePolicyDocument=json.dumps(trust_policy),
                    Description="Application role for InvoiceFlow AI Streamlit app"
                )
                role_arn = role_response['Role']['Arn']
                print(f"✅ Created app role: {role_arn}")
            except self.iam_client.exceptions.EntityAlreadyExistsException:
                role_arn = f"arn:aws:iam::{account_id}:role/{app_role_name}"
                print(f"ℹ️  Using existing app role: {role_arn}")
            
            # Load app policy from file
            try:
                with open('app-user-policy.json', 'r', encoding='utf-8') as f:
                    policy_text = f.read()
                
                # Substitute placeholders with actual values
                policy_text = policy_text.replace('${AWS::AccountId}', account_id)
                policy_text = policy_text.replace('${AWS::Region}', self.region)
                
                # Substitute KB ID if available, otherwise use account-scoped wildcard
                if kb_id:
                    policy_text = policy_text.replace('knowledge-base/*', f'knowledge-base/{kb_id}')
                
                app_policy = json.loads(policy_text)
                
                # Attach the policy
                self.iam_client.put_role_policy(
                    RoleName=app_role_name,
                    PolicyName='AppUserAccess',
                    PolicyDocument=json.dumps(app_policy)
                )
                print(f"✅ Attached app permissions policy")
            except Exception as e:
                print(f"⚠️ Failed to attach app policy: {e}")
                # Continue without failing the entire deployment
            
            return {
                "role_arn": role_arn,
                "role_name": app_role_name
            }
            
        except Exception as e:
            print(f"❌ Error creating app role: {e}")
            return None
    
    def print_deployment_summary(self, outputs, kb_info=None):
        """Print deployment summary."""
        print("\n" + "="*60)
        print("🎉 DEPLOYMENT COMPLETE!")
        print("="*60)
        print(f"\n� CogBnito User Pool ID: {outputs.get('CognitoUserPoolId', 'N/A')}")
        print(f"🔑 Cognito Client ID: {outputs.get('CognitoClientId', 'N/A')}")
        print(f"🌍 Cognito Domain: {outputs.get('CognitoUserPoolDomain', 'N/A')}.auth.{self.region}.amazoncognito.com")
        
        if kb_info:
            print(f"\n🧠 Knowledge Base ID: {kb_info.get('knowledge_base_id', 'N/A')}")
            print(f"📚 Data Source ID: {kb_info.get('data_source_id', 'N/A')}")
        
        print("\n" + "="*60)
        print("📝 Next Steps:")
        print("1. Run: streamlit run simplified_app.py")
        print("2. Upload contracts to S3: invoiceflow-ai-bucket/knowledge-base/contracts/")
        print("3. Sync Knowledge Base data source")
        print("="*60 + "\n")

def main():
    """Main deployment function."""
    print("🚀 InvoiceFlow AI - Complete Infrastructure Deployment")
    print("="*60 + "\n")
    
    # Get session with assumed role if configured
    session = get_session_with_role()
    
    # Get account ID for bucket naming
    account_id = session.client('sts').get_caller_identity()['Account']
    bucket_name = f"{APP_NAME}-bucket-{account_id}"
    
    print()
    deployer = InfrastructureDeployer(session=session)
    
    # Deploy CloudFormation stack (includes S3 bucket)
    outputs = deployer.deploy_stack()
    
    # Get bucket name from CloudFormation outputs
    bucket_name = outputs.get('DocumentBucketName', bucket_name)
    
    # Create default user
    if outputs.get('CognitoUserPoolId'):
        deployer.create_default_user(outputs['CognitoUserPoolId'])
    
    # Retrieve client secret for the app
    if outputs.get('CognitoUserPoolId') and outputs.get('CognitoClientId'):
        try:
            resp = deployer.cognito_client.describe_user_pool_client(
                UserPoolId=outputs['CognitoUserPoolId'],
                ClientId=outputs['CognitoClientId']
            )
            client_secret = resp['UserPoolClient'].get('ClientSecret')
            if client_secret:
                outputs['cognito_client_secret'] = client_secret
        except Exception as e:
            logger.warning(f"Could not retrieve client secret: {e}")
    
    # Create Knowledge Base programmatically
    print("\n" + "="*60)
    kb_info = deployer.create_knowledge_base(bucket_name)
    
    # Always add S3 bucket to outputs (from CloudFormation)
    outputs['s3_bucket'] = bucket_name
    
    if kb_info:
        # Add Knowledge Base info to outputs
        outputs['knowledge_base_id'] = kb_info['knowledge_base_id']
        outputs['data_source_id'] = kb_info['data_source_id']
        outputs['knowledge_base_arn'] = kb_info['knowledge_base_arn']
        outputs['role_arn'] = kb_info['role_arn']
        outputs['vector_bucket'] = kb_info['vector_bucket']
        outputs['index_arn'] = kb_info['index_arn']
        print(f"\n🧠 Knowledge Base ID: {kb_info['knowledge_base_id']}")
        print(f"📚 Data Source ID: {kb_info['data_source_id']}")
        print("\n✅ Knowledge Base created successfully!")
    else:
        print("\n⚠️  Knowledge Base creation failed - check logs above")
    
    # Print summary
    deployer.print_deployment_summary(outputs, kb_info)
    
    # Create app-specific IAM role
    print("\n" + "="*60)
    app_role_info = deployer.create_app_role(bucket_name, kb_id=kb_info.get('knowledge_base_id') if kb_info else None)
    
    if app_role_info:
        outputs['app_role_arn'] = app_role_info['role_arn']
        print(f"\n🔑 App Role ARN: {app_role_info['role_arn']}")
    
    # Save outputs to file
    # Map CloudFormation PascalCase keys to snake_case for the app
    if 'CognitoUserPoolId' in outputs:
        outputs['cognito_user_pool_id'] = outputs['CognitoUserPoolId']
    if 'CognitoClientId' in outputs:
        outputs['cognito_client_id'] = outputs['CognitoClientId']
    if 'CognitoUserPoolDomain' in outputs:
        outputs['cognito_domain'] = outputs['CognitoUserPoolDomain']
    if kb_info and kb_info.get('guardrail_id'):
        outputs['guardrail_id'] = kb_info['guardrail_id']
        outputs['guardrail_version'] = kb_info.get('guardrail_version', 'DRAFT')
    
    outputs_file = 'infrastructure_outputs.json'
    try:
        with open(outputs_file, 'w', encoding='utf-8') as f:
            json.dump(outputs, f, indent=2)
        
        # Validate the file was written correctly
        with open(outputs_file, 'r', encoding='utf-8') as f:
            saved_config = json.load(f)
            required_keys = ['knowledge_base_id', 'data_source_id', 's3_bucket']
            missing_keys = [key for key in required_keys if not saved_config.get(key)]
            if missing_keys:
                print(f"❌ ERROR: Configuration file missing required keys: {missing_keys}")
                return False
        
        print(f"💾 Outputs saved and validated: {outputs_file}")
        
    except Exception as e:
        print(f"❌ ERROR: Failed to save configuration file: {e}")
        return False
    
    # Also print the KB IDs again for clarity
    if kb_info:
        print(f"\n🔍 Knowledge Base Configuration:")
        print(f"   KB ID: {kb_info['knowledge_base_id']}")
        print(f"   Data Source ID: {kb_info['data_source_id']}")
    
    if app_role_info:
        print(f"\n🚀 To run the app with proper permissions:")
        print(f"   export APP_ROLE_ARN='{app_role_info['role_arn']}'")
        print(f"   streamlit run simplified_app.py")

if __name__ == "__main__":
    main()
