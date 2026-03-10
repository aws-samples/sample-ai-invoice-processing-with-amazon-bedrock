---
inclusion: manual
---

# Seed-Farmer Guide

## Overview

Seed-Farmer is a Python-based CICD library that leverages the GitOps paradigm to manage deployed code. It is tooling-agnostic, supporting AWS CDK, CloudFormation, bash scripting, Terraform, and more. Seed-Farmer uses declarative manifests to define deployable code (modules) and manages the state of deployed code, detecting and applying changes as needed.

## Key Concepts

- **Project**: A direct one-to-one relationship with an AWS CodeSeeder managed CodeBuild project. Projects are isolated from one another.
- **Deployment**: Represents all modules leveraging AWS resources in one or many accounts. Provides isolation from other deployments in the same project.
- **Group**: Represents modules that can be deployed concurrently. No module in a group can depend on another module in the same group.
- **Module**: The deployable unit of code. A module can be deployed multiple times in the same deployment as long as it has a unique logical name.

## Multi-Account Support

Seed-Farmer uses the concept of a "toolchain account" and "target account(s)":

- **Toolchain Account**: The primary account that stores deployment-specific information and has the toolchain-role necessary to manage deployments.
- **Target Account(s)**: The account(s) where modules are deployed, with the deployment-role necessary to deploy modules.

There can be only ONE toolchain account with MANY target accounts. A toolchain account can also be a target account. Each account only needs to be bootstrapped once regardless of the region where modules are deployed.

## Getting Started

### Installation

```bash
# Create a virtual environment
python -m venv .venv
source .venv/bin/activate

# Install Seed-Farmer
pip install seed-farmer
```

### Bootstrap Your Account

```bash
# Replace with your account ID and project name
seedfarmer bootstrap toolchain \
--project yourproject \
-t arn:aws:iam::123456789012:role/Admin \
--as-target
```

### Deploy a Deployment

```bash
# Create a .env file with your account ID
echo PRIMARY_ACCOUNT=123456789012 >> .env

# Apply a deployment manifest
seedfarmer apply manifests/examples/deployment.yaml --env-file .env
```

### Destroy a Deployment

```bash
seedfarmer destroy deployment-name --env-file .env
```

## Manifests

### Deployment Manifest

The deployment manifest is the top-level manifest that defines your deployment. It includes information about the deployment name, toolchain region, groups of modules, and target account mappings.

#### Example Deployment Manifest

```yaml
name: examples
nameGenerator:
  prefix: myprefix
  suffix:
    valueFrom:
        envVariable: SUFFIX_ENV_VARIABLE
toolchainRegion: us-west-2
forceDependencyRedeploy: False
archiveSecret: example-archive-credentials-modules
groups:
  - name: optionals
    path: manifests-multi/examples/optional-modules.yaml
    concurrency: 2
  - name: optionals-2
    path: manifests-multi/examples/optional-modules-2.yaml
targetAccountMappings:
  - alias: primary
    accountId:
      valueFrom:
        envVariable: PRIMARY_ACCOUNT
    default: true
    codebuildImage: XXXXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/aws-codeseeder/code-build-base:5.5.0
    runtimeOverrides:
      python: "3.13"
    parametersGlobal:
      dockerCredentialsSecret: nameofsecret
      permissionsBoundaryName: policyname
    regionMappings:
      - region: us-east-2
        default: true
        parametersRegional:
          vpcId: vpc-XXXXXXXXX
          privateSubnetIds:
            - subnet-XXXXXXXXX
            - subnet-XXXXXXXXX
          securityGroupsId:
            - sg-XXXXXXXXX
  - alias: secondary
    accountId: 123456789012
    regionMappings:
      - region: us-west-2
      - region: us-east-2
        default: true
```

#### Key Components of Deployment Manifest

- **name**: The name of your deployment (cannot be used with nameGenerator)
- **nameGenerator**: Dynamically generate a deployment name with prefix and suffix
- **toolchainRegion**: The region where the toolchain is created
- **forceDependencyRedeploy**: Boolean to redeploy all dependency modules (default: False)
- **archiveSecret**: Name of a secret in SecretsManager for private HTTPS archive credentials
- **groups**: List of module groups with their paths and concurrency settings
- **targetAccountMappings**: Configuration for target accounts including:
  - **alias**: Logical name for the account
  - **accountId**: The AWS account ID (can use environment variables)
  - **default**: Designates this as the default account
  - **codebuildImage**: Custom build image to use
  - **runtimeOverrides**: Runtime versions for the build environment
  - **parametersGlobal**: Parameters that apply to all region mappings
  - **regionMappings**: Region-specific configurations

### Module Manifest

Module manifests define individual modules within a group. Each module has its own configuration including path, target account, parameters, and more.

#### Example Module Manifest

```yaml
name: networking
path: modules/optionals/networking/
targetAccount: primary
parameters:
  - name: internet-accessible
    value: true
---
name: buckets
path: modules/optionals/buckets
targetAccount: secondary
targetRegion: us-west-2
codebuildImage: XXXXXXXXXXXX.dkr.ecr.us-east-1.amazonaws.com/aws-codeseeder/code-build-base:3.3.0
parameters:
  - name: encryption-type
    value: SSE
  - name: some-name
    valueFrom:
      moduleMetadata:
        group: optionals
        name: networking
        key: VpcId
dataFiles:
  - filePath: data/test2.txt
  - filePath: test1.txt
```

#### Key Components of Module Manifest

- **name**: The name of the module (must be unique in the group)
- **path**: Path to the module code (local path or Git repository)
- **targetAccount**: The alias of the account from deployment manifest
- **targetRegion**: The region to deploy to (overrides any mappings)
- **codebuildImage**: Custom build image to use
- **parameters**: List of parameters for the module
  - **name**: Parameter name
  - **value**: Direct value or valueFrom source
  - **valueFrom**: Get value from moduleMetadata, parameterStore, secretsManager, etc.
- **dataFiles**: Additional files to add to the bundle

### Git Repository References

You can reference modules from Git repositories:

```yaml
name: networking
path: git::https://github.com/awslabs/idf-modules.git//modules/network/basic-cdk?ref=release/1.0.0&depth=1
targetAccount: secondary
parameters:
  - name: internet-accessible
    value: true
```

### Archive References

You can reference modules from archives:

```yaml
name: networking
path: archive::https://github.com/awslabs/idf-modules/archive/refs/tags/v1.6.0.tar.gz?module=modules/network/basic-cdk
targetAccount: secondary
parameters:
  - name: internet-accessible
    value: true
```

## Module Development

### Required Files

Every module must have:
- Deployment manifest
- Module manifest
- deployspec.yaml
- README.md

### Optional Files

- modulestack.yaml (for IAM permissions)

### Creating a New Module

```bash
seedfarmer init module -g mygroup -m mymodule
cd modules/mygroup/mymodule
```

### Deployspec

The deployspec.yaml file defines deployment instructions for a module. It includes commands for installing dependencies, building, and destroying resources.

#### Basic Deployspec Example

```yaml
deploy:
  phases:
    install:
      commands:
      - pip install -r requirements.txt
    pre_build:
      commands:
      - echo "Prebuild stage"
    build:
      commands:
      - echo "bash deploy.sh"
    post_build:
      commands:
      - echo "Deploy successful"
destroy:
  phases:
    install:
      commands:
      - pip install -r requirements.txt
    pre_build:
      commands:
      - echo "Prebuild stage"
    build:
      commands:
      - echo "DESTROY!"
    post_build:
      commands:
      - echo "Destroy successful"
build_type: BUILD_GENERAL1_LARGE
publishGenericEnvVariables: true
```

#### Project-Specific Module Deployspec Example

```yaml
deploy:
  phases:
    install:
      commands:
        - npm install -g aws-cdk@2.20.0
        - apt-get install jq
        - pip install -r requirements.txt
    build:
      commands:
        - aws iam create-service-linked-role --aws-service-name elasticmapreduce.amazonaws.com || true
        - export ECR_REPO_NAME=$(echo $MYAPP_PARAMETER_FARGATE | jq -r '."ecr-repository-name"')
        - aws ecr describe-repositories --repository-names ${ECR_REPO_NAME} || aws ecr create-repository --repository-name ${ECR_REPO_NAME}
        - export IMAGE_NAME=$(echo $MYAPP_PARAMETER_FARGATE | jq -r '."image-name"')
        - export COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
        - export IMAGE_TAG=${COMMIT_HASH:=latest}
        - export REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPO_NAME
        - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
        - echo "MYAPP_PARAMETER_SHARED_BUCKET_NAME: ${MYAPP_PARAMETER_SHARED_BUCKET_NAME}"
        - echo Building the Docker image...          
        - cd service/ && docker build -t $REPOSITORY_URI:latest .
        - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
        - docker push $REPOSITORY_URI:latest && docker push $REPOSITORY_URI:$IMAGE_TAG
        - cd.. && cdk deploy --all --require-approval never --progress events --app "python app.py" --outputs-file ./cdk-exports.json
        - export MYAPP_MODULE_METADATA=$(python -c "import json; file=open('cdk-exports.json'); print(json.load(file)['myapp-${MYAPP_DEPLOYMENT_NAME}-${MYAPP_MODULE_NAME}']['metadata'])")
destroy:
  phases:
    install:
      commands:
      - npm install -g aws-cdk@2.20.0
      - pip install -r requirements.txt
    build:
      commands:
      - cdk destroy --all --force --app "python app.py"
build_type: BUILD_GENERAL1_LARGE
```

#### Generic Module Deployspec Example

```yaml
deploy:
  phases:
    install:
      commands:
        - npm install -g aws-cdk@2.20.0
        - apt-get install jq
        - pip install -r requirements.txt
    build:
      commands:
        - aws iam create-service-linked-role --aws-service-name elasticmapreduce.amazonaws.com || true
        - export ECR_REPO_NAME=$(echo $SEEDFARMER_PARAMETER_FARGATE | jq -r '."ecr-repository-name"')
        - aws ecr describe-repositories --repository-names ${ECR_REPO_NAME} || aws ecr create-repository --repository-name ${ECR_REPO_NAME}
        - export IMAGE_NAME=$(echo $SEEDFARMER_PARAMETER_FARGATE | jq -r '."image-name"')
        - export COMMIT_HASH=$(echo $CODEBUILD_RESOLVED_SOURCE_VERSION | cut -c 1-7)
        - export IMAGE_TAG=${COMMIT_HASH:=latest}
        - export REPOSITORY_URI=$AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com/$ECR_REPO_NAME
        - aws ecr get-login-password --region $AWS_DEFAULT_REGION | docker login --username AWS --password-stdin $AWS_ACCOUNT_ID.dkr.ecr.$AWS_DEFAULT_REGION.amazonaws.com
        - echo "SEEDFARMER_PARAMETER_SHARED_BUCKET_NAME: ${SEEDFARMER_PARAMETER_SHARED_BUCKET_NAME}"
        - echo Building the Docker image...          
        - cd service/ && docker build -t $REPOSITORY_URI:latest .
        - docker tag $REPOSITORY_URI:latest $REPOSITORY_URI:$IMAGE_TAG
        - docker push $REPOSITORY_URI:latest && docker push $REPOSITORY_URI:$IMAGE_TAG
        - cd.. && cdk deploy --all --require-approval never --progress events --app "python app.py" --outputs-file ./cdk-exports.json
        - export SEEDFARMER_MODULE_METADATA=$(python -c "import json; file=open('cdk-exports.json'); print(json.load(file)['seedfarmer-${SEEDFARMER_DEPLOYMENT_NAME}-${SEEDFARMER_MODULE_NAME}']['metadata'])")
destroy:
  phases:
    install:
      commands:
      - npm install -g aws-cdk@2.20.0
      - pip install -r requirements.txt
    build:
      commands:
      - cdk destroy --all --force --app "python app.py"
build_type: BUILD_GENERAL1_LARGE
publishGenericEnvVariables: true
```

### Deployspec Parameters

- **build_type**: Size of the compute instance (BUILD_GENERAL1_SMALL, BUILD_GENERAL1_MEDIUM, BUILD_GENERAL1_LARGE, BUILD_GENERAL1_2XLARGE)
- **publishGenericEnvVariables**: Boolean to use SEEDFARMER_ prefix instead of project name prefix for environment variables

### Metadata CLI Helper Commands

Seed-Farmer provides CLI commands to manage metadata in module deployments:

```bash
seedfarmer metadata --help
```

Available commands:
- **add**: Add key-value pairs to metadata
- **convert**: Convert CDK output to Seed-Farmer metadata
- **depmod**: Get the full name of the module
- **paramvalue**: Get parameter value based on suffix

Example usage in deployspec.yaml:

```yaml
deploy:
  phases:
    build:
      commands:
      # execute the CDK
      - cdk deploy --require-approval never --progress events --app "python app.py" --outputs-file ./cdk-exports.json
      - seedfarmer metadata add -k TestKeyValue -v TestKeyValueValue || true
      - seedfarmer metadata add -j '{"JsonTest":"ValHere"}' || true
      - export DEPMOD=$(seedfarmer metadata depmod)
      - echo ${DEPMOD}
      - seedfarmer metadata convert
      - seedfarmer metadata convert -f cdk-exports.json
      - seedfarmer metadata convert -jq .${DEPMOD}.metadata
      - echo $(seedfarmer metadata paramvalue -s DEPLOYMENT_NAME)
```

### Module README

Each module should have a README.md that describes:
- Description of the module
- Input parameters (required and optional)
- Output parameters with example JSON

Example README.md:

```markdown
# OpenSearch Module

## Description

This module creates an OpenSearch cluster

## Inputs/Outputs

### Input Parameters

#### Required

- `vpc-id`: The VPC-ID that the cluster will be created in

#### Optional
- `opensearch_data_nodes`: The number of data nodes, defaults to `1`
- `opensearch_data_nodes_instance_type`: The data node type, defaults to `r6g.large.search`
- `opensearch_master_nodes`: The number of master nodes, defaults to `0`
- `opensearch_master_nodes_instance_type`: The master node type, defaults to `r6g.large.search`
- `opensearch_ebs_volume_size`: The EBS volume size (in GB), defaults to `10`

### Module Metadata Outputs

- `OpenSearchDomainEndpoint`: the endpoint name of the OpenSearch Domain
- `OpenSearchDomainName`: the name of the OpenSearch Domain
- `OpenSeearchDashboardUrl`: URL of the OpenSearch cluster dashboard
- `OpenSearchSecurityGroupId`: name of the DDB table created for Rosbag Scene Data

#### Output Example

```json
{
  "OpenSearchDashboardUrl": "https://vpc-myapp-test-core-opensearch-aaa.us-east-1.es.amazonaws.com/_dashboards/",
  "OpenSearchDomainName": "vpc-myapp-test-core-opensearch-aaa",
  "OpenSearchDomainEndpoint": "vpc-myapp-test-core-opensearch-aaa.us-east-1.es.amazonaws.com",
  "OpenSearchSecurityGroupId": "sg-0475c9e7efba05c0d"
}
```
```

### ModuleStack

The modulestack.yaml file contains IAM permissions that AWS CodeSeeder needs to deploy your module. It's recommended to use least-privilege policies.

#### Initial Template

```yaml
AWSTemplateFormatVersion: 2010-09-09
Description: This template deploys a Module specific IAM permissions

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
            Action: '*'
            Resource: '*'
        Version: 2012-10-17
      PolicyName: "myapp-modulespecific-policy"
      Roles: [!Ref RoleName]
```

#### Example with Parameter References

```yaml
Parameters:
  InstanceName:
    Type: String
    Description: The name of the Cloud9 instance

Resources:
  Policy:
    Type: "AWS::IAM::Policy"
    Properties:
      PolicyDocument:
        Statement:
          - Effect: Allow
            Action:
              - "ec2:ModifyVolume"
            Resource: "*"
            Condition:
              StringLike:
                ec2:ResourceTag/Name: !Sub 'aws-cloud9-${InstanceName}-*'
```

## Network Configuration

Seed-Farmer supports various ways to configure network settings:

### Hardcoded Values

```yaml
network: 
  vpcId: vpc-XXXXXXXXX    
  privateSubnetIds:
    - subnet-XXXXXXXXX
    - subnet-XXXXXXXXX
  securityGroupsIds:
    - sg-XXXXXXXXX
```

### Regional Parameters

```yaml
network: 
  vpcId:
    valueFrom:
      parameterValue: vpcId
  privateSubnetIds:
    valueFrom:
      parameterValue: privateSubnetIds
  securityGroupIds:
    valueFrom:
      parameterValue: securityGroupIds
```

### AWS SSM Parameters

```yaml
network: 
  vpcId: 
    valueFrom:
      parameterStore: /idf/testing/vpcid
  privateSubnetIds:
    valueFrom:
      parameterStore: /idf/testing/privatesubnets
  securityGroupIds:
    valueFrom:
      parameterStore: /idf/testing/securitygroups
```

### Environment Variables

```yaml
network: 
  vpcId: 
    valueFrom:
      envVariable: VPCID
  privateSubnetIds:
    valueFrom:
      envVariable: PRIVATESUBNETS
  securityGroupIds:
    valueFrom:
      envVariable: SECURITYGROUPS
```

## Best Practices

1. Use least-privilege IAM policies in modulestack.yaml
2. Document module inputs and outputs in README.md
3. Use environment variables for account IDs and other sensitive values
4. Organize modules into logical groups based on dependencies
5. Test modules locally before deploying to production
6. Use generic modules with `publishGenericEnvVariables: true` for reusability
7. Provide detailed metadata outputs for dependent modules
8. Use concurrency settings to optimize deployment speed
9. Leverage parameter stores for configuration values
10. Follow the shared-responsibility model for dependency management

## CLI Commands

```bash
# List available commands
seedfarmer --help

# Bootstrap an account
seedfarmer bootstrap toolchain --help

# Deploy a manifest
seedfarmer apply --help

# Destroy a deployment
seedfarmer destroy --help

# Initialize a new module
seedfarmer init module --help

# Manage metadata
seedfarmer metadata --help
```

## Dependency Management

Seed-Farmer has a shared-responsibility model for dependency management. It prevents:
- Deletion of modules that have downstream dependencies
- Circular references between modules

However, users are responsible for:
- Managing relationships between modules
- Assessing impact of changes via redeployment
- Resolving blockers due to failed module deployments

## References

For more detailed information, refer to the [Seed-Farmer documentation](https://seed-farmer.readthedocs.io/).