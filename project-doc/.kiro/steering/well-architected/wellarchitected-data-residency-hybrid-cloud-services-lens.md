---
inclusion: manual
---

# AWS Data Residency and Hybrid Cloud Lens - Steering File

## Document Overview

This document presents the Data Residency with Hybrid Cloud Services Lens (DRHC) for the AWS Well-Architected Framework. 
Published on April 3, 2025, it provides comprehensive guidance for designing and operating Well-Architected hybrid cloud 
workloads with data residency requirements. The lens covers best practices across the six pillars of the AWS Well-Architected 
Framework: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

The DRHC Lens helps organizations optimize their hybrid cloud infrastructure while maintaining control over their data's 
geographic location to comply with local laws and regulations. It draws from extensive experience in architecting cloud 
solutions to address the unique challenges of managing data residency requirements in hybrid environments.

## Key Topics

1. Data Residency Definitions and Concepts
   • AWS definitions (Outposts, Local Zones, Regions, etc.)
   • Industry definitions (data residency, data sovereignty, etc.)

2. Design Principles for Hybrid Cloud with Data Residency
   • Data classification
   • Operational practices for data sovereignty
   • Using regional cloud services with on-premises solutions
   • Infrastructure automation

3. Data Residency Scenarios
   • User and audit consent for data storage outside country
   • Sharing data across countries with similar standards
   • Maintaining primary service copy within country
   • In-country data storage and processing requirements

4. Operational Excellence for Hybrid Edge Workloads
   • Understanding data residency regulations
   • Choosing between AWS Local Zones and AWS Outposts
   • Business continuity planning
   • Network connectivity design
   • Monitoring and alerting

5. Security for Data Residency
   • Control objectives and workload separation
   • Identity and access management
   • Detection mechanisms
   • Infrastructure protection
   • Data protection and incident response

6. Reliability for Hybrid Cloud
   • Service quotas management
   • Redundant power and network
   • Workload architecture for failover
   • Capacity planning
   • Failure management

7. Performance Efficiency
   • Architecture selection based on data residency
   • Monitoring hybrid edge metrics
   • Network traffic optimization
   • Workload health KPIs

8. Cost Optimization
   • Tagging strategy for hybrid edge workloads
   • Capacity and utilization management
   • Workload placement optimization
   • Data lifecycle management
   • Network configuration optimization

9. Sustainability
   • Region selection for sustainability
   • Alignment to demand
   • Resource utilization monitoring
   • Data management practices
   • Hardware and services selection

## Best Practices

### Organization and Planning

1. Data Classification
   • Classify which workloads and datasets need to stay on-premises and which can be moved to the Region
   • Conduct data classification exercises for individual fields in datasets
   • Align data with relevant data privacy laws and industry-specific regulations

2. Account Management
   • Separate workloads with different data residency requirements into different AWS accounts
   • Group workloads with similar data residency requirements in the same Organizational Units (OUs)
   • Apply Service Control Policies (SCPs) at the OU level to minimize overhead

3. Regulatory Compliance
   • Understand specific legal and compliance requirements for data residency
   • Document any differences in the treatment of log data in control objectives
   • Build feedback loops to adapt to changing data residency requirements

### Infrastructure Selection and Design

1. Service Selection
   • Consider AWS Outposts for data residency requirements when control over data and physical location is needed
   • Consider AWS Local Zones for low-latency access from specific geographic locations
   • Choose the Local Zone anchored to the Region that best aligns with sustainability goals

2. Network Design
   • Design robust network connectivity for Outposts and Local Zone workloads
   • Build redundant network connectivity using AWS Direct Connect with redundant tunnels
   • Engineer optimal traffic flow for edge solutions using local VPC peering over AWS Transit Gateway

3. Storage Options
   • Review available data storage options to keep data within required geographic boundaries
   • Consider sustainable object storage options for Local Zones
   • Use Amazon S3 on Outposts or deploy self-managed shared-file solutions to minimize data duplication

### Operations and Monitoring

1. Capacity Management
   • Set service quotas to accommodate peak usage of AWS resources on Outposts
   • Plan ahead for required compute, storage, and network resources due to finite Outposts capacity
   • Provision spare compute capacity following an N+M model

2. Monitoring and Alerting
   • Implement proper monitoring practices to track resource utilization and application health
   • Understand monitoring requirements specific to Local Zones and Outposts
   • Develop processes for each alert defined for Outposts and Local Zone workloads

3. Automation
   • Use AWS services and tools for automation and infrastructure as code (IaC) across hybrid environments
   • Implement failover automation and test disaster recovery strategies
   • Automate infrastructure based on data classification

### Security Implementation

1. Control Objectives
   • Update control objectives to address data residency compliance requirements
   • Implement controls that enhance digital sovereignty governance posture
   • Deploy AWS Control Tower digital sovereignty group of controls

2. Access Control
   • Restrict access by location of resource using IAM policies
   • Grant least privilege access with focus on actions that enable data storage
   • Implement permission guardrails for organizations

3. Detection and Protection
   • Implement detective controls to notify security teams when resources are in unauthorized locations
   • Restrict physical access to AWS Outposts locations
   • Implement network traffic inspection-based protection

4. Data Protection
   • Implement backups to enable recovery from data corruption and deletion
   • Configure Amazon EBS snapshots and S3 Versioning on Outposts
   • Enable S3 Replication on Outposts to replicate objects to another Outpost

### Disaster Recovery and Business Continuity

1. Recovery Planning
   • Understand RTO and RPO requirements and build appropriate disaster recovery solutions
   • Determine factors that influence data replication strategy
   • Deploy multiple Outposts anchored to different Availability Zones or Regions for high availability

2. Failure Management
   • Design environments to maintain availability during failures in critical sub-systems
   • Maintain high availability during on-premises maintenance activities
   • Use AWS Health to receive EC2 instance retirement notifications and scheduled events

## Guidelines and Recommendations

### Data Residency Scenario Selection

1. Scenario A: User and audit consent for data storage outside country
   • Applicable when regulations allow data storage outside the country with user consent
   • Requires validation checks for consent and compliance with country regulations
   • Data can be stored in Region Y if preconditions are satisfied

2. Scenario B: Sharing data across countries with similar standards
   • Applicable when transfer is allowed to countries with same/higher data protection standards
   • Requires checking available Regions against origin country standards
   • Select Region Y when it meets the requirements

3. Scenario C: Primary service copy within country
   • Primary copy of data must be maintained within the country
   • Two deployment options:
     • Option 1: Use AWS Local Zones and AWS Outposts in corporate data centers
     • Option 2: Use AWS Outposts only in corporate data centers

4. Scenario D: In-country data storage and processing
   • All in-scope data must be stored and processed within country borders
   • Two deployment options:
     • Option 1: Use AWS Local Zones and AWS Outposts with strict SCPs
     • Option 2: Use AWS Outposts only with custom controls

### Implementation Guidelines

1. AWS Outposts Implementation
   • Verify facilities meet requirements to operate within laws for regulated workloads
   • Provision redundant power and network to on-premises components
   • Plan ahead for compute, storage, and network capacity requirements
   • Monitor and manage capacity utilization effectively

2. AWS Local Zones Implementation
   • Design network connectivity similar to Availability Zones
   • Monitor and scale workloads to match demand
   • Use only the minimum required resources for sustainability
   • Consider AWS-managed file services to minimize data duplication

3. Security Controls Implementation
   • Deploy SCPs to deny specific actions that could violate data residency
   • Create detective controls using AWS Config Rules or Cloud Custodian
   • Automate remediation of findings where possible
   • Train incident responders on data residency policies

4. Network Configuration
   • Use local gateway path instead of service link path for Outposts
   • Route internet traffic over local gateway path where possible
   • Provision redundant network paths between Outpost LGW and critical on-premises resources
   • Use dynamic routing to automate traffic redirection around failures

## Important Concepts

1. Data Residency vs. Data Sovereignty
   • **Data residency**: The requirement of keeping data in a certain region or country to comply with local laws and 
regulations.
   • **Data sovereignty**: An organization or country's ability to have full control and ownership over the data they generate
and store, including where it's stored, who can access it, and providing resilience from external factors.

2. AWS Hybrid Edge Services
   • **AWS Outposts**: A fully managed service that extends AWS infrastructure, services, APIs, and tools on premises for a 
consistent hybrid experience.
   • **AWS Local Zones**: A type of infrastructure deployment that places select AWS services closer to end users and 
workloads.
   • **AWS Regions**: Physical locations around the world where AWS clusters data centers.
   • **Availability Zone (AZ)**: One or more discrete data centers with redundant power, networking, and connectivity in an 
AWS Region.

3. Control Plane vs. Data Plane
   • **Control plane**: Provides administrative APIs used to create, read, update, delete, and list resources.
   • **Data plane**: Provides the primary function of the service (e.g., running EC2 instance, reading/writing to EBS volume).

4. Shared Responsibility Model for Outposts
   • AWS is responsible for the hardware and software that run AWS services
   • Customers are responsible for capacity planning, physical security, and network connectivity
   • Customers must provide dual power sources and redundant network connectivity

5. Recovery Objectives
   • **Recovery Time Objective (RTO)**: Maximum acceptable duration of downtime before recovery
   • **Recovery Point Objective (RPO)**: Maximum acceptable amount of data loss or age of recoverable data

## Examples and Use Cases

### Example 1: Multi-Outpost High Availability Architecture

For a scenario where data must be stored and processed in-country:
1. Deploy AWS Outposts racks in multiple data centers within the country
2. Anchor each Outpost to a different Availability Zone for resilience
3. Implement load balancing across Outposts using Application Load Balancers and Amazon Route 53
4. Configure Amazon S3 on Outposts for local data storage
5. Use Amazon EBS local snapshots for backup and recovery
6. Implement EC2 Auto Scaling groups for automatic recovery from failures

### Example 2: Local Zone with Region Backup

For a scenario where primary copy must stay in-country but backups can be stored elsewhere:
1. Deploy primary workload in AWS Local Zone within the country
2. Configure data replication to AWS Region for backup purposes
3. Use AWS Direct Connect for secure, high-performance connectivity
4. Implement Amazon CloudWatch for monitoring and alerting
5. Set up automated failover mechanisms within the Local Zone

### Example 3: Tagging Strategy for Cost Attribution

For hybrid edge workloads spanning multiple environments:
1. Define consistent tagging schema across all resources
2. Activate tags as cost allocation tags in Cost and Usage Report
3. Tag resources with attributes like:
   • Data classification level
   • Compliance requirements
   • Business unit
   • Environment (dev, test, prod)
4. Use AWS Config to enforce tagging policies
5. Create CloudWatch dashboards to visualize costs by tag

## Cautions and Limitations

1. Service Availability Limitations
   • Not all AWS services are available in Local Zones and Outposts
   • Local Zones provide only a subset of EC2 instance families and types
   • AWS WAF, AWS Network Firewall, and Advanced level of AWS Shield are not supported in Edge services

2. Capacity Constraints
   • Outposts have fixed and finite capacity that cannot be quickly scaled
   • Capacity planning is critical for Outposts to avoid running out of resources
   • Spare capacity must be maintained for resilience (N+M model recommended)

3. Network Connectivity Risks
   • Outposts depend on connection to parent Region for management and monitoring
   • Network disruptions can impact control plane operations
   • During disconnect events, mutating requests and control plane operations will fail

4. Data Transfer Considerations
   • Data transfer from Outposts to AWS Regions is free
   • Transfers from Regions to Outposts are more expensive over internet vs. Direct Connect
   • Local Zones have internet gateways for local egress, but routing to Regions incurs charges

5. Maintenance and Hardware Failures
   • Hardware on AWS Outposts can eventually fail and need replacement
   • If AWS detects irreparable issues, affected instances are scheduled for retirement
   • Without additional capacity, instances may remain in stopped state

6. Compliance Verification
   • Organizations must verify that their implementation meets specific regulatory requirements
   • AWS provides tools but ultimate compliance responsibility lies with the customer
   • Backup and snapshot considerations must be validated with relevant regulators

## Additional Resources

1. AWS Documentation
   • AWS Outposts User Guide
   • AWS Local Zones User Guide
   • AWS Well-Architected Framework
   • Data Residency Whitepaper
   • Addressing Data Residency Requirements with AWS

2. Implementation Guides
   • Architecting for data residency with AWS Outposts rack and landing zone guardrails
   • Best Practices for managing data residency in AWS Local Zones using landing zone controls
   • Architecting for Disaster Recovery on AWS Outposts racks with AWS Elastic Disaster Recovery
   • Monitoring best practices for AWS Outposts
   • Connectivity options for Local Zones

3. Whitepapers
   • Data Residency Whitepaper
   • Addressing Data Residency Requirements with AWS
   • Operational observability
   • Hybrid Networking Lens - Operational excellence pillar
   • AWS Outposts High Availability Design and Architecture Considerations

4. Tools and Services
   • AWS Control Tower
   • AWS Organizations
   • AWS Config
   • AWS CloudWatch
   • AWS Health
   • AWS Systems Manager
   • AWS DataSync

5. Blogs and Videos
   • Deploying an automated Amazon CloudWatch dashboard for AWS Outposts using AWS CDK
   • re:Invent 2024 SEC360: Respond and recovery faster with AWS Security Incident Response
