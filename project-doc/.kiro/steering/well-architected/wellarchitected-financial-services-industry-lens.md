---
inclusion: manual
---

# AWS Well-Architected Framework Financial Services Industry Lens - Steering File

## Document Overview

The AWS Well-Architected Framework Financial Services Industry Lens is a comprehensive guide that applies the AWS Well-Architected Framework specifically to financial services workloads. It provides architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and sustainable systems in the cloud for financial services institutions. The document focuses on how to design, deploy, and architect financial services industry workloads that promote resiliency, security, cost savings, and operational performance in line with risk and control objectives, including those that help align with regulatory and compliance requirements of supervisory authorities.

This lens is intended for technology leadership roles such as CTOs, architectural leadership, developers, engineers, operations teams, as well as individuals in risk, compliance, and audit functions within financial services organizations.

## Key Topics

1. Design Principles - Overarching principles for financial services workloads in the cloud
2. Common Scenarios - Reference architectures for common financial services use cases
   • Financial data mesh
   • Artificial intelligence and machine learning
   • Cyber event recovery
   • Open banking
   • Payments
   • Insurance lake
   • Capital markets
3. Operational Excellence - Managing risks and satisfying regulatory requirements
4. Security - Protecting information, systems, and assets through risk assessments and mitigation strategies
5. Reliability - Ensuring workloads perform intended functions correctly and consistently
6. Performance Efficiency - Efficient use of resources to meet requirements
7. Cost Optimization - Optimizing costs while maintaining business value
8. Sustainability - Addressing long-term environmental, economic, and societal impact

## Best Practices

### General Design Principles

1. Documented Operational Planning
   • Implement the "Three Lines of Defense" model for risk management
   • Establish clear roles and responsibilities across defense functions
   • Define operational procedures and controls

2. Automated Infrastructure and Application Deployment
   • Implement automation to perform and innovate quickly
   • Scale security, compliance, and governance activities
   • Embed security and governance best practices into the software development lifecycle

3. Security by Design
   • Implement architectures pre-tested from a security perspective
   • Use standardized, automated, prescriptive, and repeatable design templates
   • Implement control objectives, security baselines, and audit capabilities
   • Enable encryption for data at rest, in transit, and at the application level by default

4. Automated Governance
   • Implement automated governance checks for application deployment at scale
   • Address account management, budget and cost management, and security and compliance automation

### Operational Excellence

1. Organization
   • Define risk management roles for the cloud
   • Establish clear roles and responsibilities across the three lines of defense
   • Engage with risk management and internal audit functions
   • Implement a process for adopting appropriate risk appetites

2. Preparation
   • Complete operational risk assessments
   • Understand the AWS Shared Responsibility Model
   • Develop an enterprise cloud risk plan
   • Assess workloads against regulatory needs

3. Operation
   • Implement a change management process for cloud resources
   • Implement infrastructure as code
   • Prevent configuration drift
   • Use enhanced monitoring in the cloud
   • Monitor cloud provider events
   • Manage cloud provider service events

4. Evolution
   • Test, model, and simulate scenarios before rollout
   • Conduct post-event operational reviews

### Security

1. Security Foundations
   • Leverage a Cloud Center of Excellence (CCoE)
   • Use cloud-native services for management and governance
   • Automate compliance management
   • Use ready-to-deploy templates for standards and best practices

2. Identity and Access Management
   • Monitor the use of elevated credentials
   • Review IAM policies and permissions regularly
   • Mitigate privilege escalation
   • Monitor unauthorized activity
   • Implement the principle of separation of duties
   • Use AWS Config to view historical IAM configuration
   • Set up alerts for IAM configuration changes

3. Detection
   • Track configuration changes
   • Detect unusual and unauthorized activity early
   • Automate remediation of common vulnerabilities and exposures
   • Perform static analysis on all code deploys
   • Conduct regular penetration testing
   • Deploy web application firewalls
   • Monitor instance traffic
   • Use VPC Traffic Mirroring
   • Use immutable infrastructure with no human access
   • Allow interactive access for emergencies only

4. Infrastructure Protection
   • Implement a multi-account strategy
   • Enforce network isolation
   • Isolate SDLC environments (development, test, production)

5. Data Protection
   • Manage encryption keys properly
   • Consider compliance obligations regarding location of cryptographic keys
   • Prevent modifications and deletions of logs and data
   • Limit and monitor key deletes
   • Protect against ransomware

6. Incident Response
   • Regularly review incident response plans for regulatory compliance

### Reliability

1. Software Development Lifecycle
   • Treat CI/CD tools as critical workload components for recovery
   • Practice continuous resilience testing
   • Implement an operational readiness review process

2. Resilience Requirement Planning
   • Use business criticality to drive recovery objectives
   • Apply fine-grained workload resilience requirements
   • Use past examples of market volatility in determining peak loads
   • Model failures to identify resilience requirements

3. Resilience Architecture
   • Implement best practices for highly resilient critical workloads
   • Provide external dependency accessibility from failover environments
   • Decouple dependencies
   • Evaluate the resilience of cross-cloud application architectures
   • Address hybrid resiliency

4. Observability
   • Detect, locate, and recover from gray failures
   • Monitor indicators aside from system metrics
   • Find outliers hiding in aggregate metrics
   • Use anomaly detection for user engagement metrics
   • Have a way to manually route away during failure
   • Establish baselines for expected network traffic
   • Monitor and validate RPO and RTO
   • Use a single pane of glass for monitoring
   • Alert on the absence of an event
   • Identify metrics and validate alerts through load testing
   • Use distributed tracing tools for service-oriented architectures

5. Backup and Retention
   • Implement a comprehensive backup strategy
   • Maintain backups in a secondary Region
   • Understand requirements for data backup and retention
   • Back up logs as part of the backup strategy
   • Incorporate anti-ransomware backups
   • Create lifecycle policies for backups
   • Use Glacier Vault Lock and S3 Object Lock for WORM storage

### Performance Efficiency

1. Selection
   • Use internal and external risk to determine performance requirements
   • Factor in rate of increase in load and scale-out intervals
   • Benchmark solutions
   • Select compute architecture based on workload requirements
   • Select storage architecture based on workload requirements
   • Consider changing needs over the entire lifecycle of data
   • Use AWS services to optimize network routes
   • Use Amazon EC2 instances and features to optimize networking

2. Monitoring
   • Use Application Performance Monitoring (APM) tools
   • Integrate performance testing into the release cycle
   • Verify consistency and failure recovery during load tests
   • Understand performance under peak load and in failure scenarios
   • Include dependencies in load tests

3. Trade-offs
   • Understand priorities and architect to meet them
   • Balance performance with other factors like cost and availability

### Cost Optimization

1. Cloud Financial Management
   • Educate cloud teams on technical and commercial optimization mechanisms
   • Apply the Pareto-principle (80/20 rule) to manage, optimize, and plan cloud usage
   • Use automation to drive scale for Cloud Financial Management practices

2. Expenditure and Usage Awareness
   • Promote cost-awareness within the organization
   • Track anomalies in ongoing costs for AWS services
   • Track workload usage cycles

3. Cost-effective Resources
   • Use available AWS credit and investment programs
   • Monitor usage of Savings Plans regularly
   • Use tiered storage cost advantages
   • Use lower cost Regions for less time-sensitive workloads
   • Consider cost tradeoffs of various AWS pricing models
   • Save costs by adopting modern microservice architectures
   • Use cloud services for consulting or testing projects
   • Measure the cost of licensing third-party applications

4. Optimization Over Time
   • Review ongoing cost structure tradeoffs
   • Continuously assess costs and usage
   • Continually review workloads for cost-effective resources
   • Set workload modernization or refactoring goals
   • Use the cloud to drive innovation and operational excellence

### Sustainability

1. Region Selection
   • Select Regions with lower environmental impact
   • Address data sovereignty regulations
   • Select Regions that offer required services and sustainable hardware

2. Alignment to Demand
   • Prioritize business-critical functions over non-critical functions
   • Define, review, and optimize network access patterns

3. Software and Architecture
   • Monitor and minimize resource usage
   • Optimize batch processing components
   • Use event-driven architecture
   • Optimize resource-intensive code
   • Select storage classes with lowest carbon footprint
   • Store processed data rather than raw data when possible

4. Hardware and Services
   • Benchmark instances for existing workloads
   • Complete workloads over more time while meeting SLAs
   • Use multi-architecture images for grid computing systems
   • Test workloads that require floating point precision

5. Process and Culture
   • Use development resources judiciously
   • Minimize test, staging, and sandbox instances
   • Define minimum response time requirements to maximize green SLAs

## Guidelines and Recommendations

### Financial Services Specific Considerations

1. Regulatory Compliance
   • Financial institutions must be aware of all applicable regulatory and compliance obligations
   • Implement policies to achieve defined security objectives
   • Monitor and report on compliance with requirements
   • Translate regulatory requirements into security control objectives

2. Risk Management
   • Implement the Three Lines of Defense model:
     • First line: Operational managers performing day-to-day risk and control procedures
     • Second line: Risk management and compliance functions
     • Third line: Internal auditors providing independent assurance
   • Establish clear roles and responsibilities across defense functions
   • Conduct regular risk assessments of cloud environments

3. Data Protection
   • Implement encryption for data at rest, in transit, and at the application level
   • Carefully manage access to encryption keys
   • Consider compliance obligations regarding location of cryptographic keys
   • Implement WORM (write once, read many) storage for regulatory compliance
   • Create lifecycle policies for data retention based on regulatory requirements

4. Resilience Requirements
   • Define recovery objectives (RTO and RPO) based on business criticality
   • Consider tiered resilience requirements:
     • Platinum (Tier 1): Mission-critical workloads (RTO: 15 minutes, RPO: 30 seconds)
     • Gold (Tier 2): Important but not mission-critical (RTO: 15 minutes - 8 hours, RPO: 2 hours)
     • Silver (Tier 3): Non-critical workloads (RTO: 6 hours - days, RPO: 24 hours)
   • Apply fine-grained resilience requirements to different functions within a workload

5. Operational Monitoring
   • Implement enhanced monitoring for financial services workloads
   • Collect and centralize logs and audit trails
   • Monitor for unusual and unauthorized activity
   • Set up alerts for configuration changes
   • Implement a process for reporting service disruptions to stakeholders and regulators

## Important Concepts

1. Three Lines of Defense Model
   • A risk management framework widely adopted by financial institutions
   • First line: Operational managers (day-to-day risk management)
   • Second line: Risk management and compliance functions
   • Third line: Internal audit (independent assurance)

2. AWS Shared Responsibility Model
   • AWS is responsible for security "of" the cloud (infrastructure)
   • Customers are responsible for security "in" the cloud (data, applications, etc.)
   • Understanding this model is crucial for implementing appropriate controls

3. Recovery Time Objective (RTO) and Recovery Point Objective (RPO)
   • RTO: Maximum acceptable time to restore service after a disruption
   • RPO: Maximum acceptable data loss measured in time
   • These metrics define the resilience requirements for financial services workloads

4. Gray Failures
   • Non-binary failures characterized by differential observability
   • Different entities observe the failure differently
   • Examples: partial packet loss, intermittent failures behind load balancers
   • Difficult to detect using traditional monitoring approaches

5. Write Once, Read Many (WORM)
   • Storage format required by financial regulators like SEC and FINRA
   • Data cannot be modified or deleted once written
   • Implemented using S3 Object Lock or Glacier Vault Lock

6. Cloud Financial Management (CFM)
   • Framework for managing, optimizing, and planning costs in the cloud
   • Four pillars: see, save, plan, and run
   • Essential for managing costs in financial services workloads

7. Security by Design (SbD)
   • Approach to implement architectures pre-tested from a security perspective
   • Helps implement control objectives, security baselines, and audit capabilities
   • Uses standardized, automated templates to accelerate deployment

## Examples and Use Cases

### Financial Data Mesh

A data mesh architecture enables access to diverse data across the enterprise through distributed and decentralized ownership.
The reference architecture includes:

• Producer accounts: Business domains manage their datasets
• Catalog account: Centralized catalog and access management
• Consumer accounts: Data lake administrators manage access policies

This architecture helps financial institutions combine market data, transaction data, and third-party data for analytics and 
machine learning.

### Artificial Intelligence and Machine Learning

Financial institutions use AI/ML for:
• Surveillance
• Fraud reduction
• Risk mitigation and compliance
• Customer interactions
• Operational efficiency

The reference architecture includes:
1. Business requirements phase
2. ML infrastructure phase
3. Continuous integration phase (data preparation and model building)
4. Continuous delivery phase (deployment and monitoring)

### Cyber Event Recovery

The reference architecture for cyber event recovery includes:
• Ingress zone: Raw data storage
• Analytics zone: Data analysis to prevent transmission of corrupt data
• Vault zone: WORM-compliant storage
• Forensics zone: Analysis for anomalies
• Egress zone: Recovery process
• Management interface zone: Authentication and reporting

### Open Banking

Open banking allows banks to securely share customer data with third parties through APIs. The reference architecture shows:
1. Consumer access to third-party applications
2. Third-party services for account information and payments
3. Trust service provider for authentication
4. Bank's IT environment with AWS services

### Payments

The reference architecture for QR payments shows:
1. Customer scanning business QR code
2. Traffic routing through Route 53 and API Gateway
3. Content delivery through CloudFront
4. Security services like AWS WAF and Shield
5. Request routing through Network Load Balancer
6. Payment processing using Amazon ECS and AWS Fargate
7. Data storage in Aurora or DynamoDB
8. Security and compliance monitoring

### Insurance Lake

The insurance data lake follows the four Cs pattern:
1. Collect: Store data in Amazon S3
2. Cleanse and curate: Validate, map, transform, and log actions
3. Consume: Derive insights
4. Comply and secure: Automate audit and regulatory compliance

### Capital Markets

The market data ingestion and distribution architecture shows:
• Data extraction from real-time and historical sources
• Data ingestion, cataloging, and packaging workflow
• Connectivity options including AWS Outposts and Direct Connect
• Stream processing with Amazon MSK and Apache Flink
• Data lake implementation with S3 and AWS Glue
• Data governance with AWS Lake Formation
• Data distribution through AWS Data Exchange and API Gateway

## Cautions and Limitations

1. Regulatory Compliance
   • Financial institutions must be aware of all applicable regulatory requirements
   • Requirements vary by region and jurisdiction
   • Institutions operating in multiple regions must meet different requirements in different places

2. Security Risks
   • Financial institutions are frequent targets of security incidents
   • Institutions must comply with rules around protection of personal and financial information
   • Continuity of operations depends on security resilience

3. Performance Trade-offs
   • Some financial services workloads (like trading systems) require very low latency
   • Performance requirements may necessitate trade-offs with cost efficiency or other factors
   • Consider the impact of these trade-offs when designing workloads

4. Data Sovereignty
   • Data residency requirements may limit the use of certain Regions
   • This can impact sustainability goals if lower-carbon Regions cannot be used
   • May require separating data and processing to comply with requirements

5. Testing Limitations
   • Running load tests on AWS can initiate security mechanisms
   • Penetration testing can be run only on permitted AWS services
   • DDoS testing must be performed by pre-approved AWS Partners

6. Shared Responsibility Model
   • AWS is responsible for the resilience of the cloud
   • Customers are responsible for resilience in the cloud
   • Understanding this division is crucial for implementing appropriate controls

7. Cost Optimization Challenges
   • Design decisions are sometimes directed by haste rather than data
   • Overcompensation for worst-case scenarios can lead to over-provisioned deployments
   • Balancing cost optimization with other requirements can be challenging

## Additional Resources

### Documentation and Blogs
• Building Your Own Game Day to Support Operational Resilience
• How Financial Institutions can Address Regulatory Reporting
• How Financial Institutions can Select the Appropriate Controls to Protect Sensitive Data
• Automating and Scaling Chaos Engineering using AWS Fault Injection Service
• Best Practices for AWS Organizations Service Control Policies in a Multi-Account Environment
• How financial institutions modernize record retention on AWS
• Resilience lifecycle framework: A continuous approach to resilience improvement
• Banking Trends 2022: Cyber Vault and Ransomware
• Implement an SQL Server HA/DR Solution on AWS Outposts
• Disaster Recovery Compliance in the Cloud
• Chaos Engineering in the Cloud
• Amazon Builders Library
• Rethinking the low latency trade value proposition using AWS Local Zones
• How to improve FRTB's Internal Model Approach implementation using Apache Spark and Amazon EMR
• How cloud increases flexibility of trading risk infrastructure for FRTB compliance
• Crypto market-making latency and Amazon EC2 shared placement groups

### Whitepapers
• IIA's Three Lines of Defense model update
• Customers can achieve and test resiliency on AWS
• AWS Cloud Adoption Framework: Operations Perspective
• Designing Highly Resilient Financial Services Applications
• Running an Exchange in the Cloud
• AWS Fault Isolation Boundaries
• Financial Services Grid Computing on AWS
• Cohasset Associates Compliance Assessment for Amazon S3
• AWS Fault Isolation Boundaries
• Availability and Beyond
• Best Practices for Tagging AWS Resources
• The Hartford: Total Cloud Migration

### Videos
• AWS re:Invent 2019: Leadership session: Running critical FSI applications on AWS
• Simplify the AWS Shared Responsibility Model
• AWS re:Invent 2021 - Cloud compliance, assurance, and auditing
• Simplify Operational Change Management with Change Manager
• AWS re:Invent 2021 - Intelligently automating cloud operations
• Building a Robust Monitoring Strategy - AWS Virtual Workshop
• AWS re:Invent 2022 - AWS Incident Detection and Response
• Building Confidence through chaos engineering on AWS
• NYSE: Protecting markets through real-time data processing
• Nasdaq: Moving mission-critical, low-latency workloads to AWS
• HSBC Uses Serverless to Process Millions of Transactions in Real Time
• FINRA Collects, Analyzes Billions of Brokerage Transaction Records Daily Using AWS
• How Morgan Stanley leveraged Amazon EC2 Spot to Scale on Demand
• Risk calculations using HPC and Spot Instances with Morgan Stanley
• DBS Bank: Scalable Serverless Compute Grid on AWS

### Training Materials
• AWS Well-Architected Considerations for Financial Services
• Industry Quest: Financial Services (Amazon)
• AWS Observability
• Getting Started with AWS Systems Manager
• AWS Systems Manager
• Getting Started with AWS Config
• Getting Started with AWS CloudTrail
• Introduction to Amazon CloudWatch
• Introduction to Amazon CloudWatch Logs
• AWS Cloud Essentials for Business Leaders (Financial Services)
• AWS Ramp-Up Guide: Financial Services Industry (FSI)
• Skill Builder - Cloud for Finance Professionals
• AWS Well-Architected Cost Optimization Workshop
