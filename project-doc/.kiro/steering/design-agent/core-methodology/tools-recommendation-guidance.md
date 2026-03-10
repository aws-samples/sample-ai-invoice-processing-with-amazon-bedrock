---
inclusion: manual
---

# Tools Recommendation Guidance for Design Agent

## Purpose

This document provides comprehensive guidance for the Design Agent's tools recommendation task (Task 6.1: Tools Prescriptive Guidance Generation). It establishes the framework for analyzing and recommending both MCP servers and Skills, categorizing them by value and use case, and generating project-specific recommendations that align with the design agent workflow.

## Overview: MCPs and ProServe Skills

### Model Context Protocol (MCP) Servers
**Purpose**: External tools and integrations that extend AI agent capabilities through standardized protocols
**Integration**: Configured in `.kiro/settings/mcp.json` or platform-specific MCP configuration
**Usage**: Real-time tool access during agent execution for documentation, diagrams, APIs, and data generation
**Repository**: https://github.com/awslabs/mcp (AWS Labs MCP servers)

### ProServe Skills
**Purpose**: AWS ProServe-specific implementation patterns for enterprise solutions
**Integration**: Cloned from ProServe repository and adapted to project needs
**Usage**: Enterprise-grade reference architectures for agent-based solutions, authentication patterns, and multi-component deployments
**Repository**: https://code.aws.dev/proserve/proserve-apex/proserve-skills

## Design Agent Tool Requirements

### Core Workflow Integration

The Design Agent follows a six-stage workflow where tools provide critical capabilities:

**Stage 1: Project Analysis**
- **MCPs**: Analyze existing codebases for complexity assessment, research reference architectures
- **ProServe Skills**: Reference existing implementation patterns for complexity estimation

**Stage 2: Requirements Generation** 
- **MCPs**: Validate AWS service capabilities, generate test data scenarios, access authoritative documentation
- **ProServe Skills**: Reference proven requirement patterns for similar project types

**Stage 3: Architecture Generation**
- **MCPs**: Access Well-Architected Framework, generate architecture diagrams, discover reference implementations
- **ProServe Skills**: Apply enterprise-grade multi-component architectures for agent-based solutions

**Stage 4: Quality Assessment**
- **MCPs**: Validate architecture against AWS best practices, generate visual diagrams for gap analysis
- **ProServe Skills**: Compare against proven implementation patterns

**Stage 5: Security Assessment**
- **MCPs**: Access security best practices, generate threat model diagrams
- **ProServe Skills**: Reference proven security implementation patterns

**Stage 6: Documentation Generation**
- **MCPs**: Generate final architecture diagrams for deliverables
- **ProServe Skills**: Reference documentation patterns and templates

## MCP Server Categories for Design Agent

### Essential MCPs (Always Recommend)

#### 1. AWS Knowledge MCP Server ⭐⭐⭐⭐⭐
**Server ID**: `awslabs.aws-knowledge-mcp-server`
**Purpose**: Access to AWS documentation, API references, What's New, blogs, Well-Architected guidance
**Critical Use Cases**:
- Requirements validation against AWS service capabilities
- Architecture best practices and Well-Architected Framework access
- Security best practices for threat modeling
- Service limits and quotas research

**Workflow Integration**:
- Stage 2: Service capability validation for requirements
- Stage 3: Technology selection justification and best practices
- Stage 4: Architecture validation against AWS patterns
- Stage 5: Security controls and compliance guidance

#### 2. AWS Diagram MCP Server ⭐⭐⭐⭐⭐
**Server ID**: `awslabs.aws-diagram-mcp-server`
**Purpose**: Generate architecture diagrams and technical illustrations
**Critical Use Cases**:
- System architecture diagrams for specifications
- Component interaction and data flow diagrams
- Deployment architecture visualizations
- Threat model diagrams for security assessment

**Workflow Integration**:
- Stage 3: Automated diagram generation from architecture decisions
- Stage 4: Visual architecture validation and gap analysis
- Stage 5: Security architecture and threat model visualization
- Stage 6: Professional diagram inclusion in deliverables

### High-Value MCPs (Recommend for Most Projects)

#### 3. Git Repo Research MCP Server ⭐⭐⭐⭐
**Server ID**: `awslabs.git-repo-research-mcp-server`
**Purpose**: Semantic code search and repository analysis
**Use Cases**:
- AWS samples repository analysis for reference architectures
- CDK/Terraform pattern discovery
- Community implementation validation
- Proven pattern identification

**Workflow Integration**:
- Stage 1: Existing codebase complexity assessment
- Stage 3: Reference architecture discovery and pattern validation
- Stage 4: Architecture validation against proven implementations

#### 4. AWS Documentation MCP Server ⭐⭐⭐⭐
**Server ID**: `awslabs.aws-documentation-mcp-server`
**Purpose**: Latest AWS documentation and API references
**Use Cases**:
- Service-specific documentation for detailed requirements
- API specifications for integration design
- Security configuration guidance
- SDK documentation for implementation planning

**Workflow Integration**:
- Stage 2: API capability validation for requirements
- Stage 3: Integration pattern selection and specification
- Stage 5: Security configuration reference and validation

### Conditional MCPs (Project-Type Specific)

#### 5. Code Documentation Generator MCP Server ⭐⭐⭐
**Server ID**: `awslabs.code-doc-gen-mcp-server`
**Purpose**: Automated documentation from code analysis
**When to Recommend**: Projects with existing codebases requiring analysis
**Use Cases**:
- Extract functional requirements from existing code
- Document as-is architecture patterns
- Generate API documentation from code analysis

#### 6. Synthetic Data MCP Server ⭐⭐⭐
**Server ID**: `awslabs.syntheticdata-mcp-server`
**Purpose**: Generate realistic test data for development and ML
**When to Recommend**: Data-intensive projects or those requiring concrete examples
**Use Cases**:
- Test data scenarios for acceptance criteria
- Realistic data models for architecture validation
- Performance testing data generation

#### 7. AWS Pricing MCP Server ⭐⭐⭐⭐
**Server ID**: `awslabs.aws-pricing-mcp-server`
**Purpose**: AWS service pricing and cost estimates
**When to Recommend**: Projects with specific budget constraints or cost optimization requirements
**Use Cases**:
- Architecture cost estimation and validation
- Budget feasibility analysis
- Cost optimization recommendations

#### 8. Amazon Bedrock AgentCore MCP Server ⭐⭐⭐
**Server ID**: `awslabs.amazon-bedrock-agentcore-mcp-server`
**Purpose**: AgentCore platform services, APIs, and best practices
**When to Recommend**: Projects involving AI agents or AgentCore integration
**Use Cases**:
- Agentic AI architecture patterns
- AgentCore service integration guidance
- AI/ML workflow design patterns

#### 9. Frontend MCP Server ⭐⭐
**Server ID**: `awslabs.frontend-mcp-server`
**Purpose**: React and modern web development guidance
**When to Recommend**: Projects with significant web frontend components
**Use Cases**:
- UI/UX requirements for web applications
- Frontend architecture patterns and best practices
- API integration patterns for SPAs

### Validation MCPs (Optional but Valuable)

#### 10. AWS API MCP Server ⭐⭐⭐
**Server ID**: `awslabs.aws-api-mcp-server`
**Purpose**: Comprehensive AWS API support with command validation
**When to Recommend**: Projects requiring real-time validation of AWS capabilities
**Use Cases**:
- Service quotas and limits validation
- API capability verification
- Technical feasibility validation

## ProServe Skills for Design Agent

### ProServe Skills

**Purpose**: AWS ProServe pre-built, reusable components implementing common AWS patterns and services  
**Repository**: https://code.aws.dev/proserve/proserve-apex/proserve-skills
**Complete Documentation**: See `AGENT.md` in repository for comprehensive usage guidelines, available skills, and implementation process

**Overview**:

ProServe Skills are self-contained components with Infrastructure as Code (CDK/CloudFormation), configuration management, deployment scripts, testing, and complete documentation. Skills include identity management, AgentCore networking and runtime, knowledge bases, user interfaces, Lambda functions, and agent evaluation frameworks.

**When to Recommend**:
- Conversational AI applications with multi-component architecture
- Agent-based solutions requiring identity management or AgentCore Runtime
- Projects needing Bedrock Knowledge Base, agent deployment, or coordinated multi-component deployment
- GenAI applications where proven reference patterns can accelerate development
- Projects using CDK or CloudFormation for infrastructure

**Functional Fit Assessment**:
- **Multi-Component Need**: Project requires coordinated identity, agent, API, and UI components
- **AgentCore Runtime**: Project can leverage AgentCore Runtime for agent/MCP deployment
- **Authentication Integration**: Standard Cognito authentication patterns meet security requirements
- **Configuration Management**: Project can use central `project/config.yaml` for dependency coordination
- **Infrastructure as Code**: Project uses CDK or CloudFormation

**Customization Decision Framework**:

**Use As Foundation When**:
- Standard multi-component agent architecture fits project needs
- Proven authentication and deployment patterns are acceptable
- Time-to-market benefits outweigh customization constraints
- Project uses CDK/CloudFormation for infrastructure

**Extend and Adapt When**:
- Core patterns fit but additional functionality or integration required
- Standard components provide solid foundation for custom extensions
- Specific skills need customization for project requirements

**Use as Reference When**:
- Project architecture differs significantly from standard patterns
- Custom frameworks or authentication approaches required
- Project uses different IaC tools (Terraform, etc.)

**Implementation Guidance**:

For complete details on available skills, implementation process, configuration management, and usage patterns, refer to `AGENT.md` in the ProServe Skills repository. The AGENT.md file provides:
- Complete list of available skills with descriptions
- Implementation process
- Configuration management patterns with `project/config.yaml`
- SKILL.md documentation structure for each skill

## Tools Recommendation Framework

### Project Analysis Decision Tree

Use this systematic approach to analyze project characteristics and generate tool recommendations:

#### Step 1: Project Type Classification
**Analyze project characteristics to determine tool needs:**

```
Project Type Assessment:
├── Greenfield vs. Existing System
│   ├── Greenfield → Focus on Essential MCPs + ProServe Skills for patterns
│   └── Existing System → Add Code Documentation Generator MCP
├── Application Type
│   ├── Web Application → Consider Frontend MCP
│   ├── AI/ML Application → Consider Bedrock AgentCore MCP
│   ├── Agent-Based Solution → Strongly Consider ProServe Skills
│   ├── Data-Intensive → Consider Synthetic Data MCP
│   └── Standard Application → Essential MCPs
├── Budget Constraints
│   ├── Budget-Constrained → Add AWS Pricing MCP (mandatory)
│   └── Standard Budget → AWS Pricing MCP (optional)
└── Validation Requirements
    ├── Real-time Validation Needed → Add AWS API MCP
    └── Standard Validation → Use AWS Documentation MCP
```

#### Step 2: Architecture Complexity Assessment
**Determine tool scope based on project complexity:**

| Complexity Level | Indicators | MCP Recommendation | ProServe Skills Recommendation |
|------------------|------------|-------------------|-------------------------------|
| **Simple** | Single service, basic functionality, small team | Essential MCPs only | Consider as reference only |
| **Moderate** | Multiple services, standard patterns, experienced team | Essential + High-Value MCPs | Consider if agent-based architecture |
| **Complex** | Distributed architecture, custom patterns, large team | Essential + High-Value + Conditional MCPs | Strongly recommend for enterprise patterns |

#### Step 3: Team Experience Evaluation
**Adjust recommendations based on team capabilities:**

| Experience Level | Characteristics | MCP Focus | ProServe Skills Focus |
|------------------|----------------|-----------|----------------------|
| **Experienced** | AWS-familiar, efficiency-focused | Efficiency MCPs (diagrams, automation) | Reference patterns for acceleration |
| **Learning** | New to AWS, guidance-needed | Guidance MCPs (knowledge, documentation) | Detailed implementation templates |
| **Mixed** | Varied experience levels | Balanced approach with both guidance and efficiency | Mix of reference patterns and detailed templates |

#### Step 4: Timeline and Resource Constraints
**Consider project constraints for tool selection:**

| Constraint Type | Impact on MCP Selection | Impact on ProServe Skills Selection |
|----------------|------------------------|-------------------------------------|
| **Tight Timeline** | Minimal MCP set, focus on essential only | Prioritize proven patterns for rapid development |
| **Standard Timeline** | Full recommended MCP set | Balanced use of reference patterns |
| **Extended Timeline** | Include optional validation MCPs | Opportunity for custom implementations |
| **Limited Resources** | Prioritize automation MCPs (diagrams, code generation) | Leverage complete implementation templates |
| **Ample Resources** | Include comprehensive MCP set with validation tools | Mix of reference patterns and custom development |

### Tools Selection Decision Matrix

Use this matrix to systematically select tools based on project analysis:

| Tool | Type | Essential | Simple Projects | Moderate Projects | Complex Projects | Specific Triggers |
|------|------|-----------|----------------|-------------------|------------------|-------------------|
| **AWS Knowledge** | MCP | ✅ Always | ✅ Include | ✅ Include | ✅ Include | All projects |
| **AWS Diagram** | MCP | ✅ Always | ✅ Include | ✅ Include | ✅ Include | All projects |
| **Git Repo Research** | MCP | High-Value | ⚠️ Consider | ✅ Include | ✅ Include | Reference architecture needs |
| **AWS Documentation** | MCP | High-Value | ⚠️ Consider | ✅ Include | ✅ Include | API integration requirements |
| **Code Documentation** | MCP | Conditional | ❌ Skip | ⚠️ Consider | ✅ Include | Existing codebase present |
| **Synthetic Data** | MCP | Conditional | ❌ Skip | ⚠️ Consider | ✅ Include | Data-intensive projects |
| **AWS Pricing** | MCP | Conditional | ⚠️ Consider | ⚠️ Consider | ✅ Include | Budget constraints present |
| **Bedrock AgentCore** | MCP | Conditional | ❌ Skip | ⚠️ Consider | ✅ Include | AI/ML components present |
| **Frontend** | MCP | Conditional | ❌ Skip | ⚠️ Consider | ⚠️ Consider | Web application with UI |
| **AWS API** | MCP | Validation | ❌ Skip | ❌ Skip | ⚠️ Consider | Real-time validation needed |
| **ProServe Skills** | Skills | Conditional | ❌ Skip | ⚠️ Consider | ✅ Include | Agent-based multi-component architecture |

**Legend**: ✅ Include, ⚠️ Consider (project-dependent), ❌ Skip

### Recommendation Template Structure

```markdown
# Tools Prescriptive Guidance

## Executive Summary
[Project-specific tools landscape overview and key recommendations based on decision tree analysis]

## Project Analysis Summary
### Project Characteristics Assessment
[Document project type, complexity, team experience, and constraints that drove tool selection]

### Tools Requirements Analysis
[Explain how project characteristics led to specific MCP and Skills category selections]

## Available Tools

### MCP Servers

#### Essential MCPs (Required for All Projects)
[Always include AWS Knowledge and AWS Diagram MCPs with detailed configuration and workflow integration]

#### High-Value MCPs (Recommended for This Project)
[Include Git Repo Research and AWS Documentation with project-specific justification based on decision matrix]

#### Project-Specific MCPs
[Include conditional MCPs based on decision matrix analysis with clear business justification]

#### Optional MCPs (Available but Not Recommended)
[List other available MCPs with brief explanation of why they're not recommended for this specific project]

### ProServe Skills

#### ProServe Skills (If Applicable)
[Recommend ProServe Skills if project matches agent-based multi-component architecture]

**Applicability Assessment**:
- [Evaluation against ProServe Skills criteria]
- [Customization approach: Foundation/Extend/Reference]

**Recommended Skills**:
- [Skill Component]: [Specific use case and customization approach]
- [Skill Component]: [Specific use case and customization approach]

**Repository**: https://code.aws.dev/proserve/proserve-apex/proserve-skills
**Integration Approach**: [How to clone and adapt ProServe Skills to project needs]

## Project-Specific Recommendations

### Primary Tools Configuration

#### MCP Configuration
[Recommended MCP server list with configuration details following decision matrix results]

#### ProServe Skills Integration Strategy
[Recommended approach for integrating ProServe Skills if applicable]

### Implementation Strategy

#### MCP Setup and Usage
[Phased approach for configuring and using recommended MCPs aligned with design workflow stages]

#### ProServe Skills Integration Process
[Step-by-step process for cloning, adapting, and integrating ProServe Skills if applicable]

### Usage Patterns

#### MCP Usage Patterns
[Specific usage patterns for each recommended MCP in the context of this project's workflow stages]

#### ProServe Skills Usage Patterns
[How to leverage ProServe Skills as reference implementations, starter templates, or pattern libraries]

## Configuration Examples

### Workspace MCP Configuration
[Provide specific .kiro/settings/mcp.json configuration for recommended MCPs with auto-approve settings]

```json
{
  "mcpServers": {
    "awslabs.aws-knowledge-mcp-server": {
      "command": "uvx",
      "args": ["awslabs.aws-knowledge-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    },
    "awslabs.aws-diagram-mcp-server": {
      "command": "uvx", 
      "args": ["awslabs.aws-diagram-mcp-server@latest"],
      "env": {
        "FASTMCP_LOG_LEVEL": "ERROR"
      },
      "disabled": false,
      "autoApprove": []
    }
  }
}
```

### ProServe Skills Integration Commands

**ProServe Skills** (if applicable):
```bash
# Clone ProServe Skills repository
git clone git@ssh.code.aws.dev:proserve/proserve-apex/proserve-skills.git 

# Navigate to relevant skill component
cd proserve-skills/[component-name]

# Follow SKILL.md for skill-specific integration guidance
```

### Usage Guidelines
[Best practices for using MCPs and ProServe Skills in the design agent workflow with project-specific considerations]

## Quality Standards

### Information Traceability
- All MCP-sourced information must include source URLs and server identification
- MCP responses must be validated against project context and requirements
- Skills recommendations must be justified based on project architecture and requirements
- All tool recommendations must be justified in architecture decision records

### Validation Requirements
- MCP-generated diagrams must be reviewed for accuracy and completeness
- AWS Knowledge MCP guidance must align with Well-Architected principles
- Reference architectures from Git Repo Research must be validated for project relevance
- ProServe Skills patterns must be evaluated for fit with project architecture and requirements
- ProServe Skills customization approach must be clearly documented

## Implementation Roadmap

### Phase 1: MCP Setup
[Step-by-step MCP configuration and validation]

### Phase 2: ProServe Skills Integration
[ProServe Skills repository cloning and initial integration if applicable]

### Phase 3: Tools Validation
[Testing and validation of MCP and ProServe Skills integration]

### Phase 4: Team Enablement
[Training and documentation for development team]

## Risk Assessment and Mitigation

### MCP Dependency Risks
[MCP server availability risks and alternative approaches]

### ProServe Skills Integration Risks
[Risks related to ProServe Skills adaptation and customization]

### Mitigation Strategies
[Specific mitigation approaches for identified risks]
```

## Quality Criteria for Tools Recommendations

### Completeness Requirements
- [ ] All available MCP servers documented with purpose and capabilities
- [ ] ProServe Skills applicability assessed with clear justification
- [ ] Project-specific analysis completed with clear justification
- [ ] Configuration examples provided for all recommended MCPs
- [ ] Integration guidance provided for ProServe Skills if applicable
- [ ] Usage patterns documented for each workflow stage

### Accuracy Requirements
- [ ] MCP server capabilities correctly identified and described
- [ ] ProServe Skills patterns accurately matched to project requirements
- [ ] Project analysis accurately reflects requirements and architecture
- [ ] Configuration examples tested and validated
- [ ] Usage guidance aligns with MCP server and ProServe Skills capabilities

### Actionability Requirements
- [ ] Clear implementation steps provided for MCPs and ProServe Skills
- [ ] Specific configuration details included for MCPs
- [ ] Specific integration commands and processes provided for ProServe Skills if applicable
- [ ] Usage examples relevant to project context
- [ ] Troubleshooting guidance included

### Professional Standards
- [ ] Recommendations suitable for enterprise decision-making
- [ ] Clear business justification for each MCP and ProServe Skills recommendation
- [ ] Risk assessment included for tool dependencies
- [ ] Alternative approaches documented where applicable

## Integration with Design Agent Workflow

### Workflow Stage Integration

**Stage 0: Session Management**
- Check existing MCP configuration and ProServe Skills repository access
- Validate MCP server availability and ProServe Skills repository access
- Document tools readiness for workflow execution

**Stage 1: Project Analysis**
- Use project characteristics to determine MCP and ProServe Skills recommendations
- Analyze complexity to determine tool scope
- Document tools requirements in project analysis

**Stage 6: Documentation Generation (Task 6.1)**
- Generate comprehensive tools prescriptive guidance
- Include project-specific recommendations and configuration for MCPs
- Include ProServe Skills integration strategy and repository references if applicable
- Provide implementation roadmap for recommended tools

### Handoff Requirements

The tools prescriptive guidance document must:
- Provide clear next steps for MCP implementation and ProServe Skills integration
- Include complete configuration examples for MCPs
- Include repository URLs and integration commands for ProServe Skills if applicable
- Document expected benefits and success metrics
- Enable smooth handoff to implementation teams

## Success Metrics

### Quantitative Metrics
- **Coverage Completeness**: All available MCPs and ProServe Skills documented and categorized
- **Recommendation Relevance**: 90%+ of recommendations applicable to project needs

### Qualitative Metrics
- **Implementation Clarity**: Clear, actionable guidance for MCP setup and ProServe Skills integration
- **Business Justification**: Strong business case for each MCP and ProServe Skills recommendation
- **Technical Accuracy**: Accurate representation of MCP and ProServe Skills capabilities and limitations
- **Professional Quality**: Enterprise-grade documentation suitable for stakeholder review

## Framework Application Process

### Step-by-Step Recommendation Process

**Step 1: Load and Apply Framework**
1. Read this complete tools recommendation guidance document
2. Review MCP server categories and ProServe Skills framework
3. Understand the decision tree and selection matrix
4. Prepare to apply systematic analysis to the specific project

**Step 2: Conduct Project Analysis**
1. **Project Type Classification**: Use decision tree to classify project characteristics
2. **Complexity Assessment**: Determine simple/moderate/complex classification
3. **Team Experience Evaluation**: Assess team AWS familiarity and preferences
4. **Constraint Analysis**: Consider timeline, budget, and resource limitations

**Step 3: Apply Selection Matrix**
1. Start with Essential MCPs (always include AWS Knowledge and AWS Diagram)
2. Evaluate High-Value MCPs based on project complexity and needs
3. Consider Conditional MCPs based on specific project triggers
4. Evaluate ProServe Skills applicability for agent-based multi-component architectures
5. Validate selections against team experience and constraints

**Step 4: Generate Recommendations**
1. Create project-specific justification for each selected MCP and ProServe Skills
2. Provide complete configuration examples for MCPs following templates
3. Provide repository URLs and integration guidance for ProServe Skills if applicable
4. Document usage patterns for each workflow stage
5. Include implementation roadmap and risk mitigation

**Step 5: Quality Validation**
1. Ensure all recommendations follow framework patterns
2. Verify business justification for each MCP and ProServe Skills selection
3. Confirm configuration examples are complete and actionable
4. Validate ProServe Skills integration guidance is clear and specific if applicable
5. Validate against anti-patterns to avoid common mistakes

## Common Patterns and Anti-Patterns

### Recommended Patterns
✅ **Framework-Driven Selection**: Always use decision tree and selection matrix
✅ **Project-Specific Analysis**: Conduct thorough project characteristics assessment
✅ **Essential MCPs First**: Always include AWS Knowledge and AWS Diagram MCPs
✅ **ProServe Skills Evaluation**: Assess ProServe Skills applicability for agent-based architectures
✅ **Justified Conditional Tools**: Include conditional MCPs and ProServe Skills only with specific project triggers
✅ **Complete Configuration Examples**: Provide actionable .kiro/settings/mcp.json configurations
✅ **Clear ProServe Skills Integration**: Provide specific repository URLs and integration commands if applicable
✅ **Workflow Integration**: Document integration points with all six design workflow stages
✅ **Business Justification**: Include clear business value proposition for each recommendation
✅ **Implementation Roadmap**: Provide phased approach with success criteria

### Anti-Patterns to Avoid
❌ **Configuration-Based Recommendations**: Don't just document existing user MCP configuration
❌ **Recommending All Available Tools**: Avoid suggesting all MCPs and ProServe Skills without project-specific justification
❌ **Generic Recommendations**: Don't provide one-size-fits-all recommendations without project analysis
❌ **Incomplete Configuration Examples**: Avoid partial configurations that cannot be directly implemented
❌ **Missing Business Justification**: Don't recommend tools without clear business value explanation
❌ **Vague ProServe Skills Guidance**: Don't recommend ProServe Skills without specific integration approach
❌ **Ignoring Team Experience**: Don't overlook team capabilities and learning preferences
❌ **Skipping Framework Steps**: Don't bypass decision tree or selection matrix analysis
❌ **No Risk Assessment**: Don't omit tool dependency risks and mitigation strategies
❌ **ProServe Skills Without Customization Guidance**: Don't recommend ProServe Skills without clear customization approach (Foundation/Extend/Reference)
