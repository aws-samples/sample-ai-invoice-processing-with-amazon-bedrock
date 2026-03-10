---
inclusion: manual
---

# ADDF Module Development Guide

## Overview

The Autonomous Driving Data Framework (ADDF) is a collection of modules for Scene Detection, Simulation, Visualization, Compute, Storage, and more, deployed using the SeedFarmer orchestration tool. This guide provides instructions for developing, testing, and deploying ADDF modules using Kiro.

## Module Structure

Every ADDF module follows a standard structure:

```
module-name/
├── app.py                # CDK application entry point
├── stack.py              # CDK stack definition
├── deployspec.yaml       # SeedFarmer deployment instructions
├── modulestack.yaml      # IAM permissions for deployment
├── README.md             # Module documentation
├── requirements.txt      # Python dependencies
└── tests/                # Unit and integration tests
```

### Required Files

1. **app.py**: Entry point for CDK application that creates the stack
2. **stack.py**: Contains the CDK stack definition with AWS resources
3. **deployspec.yaml**: Defines how SeedFarmer should deploy the module
4. **modulestack.yaml**: Contains IAM permissions needed for deployment
5. **README.md**: Documentation with inputs, outputs, and usage examples

## Development Workflow

### 1. Setting Up Development Environment

```bash
# Clone the ADDF repository
git clone https://github.com/awslabs/autonomous-driving-data-framework.git
cd autonomous-driving-data-framework

# Create and activate virtual environment
python -m venv .venv
source .venv/bin/activate

# Install dependencies
pip install -r requirements.txt
```

### 2. Creating a New Module

```bash
# Create module directory structure
mkdir -p modules/category/new-module-name
cd modules/category/new-module-name

# Create required files
touch app.py stack.py deployspec.yaml modulestack.yaml README.md requirements.txt
mkdir tests
```

### 3. Implementing the Module

#### app.py Template

```python
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

import os
from aws_cdk import App
from stack import YourModuleStack

# Get environment variables set by SeedFarmer
project_name = os.getenv("SEEDFARMER_PROJECT_NAME", "")
deployment_name = os.getenv("SEEDFARMER_DEPLOYMENT_NAME", "")
module_name = os.getenv("SEEDFARMER_MODULE_NAME", "")

# Helper function to get parameters
def _param(name: str) -> str:
    return f"SEEDFARMER_PARAMETER_{name}"

# Get module parameters
param1 = os.getenv(_param("PARAM1"))
param2 = os.getenv(_param("PARAM2"))

# Create CDK app and stack
app = App()
stack = YourModuleStack(
    app,
    f"{project_name}-{deployment_name}-{module_name}",
    parameters={
        "param1": param1,
        "param2": param2,
    },
    env={
        "account": os.environ["CDK_DEFAULT_ACCOUNT"],
        "region": os.environ["CDK_DEFAULT_REGION"],
    },
)

app.synth()
```

#### stack.py Template

```python
# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved.
# SPDX-License-Identifier: Apache-2.0

from aws_cdk import Stack, CfnOutput
from constructs import Construct

class YourModuleStack(Stack):
    def __init__(self, scope: Construct, id: str, parameters: dict, **kwargs) -> None:
        super().__init__(scope, id, **kwargs)
        
        # Extract parameters
        param1 = parameters.get("param1")
        param2 = parameters.get("param2")
        
        # Create AWS resources
        # ...
        
        # Export outputs for other modules to use
        CfnOutput(self, "Output1", value="value1")
        CfnOutput(self, "Output2", value="value2")
        
        # Add metadata for SeedFarmer
        self.export_value("value1", name="Output1")
        self.export_value("value2", name="Output2")
```

#### deployspec.yaml Template

```yaml
publishGenericEnvVariables: true
deploy:
  phases:
    install:
      commands:
      - npm install -g aws-cdk@2.146.0
      - pip install -r requirements.txt
    build:
      commands:
      - cdk deploy --require-approval never --progress events --app "python app.py" --outputs-file ./cdk-exports.json
      - seedfarmer metadata convert -f cdk-exports.json
destroy:
  phases:
    install:
      commands:
      - npm install -g aws-cdk@2.146.0
      - pip install -r requirements.txt
    build:
      commands:
      - cdk destroy --force --app "python app.py"
build_type: BUILD_GENERAL1_LARGE
```

#### modulestack.yaml Template

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: This template deploys Module specific IAM permissions

Parameters:
  DeploymentName:
    Type: String
    Description: The name of the deployment
  ModuleName:
    Type: String
    Description: The name of the Module
  RoleName:
    Type: String
    Description: The name of the IAM Role

Resources:
  Policy:
    Type: 'AWS::IAM::Policy'
    Properties:
      PolicyDocument:
        Statement:
          - Effect: Allow
            Action:
              - 's3:GetObject'
              - 's3:PutObject'
              - 's3:ListBucket'
            Resource: '*'
        Version: 2012-10-17
      PolicyName: !Sub "${DeploymentName}-${ModuleName}-policy"
      Roles: [!Ref RoleName]
```

#### README.md Template

```markdown
# Module Name

## Description

Brief description of what this module does and what AWS resources it creates.

## Inputs/Outputs

### Input Parameters

#### Required

- `param1`: Description of parameter 1
- `param2`: Description of parameter 2

#### Optional

- `optional-param`: Description of optional parameter (default: `default-value`)

### Module Metadata Outputs

- `Output1`: Description of output 1
- `Output2`: Description of output 2

#### Output Example

```json
{
  "Output1": "value1",
  "Output2": "value2"
}
```

## Testing

Instructions for testing the module.
```

### 4. Writing Tests

Create unit tests in the `tests` directory:

```python
# tests/test_stack.py
import aws_cdk as cdk
import pytest
from stack import YourModuleStack

def test_stack_creates_resources():
    # GIVEN
    app = cdk.App()
    
    # WHEN
    stack = YourModuleStack(
        app, 
        "test-stack",
        parameters={
            "param1": "value1",
            "param2": "value2",
        }
    )
    
    # THEN
    template = cdk.assertions.Template.from_stack(stack)
    template.resource_count_is("AWS::S3::Bucket", 1)
```

### 5. Testing Locally

```bash
# Run unit tests
pytest tests/

# Synthesize CDK template
cdk synth --app "python app.py"
```

## Deployment Workflow

### 1. Creating Module Manifest

Create a module manifest file in the `manifests` directory:

```yaml
# manifests/your-deployment/your-modules.yaml
name: your-module-name
path: modules/category/your-module-name
targetAccount: primary
parameters:
  - name: param1
    value: value1
  - name: param2
    value: value2
  - name: dependency-param
    valueFrom:
      moduleMetadata:
        group: other-group
        name: other-module
        key: OutputKey
```

### 2. Adding to Deployment Manifest

Add your module group to the deployment manifest:

```yaml
# manifests/your-deployment/deployment.yaml
name: your-deployment
toolchainRegion: us-west-2
groups:
  - name: existing-group
    path: manifests/your-deployment/existing-modules.yaml
  - name: your-group
    path: manifests/your-deployment/your-modules.yaml
targetAccountMappings:
  - alias: primary
    accountId:
      valueFrom:
        envVariable: PRIMARY_ACCOUNT
    default: true
    regionMappings:
      - region: us-west-2
        default: true
```

### 3. Deploying with SeedFarmer

```bash
# Create .env file with account ID
echo "PRIMARY_ACCOUNT=123456789012" > .env

# Deploy using SeedFarmer
seedfarmer apply manifests/your-deployment/deployment.yaml --env-file .env
```

### 4. Testing Deployment

After deployment, verify that your module is working correctly:

1. Check AWS CloudFormation for successful stack creation
2. Verify that resources were created correctly
3. Test functionality using the AWS Console or CLI
4. Check CloudWatch Logs for any errors

### 5. Destroying Resources

```bash
# Destroy specific module
seedfarmer destroy your-deployment --modules your-group/your-module-name

# Destroy entire deployment
seedfarmer destroy your-deployment
```

## Best Practices

### Module Development

1. **Follow the Single Responsibility Principle**: Each module should do one thing well
2. **Use Least Privilege IAM Permissions**: Only request permissions your module actually needs
3. **Document All Inputs and Outputs**: Clearly document all parameters and outputs in README.md
4. **Handle Dependencies Properly**: Use moduleMetadata to reference outputs from other modules
5. **Include Comprehensive Tests**: Write unit tests for all CDK constructs
6. **Use CDK Constructs**: Prefer higher-level CDK constructs over CloudFormation resources
7. **Implement Proper Error Handling**: Handle errors gracefully in your CDK code
8. **Use Tags**: Tag all resources for better organization and cost tracking

### Module Testing

1. **Test Locally First**: Use `cdk synth` to validate your CDK code
2. **Write Unit Tests**: Test all CDK constructs with pytest
3. **Test with Minimal Permissions**: Ensure your module works with least privilege
4. **Test Dependencies**: Verify that your module correctly uses outputs from dependencies
5. **Test Cleanup**: Ensure your module cleans up all resources when destroyed

### Module Deployment

1. **Use Environment Variables**: Store sensitive values in environment variables
2. **Version Your Modules**: Use git tags to version your modules
3. **Document Deployment Steps**: Include clear deployment instructions in README.md
4. **Test in Isolation**: Deploy and test your module in isolation before integrating
5. **Monitor Deployments**: Use CloudWatch to monitor your deployed resources

## Common Issues and Solutions

### Issue: Module Deployment Fails

**Solution**: Check CloudWatch Logs for the CodeBuild project to see detailed error messages.

### Issue: Module Can't Access Resources from Dependencies

**Solution**: Verify that you're correctly referencing moduleMetadata and that the dependency module is in a group that's deployed before your module.

### Issue: IAM Permission Errors

**Solution**: Add the required permissions to your modulestack.yaml file.

### Issue: CDK Synthesis Errors

**Solution**: Check your CDK code for errors, especially property types and required values.

## Reference Documentation

- [SeedFarmer Documentation](https://seed-farmer.readthedocs.io/)
- [AWS CDK Documentation](https://docs.aws.amazon.com/cdk/latest/guide/home.html)
- [ADDF GitHub Repository](https://github.com/awslabs/autonomous-driving-data-framework)