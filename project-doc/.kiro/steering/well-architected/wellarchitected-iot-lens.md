---
inclusion: manual
---

# AWS IoT Lens Steering Guide

## Document Overview

This steering guide is based on the AWS Well-Architected Framework Internet of Things (IoT) Lens whitepaper (July 2, 2025 
version). The document provides architectural best practices for designing, deploying, and architecting IoT workloads at the 
edge and in the AWS Cloud. It covers both IoT and industrial IoT (IIoT) workloads across six pillars: operational excellence, 
security, reliability, performance efficiency, cost optimization, and sustainability. The guidance helps organizations 
implement well-architected IoT applications from procurement of connected physical assets through operation to eventual 
decommissioning in a secure, reliable, scalable, sustainable, and automated fashion.

## Key Topics

1. IoT Architecture Layers
   • Design and manufacturing layer
   • Edge layer
   • Fleet provisioning layer
   • Communication layer
   • Ingestion layer
   • Analytics layer
   • Application layer

2. Common IoT Scenarios
   • Device provisioning
   • Device telemetry
   • Device commands
   • IoT Edge computing
   • Generative AI and IoT

3. Well-Architected Framework Pillars for IoT
   • Operational excellence
   • Security
   • Reliability
   • Performance efficiency
   • Cost optimization
   • Sustainability

4. IoT Device Lifecycle Management
   • Manufacturing and provisioning
   • Deployment and operation
   • Monitoring and maintenance
   • Updates and patching
   • Decommissioning and disposal

## Best Practices

### Operational Excellence

1. Organization
   • Conduct OT and IT cybersecurity risk assessments using common frameworks
   • Evaluate OT and IT security policies and controls
   • Consolidate resources into centers of excellence

2. Device Fleet Management
   • Use static and dynamic device hierarchies for fleet operations
   • Implement index and search services for rapid device identification
   • Document device provisioning processes from manufacturing to deployment
   • Use programmatic techniques for device provisioning at scale
   • Implement device-level features for re-provisioning

3. Monitoring and Observability
   • Implement comprehensive monitoring for logs and metrics
   • Monitor application performance at the edge
   • Track device connectivity status
   • Use device state management services to detect connectivity patterns

4. Operational Response
   • Enable appropriate responses to events
   • Use data-driven auditing metrics to detect potentially compromised devices
   • Identify devices with anomalous behavior using attributes

5. Change Management
   • Analyze operational metrics across business teams
   • Document learnings and define action items for firmware deployments
   • Train team members on IoT application lifecycles and business objectives

### Security

1. Identity and Access Management
   • Assign unique identities to each IoT device
   • Use hardware security modules or secure areas to store credentials
   • Implement TPMs for cryptographic controls
   • Use protected boot and persistent storage encryption
   • Implement authentication and authorization for users accessing IoT resources
   • Apply least privilege access to devices

2. Certificate Management
   • Perform certificate lifecycle management (creation, activation, rotation, revocation)

3. Detective Controls
   • Collect and analyze logs and metrics to capture authorization errors
   • Alert on security events, misconfigurations, and behavior violations
   • Monitor non-compliant device configurations and remediate using automation

4. Infrastructure Protection
   • Configure secure communications for cloud infrastructure
   • Restrict network communications to required ports and protocols
   • Log and monitor network configuration changes
   • Implement automated mechanisms for network management
   • Manage device software and configurations using automated processes

5. Data Protection
   • Encrypt IoT data in transit and at rest
   • Implement data classification strategies
   • Ensure regulatory compliance for IoT data

6. Incident Response
   • Build scalable incident response mechanisms
   • Require timely vulnerability notifications from providers

7. Application Security
   • Use source code management tools for device firmware
   • Implement static code analysis and scanning
   • Deploy applications using IaC and CI/CD pipelines

8. Vulnerability Management
   • Scan code and packages during development
   • Deploy updates to address identified issues
   • Identify devices requiring updates and schedule them

9. Security Governance
   • Establish security governance teams
   • Define security policies as code
   • Implement risk assessment processes

10. Security Assurance
    • Identify relevant regulations
    • Configure logging for compliance auditing
    • Implement automated compliance checking

### Reliability

1. Foundations
   • Use NTP for time synchronization on devices
   • Manage service quotas and constraints
   • Optimize data for network and storage constraints
   • Control message delivery frequency to devices

2. Workload Architecture
   • Decouple IoT applications through an ingestion layer
   • Scale cloud resources dynamically based on utilization
   • Implement appropriate storage strategies for IoT data

3. Change Management
   • Use mechanisms to deploy and monitor firmware updates
   • Configure firmware rollback capabilities
   • Support incremental updates to target device groups
   • Implement dynamic configuration management
   • Test using device simulation

4. Failure Management
   • Leverage cloud service capabilities for component failures
   • Implement automatic reconnection logic for devices
   • Support multiple communication methods
   • Alert on reconnection failures
   • Provide local storage for offline operations
   • Synchronize device states upon cloud connection
   • Configure reliable message processing
   • Design for disaster recovery

### Performance Efficiency

1. Architecture Selection
   • Optimize for device hardware resource utilization

2. Compute and Hardware
   • Implement monitoring solutions for device performance data
   • Evaluate runtime application performance

3. Data Management
   • Include timestamps in published messages
   • Implement payload filtering and stream prioritization
   • Optimize telemetry data ingestion
   • Choose appropriate data storage tiers

4. Networking
   • Optimize network topology for distributed devices
   • Verify device connectivity in a timely manner

5. Process and Culture
   • Load test IoT applications
   • Monitor service quotas and metrics
   • Maintain device inventory for configuration and diagnostics

### Cost Optimization

1. Data Management
   • Use data lakes for raw telemetry
   • Provide self-service interfaces for data access
   • Track data source utilization
   • Aggregate data at the edge
   • Implement lifecycle policies for data archiving
   • Choose appropriate storage services
   • Store archival data cost-effectively

2. Device Communication
   • Select services to optimize cost
   • Configure telemetry to reduce data transfer costs
   • Use device shadows only for slowly changing data
   • Group and tag devices for cost allocation
   • Optimize message payload size and frequency

3. Resource Management
   • Plan expected usage over time
   • Balance network throughput against payload size
   • Optimize shadow operations

### Sustainability

1. Software Optimization
   • Eliminate unnecessary modules, libraries, and processes
   • Use AWS IoT features to optimize network usage and power
   • Implement hardware watchdogs for automatic restarts
   • Design resilient client communication patterns

2. Cloud Services
   • Use Basic Ingest feature in AWS IoT Core
   • Choose appropriate Quality of Service (QoS) levels

3. Hardware Selection
   • Source sustainable components
   • Consider manufacturing and distribution footprint
   • Use benchmarks for processor selection
   • Optimize based on real-world testing
   • Use sensors with built-in event detection
   • Implement hardware acceleration for video processing
   • Use HSMs for cryptographic operations
   • Choose low-power location tracking solutions

4. Power Management
   • Use energy harvesting technologies
   • Implement tickless operation and low-power modes
   • Allow dynamic adjustment of settings based on requirements

5. User Education
   • Create detailed documentation
   • Promote responsible disposal and repairability
   • Identify when devices should be retired

## Guidelines and Recommendations

### Device Design and Manufacturing

1. Hardware Selection
   • Choose processors that minimize energy usage for your workload
   • Select processors with advanced power management features
   • Use accelerators for machine learning inference
   • Choose storage that supports device longevity
   • Select power sources with high efficiency
   • Dimension batteries to maximize device lifetime

2. Software Design
   • Choose appropriate operating systems for device capabilities
   • Implement event-driven architectures
   • Select power-efficient programming languages
   • Optimize ML models for edge deployment

### Device Provisioning and Identity

1. Identity Management
   • "Assign unique identities to each IoT device"
   • "Use X.509 client certificates to authenticate over TLS 1.2/1.3"
   • "Choose the appropriate certificate vending mechanisms for your use case"

2. Credential Protection
   • "Use a separate hardware or a secure area on your devices to store credentials"
   • "Store all secret keys from the manufacturer required for secure boot, such as attestation keys, storage keys, and 
application keys, in the secure enclave of the chip"
   • "Use cryptographic API operations provided by the secure element hardware for protecting the secrets on the device"

3. Provisioning Methods
   • "Use programmatic techniques to provision devices at scale"
   • "Embed provisioning claims into the devices that are mapped to approval authorities recognized by the provisioning 
service"
   • "Use device level features to enable re-provisioning"

### Communication and Connectivity

1. Protocol Selection
   • "Choose a lightweight protocol for messaging"
   • "Choose an appropriate Quality of Service (QoS) level"
   • Use MQTT for most IoT device communications
   • Consider HTTPS for large data transfers

2. Network Optimization
   • "Adopt power conservation practices appropriate to your wireless technology"
   • "Reduce the amount of data transmitted"
   • "Reduce the distance traveled by data"
   • "Buffer and spool messages"
   • "Optimize the frequency of messages for your use case"

3. Connectivity Management
   • "Implement device logic to automatically reconnect to the cloud"
   • "Design devices to use multiple methods of communication"
   • "Perform timely connectivity verification for devices"

### Data Management

1. Data Collection and Processing
   • "Down sample data to reduce storage requirements and network utilization"
   • "Add timestamps to each published message"
   • "Optimize data sent from devices to backend services"
   • "Aggregate data at the edge where possible"

2. Storage Strategies
   • "Store data before processing"
   • "Store data in different tiers following formats, access patterns and methods"
   • "Use a data lake for raw telemetry data"
   • "Use lifecycle policies to archive your data"

3. Edge Analytics
   • "Perform analytics at the edge"
   • "Use gateways to offload and pre-process your data at the edge"

### Device Management and Operations

1. Fleet Management
   • "Use static and dynamic device hierarchies to support fleet operations"
   • "Use index and search services to enable rapid identification of target devices"
   • "Have device inventory in the IoT system that centralizes device configuration and diagnostics"

2. Monitoring and Observability
   • "Monitor the status of your IoT devices"
   • "Use device state management services to detect status and connectivity patterns"
   • "Implement monitoring to capture logs and metrics"
   • "Capture and monitor application performance at the edge"

3. Updates and Maintenance
   • "Use Over-The-Air device management"
   • "Use a mechanism to deploy and monitor firmware updates"
   • "Configure firmware rollback capabilities in devices"
   • "Implement support for incremental updates to target device groups"
   • "Implement dynamic configuration management for devices"

### Security Implementation

1. Device Security
   • "Use protected boot and persistent storage encryption"
   • "Boot devices using a cryptographically verified operating system image"
   • "Create separate filesystem partitions for the boot-loader and the applications"
   • "Use encryption utilities provided by the host operating system to encrypt the writable filesystem"

2. Network Security
   • "Configure cloud infrastructure to have secure communications"
   • "Define networking configuration which restricts communications to only those ports and protocols which are required"
   • "Log and monitor network configuration changes and network communication"

3. Data Protection
   • "Use encryption to protect IoT data in transit and at rest"
   • "Use data classification strategies to categorize data access based on levels of sensitivity"
   • "Protect your IoT data in compliance with regulatory requirements"

## Important Concepts

### IoT Architecture Layers

1. Design and Manufacturing Layer
   • Product conceptualization, requirements gathering, prototyping, design, component sourcing, manufacturing, and 
distribution
   • Decisions here affect subsequent layers of the IoT workload

2. Edge Layer
   • Physical hardware, embedded OS, and device firmware
   • Responsible for sensing and acting on peripheral devices
   • Follows the "three laws of distributed computing": physics (latency/throughput constraints), economics (cost-
effectiveness of data transfer), and law of the land (data regulations)

3. Fleet Provisioning Layer
   • Mechanisms for creating device identities and providing configuration
   • Includes Public Key Infrastructure (PKI) and ongoing maintenance
   • Enables frictionless addition and management of devices

4. Communication Layer
   • Handles connectivity and message routing between devices and cloud
   • Enables devices to establish how messages are sent/received
   • Represents and stores physical state in the cloud

5. Ingestion Layer
   • Collects disparate data streams from devices
   • Transmits data securely and reliably
   • Decouples data flow from device communication

6. Analytics Layer
   • Processes and analyzes IoT data for insights
   • Includes storage services and analytics/ML services
   • Enables proactive strategies like predictive maintenance

7. Application Layer
   • Management applications for operating, inspecting, and managing IoT operations
   • User applications for external systems and interfaces
   • Database and compute services to support applications

### IoT Device Classes

1. Microcontroller (MCU) Class Devices
   • Low-power, resource-constrained applications
   • Often battery-operated
   • Limited processing capabilities

2. Microprocessor (MPU) Class Devices
   • Higher computational power
   • Multitasking capabilities
   • More capable operating systems

3. Inference Class Devices
   • Hardware acceleration for machine learning
   • May include GPUs, NPUs, DSPs, or FPGAs
   • Optimized for specific computational tasks

### IoT Communication Protocols

1. MQTT (Message Queuing Telemetry Transport)
   • Lightweight publish/subscribe messaging protocol
   • Designed for constrained devices and low-bandwidth networks
   • Supports different QoS levels
   • MQTT5 adds features like shared subscriptions and message expiry

2. HTTPS
   • More heavyweight protocol for web-based applications
   • Request-response model requiring larger data exchanges
   • Suitable for large file transfers and bulk data

3. LoRaWAN
   • Long-range, low-power protocol
   • Suitable for applications like smart agriculture and asset tracking
   • Optimized for battery-powered devices

### Device Lifecycle Phases

1. Design and Build Phase
   • Accounts for most of the carbon footprint (embodied carbon)
   • Includes component selection and manufacturing decisions

2. Operational Phase
   • Accounts for 10-15% of lifecycle carbon footprint for battery-powered devices
   • Accounts for 60-80% for plugged-in devices
   • Focus on energy efficiency and resource optimization

3. Disposal Phase
   • When a device is no longer needed or usable
   • Requires responsible disposal practices
   • Can be extended through repairability and transferability

## Examples and Use Cases

### Device Provisioning Scenario

Registration flow:
1. Device connects with claim certificate to AWS IoT Core
2. Fleet Provisioning service creates new certificate and private key assigned with AWS CA
3. Device writes the unique private key and certificate to secure storage
4. With the parameters published from the device, Fleet Provisioning service triggers Pre-Provisioning lambda function
5. Lambda function performs additional verification logic such as checking the hardware secret against a DynamoDB table with verified devices
6. Fleet provisioning service creates IoT Thing, Policy, and activates certificate based on Provisioning template and publishes this to the device
7. Device applies the new configuration and connects with the unique private key, certificates and configuration

### Device Telemetry Scenarios

Options for capturing telemetry:
1. One publishing topic and one subscriber. For example, a smart light bulb that publishes its brightness level to a single topic where only a single application can subscribe.
2. One publishing topic with variables and one subscriber. For example, a collection of smart bulbs publishing their brightness on similar but unique topics. Each subscriber can listen to a unique publish message.
3. Single publishing topic and multiple subscribers. In this case, a light sensor that publishes its values to a topic that all the light bulbs in a house subscribe to.
4. Multiple publishing topics and a single subscriber. For example, a collection of light bulbs with motion sensors. The smart home system subscribes to all of the light bulb topics, inclusive of motion sensors, and creates a composite view of brightness and motion sensor data.
5. AWS IoT Sitewise edge software running on an edge gateway is used to collect, organize, process, and monitor equipment data on-premises and sends it to AWS IoT Sitewise cloud service for data storage, organization and visualization.

### Device Commands Example

Using Device Shadow with devices:
1. The device should check its desired state as soon as it comes online by subscribing to the $aws/things/<<thingName>>/shadow/name/<<shadowName>>/get topic. A device reports initial device state by publishing that state as a message to the update topic $aws/things/<<thingName>>/shadow/name/<<shadowName>>/update.
2. The Device Shadow reads the message from the topic and records the device state in a persistent data store.
3. A device subscribes to the delta messaging topic $aws/things/<<thingName>>/shadow/name/<<shadowName>>/update/delta upon which device-related state change messages will arrive.
4. A component of the solution publishes a desired state message to the topic $aws/things/<<thingName>>/shadow/name/<<shadowName>>/update and the Device Shadow tracking this device records the desired device state in a persistent data store.
5. The Device Shadow publishes a delta message to the topic $aws/things/<<thingName>>/shadow/name/<<shadowName>>/update/delta, and the Message Broker sends the message to the device.
6. A device receives the delta message and performs the desired state changes.
7. A device publishes an acknowledgment message reflecting the new state to the update topic $aws/things/<<thingName>>/shadow/name/<<shadowName>>/update and the Device Shadow tracking this device records the new state in a persistent data store.
8. The Device Shadow publishes a message to the $aws/things/<<thingName>>/shadow/name/<<shadowName>>/update/accepted topic.
9. A component of the solution can now request the updated state from the Device Shadow.

### Firmware Update Example

Updating firmware on devices:
1. A device subscribes to the IoT job notification topic $aws/things/<<thingName>>/jobs/notify-next upon which IoT job notification messages will arrive.
2. A device publishes a message to $aws/things/<<thingName>>/jobs/start-next to start the next job and get the next job, its job document, and other details including states saved in statusDetails.
3. The AWS IoT Jobs service retrieves the next job document for the specific device and sends this document on the subscribed topic $aws/things/<<thingName>>/jobs/start-next/accepted.
4. A device performs the actions specified by the job document using the $aws/things/<<thingName>>/jobs/jobId/update MQTT topic to report on the progress of the job.
5. During the upgrade process, a device downloads firmware using a pre-signed URL for Amazon S3. Use code-signing to sign the firmware when uploading to Amazon S3. By code-signing your firmware the end-device can verify the authenticity of the firmware before installing.
6. The device publishes an update status message to the job topic $aws/things/<<thingName>>/jobs/jobId/update reporting success or failure.
7. Because this job's execution status has changed to final state, the next IoT job available for execution (if any) will change.

### IoT Edge Computing Example

IoT edge computing using AWS IoT Greengrass:
- Two client devices with private keys, device certificates, and root CA certificates
- A core device with AWS IoT Greengrass deployed with MQTT broker, MQTT bridge, client device authentication, and IP detector
- Client devices communicate with each other through the core device's MQTT broker
- Client devices communicate with AWS IoT Core through the MQTT broker and bridge
- AWS IoT Core can send messages to client devices through the MQTT test client, bridge, and broker

### Generative AI and IoT Use Case

In an industrial setting, you can monitor equipment, detect anomalies, provide recommendations to optimize production, reduce energy consumption, and reduce equipment failures. By combining IoT and generative AI, you will be able to gain situational awareness and understand what happened? why it happened? and what to do next? in your IoT applications.

## Cautions and Limitations

### Security Considerations

1. Device Credential Protection
   • "Never store or cache device credentials outside of the SE"
   • "If supported, generate public or private key pairs using the SE, and generate the Certificate Signing Requests (CSRs) on
the device"

2. Certificate Management Risks
   • "Every X.509 certificate has an expiration. This includes certificates representing certificate authorities, including 
root certificate authorities"
   • "Devices must support the replacement of trusted root and intermediate certificate authorities"

3. Network Security Risks
   • "IoT devices are often deployed behind restricted firewalls at remote sites"
   • "Many legacy OT systems have limited security features and use industrial protocols which does not support 
authentication, authorization and encryption"

4. Data Protection Concerns
   • "Unlike traditional cloud applications, data sensitivity and governance extend to the IoT devices that are deployed in 
remote locations outside of your network boundary"
   • "Attention to data classification, governance, and controls is important because IoT devices may handle personally 
identifiable data"

### Operational Challenges

1. Device Connectivity
   • "Due to things like connectivity issues or misconfigured settings, devices may go offline for longer periods of time than
anticipated"
   • "Design your edge software to handle extended periods of offline connectivity"

2. Resource Constraints
   • "IoT hardware devices are frequently resource constrained"
   • "The overall logic tasks workflow of your IoT application must push compute and energy-intensive activities away from 
field-deployed devices"

3. Firmware Update Risks
   • "Deploying software changes to devices constitutes a high-risk operation due to the recovery cost associated with 
remotely deployed devices"
   • "Supporting firmware upgrades without human intervention is critical for security, scalability, and delivering new 
capabilities"

4. Scaling Limitations
   • "AWS IoT provides a set of soft and hard limits for different dimensions of usage"
   • "It's important to review the IoT limits and make sure that your application adheres to any soft limits related to the 
data plane, while not exceeding any hard limits"

### Sustainability Tradeoffs

1. Hardware Selection
   • "Implementing the best practices outlined here involves trade-offs between cost, reliability, performance, carbon 
footprint, and any current or future regulatory requirements"
   • "Over-provisioning hardware can lead to choosing a processor that has a large power draw but stays mostly idle"
   • "Under-sizing hardware can lead to long execution times or a lack of extensibility necessary to insure the longevity of 
the device"

2. Power Management
   • "PSM is more power efficient than eDRX. However, there is an inflection point at which it may make more sense for a 
device to use one versus the other"
   • "While building an application you should test your particular hardware for overall power consumption during a typical 
window of sleep and active states"

3. Data Transmission
   • "Data aggregation is an architectural decision that can have impacts on data fidelity"
   • "Aggregations should be thoroughly reviewed with engineering and architectural teams before implementation"

## Additional Resources

### AWS Services for IoT

1. Edge and Device Services
   • AWS IoT Device SDKs
   • FreeRTOS
   • AWS IoT Greengrass
   • AWS IoT SiteWise Edge
   • AWS IoT FleetWise Edge
   • AWS IoT ExpressLink

2. Core IoT Services
   • AWS IoT Core
   • AWS IoT Device Registry
   • AWS Private Certificate Authority
   • AWS IoT Device Shadow service
   • AWS IoT Core for LoRaWAN

3. Management and Security Services
   • AWS IoT Device Defender
   • AWS IoT Device Management
   • AWS IoT Events
   • AWS Certificate Manager
   • AWS IoT Jobs

4. Analytics and Storage Services
   • AWS IoT Analytics
   • AWS IoT SiteWise
   • AWS IoT TwinMaker
   • Amazon Timestream
   • Amazon S3
   • Amazon DynamoDB
   • Amazon Kinesis

### Documentation and Resources

1. AWS Documentation
   • AWS IoT Device Management features
   • Security in AWS IoT
   • AWS IoT Device Defender
   • AWS IoT SiteWise
   • Authentication
   • MQTT with TLS client authentication

2. Whitepapers
   • Designing MQTT Topics for AWS IoT Core
   • Security Best Practices in Manufacturing OT
   • Securing Internet of Things (IoT) with AWS
   • Device Manufacturing and Provisioning with X.509 Certificates in AWS IoT Core

3. Blogs and Guides
   • AWS IoT Blogs
   • The Internet of Things on AWS – Official Blog
   • AWS Security Incident Response Guide
   • Ten security golden rules for Industrial IoT solutions
   • Ten security golden rules for connected mobility solutions
