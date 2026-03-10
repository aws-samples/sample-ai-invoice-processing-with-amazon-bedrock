---
inclusion: manual
---

# AWS Well-Architected Framework: Healthcare Industry Lens Steering Guide

## Document Overview

This document presents the Healthcare Industry Lens for the AWS Well-Architected Framework, which enables customers to review 
and improve their cloud-based healthcare architectures. It provides industry-specific guidance on designing and operating 
reliable, secure, efficient, sustainable, and cost-effective healthcare systems on AWS. The lens augments the standard Well-
Architected Framework with healthcare-specific principles, best practices, and considerations across all six pillars, along 
with reference architectures for common healthcare scenarios.

## Key Topics

1. Healthcare-specific design principles
2. Operational excellence for healthcare workloads
3. Security considerations for health data
4. Reliability requirements for healthcare systems
5. Performance efficiency in healthcare applications
6. Cost optimization strategies for healthcare workloads
7. Sustainability practices for healthcare organizations
8. Common healthcare scenarios and reference architectures:
   • Electronic healthcare record and revenue cycle systems
   • Healthcare interoperability
   • Medical imaging
   • Healthcare analytics
   • Machine learning for healthcare

## Best Practices

### General Design Principles

• **Align with applicable regulatory and quality frameworks**: Identify relevant regulations early and architect solutions 
from the start to meet regulatory requirements.
• **Automation reduces operational risk**: Implement continuous integration and continuous delivery with automated checks 
aligned to specific control frameworks.
• **Encrypt all sensitive data**: Implement encryption of all health data both at rest and in transit.
• **Log everything**: Monitor system and data access to verify only authorized individuals access appropriate data. Implement 
immutable logs for long-term retention.
• **Implement least privilege for all data**: Restrict access to production systems and health data to only those who need it.
Implement reviews to maintain least privilege over time.
• **Adopt modern software communication protocols**: Use data standards and communication protocols in-line with best 
practices.
• **Promote interoperability**: Design architectures that facilitate secure, governed access to health data across silos.
• **Plan to recover from failures automatically**: Design architectures with monitoring and automated recovery processes to 
ensure systems meet availability requirements.

### Operational Excellence

• **Develop a hub-and-spoke model for compliance controls**: Map to a central control framework (like NIST or HITRUST) to 
simplify mapping to multiple regulations.
• **Align software and infrastructure development with applicable quality frameworks**: Align with frameworks like ISO 13485 
and ISO 14971.
• **Take advantage of AWS fully managed services**: Leverage managed cloud services to simplify meeting regulatory 
requirements and maintaining security.
• **Create and document a risk management program**: Develop a comprehensive program covering operational, clinical, 
strategic, financial, legal, and environmental risks.
• **Create a risk authority team**: Establish a team to evaluate criticality of business processes and specify required 
availability levels.
• **Create policies and procedures for cloud governance**: Establish a control environment that meets compliance objectives 
and requirements.
• **Map security controls to compliance requirements**: Use a hub-and-spoke model to map controls to multiple regulatory 
frameworks.
• **Train employees on health data access**: Ensure employees with access to sensitive data understand rules and regulations.
• **Partition workloads with sensitive data**: Isolate workloads to separate environments requiring additional controls for 
access.
• **Architect for continuous compliance evidence**: Build systems that can generate evidence demonstrating compliance.
• **Automate remediation of compliance violations**: Implement event-driven architectures to improve remediation times.

### Security

• **Implement a strong identity foundation**: Centralize identity management and avoid reliance on long-term static 
credentials.
• **Enable traceability**: Monitor, alert, and audit actions and changes to your environment in real time.
• **Apply security at all layers**: Implement multiple security controls at all layers from network edge to application code.
• **Automate security best practices**: Use automated security mechanisms to scale securely and cost-effectively.
• **Keep people away from data**: Use mechanisms to reduce direct access to health data.
• **Prepare for security events**: Develop incident management and investigation policies aligned with regulatory frameworks.
• **Create a data classification strategy**: Implement a policy that extends beyond marking health data to include other 
sensitive data.
• **Use identity and access management**: Control access to AWS services and resources with IAM following least privilege 
principles.
• **Configure audit logs to be centralized and immutable**: Save logs to a centralized location and make them immutable to 
verify integrity.
• **Regularly review audit logs**: Create procedures to review audit logs on a regular basis.
• **Automate alerts for anomalies**: Use automated systems to generate alerts for anomalies detected in logs.
• **Enforce data locality requirements**: Use AWS Regions and service control policies to enforce data residency requirements.
• **Encrypt health data at rest and in transit**: Use AWS encryption services to protect sensitive data throughout its 
lifecycle.
• **Isolate health data from non-health data**: Use multiple AWS accounts and designate specific accounts for health data.

### Reliability

• **Evaluate and understand availability and latency implications**: Consider requirements in defining cloud architecture 
based on real-world scenarios.
• **Address potential implications by defining requirements**: Understand availability requirements and consequences of 
service disruptions.
• **Understand the end user setting**: Document where and how end users will access your solution.
• **Architect systems for elasticity**: Implement architectures that automatically adapt to changes in demand.
• **Architect redundant network connections**: Ensure secure connectivity between cloud and on-premises resources for care 
continuity.

### Performance Efficiency

• **Offload encryption to hardware**: Use the AWS Nitro System to offload encryption services to hardware.
• **Select compute services that meet regulatory and performance requirements**: Choose appropriate compute options based on 
workload needs.
• **Define and test network performance requirements**: Ensure network architecture meets healthcare application needs.
• **Define and test storage performance requirements**: Select appropriate storage options based on durability and performance
needs.

### Cost Optimization

• **Determine applicable regulatory frameworks for data retention**: Establish data retention policies aligned with regulatory
requirements.
• **Implement data lifecycle policies**: Transition infrequently-accessed data to lower-cost storage tiers.
• **Centralize automated policy enforcement**: Use infrastructure as code to define and test data retention policies.
• **Validate lifecycle policies are enforced**: Monitor changes to data retention policies.

### Sustainability

• **Prioritize targets for improvement**: Review workloads against sustainability principles.
• **Scale infrastructure to match user demand**: Minimize hardware by scaling workloads down during periods of low demand.
• **Analyze workload activity**: Identify components that can be removed or refactored.
• **Evaluate impact of applications and equipment**: Consider backward compatibility to minimize hardware replacement.
• **Quantify and report sustainability results**: Add metrics to quantify sustainability improvement.
• **Automate data retention processes**: Retain minimum amount of health data required to meet requirements.

## Guidelines and Recommendations

### Healthcare Interoperability

1. Identify and prioritize interoperability standards:
   • Leverage thought leadership organizations to understand emerging trends
   • Use capabilities of your customers' systems
   • Consider modern standards like FHIR to reduce integration complexity

2. Determine unidirectional or bidirectional needs:
   • Understand what interoperability is needed for your use cases
   • Consider custom integration work for bidirectional interoperability

3. Standardize terminology:
   • Work with customers to understand vocabularies they employ
   • Leverage modern standards that provide semantic interoperability
   • Use AI services like Amazon Comprehend Medical to link concepts to standard ontologies

4. Protect integration endpoints:
   • Use end-to-end encryption for health data exchanged over networks
   • Implement VPN tunnels or additional encryption for protocols that don't support TLS
   • Restrict access to integration endpoints to allow-listed IP addresses

### Medical Imaging

1. Benchmark performance:
   • Quantitatively test performance in retrieving, analyzing, and reporting on images
   • Simulate realistic network bandwidth, data volume, and concurrent users

2. Optimize network protocols:
   • Use high-performance, parallelized protocols like HTTP/2
   • Leverage compression algorithms to reduce data transfer volume

3. Prioritize data transmission:
   • Optimize end user experience by prioritizing transmission of highest-interest images or areas

4. Select appropriate storage:
   • Balance performance requirements with cost-effective storage options
   • Move images to lower-cost tiers as access frequency decreases

### Healthcare Analytics

1. Implement master data management:
   • Use central Data Catalog to register and discover datasets
   • Automate processes to reduce burden and improve adoption
   • Prefer standard healthcare ontologies over proprietary ones

2. Update vocabularies regularly:
   • Automate processes for keeping content updated
   • Align update schedules with content owner publication schedules

3. Use open data formats:
   • Store data in open standard formats (HL7, DICOM, XML, JSON, etc.)
   • Reduce transformations needed for interoperability

4. Implement fine-grained access control:
   • Use role-based and attribute-based mechanisms
   • Control access at table, column, or row level
   • Verify that combining datasets doesn't expose unintended risks

### Machine Learning for Healthcare

1. Track model revisions:
   • Employ version control for source code, data, and ML artifacts
   • Ensure traceability of production ML deployments

2. Review open-source dependencies:
   • Establish processes to review privacy and license agreements
   • Verify compliance with organizational requirements

3. De-identify health data:
   • Apply ML to de-identified data where possible
   • Use services like Amazon Comprehend Medical DetectPHI API

4. Identify and limit biases:
   • Examine data distributions to quantify and mitigate biases
   • Consider care setting and health insurance coverage impacts

5. Monitor model performance:
   • Create baselines for data quality
   • Automate monitoring of performance in production
   • Set alerts for changes in data quality or distributions

## Important Concepts

### Health Data and Sensitive Data
Health data is broadly defined as information relating to an identified or identifiable person, including identification 
numbers, location data, genetic information, cultural and social attributes, and identifiable health records. Specific 
regulations like HIPAA define Protected Health Information (PHI) that is covered under regulatory standards.

### Shared Responsibility Model
AWS operates, manages, and controls components from the host operating system and virtualization layer down to the physical 
security of facilities. Customers assume responsibility for the guest operating system, application software, and security 
group firewall configuration. This is commonly described as "AWS assumes security of the cloud, and customers assume security 
in the cloud."

### Healthcare Interoperability Levels
As defined by HIMSS:
1. Foundational: Establishing interconnectivity for secure data exchange
2. Structural: Defining standards for format, syntax, and organization of data
3. Semantic: Using standardized coding vocabularies for shared understanding of meaning
4. Organization: Managing governance and legal aspects of data exchange

### Data Classification and Lifecycle
Healthcare data should be classified according to sensitivity and regulatory requirements. As data ages, its access frequency 
typically declines, allowing for lifecycle policies that transition infrequently-accessed data to lower-cost storage tiers 
while maintaining compliance with retention requirements.

### Healthcare ML Considerations
Healthcare ML applications pose unique challenges including regulatory oversight, design control obligations, and 
interpretability requirements. Healthcare data is often high dimensional, multi-modal, and suffers from missingness due to 
episodic care. Models may need to be validated for face validity and alignment with medical knowledge.

## Examples and Use Cases

### Electronic Healthcare Record Systems
Characteristics:
- High-scale transactional databases hosting patient, care delivery, and payment records
- Workflow-specific user interfaces for highly skilled end users
- Embedded analytics and AI/ML algorithms supporting workflows
- Stringent availability and resilience requirements
- Integration with third-party applications

### Healthcare Interoperability Architecture (FHIR Example)
1. API Gateway provides scalable endpoint for integration
2. Requests authenticated with OAuth or Amazon Cognito
3. Inbound payloads checked for conformance to standards
4. Data written to or pulled from systems of record
5. Transformations map data elements to/from interoperability standard
6. Data may be stored in DynamoDB or exchanged without persistence
7. AWS HealthLake enables enrichment of FHIR data

### Medical Imaging Architecture
- Highly available solution deployed across multiple AWS Availability Zones
- Front-end viewers, application servers, databases, and storage tiers
- Auto-scaling based on load for performance during peak demand
- Recently ingested studies cached on high-performance storage
- Older data moved to lower-cost tiers as access frequency declines
- Metadata stored in high-performance databases with in-memory caches
- Redundant network connections between care settings and cloud

### Healthcare Analytics Environment
- Multiple communication protocols supported (SFTP, HL7v2, FHIR)
- Raw data stored in Amazon S3 with default encryption
- High-volume messages batched through Amazon Kinesis
- AWS Glue Crawlers automatically discover and catalog schemas
- End users interact through dashboards, custom applications, or ML
- IAM and Lake Formation enforce access controls

### Machine Learning Lifecycle
1. Data collected and pre-processed using a data lake
2. Features extracted and stored in feature stores
3. Ground truth populated and reviewed by humans
4. Standard ML training, tuning, and evaluation workflows used
5. Models reviewed by cross-functional stakeholders
6. Accepted models integrated with IT systems
7. Model inferences incorporated in clinical workflows
8. Model inferencing pipelines monitored for performance

## Cautions and Limitations

• **Regulatory Compliance**: Healthcare organizations are subject to various regulations depending on geography and 
activities. Failure to comply can result in penalties and reputational damage.

• **Data Residency**: Many healthcare organizations fall under data locality requirements or regulations on where data may be 
physically located. Review requirements with legal counsel and implement appropriate controls.

• **Legacy Systems**: Migrated healthcare workloads may have dependencies on older technologies, software applications, and 
host operating systems, requiring special security considerations.

• **Model Bias**: Statistical models trained on real-world health data are susceptible to biases from population 
characteristics, care settings, and health insurance coverage. These biases must be quantified and mitigated.

• **Data Access**: Granting access to health data should follow least privilege principles. Access should be limited to only 
those who require it for their job functions.

• **Encryption Requirements**: The AWS Business Associate Addendum (BAA) requires encryption of protected health information 
at rest and in transit. Other regulatory frameworks may have similar requirements.

• **Audit Logging**: Organizations must maintain comprehensive audit logs of all access to health data, with logs being 
centralized and immutable.

• **Network Connectivity**: Healthcare applications in hospitals require secure connectivity between cloud and on-premises 
resources. Redundant connections are critical to verify service continuity.

## Additional Resources

### AWS Documentation
• AWS Well-Architected Framework
• AWS Well-Architected Lenses
• AWS Compliance Programs
• AWS Quick Starts
• Healthcare Compliance in the Cloud
• How to protect sensitive data for its entire lifecycle in AWS

### Whitepapers
• Architecting for HIPAA Security and Compliance on Amazon Web Services
• Introduction to AWS Security
• Data residency: AWS policy perspectives
• Logical Separation on AWS
• Storage Best Practices for Data and Analytics Applications
• Data Classification
• Machine Learning Best Practices in Healthcare and Life Sciences
• Model Explainability with AWS Artificial Intelligence and Machine Learning Solutions

### Videos
• AWS Security Webinar: The Key to Effective Cloud Encryption
• Powering next-gen Amazon EC2: Deep dive on the Nitro System
• Simplify Your Data Lifecycle and Optimize Storage Costs With Amazon S3 Lifecycle
• Simplify Backup Auditing and Compliance with AWS Backup Audit Manager
• Connectivity to AWS and hybrid AWS network architectures
• AWS re:Invent 2021 - Cloud compliance, assurance, and auditing
• Enforce compliance with AWS Config
