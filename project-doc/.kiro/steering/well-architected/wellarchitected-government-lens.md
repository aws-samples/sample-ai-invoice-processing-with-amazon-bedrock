---
inclusion: manual
---

# AWS Well-Architected Framework Government Lens - Steering File

## Document Overview

The Government Lens for the AWS Well-Architected Framework provides architectural and operational best practices for designing and operating reliable, secure, efficient, effective, sustainable, and compliant government services on AWS. It addresses the unique requirements, context, and responsibilities of government organizations, expanding upon the standard AWS Well-
Architected Framework to include government-specific considerations. The document was published by AWS on January 10, 2024 and serves as a guide for anyone responsible for or involved in the design and delivery of government services on AWS.

## Key Topics

1. Government-specific design principles
2. Special requirements and context for government services
3. Common government scenarios and reference architectures
4. Government-specific considerations for each Well-Architected Framework pillar
5. Service outcomes for government
6. Operational models for government services
7. Security and privacy considerations for government
8. Reliability and continuity for critical government services
9. Performance efficiency in policy implementation
10. Cost optimization in a public value context
11. Sustainability in government operations
12. Artificial intelligence in the public sector
13. Classified information systems
14. Omni-channel public services
15. Open government methods and tools
16. Verifiable credentials for government

## Best Practices

### General Design Principles

1. Design with purpose
   • Understand mission, mandate, and policy objectives
   • Define intended impact and measurement framework
   • Include customer/user feedback in measurements
   • Consider potential risks to the community

2. Design with end users
   • Include end users in research, design, testing, and improvement
   • Define who end users are clearly
   • Test multiple solution concepts with users
   • Establish feedback mechanisms for continuous improvement

3. Make services simple and intuitive
   • Design for simplicity and intuitive use
   • Engage diverse user groups throughout development
   • Use simple and clear language
   • Maintain consistent design across services

4. Iterate and improve frequently
   • Establish mechanisms for collecting and responding to feedback
   • Enable frequent product improvements
   • Streamline deployment processes
   • Ensure ongoing funding and resources past initial launch

5. Collaborate and work in the open by default
   • Share non-sensitive data, code, evidence, research, and decision-making
   • Use open standards and open-source licensing where possible
   • Enable public participation in design and improvements
   • Share work for reuse by other governments

6. Address security and privacy risks
   • Implement appropriate privacy and security measures
   • Support frictionless security for service operations
   • Practice responsible data stewardship
   • Understand jurisdictional requirements for identity and data sharing

7. Build inclusive services
   • Meet or exceed accessibility standards
   • Provide offline options to complement online channels
   • Design omni-channel services
   • Engage users with distinct needs from the outset

8. Design trustworthy services
   • Make services explainable, auditable, and appealable
   • Include ethical considerations in design and governance
   • Comply with relevant ethical guidelines
   • Ensure fair and equitable treatment

9. Measure, report, and take data-driven decisions
   • Define success metrics for government services
   • Build measurement capabilities from the beginning
   • Use testing and actual data to drive decision-making
   • Monitor service performance, user experience, and policy impact

10. Consider composable architecture and reusability
    • Design modular, extendable architectures
    • Leverage existing design systems and component catalogs
    • Use defined core environments or components
    • Engage with government architectural standards

11. Maintain service continuity
    • Design resilient architectures for critical services
    • Take a risk-based approach to architectural decisions
    • Plan for service disruptions and recovery

### Operational Excellence

1. Reshape the operating model
   • Establish persistent multi-disciplinary team structures
   • Enable delegation of delivery decision-making
   • Create a Concept of Operations document
   • Consider all relevant feedback loops
   • Use minimum viable product deployment models where viable
   • Document and engage with cultural context

2. Verify digital experiences remain operational and relevant
   • Support staff to operate the service effectively
   • Embed continuous improvement into the operating model
   • Implement design-led agile development and funding frameworks

3. Ensure operational transparency
   • Document operational accountability requirements
   • Plan how citizens and companies will be kept informed

4. Improve solution definition criteria
   • Test multiple concepts with end users
   • Identify patterns in service capabilities
   • Define foundational reusable components

5. Improve solution acquisition criteria
   • Prioritize reuse where appropriate
   • Consider build versus buy/acquire strategically
   • Share code, research, and efforts
   • Take a sustainable approach to sourcing
   • Consider suitability of solution licensing

6. Manage organizational risk
   • Take an all-hazards approach
   • Develop a risk management plan
   • Align with required compliance frameworks
   • Determine necessary conditions of engagement

### Security

1. Verify privacy-by-design
   • Elevate encryption beyond basics
   • Document privacy and end user control considerations
   • Give end users appropriate control over their data
   • Minimize data copies where avoidable
   • Enforce exposure consequences

2. Shift to real-time security model
   • Conduct threat modeling and scenario planning
   • Test and document real-time threat detection and disruption
   • Document critical infrastructure considerations

### Reliability

1. Test service and demonstrate resilience
   • Establish test-driven design and implementation
   • Conduct scenario testing and mitigation planning
   • Seek peer review of reliability planning

2. Plan for service continuity
   • Assess impact of downtime and service deadlines
   • Plan for graceful degradation with appropriate fail-overs
   • Document processes for post-incident reviews and reporting

### Performance Efficiency

1. Report outcomes performance
   • Document public and governmental reporting mechanisms
   • Define measurement and monitoring approach
   • Document compliance foundations and ongoing costs

2. Manage continuous change for service reliability
   • Document processes, costs, and resourcing for various change scenarios

### Cost Optimization

1. Demonstrate value for money in government context
   • Document the definition of value for money for the jurisdiction
   • Define cost and value reporting mechanisms
   • Build in-house capability to manage costs
   • Leverage existing solutions and capabilities
   • Engage with professional networks and user groups
   • Optimize for speed of change when necessary
   • Align with budget planning processes

### Sustainability

1. Align with jurisdictional sustainability policies
   • Document sustainability reporting mechanisms
   • Minimize duplication of computing power
   • Share best sustainability practices
   • Identify sharable data
   • Identify relevant sustainability policies

2. Design for sustainability outcomes
   • Include jurisdictional sustainability goals
   • Use contextual design methods
   • Minimize physical impact of services

3. Build extendable solutions
   • Leverage automation and virtualization
   • Consider low energy sensor technologies

## Guidelines and Recommendations

### Artificial Intelligence in the Public Sector

1. Clearly delineate between systems requiring explainability and those that don't
   • Systems deciding eligibility for social services require explainability
   • General research or patterns analysis may not require the same level of explainability

2. Address bias in AI systems
   • Implement good practices for identifying and addressing bias in training data
   • Monitor AI models for bias continuously

3. Monitor measurable impacts
   • Track intended and unintended impacts on people, communities, and environment
   • Incorporate user and staff feedback for continuous improvement

4. Ensure lawfulness of outcomes
   • Make sure AI systems produce demonstrably lawful outcomes, especially for decision-making

5. Maintain transparency
   • Be transparent about when and how AI is used
   • Provide clear information to users interacting with AI systems

6. Focus on augmentation over automation
   • Use AI to improve policy and community outcomes
   • Avoid focusing solely on efficiency through automation

7. Build public trust
   • Design systems that are perceived as lawful, fair, and trustworthy

8. Consider AI usage patterns and appropriate governance
   • Analytical AI: Systems that perform analysis, identify patterns, produce trends
   • Process Automation: Systems that automate existing or inferred processes
   • Automated Decision Making: Systems that generate specific decisions or actions
   • Generative AI: Systems that produce consumable content
   • Virtual Assistance: Systems that provide assistance or augment user experience

### Classified Information Systems

1. Govern business information systematically throughout its lifecycle
2. Create only necessary business information
3. Describe business information adequately
4. Store and preserve business information suitably
5. Define retention periods for business information
6. Destroy or transfer business information accountably
7. Save business information in manageable and monitorable systems
8. Make business information available for use and reuse

### Omni-Channel Public Services

1. Ensure consistency across channels
   • Maintain consistent functionality and features across all channels
   • Use a virtualized presentation layer for all channels

2. Implement an integration layer
   • Provide secure, consistent management of data, content, rules, and functions
   • Enable common business functions across all channels

3. Design for channel agility
   • Allow channels to evolve according to new technologies and user needs
   • Decouple channel management from business systems

4. Enable measurement and monitoring
   • Use the same infrastructure to measure, monitor, and model impacts across channels

### Open Government Methods and Tools

1. Work in the open
   • Share tools, code, and progress publicly when possible
   • Enable peer review, partnerships, and public participation

2. Publish and reuse open-source software
   • Understand open-source policies and requirements
   • Explore reuse of existing open-source solutions

3. Implement algorithmic transparency
   • Consider publishing algorithms used for automated decision-making
   • Provide explainability for algorithmic decisions

4. Report performance publicly
   • Publish performance data through public dashboards
   • Define useful metrics for monitoring and reporting

5. Share open government data
   • Identify non-private data that can provide value if shared
   • Establish mechanisms for publishing and accessing data

### Verifiable Credentials for Government

1. Establish government as a trust anchor
   • Issue digital credentials that can be used to make other credentials trustworthy
   • Leverage decentralized architecture of VCs and Digital Identities

2. Implement verifiable credential architecture
   • Enable programmatic verification of claims in real time
   • Ensure credentials are trustworthy for stakeholders
   • Provide personalized service without oversharing personal information
   • Make VCs available as a utility for multiple use cases

3. Ensure proper credential governance
   • Sign VCs from central, reliable sources
   • Align VCs with legislative or administrative scope
   • Provide human-understandable descriptions
   • Map VC domains to legislation or international agreements
   • Implement testing to ensure quality claims

## Important Concepts

1. Government Service Context
   • Government services have special legal, legislative, accountability, and trust requirements
   • Services often have significant impact on society
   • Different governments operate in unique cultural and historical contexts
   • Services must be designed with awareness of jurisdictional requirements

2. Value for Money in Government
   • Definition varies across jurisdictions
   • May include best functionality for cost to deliver policy outcomes
   • May consider balance of social, public, and environmental benefits alongside cost
   • Influences how cost optimization is perceived and implemented

3. Administrative Law Compliance
   • Government systems must comply with principles of Administrative Law
   • Decision-making must be explainable, accountable, appealable, consistent with law
   • High-integrity record keeping is critical
   • Services should be auditable in real time

4. Service Effectiveness Measurement
   • Policy outcomes: Measuring how well the service delivers on policy intentions
   • Human outcomes: Monitoring impacts on quality of life and well-being
   • User outcomes: Tracking what "done" means for users
   • User satisfaction: Measuring end-user experience and expectations

5. Government as a Platform (GaaP)
   • Providing reusable modular components for common functions
   • Components include payments, notifications, identity verification, form collection
   • Allows service teams to focus on unique aspects of their service

6. Digital Nations Charter
   • Commitment to digital reform and best practices
   • Prioritizes open government, open data, open source, open standards, open markets
   • Supports sustainable digital transformation of governments

7. Open Government
   • Citizens have right to access documents and proceedings
   • Includes transparency, public reporting, accountability mechanisms
   • Often includes public participation in improving services and policies

## Examples and Use Cases

### Artificial Intelligence in Public Sector

1. NASA using AWS to protect life and infrastructure
2. Forecasting spread of COVID-19
3. Using AI to rethink document automation and extract insights
4. Chesterfield County Public Schools using machine learning to predict chronic absenteeism
5. Using advanced analytics to accelerate problem solving
6. Tackling global teacher shortage with AI and ML
7. Improving school safety with cloud solutions
8. Hurricane response and preparation

### Reference Architectures

1. Citizen Engagement Architecture
   • Integrates mobile applications, web portals, call centers, and chatbots
   • Handles high volumes of real-time ingestion from public and private sources
   • Implements different data protection based on classification
   • Uses event-driven architecture for scalability

2. Regulatory Reporting Architecture
   • Builds reporting data lake on AWS
   • Implements data quality, integrity, and lineage in pipelines
   • Encrypts data at rest and in transit
   • Masks or tokenizes PII data
   • Uses data catalogs with fine-grained access control

3. Distributed Processing of Sensitive Documents
   • Separates processing in segmented ways for heightened security
   • Enables effective processing of confidential information
   • Maintains segregated environments

4. Omni-channel Public Services Architecture
   • Provides virtualized presentation layer
   • Offers reusable service components through integration layer
   • Enables consistent experience across channels
   • Supports flexibility for channel-specific optimization

5. Verifiable Credentials Trust Graph
   • Combines claims from various departments
   • Enables verification of entity identity and information
   • Supports automated verification of document integrity
   • Creates trust chains through credential connections

## Cautions and Limitations

1. AI System Risks
   • AI systems can perpetuate bias and inaccuracies from past systems
   • ML-based Automated Decision Making systems currently lack traceability to legal authority
   • Generative AI can create reputational risk if content is perceived as representing government
   • Virtual assistance systems can directly influence public perception of institutions

2. Privacy Considerations
   • Government privacy requirements can be extremely strict
   • Personalized service delivery must be balanced with user control and privacy
   • Data copies should be minimized where possible
   • Vendor contracts must inherit privacy obligations

3. Service Continuity Risks
   • Unexpected downtime in critical services can endanger quality of life
   • Services like emergency services, welfare payments, and healthcare cannot tolerate disruption
   • Impact of downtime around deadlines (elections, emergencies) must be assessed

4. Operational Model Challenges
   • Functionally segmented structures create challenges for modern delivery
   • Technology in corporate silos or outsourced creates operational divides
   • Project-based teams disbanded after completion leave services without product management
   • Fixed funding models can make continuous improvement difficult

5. Compliance Limitations
   • Standards often don't prescribe how agencies should meet requirements
   • Agencies vary in size, complexity, culture, risk tolerance, legacy systems, and resources
   • Implementation must be tailored to specific circumstances

## Additional Resources

1. AWS Compliance Programs
2. Open source at AWS
3. AWS Cloud Adoption Framework (AWS CAF)
4. AWS Cloud Adoption Framework whitepaper
5. Risk Management in the AWS Cloud Adoption Framework
6. AWS risk and compliance program
7. Building your Cloud Operating Model
8. How governments can transform services securely in the cloud
9. AWS digital and operational transformation guidance
10. Digital Transformation: The Why, Who, How, and What – Parts 1 & 2
11. Four Steps Toward Digital Government
12. AWS Digital Sovereignty Pledge
13. AWS Shield Advanced Developer Guide
14. Security, Identity, and Compliance on AWS
15. AWS Risk and Compliance whitepaper
16. AWS Clean Rooms
17. AWS Data Exchange
18. Protect critical services with Continuity of Government IT on AWS solution guide
19. Leverage the latest cloud technologies to build a resilient organization
20. Modernizing government for the new normal: Advice for building resilience
21. AWS Well-Architected game days
22. New Performance Dashboard on AWS for open, responsive government
23. Four steps to build a data strategy for managing performance in the public sector
24. Raising the bar on accessibility for open-source public sector solutions
25. AWS Tools for Reporting and Cost Optimization whitepaper
26. AWS Solutions Library
27. AWS Construct Library
28. AWS Serverless Application Repository
29. How cloud can help agencies enhance security, save costs, and improve mission delivery through the Technology Modernization
Fund (TMF)
30. For Small Governments – The Cloud is Only as Big as You Want it to Be
31. Optimizing nonprofits' costs in the cloud
32. AWS Customer Carbon Footprint Tool
33. UN/CEFAFT White Paper on eDATA Verifiable Credentials for Cross Border Trade
