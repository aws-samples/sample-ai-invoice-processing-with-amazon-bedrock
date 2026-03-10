# Design Agent Workflow

## Overview

**Purpose**: Seven-stage orchestrated workflow that transforms multi-category project inputs into enterprise-grade specification packages through enhanced context classification, systematic requirements generation, policy-driven architecture design, holistic quality assessment, and comprehensive security evaluation.

**Modular Benefits**: 
- Focused, modular task files enable parallel development and avoid merge conflicts
- Each module covers a single workflow stage with complete execution instructions
- Clear separation between orchestration (this file) and detailed task execution (individual modules)
- Easy navigation to find specific task instructions quickly

## Prerequisites

### Enhanced Context Sources and Discovery Protocol
**Every task must load context from these standardized locations in this order:**

1. **`.workflow-state/design-handoff.md`** - Input scenario and workflow state
   - Read first to understand current workflow state and input scenario
   - Contains input scenario determination (Existing documents/Start from scratch/Mixed/Insufficient)
   - Contains progress tracking and task coordination information

2. **`.workflow-state/customer-context.md`** - Captured customer context
   - Always created during session management (Task 0.0)
   - Contains structured customer context (project goals, technical preferences, organizational context)
   - Load for all tasks requiring customer context

3. **Enhanced Input Analysis** - User-provided materials organized by processing stage:

   **For Requirements Generation (Stage 2):**
   **3a. `project-doc/project-context/`** - Project-specific requirements and context
   - Core business objectives, functional requirements, and user stories
   - Project-specific constraints, preferences, and stakeholder needs
   - Primary source for "what we're building"

   **3b. `project-doc/technical-knowledge/`** - External reference materials
   - External API documentation, integration specifications, and system references
   - Service limits, authentication patterns, and compatibility requirements
   - Source for "what we're integrating with" (NOT what we're building)

   **3c. `project-doc/organization-context/`** - Organizational policies and standards
   - Company naming conventions, tagging strategies, and resource patterns
   - Security policies, compliance requirements, and budget constraints
   - Organizational standards that must be applied to all architecture decisions

   **For Architecture Generation (Stage 3):**
   **3d. `.workflow-state/reference-architectures/`** - Analyzed existing codebases (from Stage 1)
   - Brownfield analysis results, existing code structure, and integration patterns
   - Reference system dependencies and compatibility requirements
   - Source for "what we can leverage or integrate with"

4. **Current User Prompt** - Additional context from current request
   - Extract images, descriptions, requirements provided in current session
   - Integrate with other context sources for comprehensive analysis

**Stage-Specific Processing Rules**:
- **Stage 2 (Requirements)**: Process only project-context, technical-knowledge, and organization-context
- **NEVER** treat technical-knowledge materials as project build targets
- **ALWAYS** apply organization-context policies across all architecture decisions
- **CLEARLY** separate project requirements from external integration needs
- **Stage 3 (Architecture)**: Incorporate reference system analysis from Stage 1 to inform architecture decisions

## Execution Instructions

### Core Execution Rules

**CRITICAL CONSTRAINTS**:
- **Source-traceable information only** - All information must come from verifiable sources: project documents, customer interactions, steering documents, MCP tool responses, or current prompt
- **Never invent or assume** - Do not add information from memory, experience, or assumptions not explicitly provided by traceable sources
- **Trust erosion prevention** - Inventing information appears as hallucination and destroys user trust
- **Document information sources** - All analysis, recommendations, and outputs must be traceable to specific, identifiable sources

**EXECUTION PATTERN**:
1. **LOAD** the task module file completely
2. **FOLLOW** the Context Sources and Discovery Protocol (read workflow state first)
3. **COMPLETE** the Task Checklist at the end of that module
4. **UPDATE** workflow state after task completion (write progress and status)
5. **ONLY THEN** proceed to the next stage

**WORKFLOW STATE MANAGEMENT**:
- **Read before each task** - Always load current workflow state from `.workflow-state/design-handoff.md` before starting any task
- **Update after each task** - Always update workflow state with progress and completion status after finishing any task
- **State continuity** - Workflow state enables session recovery and progress tracking across task executions

**NAVIGATION RULE**: This file is a navigation hub only. All actual task execution must follow the individual task modules. **DO NOT** execute tasks based on summaries in this file.

### Enhanced Focus Areas by Processing Stage

**Stage 2 - Requirements Generation (Three Categories Only)**:

**When processing project-context materials**:
- Extract core business objectives and functional requirements
- Identify user personas, workflows, and success criteria
- Document project-specific constraints and technical preferences
- Generate primary requirements that define "what we're building"

**When processing technical-knowledge materials**:
- Analyze external API documentation WITHOUT treating as build targets
- Extract integration patterns, data formats, and authentication requirements
- Identify service limits, rate limits, and compatibility constraints
- Document how external systems influence architecture decisions
- Generate integration requirements that define "what we're integrating with"

**When processing organization-context materials**:
- Extract naming conventions, tagging strategies, and resource patterns
- Apply security policies, compliance requirements, and budget constraints
- Enforce organizational standards across all architecture decisions
- Validate against company-specific requirements (MAP credits, cost allocation)
- Generate organizational constraints that define "how we must build"

**Stage 3 - Architecture Generation (Requirements + Reference Analysis)**:

**When incorporating reference system analysis (from Stage 1)**:
- Use comprehensive brownfield analysis from `.workflow-state/reference-architectures/`
- Identify reusable components and integration opportunities
- Document reference system dependencies and compatibility requirements
- Generate integration strategies balancing requirements with existing assets
- Balance new requirements with existing system integration opportunities

**When working with requirements and reference analysis**:
- Maintain clear separation between requirements-driven needs and existing system capabilities
- Resolve conflicts between requirements and existing system constraints
- Apply organizational constraints consistently across all architecture decisions
- Ensure reference system integration supports rather than drives requirements

### Escalation Triggers

**Immediate escalation required when**:
- Critical information gaps prevent workflow completion
- Fundamental conflicts between requirements and constraints
- Technical feasibility concerns that cannot be resolved
- Customer context insufficient for informed decision-making
- Quality thresholds cannot be achieved with available information

**Escalation process**:
1. Document specific issue and attempted resolution approaches
2. Identify minimum information needed to proceed
3. Present clear options and trade-offs to customer
4. Obtain explicit customer decision before proceeding
5. Document decision rationale in workflow state

### Success Criteria

**Overall workflow success**:
- Complete specification package with 90/100+ quality score
- Comprehensive threat model with security controls integration
- Stakeholder validation and acceptance
- All deliverables organized for seamless handoff

**Per-stage success criteria**:
- Each stage must meet its specific acceptance criteria before progression
- Quality gates enforced at stage transitions
- Continuous validation against customer context and requirements
- Documentation completeness verified at each stage

## Workflow Structure

### Stage 0: Session Management
**Module**: [Session Management](task-modules/00-session-management.md)
- **Purpose**: Execution mode detection, handoff protocols, and session recovery
- **Key Activities**: Context capture, workflow state initialization, execution mode selection
- **Deliverables**: Customer context file, design handoff file, workflow state setup

### Stage 1: Project Analysis  
**Module**: [Project Analysis](task-modules/01-project-analysis.md)
- **Purpose**: Project complexity assessment and workflow recommendations
- **Key Activities**: Input assessment, complexity evaluation, workflow path selection
- **Deliverables**: Project complexity assessment, workflow recommendations

### Stage 2: Requirements Generation
**Module**: [Requirements Generation](task-modules/02-requirements-generation.md)
- **Purpose**: Multi-category input assessment and requirements package generation with context separation
- **Key Activities**: Three-category input processing (project-context, technical-knowledge, organization-context), integration requirements extraction, policy application, reference system analysis, requirements elicitation with category-specific traceability
- **Deliverables**: Complete requirements package with category-separated functional/non-functional requirements, integration specifications, organizational compliance requirements, and reference system integration plans

### Stage 3: Architecture Generation
**Module**: [Architecture Generation](task-modules/03-architecture-generation.md)
- **Purpose**: Multi-category architecture design with optional Intelligence Hub integration and organizational policy enforcement
- **Key Activities**: Architecture design incorporating all four input categories, technology selection with organizational constraints, implementation planning with reference system integration, policy-driven validation
- **Deliverables**: Complete architecture specification with category-specific decision records, organizational compliance documentation, integration guidance, and multi-category validation report

### Stage 4: Holistic Quality Assessment
**Module**: [Holistic Quality Assessment](task-modules/04-holistic-quality.md)
- **Purpose**: Comprehensive quality evaluation and iterative improvement
- **Key Activities**: Quality scoring, gap analysis, iterative refinement
- **Deliverables**: Quality-validated specification package (90/100+ threshold)

### Stage 5: Security Assessment
**Module**: [Security Assessment](task-modules/05-security-assessment.md)
- **Purpose**: Threat modeling and security controls integration
- **Key Activities**: Threat model generation, security controls design, risk assessment
- **Deliverables**: Comprehensive threat model with integrated security controls

### Stage 6: Documentation Generation
**Module**: [Documentation Generation](task-modules/06-documentation-generation.md)
- **Purpose**: Generate prescriptive guidance and executive summaries
- **Key Activities**: MCP prescriptive guidance generation, executive summary creation
- **Deliverables**: MCP prescriptive guidance document, executive summary

### Stage 7: Output Organization
**Module**: [Output Organization](task-modules/07-output-organization.md)
- **Purpose**: Project folder structure and deliverable organization
- **Key Activities**: File organization, deliverable packaging, handoff preparation
- **Deliverables**: Organized project folder with all deliverables structured for handoff

### Stage 8+: Feedback Integration (Iterative)
**Module**: [Incorporate Feedback](task-modules/08-incorporate-feedback.md)
- **Purpose**: Stakeholder feedback analysis and iterative specification improvement
- **Key Activities**: Change detection and conflict analysis, user-guided conflict resolution, impact analysis, intelligent specification merging, complete project folder regeneration, iteration management
- **Deliverables**: Complete project iteration folders incorporating stakeholder feedback with regenerated deliverables and complete traceability

## Key Features

### Progressive Quality Validation
Each stage includes built-in quality checks and acceptance criteria, culminating in comprehensive holistic assessment in Stage 4. This approach ensures quality gates at each step while enabling final optimization of the complete specification package.

### Intelligence Hub Integration
Optional Intelligence Hub integration in Stage 3 provides expert-guided architecture recommendations with optional deep research capabilities for enhanced analysis and insights.

### Context-Driven Execution
All stages adapt execution approach based on available context sources, ensuring appropriate methodology whether starting from existing documents, scratch, or mixed inputs.

### Quality Gate Enforcement
Each stage includes specific acceptance criteria that must be met before progression, ensuring cumulative quality improvement throughout the workflow.

## Usage Recommendations

**Enterprise Projects**: Execute complete 7-stage workflow for comprehensive specification development
**Complex Specifications**: Focus on Stage 4 quality iterations for thorough refinement
**Security-Critical Systems**: Emphasize Stage 5 threat modeling and security integration
**Development Handoff**: Ensure Stage 7 completion for proper deliverable organization
**Iterative Refinement**: Use Stage 8+ feedback integration for stakeholder-driven continuous improvement

## Task Checklist

- [ ] **Session Management and Workflow Initialization**
  - [ ] LOAD [Session Management](task-modules/00-session-management.md) → COMPLETE its Task Checklist
  - [ ] Follow session management protocols for execution mode detection and handoff
  - [ ] Verify all context sources are properly established

- [ ] **Stage-by-Stage Execution (MANDATORY: Load Each Task Module → Complete Its Task Checklist)**
  - [ ] **Stage 0**: LOAD [Project Analysis](task-modules/01-project-analysis.md) → COMPLETE its Task Checklist
  - [ ] **Stage 1**: LOAD [Requirements Generation](task-modules/02-requirements-generation.md) → COMPLETE its Task Checklist  
  - [ ] **Stage 2**: LOAD [Architecture Generation](task-modules/03-architecture-generation.md) → COMPLETE its Task Checklist
  - [ ] **Stage 3**: LOAD [Holistic Quality Assessment](task-modules/04-holistic-quality.md) → COMPLETE its Task Checklist
  - [ ] **Stage 4**: LOAD [Security Assessment](task-modules/05-security-assessment.md) → COMPLETE its Task Checklist
  - [ ] **Stage 5**: LOAD [Documentation Generation](task-modules/06-documentation-generation.md) → COMPLETE its Task Checklist
  - [ ] **Stage 6**: LOAD [Output Organization](task-modules/07-output-organization.md) → COMPLETE its Task Checklist
  - [ ] **Stage 7+**: LOAD [Incorporate Feedback](task-modules/08-incorporate-feedback.md) → COMPLETE its Task Checklist (when feedback provided)

- [ ] **Critical Execution Rules Compliance**
  - [ ] NEVER execute tasks based on summaries in this file
  - [ ] ALWAYS read the complete task module file before starting any stage
  - [ ] ALWAYS complete the Task Checklist at the end of each task module
  - [ ] ALWAYS follow Input Source Discovery Protocol for each task
  - [ ] ONLY proceed to next stage after completing current stage's Task Checklist
  - [ ] Update .workflow-state/design-handoff.md after each task completion per session management protocols
  - [ ] NEVER invent information not present in context sources