---
inclusion: manual
---

# Agentic AI Patterns and Workflows on AWS

When designing and implementing agentic AI systems, internalize these foundational patterns and workflow principles that guide technical decisions toward autonomous, scalable, and production-ready solutions. These patterns become the automatic decision-making frameworks that ensure your agentic AI architecture remains modular, intelligent, and aligned with enterprise goals.

## Core Agentic Principles

### Foundational Agent Design Principles
Every agentic system must be anchored in these three foundational principles:
- **Asynchronous**: Agents operate in loosely coupled, event-rich environments
- **Autonomy**: Agents act independently, without human or external control
- **Agency**: Agents act with purpose, on behalf of a user or system, toward specific goals

### Agent Core Building Blocks
The triangle of agent capabilities that enables agentic systems:
- **Perception**: Observe and understand the environment and context
- **Reason**: Make decisions based on goals, context, and available information
- **Action**: Execute decisions and interact with tools, services, and other agents

### Modular Design Language Principles
- **HIGH**: Design agents as accessible, operational, extensible, and production-ready components
- **HIGH**: Ensure agents can be composed and orchestrated across different contexts
- **HIGH**: Build agents that provide transparency and control across reasoning stages
- **HIGH**: Implement agents with clear interfaces for integration and testing
- **MEDIUM**: Consider agent specialization vs. generalization trade-offs

## Agent Patterns

### Basic Reasoning Agents
**When to use**: Single-step reasoning, classification, or summarization tasks
- **HIGH**: Implement stateless, lightweight agents for high composability
- **HIGH**: Use structured prompts to guide behavior and ensure consistency
- **HIGH**: Design for embedding into UI, CLI, APIs, and pipelines
- **HIGH**: Leverage for conversational Q&A, policy explanations, and decision guidance
- **MEDIUM**: Consider as foundation for more advanced agent patterns
- **Implementation**: Amazon Bedrock + API Gateway/Lambda + Parameter Store for prompts

### Retrieval-Augmented Generation (RAG) Agents
**When to use**: Tasks requiring external knowledge or domain-specific information
- **HIGH**: Ground agent decisions in up-to-date, factual information
- **HIGH**: Extend agent memory without fine-tuning models
- **HIGH**: Implement semantic search with vector databases for context retrieval
- **HIGH**: Use for enterprise knowledge assistants and compliance bots
- **HIGH**: Combine with basic reasoning for enhanced accuracy
- **Implementation**: Amazon Bedrock + Kendra/OpenSearch + S3 + Lambda orchestration

### Tool-Based Function-Calling Agents
**When to use**: Tasks requiring external API calls, calculations, or data access
- **HIGH**: Enable agents to act beyond language-only reasoning
- **HIGH**: Use schema-based prompting (OpenAPI, JSON schema) for tool selection
- **HIGH**: Implement dynamic tool selection based on task context
- **HIGH**: Design for virtual assistants and API-based knowledge workers
- **HIGH**: Support stateless or session-aware operations
- **Implementation**: Amazon Bedrock with function calling + Lambda + API Gateway

### Tool-Based Server Agents
**When to use**: Complex, stateful, or resource-intensive tool operations
- **HIGH**: Delegate tool execution to dedicated server environments
- **HIGH**: Enable multitool chaining and isolated execution
- **HIGH**: Support specialized reasoning with separate AI models
- **HIGH**: Use for orchestrating model chains and complex automation
- **HIGH**: Implement for DevOps assistants and multimodal tools
- **Implementation**: Amazon Bedrock + Lambda/ECS/Fargate + EventBridge + Step Functions

### Computer-Use Agents
**When to use**: Digital environment automation and UI interaction tasks
- **HIGH**: Combine LLM reasoning with visual language models (VLMs)
- **HIGH**: Implement memory management for persistent state
- **HIGH**: Enable multimodal reasoning with visual and textual inputs
- **HIGH**: Use for AI developers, testing automation, and accessibility tools
- **HIGH**: Design for autonomous sequence execution in multistep flows
- **Implementation**: Amazon Bedrock + EC2/Lambda + S3/DynamoDB + Rekognition

### Coding Agents
**When to use**: Software development assistance and automation
- **HIGH**: Integrate with developer environments (IDEs, CLIs)
- **HIGH**: Implement high-contextual awareness (IDE state, syntax trees)
- **HIGH**: Support iterative reasoning with goals and feedback
- **HIGH**: Use for code generation, refactoring, and test authoring
- **HIGH**: Enable paired programming and documentation assistance
- **Implementation**: Amazon Bedrock + Q Developer + Lambda/ECS + Cloud9/VS Code

### Speech and Voice Agents
**When to use**: Conversational AI across telephony, mobile, and embedded platforms
- **HIGH**: Integrate speech recognition, understanding, and synthesis
- **HIGH**: Support real-time streaming and telephony integration
- **HIGH**: Implement session awareness and memory handoff
- **HIGH**: Use for IVR systems, virtual receptionists, and accessibility tools
- **HIGH**: Enable multilingual I/O with STT and TTS support
- **Implementation**: Lex V2/Transcribe + Polly + Chime SDK/Connect + Bedrock + Lambda

### Workflow Orchestration Agents
**When to use**: Multistep tasks requiring coordination across distributed systems
- **HIGH**: Manage and coordinate tasks across subagents and services
- **HIGH**: Maintain execution context and adapt based on results
- **HIGH**: Support event-driven or scheduled execution patterns
- **HIGH**: Implement hierarchical or parallel task orchestration
- **HIGH**: Use for automation flows and multi-agent compositions
- **Implementation**: Amazon Bedrock + Step Functions + EventBridge + Lambda + DynamoDB

### Memory-Augmented Agents
**When to use**: Tasks requiring context across sessions and personalization
- **HIGH**: Implement short-term and long-term memory systems
- **HIGH**: Enable session continuity and goal persistence
- **HIGH**: Support contextual awareness based on evolving state
- **HIGH**: Use for conversational copilots and adaptive workflows
- **HIGH**: Implement personalization aligned with user preferences
- **Implementation**: DynamoDB/Aurora + OpenSearch + S3 + Lambda + Bedrock

### Simulation and Test-Bed Agents
**When to use**: Training, testing, and validation in controlled environments
- **HIGH**: Operate within virtualized or controlled environments
- **HIGH**: Support trial-and-error learning and policy refinement
- **HIGH**: Enable low-risk testing for behavior and edge cases
- **HIGH**: Use for reinforcement learning and safety validation
- **HIGH**: Implement emergent behavior analysis in multi-agent setups
- **Implementation**: RoboMaker/ECS + SageMaker + CloudWatch + S3/DynamoDB

### Observer and Monitoring Agents
**When to use**: System observation, pattern detection, and intelligent alerting
- **HIGH**: Passively observe systems without direct behavior initiation
- **HIGH**: Implement AI-driven correlation across distributed signals
- **HIGH**: Support audit, compliance, and real-time insights
- **HIGH**: Use for observability, security monitoring, and anomaly detection
- **HIGH**: Enable scalable and asynchronous monitoring patterns
- **Implementation**: EventBridge + CloudWatch + Kinesis + Lambda + Bedrock + SNS

### Multi-Agent Collaboration
**When to use**: Complex problems requiring specialized, collaborative agents
- **HIGH**: Design peer-level agents with specialized roles or skills
- **HIGH**: Enable emergent behavior through communication or negotiation
- **HIGH**: Support parallel processing of multifaceted problems
- **HIGH**: Use for research teams, software development, and scenario modeling
- **HIGH**: Implement deliberation, self-correction, and reflective iteration
- **Implementation**: Bedrock + SQS/EventBridge + DynamoDB/S3 + Step Functions

## LLM Workflows

### Prompt Chaining Workflows
**When to use**: Complex tasks requiring sequential reasoning steps
- **HIGH**: Decompose tasks into discrete LLM invocations
- **HIGH**: Pass intermediate outputs as structured input to follow-up steps
- **HIGH**: Implement transparency and control across reasoning stages
- **HIGH**: Use for multistep reasoning, research synthesis, and code generation
- **HIGH**: Enable external validation and enrichment between steps
- **Pattern**: Linear or branching chains orchestrated with Step Functions or Lambda

### Routing Workflows
**When to use**: Intent classification and specialized task delegation
- **HIGH**: Use classifier LLM to interpret intent and route requests
- **HIGH**: Delegate to specialized downstream tasks or agents
- **HIGH**: Support modular expansion of capabilities
- **HIGH**: Use for multidomain assistants and decision trees
- **HIGH**: Enable dynamic tool selection based on context
- **Pattern**: First-pass LLM dispatcher routing to distinct workflows

### Parallelization Workflows
**When to use**: Independent subtasks that can be processed concurrently
- **HIGH**: Break tasks into independent, non-sequential subtasks
- **HIGH**: Process multiple items simultaneously for efficiency
- **HIGH**: Aggregate and synthesize results programmatically
- **HIGH**: Use for document analysis, batch processing, and diverse perspective generation
- **HIGH**: Implement result alignment and validation at synthesis stage
- **Pattern**: Parallel LLM execution with Lambda/Fargate and Step Functions map state

### Orchestration Workflows
**When to use**: Complex, hierarchical, or multidisciplinary task coordination
- **HIGH**: Use central orchestrator for planning and task decomposition
- **HIGH**: Delegate subtasks to specialized worker agents
- **HIGH**: Support role-based behavior and team-like collaboration
- **HIGH**: Use for project management, software development, and enterprise processes
- **HIGH**: Enable modular responsibilities and specialized tuning
- **Pattern**: Meta-agent coordinating worker agents with distinct capabilities

### Evaluator and Reflect-Refine Workflows
**When to use**: Quality assurance and iterative improvement requirements
- **HIGH**: Implement feedback loops for output evaluation and refinement
- **HIGH**: Support self-reflection, optimization, and iterative improvements
- **HIGH**: Use separate LLMs for generation and evaluation
- **HIGH**: Apply to content generation, code review, and policy enforcement
- **HIGH**: Enable autonomous validation and alignment checking
- **Pattern**: Generation-evaluation-refinement cycles with convergence thresholds

## Agentic Workflow Patterns

### Prompt Chaining Saga Patterns
**Evolution from**: Traditional saga choreography to cognitive transaction management
- **HIGH**: Implement distributed, recoverable, and semantically coordinated workflows
- **HIGH**: Treat each prompt-response as atomic task with event emission
- **HIGH**: Enable rollback and revision mechanisms through reflective sequencing
- **HIGH**: Use for transactional reasoning with adaptive replanning
- **Implementation**: EventBridge + Step Functions + Bedrock + memory stores

### Routing Dynamic Dispatch Patterns
**Evolution from**: Static routing to semantic intent-based dispatching
- **HIGH**: Replace rigid rules with LLM-based semantic classification
- **HIGH**: Enable natural extensibility through new agent roles
- **HIGH**: Support broader input understanding and intelligent fallback
- **HIGH**: Use for flexible, adaptive task delegation
- **Implementation**: Bedrock classification + EventBridge + specialized agents

### Parallelization Scatter-Gather Patterns
**Evolution from**: Service fan-out to distributed cognitive processing
- **HIGH**: Distribute LLM tasks across multiple agents for parallel reasoning
- **HIGH**: Implement intelligent result synthesis and aggregation
- **HIGH**: Enable scalable, modular, and adaptive parallel processing
- **HIGH**: Use for high cognitive throughput requirements
- **Implementation**: SNS/SQS + Lambda + Bedrock + aggregation functions

### Saga Orchestration Patterns
**Evolution from**: Service orchestration to role-based agent coordination
- **HIGH**: Use LLM-powered orchestrator for semantic task delegation
- **HIGH**: Enable reasoning about goals and adaptive workflow management
- **HIGH**: Support modularity, adaptability, and introspection
- **HIGH**: Use for complex multistep agent workflows
- **Implementation**: Bedrock supervisor + Step Functions + worker agents

### Evaluator Reflect-Refine Loop Patterns
**Evolution from**: Static validation to semantic reflection and improvement
- **HIGH**: Transform validation into cognitive feedback loops
- **HIGH**: Enable self-improving agents through reasoning-based evaluation
- **HIGH**: Support continuous adaptation toward quality goals
- **HIGH**: Use for autonomous quality assurance and alignment
- **Implementation**: Bedrock generation + evaluation agents + Step Functions

## AWS Implementation Architecture

### Core Service Mapping
Match agentic components to appropriate AWS services:
- **LLM Reasoning**: Amazon Bedrock for agent logic, planning, and tool use
- **Tool Execution**: Lambda, ECS, SageMaker for hosting external agent tools
- **Memory and RAG**: Bedrock Knowledge Base, S3, OpenSearch for persistent memory
- **Orchestration**: Step Functions for multistep task and agent coordination
- **Event Routing**: EventBridge, SQS for decoupled inter-agent messaging
- **User Interface**: API Gateway, AppSync, SDKs for application entry points
- **Monitoring**: CloudWatch, X-Ray, OpenTelemetry for observability

### Deployment Patterns
Choose appropriate deployment models based on requirements:
- **Serverless**: Lambda + Bedrock for event-driven, scalable agents
- **Container-based**: ECS/Fargate for complex, stateful agent workloads
- **Managed**: Bedrock Agents for rapid deployment without infrastructure management
- **Hybrid**: Combination of managed and custom components for flexibility

### Security and Governance
- **HIGH**: Implement IAM roles and policies for least-privilege agent access
- **HIGH**: Use VPC endpoints for secure service communication
- **HIGH**: Enable CloudTrail logging for comprehensive audit trails
- **HIGH**: Implement encryption in transit and at rest for all agent data
- **HIGH**: Use Secrets Manager for secure credential management
- **MEDIUM**: Consider AWS Config for compliance monitoring

## Anti-Patterns to Avoid

### Agent Design Anti-Patterns
- **NEVER**: Build monolithic agents that try to handle all use cases
- **NEVER**: Ignore the three foundational principles (asynchronous, autonomy, agency)
- **NEVER**: Create agents without clear perception, reasoning, and action capabilities
- **NEVER**: Design agents without considering composability and modularity
- **NEVER**: Implement agents without proper error handling and graceful degradation

### Workflow Anti-Patterns
- **NEVER**: Use sequential processing when parallelization would improve efficiency
- **NEVER**: Implement static routing when semantic classification would be more flexible
- **NEVER**: Skip evaluation and refinement loops for quality-critical applications
- **NEVER**: Create tightly coupled workflows that can't adapt to changing requirements
- **NEVER**: Ignore intermediate result validation in complex reasoning chains

### Implementation Anti-Patterns
- **NEVER**: Deploy agents without proper monitoring and observability
- **NEVER**: Implement agentic systems without security and governance frameworks
- **NEVER**: Use inappropriate AWS services for specific agentic requirements
- **NEVER**: Create agents without considering scalability and performance requirements
- **NEVER**: Deploy production agents without proper lifecycle management

### Architectural Anti-Patterns
- **NEVER**: Build event-driven systems without proper error handling and retry logic
- **NEVER**: Implement multi-agent systems without clear communication protocols
- **NEVER**: Create agentic workflows without considering failure modes and recovery
- **NEVER**: Design systems without proper separation of concerns between agents
- **NEVER**: Ignore the evolution from traditional patterns to agentic equivalents

## Best Practices for Production

### Scalability and Performance
- **HIGH**: Design agents for horizontal scaling using serverless patterns
- **HIGH**: Implement caching strategies for frequently accessed knowledge
- **HIGH**: Use asynchronous processing for long-running agent tasks
- **HIGH**: Monitor and optimize LLM token usage and costs
- **HIGH**: Implement circuit breakers and rate limiting for external dependencies

### Reliability and Resilience
- **HIGH**: Design agents with graceful degradation capabilities
- **HIGH**: Implement comprehensive retry logic with exponential backoff
- **HIGH**: Use dead letter queues for failed agent interactions
- **HIGH**: Design for eventual consistency in multi-agent systems
- **HIGH**: Implement health checks and automated recovery mechanisms

### Observability and Debugging
- **HIGH**: Log all agent decisions, tool invocations, and reasoning steps
- **HIGH**: Implement distributed tracing across agent interactions
- **HIGH**: Monitor agent performance metrics and success rates
- **HIGH**: Create dashboards for agent behavior and system health
- **HIGH**: Implement alerting for anomalous agent behavior

These patterns and principles should become internalized technical wisdom that automatically guides your agentic AI system design decisions. They represent the foundational knowledge that distinguishes scalable, production-ready agentic AI implementations from experimental prototypes that cannot evolve with enterprise requirements.