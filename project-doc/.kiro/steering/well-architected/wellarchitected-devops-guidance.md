---
inclusion: manual
---

# AWS Well-Architected DevOps Guidance Steering File

## Document Overview

The AWS Well-Architected Framework DevOps Guidance document provides a structured approach for organizations to cultivate a high-velocity, security-focused culture capable of delivering substantial business value using modern technologies and DevOps best practices. Drawing from Amazon's own transformative journey and AWS expertise in managing cloud services at global scale,
this guidance offers a comprehensive collection of capabilities that together form an approach to designing, developing, securing, and efficiently operating software at cloud scale.

## Key Topics

The document is organized around five core domains called "DevOps Sagas":

1. Organizational adoption - Creating a customer-centric, adaptive culture focused on optimizing people-driven processes
2. Development lifecycle - Enhancing the organization's capacity to develop, review, and deploy workloads swiftly and securely
3. Quality assurance - Advocating for a proactive, test-first methodology integrated into the development process
4. Automated governance - Facilitating directive, detective, preventive, and responsive measures at all stages of the development process
5. Observability - Incorporating observability within environments and workloads to detect and address issues

Each saga contains multiple capabilities, which in turn include indicators, anti-patterns, and metrics.

## Best Practices

### Organizational Adoption

#### Leader Sponsorship
• Appoint a single-threaded leader to own DevOps adoption with decision-making authority
• Align DevOps adoption with business objectives through operating plans
• Drive continued improvement through regular business reviews and KPIs
• Establish open dialogue between leadership and teams
• Create a cross-functional enabling team focused on organizational transformation

#### Supportive Team Dynamics
• Organize teams into distinct topology types (stream-aligned, platform, enabling, complicated subsystem)
• Tailor operating models to business needs and team preferences
• Prioritize shared accountability over individual achievements
• Structure teams around desired business outcomes (Conway's Law)
• Establish team norms that enhance work performance
• Provide teams ownership of the entire value stream for their product
• Amplify the scale and impact of centralized functions through the Guardian Model
• Promote cognitive diversity within teams

#### Team Interfaces
• Communicate work flow and goals between teams and stakeholders
• Streamline intra-team communication using tools and processes
• Establish mechanisms for teams to gather and manage customer feedback
• Refine error tracking and resolution
• Design adaptive approval workflows without compromising safety
• Prioritize customer needs to deliver optimal business outcomes
• Maintain a unified knowledge source for teams
• Simplify access to organizational information
• Facilitate self-service collaboration through APIs and documentation
• Choose interaction modes for improved efficiency and cost savings

#### Balanced Cognitive Load
• Clarify purpose and direction to improve cognitive well-being
• Automate repetitive tasks to reduce toil
• Reduce troubleshooting and technical debt through continuous improvement
• Boost team efficiency by limiting work in progress
• Establish clear escalation paths and encourage constructive disagreement
• Provide teams the autonomy to make decisions that align with organizational objectives
• Cultivate a psychologically-safe culture for experimentation
• Determine team sizes based on cognitive capacity (7±2 individuals)
• Use guiding principles to make consistent team decisions
• Make informed decisions using data

#### Adaptive Work Environment
• Equip teams with feature-rich tools for virtual collaboration
• Offer inclusive options for both virtual and on-site collaboration
• Balance work schedules for diverse global teams
• Provide adaptable workspaces for effective on-site collaboration
• Organize team-building activities and social events

#### Personal and Professional Development
• Encourage collaboration, innovation, learning, and continuous growth to foster a generative culture
• Allocate time and budget for targeted training
• Offer diverse and accessible training options
• Invest in attracting, developing, and retaining skilled employees
• Recognize and reward continuous learning
• Promote knowledge sharing through inter-team interest groups

### Development Lifecycle

#### Local Development
• Establish development environments for local development
• Consistently provision local environments
• Commit local changes early and often
• Enforce security checks before commit
• Enforce coding standards before commit
• Leverage extensible development tools
• Establish sandbox environments with spend limits
• Generate mock datasets for local development
• Share tool configurations
• Manage unused development environments
• Implement smart code completion with machine-learning

#### Software Component Management
• Use a version control system with appropriate access management
• Keep feature branches short-lived
• Use artifact repositories with enforced authentication and authorization
• Grant access only to trusted repositories
• Maintain an approved open-source software license list
• Maintain informative repository documentation
• Standardize vulnerability disclosure processes
• Use a versioning specification to manage software components
• Implement plans for deprecating and revoking outdated software components
• Generate a comprehensive software inventory for each build

#### Everything as Code
• Organize infrastructure as code for scale
• Modernize networks through infrastructure as code
• Codify data operations
• Implement continuous configuration for enhanced application management
• Integrate technical and operational documentation into the development lifecycle
• Use general-purpose programming languages to generate Infrastructure-as-Code
• Automate compute image generation and distribution

#### Code Review
• Standardize coding practices
• Perform peer review for code changes
• Establish clear completion criteria for code tasks
• Comprehensive code reviews with an emphasis on business logic
• Foster a constructive and inclusive review culture
• Initiate code reviews using pull requests
• Create consistent and descriptive commit messages using a specification
• Designate code owners for expert review

#### Cryptographic Signing
• Implement automated digital attestation signing
• Sign code artifacts after each build
• Enforce verification before using signed artifacts
• Enhance traceability using commit signing

#### Continuous Integration
• Integrate code changes regularly and frequently
• Trigger builds automatically upon source code modifications
• Ensure automated quality assurance for every build
• Provide consistent, actionable feedback to developers
• Sequence build actions strategically for prompt feedback
• Refine integration pipelines with build metrics
• Validate the reproducibility of builds

#### Continuous Delivery
• Deploy changes to production frequently
• Deploy exclusively from trusted artifact repositories
• Integrate quality assurance into deployments
• Automate the entire deployment process
• Ensure on-demand deployment capabilities
• Refine delivery pipelines using metrics for continuous improvement
• Remove manual approvals to practice continuous deployment

#### Advanced Deployment Strategies
• Test deployments in pre-production environments
• Implement automatic rollbacks for failed deployments
• Use staggered deployment and release strategies
• Implement incremental feature release techniques
• Ensure backwards compatibility for data store and schema changes
• Use cell-based architectures for granular deployment and release

### Quality Assurance

#### Test Environment Management
• Establish dedicated testing environments
• Ensure consistent test case execution using test beds
• Store and manage test results
• Implement a unified test data repository for enhanced test efficiency
• Run tests in parallel for faster results
• Enhance developer experience through scalable quality assurance platforms

#### Functional Testing
• Ensure individual component functionality with unit tests
• Validate system interactions and data flows with integration tests
• Confirm end-user experience and functional correctness with acceptance tests
• Balance developer feedback and test coverage using advanced test selection

#### Non-functional Testing
• Evaluate code quality through static testing
• Validate system reliability with performance testing
• Prioritize user experience with UX testing
• Enhance user experience gradually through experimentation
• Automate adherence to compliance standards through conformance testing
• Experiment with failure using resilience testing to build recovery preparedness
• Verify service integrations through contract testing
• Practice eco-conscious development with sustainability testing

#### Security Testing
• Evolve vulnerability management processes to be conducive of DevOps practices
• Normalize security testing findings
• Use application risk assessments for secure software design
• Enhance source code security with static application security testing
• Evaluate runtime security with dynamic application security testing
• Validate third-party components using software composition analysis
• Conduct proactive exploratory security testing activities
• Improve security testing accuracy using interactive application security testing

#### Data Testing
• Ensure data integrity and accuracy with data quality tests
• Enhance understanding of data through data profiling
• Validate data processing rules with data logic tests
• Detect and mitigate data issues with anomaly detection
• Utilize incremental metrics computation

### Automated Governance

#### Secure Access and Delegation
• Centralize and federate access with temporary credential vending
• Delegate identity and access management responsibilities
• Treat pipelines as production resources
• Limit human access with just-in-time access
• Implement break-glass procedures
• Conduct periodic identity and access management reviews
• Implement rotation policies for secrets, keys, and certificates
• Adopt a zero trust security model, shifting towards an identity-centric security perimeter

#### Data Lifecycle Management
• Define recovery objectives to maintain business continuity
• Strengthen security with systematic encryption enforcement
• Automate data processes for reliable collection, transformation, and storage using pipelines
• Maintain data compliance with scalable classification strategies
• Reduce risks and costs with systematic data retention strategies
• Centralize shared data to enhance governance
• Ensure data safety with automated backup processes
• Improve traceability with data provenance tracking

#### Dynamic Environment Provisioning
• Establish a controlled, multi-environment landing zone
• Continuously baseline environments to manage drift
• Enable deployment to the landing zone
• Codify environment vending
• Standardize and manage shared resources across environments
• Test landing zone changes in a mirrored non-production landing zone
• Utilize metadata for scalable environment management
• Implement a unified developer portal for self-service environment management

#### Automated Compliance and Guardrails
• Adopt a risk-based compliance framework
• Implement controlled procedures for introducing new services and features
• Automate deployment of detective controls
• Strengthen security posture with ubiquitous preventative guardrails
• Automate compliance for data regulations and policies
• Implement auto-remediation for non-compliant findings
• Use automated tools for scalable cost management
• Conduct regular scans to identify and remove unused resources
• Integrate software provenance tracking throughout the development lifecycle
• Automate resolution of findings in tracking systems
• Digital attestation verification for zero trust deployments

#### Continuous Auditing
• Establish comprehensive audit trails
• Optimize configuration item management
• Implement systematic exception tracking and review processes
• Enable iterative internal auditing practices

### Observability

#### Strategic Instrumentation
• Center observability strategies around business and technical outcomes
• Centralize tooling for streamlined system instrumentation and telemetry data interpretation
• Instrument all systems for comprehensive telemetry data collection
• Build health checks into every service
• Set and monitor service level objectives against performance standards

#### Data Ingestion and Processing
• Aggregate logs and events across workloads
• Centralize logs for enhanced security investigations
• Implement distributed tracing for system-wide request tracking
• Aggregate health and status metrics across workloads
• Optimize telemetry data storage and costs
• Standardize telemetry data with common formats

#### Continuous Monitoring
• Automate alerts for security and performance issues
• Plan for large scale events
• Conduct post-incident analysis for continuous improvement
• Report on business metrics to drive data-driven decision making
• Detect performance issues using application performance monitoring
• Gather user experience insights using digital experience monitoring
• Visualize telemetry data in real-time
• Hold operational review meetings for data transparency
• Optimize alerts to prevent fatigue and minimize monitoring costs
• Proactively detect issues using AI/ML

## Guidelines and Recommendations

### DevOps Adoption Approach

1. Start with Leadership Commitment:
  > "DevOps adoption requires a dedicated leader to help facilitate continued progress, make resource decisions, and gain 
alignment with leaders throughout the organization."

2. Align with Business Objectives:
  > "DevOps adoption should not be an isolated project within the organization. It should be aligned to broader business 
goals, fully supported by leadership, with other teams also adopting capabilities to streamline their individual value 
streams."

3. Implement Gradually:
  > "There is no one-size-fits-all approach to adopting DevOps. Tailor these recommendations to suit your individual 
environment, quality, and security needs."

4. Focus on People and Culture First:
  > "It emphasizes that DevOps is first-and-foremost about people and culture, highlighting the significance of optimizing 
people-driven processes as the foundation for successful DevOps adoption."

5. Organize Teams Appropriately:
  > "Organize teams into distinct topology types (stream-aligned, platform, enabling, complicated subsystem) to optimize the 
value stream and achieve desired business outcomes."

6. Implement Continuous Integration and Delivery:
  > "Continuous integration (CI) is a software development practice where developers make regular, small alterations to the 
code and integrate them into a releasable branch of the code repository."

7. Automate Testing and Quality Assurance:
  > "Quality assurance emphasizes the integration of test-driven methodologies into every phase of the software development 
process."

8. Implement Automated Governance:
  > "Automated governance facilitates a balance between agility and control, providing assurance and accountability while 
enabling innovation and rapid deployment."

9. Establish Observability:
  > "Observability helps teams make timely decisions based on their systems' performance and how well they meet customer 
needs and business objectives."

### Team Structure Guidelines

1. Team Size:
  > "Keep team sizes manageable, and foster effective communication, collaboration, and decision-making. Regularly assess the
team's composition and structure, making adjustments as needed to maintain efficiency and effectiveness."

2. Team Topologies:
  > "Stream-aligned teams are responsible for delivering value to customers by focusing on specific product lines or customer
segments... Platform teams create and maintain shared infrastructure, tools, and services that support multiple stream-
aligned teams across the organization... Teams support other teams by providing just-in-time skills, knowledge, and 
expertise... Complicated subsystem teams are teams responsible for specialized subsystems within a larger system that require 
complex, deep domain knowledge and expertise."

3. Team Autonomy:
  > "Provide teams with the autonomy to make decisions and changes at the lowest level possible. Provide the necessary 
information, policies, and tools to make informed decisions aligned with the organization's goals and objectives."

## Important Concepts

### DevOps Sagas
DevOps Sagas are core domains within the software delivery process that collectively form AWS DevOps best practices. They 
represent a comprehensive approach to designing, developing, securing, and efficiently operating software at cloud scale.

### Capabilities
Capabilities are repeatable mechanisms that an organization can continuously improve to sustainably practice DevOps and 
achieve measurable outcomes. Each capability includes best practice indicators, metrics, and anti-patterns that can be tracked
and refined over time.

### Indicators
Indicators are best practices spanning people, process, and technology. They can be used as qualitative measurements to assess
and track an organization's ability to perform a capability. Indicators fall into three categories:
• **Foundational**: Essential requirements for minimum viability
• **Recommended**: Best practices that can improve performance
• **Optional**: Minor adjustments that further enhance implementation

### Anti-patterns
Anti-patterns are practices that might seem beneficial initially but have the potential to lead to unexpected or negative 
outcomes. They are indicators that can slow down or halt progress when adopting DevOps.

### Metrics
Metrics are quantifiable measures of an organization's ability to perform a capability. They help track how well an 
organization is implementing a capability.

### Team Topologies
The document references four team topologies from the book "Team Topologies" by Matthew Skelton and Manuel Pais:
1. Stream-aligned teams: Deliver value to customers by focusing on specific product lines
2. Platform teams: Create and maintain shared infrastructure, tools, and services
3. Enabling teams: Provide just-in-time skills, knowledge, and expertise
4. Complicated subsystem teams: Responsible for specialized subsystems requiring deep domain knowledge

### X as a Service (XaaS)
An interaction mode where a team provides an interface that can easily be integrated into the existing workflows of one or 
more teams, allowing for self-service capabilities.

### You Build It, You Run It
An approach where the team responsible for building a system is also responsible for running, maintaining, and owning it, 
minimizing handoffs and making teams both creators and custodians of their products.

### Guardian Model
A model where specialized champions or Guardians are embedded within individual teams to enhance and scale the capabilities of
centralized functions, such as security, quality, and audit.

## Examples and Use Cases

### Amazon's Operating Plan Process
│ "To kick start the yearly planning process, members of every team in the organization dedicate weeks of effort to focus on 
planning. The Senior Leadership team (S-Team) kicks off the process by defining business objectives. These high-level 
objectives are generally based on current business needs and future aspirations. Teams build their operating plans based on 
the leadership-defined expectations and objectives."

### Amazon's Weekly Business Reviews
│ "Within Amazon, teams and leaders meet regularly during weekly business reviews (WBRs) to assess the validity and quality of
KPIs against organizational goals. For a data-driven, systematic approach to this process, we follow the DMAIC—Define, 
Measure, Analyze, Improve, and Control—improvement cycle."

### Amazon's Two-Pizza Teams
│ "At Amazon, we call these small, autonomous teams with a single-threaded focus two-pizza teams. This approach minimizes 
handoffs and makes teams both the creators and custodians of their products."

### Amazon's Security Guardians
│ "We recommend adopting a Guardian Model within your organization to scale centralized functions. This involves embedding 
specialized champions or Guardians within individual teams to enhance and scale the capabilities of centralized functions, 
such as security, quality, and audit."

### Amazon's Working Backwards Process
│ "An example of this is the Amazon working backwards process. At Amazon, the development process begins with a document that 
outlines the product's core value to customers as a Press Release and Frequently Asked Questions (PRFAQ) document."

### Amazon's Ops Review Meetings
│ "Amazon implements this by holding weekly Ops review meetings and using the spinning wheel as a random selection method for 
which team will present. The randomness of the selection ensures that each team comes prepared, as any team can be called upon
to present."

## Cautions and Limitations

### DevOps Adoption Challenges
│ "There is no one-size-fits-all approach to adopting DevOps. Tailor these recommendations to suit your individual 
environment, quality, and security needs."

### Team Structure Considerations
│ "Not all operating models support a DevOps culture, and DevOps might not be suitable for every system. In some cases, 
especially in large and diverse organizations, it might be necessary to support stringent compliance requirements."

### Continuous Deployment Limitations
│ "This level of automation is a hallmark of mature DevOps practices. However, it is an optional capability as it is not 
always achievable or desired, especially in heavily regulated industries or in organizations with strict governance controls."

### Advanced Test Selection Cautions
│ "Using ML for this purpose introduces a level of uncertainty into the quality assurance process. If you do choose to 
implement predictive test selection, we recommend putting additional controls in place... We do not recommend using predictive
test selection to exclude security-related tests or relying on this approach for sensitive systems which are critical to your
business."

### Landing Zone Management
│ "For most organizations, a single landing zone that includes all environments for all workloads should suffice. Only under 
special circumstances, such as acquisitions, divestments, management of exceptionally large environments, specific billing 
requirements, or varying classification levels for government applications, might an organization need to manage multiple 
landing zones."

### Resilience Testing Cautions
│ "Before running resilience tests in either test or production environments, consider the use case, the benefits of the test,
and the system's readiness. Regardless of the target environment, always inform all stakeholders of the system before 
executing significant resilience tests."

## Additional Resources

### AWS Resources
• AWS Well-Architected Framework
• AWS Deployment Pipeline Reference Architecture
• AWS Observability Best Practices Guide
• AWS Cloud Adoption Framework: Operations Perspective
• AWS Ramp-Up Guide: DevOps Engineer
• The Amazon Builders' Library

### Books and Publications
• Team Topologies by Matthew Skelton and Manuel Pais
• The Lean Startup by Eric Ries
• Developmental Sequence in Small Groups by Bruce Tuckman
• How Do Committees Invent? by Melvin Conway

### Standards and Frameworks
• NIST Cybersecurity Framework
• ISO 27001
• CIS Controls
• DORA (DevOps Research and Assessment)
• SPACE Framework
• OWASP Top 10
• Common Vulnerability Scoring System (CVSS)
• Open Cybersecurity Alliance Schema Framework (OCSF)
• OpenTelemetry

### AWS Services Referenced
• AWS Control Tower
• AWS Organizations
• AWS CloudFormation
• AWS Cloud Development Kit (CDK)
• AWS CodeGuru
• AWS CloudWatch
• AWS X-Ray
• AWS Config
• AWS Security Hub
• AWS Fault Injection Service
• AWS Resilience Hub
• AWS Audit Manager
• AWS Backup
• AWS Proton
• AWS Service Catalog
• AWS Secrets Manager
• AWS Certificate Manager
• AWS Key Management Service
