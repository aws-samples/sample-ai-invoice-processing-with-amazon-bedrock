---
inclusion: manual
---

# Architecture Generation Principles

## Purpose

This document provides universal principles and quality standards for architecture generation that apply regardless of the specific workflow or tools used. These principles support both Intelligence Hub-enhanced and standard architecture generation approaches.

## Architecture Quality Principles

### Customer Context Awareness

**Principle**: Architecture complexity and approach must align with customer context and project constraints.

**Application Guidelines**:
- **POC Mode**: Focus on core functionality validation, avoid enterprise complexity
- **Production Mode**: Include full enterprise considerations (scalability, availability, security)
- **Compliance Mode**: Integrate regulatory requirements and security controls
- **Budget-Conscious Mode**: Optimize for cost-effectiveness and resource efficiency

### Reference Architecture Leverage

**Principle**: Prefer proven reference architectures over custom solutions when applicable.

**Application Guidelines**:
- **Intelligence Hub Available**: Expert recommendations will guide technology selection and architecture patterns
- **Intelligence Hub Unavailable**: Apply systematic guidance selection framework to identify relevant reference architectures
- **Hybrid Approach**: Combine expert insights with reference architecture analysis when both are available

### Technology Selection Standards

**Principle**: Technology choices must be justified with clear rationale and aligned with project constraints.

**Selection Criteria**:
- **Functional Fit**: Technology meets functional requirements
- **Non-Functional Alignment**: Supports performance, security, scalability needs
- **Team Capability**: Aligns with team skills and experience
- **Operational Complexity**: Matches operational maturity and resources
- **Cost Effectiveness**: Balances capability with budget constraints

### Expert Insight Integration

**Principle**: When expert recommendations are available (Intelligence Hub or other sources), integrate insights systematically.

**Integration Standards**:
- **Asset Ranking Threshold**: Apply 60% threshold for technology recommendations
- **Decision Influence Documentation**: Record how expert insights influenced decisions
- **Alternative Consideration**: Document alternatives evaluated and rationale for selection
- **Risk Assessment**: Include expert-identified risks and mitigation strategies

### Intelligence Hub Integration Standards

**When Intelligence Hub is Available**:

**MCP Tool Usage Standards**:
- **Job Submission**: Use `mcp_intelligence_hub_submit_job` with functional and non-functional requirements
- **Status Monitoring**: Use `mcp_intelligence_hub_check_status` - poll every 60 seconds until COMPLETED status
- **Results Retrieval**: Use `mcp_intelligence_hub_get_result` only when status is COMPLETED (never on EXPERT_COMPLETED)
- **Response Preservation**: Save complete JSON response for debugging and audit trail

**Deep Research Decision Framework**:
- **Standard Analysis**: 10-15 minutes processing time, basic expert recommendations
- **Deep Research**: Up to 60 minutes processing time, comprehensive analysis with extended insights
- **User Choice Required**: Always prompt user for deep research preference before job submission
- **Timeout Handling**: If timeout exceeded, document and proceed with standard architecture generation

**Status Flow Understanding**:
- **SUBMITTED** → Job has been submitted to Intelligence Hub
- **PROCESSING** → Job is being processed by expert systems
- **EXPERT_COMPLETED** → Expert analysis complete (deep research may still be running)
- **COMPLETED** → All processing finished (safe to retrieve results)

**Critical Integration Rules**:
- Never call `get_result()` on EXPERT_COMPLETED status
- Continue polling while status is SUBMITTED, PROCESSING, or EXPERT_COMPLETED
- Block workflow progression until COMPLETED status or timeout when deep research is requested
- Document Intelligence Hub influence on all architecture decisions

---

## Architecture Documentation Standards

### Architecture Decision Records (ADRs)

**Principle**: Document architectural decisions with clear rationale and context.

**Quality Standards**:
- **Individual Files**: Create separate markdown files for each Architecture Decision Record
- **Naming Convention**: Use `ADR-XXX-[descriptive-title].md` format
- **Folder Organization**: Place in `architecture-decision-records/` folder
- **Sequential Numbering**: Use zero-padded numbering (001, 002, 003, etc.)

**ADR Content Requirements**:
- **Context**: Clear problem statement and constraints
- **Decision**: Specific architectural choice made
- **Consequences**: Trade-offs and implications
- **Alternatives**: Options considered and why they were rejected
- **Rationale**: Reasoning behind the decision (expert insights, customer context, constraints)

### Technical Specification Standards

**Principle**: Provide implementable technical specifications that development teams can follow directly.

**Quality Criteria**:
- **Component Specifications**: Clear purpose, responsibilities, interfaces, dependencies
- **API Specifications**: Complete endpoint definitions with request/response formats
- **Data Architecture**: Data models, schema design, indexing strategy
- **Integration Patterns**: External system integrations and internal service communication
- **Deployment Architecture**: Environment setup, deployment pipeline, infrastructure as code

### Architecture Package Structure

**Standard Organization**:
```
architecture/
├── system-architecture.md
├── architecture-decision-records/
│   ├── ADR-001-[decision-title].md
│   ├── ADR-002-[decision-title].md
│   └── ADR-00X-[decision-title].md
├── technical-specifications.md
├── api-specifications.md
├── data-architecture.md
├── integration-architecture.md
└── deployment-architecture.md
```

## Architecture Quality Assessment

### Technical Accuracy Standards

**Principle**: All architectural decisions must be technically sound and implementable.

**Validation Criteria**:
- **Service Limits Awareness**: Architecture considers AWS service quotas and limits
- **Scalability Validation**: Components can scale to meet non-functional requirements
- **Security Integration**: Security controls integrated throughout architecture
- **Performance Feasibility**: Architecture can meet performance requirements
- **Cost Optimization**: Architecture balances capability with cost constraints

### Implementation Readiness

**Principle**: Architecture documentation must provide sufficient detail for development teams to implement without additional clarification.

**Readiness Indicators**:
- **Complete Specifications**: All components fully specified
- **Clear Interfaces**: Component interactions well-defined
- **Technology Justification**: Technology choices explained with rationale
- **Implementation Guidance**: Development strategy and phases defined
- **Risk Mitigation**: Known risks identified with mitigation strategies

### Stakeholder Communication

**Principle**: Architecture must be communicated effectively to different stakeholder groups.

**Communication Standards**:
- **Executive Summary**: High-level overview focusing on business alignment and risk
- **Development Team View**: Detailed technical specifications and implementation guidance
- **Operations View**: Deployment, monitoring, and operational considerations
- **Security View**: Security controls, compliance, and risk mitigation measures

## Continuous Improvement Standards

### Architecture Feedback Integration

**Principle**: Architecture effectiveness should be measured and improved continuously through systematic stakeholder feedback integration.

**Feedback Mechanisms**:
- **Implementation Velocity**: Track time from architecture to working implementation
- **Architecture Clarity**: Monitor clarification requests during development
- **Technical Debt**: Assess architecture decisions requiring future refactoring
- **Performance Achievement**: Compare actual vs. planned performance outcomes
- **Team Satisfaction**: Collect feedback on architecture quality and usability
- **Stakeholder Feedback Integration**: Systematic collection and analysis of feedback through `project-doc/feedback/iteration-N/` folders
- **Dynamic Improvement**: Automatic generation of architecture improvement tasks based on feedback content

**Iterative Architecture Refinement**:
- **Feedback-Driven Updates**: Architecture modifications based on systematic stakeholder feedback analysis
- **Complete Project Iterations**: Creation of new complete project folders (project-name-iteration-N) incorporating feedback
- **Traceability Maintenance**: Complete audit trail linking feedback documents to specific architecture changes
- **Quality Continuity**: Ensure architecture quality standards are maintained or improved across feedback iterations

### Version Control and Change Management

**Principle**: Architecture changes must be tracked and managed systematically across feedback iterations.

**Change Management Standards**:
- **Version Control**: All architecture documents under version control with iteration-based versioning
- **Change Logs**: Document all architectural modifications with rationale and feedback source traceability
- **Review Cycles**: Regular architecture review with development teams and systematic stakeholder feedback integration
- **Update Procedures**: Clear process for updating architecture based on feedback through dynamic task generation
- **Iteration Management**: Systematic management of complete project folder iterations with proper versioning and organization
