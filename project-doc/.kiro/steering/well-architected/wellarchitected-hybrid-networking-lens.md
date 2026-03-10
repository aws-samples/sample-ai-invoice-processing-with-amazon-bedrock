---
inclusion: manual
---

# AWS Well-Architected Framework: Hybrid Networking Lens Steering Guide

## Document Overview

This document presents the Hybrid Networking Lens for the AWS Well-Architected Framework, which helps customers review and 
improve their cloud-based architectures with a focus on hybrid networking. It provides architectural best practices for 
designing and operating reliable, secure, efficient, and cost-effective hybrid networking systems that connect AWS and on-
premises environments. The lens is structured around the six pillars of the Well-Architected Framework: operational 
excellence, security, reliability, performance efficiency, cost optimization, and sustainability.

## Key Topics

1. Definition and Components of Hybrid Networking
   • Data layer components (AWS VPN, Direct Connect, Transit Gateway)
   • Monitoring and configuration management
   • Security considerations

2. General Design Principles
   • Site-to-Site VPN connectivity
   • Fiber connectivity for critical workloads

3. Operational Excellence in Hybrid Networking
   • IP address allocation
   • Health monitoring
   • Operational event management

4. Security in Hybrid Networking
   • Identity and access management
   • Detection controls
   • Infrastructure protection
   • Data protection
   • Incident response

5. Reliability in Hybrid Networking
   • Service quotas management
   • Change management
   • Failure management

6. Performance Efficiency in Hybrid Networking
   • Connectivity option selection
   • Performance requirements definition
   • Monitoring and scaling
   • Performance tradeoffs

7. Cost Optimization in Hybrid Networking
   • Usage monitoring
   • Data transfer cost identification
   • Cost-effective resource selection
   • Demand and supply management
   • Architecture optimization for data transfer

## Best Practices

### Operational Excellence

1. IP Address Allocation
   • Implement a well-defined IP address allocation scheme to enable efficient routing
   • Avoid overlapping CIDR ranges between VPC and on-premises networks
   • Track IP prefixes and allocate CIDR ranges systematically
   • Right-size CIDR ranges for VPCs based on workload requirements

2. Health Monitoring
   • Use Amazon CloudWatch to collect and process metrics from AWS Direct Connect
   • Monitor VPN tunnels using CloudWatch for near real-time metrics
   • Leverage AWS Transit Gateway statistics and logs for monitoring
   • Use AWS Transit Gateway Network Manager for a global view of your network

3. Operational Event Management
   • Use AWS Health Dashboard to receive notifications for scheduled maintenance
   • Prepare for unplanned outages with redundant connections
   • Enable Bidirectional Forwarding Detection (BFD) for fast detection and failover
   • Test high-availability design and configuration periodically

### Security

1. Identity and Access Management
   • Implement a landing zone with AWS Control Tower for secure multi-account environments
   • Create a separate Central Networking cloud account for network specialists
   • Apply the principle of least privilege for network resources
   • Restrict sensitive APIs for hybrid connectivity to networking specialists
   • Tag AWS hybrid network resources upon creation
   • Use VPC sharing to improve security and compliance across accounts

2. Network Segmentation
   • Verify customer gateway router and firewall configurations align with traffic separation needs
   • Control access between on-premises and AWS environments
   • Use role-based access control for AWS platform access

3. Detection Controls
   • Implement immediate response processes for suspicious activity
   • Set up central logging and analytics for hybrid environments
   • Use CloudWatch metric math for monitoring multiple virtual interfaces
   • Leverage Transit Gateway Route Analyzer to verify routes

4. Infrastructure Protection
   • Use security groups as stateful (layer 4) firewalls
   • Implement Network Access Control Lists (NACLs) as stateless firewalls
   • Configure AWS Transit Gateway route tables for defined connectivity
   • Consider Gateway Load Balancer for third-party security appliances
   • Deploy AWS Network Firewall to secure Direct Connect and VPN traffic
   • Use Amazon Route 53 Resolver DNS Firewall to protect against DNS-level threats

5. Data Protection
   • Use IPSec VPN for encrypted tunnels over the internet
   • Configure MACsec encryption for dedicated 10Gbps and 100Gbps Direct Connect connections
   • Use application-level encryption or VPN for hosted connections and speeds lower than 10Gbps
   • Leverage certificates for authentication where available

6. Incident Response
   • Use Amazon GuardDuty to continuously monitor for malicious behavior
   • Follow the principle of least privilege for all users
   • Implement Network Access Control Lists to block traffic during incidents
   • Automate incident response rather than using manual processes

### Reliability

1. Service Quotas Management
   • Monitor and adjust service quotas to meet business needs
   • Proactively manage quotas using CloudWatch alarms
   • Ensure sufficient gap between service quotas and maximum usage

2. Change Management
   • Prepare for AWS Direct Connect scheduled maintenance
   • Consider redundant Direct Connect connections or VPN backups
   • Monitor bandwidth usage and increase capacity as needed

3. Failure Management
   • Design highly resilient network connections with redundancy
   • Connect from multiple data centers for physical location redundancy
   • Use redundant hardware and telecommunications providers
   • Configure both tunnels for VPN connections for redundancy
   • Test failover scenarios regularly using the Resiliency Toolkit

### Performance Efficiency

1. Connectivity Option Selection
   • Choose between AWS Direct Connect and AWS VPN based on bandwidth, latency, and jitter requirements
   • Select the right VPN termination endpoint (virtual private gateway, Transit Gateway, or EC2 instance)
   • Consider accelerated Site-to-Site VPN for better performance

2. Direct Connect Implementation
   • Choose Direct Connect locations that minimize combined latency
   • Select the right termination endpoint (private virtual interface or transit virtual interface)
   • Consider AWS Local Zones for workloads requiring very low latency
   • Use Link Aggregation Groups (LAG) to aggregate multiple connections

3. Monitoring and Scaling
   • Track usage of VPN and Direct Connect connections using CloudWatch metrics
   • Estimate bandwidth requirements for new applications
   • Scale VPN bandwidth by moving to Transit Gateway and adding connections
   • Add Direct Connect capacity through LAG or additional connections

4. Performance Tradeoffs
   • Balance performance, cost, and setup time when choosing connectivity options
   • Consider tradeoffs between AWS VPN and third-party VPN solutions

### Cost Optimization

1. Usage Monitoring
   • Integrate existing network monitoring with cloud monitoring solutions
   • Use AWS Cost & Usage Report and VPC Flow Logs to track costs
   • Leverage Amazon Athena and QuickSight for cost analysis and visualization

2. Cost-Effective Resource Selection
   • Use internet-based VPN for non-mission critical workloads
   • Start with internet-based connections during testing phases
   • Consider Virtual Private Gateway for small hybrid setups
   • Use Transit Gateway for multiple VPCs requiring hybrid connectivity

3. Demand and Supply Management
   • Plan and forecast hybrid connectivity demands in advance
   • Profile application demand to prevent under/over-provisioning
   • Create Link Aggregation Groups with minimum initial connections
   • Leverage prioritization and queuing techniques for bandwidth management

4. Data Transfer Optimization
   • Understand data transfer costs for different connectivity options
   • Consider Direct Connect for cost-effective high-volume data transfer
   • Be aware of data processing costs with Transit Gateway
   • Choose the right termination option based on data transfer patterns

## Guidelines and Recommendations

### Hybrid Connectivity Design

1. Site-to-Site VPN Design
   • Each AWS Site-to-Site VPN connection consists of two VPN tunnel endpoints for redundancy
   • Terminate VPN tunnels on both endpoints for high availability
   • Configure redundant physical devices in your data center
   • Consider AWS Transit Gateway for connecting to thousands of VPCs over a pair of VPN tunnels
   • Enable acceleration for better performance using AWS Global Accelerator

2. Direct Connect Design
   • Follow the AWS Direct Connect maximum resiliency architecture
   • Connect from multiple data centers for physical location redundancy
   • Establish multiple connections at a Direct Connect location for device redundancy
   • Use dynamic routing with Active/Active connections for load balancing and failover
   • Provision sufficient network capacity to handle connection failures
   • Consider Link Aggregation Groups (LAG) for bandwidth over 100 Gbps
   • Use Direct Connect gateway for global connectivity across AWS Regions

3. Transit Gateway Implementation
   • Use Transit Gateway as a central hub for VPC and on-premises connectivity
   • Leverage Transit Gateway route tables for traffic control and security isolation
   • Keep the number of route tables to a minimum by grouping VPCs with similar routing behavior
   • Use Transit Gateway Network Manager to visualize and monitor your global network

### Security Implementation

1. Account Structure
   • Create a separate Central Networking account for network specialists
   • Deploy hybrid networking constructs in the Central Networking account
   • Share Transit Gateway through RAM with VPCs in other accounts
   • Restrict sensitive APIs to the networking account and specialists

2. Network Protection
   • Implement multiple layers of defense and segmentation
   • Use security groups, NACLs, Transit Gateway route tables, Gateway Load Balancer, and AWS Network Firewall
   • Consider managed prefix lists for consistency across VPCs
   • Implement Amazon Route 53 Resolver DNS Firewall for DNS-level protection

3. Data Encryption
   • Use IPSec VPN for internet connectivity
   • Configure MACsec for dedicated high-bandwidth Direct Connect connections
   • Use application-level encryption or VPN for hosted connections
   • Establish IPSec VPN over Direct Connect for additional security

### Performance Optimization

1. VPN Performance
   • Terminate VPN on Transit Gateway for higher throughput using ECMP
   • Enable acceleration for better latency and jitter performance
   • Scale bandwidth by adding VPN connections with consistent BGP attributes

2. Direct Connect Performance
   • Choose Direct Connect locations that minimize overall latency
   • Use transit virtual interface for hub and spoke topology
   • Consider private virtual interface for very high bandwidth requirements
   • Use AWS Local Zones for very low-latency requirements
   • Aggregate connections in a LAG or use BGP ECMP for load balancing

### Cost Management

1. Data Transfer Cost Optimization
   • Understand data transfer pricing for different connectivity options
   • Use Direct Connect for cost-effective high-volume data transfer
   • Be aware of Transit Gateway data processing costs
   • Consider hybrid approaches for different traffic patterns
   • Terminate inactive VPNs to avoid unnecessary costs

2. Architecture Selection
   • Start with internet-based solutions for testing and development
   • Move to dedicated connections for production workloads
   • Consider bypassing Transit Gateway for very large data transfers
   • Balance operational overhead against Transit Gateway costs

## Important Concepts

1. Hybrid Networking Definition
   • A network that spans AWS and an on-premises data center
   • Integrates on-premises and AWS operations using common cloud services, tools, and APIs
   • Establishes connectivity through services like Amazon VPC, AWS Site-to-Site VPN, and AWS Direct Connect

2. AWS Direct Connect Components
   • **Dedicated Connection**: Private physical Ethernet connection from customer to AWS (1, 10, or 100 Gbps)
   • **Hosted Connection**: Connection provided by AWS Direct Connect Partners (50 Mbps to 10 Gbps)
   • **Virtual Interfaces**: Logical connections on top of physical Direct Connect connections
     • Public virtual interfaces: For public AWS resources
     • Private virtual interfaces: For private VPC resources
     • Transit virtual interfaces: For Transit Gateway connectivity

3. AWS Transit Gateway
   • Fully managed AWS gateway that acts as a cloud router
   • Connects VPCs and on-premises networks through a central hub
   • Enables rich routing scenarios and simplifies complex connections
   • Supports Equal Cost Multipath (ECMP) routing for load balancing

4. AWS Shared Responsibility Model
   • AWS secures the infrastructure that supports cloud services
   • Customers focus on using services to accomplish their goals
   • Provides greater access to security data and automated response to security events

5. Link Aggregation Group (LAG)
   • Logical interface that uses Link Aggregation Control Protocol (LACP)
   • Aggregates multiple connections at a single Direct Connect location
   • Treated as a single, managed connection
   • Limited to two 100G connections or four connections with port speed less than 100G
   • All connections in a LAG terminate on the same AWS device

## Examples and Use Cases

1. Getting Started with Hybrid Connectivity
   • Using Site-to-Site VPN over the internet as an entry point
   • Establishing IPsec tunnels with BGP or static routes
   • Terminating VPN on virtual private gateway for single VPC access
   • Terminating VPN on Transit Gateway for connectivity to thousands of VPCs

2. Critical Workload Connectivity
   • Using AWS Direct Connect for consistent, low-latency, high-bandwidth connectivity
   • Implementing maximum resiliency architecture with connections from multiple data centers
   • Using Link Aggregation Groups for bandwidth over 100 Gbps
   • Leveraging Direct Connect gateway for global connectivity

3. Central Network Management
   • Creating a Central Networking account for network specialists
   • Deploying Direct Connect, Transit Gateway, and other networking resources centrally
   • Sharing Transit Gateway through RAM with VPCs in other accounts
   • Implementing consistent security policies across the organization

4. Security Incident Response
   • Using GuardDuty to detect threats across the hybrid environment
   • Implementing NACLs to block traffic during ransomware incidents
   • Using Network Firewall to block communication with known malware hosts
   • Automating responses with Security Hub, Lambda, and Step Functions

5. Data Transfer Cost Optimization
   • Using Transit VPC with customer-managed VPN for multi-VPC connectivity
   • Terminating Site-to-Site VPN on Virtual Gateway for single VPC access
   • Using Transit Gateway for scalable multi-VPC connectivity
   • Implementing Direct Connect with Virtual Gateway or Transit Gateway based on data transfer patterns

## Cautions and Limitations

1. VPN Limitations
   • Bandwidth limited to 1.25 Gbps per VPN connection/tunnel
   • Performance affected by internet congestion and routing
   • Latency and jitter can vary due to internet conditions
   • Virtual private gateway cannot load balance traffic across multiple VPN connections

2. Direct Connect Considerations
   • Requires physical connectivity to AWS Direct Connect locations
   • Setup times can range from days to weeks depending on circuit availability
   • Link Aggregation Groups (LAG) only include ports on the same AWS device
   • AWS doesn't support multi-chassis LAG, limiting high-availability options

3. Transit Gateway Constraints
   • Data processing costs for all traffic flowing through Transit Gateway
   • Transit Gateway attachment to Direct Connect limited to 50 Gbps
   • Limited number of route tables to stay within service limits
   • Cross-region peering incurs additional data transfer costs

4. Security Boundaries
   • Avoid using a single transit gateway route table per VPC as a security feature
   • Customer gateway router and firewall configurations must align with traffic separation needs
   • Careful management of IP prefixes needed to avoid resource starvation
   • Ransomware can spread across hybrid networks without proper isolation

5. Service Quotas
   • Direct Connect bandwidth limited to specific tiers (1, 10, 100 Gbps)
   • VPN throughput limited to 1.25 Gbps per virtual gateway
   • Service quotas need to be increased from default values for large deployments
   • Sufficient gap needed between quotas and maximum usage

## Additional Resources

### Documentation and Blogs
• AWS Direct Connect User Guide
• AWS VPN User Guide
• Hybrid Connectivity Whitepaper
• Logging and Monitoring AWS Site-to-site VPN
• IAM for AWS Site-to-site VPN and AWS Direct Connect
• Data protection in AWS Site-to-site VPN and AWS Direct Connect
• Deployment models for AWS Network Firewall

### AWS Support Resources
• How to create a certificate-based VPN using AWS Site-to-Site VPN
• How to establish an AWS VPN over an AWS Direct Connect connection
• How to get notifications for AWS Direct Connect scheduled maintenance
• How to prepare for maintenance on Direct Connect connections
• How to monitor AWS VPN tunnels using Amazon CloudWatch alarms
• How to check the current status of VPN tunnels

### Videos
• AWS Networking Series | Episode 2 | Connectivity to AWS and Hybrid AWS Network Architectures
• AWS re:Invent 2019: The right AWS network architecture for the right reason (NET320)
• AWS re:Invent 2019: Connectivity to AWS and hybrid AWS network architectures (NET317)
• AWS re:Invent 2020: Go global with AWS multi-Region network services
• NET305 Behind the Scenes: Exploring the AWS Global Network
• Nine Ways to Reduce Your AWS Bill
• Pricing Model Analysis

### Labs and Tools
• AWS Well-Architected Lab on Data Transfer Cost Analysis
• AWS Direct Connect Resiliency toolkit failover testing
• Transit Gateway Network Manager
• Route Analyzer
• VPC Reachability Analyzer
