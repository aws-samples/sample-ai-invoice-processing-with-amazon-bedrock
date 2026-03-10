---
inclusion: manual
---

# DSR Security Review

When writing infrastructure code you need to follow the below rules.

## Rules

### General Development Principles

#### Security Requirements
   - HIGH: Implement principle of least privilege for all IAM roles and policies
   - HIGH: Enable encryption at rest for all data storage services
   - HIGH: Enable encryption in transit for all data transfer
   - HIGH: Follow OWASP Top 10 security requirements
   - HIGH: Prevent modification of existing network controls
   - HIGH: Use secrets management for sensitive data
   - LOW: Implement additional security best practices beyond OWASP Top 10

#### Infrastructure Design
   - HIGH: Implement multi-AZ deployments for high availability
   - HIGH: Design and implement rollback mechanisms
   - HIGH: Use consistent resource tagging
   - HIGH: Prevent concurrent deployments unless explicitly specified
   - HIGH: Document all created resources
   - HIGH: Use Infrastructure as Code best practices
   - MEDIUM: Implement cost optimization strategies

#### Compliance & Documentation
   - HIGH: Validate all open source libraries against approved license list
   - HIGH: Include copyright headers and software bill of materials
   - HIGH: Enable appropriate logging and monitoring
   - HIGH: Document all security configurations
   - LOW: Implement automated compliance checks

### Networking & Security

#### VPC Configuration:
  - HIGH: Use multiple availability zones
  - HIGH: Implement private subnets for sensitive resources
  - HIGH: Enable VPC flow logs
  - HIGH: Configure proper routing tables
  - HIGH: No direct internet access for private resources
  - MEDIUM: Use VPC endpoints for AWS services

#### Security Groups:
  - HIGH: No 0.0.0.0/0 inbound access
  - HIGH: Limit egress rules to specific CIDR ranges
  - HIGH: Document all rule justifications
  - LOW: Use security group references instead of CIDR ranges where possible

### Data Storage & Processing

#### S3 Buckets:
  - HIGH: Block public access using BlockPublicAccess.BLOCK_ALL
  - HIGH: Enable server access logging with dedicated logging bucket
  - HIGH: Enable server-side encryption (minimum S3_MANAGED)
  - HIGH: Enable enforceSSL
  - HIGH: Enable versioning
  - HIGH: Set appropriate removal policy
  - HIGH: Implement least privilege bucket policies
  - MEDIUM: Implement lifecycle policies
  - MEDIUM: Use KMS encryption for sensitive data

#### Databases:
  - HIGH: Deploy in private subnets
  - HIGH: Enable encryption at rest
  - HIGH: Configure backup retention
  - HIGH: Enable audit logging
  - HIGH: Implement secure security groups
  - LOW: Use multi-AZ deployment
  - LOW: Implement performance insights

### Compute Services

#### EC2/ECS/EKS:
  - HIGH: Use IMDSv2
  - HIGH: Implement least privilege IAM roles
  - HIGH: Enable container insights
  - HIGH: Configure logging
  - HIGH: Use private endpoints
  - HIGH: Implement secure security groups
  - LOW: Use auto-scaling
  - LOW: Implement monitoring and alerting

#### Lambda:
  - HIGH: Implement proper error handling
  - HIGH: Use Secrets Manager for sensitive environment variables
  - HIGH: Configure appropriate timeout and memory
  - HIGH: Enable X-Ray tracing
  - HIGH: Implement least privilege IAM roles
  - MEDIUM: Implement dead-letter queues
  - MEDIUM: Configure VPC access if needed

### API & Frontend Services

#### API Gateway:
  - HIGH: Enable access logging
  - HIGH: Implement request validation
  - HIGH: Use WAF for public endpoints
  - HIGH: Implement authentication
  - HIGH: Use HTTPS only
  - LOW: Use VPC endpoints when possible
  - LOW: Implement API key usage

#### CloudFront:
  - HIGH: Enable HTTPS only
  - HIGH: Configure security headers
  - HIGH: Use Origin Access Identity
  - HIGH: Enable access logging
  - HIGH: Configure proper cache behaviors
  - HIGH: Use WAF
  - LOW: Implement geo-restrictions if needed

### Security Services

#### IAM:
  - HIGH: Follow principle of least privilege
  - HIGH: Use service roles appropriately
  - HIGH: Implement resource policies
  - HIGH: Use permissions boundaries where appropriate
  - HIGH: Document any use of wildcard permissions
  - MEDIUM: Implement custom policies instead of AWS managed where possible
  - LOW: Use ABAC when appropriate

#### Secrets Management:
  - HIGH: Use Secrets Manager for sensitive data
  - HIGH: Implement automatic rotation where possible
  - HIGH: Use KMS for encryption
  - HIGH: Implement least privilege access policies
  - MEDIUM: Implement secret versioning
  - LOW: Use customer managed KMS keys

### Implementation Requirements

When implementing CDK constructs:
  - HIGH: Create custom constructs that enforce security requirements
  - HIGH: Implement proper error handling
  - HIGH: Use proper typing and documentation
  - HIGH: Include security unit tests
  - HIGH: Implement logging and monitoring
  - LOW: Create reusable security patterns
  - LOW: Implement custom validations