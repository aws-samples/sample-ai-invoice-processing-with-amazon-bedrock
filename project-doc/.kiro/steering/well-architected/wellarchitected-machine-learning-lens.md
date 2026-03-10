---
inclusion: manual
---

# AWS Well-Architected Machine Learning Lens - Steering Guide

## Document Overview

The AWS Well-Architected Machine Learning Lens provides architectural best practices for designing and operating machine 
learning (ML) workloads on AWS. It extends the AWS Well-Architected Framework by addressing the specific challenges of ML 
workloads across the six pillars: operational excellence, security, reliability, performance efficiency, cost optimization, 
and sustainability. The document guides organizations through the entire ML lifecycle, from business goal identification to 
model monitoring, with practical implementation guidance for each phase.

## Key Topics

1. ML Lifecycle Phases:
   • Business goal identification
   • ML problem framing
   • Data processing (collection and preparation)
   • Model development (training, tuning, evaluation)
   • Deployment
   • Monitoring

2. Well-Architected Framework Pillars applied to ML:
   • Operational Excellence
   • Security
   • Reliability
   • Performance Efficiency
   • Cost Optimization
   • Sustainability

3. ML Design Principles:
   • Assign ownership
   • Provide protection
   • Enable resiliency
   • Enable reusability
   • Enable reproducibility
   • Optimize resources
   • Reduce cost
   • Enable automation
   • Enable continuous improvement
   • Minimize environmental impact

4. ML Architecture Components:
   • Lineage tracking
   • Feature stores
   • Model registry
   • Pipelines (data, feature, CI/CD/CT)
   • Monitoring systems

## Best Practices

### Business Goal Identification Phase

Operational Excellence:
• MLOE-01: Develop the right skills with accountability and empowerment
• MLOE-02: Discuss and agree on the level of model explainability
• MLOE-03: Monitor model compliance to business requirements

Security:
• MLSEC-01: Validate ML data permissions, privacy, software, and license terms

Performance Efficiency:
• MLPER-01: Determine key performance indicators

Cost Optimization:
• MLCOST-01: Define overall return on investment (ROI) and opportunity cost
• MLCOST-02: Use managed services to reduce total cost of ownership (TCO)

Sustainability:
• MLSUS-01: Define the overall environmental impact or benefit

### ML Problem Framing Phase

Operational Excellence:
• MLOE-04: Establish ML roles and responsibilities
• MLOE-05: Prepare an ML profile template
• MLOE-06: Establish model improvement strategies
• MLOE-07: Establish a lineage tracker system
• MLOE-08: Establish feedback loops across ML lifecycle phases
• MLOE-09: Review fairness and explainability

Security:
• MLSEC-02: Design data encryption and obfuscation

Reliability:
• MLREL-01: Use APIs to abstract change from model consuming applications
• MLREL-02: Adopt a machine learning microservice strategy

Performance Efficiency:
• MLPER-02: Use purpose-built AI and ML services and resources
• MLPER-03: Define relevant evaluation metrics

Cost Optimization:
• MLCOST-03: Identify if machine learning is the right solution
• MLCOST-04: Tradeoff analysis on custom versus pre-trained models

Sustainability:
• MLSUS-02: Consider AI services and pre-trained models
• MLSUS-03: Select sustainable Regions

### Data Processing Phase

Operational Excellence:
• MLOE-10: Profile data to improve quality
• MLOE-11: Create tracking and version control mechanisms

Security:
• MLSEC-03: Ensure least privilege access
• MLSEC-04: Secure data and modeling environment
• MLSEC-05: Protect sensitive data privacy
• MLSEC-06: Enforce data lineage
• MLSEC-07: Keep only relevant data

Reliability:
• MLREL-03: Use a data catalog
• MLREL-04: Use a data pipeline
• MLREL-05: Automate managing data changes

Performance Efficiency:
• MLPER-04: Use a modern data architecture

Cost Optimization:
• MLCOST-05: Use managed data labeling
• MLCOST-06: Use data wrangler tools for interactive analysis
• MLCOST-07: Use managed data processing capabilities
• MLCOST-08: Enable feature reusability

Sustainability:
• MLSUS-04: Minimize idle resources
• MLSUS-05: Implement data lifecycle policies aligned with sustainability goals
• MLSUS-06: Adopt sustainable storage options

### Model Development Phase

Operational Excellence:
• MLOE-12: Automate operations through MLOps and CI/CD
• MLOE-13: Establish reliable packaging patterns to access approved public libraries

Security:
• MLSEC-08: Secure governed ML environment
• MLSEC-09: Secure inter-node cluster communications
• MLSEC-10: Protect against data poisoning threats

Reliability:
• MLREL-06: Enable CI/CD/CT automation with traceability
• MLREL-07: Ensure feature consistency across training and inference
• MLREL-08: Ensure model validation with relevant data
• MLREL-09: Establish data bias detection and mitigation

Performance Efficiency:
• MLPER-05: Optimize training and inference instance types
• MLPER-06: Explore alternatives for performance improvement
• MLPER-07: Establish a model performance evaluation pipeline
• MLPER-08: Establish feature statistics
• MLPER-09: Perform a performance trade-off analysis
• MLPER-10: Detect performance issues when using transfer learning

Cost Optimization:
• MLCOST-09: Select optimal computing instance size
• MLCOST-10: Use managed build environments
• MLCOST-11: Select local training for small scale experiments
• MLCOST-12: Select an optimal ML framework
• MLCOST-13: Use automated machine learning
• MLCOST-14: Use managed training capabilities
• MLCOST-15: Use distributed training
• MLCOST-16: Stop resources when not in use
• MLCOST-17: Start training with small datasets
• MLCOST-18: Use warm-start and checkpointing hyperparameter tuning
• MLCOST-19: Use hyperparameter optimization technologies
• MLCOST-20: Setup budget and use resource tagging to track costs
• MLCOST-21: Enable data and compute proximity
• MLCOST-22: Select optimal algorithms
• MLCOST-23: Enable debugging and logging

Sustainability:
• MLSUS-07: Define sustainable performance criteria
• MLSUS-08: Select energy-efficient algorithms
• MLSUS-09: Archive or delete unnecessary training artifacts
• MLSUS-10: Use efficient model tuning methods

### Deployment Phase

Operational Excellence:
• MLOE-14: Establish deployment environment metrics

Security:
• MLSEC-11: Protect against adversarial and malicious activities

Reliability:
• MLREL-10: Automate endpoint changes through a pipeline
• MLREL-11: Use an appropriate deployment and testing strategy

Performance Efficiency:
• MLPER-11: Evaluate cloud versus edge options for machine learning deployment
• MLPER-12: Choose an optimal deployment option in the cloud

Cost Optimization:
• MLCOST-24: Use appropriate deployment option
• MLCOST-25: Explore cost effective hardware options
• MLCOST-26: Right-size the model hosting instance fleet

Sustainability:
• MLSUS-11: Align SLAs with sustainability goals
• MLSUS-12: Use efficient silicon
• MLSUS-13: Optimize models for inference
• MLSUS-14: Deploy multiple models behind a single endpoint

### Monitoring Phase

Operational Excellence:
• MLOE-15: Enable model observability and tracking
• MLOE-16: Synchronize architecture and configuration, and check for skew across environments

Security:
• MLSEC-12: Restrict access to intended legitimate consumers
• MLSEC-13: Monitor human interactions with data for anomalous activity

Reliability:
• MLREL-12: Allow automatic scaling of the model endpoint
• MLREL-13: Ensure a recoverable endpoint with a managed version control strategy

Performance Efficiency:
• MLPER-13: Evaluate model explainability
• MLPER-14: Evaluate data drift
• MLPER-15: Monitor, detect, and handle model performance degradation
• MLPER-16: Establish an automated re-training framework
• MLPER-17: Review for updated data/features for retraining
• MLPER-18: Include human-in-the-loop monitoring

Cost Optimization:
• MLCOST-27: Monitor usage and cost by ML activity
• MLCOST-28: Monitor Return on Investment for ML models
• MLCOST-29: Monitor endpoint usage and right-size the instance fleet

Sustainability:
• MLSUS-15: Measure material efficiency
• MLSUS-16: Retrain only when necessary

## Guidelines and Recommendations

### ML Lifecycle Management

1. Business Goal Identification:
   • Clearly define the business problem and value to be gained
   • Establish measurable business objectives and success criteria
   • Evaluate if ML is the appropriate approach
   • Ensure sufficient relevant, high-quality training data is available

2. ML Problem Framing:
   • Define what is observed and what should be predicted
   • Establish observable and quantifiable performance metrics
   • Define the relationship between technical metrics and business outcomes
   • Start with simple models that are easy to interpret

3. Data Processing:
   • Ensure data quality through preprocessing strategies (cleaning, balancing, replacing, imputing, partitioning, scaling)
   • Implement feature engineering (creation, transformation, extraction, selection)
   • Apply the same data processing steps to both training data and inference requests
   • Use exploratory data analysis (EDA) to understand data patterns

4. Model Development:
   • Select appropriate algorithms based on the problem type
   • Implement proper training, tuning, and evaluation processes
   • Use validation metrics appropriate for the model type
   • Implement hyperparameter tuning to optimize model performance
   • Use model versioning and lineage tracking

5. Deployment:
   • Choose appropriate deployment strategies (blue/green, canary, A/B, shadow)
   • Implement inference pipelines for real-time or batch predictions
   • Set up scheduler pipelines for model retraining
   • Ensure proper governance and quality gates

6. Monitoring:
   • Implement model observability and tracking
   • Detect data and concept drift
   • Set up alerts and model update pipelines
   • Include human-in-the-loop monitoring when appropriate

### AWS Implementation Recommendations

1. Use Amazon SageMaker AI Services:
   • SageMaker AI Studio for development environment
   • SageMaker AI Experiments for tracking and comparing models
   • SageMaker AI Data Wrangler for data preparation
   • SageMaker AI Feature Store for feature management
   • SageMaker AI Pipelines for workflow automation
   • SageMaker AI Model Registry for model versioning
   • SageMaker AI Model Monitor for drift detection
   • SageMaker AI Clarify for bias detection and explainability
   • SageMaker AI Debugger for training visibility
   • SageMaker AI Autopilot for automated ML

2. Use AWS Supporting Services:
   • AWS Glue for data catalog and ETL
   • Amazon S3 for data storage
   • Amazon ECR for container registry
   • AWS CloudFormation for infrastructure as code
   • AWS Step Functions for workflow orchestration
   • Amazon CloudWatch for monitoring and alerting
   • AWS IAM for access control
   • AWS KMS for encryption
   • Amazon API Gateway for API management
   • AWS Lambda for serverless computing

## Important Concepts

### ML Lifecycle
The ML lifecycle is a cyclic iterative process with defined phases for developing an ML workload. It includes business goal 
identification, ML problem framing, data processing, model development, deployment, and monitoring. These phases are not 
necessarily sequential and can have feedback loops.

### Lineage Tracking
Lineage tracking enables reproducible machine learning by collecting references to traceable data, model, and infrastructure 
resource changes. Components include:
• Infrastructure as code (IaC)
• Data (metadata, values, features)
• Model (algorithm, features, parameters, hyperparameters)
• Code (implementation, modeling, pipeline)

### Feature Store
A feature store reduces duplication and the need to rerun feature engineering code across teams and projects. It has two 
components:
• Online store: For low-latency retrieval during real-time inference
• Offline store: For maintaining feature history for training and batch scoring

### Model Registry
A repository for storing ML model artifacts including trained models and related metadata (data, code, model). It enables 
tracking the lineage of ML models and acts as a version control system.

### Data and Concept Drift
• **Data drift**: Significant changes to the data distribution compared to the data used for training
• **Concept drift**: When the properties of the target variables change
• Both types of drift result in model performance degradation

### Model Explainability
The ability to understand and interpret the decisions made by ML models. Important for:
• Building trust in model predictions
• Meeting regulatory requirements
• Debugging model behavior
• Identifying bias in model predictions

### Deployment Strategies
• **Blue/Green**: Two identical environments where blue is existing and green is for testing
• **Canary**: New release deployed to a small group before full rollout
• **A/B testing**: Directing defined portions of traffic to different model versions
• **Shadow**: Running new version alongside old version for testing without affecting production

## Examples and Use Cases

### Example 1: Manufacturing Predictive Maintenance
A manufacturing company wants to maximize profits by predicting equipment failures before they occur. The ML approach could 
include:
• Forecasting maintenance needs to reduce downtime
• Predicting required input materials to optimize inventory
• Using sensor data to detect anomalies in equipment performance

Implementation using AWS services:
• Amazon SageMaker AI for model development and deployment
• AWS IoT Greengrass for edge inference on factory floor
• Amazon SageMaker AI Edge Manager for model optimization on edge devices
• Amazon SageMaker AI Model Monitor for drift detection

### Example 2: Financial Fraud Detection
A financial institution wants to detect fraudulent transactions in real-time:
• Data processing includes feature engineering from transaction history
• Model development uses ensemble methods for higher accuracy
• Deployment requires real-time inference with low latency
• Monitoring includes bias detection to ensure fair treatment across customer segments

Implementation using AWS services:
• Amazon SageMaker AI Feature Store for consistent features
• Amazon SageMaker AI Clarify for bias detection
• Amazon SageMaker AI Real-time Inference for low-latency predictions
• Amazon CloudWatch for monitoring endpoint performance

### Example 3: Customer Churn Prediction
A company wants to predict which customers are likely to churn:
• Data includes customer demographics, purchase history, and engagement metrics
• Model development compares different algorithms (logistic regression, random forest, XGBoost)
• Deployment uses batch inference for weekly predictions
• Monitoring tracks model performance against actual churn rates

Implementation using AWS services:
• AWS Glue for data preparation
• Amazon SageMaker AI Autopilot for automated model selection
• Amazon SageMaker AI Batch Transform for weekly predictions
• Amazon QuickSight for visualizing model performance

## Cautions and Limitations

### ML Model Limitations
1. Model Drift: ML models degrade over time due to changes in the real world (data drift and concept drift)
2. Explainability Challenges: Complex models like deep neural networks can be difficult to interpret
3. Bias and Fairness: Models can perpetuate or amplify biases present in training data
4. Data Quality Dependencies: Models are only as good as the data used to train them

### Implementation Considerations
1. Security Risks:
   • Data poisoning threats can corrupt training data
   • Adversarial attacks can manipulate model predictions
   • Unauthorized access to model endpoints can expose sensitive information

2. Cost Considerations:
   • Training deep learning models can be computationally expensive
   • Idle resources can significantly increase costs
   • Inference can account for up to 90% of ML infrastructure costs

3. Operational Challenges:
   • Maintaining consistency between training and inference environments
   • Managing model versions and dependencies
   • Ensuring reproducibility of model training

4. Sustainability Impacts:
   • ML workloads can have significant environmental impacts
   • Training large models consumes substantial energy
   • Unnecessary retraining increases carbon footprint

## Additional Resources

### AWS Documentation
• [AWS Well-Architected Framework](https://aws.amazon.com/architecture/well-architected/)
• [Architecture Best Practices for Machine Learning](https://docs.aws.amazon.com/wellarchitected/latest/machine-learning-lens/
wellarchitected-machine-learning-lens.html)
• [Amazon SageMaker AI Documentation](https://docs.aws.amazon.com/sagemaker/)
• [AWS MLOps Framework](https://aws.amazon.com/solutions/implementations/aws-mlops-framework/)

### AWS Services for ML
• [Amazon SageMaker AI](https://aws.amazon.com/sagemaker/)
• [AWS Glue](https://aws.amazon.com/glue/)
• [Amazon S3](https://aws.amazon.com/s3/)
• [AWS Lambda](https://aws.amazon.com/lambda/)
• [Amazon CloudWatch](https://aws.amazon.com/cloudwatch/)
• [AWS Step Functions](https://aws.amazon.com/step-functions/)
• [Amazon API Gateway](https://aws.amazon.com/api-gateway/)
• [AWS CloudFormation](https://aws.amazon.com/cloudformation/)

### Blogs and Whitepapers
• [Amazon AI Fairness and Explainability Whitepaper](https://pages.awscloud.com/rs/112-TZM-766/images/
Amazon.AI.Fairness.and.Explainability.Whitepaper.pdf)
• [Optimizing AI/ML workloads for sustainability](https://aws.amazon.com/blogs/machine-learning/optimize-ai-ml-workloads-for-
sustainability/)
• [Building a CI/CD pipeline for deploying custom machine learning models](https://aws.amazon.com/blogs/machine-learning/build
-a-ci-cd-pipeline-for-deploying-custom-machine-learning-models-using-aws-services/)

### Tools and Frameworks
• [AWS Deep Learning AMIs](https://aws.amazon.com/machine-learning/amis/)
• [AWS Deep Learning Containers](https://aws.amazon.com/machine-learning/containers/)
• [SageMaker AI JumpStart](https://aws.amazon.com/sagemaker/jumpstart/)
• [AWS Marketplace for Machine Learning](https://aws.amazon.com/marketplace/solutions/machine-learning)
