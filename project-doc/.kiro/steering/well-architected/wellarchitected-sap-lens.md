---
inclusion: manual
---

# SAP Lens for AWS Well-Architected Framework - Steering Guide

## Document Overview

The SAP Lens for AWS Well-Architected Framework is a collection of customer-proven design principles and best practices for ensuring SAP workloads on AWS are well-architected. It serves as a supplement to the AWS Well-Architected Framework, providing specialized guidance for building secure, high-performing, resilient, and efficient SAP applications on AWS. The document is organized around the six pillars of the AWS Well-Architected Framework: operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

The intended audience includes SAP technology architects, cloud architects, and team members who build, operate, and maintain SAP systems on AWS. The lens is designed to help organizations adopt a cloud-native approach to running SAP workloads on AWS.

## Key Topics

1. Operational Excellence
   • Monitoring and observability for SAP workloads
   • Change management and deployment practices
   • Operational readiness and procedures
   • Continuous improvement and validation

2. Security
   • Security standards and controls
   • Infrastructure and software security
   • Identity and access management
   • Data protection (at rest and in transit)
   • Security monitoring and incident response

3. Reliability
   • Design for failure resilience
   • Failure detection and response
   • Data recovery planning
   • Testing resilience

4. Performance Efficiency
   • Compute solution selection
   • Storage optimization
   • System tuning (OS, database, SAP application)
   • Performance monitoring and optimization

5. Cost Optimization
   • Architecture patterns for cost efficiency
   • Compute resource optimization
   • Data storage optimization
   • Cost management and governance

6. Sustainability
   • Sustainable architecture patterns
   • Infrastructure and software sustainability
   • Sustainability monitoring

## Best Practices

### Operational Excellence

1. Monitoring and Observability
   • Implement prerequisites for monitoring SAP on AWS (AWS Data Provider for SAP, CloudWatch detailed monitoring)
   • Implement infrastructure monitoring for SAP components
   • Implement application and database monitoring
   • Implement workload configuration monitoring
   • Implement user activity monitoring
   • Implement dependency monitoring
   • Create a single pane of glass health dashboard
   • Use automated response and recovery techniques

2. Change Management
   • Use version control and configuration management
   • Implement practices to improve code quality
   • Use build and deployment management systems
   • Use multiple environments (dev, test, prod)
   • Test and validate changes
   • Make frequent, small, and reversible changes
   • Automate testing, integration, and deployment

3. Operational Readiness
   • Ensure personnel capability with appropriate training and certifications
   • Align cloud operating model with operational aims
   • Share design standards and educate support personnel
   • Use runbooks for SAP landscape operations
   • Use playbooks to investigate issues
   • Automate SAP landscape operations

4. Continuous Improvement
   • Understand and plan for lifecycle events
   • Regularly perform patch management
   • Test business continuity plans and fault recovery
   • Perform regular workload reviews for optimization

### Security

1. Security Standards
   • Define security roles and responsibilities
   • Classify data within SAP workloads
   • Determine required security controls based on classification
   • Create a strategy for managing security controls

2. Infrastructure and Software Security
   • Ensure security in network design
   • Build and protect the operating system
   • Protect the database and application
   • Establish a plan for upgrading and patching

3. Identity and Access Management
   • Understand user categories and access mechanisms
   • Manage privileged access
   • Implement identity management approach
   • Implement logging and reporting for access events

4. Data Protection
   • Encrypt data at rest
   • Encrypt data in transit
   • Secure data recovery mechanisms against threats

5. Security Monitoring and Response
   • Implement security event analysis strategy
   • Perform periodic security testing
   • Document security incident response plans

### Reliability

1. Design for Failure
   • Agree on availability goals aligned with business requirements
   • Select appropriate deployment patterns for availability
   • Define approach for critical data availability
   • Validate design against business requirements

2. Detect and React to Failures
   • Monitor failures of applications, resources, and connectivity
   • Define approach to maintain availability
   • Define approach to restore service availability
   • Conduct periodic resilience tests
   • Automate reaction to failures

3. Data Recovery
   • Establish methods for consistent business data recovery
   • Establish methods for configuration data recovery
   • Define recovery approach for complete SAP estate
   • Test recovery procedures regularly

### Performance Efficiency

1. Compute Solution Selection
   • Evaluate or estimate performance requirements
   • Select EC2 instances suitable for SAP workloads
   • Select architectures allowing independent scaling
   • Choose instance location to minimize latency

2. Storage Optimization
   • Create mount points and volume associations by function
   • Select and configure EBS types for performance requirements
   • Evaluate EFS and FSx performance suitability
   • Consider memory as storage alternative
   • Choose appropriate backup solutions

3. System Tuning
   • Follow OS guidelines for SAP performance
   • Modify database parameters for hardware alignment
   • Modify SAP parameters for hardware alignment
   • Consider performance tuning for recovery options

4. Performance Monitoring
   • Collect performance evaluation data
   • Establish baseline performance requirements
   • Identify performance trends
   • Identify and triage performance issues
   • Scale to meet performance demands
   • Simulate production load for analysis
   • Continuously optimize based on performance data

### Cost Optimization

1. Architecture Patterns
   • Evaluate use of SAP managed service offerings
   • Evaluate cost characteristics of application architecture
   • Understand business requirements for cost-optimized design
   • Review instance sizing and availability
   • Consider on-demand capacity for efficiency
   • Evaluate shared services benefits
   • Evaluate automation benefits

2. Compute Resources
   • Understand EC2 payment and commitment options
   • Use cost as key consideration for instance selection
   • Evaluate licensing impact and optimization
   • Evaluate storage cost impact

3. Data Storage
   • Understand access and retention requirements
   • Delete unnecessary data through housekeeping
   • Use compression and reclaim strategies
   • Review backup strategies
   • Consider data tiering options
   • Evaluate archiving options

4. Cost Management
   • Plan consumption model during project phases
   • Establish multi-year cost model with pricing approaches
   • Establish budget and cost allocation mechanisms
   • Establish cost-related approval procedures
   • Review usage for optimization opportunities

### Sustainability

1. Sustainable Architecture
   • Understand business requirements for sustainability
   • Implement infrastructure and software improvements
   • Implement sustainability monitoring

## Guidelines and Recommendations

### SAP Monitoring and Observability

1. AWS Data Provider for SAP
   • Install AWS Data Provider for SAP on each EC2 instance supporting SAP NetWeaver workloads
   • This agent collects performance metrics from AWS services for SAP monitoring tools
   • Required for SAP transaction code ST06n and Solution Manager monitoring

2. Monitoring Strategy
   • Create a comprehensive monitoring strategy covering:
     • Infrastructure (CPU, memory, storage, network)
     • SAP application and database
     • Configuration changes
     • User activity
     • Dependencies and interfaces
   • Implement CloudWatch metrics and alarms for supporting services
   • Monitor AWS service quotas (especially EC2 and EBS)
   • Expose SAP monitoring data outside SAP tools for independent observability

3. Backup and Recovery Monitoring
   • Monitor database backups
   • Monitor database replication
   • Monitor file storage backups
   • Monitor cross-region recovery mechanisms
   • Monitor cross-account recovery mechanisms

### SAP Change Management

1. Version Control
   • Implement version control for all components:
     • Infrastructure
     • Database
     • Application
     • Custom code (ABAP, Java, UI5/JavaScript)
   • Use SAP change control tools for development code
   • Use configuration management systems for operating systems
   • Use infrastructure as code (IaC) for AWS resources

2. Environment Strategy
   • Use temporary environments for experimentation
   • Provide development environments for parallel work
   • Provide test environments that mirror production
   • Use IaC for consistent environment deployment
   • Turn off non-production environments when not in use

3. Testing Approach
   • Test changes at all lifecycle stages
   • Maintain testing baselines
   • Define appropriate testing levels for different changes
   • Automate testing where possible

### SAP Security

1. Network Security
   • Understand SAP traffic flows (inbound, outbound, internal)
   • Evaluate options to permit/restrict traffic
   • Use design guidelines and AWS tooling to simplify management
   • Consider AWS Shield and AWS WAF for public-facing endpoints

2. Operating System Security
   • Follow SAP-specific OS hardening guidelines
   • Implement secure provisioning approaches
   • Establish patching procedures
   • Validate security posture regularly

3. Database and Application Security
   • Follow SAP guidance for database security
   • Follow SAP guidance for application security
   • Subscribe to security alerts from vendors
   • Review and implement security patches promptly

4. Identity and Access Management
   • Understand data access permissions for different user types
   • Manage AWS credentials and authentication
   • Manage SAP administrative credentials
   • Implement centralized identity management
   • Consider multi-factor authentication
   • Manage certificates properly

5. Data Protection
   • Encrypt data at rest using appropriate AWS services
   • Encrypt application traffic using SAP protocols
   • Encrypt internet protocol traffic
   • Encrypt file and message transfers
   • Encrypt administrative access
   • Implement network-level encryption
   • Secure backups in separate accounts with additional controls

### SAP Reliability

1. Availability Planning
   • Identify applications and their interdependencies
   • Classify systems based on failure impact
   • Assess business impact of outages
   • Understand compliance requirements
   • Define acceptable uptime percentages

2. Architecture Selection
   • Identify all required components and services
   • Use SLAs and historical data to assess failure likelihood
   • Assess clustering, resilience, and load balancing options
   • Verify EC2 instance family availability in AZs
   • Implement capacity reservation strategies
   • Design VPC across multiple AZs

3. Data Availability
   • Evaluate MTTR requirements
   • Determine backup recovery scenarios
   • Implement appropriate data replication
   • Ensure consistent configuration and binaries
   • Take holistic approach to data consistency
   • Build strategy for interface replay
   • Consider data bunker for protection

4. Failure Detection and Response
   • Use AWS Personal Health Dashboard
   • Implement CloudWatch monitoring
   • Use SAP monitoring tools
   • Consider third-party monitoring solutions
   • Avoid resource exhaustion
   • Plan for scheduled maintenance
   • Protect single points of failure
   • Consider redundant capacity
   • Ensure capacity for failure scenarios
   • Use inherently available AWS services
   • Follow network connectivity best practices

5. Recovery Planning
   • Enable EC2 instance recovery
   • Use AMIs and IaC for rebuilding
   • Understand EBS failure scenarios
   • React to AWS Health notifications
   • Protect against accidental/malicious events
   • Identify external dependencies

### SAP Performance

1. Compute Selection
   • Reference SAPS metrics for sizing
   • Use SAP EarlyWatch Alert reports for usage details
   • Use SAP HANA sizing reports for HANA workloads
   • Use SAP Quick Sizer for new implementations
   • Consider proof of concept deployments for validation
   • Follow SAP guidance on supported configurations
   • Use hardware metrics and SAPS for selection
   • Be aware of EC2 instance features and throughput

2. Storage Configuration
   • Identify SAP filesystem requirements
   • Map appropriate AWS storage services to functions
   • Use supported filesystem types
   • Evaluate EBS volume types for performance needs
   • Use LVM striping for linear scaling
   • Follow AWS storage guidelines for SAP HANA
   • Evaluate EFS/FSx performance options
   • Consider memory as storage alternative
   • Plan backup windows to minimize performance impact

3. System Tuning
   • Review OS-related SAP notes before changes
   • Use vendor-supplied SAP tuning tools
   • Apply relevant network parameters
   • Review database-specific tuning parameters
   • Allow SAP to self-tune according to PHYS_MEMSIZE
   • Review swap space configuration
   • Optimize backup and recovery performance
   • Configure clustering parameters appropriately

### SAP Cost Optimization

1. Service Provider Evaluation
   • Understand available managed service offerings
   • Define roles and responsibilities for cost control
   • Agree on cost management approach with partners

2. Architecture Cost Considerations
   • Review SAP installation patterns (standalone, distributed, HA)
   • Consider exceptions for multitenancy
   • Evaluate single-host installations for non-critical systems
   • Choose cost-effective AWS Regions
   • Design scalable architectures for failure scenarios
   • Consider minimum compute capacity during failures
   • Evaluate storage-based recovery options
   • Understand networking costs

3. Environment Optimization
   • Evaluate if non-production needs full production data
   • Evaluate if non-production needs production performance
   • Evaluate if non-production needs production operating hours
   • Evaluate if non-production needs production reliability
   • Evaluate requirements for support and legacy systems

4. EC2 Instance Optimization
   • Use smaller instances for flexibility
   • Consider scale-out configurations where supported
   • Use on-demand for systems with reduced hours
   • Implement scheduled or dynamic scaling

5. Licensing Optimization
   • Understand CPU/memory impact on licensing
   • Evaluate operating system purchasing options
   • Consider EC2 Dedicated Hosts for licensing restrictions
   • Evaluate moving away from per-GB or per-core licensing

6. Data Management
   • Categorize business data types and access patterns
   • Implement regular housekeeping for technical tables
   • Control filesystem growth through cleanup
   • Use database compression features
   • Perform regular reorganizations
   • Store backups in appropriate locations with lifecycle policies
   • Implement data tiering and archiving

## Important Concepts

1. SAP Workload
   • A collection of SAP resources delivering business value
   • Includes customer-facing components and backend processes
   • May span multiple AWS accounts

2. AWS Shared Responsibility Model
   • AWS is responsible for security "of" the cloud
   • Customer is responsible for security "in" the cloud
   • Applies to security, reliability, and operational aspects

3. SAP System Components
   • **SAP SID**: System Identifier uniquely identifying an SAP system
   • **SAP Technical Components**: Administrative units (Application Server, Database, Web Dispatcher)
   • **SAP Environment**: Integrated grouping forming path to production (Dev, QA, Prod)

4. SAPS Rating
   • SAP Application Performance Standard
   • Hardware-independent unit measuring system performance
   • 100 SAPS = 2,000 fully processed order line items per hour

5. SAP Deployment Patterns
   • **Standalone**: All components on a single host
   • **Distributed**: Components spread across multiple hosts
   • **High Availability (HA)**: Redundant components for resilience

6. Recovery Objectives
   • **Recovery Time Objective (RTO)**: Maximum acceptable time to restore service
   • **Recovery Point Objective (RPO)**: Maximum acceptable data loss period
   • **Mean Time to Recovery (MTTR)**: Average time to restore service

7. AWS Pricing Models
   • **On-Demand**: Pay by the hour with no commitment
   • **Reserved Instances**: Commitment-based discount (Standard or Convertible)
   • **Savings Plans**: Commitment to spend for discount (Compute or EC2 Instance)

## Examples and Use Cases

1. SAP Monitoring Integration
  

   Implement CloudWatch metrics and alarms for common problems affecting SAP:
   - Amazon EC2 high CPU utilization
   - Amazon EC2 high memory utilization
   - Amazon EBS storage paging
   - Amazon EBS storage throughput
   - Amazon EBS storage IOPS
   - Amazon EBS storage space free
   - Amazon EC2 network saturation
   - ELB/ALB health and target group health
   


2. SAP High Availability Architecture
  

   For a three Availability Zone architecture with 150% capacity:
   - AZ1: 50% of required capacity
   - AZ2: 50% of required capacity
   - AZ3: 50% of required capacity
   
   If any single AZ fails, the remaining two AZs still provide 100% of required capacity.
   


3. SAP Cost Optimization Timeline
  

   Example timeline for planning SAP on AWS compute commitments:
   - Year 1-3: 3-year commitment for stable core systems
   - Year 1: 1-year commitment for systems with uncertain future
   - Month-to-month: On-demand for temporary or project systems
   - Adjust commitments as systems stabilize or requirements change
   


4. SAP Storage Layout for HANA
  

   For SAP HANA storage configuration:
   - Use gp3 or io2 volumes for data and log
   - Implement LVM striping with 256KB stripe size for data volumes
   - Implement LVM striping with 64KB stripe size for log volumes
   - Follow AWS-provided storage layout that balances performance, cost, and durability
   


5. SAP System Shutdown for Cost Savings
  

   For a training system used 40 hours per week:
   - Using on-demand pricing (~23% uptime) is cheaper than running 24/7 with a 3-year Reserved Instance
   - Implement automated start/stop schedules
   - Consider AWS Systems Manager Automation for orchestration
   


## Cautions and Limitations

1. SAP Support Prerequisites
   • AWS Data Provider for SAP is required for SAP NetWeaver workloads
   • CloudWatch detailed monitoring must be enabled
   • SAP enhanced monitoring must be configured
   • Business Support or higher AWS support plan is required

2. EC2 Instance Availability
   • Some EC2 instance families (X and U series) are not available in all AZs
   • Verify instance availability in target AZs during planning
   • Logical AZ identifiers may differ across AWS accounts

3. SAP HANA Deployment Restrictions
   • SAP HANA has specific certified EC2 instance types
   • Scale-out deployments require cluster placement groups
   • S/4HANA has limited scale-out support with restrictions

4. Network Latency Requirements
   • SAP provides guidance for acceptable network latency
   • Multi-AZ deployments may impact performance for latency-sensitive transactions
   • Use SAP Logon Groups and batch server groups to optimize placement

5. Licensing Considerations
   • Database licensing policies may impact architecture decisions
   • Oracle, SQL Server, and IBM Db2 have specific licensing requirements
   • Consider SAP Runtime database licensing model as alternative

6. Spot Instances Limitations
   • AWS Spot Instances can be reclaimed with two-minutes notice
   • Not generally suited for running SAP workloads

7. SAP Application Server Scaling
   • Consider impact on user connections and batch jobs when scaling down
   • SAP components are stateful, requiring careful shutdown procedures

8. Data Protection Limitations
   • SAP HANA data-at-rest encryption root keys can only be stored in instance secure store or SAP Data Custodian
   • Some database encryption features require additional licenses

## Additional Resources

1. AWS Documentation
   • AWS Well-Architected Framework
   • AWS Data Provider for SAP
   • Architecture Guidance for Availability and Reliability of SAP on AWS
   • SAP HANA on AWS: High Availability Configuration Guide
   • SAP NetWeaver on AWS: Monitoring Guide
   • AWS Launch Wizard for SAP

2. SAP Resources
   • SAP Product Availability Matrix (PAM)
   • SAP Notes (requires SAP Portal access):
     • 1656250: SAP on AWS: Support Prerequisites
     • 1656099: SAP Applications on AWS: Supported DB/OS and Amazon EC2 products
     • 2408419: SAP S/4HANA - Multi-Node Support
   • SAP Solution Manager 7.2 - Application Operations
   • SAP HANA Administration Guide
   • SAP NetWeaver Security Guide

3. AWS Services for SAP
   • AWS Launch Wizard for SAP
   • AWS Backint Agent for SAP HANA
   • Amazon CloudWatch Application Insights for SAP HANA
   • AWS Systems Manager for SAP
   • AWS Cloud Migration Factory for SAP

4. Blogs and Community
   • SAP on AWS Blog
   • AWS re:Post - SAP on AWS topic
   • AWS Marketplace: Products and Tools for SAP Monitoring
   • AWS Marketplace: Products and Tools for DevOps
   • AWS Marketplace: Products and Tools for Testing
