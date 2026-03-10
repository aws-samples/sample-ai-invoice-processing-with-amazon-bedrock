---
inclusion: manual
---

# AWS Well-Architected Framework - Serverless Applications Lens Steering Guide

## Document Overview

This document presents the Serverless Applications Lens for the AWS Well-Architected Framework. It focuses on how to design, 
deploy, and architect serverless application workloads in the AWS Cloud, covering best practices and strategies for building 
well-architected serverless systems. The lens examines common serverless application scenarios and identifies key elements to 
ensure workloads are architected according to best practices across the six pillars of the Well-Architected Framework: 
operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

## Key Topics

1. Serverless Architecture Components
   • Compute layer (Lambda, API Gateway, Step Functions)
   • Data layer (DynamoDB, S3, OpenSearch Service, AppSync)
   • Messaging and streaming layer (SNS, Kinesis, Data Firehose)
   • User management and identity layer (Cognito)
   • Edge layer (CloudFront)
   • Systems monitoring and deployment (CloudWatch, X-Ray, SAM)

2. Deployment Approaches
   • All-at-once deployments
   • Blue/green deployments
   • Canary deployments
   • Lambda version control

3. Common Serverless Scenarios
   • RESTful microservices
   • Alexa skills
   • Mobile backend
   • Streaming processing
   • Web application
   • Event-driven architectures

4. Well-Architected Pillars Applied to Serverless
   • Operational excellence
   • Security
   • Reliability
   • Performance efficiency
   • Cost optimization
   • Sustainability

## Best Practices

### Design Principles

1. Speedy, simple, singular
   • Functions should be concise, short, single-purpose
   • Transactions should be efficiently cost-aware with faster initiations preferred

2. Think concurrent requests, not total requests
   • Serverless applications take advantage of the concurrency model
   • Design tradeoffs should be evaluated based on concurrency

3. Share nothing
   • Function runtime environment and infrastructure are short-lived
   • Use persistent storage for highly durable requirements

4. Assume no hardware affinity
   • Use code or dependencies that are hardware-agnostic
   • Underlying infrastructure may change

5. Orchestrate with state machines, not functions
   • Use state machines to orchestrate transactions and communication flows
   • Avoid chaining Lambda executions within code

6. Use events to trigger transactions
   • Events allow for just-in-time processing and lean service design
   • Design for asynchronous event behavior

7. Design for failures and duplicates
   • Operations must be idempotent
   • Include appropriate retries for downstream calls

### Operational Excellence

1. Metrics and Alerts
   • Understand CloudWatch metrics and dimensions for every AWS service
   • Configure alarms at both individual and aggregated levels
   • Use Lambda Powertools or CloudWatch Embedded Metric Format (EMF) for custom metrics
   • Focus on four types of metrics:
     • Business metrics (KPIs)
     • Customer experience metrics
     • System metrics
     • Operational metrics

2. Logging
   • Standardize application logging with structured logging (JSON format)
   • Include correlation IDs and pass them to downstream systems
   • Use appropriate logging levels and sampling mechanisms
   • Consider Lambda Logs API for sending logs to locations other than CloudWatch

3. Distributed Tracing
   • Enable active tracing with AWS X-Ray
   • Use annotations and subsegments to identify performance statistics
   • Implement retries, backoffs, and circuit breakers for integration points

4. Testing
   • Develop robust testing strategies (unit, integration, acceptance tests)
   • Use real services for integration tests
   • Consider Lambda function memory usage and VPC IP address space during testing

5. Deployment
   • Use infrastructure as code and version control
   • Isolate development and production stages in separate environments
   • Use serverless frameworks like AWS SAM or Serverless Framework
   • Create separate stages using CI/CD pipelines
   • Favor safe deployments over all-at-once systems

### Security

1. API Authentication and Authorization
   • Use one of the five mechanisms to authorize API calls:
     • AWS_IAM authorization
     • Amazon Cognito user pools
     • API Gateway Lambda authorizer
     • Resource policies
     • Mutual TLS authentication
   • Avoid using API Keys for authorization (use for tracking consumer usage only)
   • Don't pass credentials through query string parameters or headers

2. Access Control
   • Follow least-privileged access for Lambda functions
   • Create smaller functions with scoped activities
   • Avoid sharing IAM roles across multiple Lambda functions

3. Data Protection
   • Encrypt sensitive data at all layers
   • Avoid sending, logging, or storing unencrypted sensitive data
   • Use AWS Secrets Manager for storing secrets
   • Enable code signing for Lambda to protect against unauthorized changes

4. Network Security
   • Configure Lambda functions to access VPC resources when needed
   • Use VPC endpoints for service-to-service communication
   • Consider API Gateway private endpoints for restricting access

### Reliability

1. Throttling and Concurrency Control
   • Enable throttling at the API level to enforce access patterns
   • Return appropriate HTTP status codes (e.g., 429 for throttling)
   • Use API keys with usage plans for granular throttling
   • Implement concurrency controls for Lambda functions to protect:
     • Sensitive backend systems with scaling limitations
     • Against recursive invocations
     • Database connection pool restrictions
     • Critical path services

2. Resilience
   • Manage transaction, partial, and intermittent failures
   • Design applications to process duplicate events idempotently
   • Use state machines for long-running transactions
   • Consider scaling patterns at burst rates

3. Error Handling
   • Use dead-letter queues (DLQ) to retain, investigate, and retry failed transactions
   • Configure Lambda error handling controls (maximum retry attempts, maximum record age, etc.)
   • Review and tune AWS SDK back-off and retry mechanisms
   • Use Step Functions to minimize custom try/catch logic
   • Handle partial failures in non-atomic operations

### Performance Efficiency

1. Service Selection and Configuration
   • API Gateway: Use Edge endpoints for geographically dispersed customers, Regional for regional customers
   • Lambda: Test different memory settings, optimize static initialization, consider provisioned concurrency
   • Step Functions: Test Standard and Express Workflows, consider per-second rates
   • DynamoDB: Use on-demand for unpredictable traffic, provisioned for consistent traffic
   • Kinesis: Use enhanced fan-out for multiple consumers, extended batch window for low volume

2. Lambda Optimization
   • Set timeouts a few seconds higher than average execution
   • Use container reuse and global scope for one-off expensive operations
   • Consider connection pooling with Amazon RDS Proxy
   • Break down monolithic functions into microservices
   • Use API Gateway native routing instead of web frameworks

3. Asynchronous Processing
   • Implement event-driven architectures to limit consumer wait cycles
   • Decouple user experience with asynchronous calls
   • Use Step Functions for long-running transactions
   • Consider WebSockets or polling for status updates

### Cost Optimization

1. Resource Optimization
   • Use AWS Compute Optimizer for Lambda memory size recommendations
   • Consider ARM/Graviton processors for cost and performance benefits
   • Optimize logging ingestion and storage costs
   • Set appropriate log retention periods

2. Service Selection for Cost
   • Use VPC endpoints instead of NAT/Internet Gateways when possible
   • Choose appropriate DynamoDB capacity mode (on-demand vs. provisioned)
   • Select appropriate Step Functions workflow type (Standard vs. Express)
   • Use direct service integrations instead of Lambda when possible

3. Code Optimization
   • Use global variables to maintain connections
   • Consider connection pooling with RDS Proxy
   • Use Athena SQL queries or S3 Select to retrieve only needed data

## Guidelines and Recommendations

### Deployment Approaches

1. All-at-once deployments
   • Low-effort but higher risk for rollback
   • Usually causes downtime
   • Best for non-critical environments (development)

2. Blue/green deployments
   • Near zero-downtime releases
   • Traffic shifted to new environment while keeping old environment warm
   • Good for production changes
   • Use CloudWatch high-resolution metrics for quick rollback if needed

3. Canary deployments
   • Deploy percentage of requests to new code
   • Monitor for errors, degradations, or regressions
   • Use Lambda function aliases with AWS CodeDeploy
   • Control gradual deployments with pre/post-traffic hooks

### Lambda Version Control

1. Use versioning to maintain immutable versions of functions
2. Use Lambda function aliases to activate different variations in development workflow
3. Point API Gateway integrations to alias ARNs rather than specific versions

### API Gateway Configuration

1. Use API Gateway logging to understand consumer access behaviors
2. Enable request validation to ensure requests adhere to JSON-schema
3. Consider content encoding to compress payload responses
4. For private resources, use API Gateway private integration over Lambda in VPC

### Lambda Function Configuration

1. Configure memory based on performance testing results
2. Set appropriate timeout values based on function execution patterns
3. Use provisioned concurrency for functions that need to scale without latency fluctuations
4. Configure VPC access only when necessary
5. Use Lambda extensions judiciously as they impact performance and resources

### DynamoDB Configuration

1. Use on-demand tables unless performance tests exceed current quotas
2. Follow best practices when creating tables (well-distributed hash key, indexes)
3. Use DynamoDB Accelerator (DAX) for skills heavy on reads
4. Consider Time to Live (TTL) feature to expire unwanted data

### Step Functions Usage

1. Use Standard Workflows for long-running, durable, and auditable workflows
2. Use Express Workflows for high-volume, event-processing workloads
3. Avoid polling loops by using Callbacks or .sync Service integration
4. Ensure Express Workflow state machine logic is idempotent
5. Consider combining Standard and Express Workflows for optimal cost and functionality

### Event Processing

1. For Kinesis streams:
   • Configure appropriate batch size and batch window
   • Use enhanced fan-out for multiple consumers
   • Consider parallelization factor to increase concurrency
   • Monitor IteratorAge metric for latency estimation

2. For asynchronous processing:
   • Use event filtering to reduce unnecessary Lambda invocations
   • Configure appropriate error handling and retry mechanisms
   • Consider using tumbling windows for time-based aggregations

## Important Concepts

1. Serverless Computing Model
   • Pay-per-value pricing model
   • Scale based on demand
   • No server management required
   • Short-lived execution environments

2. Event-Driven Architecture
   • Asynchronous, message-driven communication
   • Components respond to events rather than direct calls
   • Enables loose coupling between services
   • Consists of event sources, event routers, and event destinations

3. Idempotency
   • Operations can be applied multiple times without changing the result
   • Critical for handling duplicate events and retries
   • Essential for reliable serverless applications

4. Cold Start
   • Initial startup delay when a new Lambda execution environment is created
   • Impacts performance and user experience
   • Can be mitigated with provisioned concurrency

5. Concurrency Model
   • Lambda scales by creating multiple execution environments
   • Account-level and function-level concurrency limits apply
   • Throttling occurs when concurrency limits are exceeded

6. Statelessness
   • Functions should not rely on in-memory state between invocations
   • State should be externalized to persistent storage
   • Enables horizontal scaling and resilience

## Examples and Use Cases

### RESTful Microservices

1. Customers leverage microservices by making HTTP API calls
2. Amazon API Gateway hosts RESTful HTTP requests and responses
3. AWS Lambda contains business logic to process incoming API calls
4. Amazon DynamoDB persistently stores microservices data

### Alexa Skills

1. Alexa users interact with skills via voice on Alexa-enabled devices
2. Alexa Service performs Speech Language Understanding processing
3. Alexa Skills Kit integrates with AWS Lambda
4. Lambda function processes requests and builds speech responses
5. DynamoDB persists user state and sessions

### Mobile Backend

1. Amazon Cognito manages user authentication and identity
2. Mobile users interact with backend via GraphQL operations
3. AWS AppSync hosts GraphQL requests and responses
4. Data sources include DynamoDB, OpenSearch Service, or Lambda
5. Amazon Pinpoint captures analytics and delivers targeted messages

### Streaming Processing

1. Data producers use Kinesis Producer Library to send streaming data
2. Amazon Kinesis stream collects and processes real-time data
3. AWS Lambda consumes the stream and processes data
4. Processed data is stored in DynamoDB
5. Business users access insights via reporting interface

### Web Application

1. Amazon Cognito provides user management
2. CloudFront accelerates content delivery
3. Amazon S3 hosts static assets
4. API Gateway serves as secure HTTPS endpoint
5. Lambda provides CRUD operations
6. DynamoDB stores application data

### Event-Driven Architecture

1. Event sources (AWS services, microservices, SaaS applications)
2. Amazon EventBridge routes events based on rules
3. Event destinations (Lambda, Step Functions, SQS, etc.)

## Cautions and Limitations

1. API Gateway Throttling
   • API Keys are not a security mechanism and should not be used for authorization
   • Only use API Keys to track consumer usage

2. Lambda Function Limitations
   • Maximum execution duration of 15 minutes
   • Cold starts can impact performance
   • Memory settings affect CPU, network, and storage IOPS allocation
   • Lambda extensions impact performance and resource usage

3. Step Functions Limitations
   • Standard Workflows have a maximum duration of 1 year
   • Express Workflows have a maximum duration of 5 minutes
   • State transitions are throttled using a token bucket scheme

4. Security Considerations
   • Avoid passing credentials through query string parameters or headers
   • Don't log or store unencrypted sensitive data
   • Be cautious with API Gateway Access Logs as they might contain sensitive data

5. Concurrency and Scaling
   • Lambda concurrency quotas are applied per account and Region
   • One function can consume concurrency such that other functions are throttled
   • API Gateway and Lambda have different limits for steady and burst request rates

6. Error Handling
   • Non-atomic operations like PutRecords (Kinesis) and BatchWriteItem (DynamoDB) can have partial failures
   • Duplicate records may occur in streaming applications
   • Asynchronous calls that fail should be captured and retried to prevent data loss

## Additional Resources

### Documentation and Blogs
• AWS SAM
• API Gateway stage variables
• Lambda environment variables
• Powertools for AWS Lambda (Python, TypeScript, Java, .NET)
• CloudWatch Embedded Metric Format libraries
• Operating Lambda: Logging and custom metrics
• Operating Lambda: Using CloudWatch Logs Insights
• X-Ray latency distribution
• Troubleshooting Lambda-based applications with X-Ray
• System Manager (SSM) Parameter Store
• AWS AppConfig integration with Lambda Extensions
• AWS Secrets Manager
• Serverless CI/CD for the Enterprise on AWS

### Whitepapers
• Security Overview of AWS Lambda
• OWASP Top Ten
• OWASP Secure Coding Best Practices
• Implementing Microservices on AWS
• Disaster Recovery of Workloads on AWS
• Optimizing Enterprise Economics with Serverless Architectures

### Third-party Tools
• Serverless Developer Tools page including third-party frameworks/tools
• Stelligent: CodePipeline Dashboard for operational metrics
• OWASP Vulnerability Dependency Check
• Snyk – Commercial Vulnerability DB and Dependency Check
• Hashicorp Vault with Lambda & API Gateway
