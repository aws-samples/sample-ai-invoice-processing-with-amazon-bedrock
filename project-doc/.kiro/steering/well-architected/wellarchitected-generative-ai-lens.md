---
inclusion: manual
---

# AWS Well-Architected Generative AI Lens - Steering File

## Document Overview

The AWS Well-Architected Generative AI Lens is a comprehensive framework that extends the AWS Well-Architected Framework to 
address the unique considerations and opportunities presented by generative AI technologies. Published in April 2025, this 
document provides guidance and best practices for designing, deploying, and operating generative AI applications on AWS that 
are secure, efficient, scalable, and aligned with responsible AI principles. It helps architects, developers, and decision-
makers create solutions that maximize the potential of generative AI technologies while maintaining security, reliability, 
performance, cost-effectiveness, and sustainability.

## Key Topics

1. Generative AI Lifecycle
   • Scoping
   • Model selection
   • Model customization
   • Development and integration
   • Deployment
   • Continuous improvement

2. Data Architecture for generative AI systems

3. Operational Excellence in generative AI workloads
   • Model performance evaluation
   • Operational health monitoring
   • Observability
   • Lifecycle automation
   • Model customization

4. Security considerations for generative AI
   • Endpoint security
   • Response validation
   • Event monitoring
   • Prompt security
   • Excessive agency prevention
   • Data poisoning mitigation

5. Reliability in generative AI systems
   • Throughput quota management
   • Network reliability
   • Prompt remediation and recovery
   • Prompt management
   • Distributed availability
   • Distributed compute tasks

6. Performance Efficiency for generative AI
   • Performance evaluation processes
   • Model performance maintenance
   • High-performance compute optimization
   • Vector store optimization

7. Cost Optimization strategies
   • Model selection considerations
   • Pricing model selection
   • Cost-aware prompting
   • Vector store cost optimization
   • Agent workflow cost management

8. Sustainability in generative AI
   • Energy-efficient infrastructure
   • Sustainable data processing
   • Energy-efficient model selection

9. Responsible AI principles and practices

## Best Practices

### Operational Excellence

1. Model Performance Evaluation
   • **GENOPS01-BP01**: Periodically evaluate functional performance using stratified sampling and custom metrics
   • **GENOPS01-BP02**: Collect and monitor user feedback to surface performance issues

2. Operational Health Monitoring
   • **GENOPS02-BP01**: Monitor all application layers from user interactions to core model performance
   • **GENOPS02-BP02**: Monitor foundation model metrics including invocation counts, latency, token usage
   • **GENOPS02-BP03**: Implement rate limiting and throttling to prevent system overload

3. Observability
   • **GENOPS03-BP01**: Implement prompt template management with versioning and testing
   • **GENOPS03-BP02**: Enable tracing for agents and RAG workflows to enhance decision-making

4. Lifecycle Automation
   • **GENOPS04-BP01**: Automate generative AI application lifecycle with infrastructure as code (IaC)
   • **GENOPS04-BP02**: Follow GenAIOps practices to optimize the application lifecycle

5. Model Customization
   • **GENOPS05-BP01**: Learn when to customize models, starting with prompt engineering before more resource-intensive 
approaches

### Security

1. Endpoint Security
   • **GENSEC01-BP01**: Grant least privilege access to foundation model endpoints
   • **GENSEC01-BP02**: Implement private network communication between foundation models and applications
   • **GENSEC01-BP03**: Implement least privilege access permissions for foundation models accessing data stores
   • **GENSEC01-BP04**: Implement access monitoring to generative AI services and foundation models

2. Response Validation
   • **GENSEC02-BP01**: Implement guardrails to mitigate harmful or incorrect model responses

3. Event Monitoring
   • **GENSEC03-BP01**: Implement control plane and data access monitoring to generative AI services and foundation models

4. Prompt Security
   • **GENSEC04-BP01**: Implement a secure prompt catalog
   • **GENSEC04-BP02**: Sanitize and validate user inputs to foundation models

5. Excessive Agency Prevention
   • **GENSEC05-BP01**: Implement least privilege access and permissions boundaries for agentic workflows

6. Data Poisoning Mitigation
   • **GENSEC06-BP01**: Implement data purification filters for model training workflows

### Reliability

1. Throughput Quota Management
   • **GENREL01-BP01**: Scale and balance foundation model throughput as a function of utilization

2. Network Reliability
   • **GENREL02-BP01**: Implement redundant network connections between model endpoints and supporting infrastructure

3. Prompt Remediation and Recovery
   • **GENREL03-BP01**: Use logic to manage prompt flows and gracefully recover from failure
   • **GENREL03-BP02**: Implement timeout mechanisms on agentic workflows

4. Prompt Management
   • **GENREL04-BP01**: Implement a prompt catalog for versioning and management
   • **GENREL04-BP02**: Implement a model catalog for tracking model versions

5. Distributed Availability
   • **GENREL05-BP01**: Load-balance inference requests across all regions of availability
   • **GENREL05-BP02**: Replicate embedding data across all regions of availability
   • **GENREL05-BP03**: Verify that agent capabilities are available across all regions of availability

6. Distributed Compute Tasks
   • **GENREL06-BP01**: Design for fault-tolerance for high-performance distributed computation tasks

### Performance Efficiency

1. Performance Evaluation Processes
   • **GENPERF01-BP01**: Define a ground truth data set of prompts and responses
   • **GENPERF01-BP02**: Collect performance metrics from generative AI workloads

2. Model Performance Maintenance
   • **GENPERF02-BP01**: Load test model endpoints
   • **GENPERF02-BP02**: Optimize inference parameters to improve response quality
   • **GENPERF02-BP03**: Select and customize the appropriate model for your use case

3. High-Performance Compute Optimization
   • **GENPERF03-BP01**: Use managed solutions for model hosting and customization

4. Vector Store Optimization
   • **GENPERF04-BP01**: Test vector store features for latency and relevant performance
   • **GENPERF04-BP02**: Optimize vector sizes for your use case

### Cost Optimization

1. Model Selection
   • **GENCOST01-BP01**: Right-size model selection to optimize inference costs

2. Pricing Model Selection
   • **GENCOST02-BP01**: Balance cost and performance when selecting inference paradigms
   • **GENCOST02-BP02**: Optimize resource consumption to minimize hosting costs

3. Cost-Aware Prompting
   • **GENCOST03-BP01**: Reduce prompt token length
   • **GENCOST03-BP02**: Control model response length

4. Vector Store Cost Optimization
   • **GENCOST04-BP01**: Reduce vector length on embedded tokens

5. Agent Workflow Cost Management
   • **GENCOST05-BP01**: Create stopping conditions to control long-running workflows

### Sustainability

1. Energy-Efficient Infrastructure
   • **GENSUS01-BP01**: Implement auto scaling and serverless architectures to optimize resource utilization
   • **GENSUS01-BP02**: Use efficient model customization services

2. Sustainable Data Processing
   • **GENSUS02-BP01**: Optimize data processing and storage to minimize energy consumption

3. Energy-Efficient Models
   • **GENSUS03-BP01**: Leverage smaller models to reduce carbon footprint

## Guidelines and Recommendations

### Design Principles

1. Design for controlled autonomy: Implement comprehensive guardrails and boundaries that govern how AI systems operate, scale,
and interact.

2. Implement comprehensive observability: Monitor and measure specific aspects of your generative AI system, from security and 
performance to cost and environmental impact.

3. Optimize resource efficiency: Select and configure AI components based on empirical requirements rather than assumptions.

4. Establish distributed resilience: Design systems that remain operational despite component or regional failures.

5. Standardize resource management: Maintain centralized catalogs and controls for critical components like prompts, models, 
and access permissions.

6. Secure interaction boundaries: Protect and control data flows and system interfaces.

### Generative AI Lifecycle Recommendations

1. Scoping Phase:
   • Determine the relevance of generative AI in solving the problem
   • Consider risks and costs of investment
   • Establish success metrics
   • Determine technical and organizational feasibility
   • Develop a comprehensive risk profile

2. Model Selection Phase:
   • Evaluate different models based on specific requirements and use cases
   • Consider modality, size, accuracy, training data, pricing, context window, inference latency
   • Understand data usage policies by model hosting providers

3. Model Customization Phase:
   • Start with prompt engineering before more resource-intensive approaches
   • Consider RAG to customize model behavior without retraining
   • Use fine-tuning or continued pre-training when specific domain knowledge is required
   • Build custom foundation models only when absolutely necessary

4. Development and Integration Phase:
   • Implement the selected model into your workflow
   • Connect to relevant databases, data pipelines, and other applications
   • Implement security measures and responsible AI practices
   • Optimize the model for efficient real-time inference
   • Create APIs for application interaction
   • Build user-friendly interfaces

5. Deployment Phase:
   • Implement CI/CD pipelines
   • Use infrastructure as code principles
   • Maintain system uptime and resiliency
   • Validate compliance with security and privacy requirements

6. Continuous Improvement Phase:
   • Monitor model performance
   • Collect user feedback
   • Make iterative adjustments
   • Update training data
   • Experiment with new techniques

### Data Architecture Guidelines

1. Pre-training Data Architecture:
   • Manage and process vast, diverse datasets
   • Implement scalable infrastructure
   • Address data quality management
   • Implement efficient storage and retrieval
   • Consider data versioning and privacy protection

2. Fine-tuning Data Architecture:
   • Focus on smaller, more focused datasets
   • Implement flexible architectures
   • Address data selection and curation
   • Support rapid iteration and efficient preprocessing

3. RAG Data Architecture:
   • Implement low-latency data retrieval systems
   • Seamlessly integrate external knowledge with model inference
   • Address efficient indexing of knowledge bases
   • Maintain up-to-date information

### Responsible AI Guidelines

Focus on these key dimensions:
• **Fairness**: Consider impacts on different stakeholder groups
• **Explainability**: Understand and evaluate system outputs
• **Privacy and security**: Appropriately obtain, use, and protect data and models
• **Safety**: Prevent harmful system output and misuse
• **Controllability**: Implement mechanisms to monitor and steer AI system behavior
• **Veracity and robustness**: Achieve correct system outputs, even with unexpected inputs
• **Governance**: Incorporate best practices into the AI supply chain
• **Transparency**: Enable stakeholders to make informed choices

## Important Concepts

1. Foundation Models: Large language models pre-trained on vast amounts of data, serving as a foundation for downstream tasks 
and fine-tuning.

2. Generative AI: AI systems capable of generating new content, such as text, images, or code, based on input data or prompts.

3. Retrieval-Augmented Generation (RAG): A technique where a language model's output is augmented with relevant information 
retrieved from a corpus of documents to ground responses and reduce hallucination.

4. Prompt Engineering: The practice of carefully crafting prompts to guide language models to produce desired outputs.

5. Fine-tuning: The process of adapting a pre-trained model to a specific task or domain by training it on a smaller, task-
specific dataset.

6. Continuous Pre-training: The process of continuously updating a pre-trained model with new data to improve its performance 
and adapt to evolving domains or tasks.

7. Model Distillation: A technique for creating a smaller, more efficient model that mimics the behavior of a larger, more 
advanced model.

8. Hallucination: A phenomenon where a generative AI model produces outputs that are inconsistent, factually incorrect, or 
unrelated to the input prompt.

9. Vector Store: A specialized data store for efficient storage and retrieval of high-dimensional vector embeddings, often used
in semantic search and retrieval tasks.

10. Agents: AI systems that can perform tasks autonomously and interact with their environment to achieve specific goals.

11. Guardrails: Techniques to identify and mitigate undesirable model output, ranging from keyword identification to automated 
reasoning.

12. Prompt Catalog: A centralized repository for storing, managing, and versioning prompts used to interact with generative AI 
models.

13. Model Catalog: A centralized location to review models, model versions, and model cards.

14. GenAIOps: Operational practices and principles for managing the lifecycle of generative AI models, including model 
selection, data preparation, deployment, monitoring, and governance.

15. Data Poisoning: A type of exploit that occurs when data not meant for model training or customization is used, resulting in
potentially undesirable effects.

## Examples and Use Cases

1. RAG Implementation:
   • Using Amazon Bedrock Knowledge Bases to automate indexing and ingestion into vector databases
   • Orchestrating retrieval processes to ground model responses in factual information

2. Agent Workflows:
   • Using Amazon Bedrock Agents to break down user requests, gather information, and complete tasks
   • Implementing timeout mechanisms to prevent excessive resource consumption
   • Creating multi-agent collaboration with supervisor routing mode

3. Model Customization:
   • Fine-tuning a model for domain-specific language (medical or legal terminology)
   • Using continued pre-training to enhance a model's understanding of a specific domain
   • Implementing model distillation to create smaller, more efficient models

4. Prompt Management:
   • Creating a prompt catalog with Amazon Bedrock Prompt Management
   • Testing prompts against multiple foundation models
   • Versioning prompts and hyperparameter ranges

5. Security Implementation:
   • Implementing Amazon Bedrock Guardrails to filter harmful content
   • Creating least privilege IAM roles for agent workflows
   • Using AWS PrivateLink for private network communication

6. Performance Optimization:
   • Load testing model endpoints to determine baseline performance
   • Optimizing inference parameters like temperature, top_p, and top_k
   • Using Amazon SageMaker AI Inference Recommender to select optimal instance types

7. Cost Optimization:
   • Reducing prompt token length through engineering
   • Controlling model response length with hyperparameters
   • Implementing stopping conditions for agent workflows

8. Sustainability Practices:
   • Using serverless architectures like Amazon Bedrock for efficient resource utilization
   • Implementing auto-scaling for SageMaker AI endpoints
   • Leveraging smaller models or quantization techniques to reduce carbon footprint

## Cautions and Limitations

1. Model Limitations:
   • Foundation models can generate harmful, biased, or factually incorrect responses if guardrails are not implemented
   • Models are inherently non-deterministic, introducing an element of randomness
   • Performance can vary across different tasks and domains

2. Security Risks:
   • Prompt injection can introduce new content that impacts model behavior
   • Excessive agency in agents can lead to unintended actions
   • Data poisoning during training can result in undesirable model behavior

3. Performance Considerations:
   • Foundation models have limited throughput for inference requests
   • Latency may increase during periods of high demand
   • Vector store performance can create bottlenecks with cascading effects

4. Cost Implications:
   • Model costs vary greatly across providers, families, sizes, and hosting paradigms
   • Long prompts and responses increase token usage and costs
   • Agent workflows can become long-running and expensive if not properly controlled

5. Sustainability Challenges:
   • Training and customizing foundation models requires significant computational resources
   • Large models have higher energy consumption and carbon footprint
   • Inefficient data processing can lead to unnecessary resource usage

6. Implementation Warnings:
   • Over-provisioning resources leads to waste and higher costs
   • Under-provisioning can result in poor performance and reliability issues
   • Lack of monitoring can hide performance degradation or security issues

## Additional Resources

1. AWS Documentation:
   • Amazon Bedrock User Guide
   • Amazon SageMaker AI Documentation
   • Amazon Q Business and Amazon Q Developer Documentation
   • Amazon OpenSearch Service Documentation

2. AWS Well-Architected Framework Resources:
   • Machine Learning Lens
   • Data Analytics Lens
   • Operational Excellence Pillar
   • Security Pillar
   • Reliability Pillar
   • Performance Efficiency Pillar
   • Cost Optimization Pillar
   • Sustainability Pillar

3. Responsible AI Resources:
   • AWS Responsible AI Policy
   • Responsible AI Best Practices: Promoting Responsible and Trustworthy AI Systems
   • Amazon AI Fairness and Explainability Whitepaper
   • AWS Generative AI Best Practices Framework
   • AWS Responsible AI Landing Page

4. Tools and Libraries:
   • fmeval library for model evaluation
   • ragas for RAG evaluation
   • OpenLLMetry for tracing
   • Guardrails AI for implementing safety measures

5. AWS Events and Workshops:
   • AWS re:Invent sessions on generative AI
   • Amazon Bedrock Model Customization Workshop
   • SageMaker AI MLOps Workshop
   • Amazon SageMaker AI HyperPod recipes

6. External Resources:
   • OWASP Top 10 for LLMs
   • HuggingFace's Massive Text Embedding Benchmark (MTEB) Leaderboard
   • Prompt Engineering Guide
