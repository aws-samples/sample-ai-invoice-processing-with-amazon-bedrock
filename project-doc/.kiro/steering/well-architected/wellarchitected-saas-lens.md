---
inclusion: manual
---

# AWS Well-Architected Framework SaaS Lens - Steering Guide

## Document Overview

The AWS Well-Architected Framework SaaS Lens provides architectural best practices for designing, deploying, and architecting 
multi-tenant software as a service (SaaS) applications in the AWS Cloud. It extends the AWS Well-Architected Framework by 
focusing on SaaS-specific considerations across the six pillars: operational excellence, security, reliability, performance 
efficiency, cost optimization, and sustainability. The document helps technology leaders understand AWS best practices and 
strategies for SaaS architectures.

## Key Topics

1. SaaS Fundamentals
   • Tenant definitions and management
   • SaaS deployment models (Silo, Pool, and Bridge)
   • SaaS identity and tenant isolation
   • Data partitioning strategies

2. General Design Principles for SaaS
   • Architectural considerations
   • Tenant isolation and security
   • Growth and scaling strategies
   • Metrics and instrumentation

3. Common SaaS Architecture Scenarios
   • Serverless SaaS
   • Amazon EKS SaaS
   • Full stack isolation
   • Hybrid SaaS deployment
   • Multi-tenant microservices
   • Tenant insights

4. Well-Architected Pillars for SaaS
   • Operational excellence in SaaS
   • Security in multi-tenant environments
   • Reliability in SaaS applications
   • Performance efficiency for multi-tenant workloads
   • Cost optimization for SaaS
   • Sustainability in SaaS environments

## Best Practices

### SaaS Architecture Design

1. No One-Size-Fits-All Approach
   • Recognize that SaaS architecture varies based on business needs, domain, compliance requirements, market segments, and 
solution nature
   • Ensure all architectures enable tenant onboarding, management, and operations through a single pane of glass

2. Service Decomposition
   • Decompose services based on multi-tenant load and isolation profiles
   • Consider how compliance, noisy neighbor concerns, and tenant tiers influence service design

3. Tenant Resource Isolation
   • Implement robust isolation strategies across all architecture layers
   • Ensure any attempt to access tenant resources is validated for the current tenant context

4. Growth-Oriented Design
   • Build highly agile, frictionless environments that accommodate spikes in tenant onboarding
   • Design for growth without expanding operational or infrastructure footprint

5. Tenant Metrics
   • Instrument applications to capture tenant-specific metrics
   • Surface insights into tenant feature usage, system load, bottlenecks, and cost profiles

6. Automated Tenant Onboarding
   • Implement single, automated, repeatable processes for tenant onboarding
   • Promote scale and enable growth through frictionless onboarding

7. Multi-Tier Tenant Support
   • Plan for multiple tenant experiences within a single environment
   • Build constructs to support different tenant tiers without requiring one-off product versions

8. Customization Through Configuration
   • Support one-off requirements through global customization options
   • Implement features as configuration options available to all customers

9. User-Tenant Identity Binding
   • Bind user identity to tenant identity as a first-class construct
   • Enable easy access to tenant context throughout the application

10. Infrastructure-Activity Alignment
    • Align infrastructure consumption with tenant activity
    • Employ policies that limit over-provisioning

11. Limited Developer Awareness of Multi-Tenancy
    • Minimize developer exposure to tenancy concepts
    • Provide libraries and reusable constructs that hide tenancy details

12. Business-Focused Approach
    • Treat SaaS as a business strategy, not just a technical implementation
    • Design for agility, innovation, and operational efficiency

13. Tenant-Aware Operations
    • Create operational views that provide insights into tenant and tier activity
    • Enable troubleshooting through the lens of individual tenants

14. Tenant Cost Measurement
    • Measure the cost impact of individual tenants
    • Understand how tenant consumption patterns affect cost profiles

### Operational Excellence

1. Tenant-Aware Monitoring
   • Create operational dashboards with views of health by tenant and tenant tier
   • Include the ability to drill into operational data for individual tenants

2. Frictionless Tenant Onboarding
   • Automate the creation, configuration, and provisioning of tenant resources
   • Orchestrate shared services to configure all resources needed for new tenants

3. Tenant Customization Management
   • Use feature flags to introduce customization without creating separate product versions
   • Apply customization options selectively to avoid unmanageable complexity

4. Tenant Metrics Collection
   • Instrument applications to publish rich tenant metrics
   • Capture operational usage patterns fundamental to understanding multi-tenant loads

### Security

1. SaaS Identity Implementation
   • Associate tenant context with users during authentication
   • Inject tenant context at the point where users enter the application
   • Use custom claims or attributes to bind tenant context to user identity

2. Tenant Isolation Strategies
   • Ensure isolation is a foundational element of SaaS design
   • Implement isolation enforcement outside developer view
   • Consider domain-specific isolation requirements

3. Isolation Models
   • **Silo Isolation**: Deploy fully isolated stacks for each tenant
   • **Pool Isolation**: Share resources across tenants with logical isolation
   • **Bridge Isolation**: Combine silo and pool models based on service needs
   • **Tier-Based Isolation**: Vary isolation strategies by tenant tier
   • **Targeted Isolation**: Apply different isolation models to different microservices

### Reliability

1. Tenant Load Management
   • Implement throttling to prevent tenants from consuming excess resources
   • Use usage plans to define separate experiences for different tenant tiers

2. Proactive Tenant Health Monitoring
   • Surface tenant-aware reliability data
   • Build alarms and automation to heal issues before they impact tenants

3. Multi-Tenant Testing
   • Test cross-tenant impact scenarios
   • Validate tenant consumption patterns
   • Verify tenant workflow performance
   • Test tenant onboarding resilience
   • Validate API throttling policies
   • Test data distribution strategies
   • Verify tenant isolation enforcement

### Performance Efficiency

1. Cross-Tenant Performance Protection
   • Prevent one tenant from adversely impacting others
   • Consider selective service isolation for critical performance areas
   • Implement effective scaling strategies for shared infrastructure

2. Resource-Activity Alignment
   • Align infrastructure consumption with tenant activity
   • Consider serverless technologies to match consumption with actual load
   • Capture and publish tenant consumption metrics for scaling policies

3. Tiered Performance Management
   • Enable varying performance levels for different tenant tiers
   • Implement throttling policies based on tenant tiers
   • Consider architectural optimizations for premium tiers

### Cost Optimization

1. Tenant Consumption Measurement
   • Design consumption mapping models to attribute resource usage to tenants
   • Focus on areas that contribute most to your AWS bill
   • Balance granularity with instrumentation complexity

2. Tenant Cost Correlation
   • Correlate tenant consumption with infrastructure costs
   • Calculate cost per tenant to guide business and architectural decisions
   • Analyze cost distribution across tenant tiers

### Sustainability

1. Deployment Model Optimization
   • Use appropriate deployment models (silo, bridge, pool) to align tenant consumption with resource utilization
   • Understand operational tradeoffs of each model

2. Resource Value Maximization
   • Use managed services to optimize hardware utilization
   • Right-size compute resources based on architecture
   • Consider serverless computing to automatically scale resources as needed

3. Tenant Off-boarding Planning
   • Maintain an updated list of infrastructure resources per tenant
   • Create and test tenant off-boarding runbooks
   • Automate decommissioning processes
   • Ensure data archiving meets compliance requirements

4. Per-Tenant Footprint Visibility
   • Instrument applications to collect per-tenant metrics
   • Monitor infrastructure usage patterns by tenant
   • Provide dashboards showing tenant operational data

## Guidelines and Recommendations

### SaaS Identity

1. Implement tenant context in authentication:
  

   The key attribute of the SaaS identity is that it elevates tenant context to a first-class construct, connecting it directly to the overall authentication and authorization model of your SaaS application.
   


2. Use JWT tokens to convey tenant context:
  

   The authorizer would extract the tenant context from the incoming JWT and publish an event that records this activity for the tenant.
   


3. Flow tenant context through microservices:
  

   This service can now acquire and apply the context from this token without calling another service... This illustrates how the tenant context can flow across all of your microservice calls without adding any additional lookups or latency.
   


### Tenant Isolation

1. Treat isolation as non-optional:
  

   Isolation is a foundational element of SaaS and every system that delivers a solution in a multi-tenant model should ensure that their systems take measures to ensure that tenant resources are isolated.
   


2. Don't rely solely on authentication:
  

   While it is expected that you will control access to your SaaS environments through authentication and authorization, getting beyond the entry points of a login screen or an API does not mean you have achieved isolation. This is just one piece of the isolation puzzle and is not enough on its own.
   


3. Enforce isolation outside developer code:
  

   While developers are never expected to introduce code that might violate isolation, it's unrealistic to expect that they will never unintentionally cross a tenant boundary. To mitigate this, scoping of access to resources should be controlled through some shared mechanism that is responsible for applying isolation rules (outside the view of developers).
   


4. Consider logical isolation for shared resources:
  

   Even in scenarios where resources are shared—in fact, especially in environments where resources are shared—there are ways to achieve isolation. In this shared resource model, isolation can be a logical construct that is enforced by runtime applied policies.
   


### Tenant Onboarding

1. Automate the onboarding process:
  

   By creating an architecture that promotes a frictionless, repeatable onboarding process, SaaS organizations are able to streamline, optimize, and scale their ability to introduce new tenants into their SaaS environment.
   


2. Orchestrate shared services:
  

   The registration service will then sit at the middle of the onboarding process, orchestrating all the services needed to create the new tenant environment.
   


### Tenant Customization

1. Use feature flags for customization:
  

   A common approach to this problem is to use feature flags. Feature flags are commonly used by application developers as a way to have multiple paths of execution in a common code base with flags that enable or disable each of the different capabilities at runtime.
   


2. Avoid one-off customizations:
  

   As a rule of thumb, the business should not see this as a sales tool that enables the organization to offer one-off customizations to new customers.
   


### Tenant-Aware Operations

1. Create tenant-specific operational views:
  

   A SaaS operations dashboard, for example, should include views of health that are presented through the lens of tenants and tenant tiers. While viewing the global view of health is still part of this experience, a SaaS operations team also needs the ability to see the health and activity of tenants.
   


2. Inject tenant context into operational data:
  

   This requires SaaS architects to give care consideration to how and where they can inject tenant context into the various mechanisms that are used to record health and activity events. For example, logs should include mechanisms to ensure that tenant context (such as tenant identifier and tier) are injected into your system's log data.
   


### Tenant Performance Management

1. Implement throttling by tenant tier:
  

   This approach uses separate API keys for the basic and advanced tiers of the system and these keys are connected to usage plans that have different SLAs. This approach enables two different levels of control. First, it can ensure that all tenants are prevented from saturating our system with requests through the configuration of the usage plans. The other benefit is that we can use these usage plan configurations to prevent lower tier tenants from impacting the experience of higher tier tenants.
   


2. Consider serverless for consumption alignment:
  

   The simplest approach to aligning consumption with activity is to use AWS services that provide a serverless experience. The classic example of this would be AWS Lambda. With AWS Lambda, you can build a model where servers and scaling policies are no longer your responsibility. With serverless, your SaaS application will only incur those charges that are directly correlated with tenant consumption.
   


3. Use reserve concurrency for tier-based performance:
  

   In AWS Lambda, you can use reserve concurrency to limit the consumption of a given tenant tier... The Basic tier has a reserve concurrency of 100 and the Advanced tier has 300. The idea here is that the consumption of my lower end tiers will be capped, leaving all the remain concurrency for the premium tier.
   


### Tenant Cost Management

1. Attribute consumption to tenants:
  

   Measuring and attributing costs in a multi-tenant environment begins with having a solid strategy for attributing consumption to tenants. This will require teams to design and develop a consumption mapping model that represents a clear view of how tenants are consuming the resources of your system.
   


2. Analyze cost distribution by tier:
  

   This graph illustrates the distribution of costs across the tiers of a SaaS offering. Here you'll see a large difference between the infrastructure costs of Basic and Advanced tier tenants. The key observation is that the Basic tier, which generates the smallest revenue, is responsible for the largest portion of the system's infrastructure costs.
   


## Important Concepts

### Tenant
A tenant is a customer that signs up to use your SaaS application. All customers using your SaaS environment collectively are 
the tenants of your system. Each tenant typically has a tenant administrator who can configure the system and add users to 
their tenant environment.

### SaaS Deployment Models
1. Silo Model: Tenants are provided dedicated resources. Even with dedicated resources, a silo environment still relies on 
shared identity, onboarding, and operational experiences.

2. Pool Model: Tenants share resources, achieving economies of scale, manageability, and agility. Resources can include 
compute, storage, messaging, etc.

3. Bridge Model: A mixed mode where some parts of the system use silo and others use pool. This acknowledges that SaaS 
businesses aren't always exclusively silo or pool.

### SaaS Identity
SaaS identity extends traditional identity by incorporating tenancy. After authenticating a user, the system needs to know 
both who the user is and which tenant they're associated with. This merged user-tenant identity provides the tenant context 
used throughout the application.

### Tenant Isolation
Tenant isolation ensures that each tenant is prevented from accessing another tenant's resources. Isolation strategies vary 
based on domain, compliance, deployment model, and AWS services used. Isolation can be implemented through:
• Physical separation (silo model)
• Logical separation with runtime policies (pool model)
• A combination of both approaches (bridge model)

### Data Partitioning
Data partitioning refers to how multi-tenant data is organized. Options include separate databases per tenant or comingled 
data in shared constructs with logical separation.

### Noisy Neighbor
The concept where one tenant's activity could degrade the experience of other tenants by placing excessive load on shared 
resources. SaaS architectures must employ strategies to manage and minimize potential impacts of noisy tenants.

### Tenant Tiers
Different pricing and experience levels offered to different market segments. Supporting various tiers requires architectural 
constructs that shape the experience of each tier, influencing cost, operations, management, and reliability.

### Tenant-Aware Operations
The need for additional mechanisms and tooling to create tenant-aware insights into activity and consumption patterns of 
individual tenants and tiers. This allows viewing system activity and health through the lens of individual tenants.

## Examples and Use Cases

### Serverless SaaS Architecture
The moving parts of a Serverless SaaS architecture aren't all that different than a classic serverless web application architecture. On the left of this diagram, you see that we have our web application hosted and served from an Amazon S3 bucket (presumably using one of the modern client frameworks like React, Angular, etc.).

In this architecture, the application is leveraging Amazon Cognito as our SaaS identity provider. The authentication experience here yields a token that includes our SaaS context that is conveyed via a JSON Web Token (JWT). This token is then injected into our interactions with all downstream application services.

### Amazon EKS SaaS Architecture
For container-based environments, much of the architecture is focused on how to successfully ensure that we're preventing cross-tenant access. While there can be a temptation to allow tenants to share containers, this presumes that tenants would be comfortable with a notion of soft multi-tenancy.

The general guidance for building SaaS architectures with Amazon EKS is to prevent any sharing of containers across tenants. While this adds complexity to the footprint of the architecture, it addresses the fundamental need to ensure that we have created an isolation model that will address the domain, compliance, and regulatory needs of multi-tenant customers.

### Full Stack Isolation Example
Each tenant environment in this model is straightforward. You'll see here that we've provided a separate VPC for each tenant. These VPCs hold the full isolated stack that will be used by each tenant. The compute and storage constructs could be composed from any combination of AWS services. The key is that each tenant environment is meant to have the same infrastructure configuration and the same version of your product.

### Hybrid SaaS Deployment
In this diagram, you'll notice that we have two separate deployments of our SaaS environment. The left side is deployed in a pooled model with shared infrastructure. The majority of our tenants are running in this environment. However, on the right side, we've deployed a separate copy of the multi-tenant environment that is hosting one tenant (tenant 4).

The key to this strategy is that both environments (the left and right) are running the same version of the SaaS application. Any new changes or updates are applied to both environments at the same time. More importantly, you'll see that we have a single, unified management experience that spans both of these environments.

### Multi-Tenant Microservices Development
The key idea here is that we've taken anything that relies on tenant context and used libraries to apply multi-tenant policies.

This example illustrates a number of scenarios where a SaaS microservice might need access to tenant context. The flow starts with a call into our microservice with a request to get a list of products. Somewhere in the code of our service, your service logs a message. The microservice developer simply logs a message to a logging wrapper. This wrapper gets the tenant context from the Token Manager and injects that context into our message that is, in this example, published to Amazon S3.

### Tenant Cost Analysis
This graph illustrates the distribution of costs across the tiers of a SaaS offering. Here you'll see a large difference between the infrastructure costs of Basic and Advanced tier tenants. The key observation is that the Basic tier, which generates the smallest revenue, is responsible for the largest portion of the system's infrastructure costs. Meanwhile, the Advanced tier, which generates the most revenue, has a much smaller cost footprint. This imbalance likely means there's something wrong with our model.

## Cautions and Limitations

### Silo Model Challenges
1. Scaling issues: Account limits may prevent scaling to many tenants
2. Cost inefficiency: Dedicated resources may remain idle during low-usage periods
3. Reduced agility: Decentralized nature adds complexity to management and operations
4. Onboarding complexity: Provisioning new infrastructure for each tenant adds overhead
5. Management complexity: Aggregating data from decentralized tenant footprints is more complex

### Pool Model Risks
1. Noisy neighbor concerns: One tenant's activity may impact others
2. Cost tracking challenges: Attributing resource consumption to specific tenants is more difficult
3. Wider impact scope: Outages may affect all tenants simultaneously
4. Compliance challenges: Some regulatory requirements may not be satisfied by shared infrastructure

### Feature Flag Cautions
While this can be a powerful construct, it should be applied with caution. If, by introducing feature flags, you create a complex maze of options that end up presenting every tenant a unique experience, your system will quickly become unmanageable. Try to be selective about how and when you introduce these flags.

### Tenant Isolation Warnings
While the need for tenant isolation is viewed as essential to SaaS providers, the strategies and approaches to achieving this isolation are not universal. There are a wide range of factors that can influence how tenant isolation is realized in any SaaS environment. The domain, compliance, deployment model, and the selection of AWS services all bring their own unique set of considerations to the tenant isolation story.

### Cross-Tenant Access Risks
Crossing this boundary in any form would represent a significant and potentially unrecoverable event for a SaaS business.

## Additional Resources

### Documentation and Blogs
• GPSTEC309-SaaS Monitoring Creating a Unified View of Multi-tenant Health featuring New Relic Slides
• Feature Toggles (aka Feature Flags)
• Tenant Onboarding Best Practices in SaaS with the AWS Well-Architected SaaS Lens
• Isolating SaaS Tenants with Dynamically Generated IAM Policies
• Partitioning Pooled Multi-Tenant SaaS Data with Amazon DynamoDB
• Multi-tenant data isolation with PostgreSQL Row Level Security
• Identity Federation and SSO for SaaS on AWS
• Managing SaaS Identity Through Custom Attributes and Amazon Cognito
• Onboarding and Managing Agents in a SaaS Solution
• Throttling a tiered, multi-tenant REST API at scale using API Gateway (Parts 1 & 2)
• Monolith to serverless SaaS: Migrating to multi-tenant architecture
• Testing SaaS Solutions on AWS
• Calculating Tenant Costs in SaaS Environments
• Building Sustainable, Efficient, and Cost-Optimized Applications on AWS

### Whitepapers
• SaaS Tenant Isolation Strategies whitepaper
• SaaS Storage Strategies whitepaper
• AWS Well-Architected Framework whitepaper
• Operational Excellence Pillar whitepaper
• Serverless Applications Lens whitepaper

### Videos
• AWS re:Invent 2016: The Secret to SaaS (Hint: It's Identity) (GPSSI404)
• AWS re:Invent 2017: GPS: SaaS Monitoring - Creating a Unified View of Multi-tenant Health featuring New Relic (GPSTEC309)
• AWS re:Invent 2017: SaaS and OpenID Connect: The Secret Sauce of Multi-Tenant Identity
• AWS re:Invent 2019: SaaS tenant isolation patterns
• AWS re:Invent 2019: Building serverless SaaS on AWS
• AWS re:Invent 2018: SaaS Reference: Review of Real-World Patterns & Strategies
• SaaS Metrics: The Ultimate View of Tenant Consumption

### Tools and Labs
• AWS Well-Architected Tool (SaaS Lens available in the Lens Catalog)
• AWS Well-Architected Labs for Sustainability Pillar
• AWS Well-Architected Labs – Cloud Intelligence Dashboards
