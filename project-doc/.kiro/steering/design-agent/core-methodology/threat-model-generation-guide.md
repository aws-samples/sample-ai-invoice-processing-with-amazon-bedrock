---
inclusion: manual
---

# Threat Model Generation Methodology v2.0

## Overview

This methodology provides a systematic approach for generating comprehensive, enterprise-grade threat model documents that follow industry best practices including STRIDE methodology, AWS security standards, and OWASP guidelines. This guide is designed to produce detailed threat models similar to AWS ThreatComposer outputs and enterprise security assessments.

## Target Output Format

**CRITICAL**: The threat models generated using this methodology MUST follow the EXACT format defined in the template file: `docs/threat-model-template.md`

### Template Reference

The complete threat model template is located at: **`docs/threat-model-template.md`**

This template defines:
- All required document sections (Application Info, Architecture, Dataflow, Assumptions, Threats, Mitigations, Impacted Assets, Existing Controls, Residual Threats)
- Exact table formats with all required columns
- Threat statement structure requirements
- Cross-referencing rules with markdown anchor links
- Diagram requirements (architecture and dataflow ASCII diagrams)
- Evidence-based threat requirements with prefixes
- Quality validation checklist
- Template enforcement rules

**DO NOT deviate from the template format.** Follow the template at `docs/threat-model-template.md` exactly to ensure consistency and quality.

### Required Sections Quick Reference

The threat model MUST include these 10 sections in order:

1. **Application Info** (with disclaimers, summary, features, architecture references)
2. **Architecture** (with ASCII diagram, components, workflow)
3. **Dataflow** (with entities, flows, trust boundaries, ASCII diagram)
4. **Assumptions Table** (with cross-references to threats and mitigations)
5. **Threats Table** (with cross-references to mitigations and assumptions)
6. **Mitigations Table** (with cross-references to threats and assumptions)
7. **Impacted Assets Table** (with cross-references to related threats)
8. **Existing Controls Table** (with evidence, effectiveness, gaps)
9. **Residual Threats Table** (with recommended mitigations, priority, effort)
10. **AWS Well-Architected Mappings** (optional)

---

## Security Analysis Principles

### Objectivity and Thoroughness Requirements

All threat model analyses must maintain rigorous objectivity and avoid these problematic patterns:

### Red Flags to Avoid:

1. **Overly Defensive Tone**
   - Do NOT write like an advocate trying to minimize security concerns
   - DO maintain objective, analytical tone throughout
   - DO acknowledge legitimate security risks without downplaying them

2. **Scope Minimization**
   - Do NOT understate the system's actual capabilities or reach
   - Do NOT ignore indirect impacts (e.g., "system doesn't process data" while ignoring that it influences systems that DO process data)
   - DO consider the full scope of influence, including downstream effects
   - DO analyze what the system actually enables, not just what it directly does

3. **Risk Dismissal Patterns**
   - Do NOT systematically dismiss security concerns without thorough investigation
   - Do NOT use dismissive language without detailed justification
   - DO provide substantive analysis for why risks are or aren't applicable
   - DO explain the reasoning behind risk assessments

4. **Contradictory Evidence Gaps**
   - Do NOT mention security features without explaining why they're necessary
   - DO explain why security controls exist and what threats they address
   - DO ensure consistency between stated risk levels and implemented controls

5. **Responsibility Shifting**
   - Do NOT dismiss risks by claiming "other systems will handle security"
   - Do NOT ignore how your system influences or enables security risks in connected systems
   - DO analyze the security implications of your system's role in the broader ecosystem
   - DO consider how your system's outputs or behaviors affect downstream security

### Analysis Quality Indicators:

**High-Quality Analysis Includes:**
- Detailed investigation of each potential threat vector
- Clear explanation of why certain risks apply or don't apply
- Consideration of both direct and indirect security impacts
- Acknowledgment of limitations and areas requiring further review
- Consistent tone that prioritizes security over convenience
- Specific, actionable mitigations with measurable outcomes

**Warning Signs of Poor Analysis:**
- Repetitive justifications that sound like marketing copy
- Systematic dismissal of entire threat categories
- Vague statements about security without specific details
- Contradictions between stated risk levels and security measures
- Focus on what the system "doesn't do" rather than what it enables

---

## Threat Model Development Framework

### Phase 1: Information Gathering

#### Required Inputs

Comprehensive threat modeling requires analysis of:

1. **Project Documentation**
   - Business requirements and objectives
   - User stories and use cases
   - Compliance requirements
   - Service Level Agreements (SLAs)

2. **Architecture Documentation**
   - System architecture diagrams
   - Component descriptions
   - Technology stack details
   - Deployment architecture
   - Network topology

3. **API and Interface Specifications**
   - API endpoint definitions
   - Authentication/authorization mechanisms
   - Data formats and protocols
   - Integration points

4. **Data Architecture**
   - Data flow diagrams
   - Data classification
   - Storage locations
   - Data lifecycle

5. **Security Requirements**
   - Existing security controls
   - Compliance constraints
   - Security policies
   - Incident response procedures

### Phase 2: Document Structure Creation

#### 1. Document Header and Executive Summary

**Template:**

**NOTE**: The following sections are extracted from `docs/threat-model-template.md` and embedded here for immediate reference. For the complete template with all examples and detailed guidance, refer to the template file.

---

```markdown
# {Application Name} - Threat Model

This rule defines the EXACT format for generating AWS ProServe quality threat models following the ThreatComposer standard.

## CRITICAL FORMAT REQUIREMENTS

### 1. ALL Content MUST Be in TABLE Format
- NO paragraph sections
- NO "Key Security Concerns" sections  
- NO coverage percentages
- Use tables for ALL assumptions, threats, and mitigations

### 2. ID Format Requirements
- Assumptions: `A-0001`, `A-0002`, etc.
- Threats: `T-0001`, `T-0002`, etc.
- Mitigations: `M-0001`, `M-0002`, etc.
- ALL IDs must be cross-referenced with markdown links: `[**T-0001**](#T-0001)`

### 3. Threat Statement Structure
Every threat MUST follow this exact format:
```
A [threat actor] who [capability] can [action], which leads to [impact], resulting in [business impact]
```

**Good Example:**
```
A malicious user who has stolen valid credentials can bypass MFA by exploiting session token reuse, which leads to unauthorized access to betting workflows, resulting in fraudulent betting activity and financial loss
```

**Bad Example (too vague):**
```
An attacker can compromise the system and cause damage
```

**Key Elements:**
- **Threat Actor**: Be specific (malicious user, insider, external attacker, compromised account)
- **Capability**: What enables the attack (stolen credentials, network access, admin privileges)
- **Action**: Specific exploit or attack method (bypass MFA, inject SQL, intercept traffic)
- **Impact**: Technical consequence (unauthorized access, data breach, service disruption)
- **Business Impact**: Real-world consequence (financial loss, compliance violation, reputational damage)

## REQUIRED DOCUMENT STRUCTURE

### Section 1: Application Info

#### Disclaimers (REQUIRED)

_**1. Motivation for externalizing this threat model:**_

_This threat model for '{Application Name}' is informational only and provided "as is" with no representations or warranties whatsoever, and may change at any time due to a variety of factors, such as changes to AWS's services. The provision of this threat model does not create any warranties, representations, contractual commitments, conditions or assurances from AWS, its affiliates, suppliers or licensors. This threat model is a comprehensive security analysis and is not suitable for every possible interaction or use case. It aims to provide a detailed assessment of threats, assumptions and mitigations specific to this application. You may have different perspectives on the assumptions, threats, mitigations and prioritization based on your organization's risk appetite. You may want to use this threat model as the base or starting point to generate a contextualized threat model for your own specific needs and deployment. This threat model uses the actual system architecture and is tailored to the specific implementation. You are solely responsible for making your own independent assessment of this threat model and its applicability to your organization._

_**2. Criteria for prioritizing threats**_

_In this threat model, threats are prioritized based on their potential impact to confidentiality, integrity, and availability (CIA triad) of the system and data. The prioritization considers the specific business context, regulatory requirements, and operational constraints of the application. Please note, these priorities are based on the current system architecture and threat landscape. Organizations should calculate priority using their own factors as part of any internal risk frameworks._

_**3. Agreement**_

_All use of AWS's services will be governed by the AWS Customer Agreement available at http://aws.amazon.com/agreement/ (or other definitive written agreement as may be agreed between the parties governing the use of AWS's services). If you use any artificial intelligence and machine learning Services, features, and functionality (including third-party models) that we provide, you will comply with the AWS Responsible AI Policy._

#### Summary
- Brief description of the application and its purpose
- Key business context and use cases

#### Key Features
- Bullet list of main features and capabilities
- Integration points with other systems

#### Architecture and Documentation References
- Links to architecture diagrams
- References to related documentation
- Source code repositories (if applicable)
- Related AWS service documentation

### Section 2: Architecture
**CRITICAL**: Architecture section MUST include comprehensive component analysis and visual diagrams

#### Introduction
Brief overview of the system architecture and its purpose

#### Key Benefits
- **Benefit 1**: Description of key architectural advantage
- **Benefit 2**: Description of scalability or performance benefit
- **Benefit 3**: Description of security or reliability benefit
- **Benefit 4**: Description of operational benefit

#### Architecture Components
Detailed breakdown of components by layer:

**Layer 1: [Layer Name]** (e.g., Frontend Layer, API Layer)
- Component 1: Description and responsibilities
- Component 2: Description and responsibilities

**Layer 2: [Layer Name]** (e.g., Application Layer, Processing Layer)
- Component 3: Description and responsibilities
- Component 4: Description and responsibilities

**Layer 3: [Layer Name]** (e.g., Data Layer, Storage Layer)
- Component 5: Description and responsibilities
- Component 6: Description and responsibilities

#### Workflow
Numbered steps showing how the system processes requests:
1. **Step 1**: User initiates action (e.g., submits request via web interface)
2. **Step 2**: Frontend validates and forwards request
3. **Step 3**: API Gateway authenticates and routes request
4. **Step 4**: Backend processes request and queries data
5. **Step 5**: Response is formatted and returned to user

#### Architecture Diagram
**IMPORTANT**: Create a comprehensive diagram showing:
- All major components organized by layer
- Component relationships and interactions
- Security boundaries and controls
- Data flow directions
- External integrations

**Example Structure** (customize for your architecture):
```
┌─────────────────────────────────────────────────────────────────┐
│                    [System Name] Architecture                    │
├─────────────────────────────────────────────────────────────────┤
│  Frontend Layer                                                 │
│  ┌─────────────────────┐    ┌──────────────────────────────────┐│
│  │ Web Application     │    │ Mobile App                       ││
│  │ - React/Angular     │    │ - iOS/Android                    ││
│  │ - User Interface    │    │ - Native UI                      ││
│  └─────────────────────┘    └──────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────┤
│  API & Integration Layer                                        │
│  ┌─────────────────────┐    ┌──────────────────────────────────┐│
│  │ API Gateway         │    │ Authentication                   ││
│  │ - REST/GraphQL      │    │ - Cognito/OAuth                  ││
│  │ - Rate Limiting     │    │ - JWT Tokens                     ││
│  └─────────────────────┘    └──────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────┤
│  Application Layer                                              │
│  ┌─────────────────────┐    ┌──────────────────────────────────┐│
│  │ Lambda Functions    │    │ Business Logic                   ││
│  │ - Serverless        │    │ - Processing                     ││
│  │ - Event-driven      │    │ - Orchestration                  ││
│  └─────────────────────┘    └──────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────┤
│  Data Layer                                                     │
│  ┌─────────────────────┐    ┌──────────────────────────────────┐│
│  │ DynamoDB            │    │ S3 Storage                       ││
│  │ - NoSQL Database    │    │ - Object Storage                 ││
│  │ - Encrypted         │    │ - Versioning                     ││
│  └─────────────────────┘    └──────────────────────────────────┘│
├─────────────────────────────────────────────────────────────────┤
│  Security & Monitoring                                          │
│  ┌─────────────────────┐    ┌──────────────────────────────────┐│
│  │ CloudWatch          │    │ AWS WAF                          ││
│  │ - Logs & Metrics    │    │ - Web Firewall                   ││
│  │ - Alarms            │    │ - DDoS Protection                ││
│  └─────────────────────┘    └──────────────────────────────────┘│
└─────────────────────────────────────────────────────────────────┘
```

**Architecture Diagram Requirements**:
- Use ASCII art with box-drawing characters
- Organize components by logical layers
- Show component relationships clearly
- Include security and monitoring components
- Use consistent formatting and alignment
- Label each layer clearly
- Show key features/technologies for each component

### Section 3: Dataflow
**CRITICAL**: Dataflow section MUST include comprehensive analysis with visual diagrams

#### Introduction
Brief overview of how data flows through the system and key processes

#### Entities Table
| Entity | Description |
|-|-|
| User | The individual who interacts with the system |
| Web App | The frontend interface for input and output |
| API Gateway | Orchestrates API requests and responses |
| Lambda | Serverless functions interacting with services |
| DynamoDB | Stores application data |

#### Data Flows Definition Table
| Flow Identifier | Flow Description | Source Entity | Target Entity | Assets |
|-|-|-|-|-|
| DF1 | User submits request | User | Web App | User supplied data |
| DF2 | Query is authenticated | Web App | API Gateway | Credentials + Auth tokens |
| DF3 | API request handled | API Gateway | Lambda | User data, Auth tokens |
| DF4 | Data stored | Lambda | DynamoDB | Application data |

#### Trust Boundaries Table
| Boundary Identifier | Purpose | Source Entity | Target Entity |
|-|-|-|-|
| TB1 | Validates input, ensures privacy | User | Web App |
| TB2 | Allows authorized backend access | Web App | API Gateway |
| TB3 | Triggers Lambda securely | API Gateway | Lambda |
| TB4 | Allows secure data storage | Lambda | DynamoDB |

#### Possible Threat Sources Table
| Category | Description | Examples |
|-|-|-|
| Legitimate Users | Valid users who unintentionally trigger issues | An internal actor, An end user |
| Malicious Internal Actors | Trusted insiders who intentionally cause harm | An overprivileged admin, An internal developer |
| External Threat Actors | External attackers targeting the system | A threat actor, An external threat actor |
| Untrusted Data Suppliers | External data sources that provide bad data | A third-party data supplier |
| Unauthorized External Users | External entities with no system access | A malicious user (no system access) |

#### Dataflow Diagram
**IMPORTANT**: Create a comprehensive diagram showing:
- All entities and components
- Data flow arrows with labels (DF1, DF2, etc.)
- Trust boundaries marked with `╔═══╗` borders
- Clear visual hierarchy and relationships

**Example Structure** (customize for your architecture):
```
                    ┌─────────────────────┐
                    │   External Users    │
                    └──────────┬──────────┘
                               │
    ╔══════════════════════════╧═══════════════════════════╗
    ║              [TB1] Trust Boundary                    ║
    ║         (Internet → Application Frontend)            ║
    ╚══════════════════════════╤═══════════════════════════╝
                               │
                    ┌──────────▼──────────┐
                    │   Frontend (Web)    │
                    └──────────┬──────────┘
                               │ DF1
    ╔══════════════════════════╧═══════════════════════════╗
    ║              [TB2] Trust Boundary                    ║
    ║         (Frontend → API Gateway)                     ║
    ╚══════════════════════════╤═══════════════════════════╝
                               │
                    ┌──────────▼──────────┐
                    │   API Gateway       │
                    └──────────┬──────────┘
                               │ DF2
    ╔══════════════════════════╧═══════════════════════════╗
    ║              [TB3] Trust Boundary                    ║
    ║         (API Gateway → Lambda)                       ║
    ╚══════════════════════════╤═══════════════════════════╝
                               │
                    ┌──────────▼──────────┐
                    │   Lambda Functions  │
                    └──────────┬──────────┘
                               │ DF3
                    ┌──────────▼──────────┐
                    │   DynamoDB Tables   │
                    └─────────────────────┘
```

**Dataflow Diagram Requirements**:
- Use ASCII art with box-drawing characters
- Label all data flows (DF1, DF2, DF3, etc.)
- Mark trust boundaries with double-line borders
- Show directionality with arrows (▼, ►, ◄, ▲)
- Include all major components from architecture
- Align components vertically by layer/tier
- Use consistent spacing and formatting

### Section 4: Assumptions Table
**CRITICAL**: Assumptions table MUST include cross-references to related threats and mitigations

| Assumption Number | Assumption | Linked Threats | Linked Mitigations | Comments |
|-------------------|------------|----------------|-------------------|----------|
| [**A-0001**](#A-0001) | Users authenticate via AWS Cognito | [**T-0001**](#T-0001): Credential theft threat<br/>[**T-0002**](#T-0002): Session hijacking threat | [**M-0001**](#M-0001): MFA implementation<br/>[**M-0002**](#M-0002): Session timeout controls | Application uses Cognito User Pool for authentication |
| [**A-0002**](#A-0002) | All data at rest is encrypted | [**T-0003**](#T-0003): Data breach threat | [**M-0003**](#M-0003): S3 bucket encryption | S3 buckets have default encryption enabled |

**Column Requirements**:
- **Assumption Number**: Unique ID with anchor tag (A-0001, A-0002, etc.)
- **Assumption**: Clear statement of what is assumed about the system
- **Linked Threats**: ALL threats that depend on this assumption, with full threat statements using `<br/>` separator
- **Linked Mitigations**: ALL mitigations that address risks related to this assumption, using `<br/>` separator
- **Comments**: Additional context, rationale, or HTML formatted explanations using `<p>` tags

### Section 5: Threats Table
**CRITICAL**: Threats table MUST include cross-references to mitigations and assumptions

| Threat Number | Threat | Mitigations | Assumptions | Status | Priority | STRIDE | Comments |
|---------------|--------|-------------|-------------|--------|----------|--------|----------|
| [**T-0001**](#T-0001) | A malicious user who has valid credentials can access unauthorized data by exploiting insufficient access controls, which leads to data breach, resulting in compliance violations | [**M-0001**](#M-0001): Implement least privilege IAM policies<br/>[**M-0002**](#M-0002): Enable MFA for all users | [**A-0001**](#A-0001): Users authenticate via AWS Cognito | Identified | High | S | AWS Well-Architected Framework mapping: SEC-02 |
| [**T-0002**](#T-0002) | An attacker who intercepts network traffic can steal sensitive data by exploiting unencrypted connections, which leads to data exposure, resulting in financial loss | [**M-0003**](#M-0003): Enable TLS 1.2+ for all connections | [**A-0002**](#A-0002): All data at rest is encrypted | Identified | High | T | AWS Well-Architected Framework mapping: SEC-08 |

**Column Requirements**:
- **Threat Number**: Unique ID with anchor tag (T-0001, T-0002, etc.)
- **Threat**: Full threat statement following the required format
- **Mitigations**: ALL mitigations that address this threat, using `<br/>` separator
- **Assumptions**: Related assumptions that this threat depends on, using `<br/>` separator
- **Status**: Typically "Identified" for all threats
- **Priority**: Critical, High, Medium, or Low
- **STRIDE**: One or more STRIDE categories (S, T, R, I, D, E)
- **Comments**: Optional HTML formatted comments using `<p>` tags, AWS Well-Architected mappings, or additional context

### Section 6: Mitigations Table
**CRITICAL**: Mitigations table MUST include cross-references to threats and assumptions

| Mitigation Number | Mitigation | Threats Mitigating | Assumptions | Status | Comments |
|-------------------|------------|-------------------|-------------|--------|----------|
| [**M-0001**](#M-0001) | Implement least privilege IAM policies | [**T-0001**](#T-0001): A malicious user who has valid credentials can access unauthorized data by exploiting insufficient access controls, which leads to data breach, resulting in compliance violations | [**A-0001**](#A-0001): Users authenticate via AWS Cognito | Identified | Use IAM roles with minimal permissions. AWS Well-Architected: SEC-02 |
| [**M-0002**](#M-0002) | Enable TLS 1.2+ for all connections | [**T-0002**](#T-0002): An attacker who intercepts network traffic can steal sensitive data by exploiting unencrypted connections, which leads to data exposure, resulting in financial loss | [**A-0002**](#A-0002): All data at rest is encrypted | Identified | Configure ALB with TLS 1.2 minimum. AWS Well-Architected: SEC-08 |

**Column Requirements**:
- **Mitigation Number**: Unique ID with anchor tag (M-0001, M-0002, etc.)
- **Mitigation**: Clear, concise mitigation description
- **Threats Mitigating**: ALL threats this mitigation addresses, with full threat statements using `<br/>` separator
- **Assumptions**: Related assumptions, using `<br/>` separator (can be empty if no assumptions)
- **Status**: Typically "Identified" for all mitigations
- **Comments**: HTML formatted implementation details using `<p>` tags, AWS Well-Architected mappings, links to documentation

### Section 7: Impacted Assets Table
**CRITICAL**: This section MUST use table format with asset IDs and threat cross-references

| Asset Number | Asset | Related Threats |
|--------------|-------|-----------------|
| [**AS-0001**](#AS-0001) | User credentials and authentication tokens | [**T-0001**](#T-0001): Credential theft threat<br/>[**T-0002**](#T-0002): Session hijacking threat |
| [**AS-0002**](#AS-0002) | Customer PII and sensitive data | [**T-0003**](#T-0003): Data breach threat<br/>[**T-0007**](#T-0007): PII exposure threat |

**Asset Categorization Guidelines**:
- **Critical Assets**: Data/systems whose compromise would cause severe business impact
- **High-Value Assets**: Important resources with significant but not catastrophic impact
- **Supporting Assets**: Infrastructure and operational resources

**Each asset entry must**:
- Have unique ID (AS-0001, AS-0002, etc.)
- Include clear asset description
- List ALL related threats with full threat statements (not just IDs)
- Use `<br/>` for multiple threats in same cell

### Section 8: Existing Controls Table
**CRITICAL**: This section MUST document security controls already implemented in the system with evidence

| Control Number | Control Name | Control Type | Implementation Evidence | Threats Addressed | Effectiveness | Gaps/Weaknesses | Comments |
|----------------|--------------|--------------|-------------------------|-------------------|---------------|-----------------|----------|
| [**EC-0001**](#EC-0001) | AWS Cognito User Pool Authentication | Preventive | **Found in repo**: `infra/cognito-stack.ts` line 23 - Cognito User Pool configured with password policy<br/>**Found in repo**: `src/auth/cognito-auth.ts` line 45 - JWT token validation implemented | [**T-0001**](#T-0001): Credential theft threat<br/>[**T-0002**](#T-0002): Session hijacking threat | Partial | MFA is OPTIONAL, not enforced for all users. Session timeout set to 24 hours (too long) | <p>AWS Well-Architected: SEC-02</p><p>Recommendation: Enforce MFA for all users and reduce session timeout to 1 hour</p> |
| [**EC-0002**](#EC-0002) | S3 Bucket Encryption at Rest | Preventive | **Found in repo**: `infra/storage-stack.ts` line 67 - S3 buckets have AES-256 encryption enabled by default | [**T-0003**](#T-0003): Data breach threat | Effective | No customer-managed KMS keys, using AWS-managed keys only | <p>AWS Well-Architected: SEC-08</p><p>Consider using customer-managed KMS keys for sensitive data</p> |
| [**EC-0003**](#EC-0003) | CloudWatch Logging | Detective | **Found in repo**: `infra/monitoring-stack.ts` line 89 - CloudWatch Logs enabled for Lambda functions and API Gateway | [**T-0004**](#T-0004): Repudiation threat | Partial | Log retention set to 7 days only. No log integrity validation | <p>AWS Well-Architected: SEC-04</p><p>Increase retention to 90 days minimum and enable CloudWatch Logs Insights</p> |

**Column Requirements**:
- **Control Number**: Unique ID with anchor tag (EC-0001, EC-0002, etc.)
- **Control Name**: Clear, descriptive name of the security control
- **Control Type**: Preventive, Detective, or Corrective
- **Implementation Evidence**: Specific evidence from repository, container, architecture, or diagram with file paths and line numbers
- **Threats Addressed**: ALL threats this control mitigates, with full threat statements using `<br/>` separator
- **Effectiveness**: Effective, Partial, or Ineffective (with brief explanation)
- **Gaps/Weaknesses**: Specific limitations or weaknesses in current implementation
- **Comments**: HTML formatted recommendations using `<p>` tags, AWS Well-Architected mappings, implementation improvements

**Control Type Definitions**:
- **Preventive**: Controls that prevent security incidents (e.g., IAM policies, encryption, MFA)
- **Detective**: Controls that detect security incidents (e.g., CloudWatch alarms, GuardDuty, CloudTrail)
- **Corrective**: Controls that correct security incidents (e.g., automated remediation, incident response)

**Effectiveness Levels**:
- **Effective**: Control fully addresses the threat with no significant gaps
- **Partial**: Control addresses the threat but has limitations or gaps
- **Ineffective**: Control does not adequately address the threat

**Evidence Requirements**:
- MUST include specific file paths, line numbers, or configuration details
- MUST use evidence prefixes: "**Found in repo**:", "**Found in image**:", "**Found in architecture**:", "**Found in diagram**:"
- MUST reference actual component names and configurations
- MUST quantify effectiveness where possible (e.g., "covers 80% of API endpoints")

### Section 9: Residual Threats and Recommended Mitigations Table

**PURPOSE**: This section translates the gaps identified in Existing Controls (Section 8) into an actionable remediation roadmap. While the Existing Controls table shows "what's wrong," this table shows "what to do about it" with priorities, effort estimates, and validation steps.

**CRITICAL MAPPING REQUIREMENT**: Each Residual Threat MUST correspond to an Existing Control marked as "Partial" or "Ineffective". 

**Important Notes**:
- If one Existing Control has multiple gaps affecting different threats, create separate RT entries for each gap
- Example: EC-0005 (CloudWatch Logs) addresses both T-0006 (log retention) and T-0008 (log sanitization) with "Partial" effectiveness → Create RT-0005 for T-0006 gap AND RT-0007 for T-0008 gap
- **Validation**: Count your "Partial" and "Ineffective" ECs, then verify you have at least that many RT entries (may be more if ECs address multiple threats)

**Target Audiences**:
- **Implementation Teams**: Detailed steps for remediation
- **Project Managers**: Effort estimates and priorities for planning
- **Executives**: Risk reduction ROI and business justification
- **Compliance Teams**: Remediation roadmap for audit findings

| Residual Threat Number | Residual Threat | Current Control Gaps | Recommended Mitigation | Priority | Implementation Effort | AWS Services Required | Expected Risk Reduction | Comments |
|-------------------------|-----------------|----------------------|------------------------|----------|----------------------|----------------------|-------------------------|----------|
| [**RT-0001**](#RT-0001) | A malicious user who has valid credentials can access unauthorized data by exploiting insufficient access controls, which leads to data breach, resulting in compliance violations | [**EC-0001**](#EC-0001): MFA is optional, not enforced<br/>[**EC-0002**](#EC-0002): No fine-grained access controls on S3 buckets | [**M-0001**](#M-0001): Enforce MFA for all users<br/>[**M-0004**](#M-0004): Implement S3 bucket policies with least privilege access | Critical | Medium (2-3 weeks) | AWS Cognito (MFA enforcement)<br/>AWS IAM (S3 bucket policies)<br/>AWS CloudTrail (audit logging) | High (reduces risk from High to Low) | <p>AWS Well-Architected: SEC-02, SEC-03</p><p>Implementation: Update Cognito User Pool to require MFA, create S3 bucket policies with explicit deny for unauthorized access patterns</p><p>Validation: Test with non-MFA users (should be blocked), verify S3 access with different IAM roles</p> |
| [**RT-0002**](#RT-0002) | An attacker who intercepts network traffic can steal sensitive data by exploiting unencrypted connections, which leads to data exposure, resulting in financial loss | No existing control for TLS enforcement on ALB | [**M-0005**](#M-0005): Configure ALB to enforce TLS 1.2+ and redirect HTTP to HTTPS<br/>[**M-0006**](#M-0006): Enable AWS Certificate Manager for SSL/TLS certificates | High | Low (1 week) | AWS ALB (TLS configuration)<br/>AWS Certificate Manager (SSL certificates)<br/>AWS WAF (additional protection) | High (reduces risk from High to Low) | <p>AWS Well-Architected: SEC-08</p><p>Implementation: Update ALB listener rules to enforce HTTPS, configure security policy to TLS 1.2 minimum</p><p>Validation: Test HTTP connections (should redirect to HTTPS), verify TLS version with SSL Labs scan</p> |
| [**RT-0003**](#RT-0003) | A malicious actor who gains access to CloudWatch Logs can tamper with audit logs by exploiting lack of log integrity validation, which leads to evidence destruction, resulting in inability to investigate security incidents | [**EC-0003**](#EC-0003): No log integrity validation, short retention period | [**M-0007**](#M-0007): Enable CloudWatch Logs encryption with KMS<br/>[**M-0008**](#M-0008): Implement log file integrity validation using CloudWatch Logs Insights<br/>[**M-0009**](#M-0009): Increase log retention to 90 days minimum | Medium | Medium (2 weeks) | AWS CloudWatch Logs (encryption, retention)<br/>AWS KMS (log encryption keys)<br/>AWS Lambda (integrity validation) | Medium (reduces risk from Medium to Low) | <p>AWS Well-Architected: SEC-04, SEC-07</p><p>Implementation: Create KMS key for log encryption, update log groups with encryption and retention settings, create Lambda function for periodic integrity checks</p><p>Validation: Verify logs are encrypted, test integrity validation with tampered logs</p> |

**Column Requirements**:
- **Residual Threat Number**: Unique ID with anchor tag (RT-0001, RT-0002, etc.)
- **Residual Threat**: Full threat statement following the required format (threat actor, capability, action, impact, business impact)
- **Current Control Gaps**: Reference to existing controls (EC-XXXX) that are insufficient, with specific gaps identified
- **Recommended Mitigation**: Reference to mitigations (M-XXXX) that address the residual threat, using `<br/>` separator for multiple mitigations
- **Priority**: Critical, High, Medium, or Low (based on risk level after existing controls)
- **Implementation Effort**: Low (< 1 week), Medium (1-3 weeks), High (> 3 weeks)
- **AWS Services Required**: Specific AWS services needed for implementation
- **Expected Risk Reduction**: Quantified risk reduction (e.g., "High to Low", "Critical to Medium")
- **Comments**: HTML formatted implementation guidance using `<p>` tags, including:
  - AWS Well-Architected Framework mappings
  - Detailed implementation steps
  - Validation criteria and test cases
  - Links to AWS documentation

**Priority Definitions**:
- **Critical**: Residual threat could cause severe business impact, immediate action required
- **High**: Residual threat could cause significant impact, action required within 1 month
- **Medium**: Residual threat could cause moderate impact, action required within 3 months
- **Low**: Residual threat has minimal impact, action required within 6 months

**Implementation Effort Guidelines**:
- **Low**: Simple configuration changes, no code changes required
- **Medium**: Moderate code changes, testing required
- **High**: Significant architectural changes, extensive testing and validation required

**Risk Reduction Calculation**:
- Consider both likelihood and impact reduction
- Quantify expected risk level after mitigation implementation
- Use format: "[Current Risk Level] to [Expected Risk Level]" (e.g., "High to Low")

### Section 10: AWS Well-Architected Framework Mappings (Optional)
Map each mitigation to relevant AWS Well-Architected pillars:
- SEC-01 through SEC-11: Security pillar
- REL-01 through REL-13: Reliability pillar
- PERF-01 through PERF-05: Performance pillar
- COST-01 through COST-10: Cost optimization pillar
- OPS-01 through OPS-11: Operational excellence pillar

## STRIDE CATEGORIES
Use these exact categories for threat classification:
- **Spoofing**: Impersonating something or someone else
- **Tampering**: Modifying data or code
- **Repudiation**: Claiming to have not performed an action
- **Information Disclosure**: Exposing information to unauthorized parties
- **Denial of Service**: Denying or degrading service
- **Elevation of Privilege**: Gaining capabilities without authorization

## IMPACT LEVELS
- **Critical**: Complete system compromise, large-scale data breach, major regulatory violation, significant financial loss, complete service outage
- **High**: Significant data loss affecting multiple users, service disruption (>1 hour), moderate financial impact, compliance violations
- **Medium**: Limited data exposure affecting few users, degraded performance, minor financial impact, temporary service issues
- **Low**: Minor inconvenience, minimal impact, no data exposure, negligible financial impact

## LIKELIHOOD LEVELS
- **High**: Easy to exploit, common attack vector
- **Medium**: Requires some skill or specific conditions
- **Low**: Difficult to exploit, requires significant resources

## QUALITY VALIDATION CHECKLIST

### Format Compliance
- [ ] All content in table format (no paragraphs for assumptions/threats/mitigations)
- [ ] No "Key Security Concerns" sections
- [ ] No coverage percentages
- [ ] Proper ID cross-referencing with markdown anchor links
- [ ] All cross-references include full threat statements (not just IDs)
- [ ] HTML formatting used in Comments columns (`<p>` tags, `<br/>` separators)

### Evidence-Based Requirements
- [ ] ALL threat descriptions start with appropriate evidence prefix:
  - Repository: "**Found in repo**:"
  - Container: "**Found in image**:"
  - Architecture Doc: "**Found in architecture**:"
  - Diagram: "**Found in diagram**:"
- [ ] Specific file paths or section references included
- [ ] Actual component names used (not generic terms)
- [ ] Impact quantified with real numbers
- [ ] No generic threats without evidence

### Threat Quality
- [ ] Structured threat statements following required format
- [ ] STRIDE categories correctly applied
- [ ] Impact and likelihood levels assigned
- [ ] All AWS services identified with actual names
- [ ] Attack scenarios include specific steps
- [ ] Affected assets listed with IDs

### Cross-Reference Integrity
- [ ] Assumptions table links to threats and mitigations
- [ ] Threats table links to mitigations and assumptions
- [ ] Mitigations table links to threats and assumptions
- [ ] Impacted Assets table links to all related threats
- [ ] All links use markdown anchor format: `[**T-0001**](#T-0001)`

### Diagram Requirements
- [ ] Architecture diagram included
- [ ] Dataflow diagram included
- [ ] All components labeled clearly
- [ ] Trust boundaries marked visually
- [ ] Data flows labeled (DF1, DF2, etc.)
- [ ] Consistent formatting and alignment

### AWS Well-Architected Mappings
- [ ] Mitigations mapped to relevant pillars
- [ ] Security pillar (SEC-XX) references included
- [ ] Implementation details provided
- [ ] Validation steps documented

### Completeness Check
- [ ] All required sections present
- [ ] Disclaimers included (if applicable)
- [ ] Summary and features documented
- [ ] Architecture components detailed
- [ ] Workflow steps numbered
- [ ] All tables properly formatted
- [ ] Existing Controls table with evidence from repo/image/architecture
- [ ] Residual Threats table with implementation guidance
- [ ] **CRITICAL**: Residual Threats count matches Partial/Ineffective Existing Controls count
- [ ] Every EC marked "Partial" has corresponding RT entry
- [ ] Both .md and .tc.json formats generated

## TEMPLATE ENFORCEMENT

**CRITICAL RULES - VIOLATIONS WILL CAUSE REJECTION**:

1. **NO Generic Threats**: Every threat MUST have evidence from actual analysis
2. **NO Missing Prefixes**: Every threat description MUST start with evidence prefix
3. **NO Incomplete Cross-References**: All cross-references MUST include full threat statements
4. **NO Paragraph Sections**: Assumptions, threats, and mitigations MUST be in tables
5. **NO Missing Diagrams**: Architecture and dataflow diagrams are MANDATORY
6. **NO Generic Component Names**: Use actual names from architecture (e.g., "chat-orchestrator Lambda" not "Lambda function")
7. **NO Unquantified Impact**: Every threat MUST include specific numbers or percentages
8. **NO Missing Table Columns**: All required columns MUST be present in every table

**Before submitting, run this final check**:
```
SEARCH FOR: "Lambda function", "DynamoDB table", "S3 bucket" (generic terms)
IF FOUND: Replace with actual component names

SEARCH FOR: Threats without "Found in repo/image/architecture/diagram"
IF FOUND: Add specific evidence

SEARCH FOR: Cross-references with only IDs (e.g., "[**T-0001**](#T-0001)" without threat statement)
IF FOUND: Add full threat statement after the link

SEARCH FOR: Paragraph sections in Assumptions/Threats/Mitigations
IF FOUND: Convert to table format

SEARCH FOR: Missing diagrams
IF FOUND: Generate ASCII diagrams for architecture and dataflow
```

## OUTPUT FORMAT

**IMPORTANT**: The threat model will be generated in markdown format following this template. After generation, use the MCP tool `generate_professional_reports` to create all required formats:

1. **Markdown (.md)**: Primary threat model document for review and documentation
2. **Word Document (.docx)**: Professional report with AWS ProServe styling and branding
3. **Interactive HTML**: Web-based report with AWS color styling, dark/light mode toggle
4. **PDF**: Printable format generated from HTML
5. **JSON (.tc.json)**: ThreatComposer format for importing into AWS ThreatComposer tool

The JSON format must follow the ThreatComposer schema with these key sections:
- `schema`: Version number (1)
- `applicationInfo`: Name and description (includes disclaimers, summary, features)
- `architecture`: Architecture diagram (base64 encoded image if available)
- `dataflow`: Dataflow diagram (base64 encoded image if available)
- `assumptions`: Array of assumption objects with id, content, linkedThreats, linkedMitigations, comments
- `threats`: Array of threat objects with id, statement, mitigations, assumptions, status, priority, stride, comments
- `mitigations`: Array of mitigation objects with id, content, threats, assumptions, status, comments
- `impactedAssets`: Array of asset objects with id, name, relatedThreats

## AI/ML SPECIFIC THREATS
When analyzing AI/ML systems, include these threat categories:

**Prompt Injection & Manipulation**:
- Direct prompt injection through user inputs
- Indirect prompt injection through data sources
- Jailbreaking attempts to bypass safety controls
- System prompt leakage

**Model Integrity**:
- Training data poisoning
- Model weight tampering
- Adversarial inputs to cause misclassification
- Model stealing through API abuse

**Data Privacy**:
- Training data memorization and leakage
- PII exposure through model responses
- Inference attacks to extract training data
- Model inversion attacks

**Operational Risks**:
- Cost exhaustion through expensive operations
- Model hallucinations leading to incorrect outputs
- Bias and fairness issues
- Model performance degradation

## EVIDENCE-BASED THREAT REQUIREMENTS

**CRITICAL**: ALL threat descriptions MUST be evidence-based and start with appropriate prefix based on analysis source:

### Analysis Source Types

**Repository Analysis** (Full Code Access):
- Prefix: `**Found in repo**:`
- Include: File paths, line numbers, actual configuration values
- Example: `**Found in repo**: Agent application (src/agent_app.py line 45) uses Cognito JWT authentication without MFA enforcement. Analysis of infra/cognito-stack.ts (line 23) shows MFA is set to OPTIONAL.`

**Container Image Analysis** (Docker/Container):
- Prefix: `**Found in image**:`
- Include: Dockerfile lines, CVE numbers, package versions
- Example: `**Found in image**: Container (Dockerfile line 12) runs as root user without USER directive. Image scan reveals 23 HIGH and 5 CRITICAL CVEs in base image python:3.9.`

**Architecture Document Analysis** (Documentation Only):
- Prefix: `**Found in architecture**:`
- Include: Section references, component names, design gaps
- Example: `**Found in architecture**: API Gateway (Section 2.3) configured without WAF protection. Architecture shows direct internet exposure with no rate limiting mentioned.`

**Architecture Diagram Image Analysis** (PNG/JPEG):
- Prefix: `**Found in diagram**:`
- Include: Spatial locations, visible components, missing elements
- Example: `**Found in diagram**: API Gateway (top-left) shows direct internet connection without WAF. Diagram depicts 5 Lambda functions with no authentication layer visible.`

### Mandatory Evidence Requirements

**Every threat description MUST include**:
1. Appropriate evidence prefix based on analysis source
2. Specific component names (not generic terms)
3. Actual file paths, section references, or diagram locations
4. Quantified impact (numbers, percentages, time windows)
5. Configuration details or missing controls

**Validation Checklist**:
- [ ] Description starts with evidence prefix
- [ ] Specific file paths or section references included
- [ ] Actual component names used (not "Lambda function" but "chat-orchestrator Lambda")
- [ ] Impact quantified with numbers
- [ ] No generic security advice without evidence

## GENERATION WORKFLOW

1. **Determine Analysis Source Type**:
   - Repository with code → Use "Found in repo" format
   - Container image → Use "Found in image" format
   - Architecture document → Use "Found in architecture" format
   - Diagram image → Use "Found in diagram" format

2. **Analyze Architecture**: 
   - Identify AWS services, data flows, trust boundaries
   - Extract actual component names and configurations
   - Document file paths or section references
   - Count resources and quantify scope

3. **Identify Assets**: 
   - Catalog sensitive data, credentials, models
   - Classify by criticality (Critical/High/Medium/Low)
   - Map to specific components and data stores

4. **Generate Assumptions** (A-0001 format): 
   - Document security assumptions with evidence
   - Link to related threats and mitigations
   - Include rationale in Comments column

5. **Create Dataflow Analysis**: 
   - Map entities with descriptions
   - Define data flows with source/target/assets
   - Identify trust boundaries
   - Categorize threat sources
   - Create comprehensive ASCII dataflow diagram

6. **Generate Architecture Diagrams**:
   - Create layered ASCII architecture diagram
   - Show all major components by layer
   - Include security and monitoring components
   - Label relationships and data flows

7. **Generate Threats** (T-0001 format): 
   - Start EVERY description with evidence prefix
   - Use structured threat statement format
   - Include specific file paths or references
   - Quantify impact with actual numbers
   - Map to mitigations and assumptions
   - Focus on high-impact, high-likelihood threats first
   - Include AI/ML specific threats for LLM systems

8. **Generate Mitigations** (M-0001 format): 
   - Provide specific, actionable mitigations
   - Include full threat statements in cross-references
   - Add implementation details in Comments
   - Map to AWS Well-Architected Framework
   - Use HTML formatting for detailed explanations

9. **Generate Impacted Assets** (AS-0001 format):
   - List all critical and high-value assets
   - Include full threat statements for each asset
   - Use `<br/>` separator for multiple threats
   - Categorize by business impact

10. **Generate Existing Controls** (EC-0001 format):
    - Identify security controls already implemented in the system
    - Provide specific evidence with file paths and line numbers
    - Assess effectiveness (Effective, Partial, Ineffective)
    - Document gaps and weaknesses in current implementation
    - Map to threats addressed by each control
    - Include AWS Well-Architected Framework mappings

11. **Generate Residual Threats** (RT-0001 format):
    - **CRITICAL**: Create RT entry for EVERY Existing Control with "Partial" or "Ineffective" effectiveness
    - Count your Existing Controls: If you have 4 EC entries marked "Partial", you MUST have at least 4 RT entries
    - Identify threats not adequately addressed by existing controls
    - Reference control gaps from Existing Controls table
    - Provide recommended mitigations with implementation steps
    - Include priority, effort, and expected risk reduction
    - Add detailed validation criteria and test cases
    - Map to AWS services required for implementation
    - **VALIDATION**: Before finishing, verify RT count matches Partial/Ineffective EC count

12. **Cross-reference IDs**: 
    - Ensure all IDs use markdown anchor links
    - Verify bidirectional references (threats ↔ mitigations ↔ assumptions)
    - Include full threat statements in cross-references

11. **Validate Quality**: 
    - Check against quality checklist
    - Verify all evidence prefixes present
    - Confirm no generic threats without evidence
    - Validate table formatting and cross-references

```

---

## Best Practices

### Do's
- **Use specific, measurable language** with quantified metrics (e.g., "51% coverage", "10,000 req/sec")
- **Provide detailed attack scenarios** with numbered steps
- **Include realistic impact assessments** with no dollar amounts
- **Consider both technical and business impacts** in every threat
- **Document assumptions clearly** with rationale
- **Update regularly** as system evolves (quarterly minimum)
- **Quantify current security posture** using the Existing Controls Mapping section
- **Use visual indicators** (✅ ⚠️ ❌) for quick scanning
- **Include actual configuration values** from architecture documentation
- **Calculate coverage percentages** for all threat categories

### Don'ts
- Don't use vague or generic descriptions
- Don't dismiss threats without thorough analysis
- Don't ignore indirect or downstream impacts
- Don't over-rely on single controls
- **Don't skip the Existing Controls Mapping section** - it's critical for stakeholders
- **Don't assume controls are implemented** - verify with architecture docs
- **Don't use qualitative assessments only** - quantify everything possible
- **Don't forget to map existing controls to threats** - show what's protecting what
- **Don't include cost estimates or specific timelines** - leave for customer to determine
- **Don't include insider threat controls** - focus on technical security controls
- **Don't include social engineering/phishing controls** - handled by awareness programs
- **Don't include third-party vendor risk controls** - handled by vendor management

### Critical Success Factors

**For Threat Models to be Actionable**:
1. **Quantified Current State**: Must show current coverage percentages (e.g., "51% overall coverage")
2. **Clear Gap Analysis**: Each threat must show what controls exist vs. what's missing
3. **Prioritized Remediation**: Critical, High, and Medium priority gaps
4. **Measurable Targets**: Define target coverage percentages
5. **Visual Communication**: Use tables, charts, and indicators for executive summaries
6. **Technical Focus**: Focus on technical security controls, excluding organizational policies
7. **Customer Flexibility**: Allow customer to determine timelines and resource allocation

**Scope Exclusions**:
- Cost estimates and budgets (customer determines based on their resources)
- Specific implementation timelines (customer determines based on priorities)
- Insider threat controls (handled by organizational HR/security policies)
- Social engineering/phishing controls (handled by security awareness programs)
- Third-party vendor risks (handled by vendor management processes)

---

## Maintenance and Updates

Threat models should be updated when:

1. **Architecture Changes**
   - New components added
   - Components removed or replaced
   - Integration points change
   - Deployment model changes

2. **New Threats Emerge**
   - New attack techniques discovered
   - Vulnerabilities disclosed
   - Threat landscape changes
   - Regulatory changes

3. **Security Incidents**
   - Incidents occur in your system
   - Similar incidents occur in industry
   - Post-incident reviews completed

4. **Regular Reviews**
   - Quarterly reviews minimum
   - Annual comprehensive reviews
   - Before major releases
   - After significant changes

---

## Conclusion

This methodology ensures comprehensive security assessment that meets enterprise security standards while supporting implementation planning objectives. The resulting threat models provide actionable security guidance that can be integrated into development workflows, security operations, and compliance programs.

By following this structured approach, security teams can produce consistent, high-quality threat models that effectively communicate security risks and drive meaningful security improvements.
