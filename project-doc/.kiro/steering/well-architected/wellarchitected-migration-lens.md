---
inclusion: manual
---

# AWS Migration Lens Steering File

## Document Overview

This document presents the Migration Lens for the AWS Well-Architected Framework, providing customers with best practices and 
guidance for migrating on-premises or hybrid workloads to a fully cloud-based implementation on AWS. It combines the three 
phases of migration (assess, mobilize, and migrate and modernize) with the six pillars of the AWS Well-Architected Framework (
operational excellence, security, reliability, performance efficiency, cost optimization, and sustainability) to help reduce 
cloud migration risks and implement AWS best practices.

## Key Topics

1. Migration Lifecycle and Phases
   • Assess phase
   • Mobilize phase
   • Migrate and modernize phase

2. Well-Architected Framework Pillars in Migration Context
   • Operational excellence
   • Security
   • Reliability
   • Performance efficiency
   • Cost optimization
   • Sustainability

3. Migration Strategies (7 Rs)
   • Retire
   • Retain
   • Rehost
   • Relocate
   • Repurchase
   • Replatform
   • Refactor

4. Migration Design Principles

5. Migration Planning and Execution

6. Post-Migration Optimization

## Best Practices

### Migration Design Principles

1. Create a clear vision for the journey: Define business goals for migration and consider transformation of both business and 
technology.

2. Get leadership support early: Secure executive sponsorship for organizational alignment and timely decision-making. Consider
forming a Cloud Center of Excellence (CCoE).

3. Understand the AWS environment: Learn about AWS differences from traditional data centers. Define AWS accounts strategy and 
leverage AWS Control Tower and AWS Organizations.

4. Define migration scope: Determine what to migrate and the migration strategy.

5. Know your applications: Define what "good" looks like when moving to AWS and choose appropriate migration strategies.

6. Get application owners' buy-in early: Understand application dependencies (technical and business, internal and external).

7. Understand application requirements: Consider performance, utilization, resiliency, security, compliance, and operations. 
Optimize workloads after migration.

8. Align with governance and compliance frameworks: Incorporate security best practices in your migration strategy.

9. Maintain operations during migration: Plan for hybrid environment operations and cloud-only operations.

10. Create migration plans: Split migration into smaller units (waves), test, validate, and repeat. Create or adapt operational
runbooks.

### Operational Excellence

#### Assess Phase
• Ensure migration planning considers scope, technology, and process
• Base migration plans on up-to-date data from discovery exercises
• Refresh data regularly for long-running migrations

#### Mobilize Phase
• Define and measure KPIs aligned with business outcomes
• Assess team skills and implement training plans
• Ensure bandwidth for operating workloads while migrating
• Establish a Cloud Center of Excellence (CCoE)
• Define a cloud operations strategy
• Align AWS operational requirements with existing tools
• Test operations in the cloud regularly
• Calculate migration velocity considering technical and non-technical factors

#### Migrate Phase
• Implement a testing phase strategy
• Review application lifecycle management (CI/CD pipeline)
• Provision resources through infrastructure as code (IaC) templates

### Security

#### Assess Phase
• Review security aspects of discovery tools
• Map existing security tools to AWS equivalents
• Establish compliance frameworks

#### Mobilize Phase
• Implement strong identity and least privilege principles
• Build AWS environment following security foundations
• Establish secure connectivity between on-premises and AWS
• Define policies for data encryption at rest
• Apply application security controls
• Establish data backup and disaster recovery strategy
• Set up monitoring controls
• Review third-party integrations for security

#### Migrate Phase
• Review security of migration tools
• Implement detection and investigation capabilities
• Establish incident response capabilities
• Protect compute and network resources
• Implement authentication and authorization for applications and databases

### Reliability

#### Assess Phase
• Define SLAs across all applications and environments
• Define and automate runbooks
• Map AWS Global Infrastructure to business SLAs
• Set up tools to monitor SLAs
• Keep business impact analysis up-to-date
• Update risk assessment for cloud-specific disaster events
• Define RPO and RTO targets
• Select disaster recovery strategy based on cloud best practices
• Estimate required maintenance windows for migration cutover

#### Mobilize Phase
• Review service quotas and constraints
• Plan network topology for migration
• Ensure sufficient bandwidth for normal traffic and data replication
• Implement highly available links to on-premises
• Design networks to prevent IP address conflicts
• Implement reliable DNS design
• Test network performance and component failure
• Establish backup strategies for migrated workloads
• Utilize fault isolation for migrated workloads

#### Migrate Phase
• Test high availability, fault tolerance, and disaster recovery

### Performance Efficiency

#### Assess Phase
• Evaluate performance requirements for workloads
• Identify existing OS platforms to meet performance requirements
• Find efficient data transfer methods
• Select optimal storage options
• Identify network requirements
• Manage IP address conflicts and DNS requirements

#### Mobilize Phase
• Set up metrics for performance monitoring
• Select best-performing cloud infrastructure that can scale
• Reduce blast radius for performance impact
• Benchmark existing workloads

#### Migrate Phase
• Perform stress and user acceptance tests
• Implement lessons learned from previous migration waves
• Perform Well-Architected Framework Reviews after each iteration
• Monitor performance through all migration phases
• Generate alarm-based notifications for metrics threshold breaches
• Implement monitoring dashboards
• Set up automated testing for application metrics
• Re-evaluate compute usage with optimization tools

### Cost Optimization

#### Assess Phase
• Assess existing infrastructure usage and application dependencies
• Leverage AWS programs designed to accelerate migrations

#### Mobilize Phase
• Use automation efficiently for migration
• Minimize applications and data to be migrated
• Right-size replication servers
• Set up cost and usage governance with IAM policies
• Define cost allocation strategy
• Design strategy to monitor and analyze AWS costs

#### Migrate Phase
• Create metrics strategy for cloud economics
• Monitor spend with budgeting and forecasting tools
• Use AWS Cost Anomaly Detection
• Implement cost dashboards
• Select right purchase options and scalable architecture
• Identify resources for future cost optimization
• Use cost optimization tools
• Prioritize workloads for modernization to drive cost optimization

### Sustainability

#### Assess Phase
• Include sustainability considerations in migration business case
• Choose AWS Regions based on business requirements and sustainability goals

#### Mobilize Phase
• Optimize cloud resources to minimize idle resources
• Consider sustainability when selecting applications for migration
• Adopt sustainability metrics
• Implement efficient workload design
• Leverage underlying infrastructure efficiency
• Use software and architecture patterns that support sustainability
• Consolidate or retire underutilized environments
• Optimize data access patterns and lifecycle

#### Migrate Phase
• Implement sustainable data management practices
• Adopt methods to reduce interim resource consumption during migration

## Guidelines and Recommendations

### Migration Planning
1. Discovery and Assessment:
   • Use discovery tools to gather comprehensive data about your environment
   • Understand application dependencies to create migration wave plans
   • Collect fine-grained infrastructure usage data (CPU, memory, disk I/O)
   • Gather data with frequent samples over at least two weeks

2. Migration Strategy Selection:
   • Choose appropriate migration strategies (7 Rs) based on application requirements
   • Retire: Shut down applications that are no longer needed
   • Retain: Keep applications in source environment if not ready to migrate
   • Rehost: Move applications without changes (lift and shift)
   • Relocate: Transfer servers in bulk from on-premises to cloud version
   • Repurchase: Replace application with different version or product
   • Replatform: Move application with some optimization
   • Refactor: Move application with architecture modifications to leverage cloud-native features

3. Team Preparation:
   • Conduct AWS Learning Needs Analysis to evaluate roles and develop training plans
   • Structure training into prerequisites, fundamentals, and advanced levels
   • Consider engaging AWS ProServe or certified AWS Migration Competency Partners
   • Run AWS Experience Based Accelerator (EBA) for hands-on experience

4. Resource Planning:
   • Build a comprehensive resource model for migration
   • Consider workstreams, roles, and team composition
   • Augment teams with skilled resources from other parts of organization or partners
   • Consider AWS Managed Services to extend operational capabilities

### Migration Execution

1. Network Preparation:
   • Establish secure connectivity between on-premises and AWS
   • Use AWS Direct Connect for large bandwidth requirements
   • Design networks to prevent overlapping IP addresses
   • Complete DNS design for resolution between environments
   • Test network performance and component failure

2. Security Implementation:
   • Implement multi-account structure for isolation
   • Establish secure connectivity to AWS
   • Set up network security controls
   • Implement data encryption at rest and in transit
   • Apply application security controls
   • Set up monitoring and incident response capabilities

3. Migration Waves:
   • Split migration into smaller units (waves)
   • Calculate potential migration velocity considering technical and non-technical factors
   • Consider network bandwidth, team availability, and change freezes
   • Test migration windows and impact
   • Plan for failure and establish rollback procedures

4. Testing Strategy:
   • Use risk-based, points-of-change testing strategy
   • Test network latencies before moving workloads
   • Test application performance before and after migration
   • Perform test cutovers in isolated environments

5. Cutover Planning:
   • Estimate required maintenance windows
   • Test migration activities to validate completion within maintenance window
   • Define communication channels and intervals
   • Determine data synchronization approach for rollbacks

### Post-Migration Optimization

1. Cost Optimization:
   • Right-size infrastructure based on actual usage
   • Leverage appropriate purchase options (Reserved Instances, Savings Plans, Spot Instances)
   • Enable autoscaling where appropriate
   • Tag resources for future optimization
   • Use AWS cost optimization tools regularly

2. Performance Monitoring:
   • Set up CloudWatch or QuickSight dashboards
   • Generate alarm-based notifications for metrics threshold breaches
   • Implement automated testing for applications
   • Re-evaluate compute usage with optimization tools

3. Continuous Improvement:
   • Perform Well-Architected Framework Reviews after each migration wave
   • Review and implement lessons learned
   • Re-evaluate migration strategies based on experience
   • Consider modernization opportunities

## Important Concepts

### AWS Migration Acceleration Program (MAP)
A comprehensive cloud migration program based on AWS experience with thousands of enterprise customers. MAP provides tools to 
reduce costs, automate execution, and accelerate results, along with training approaches, expertise from AWS Professional 
Services, partner ecosystem, and AWS investment.

### Cloud Center of Excellence (CCoE)
A multi-disciplinary team assembled to implement governance, best practices, training, and architecture needed for cloud 
adoption in a repeatable manner. The CCoE transforms the IT organization from an on-premises operating model to a Cloud 
Operating Model (COM).

### Landing Zone
The foundational components built during the mobilize phase, including AWS accounts, networking, and security, before 
workloads move to AWS. This provides ongoing account management, governance, and implementation of AWS best practices.

### Migration Waves
Groups of applications and their dependencies combined for migration over a 4-8 week period. Waves typically contain one or 
more migration events and help address challenges of dependency mapping.

### Shared Responsibility Model
Defines security responsibilities between AWS and customers. AWS is responsible for security "of" the cloud (infrastructure), 
while customers are responsible for security "in" the cloud (determined by the AWS services used).

### Migration Velocity
The rate at which servers and applications can be migrated, influenced by factors such as people resources, network bandwidth,
application complexity, and change management processes.

## Examples and Use Cases

### Migration Velocity Calculation Example
│ "Let's assume a customer has 1,000 servers to migrate in order to vacate their source data center. They're planning to 
rehost all of their servers using the AWS Application Migration Service (MGN) and have calculated it'll take approximately 
five weeks to complete a migration wave from an end-to-end perspective (including change control, governance, migrating the 
data, and acceptance testing). On average, their migration waves include 50 servers, so with one migration team it could take 
approximately two years to complete (100 weeks). However, they have sufficient network bandwidth and people to increase this 
to four migration teams working in parallel, so their migration could take approximately 25 weeks to complete. During the 25-
week window, there's a two week change freeze where all migrations are impacted, which means their total estimated migration 
duration is 27 weeks, with an average velocity of 200 servers every five weeks."

### Network Testing Example
│ "Testing how applications respond to connectivity events can be performed using AWS Fault Injection Service. For more 
detail, see Tutorial: Simulate a connectivity event."

### Storage Selection Example
│ "Use provisioned IOPS SSD (io1) volumes for high performance databases and transactional workloads. io1 provides low latency
and the ability to provision high IOPS. However, it is more expensive than other EBS types.
│ 
│ Use general purpose SSD (gp2) volumes for most workloads. gp2 provides a good blend of price and performance. You can 
provision up to 16,000 IOPS per volume.
│ 
│ Use throughput optimized HDD (st1) for large, sequential workloads like log processing. st1 provides low cost per GB of 
storage.
│ 
│ Use cold HDD (sc1) for infrequently accessed storage. sc1 is the lowest cost EBS storage."

## Cautions and Limitations

1. Migration Tool Security:
  > "Organizations have to meet different security and compliance standards. Ensure you fully understand the impact of any 
discovery tool against your security posture by assessing the risk profile of the discovery tool, how the data about on-
premises environment is collected, where the data is stored, and how the stored data is secured."

2. Testing Limitations:
  > "When using a rehost migration pattern, your source workloads are cloned into AWS, and when they launch on the Amazon EC2
platform, they may attempt to speak to the services and applications which are still hosted on-premises. This could cause 
outages to your live systems and corrupt application data, so any testing with cloned workloads must be performed within an 
isolated network environment, or while the source systems are powered off."

3. Service Quotas:
  > "Service quotas exist to prevent accidentally provisioning more resources than you need, and to limit request rates on 
API operations so as to protect services from abuse. Migrations can add new resources to existing accounts and therefore 
affect service quotas. Migration services have quotas which can affect the speed migrations can be performed."

4. Network Considerations:
  > "If network connectivity is disrupted, migration replication may need to be restarted."

5. IP Address Conflicts:
  > "Design networks to prevent overlapping IP addresses with your on-premises network. Select new IP ranges to be assigned 
to AWS VPCs which do not clash with any existing networks. Even though some networks may eventually by freed by the migration,
both networks are in use during the migration and difficult to free up until the end of the migration."

## Additional Resources

1. AWS Well-Architected Framework Whitepaper
   • Provides architectural best practices for designing and operating reliable, secure, efficient, cost-effective, and 
sustainable systems in the cloud

2. AWS Migration Tools:
   • AWS Application Migration Service (MGN)
   • AWS Database Migration Service (DMS)
   • AWS Migration Hub
   • Cloud Migration Factory
   • AWS DataSync
   • AWS Transfer Family
   • AWS Snow Family

3. AWS Services for Migration:
   • AWS Control Tower
   • AWS Organizations
   • AWS Direct Connect
   • AWS VPN
   • AWS Transit Gateway
   • AWS PrivateLink
   • AWS Backup
   • AWS Elastic Disaster Recovery

4. AWS Migration Programs:
   • AWS Migration Acceleration Program (MAP)
   • MAP specialized workloads (Mainframe, Windows, Storage, VMware Cloud on AWS, SAP, Databases, and Connect)
   • AWS Experience Based Accelerator (EBA)
   • Migration Immersion Day

5. AWS Cost Management Tools:
   • AWS Cost Explorer
   • AWS Budgets
   • AWS Cost Anomaly Detection
   • AWS Compute Optimizer
   • AWS Trusted Advisor

6. AWS Security Services:
   • AWS Identity and Access Management (IAM)
   • AWS Directory Service
   • AWS IAM Identity Center
   • Amazon Cognito
   • AWS Key Management Service (KMS)
   • AWS CloudHSM
   • AWS Web Application Firewall (WAF)
   • AWS Shield
   • Amazon GuardDuty
   • AWS Security Hub
   • Amazon Detective

7. AWS Monitoring and Observability:
   • Amazon CloudWatch
   • AWS X-Ray
   • AWS CloudTrail
   • Amazon CloudWatch Synthetic Monitoring
