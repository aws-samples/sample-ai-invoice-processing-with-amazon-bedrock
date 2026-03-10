---
inclusion: manual
---

# Amazon OpenSearch Service Lens: AWS Well-Architected Framework Steering Guide

## Document Overview

This document is the AWS Well-Architected Amazon OpenSearch Service Lens, which serves as a comprehensive resource for 
engineering and implementing secure, efficient, and high-performing OpenSearch Service workloads. It's designed for technology
professionals including CTOs, architects, developers, and operational teams, providing best practices and strategies to 
optimize OpenSearch Service designs according to the six pillars of the AWS Well-Architected Framework: Operational 
Excellence, Security, Reliability, Performance Efficiency, Cost Optimization, and Sustainability.

## Key Topics

1. Design Principles - Fundamental principles for building well-architected OpenSearch domains
2. Common Scenarios - Log analytics and search workloads use cases
3. Operational Excellence - Practices for effectively running and monitoring OpenSearch systems
4. Security - Approaches to protect information, systems, and assets
5. Reliability - Methods to ensure workloads perform correctly and consistently
6. Performance Efficiency - Techniques to deliver optimal performance while efficiently using resources
7. Cost Optimization - Strategies to avoid unnecessary costs
8. Sustainability - Practices to reduce environmental impact while optimizing costs

## Best Practices

### Operational Excellence

1. Index Management
   • Employ Index State Management (ISM) to manage logs or time series data
   • Configure index templates to automate index configuration upon creation
   • Remove unused indexes to optimize performance and reduce costs

2. Snapshot Management
   • Establish a manual snapshot repository
   • Automate the process of taking snapshots

3. Monitoring and Alerting
   • Establish alarms for OpenSearch Service domain
   • Configure notification services to receive monitoring alerts
   • Enable search and indexing slow log functionality
   • Enable audit logs for OpenSearch Service domains using fine-grained access control

4. Troubleshooting
   • Train staff on common OpenSearch issues and how to remediate them

### Security

1. Security Foundation
   • Launch OpenSearch Service domains within a Virtual Private Cloud
   • Activate node-to-node encryption
   • Enable encryption at rest
   • Encrypt slow and error logs in Amazon CloudWatch

2. Detection
   • Set up audit logging for domains using fine-grained access control
   • Track OpenSearch Service API calls
   • Monitor real-time events in domains
   • Assess domain configuration with AWS Config

3. Data Protection
   • Implement fine-grained access control to manage access to data
   • Secure indices, documents, and fields using fine-grained access control

### Reliability

1. Foundations
   • Implement a system update notification strategy
   • Regularly update OpenSearch Service domain to the latest version

2. Workload Architecture
   • Create Multi-AZ with Standby OpenSearch Service domains
   • Regularly review OpenSearch Service quotas
   • Implement disaster recovery strategy for business continuity
   • Implement ISM policy to generate snapshots for crucial indices
   • Enable index replication for critical indices
   • Employ cross-cluster replication to achieve higher availability
   • Implement appropriate compute sizing for production workloads

### Performance Efficiency

1. Architecture Selection
   • Maintain shard sizes at recommended ranges (10-50 GiB)
   • Check shard-to-CPU ratio (minimum 1.5 vCPUs per shard)
   • Check the number of shards per GiB of heap memory (no more than 25 shards per GiB)
   • Implement processor utilization monitoring (keep CPU usage under 75%)
   • Implement Java memory utilization monitoring (keep JVMMemoryPressure below 85%)

2. Data Management
   • Establish storage utilization thresholds (keep domain storage usage under 75%)
   • Evenly distribute data across data nodes
   • Use storage types that provide higher IOPs and throughput baseline (gp3 volumes)
   • Enable slow log functionality for search and indexing
   • Use static mapping for your index
   • Use the flat object type for nested objects

3. Node Management
   • Enable dedicated leader nodes
   • Enable dedicated coordinator nodes

4. Process and Culture
   • Identify index refresh controls for optimal ingestion performance
   • Evaluate bulk request size (recommended 3-5 MiB)
   • Implement HTTP compression
   • Evaluate filter_path criteria to reduce response sizes

### Cost Optimization

1. Resource Selection
   • Use the latest generation of instances
   • Employ the appropriate instance type and count
   • Evaluate manager nodes

2. Storage Optimization
   • Use the latest Amazon EBS gp3 volumes
   • Use instances optimized for heavy indexing use cases (OR1)
   • Use warm storage tier for significant amounts of read-only data
   • Use cold tier storage for infrequently accessed or historical data

3. Cost Management
   • Evaluate forecasting for workloads and consider Reserved Instances
   • Apply cost allocation tags for detailed cost tracking
   • Assess pricing for instances and storage
   • Examine costs associated with S3 storage for manual snapshots

### Sustainability

1. Region Selection
   • Select Region based on business requirements and sustainability goals

2. Instance Selection
   • Evaluate instances in alignment with sustainability goals (e.g., Graviton-based)
   • Use the minimum number of instances necessary

3. Data Management
   • Use ISM to manage dataset lifecycle
   • Reduce unnecessary or redundant data
   • Take manual snapshots only when necessary

4. Environment Optimization
   • Consolidate development and test environments

## Guidelines and Recommendations

### Sharding Strategy
• Keep shard sizes between 10-30 GiB for search-intensive workloads
• Keep shard sizes between 30-50 GiB for log analytics and time-series data
• Maintain a minimum shard-to-CPU ratio of 1:1.5
• Keep no more than 25 shards per GiB of Java heap memory
• Ensure no more than 1,000 shards per data node
• Use shard counts that are multiples of the data node count for even distribution

### Monitoring Thresholds
• Keep CPU utilization below 75%
• Keep JVMMemoryPressure below 85%
• Keep domain storage usage below 75%
• Set up CloudWatch alarms for critical metrics

### Storage Recommendations
• Use gp3 EBS volumes instead of gp2 for better performance and cost efficiency
• Consider OR1 instances for heavy indexing use cases
• Implement UltraWarm for read-only data that needs to be accessed occasionally
• Use cold storage for infrequently accessed historical data

### Security Implementation
• Deploy domains within a VPC rather than using public endpoints
• Enable node-to-node encryption and encryption at rest
• Implement fine-grained access control for data protection
• Set up audit logging and CloudTrail integration

### Dedicated Node Sizing
For dedicated leader nodes:
• 1-10 instances: m5.large.search or m6g.large.search (8 GiB RAM, 10K shards)
• 11-30 instances: c5.2xlarge.search or c6g.2xlarge.search (16 GiB RAM, 30K shards)
• 31-75 instances: r5.xlarge.search or r6g.xlarge.search (32 GiB RAM, 40K shards)
• 76-125 instances: r5.2xlarge.search or r6g.2xlarge.search (64 GiB RAM, 75K shards)
• 126-200 instances: r5.4xlarge.search or r6g.4xlarge.search (128 GiB RAM, 75K shards)

For dedicated coordinator nodes:
• Provision 5-10% of your domain's total data nodes as coordinator nodes
• Keep the instance family the same for coordinator and data nodes
• Start with the same instance size as data nodes

## Important Concepts

### Domain
The primary container for all OpenSearch resources, representing the entire environment where data is stored and indexed.

### Node Types
• **Data nodes**: Store and manage data, handle indexing and searching operations
• **Leader nodes**: Perform cluster management tasks but don't hold data
• **Dedicated leader nodes**: Specialized nodes configured exclusively for the leader role
• **UltraWarm and cold nodes**: Cost-effective storage options for read-only data using Amazon S3

### Multi-AZ with Standby
A deployment option providing 99.99% availability by spanning three Availability Zones, each with a complete data copy.

### Index Components
• **Index**: Data structure for storing, organizing, and searching documents
• **Shard**: Smaller segment of an index distributed across data nodes
• **Replica**: Duplication of a shard for failover and load balancing
• **Document**: Single unit of searchable data with a unique ID
• **Field**: Named, typed value within a document
• **Mapping**: Defines document structure in an index

### Operations
• **Query**: Request to search, filter, or aggregate data
• **Aggregation**: Process of grouping and summarizing data
• **Snapshot**: Point-in-time copy of data in indices

## Examples and Use Cases

### Log Analytics Workload: Web Application Log Analysis
1. Configure web application to log relevant information
2. Collect logs using Fluentbit, Amazon OpenSearch Service Ingestion, or direct sending
3. Define an OpenSearch index mapping corresponding to log structure
4. Use full-text search to identify errors, monitor performance, and analyze user behavior
5. Create visualizations and dashboards using Amazon OpenSearch Service Dashboard
6. Set up alerting for specific log patterns or anomalies

### Search Workload: E-commerce Product Search
1. Index product catalog with attributes like name, description, category, and price
2. Implement full-text search with term matching queries
3. Use bucket and aggregation search for filtering by attributes
4. Implement sorting and ranking using OpenSearch's scoring capabilities
5. Add synonym support and typo handling with fuzziness features

## Cautions and Limitations

### Performance Risks
• Exceeding 75% CPU utilization can lead to performance issues
• JVMMemoryPressure above 85% can cause excessive garbage collection or out-of-memory problems
• Storage usage above 75% can cause write operations to fail
• Node shard or storage skew can create bottlenecks and hotspots
• Using t2 or t3.small instances for production domains can lead to instability under sustained heavy load

### Security Considerations
• Domains with public endpoints are more vulnerable than those in a VPC
• Without node-to-node encryption, traffic within the VPC is unencrypted
• Without fine-grained access control, data access may not be properly restricted
• Without audit logging, user activity cannot be properly tracked for compliance

### Operational Warnings
• Domain type (VPC vs. public endpoint) cannot be changed after creation
• Improper shard sizing can lead to performance issues
• Default refresh interval of one second can impact indexing performance
• Excessive snapshots lead to unnecessary storage and energy wastage
• Uneven distribution of data across nodes can lead to node failures

## Additional Resources

### AWS Services
• Amazon OpenSearch Service
• Amazon CloudWatch
• Amazon SNS
• AWS CloudTrail
• Amazon EventBridge
• AWS Config
• AWS Key Management Service (AWS KMS)
• Amazon Virtual Private Cloud (Amazon VPC)
• Amazon Elastic Block Store (EBS)

### Documentation and Guides
• Index State Management in Amazon OpenSearch Service
• Creating index snapshots in Amazon OpenSearch Service
• Monitoring OpenSearch logs with Amazon CloudWatch Logs
• Monitoring audit logs in Amazon OpenSearch Service
• Recommended CloudWatch alarms for Amazon OpenSearch Service
• Sharding strategy
• Sizing OpenSearch Service domains
• Troubleshooting Amazon OpenSearch Service
• Fine-grained access control in Amazon OpenSearch Service
• UltraWarm storage for Amazon OpenSearch Service
• Cold storage for Amazon OpenSearch Service
• Reserved Instances in Amazon OpenSearch Service
• Amazon OpenSearch Service Pricing
• AWS Pricing Calculator
