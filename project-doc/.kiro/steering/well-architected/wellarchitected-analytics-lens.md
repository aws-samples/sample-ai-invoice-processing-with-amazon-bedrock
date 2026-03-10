---
inclusion: manual
---

# AWS Well-Architected Framework Data Analytics Lens - Steering File

## Document Overview

The AWS Well-Architected Data Analytics Lens is a collection of customer-proven best practices for designing well-architected 
analytics workloads on AWS. It provides insights gathered from real-world case studies and helps users understand key design 
elements for analytics workloads along with recommendations for improvement. The document is intended for IT architects, 
developers, and team members who build and operate analytics systems on AWS.

The lens focuses on how to design, deploy, and architect analytics application workloads in the AWS Cloud, covering six 
pillars: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

## Key Topics

1. Well-Architected Framework Pillars for Analytics
   • Operational excellence
   • Security
   • Reliability
   • Performance efficiency
   • Cost optimization
   • Sustainability

2. Analytics Workload Design Principles
   • Monitoring analytics workloads
   • Modernizing deployment of analytics jobs
   • Data governance and compliance
   • Data access control
   • Infrastructure access control
   • Resilience design
   • Data and metadata governance
   • Compute and storage optimization
   • File format and partitioning optimization
   • Cost management
   • Sustainability implementation

3. Common Analytics Scenarios
   • Data discovery
   • Modern data architecture
   • Batch data processing
   • Streaming ingest and stream processing
   • Operational analytics
   • Data visualization
   • Data mesh

## Best Practices

### Operational Excellence

1. Monitor the health of analytics application workloads
   • Validate data quality of source systems before transferring data
   • Monitor operational metrics of data processing jobs and source data availability
   • Implement data quality validation mechanisms
   • Track data freshness
   • Alert when new data hasn't arrived within expected time
   • Alert when jobs don't complete on time or don't produce results

2. Modernize deployment of analytics jobs and applications
   • Use version control for job and application changes
   • Create test data and provision staging environments
   • Test and validate analytics jobs and application deployments
   • Build standard operating procedures for deployment, test, rollback, and backfill tasks
   • Use infrastructure as code
   • Automate deployment and testing

### Security

1. Design data platforms for governance and compliance
   • Implement Privacy by Design principles
   • Apply data minimization techniques
   • Use anonymization, pseudonymization, and tokenization where appropriate
   • Support rights of individuals (Subject Access Requests, right to be forgotten)
   • Classify and protect data based on sensitivity
   • Identify source data owners and have them set data classifications
   • Record data classifications in the Data Catalog
   • Implement encryption policies for data at rest and in transit
   • Implement data retention policies
   • Enforce downstream systems to honor data classifications

2. Implement data access control
   • Allow data owners to determine access permissions
   • Build user identity solutions that uniquely identify people and systems
   • Implement required data authorization models (IAM policies, dataset-level, column-level)
   • Establish emergency access processes
   • Track data and database changes

3. Control access to workload infrastructure
   • Prevent unintended access to infrastructure
   • Implement least privilege policies
   • Monitor infrastructure changes and user activities
   • Secure audit logs

### Reliability

1. Design resilience for analytics workloads
   • Create illustrations of data flow dependencies
   • Monitor analytics systems to detect failures
   • Notify stakeholders about failures
   • Automate recovery of analytics and ETL job failures
   • Build disaster recovery plans
   • Design idempotent ETL jobs

2. Govern data and metadata changes
   • Build a central Data Catalog
   • Monitor for data quality anomalies
   • Trace data lineage
   • Control and version metadata changes
   • Capture and publish business metadata

### Performance Efficiency

1. Choose the best-performing compute solution
   • Identify analytics solutions that best suit technical challenges
   • Provision compute resources close to data storage
   • Define and measure computing performance metrics
   • Identify under-performing components and fine-tune

2. Choose the best-performing storage solution
   • Identify critical performance criteria
   • Evaluate available storage options
   • Choose optimal storage based on access patterns and requirements

3. Choose the best-performing file format and partitioning
   • Select formats based on data write frequency and patterns
   • Choose data formatting based on access patterns
   • Utilize compression techniques
   • Partition data to enable efficient data pruning

### Cost Optimization

1. Choose cost-effective compute and storage solutions
   • Decouple storage from compute
   • Plan capacity for predictable workloads
   • Use On-Demand or serverless capacity for unpredictable workloads
   • Implement auto-scaling where appropriate

2. Build financial accountability models
   • Measure data storage and processing costs per user
   • Balance agility and skill sets when building platforms
   • Build shared processing systems and measure cost per job
   • Restrict resource allocation permissions using IAM

3. Manage cost over time
   • Remove unused data and infrastructure
   • Reduce overprovisioned infrastructure
   • Evaluate and adopt new cost-effective solutions

4. Use optimal pricing models
   • Evaluate infrastructure usage patterns
   • Consult with finance teams to determine optimal payment models
   • Use Reserved Instances or Savings Plans for steady workloads
   • Use spot or serverless resources for development environments

### Sustainability

1. Sustainability implementation guidance
   • Define your organization's current environmental impact
   • Encourage sustainable thinking
   • Foster a culture of data minimization
   • Implement data retention processes
   • Optimize data modeling for efficient retrieval
   • Prevent unnecessary data movement
   • Efficiently manage analytics infrastructure

## Guidelines and Recommendations

### Data Quality and Monitoring

1. Data Quality Validation
   • "The critical attributes of data quality that should be measured and tracked through your environment are completeness, 
accuracy, and uniqueness."
   • Implement data quality scoring and share quality metrics with stakeholders
   • Alert stakeholders when data quality issues are detected

2. Monitoring Analytics Jobs
   • Monitor at multiple levels: infrastructure, ETL workflow, and application code
   • Establish end-to-end monitoring for complete analytics pipelines
   • Classify job failure severity based on business impact
   • Set up automated notifications for failures

### Data Governance and Security

1. Data Classification
   • Use a consistent classification system (e.g., restricted, confidential, internal, public)
   • Define access rules based on data sensitivity
   • Implement security zones to isolate data by classification
   • Use tags to indicate data classifications in catalogs

2. Data Protection
   • Implement encryption for data at rest and in transit
   • Apply data minimization techniques
   • Use anonymization for test environments
   • Implement proper data retention and deletion processes

3. Access Control
   • Implement role-based access control (RBAC)
   • Use column-level, row-level, and cell-level security where needed
   • Centralize workforce identities
   • Implement the two-person rule for critical operations

### Performance Optimization

1. Storage Optimization
   • Use columnar formats (Parquet, ORC) for analytical workloads
   • Implement appropriate compression techniques
   • Partition data based on common query patterns
   • Store data by temperature (hot, warm, cold)

2. Query Optimization
   • Use predicate pushdown where possible
   • Implement caching strategies (query results, data)
   • Pre-compute common aggregations
   • Use materialized views for frequently accessed data

3. Resource Allocation
   • Right-size infrastructure based on workload patterns
   • Use auto-scaling for variable workloads
   • Implement serverless options for unpredictable usage

### Cost Management

1. Resource Optimization
   • "Delete data that is out of its retention period, or not needed anymore."
   • "Delete intermediate-processed data that can be removed without business impacts."
   • "Remove unused analytics jobs that consume infrastructure resources but no one uses the job results."
   • Move infrequently accessed data to lower-cost storage tiers

2. Financial Models
   • Use tagging for cost attribution
   • Implement cost visibility and internal bill-back methods
   • Track AWS CloudTrail logs to determine usage per user/role

### Sustainability Practices

1. Data Minimization
   • "Minimize the amount of data extracted from your source systems that gets stored in your data warehouse"
   • Use appropriate data types to reduce storage requirements
   • Review APIs to minimize data shared with streaming applications
   • Reduce data migration between environments

2. Efficient Infrastructure
   • Use managed and serverless services
   • Pause resources when not in use
   • Scale resources to match demand
   • Run analytics workloads on spare capacity

## Important Concepts

### Modern Data Architecture

A modern data architecture integrates a data lake, a data warehouse, and other purpose-built data stores while enabling 
unified governance and seamless data movement. It has three data movement patterns:

1. Inside-out data movement: Moving data from a data lake to specialized data stores
2. Outside-in data movement: Moving data from specialized data stores to a data lake
3. Around the perimeter: Moving data between specialized data stores

Key characteristics include:
• Scalable data lake
• Support for diverse data types
• Schema management (schema on read, schema evolution)
• Metadata management
• Unified governance
• Transactional semantics

### Data Mesh

A data mesh is an architectural framework that enables domain teams to perform cross-domain data analysis through distributed,
decentralized ownership. It treats data as a product, with each organizational domain owning their data end-to-end.

Key characteristics include:
• Data diversity
• Data democratization
• Federated data governance
• Searchability
• Self-service data sharing
• Increased flexibility
• Reusability

### Streaming Data Architecture

Streaming data architectures are built on five core constructs:
1. Data sources
2. Stream ingestion and producers
3. Stream storage
4. Stream processing and consumers
5. Downstream destinations

Key characteristics include:
• Scalable throughput
• Dynamic stream processor consumption
• Durability
• Replay-ability
• Fault-tolerance with checkpointing
• Loosely coupled integration
• Support for multiple processing applications
• Various messaging semantics (at most once, at least once, exactly once)

## Examples and Use Cases

### Data Discovery

Data discovery involves identifying how to maximize value from data by exploring data sources, user personas, and processing 
requirements. The process includes:

1. Defining business value
2. Identifying user personas (analysts, data scientists, etc.)
3. Identifying data sources (structured, semi-structured, unstructured)
4. Defining storage, catalog, and access needs
5. Defining data processing requirements

### Batch Data Processing

Batch processing allows organizations to process data in batches at varying intervals. Example use case:
• Processing daily sales aggregations by store and writing to a data warehouse for BI reporting

Key services: Amazon EMR, Amazon Redshift, AWS Glue ETL, AWS Glue Workflows, AWS Glue DataBrew

### Streaming Ingest and Processing

Example use cases:
• Real-time analytics
• Fraud detection
• API microservices integration
• Real-time inventory and recommendations
• Click-stream, log file, and IoT device analysis

Key services: Amazon Kinesis Data Streams, Amazon MSK, AWS Lambda, Amazon EMR (Spark Structured Streaming, Apache Flink), AWS 
Glue ETL Streaming

### Operational Analytics

Operational analytics helps organizations measure and improve day-to-day business performance. It involves collecting and 
analyzing telemetry data (logs, traces, metrics) to:
• Monitor system health
• Identify operational inefficiencies
• Improve customer experience
• Automate responses to issues

Key services: Amazon OpenSearch Service, Amazon Managed Service for Prometheus, Amazon Managed Grafana

### Data Visualization

Data visualization enables decision-makers to explore and interpret information in an interactive visual environment. Example 
use cases:
• Business intelligence dashboards
• Self-service analytics
• Natural language querying with QuickSight Q
• Embedded analytics in applications

Key service: Amazon QuickSight

## Cautions and Limitations

1. Data Quality Risks
   • "Failures in data processing systems can cause data integrity or data quality issues."
   • Validate data quality before transferring to analytics systems
   • Monitor for anomalies and alert stakeholders

2. Security Considerations
   • "Care should be taken that end users of analytics applications are not exposed to sensitive data."
   • Implement proper data masking and access controls
   • Secure audit logs to prevent tampering

3. Performance Trade-offs
   • "There are often multiple storage options available for each service, each offering different characteristics and 
potentially performance benefits."
   • Balance storage efficiency with query performance
   • Consider compression vs. splittable formats trade-offs

4. Cost Management Challenges
   • "Costs can quickly get out of control if you do not plan correctly."
   • Regularly review and optimize resource usage
   • Remove unused data and infrastructure

5. Sustainability Trade-offs
   • "Implementing each of the best practices involves resource trade-offs."
   • Test recommendations to determine storage vs. compute trade-offs
   • Balance business requirements with sustainability goals

## Additional Resources

1. AWS Documentation
   • AWS Well-Architected Framework whitepaper
   • AWS Big Data Blog
   • AWS Database Blog
   • AWS Security Blog
   • AWS Management and Governance Blog

2. AWS Services Documentation
   • AWS Glue Developer Guide
   • Amazon Redshift Database Developer Guide
   • Amazon EMR Management Guide
   • Amazon Athena User Guide
   • AWS Lake Formation Developer Guide
   • Amazon OpenSearch Service Developer Guide
   • Amazon QuickSight User Guide

3. AWS Whitepapers
   • Data Classification: Secure Cloud Adoption
   • Building a Cloud Operating Model
   • Introduction to DevOps on AWS
   • Establishing your best practice AWS environment
   • Organizing Your AWS Environment Using Multiple Accounts
   • Security Pillar – AWS Well-Architected Framework
   • Derive Insights from AWS Modern Data
   • Build Modern Data Streaming Architectures on AWS

4. AWS Tools and Resources
   • AWS Customer Carbon Footprint Tool
   • AWS Cost and Usage Report
   • Cost and Usage Dashboards Operations Solution (CUDOS)
   • AWS Analytics Automation Toolkit
