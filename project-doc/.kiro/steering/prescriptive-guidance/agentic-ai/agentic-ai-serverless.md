---
inclusion: manual
---

# Building Serverless Architectures for Agentic AI on AWS

When building serverless architectures for agentic AI on AWS, internalize these foundational principles that guide technical decisions toward scalable, cost-effective, and production-ready intelligent systems. These architectural habits become the automatic decision-making patterns that ensure your serverless AI implementations remain elastic, secure, and aligned with business outcomes.

## Core Serverless AI Principles

### Event-Driven Architecture Foundation
- **HIGH**: Design all AI workflows as event-driven, reactive systems using Amazon EventBridge
- **HIGH**: Decouple AI components through asynchronous event patterns for independent scaling
- **HIGH**: Use events as triggers for AI perception, decision-making, and action cycles
- **HIGH**: Implement stateless, reactive services that respond to events without tight coupling
- **HIGH**: Enable real-time decisioning through immediate event-driven AI responses
- **MEDIUM**: Apply event-driven patterns to support autonomous agent environment interaction

### Serverless-First AI Service Selection
- **HIGH**: Prioritize fully managed, serverless AI services over infrastructure-heavy alternatives
- **HIGH**: Use Amazon Bedrock for foundation model access without infrastructure management
- **HIGH**: Leverage AWS Lambda for event-driven compute workloads and AI pre/post-processing
- **HIGH**: Implement Amazon SageMaker Serverless Inference for custom ML model deployment
- **HIGH**: Apply AWS Step Functions for orchestrating multi-step AI pipelines
- **NEVER**: Choose infrastructure-heavy solutions when serverless alternatives provide equivalent functionality

### Elastic Scalability and Cost Optimization
- **HIGH**: Design for automatic scaling based on demand without manual intervention
- **HIGH**: Implement pay-per-execution models with zero idle charges
- **HIGH**: Use tiered model selection (Amazon Nova Micro → Lite → Pro → Premier) based on complexity
- **HIGH**: Apply token optimization strategies to control Amazon Bedrock costs
- **HIGH**: Implement caching strategies for repeated AI operations and tool calls
- **MEDIUM**: Monitor and optimize cost allocation through comprehensive tagging strategies

## Orchestration Model Selection

### Rule-Based Orchestration with AWS Step Functions
**When to choose**: Deterministic workflows with well-defined paths and strong auditability requirements
- **HIGH**: Use for linear or branched control flows with explicit state transitions
- **HIGH**: Implement for workflows requiring fine-grained error handling and retries
- **HIGH**: Apply when audit trails and visual workflow representation are critical
- **HIGH**: Leverage SDK integration capabilities to reduce Lambda function overhead
- **HIGH**: Use for multi-stage AI pipelines with heterogeneous service integration
- **MEDIUM**: Consider for workflows where business rules are stable and well-understood

### AI-Native Orchestration with Amazon Bedrock Agents
**When to choose**: Dynamic, goal-driven workflows requiring semantic flexibility and natural language interaction
- **HIGH**: Implement for unstructured user input requiring intent interpretation
- **HIGH**: Use when tool selection should be determined dynamically at runtime
- **HIGH**: Apply for contextual grounding through knowledge bases and enterprise data
- **HIGH**: Leverage for goal-directed user experiences with minimal developer maintenance
- **HIGH**: Implement for conversational interfaces requiring autonomous decision-making
- **MEDIUM**: Consider when workflow logic should adapt based on context and user intent

### Hybrid Orchestration Strategy
- **HIGH**: Combine Step Functions for controlled processes with Bedrock Agents for flexible interaction
- **HIGH**: Use Step Functions for backend automation and Bedrock Agents for user-facing intelligence
- **HIGH**: Implement event-driven activation for both orchestration models through EventBridge
- **HIGH**: Design clear boundaries between deterministic and AI-native orchestration components
- **MEDIUM**: Enable seamless handoffs between rule-based and AI-native orchestration patterns

## Model Execution Strategies

### Amazon Bedrock Foundation Model Selection
**When to choose**: Generative AI tasks, conversational assistants, and semantic reasoning
- **HIGH**: Use Amazon Nova models for multimodal intelligence across text, image, and video
- **HIGH**: Leverage Amazon Nova Micro for real-time, low-latency user experience feedback
- **HIGH**: Apply Amazon Nova Pro for enterprise assistants with proprietary data grounding
- **HIGH**: Implement Amazon Nova Premier for sophisticated reasoning and model distillation
- **HIGH**: Use token-based billing for predictable cost modeling and optimization
- **MEDIUM**: Consider fine-tuning capabilities for task-specific model optimization

### Amazon SageMaker Serverless Inference Selection
**When to choose**: Custom-trained models for predictive analytics and structured data processing
- **HIGH**: Use for traditional ML models (classification, regression, forecasting)
- **HIGH**: Implement for custom model architectures requiring full training control
- **HIGH**: Apply for structured input processing and numerical predictions
- **HIGH**: Leverage for domain-specific models trained on proprietary datasets
- **HIGH**: Use pay-per-inference model with automatic scaling capabilities
- **MEDIUM**: Consider for integration with existing SageMaker training pipelines

### Model Selection Decision Matrix
Choose appropriate execution strategy based on requirements:
- **Semantic flexibility and generative tasks**: Amazon Bedrock foundation models
- **Proprietary model logic and structured predictions**: SageMaker Serverless Inference
- **Rapid iteration with zero-shot capabilities**: Amazon Bedrock with prompt engineering
- **Full control over model architecture and training**: SageMaker with custom containers
- **Multimodal understanding and generation**: Amazon Nova models through Bedrock

## Grounding and RAG Implementation

### Amazon Bedrock Knowledge Bases Strategy
- **HIGH**: Implement RAG patterns for grounding foundation models in enterprise data
- **HIGH**: Use automated embedding and semantic search across enterprise documents
- **HIGH**: Integrate with Amazon S3, Confluence, Salesforce, and SharePoint data sources
- **HIGH**: Apply hybrid retrieval techniques with Amazon Nova models for optimal grounding
- **HIGH**: Implement grounding without fine-tuning through context window injection
- **MEDIUM**: Use vector stores (Aurora, OpenSearch, Neptune) for pre-embedded indexes

### Guardrails and Safety Implementation
- **HIGH**: Apply Amazon Bedrock Guardrails for content filtering and policy enforcement
- **HIGH**: Implement denial topics to block inappropriate response categories
- **HIGH**: Use prompt inspection to identify and strip sensitive inputs
- **HIGH**: Apply user-level access control through AWS IAM integration
- **HIGH**: Implement session context constraints to prevent model drift
- **NEVER**: Deploy production agents without comprehensive guardrails and safety controls

### Automated Reasoning Enhancement
- **HIGH**: Enable synthesis and comparison across multiple retrieved documents
- **HIGH**: Implement multi-hop logic connecting facts across document sections
- **HIGH**: Use evidence-based responses with citations and justification
- **HIGH**: Apply decision-making capabilities based on rules and preferences
- **HIGH**: Implement reflection-evaluation loops for expert reasoning patterns
- **MEDIUM**: Use prompt chaining and multi-agent orchestration for complex reasoning

## Edge AI and Global Distribution

### Lambda@Edge for Global Inference
**When to choose**: Global web personalization and ultra-low latency requirements
- **HIGH**: Implement for ecommerce personalization and dynamic content delivery
- **HIGH**: Use for media streaming recommendations and regional policy adaptation
- **HIGH**: Apply for multilingual user experiences with location-based content
- **HIGH**: Leverage for marketing campaign customization at CDN edge locations
- **HIGH**: Integrate with Amazon Bedrock through asynchronous routing and caching
- **MEDIUM**: Consider for hyper-personalized, AI-driven front-end delivery

### AWS IoT Greengrass for Device Intelligence
**When to choose**: Local inference requirements with offline capabilities
- **HIGH**: Use for manufacturing defect detection without cloud round trips
- **HIGH**: Implement for healthcare monitoring in intermittent connectivity environments
- **HIGH**: Apply for agriculture and energy monitoring using anomaly detection
- **HIGH**: Leverage for industrial controllers and smart appliance intelligence
- **HIGH**: Enable secure over-the-air model updates and configuration management
- **MEDIUM**: Consider for scenarios requiring data sovereignty and local processing

### Tiered Edge AI Architecture
Implement intelligent decision-making at appropriate layers:
- **Device edge (IoT Greengrass)**: On-device, offline-capable AI logic and sensor processing
- **Network edge (Lambda@Edge)**: Content personalization and lightweight AI near users
- **Cloud core (Bedrock/SageMaker)**: Heavy AI inference, orchestration, and RAG pipelines

## Architectural Design Patterns

### Five-Layer Serverless AI Architecture
Implement consistent layered architecture across all serverless AI systems:

#### Event Trigger/Interface Layer
- **HIGH**: Use Amazon API Gateway for user input through REST or WebSocket APIs
- **HIGH**: Implement Amazon EventBridge for internal and external event routing
- **HIGH**: Apply Amazon S3 triggers for document uploads and media file processing
- **HIGH**: Use Amazon Kinesis for streaming events at scale
- **MEDIUM**: Implement schema registries for event format validation and consistency

#### Processing Layer
- **HIGH**: Use AWS Lambda for stateless, event-driven data transformation
- **HIGH**: Implement input validation, formatting, and metadata enrichment
- **HIGH**: Apply language detection and PII scanning before AI processing
- **HIGH**: Use Amazon Comprehend for preprocessing entity recognition and sentiment
- **MEDIUM**: Implement routing logic based on data attributes and user context

#### Inference Layer
- **HIGH**: Deploy Amazon Bedrock for foundation model inference and agent orchestration
- **HIGH**: Use SageMaker Serverless Inference for custom ML model execution
- **HIGH**: Implement RAG integration through Amazon Bedrock Knowledge Bases
- **HIGH**: Apply multi-model inference for complex reasoning workflows
- **MEDIUM**: Use model selection abstraction for dynamic routing and optimization

#### Post-Processing/Decisioning Layer
- **HIGH**: Implement Lambda functions for response formatting and validation
- **HIGH**: Apply conditional logic based on model confidence and business rules
- **HIGH**: Use Amazon SNS and EventBridge for downstream event emission
- **HIGH**: Implement escalation logic for low-confidence or policy violations
- **MEDIUM**: Apply cross-validation against real-time data sources

#### Output/Storage Layer
- **HIGH**: Use Amazon S3 for inference logs, summaries, and generated content
- **HIGH**: Implement Amazon DynamoDB for low-latency session-specific outputs
- **HIGH**: Apply Amazon OpenSearch Service for structured output indexing and search
- **HIGH**: Use API Gateway and WebSocket APIs for real-time response delivery
- **MEDIUM**: Implement data lakes and retraining pipelines for continuous improvement

## Implementation Best Practices

### Infrastructure as Code (IaC) Strategy
- **HIGH**: Use AWS CDK for dynamic infrastructure generation and construct reuse
- **HIGH**: Implement AWS CloudFormation for audit-aligned, declarative deployments
- **HIGH**: Apply AWS SAM for serverless-optimized application deployment
- **HIGH**: Version control all infrastructure components and AI configurations
- **HIGH**: Implement environment-specific stacks with parameterization and tagging
- **NEVER**: Deploy serverless AI systems without comprehensive IaC implementation

### Prompt and Agent Lifecycle Management
- **HIGH**: Version-control prompts and agent configurations as critical code assets
- **HIGH**: Use prompt templates with variable injection for maintainability
- **HIGH**: Implement prompt governance workflows with review and testing processes
- **HIGH**: Track model versions and provider updates for reproducibility
- **HIGH**: Log all prompts, parameters, and model responses for audit and improvement
- **MEDIUM**: Establish confidence thresholds and fallback behavior for safety

### Testing and Validation Strategy
- **HIGH**: Implement unit tests for Lambda transformation and formatting logic
- **HIGH**: Create prompt tests using golden inputs to catch drift and degradation
- **HIGH**: Validate agent tool invocation logic and parameter mapping
- **HIGH**: Test workflow integration across multi-stage orchestration pipelines
- **HIGH**: Apply schema validation and contract tests for AI output formats
- **MEDIUM**: Implement human-in-the-loop evaluations for high-trust domains

### Observability and Monitoring Implementation
- **HIGH**: Use Amazon CloudWatch Logs for comprehensive logging across all components
- **HIGH**: Implement CloudWatch metrics for custom KPIs and performance tracking
- **HIGH**: Apply AWS X-Ray for distributed tracing across serverless workflows
- **HIGH**: Use Amazon Bedrock agent trace and model invocation logging
- **HIGH**: Implement structured logging with consistent schema and correlation IDs
- **MEDIUM**: Create automated dashboards and anomaly detection for operational insights

## Security and Governance Framework

### Identity and Access Management
- **HIGH**: Implement least-privilege IAM roles for all Lambda functions and agents
- **HIGH**: Scope Amazon Bedrock agent tool permissions to required functions only
- **HIGH**: Use fine-grained IAM policies for service-to-service communication
- **HIGH**: Apply role-based access control for prompt and tool configuration
- **HIGH**: Implement audit logging of tool calls and prompt history
- **NEVER**: Deploy serverless AI without comprehensive IAM security controls

### Data Protection and Compliance
- **HIGH**: Encrypt all sensitive data in transit and at rest using AWS KMS
- **HIGH**: Implement data classification and tagging for compliance requirements
- **HIGH**: Apply prompt validation and injection protection mechanisms
- **HIGH**: Use output filtering and post-validation for generated content
- **HIGH**: Ensure data residency and regional isolation for regulated industries
- **MEDIUM**: Implement data retention and deletion policies for AI memory systems

### Governance and Audit Controls
- **HIGH**: Maintain comprehensive audit trails for all AI decisions and actions
- **HIGH**: Implement configuration drift detection and compliance monitoring
- **HIGH**: Use AWS CloudTrail for API-level access and invocation history
- **HIGH**: Apply AWS Config for policy drift and misconfiguration detection
- **HIGH**: Implement compliance integration with frameworks (ISO, SOC, NIST, HIPAA)
- **MEDIUM**: Use Amazon Macie for PII detection in logs and stored data

## Cost Optimization Strategies

### Tiered Model Selection and Routing
- **HIGH**: Route low-complexity prompts to Amazon Nova Micro for cost efficiency
- **HIGH**: Escalate to higher-tier models only when confidence thresholds aren't met
- **HIGH**: Implement dynamic model selection based on prompt complexity analysis
- **HIGH**: Use batch processing for inference operations when real-time isn't required
- **HIGH**: Apply caching strategies for repeated tool calls and knowledge base queries
- **MEDIUM**: Monitor model performance vs. cost trade-offs for optimization opportunities

### Token and Prompt Optimization
- **HIGH**: Enforce maximum prompt size limits and use concise phrasing
- **HIGH**: Trim verbose model completions and format responses efficiently
- **HIGH**: Control RAG retrieval scope using metadata filters and Top K ranking
- **HIGH**: Implement prompt templates to reduce token duplication
- **HIGH**: Use structured confidence thresholds to limit unnecessary retries
- **MEDIUM**: Apply prompt compression techniques for large context scenarios

### Workflow and Infrastructure Optimization
- **HIGH**: Use Step Functions for aggregation rather than atomic state micromanagement
- **HIGH**: Implement async response handling to avoid blocking compute resources
- **HIGH**: Apply cost allocation tags for visibility by application, team, and environment
- **HIGH**: Use reserved or provisioned concurrency only for predictable, high-volume workloads
- **HIGH**: Monitor and alert on cost thresholds using AWS Budgets and Cost Explorer
- **MEDIUM**: Implement automated cost optimization based on usage patterns and performance metrics

## Anti-Patterns to Avoid

### Architecture Anti-Patterns
- **NEVER**: Build monolithic AI systems when serverless alternatives provide better scalability
- **NEVER**: Use synchronous, blocking patterns when asynchronous event-driven alternatives exist
- **NEVER**: Implement custom infrastructure management when managed services are available
- **NEVER**: Create tightly coupled AI components that prevent independent scaling and evolution
- **NEVER**: Ignore cost optimization strategies in favor of over-provisioned resources

### Orchestration Anti-Patterns
- **NEVER**: Use AI-native orchestration for deterministic workflows better suited to Step Functions
- **NEVER**: Implement rule-based orchestration for dynamic, context-dependent user interactions
- **NEVER**: Create hybrid orchestration without clear boundaries and handoff mechanisms
- **NEVER**: Deploy orchestration systems without comprehensive error handling and retry logic
- **NEVER**: Ignore the event-driven activation patterns that enable serverless scalability

### Model Execution Anti-Patterns
- **NEVER**: Choose foundation models for structured prediction tasks better suited to custom ML
- **NEVER**: Use custom ML models for generative tasks better served by foundation models
- **NEVER**: Implement model selection without considering cost, latency, and accuracy trade-offs
- **NEVER**: Deploy models without proper grounding, guardrails, and safety controls
- **NEVER**: Ignore token optimization and cost management in foundation model usage

### Security and Governance Anti-Patterns
- **NEVER**: Deploy serverless AI without comprehensive IAM security and access controls
- **NEVER**: Implement AI systems without proper data protection and compliance measures
- **NEVER**: Create AI workflows without audit trails and governance frameworks
- **NEVER**: Deploy production AI without guardrails, safety controls, and human oversight options
- **NEVER**: Ignore prompt injection protection and output validation requirements

These principles should become internalized architectural wisdom that automatically guides your serverless AI implementation decisions. They represent the foundational habits that distinguish scalable, production-ready serverless AI systems from experimental prototypes that cannot handle enterprise requirements for security, compliance, cost control, and operational excellence.