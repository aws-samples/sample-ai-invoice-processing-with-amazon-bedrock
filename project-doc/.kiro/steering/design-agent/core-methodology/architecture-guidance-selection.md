---
inclusion: manual
---

# Architecture Guidance Selection Framework

## Purpose
This framework is used ONLY when Intelligence Hub is unavailable or disabled. It provides systematic guidance selection for standard architecture generation (Option B fallback).

**IMPORTANT**: This framework is NOT used when Intelligence Hub is available, as Intelligence Hub provides expert recommendations that supersede local guidance selection.

## Usage Context
- **When to Use**: Intelligence Hub disabled, unavailable, or connection failed
- **When NOT to Use**: Intelligence Hub is available and providing expert recommendations
- **Integration Point**: Referenced from Option B (Standard Architecture Generation) in architecture generation spec

## Decision Hierarchy (Priority Order)

### 1. ProServe Solutions (FIRST PRIORITY)
**When to use**: When project requirements specifically match available ProServe solution capabilities
**Load when**: Project matches automotive/ADAS use cases OR requires multi-account GitOps orchestration

**Available Solutions**:
- **Seed-Farmer**: `proserve-products-and-solutions/seed-farmer/`
  - GitOps-based deployment orchestration
  - Multi-account deployment management
  - Infrastructure as Code orchestration (CDK, Terraform, CloudFormation)
- **ADDF (Autonomous Driving Data Framework)**: `proserve-products-and-solutions/addf/`
  - Automotive/ADAS-specific modules using Seed-Farmer for deployment
  - Scene detection, simulation, visualization, compute, and storage modules
  - Uses Seed-Farmer as underlying deployment framework

**Decision Criteria** (ONLY load if these apply):

**Load Seed-Farmer when**:
- **Multi-account deployment**: Project spans multiple AWS accounts
- **GitOps workflow**: Customer wants GitOps-based deployment management
- **Complex infrastructure orchestration**: Need to coordinate CDK, Terraform, CloudFormation deployments
- **Deployment state management**: Need centralized deployment state tracking
- **AWS CodeBuild acceptable**: Customer can use AWS CodeBuild for deployments (Seed-Farmer requires CodeBuild)

**Load ADDF when**:
- **Automotive/ADAS project**: Building advanced driver-assistance systems
- **Autonomous driving data processing**: Need scene detection, simulation, visualization modules
- **Automotive data pipelines**: Processing sensor data, simulation workloads, analytics interfaces
- **Reusable automotive modules**: Want proven automotive-specific infrastructure patterns

**Skip both if**: Single account, simple deployments, no GitOps requirements, not automotive domain, OR customer cannot use AWS CodeBuild

### 2. Prescriptive Guidance (SECOND PRIORITY)
**When to use**: Proven patterns and implementation guides for specific use cases
**Load when**: ProServe solutions don't fully match, but you have specific use case patterns available

**Available Guidance**:
- **Agentic AI**: `prescriptive-guidance/agentic-ai/`
  - Framework selection and implementation patterns
  - Multi-tenant agentic AI architectures
  - Serverless agentic AI patterns
  - Operational best practices for agentic AI
  - Foundation patterns for autonomous systems

**Decision Criteria**: 
- Load when solutions don't fully match but agentic AI patterns are relevant
- Use for guidance on framework selection and architectural patterns
- Reference when building hybrid solutions

### 3. AWS Documentation Search (THIRD PRIORITY)
**When to use**: Search for additional solutions, patterns, or guidance not available locally
**Load when**: Local guidance doesn't cover the specific use case or technology AND MCP server is available

**MCP Availability Check**:
**CRITICAL FIRST STEP**: Before attempting AWS documentation search, verify MCP configuration:

1. **Check MCP Configuration**: Look for `"awslabs.aws-documentation-mcp-server"` in MCP configuration
   - If `"disabled": true` or server not configured, skip AWS Documentation Search
   - If `"disabled": false`, attempt server connection verification

2. **Server Connection Verification**: If enabled in config, verify actual availability
   - Test connection to AWS documentation MCP server
   - If connection fails, document and skip AWS Documentation Search

**Search Strategy** (Only when MCP server is available):
- Use `awslabs.aws-documentation-mcp-server` to search for:
  - Additional prescriptive guidance documents
  - Solution library patterns
  - Architecture center references
  - AWS blog posts with implementation guidance
- **Risk Mitigation**: Focus on official AWS documentation sources to avoid outdated content
- **Quality Filter**: Prioritize AWS Solutions Library and Architecture Center content

**Decision Criteria**:
- Search when local guidance gaps are identified AND MCP server is available
- Look for newer solutions or patterns not yet in local steering documents
- Validate currency of found content (check publication dates)
- Cross-reference with Well-Architected principles
- **Skip if**: MCP server disabled, unavailable, or connection fails

### 4. Well-Architected Framework (FOURTH PRIORITY)
**When to use**: Architectural principles and best practices validation
**Load when**: You need to validate architecture decisions against AWS best practices

**Available Lenses**:
- **Generative AI Lens**: `well-architected/wellarchitected-generative-ai-lens.md`
- **Analytics Lens**: `well-architected/wellarchitected-analytics-lens.md`
- **Machine Learning Lens**: `well-architected/wellarchitected-machine-learning-lens.md`
- **SaaS Lens**: `well-architected/wellarchitected-saas-lens.md`
- **Serverless Applications Lens**: `well-architected/wellarchitected-serverless-applications-lens.md`
- **Financial Services Lens**: `well-architected/wellarchitected-financial-services-industry-lens.md`
- **Healthcare Lens**: `well-architected/wellarchitected-healthcare-industry-lens.md`
- **Government Lens**: `well-architected/wellarchitected-government-lens.md`
- **IoT Lens**: `well-architected/wellarchitected-iot-lens.md`
- **Migration Lens**: `well-architected/wellarchitected-migration-lens.md`

**Decision Criteria**:
- Load specific lenses based on project domain (GenAI, Analytics, ML, SaaS, etc.)
- Use for architecture validation after initial design
- Reference for compliance and best practices validation

## Integration with Customer Context

**Context-Aware Selection**:
- **POC Mode**: Prioritize solutions and simple patterns, avoid enterprise complexity
- **Production Mode**: Include comprehensive guidance and Well-Architected validation
- **Compliance Mode**: Load relevant compliance lenses and security guidance
- **Budget-Conscious Mode**: Focus on cost-effective patterns and optimization guidance

**Reference Architecture Analysis Process**:
1. **Download Selected References**: Save to `.workflow-state/reference-architectures/[meaningful-folder-name]/`
2. **Gap Analysis**: Compare skill capabilities with project requirements
3. **Document Assessment**: Record fit analysis and adaptation needs
4. **Integration Design**: Plan customization and combination strategies