# Design Agent Workflow - Design Document

## Architecture Overview

This workflow implements an orchestrated process with modular task architecture that transforms project documents into enterprise-grade specification packages through systematic progression across multiple stages.

Each stage has focused objectives and clear quality gates, progressing from initial session management through requirements generation, dual-path architecture design, holistic quality assessment, comprehensive security evaluation, and final output organization.

## Modular Task Architecture

The workflow is organized into focused, modular task files for better organization and clarity:

- **Stage 0: Session Management Module** - Execution modes, handoff protocols, and session recovery
- **Stage 1: Project Analysis Module** - Project complexity assessment and workflow recommendations  
- **Stage 2: Requirements Generation Module** - Input assessment and requirements package generation
- **Stage 3: Architecture Generation Module** - Dual-path architecture design with Intelligence Hub integration
- **Stage 4: Holistic Quality Assessment Module** - Comprehensive quality evaluation and iterative improvement
- **Stage 5: Security Assessment Module** - Threat modeling and security controls integration
- **Stage 6: Documentation Generation Module** - MCP prescriptive guidance and executive summary generation
- **Stage 7: Output Organization Module** - Project folder structure and deliverable organization requirements
- **Stage 8+: Feedback Integration Module** - Stakeholder feedback analysis and iterative improvement task generation

## Enhanced Project Input System Architecture

### Input Category Framework

The input system processes project materials in two distinct phases to maintain proper separation between requirements and architecture concerns.

## Requirements Generation Phase (Stage 2)

Processes three categories of project materials to establish pure business-driven requirements:

#### Category 1: Project Context (`project-doc/project-context/`)
**Purpose**: Project-specific requirements, business context, and stakeholder needs
**Processing Logic**:
- Extract core business objectives and functional requirements
- Identify user personas, workflows, and success criteria
- Document project-specific constraints and technical preferences
- Generate primary functional and non-functional requirements
**Output**: Core project requirements that define "what we're building"

#### Category 2: Technical Knowledge (`project-doc/technical-knowledge/`)
**Purpose**: External reference materials and integration specifications
**Processing Logic**:
- Analyze external API documentation without treating as build targets
- Extract integration patterns, data formats, and authentication requirements
- Identify service limits, rate limits, and compatibility constraints
- Document how external systems influence architecture decisions
**Output**: Integration requirements that define "what we're integrating with"

#### Category 3: Organization Context (`project-doc/organization-context/`)
**Purpose**: Company policies, standards, and organizational constraints
**Processing Logic**:
- Extract naming conventions, tagging strategies, and resource patterns
- Apply security policies, compliance requirements, and budget constraints
- Enforce organizational standards across all architecture decisions
- Validate against company-specific requirements (MAP credits, cost allocation)
**Output**: Organizational constraints that define "how we must build"

## Architecture Generation Phase (Stage 3)

Incorporates reference system analysis to inform architecture decisions:

#### Project Code Analysis (from Stage 1 output)
**Purpose**: Existing codebases and reference system analysis
**Processing Logic**:
- Use comprehensive codebase analysis from Stage 1 (stored in `.workflow-state/reference-architectures/`)
- Identify reusable components and integration opportunities
- Document existing system dependencies and integration requirements
- Generate integration strategies and compatibility requirements
**Output**: Reference system considerations that inform "how we can leverage existing assets"

### Context Separation Engine

**Classification Logic**:
- Folder-based automatic categorization prevents content misinterpretation
- Clear boundaries between project scope and external dependencies
- Organizational constraints applied consistently across all decisions
- Reference system analysis separated from requirements generation

**Traceability Framework**:
- Requirements linked to specific input categories and source documents (project-context, technical-knowledge, organization-context only)
- Architecture decisions traced to requirements plus reference system analysis
- Compliance documentation showing organizational policy application
- Integration specifications clearly separated from build requirements

### Processing Workflow Integration

**Stage 0-1 Integration**: Input discovery, categorization, and project-code analysis during session management and project analysis
**Stage 2 Integration**: Three-category processing during requirements generation (project-context, technical-knowledge, organization-context)
**Stage 3 Integration**: Requirements-driven architecture generation informed by reference system analysis from Stage 1
**Stage 4-7 Integration**: Category-specific validation during quality assessment and final documentation

## Stage Architecture

### Stage 0: Session Management
**Objective**: Establish workflow context and execution mode

**Key Activities**:
- Execution mode detection (new session, continuation, recovery)
- Customer context capture (project goals, technical preferences, organizational context)
- Workflow state initialization (`.workflow-state/design-handoff.md`, `.workflow-state/customer-context.md`)
- Context source establishment (project-doc folder, customer context, current prompt)

**Quality Gates**:
- Customer context captured and documented
- Workflow state files initialized
- Context sources identified and accessible
- Execution mode determined

### Stage 1: Project Analysis
**Objective**: Assess project complexity and provide workflow recommendations

**Key Activities**:
- Input source assessment (existing documents vs scratch vs mixed)
- Document analysis (count, size, types)
- Complexity categorization (Simple/Moderate/Complex/Enterprise)
- Time estimation and workflow recommendations
- Session management strategy guidance

**Quality Gates**:
- Input scenario determined
- Clear complexity categorization documented
- Workflow recommendations provided
- Session strategy defined

### Stage 2: Requirements Generation
**Objective**: Transform project inputs into structured requirements packages based purely on business needs, integration requirements, and organizational constraints

**Three-Category Input Processing Architecture**:

**Requirements-Focused Input Analysis**:
- **project-context/**: Project-specific requirements, business context, and stakeholder needs
- **technical-knowledge/**: External reference materials, API documentation, and integration specifications
- **organization-context/**: Company policies, standards, compliance requirements, and organizational constraints

**Context Classification Engine**:
- Automatic categorization of input materials by folder structure
- Clear separation between "what we're building" vs "what we're integrating with" vs "organizational constraints" 
- Prevention of misinterpretation of external references as project build targets
- Traceability matrix linking requirements to specific input categories and source documents
- **No influence from existing code patterns** - requirements driven purely by business needs

**Category-Specific Processing Logic**:

**Project Context Processing**:
- Extract business objectives, functional requirements, and user stories
- Identify stakeholder needs and success criteria
- Document project-specific constraints and preferences
- Generate core functional and non-functional requirements

**Technical Knowledge Processing**:
- Analyze external API documentation to extract integration requirements
- Identify service limits, rate limits, and technical constraints from external systems
- Document authentication patterns, data formats, and compatibility requirements
- Generate integration specifications without treating external systems as build targets

**Organization Context Processing**:
- Extract naming conventions, tagging strategies, and resource organization patterns
- Apply AWS resource tagging requirements for cost allocation and MAP credits
- Enforce security policies, encryption standards, and access control patterns
- Validate budget limits and cost optimization requirements
- Generate organizational compliance requirements and policy constraints

**Components Generated**:
- Three-category input assessment analysis with context separation
- Project requirements documentation (functional, non-functional) from project-context
- Integration requirements specification from technical-knowledge analysis
- Organizational compliance requirements from organization-context processing
- Category-specific traceability matrices linking requirements to input sources
- Gap analysis with category-specific missing information identification
- Generation readiness assessment across the three requirements categories

**Quality Gates**:
- All requirements traceable to specific input categories and source documents
- Clear separation maintained between project requirements and external integration needs
- Organizational policies and standards properly extracted and applied as constraints
- Requirements driven purely by business needs without existing code bias
- Complete requirements package structure with category-specific organization
- Basic completeness validation across the three requirements categories

### Stage 3: Architecture Generation
**Objective**: Generate comprehensive architecture design based on stable requirements using dual-path approach

**Dual-Path Architecture**:

**Task 3.1: Intelligence Hub Availability Assessment**
- Check MCP configuration for Intelligence Hub server
- Verify connection and availability
- Document path selection (A or B) in workflow state
- Set execution parameters

**Task 3.2: Architecture Generation Execution**

**Path A: Intelligence Hub Integration** (when available)
- Present deep research decision to user (standard 15 min vs deep 60 min)
- Submit job with requirements and deep research flag
- Monitor status (SUBMITTED → PROCESSING → EXPERT_COMPLETED → COMPLETED)
- Retrieve and save complete JSON response to `architecture/intelligence-hub-response.md`
- Integrate expert insights and asset rankings (60% threshold for technology shortlisting)

**Path B: Standard Architecture Generation** (when Intelligence Hub is unavailable)
- Load customer context from `.workflow-state/customer-context.md`
- Apply architecture guidance selection framework with organizational constraints from organization-context
- Extract and document repository links from technical-knowledge materials
- Download external reference architectures to `.workflow-state/reference-architectures/`
- **Integrate multi-category requirements**: project-context (core requirements), technical-knowledge (integration needs), organization-context (policy constraints), project-code (legacy considerations)
- **Perform comprehensive gap analysis**: existing systems + external references + organizational policies vs. project requirements
- **Apply organizational standards**: naming conventions, tagging strategies, security policies from organization-context throughout architecture design

**Task 3.3: Common Architecture Activities** (path convergence)
- Design system architecture incorporating requirements and reference analysis:
  - Core components from project-context requirements
  - Integration patterns and external system interfaces from technical-knowledge
  - Organizational compliance (naming, tagging, security) from organization-context
  - Reference system integration opportunities from Stage 1 project-code analysis
- Create Architecture Decision Records (ADRs) documenting requirements influence and reference system considerations
- Document technical specifications with clear traceability to requirements and reference analysis
- Apply organizational policies consistently across all architecture components
- Balance new requirements with existing system integration opportunities

**Task 3.4: Architecture Integration Validation**
- Requirements coverage analysis (95%+ threshold)
- Component integration validation (interface compatibility, data flow)
- **Service Limits Impact Assessment**:
  - Extract AWS service inventory from architecture
  - Research current service limits using AWS documentation
  - Perform usage estimation for POC and production scenarios
  - Identify high-risk limits and document mitigation strategies
  - Plan service limit increase requests where needed
- Technical feasibility assessment
- Documentation completeness review
- Generate validation score (≥85/100 required)
- Output: `supplement-material/architecture-integration-validation.md`

**Components Generated**:
- System architecture with multi-category component specifications:
  - Core system components addressing project-context requirements
  - Integration interfaces for technical-knowledge external systems
  - Organizational compliance implementations (tagging, naming, security)
  - Reference system integration components
- Architecture decision records with category-specific influence traceability
- Technical specifications with clear input category source documentation
- Implementation planning incorporating organizational standards and reference system constraints
- Intelligence Hub response (Path A) or comprehensive multi-category reference analysis (Path B)
- Gap analysis covering project requirements, external integrations, organizational policies, and reference systems
- Architecture integration validation report with service limits and compliance assessment

**Quality Gates**:
- Complete architecture design documented
- Requirements coverage validated (95%+)
- Service limits assessed and mitigation strategies documented
- Architecture integration validation score ≥85/100
- All ADRs complete with rationale

### Stage 4: Holistic Quality Assessment
**Objective**: Achieve 90/100 quality score through systematic holistic improvement

**CRITICAL SECURITY BOUNDARY**: Stage 4 focuses on basic security requirements and patterns only. Comprehensive threat modeling and security controls are created in Stage 5.

**Output Organization**: All outputs organized in single project folder with structured layout:
```
generated/design/
├── specification-package-iteration-1/  (original generated package)
├── specification-package-iteration-2/  (first improved package)
├── specification-package-iteration-3/  (second improved package, if needed)
├── score-sheet-iteration-1.md         (initial assessment)
├── score-sheet-iteration-2.md         (second iteration scoring)
├── score-sheet-iteration-3.md         (third iteration scoring, if needed)
└── supplement-material/                (input analysis and supporting docs)
    ├── input-assessment-analysis.md
    ├── mcp-prescriptive-guidance.md
    └── [other supporting documents]
```

**Note**: threat-model/ folder is created in Stage 5, not Stage 4.

**Deferred Quality Strategy**:
- Requirements and architecture generated first (Stages 1-2)
- Holistic optimization of both domains together
- Cross-domain improvements for better outcomes
- Reduced context switching and improved efficiency

**Enhanced Quality Framework**:
- **Requirements Analysis** (25%): Completeness across all four input categories, clarity, category-specific traceability
- **Architecture & Design** (25%): Patterns, components, multi-category integration, organizational compliance
- **Security & Compliance** (20%): **BASIC SECURITY ONLY** - security requirements validation, architectural security patterns, security readiness assessment (NO comprehensive threat modeling)
- **Implementation & Operations** (15%): Development strategy, operational excellence, reference system integration
- **Business Value & Risk** (15%): Value proposition, risk assessment, organizational alignment

**Iteration Rules**:
- Modified files get "-improved" suffix
- Unchanged files copied from previous iteration
- Continue until 90/100 score achieved (max 5 iterations)
- Each iteration produces complete specification package

### Stage 5: Security Assessment
**Objective**: Integrate comprehensive security assessment

**BUILDS ON STAGE 4**: Creates comprehensive security documentation building on basic security requirements validated in Stage 4.

**Security Framework**:
- AWS threat modeling template structure
- STRIDE-based threat identification
- Baseline Security Controls (BSC) mapping
- Security testing framework with test cases
- Threat actor profiles and anti-patterns

**Output Organization**: Adds threat-model/ folder to project structure:
```
generated/design/
├── [existing files from Stage 4]
├── threat-model/                       (comprehensive security assessment - CREATED IN STAGE 5)
│   ├── threat-analysis.md
│   ├── security-controls.md
│   ├── testing-framework.md
│   └── implementation-guidance.md
└── [existing supplement-material/]
```

**Quality Gates**:
- Complete threat model with STRIDE analysis
- Security controls mapped to all identified threats
- Security testing framework with concrete test cases
- Implementation guidance provided

### Stage 6: Documentation Generation
**Objective**: Generate prescriptive guidance and executive summaries

**Key Activities**:
- Tools prescriptive guidance generation with comprehensive MCP servers and Skills inventory
- Project-specific MCP and Skills recommendations with usage patterns
- Executive summary creation synthesizing final specification package
- Stakeholder communication materials and implementation readiness assessment

**Components Generated**:
- MCP prescriptive guidance document in supplement material
- Executive summary at project root level
- Implementation guidance and recommendations
- Stakeholder communication materials

**Quality Gates**:
- Complete MCP server inventory and recommendations
- Comprehensive executive summary reflecting final quality scores
- Clear implementation guidance and next steps
- Professional stakeholder communication materials

### Stage 7: Output Organization
**Objective**: Validate folder structure and prepare final handoff

**Key Activities**:
- Project structure initialization and validation
- Iterative content management (iteration folders, score sheets)
- Specialized content organization (threat model, supplement material)
- Final handoff preparation with executive summary

**Output Structure Validation**:
```
generated/design/
├── specification-package-iteration-1/
├── specification-package-iteration-X/
├── score-sheet-iteration-1.md
├── score-sheet-iteration-X.md
├── executive-summary.md
├── threat-model/
│   ├── threat-analysis.md
│   ├── security-controls.md
│   ├── testing-framework.md
│   └── implementation-guidance.md
└── supplement-material/
    ├── input-assessment-analysis.md
    ├── gap-analysis.md (if applicable)
    ├── integration-design.md (if applicable)
    └── architecture-integration-validation.md
```

**Quality Gates**:
- Folder structure matches defined requirements
- All required files and folders present
- File naming conventions followed
- Executive summary complete
- Handoff documentation ready

### Stage 8+: Feedback Integration (Iterative)
**Objective**: Incorporate stakeholder feedback through systematic analysis, conflict detection, and iterative improvement

**Key Activities**:
- Stakeholder feedback collection from `project-doc/feedback/iteration-N/` folders
- **Change detection and content fingerprinting** to identify new, modified, and unchanged inputs
- **Conflict detection system** using semantic analysis to identify contradictions between feedback and existing decisions
- **User-guided conflict resolution** with resolution options and impact analysis
- Comprehensive feedback analysis and categorization (requirements, architecture, security, quality)
- **Incremental processing** to analyze only changed inputs and reuse cached analysis
- Dynamic improvement task generation following coding agent's Task 1 pattern
- **Intelligent specification merging** with change annotations and version tracking
- Complete project folder regeneration with new iteration folders
- Traceability maintenance linking feedback to specific improvements with changelog documentation

**Feedback Processing Architecture**:

**Task N.1: Change Detection and Analysis**
- **Content fingerprinting** using SHA-256 hashing to identify new, modified, and unchanged inputs
- **Processing history management** in `.workflow-state/processing-history.md`
- **Change categorization**: NEW, MODIFIED, REMOVED, UNCHANGED files
- **Change summary generation** documenting processing strategy and time savings
- **Incremental mode activation** when changes detected

**Task N.2: Conflict Detection and Resolution**
- **Semantic conflict detection** comparing new feedback against existing requirements and decisions
- **Conflict categorization**: Direct contradiction, implicit conflict, scope conflict, technical conflict
- **Conflict report generation** with resolution options and impact analysis
- **User-guided resolution workflow** with pause-and-resolve mechanism
- **Resolution documentation** with rationale and decision tracking

**Task N.3: Impact Analysis and Specification Merging**
- **Change impact analysis** across requirements, architecture, security, and implementation dimensions
- **Severity classification**: Critical, Major, Minor, Informational
- **Intelligent specification merging** with change annotations and version tracking
- **Previous iteration loading** and selective updates based on change analysis
- **Effort estimation** and risk assessment for all changes

**Task N.4: Complete Project Regeneration**
- Systematic updates to requirements, architecture, security, and documentation components
- Creation of new complete project iteration folder (project-name-iteration-N+1)
- Regeneration of all deliverables: specification-package, score-sheet, executive-summary, threat-model, supplement-material
- **Changelog generation** documenting specific changes from previous iteration with feedback traceability
- **Version history tracking** in `.workflow-state/version-history.md`
- Quality validation of all updated components

**Task N.5: Iteration Completion**
- Final validation of feedback incorporation across all deliverables
- Quality score reassessment for complete updated project folder
- **Processing history update** with current file fingerprints
- Stakeholder communication of changes made with changelog reference
- Preparation for potential additional feedback cycles

**Feedback Workflow States**:
- **Complete**: Initial workflow finished, ready for feedback
- **Gathering Feedback**: Feedback folder created, awaiting stakeholder input
- **In Progress**: Processing feedback and executing improvement tasks
- **Complete**: Feedback incorporated, ready for next cycle or implementation

**Quality Gates**:
- All feedback documents analyzed and categorized
- **Change detection completed** with accurate fingerprinting and categorization
- **Conflicts identified and resolved** through user-guided resolution process
- **Impact analysis completed** with severity classification and effort estimation
- Improvement tasks generated with clear scope and traceability
- **Incremental processing efficiency** achieved (target: <50% of full regeneration time)
- New complete project iteration folder created with all deliverables updated
- Quality standards maintained or improved across all updated deliverables
- **Complete audit trail** of feedback incorporation maintained with changelog documentation and version history

## Problem-Solution Mapping

### 1. Context Loss → Session Management
**Problem**: Workflow context lost between sessions or execution modes
**Solution**: Dedicated session management stage with customer context capture and workflow state initialization

### 2. Incomplete Requirements → Systematic Requirements Generation
**Problem**: Teams proceed with poorly structured requirements and lack understanding of existing systems
**Solution**: Dedicated requirements generation stage with comprehensive input assessment, brownfield codebase analysis, and traceability matrix

### 3. Poor Architecture Quality → Dual-Path Architecture Design
**Problem**: Architecture decisions lack rationale and technical depth
**Solution**: Dual-path architecture generation with Intelligence Hub integration (Path A) or systematic standard generation (Path B), both with comprehensive validation

### 4. Service Limits Risks → Proactive Service Limits Assessment
**Problem**: Implementation failures due to AWS service quota constraints
**Solution**: Comprehensive service limits impact assessment in architecture validation with mitigation strategies

### 5. Fragmented Quality Assessment → Holistic Quality Optimization
**Problem**: Requirements and architecture optimized in isolation leading to suboptimal outcomes
**Solution**: Deferred quality assessment optimizing requirements and architecture together

### 6. Security Gaps → Integrated Threat Modeling
**Problem**: Security added as afterthought
**Solution**: AWS-compliant threat modeling with STRIDE methodology and actionable mitigations

### 7. Disorganized Deliverables → Structured Output Organization
**Problem**: Scattered files and inconsistent organization
**Solution**: Dedicated output organization stage with validated folder structure and handoff preparation

### 8. Complex Navigation → Modular Task Architecture
**Problem**: Large monolithic task files difficult to navigate and maintain
**Solution**: Focused task modules with clear organization and easy navigation

### 9. Reference System Integration → Brownfield Analysis Framework
**Problem**: Existing codebases and reference systems not properly analyzed for integration
**Solution**: Comprehensive brownfield analysis methodology with codebase assessment and integration evaluation

### 10. External Reference Misinterpretation → Context Classification Engine
**Problem**: External API documentation and reference materials misinterpreted as project build targets
**Solution**: Four-category input system with automatic classification preventing confusion between "what we're building" vs "what we're integrating with"

### 11. Inconsistent Organizational Standards → Policy-Driven Architecture
**Problem**: Organizational policies and standards inconsistently applied across projects
**Solution**: Organization-context processing that automatically applies naming conventions, tagging strategies, security policies, and compliance requirements

### 12. Context Mixing and Confusion → Multi-Category Input Framework
**Problem**: Project requirements, external integrations, organizational constraints, and reference system considerations mixed together causing specification confusion
**Solution**: Structured four-folder input system with category-specific processing logic and clear traceability

### 13. Static Specification Delivery → Iterative Feedback Integration
**Problem**: Specifications delivered as final products without mechanism for stakeholder feedback and iterative improvement
**Solution**: Feedback-in-the-loop architecture enabling unlimited feedback cycles with systematic analysis, dynamic task generation, and iterative specification refinement

### 14. Manual Change Tracking → Automated Conflict Detection
**Problem**: Manual identification of conflicts between new feedback and existing decisions leads to missed contradictions and inconsistent specifications
**Solution**: Automated conflict detection system using semantic analysis, content fingerprinting, and intelligent change categorization with user-guided resolution workflow

### 15. Full Regeneration Inefficiency → Incremental Processing
**Problem**: Processing all inputs from scratch for each feedback iteration wastes time and computational resources
**Solution**: Incremental processing system with content fingerprinting, change detection, and selective analysis of only new/modified inputs while reusing cached results

## Conflict Tracking and Resolution Architecture

### Change Detection Engine

**Purpose**: Identify new, modified, and unchanged inputs to enable incremental processing and conflict detection

**Components**:

#### Content Fingerprinting System
- **Algorithm**: SHA-256 hashing of file contents for change detection
- **Storage**: `.workflow-state/processing-history.md` with file fingerprints and metadata
- **Change Categorization**: NEW, MODIFIED, REMOVED, UNCHANGED files
- **Processing Strategy**: Incremental analysis of only changed inputs

#### Change Summary Generation
```markdown
# Change Summary - Iteration X

## New Files (3)
- `project-doc/feedback/customer-meeting-2025-01-20.md`
- `project-doc/project-context/new-requirements.md`

## Modified Files (2)
- `project-doc/project-context/requirements.md`
  - Previous: sha256:abc123...
  - Current: sha256:xyz789...

## Processing Strategy
- Incremental processing enabled
- Reuse previous analysis for 15 unchanged files
- Analyze 3 new files and 2 modified files
```

### Conflict Detection System

**Purpose**: Identify contradictions between new feedback and existing decisions using semantic analysis

**Conflict Types**:
- **Direct Contradiction**: New feedback explicitly contradicts previous requirement
- **Implicit Conflict**: New feedback implies different approach than existing architecture
- **Scope Conflict**: New feedback changes project boundaries
- **Technical Conflict**: New feedback requires incompatible technology choices

#### Semantic Conflict Detector
1. Extract requirements and constraints from new feedback
2. Compare against existing requirements using semantic analysis
3. Identify contradictions using pattern matching and constraint analysis
4. Generate conflict reports with resolution options

#### Conflict Report Generation
```markdown
# Conflicts Report - Iteration X

## Conflict 1: Authentication Method [CRITICAL]

### Original Decision (Iteration 1)
**Requirement:** FR-001 - Users shall authenticate using OAuth 2.0
**Source:** project-doc/project-context/requirements.md
**Rationale:** Customer requested social login integration

### New Feedback (Iteration 2)
**Requirement:** Users shall authenticate using SAML 2.0 for enterprise SSO
**Source:** project-doc/feedback/customer-meeting-2025-01-20.md
**Rationale:** Customer IT security requires SAML for compliance

### Conflict Analysis
- **Type:** Direct Contradiction
- **Severity:** CRITICAL
- **Impact:** Complete authentication architecture redesign required

### Resolution Options
1. **Accept New (SAML 2.0)** - Meets compliance, requires redesign
2. **Keep Original (OAuth 2.0)** - No rework, doesn't meet compliance
3. **Merge Both** - Maximum flexibility, increased complexity

### Recommended Resolution
**Option 1: Accept New (SAML 2.0)**
**Rationale:** Compliance requirements are non-negotiable
```

### Conflict Resolution Workflow

**Process**:
1. **Detect conflicts** during change analysis
2. **Generate conflict report** with resolution options and impact analysis
3. **PAUSE WORKFLOW** - Present conflicts to user with clear options
4. **Wait for user decision** on each conflict with rationale
5. **Apply selected resolutions** and document decision rationale
6. **Continue with specification updates** incorporating resolved conflicts

### Change Impact Analysis System

**Purpose**: Assess how changes affect existing specifications across all dimensions

**Analysis Dimensions**:
- **Requirements Impact**: Which requirements are affected
- **Architecture Impact**: Which components need redesign
- **Security Impact**: Which threat mitigations are affected
- **Implementation Impact**: Effort required to implement changes

**Severity Classification**:
- **Critical**: Fundamental architecture changes required
- **Major**: Significant component redesign needed
- **Minor**: Localized updates required
- **Informational**: Documentation updates only

#### Impact Report Generation
```markdown
# Change Impact Analysis - Iteration X

## Executive Summary
- Total Changes: 5 new requirements, 3 modified, 1 removed
- Severity: 1 Critical, 2 Major, 2 Minor
- Estimated Effort: HIGH (3-4 weeks additional work)
- Architecture Redesign Required: Yes (authentication component)

## Detailed Impact Analysis

### Impact 1: Authentication Architecture Redesign [CRITICAL]
**Trigger:** Conflict resolution - Switch from OAuth to SAML
**Affected Components:**
- Requirements: FR-001, FR-002, FR-003
- Architecture: Identity Management Component
- ADRs: ADR-003 (superseded), ADR-015 (new)
- Security: TM-001, SC-001

**Changes Required:**
1. Redesign authentication flow for SAML
2. Update API Gateway authorizer
3. Revise security threat model
4. Update integration requirements

**Effort Estimate:** HIGH (2 weeks)
**Risk Level:** MEDIUM
```

### Incremental Processing System

**Purpose**: Process only new/changed inputs to minimize execution time while maintaining quality

**Architecture**:

#### Analysis Cache Manager
- **Location**: `.workflow-state/previous-input-assessment.md`
- **Content**: Complete input assessment analysis from previous iteration
- **Usage**: Load and reuse analysis for unchanged files

#### Differential Analyzer
- **For Modified Files**: Line-by-line diff analysis to extract only new/changed information
- **For New Files**: Full analysis with integration into existing analysis
- **For Removed Files**: Impact assessment and dependency identification

#### Processing Efficiency Metrics
- Files processed: X new + Y modified (Z total files)
- Files reused: N unchanged
- Time saved: Estimated X minutes vs full regeneration
- Analysis cache hit rate: N%

### Version Management System

**Purpose**: Maintain complete audit trail of specification evolution with conflict resolution history

#### Version History Tracking
```markdown
# Specification Version History

## Iteration 1 - 2025-01-15 14:30:00
**Type:** Initial Generation
**Quality Score:** 92/100
**Status:** Approved by customer

## Iteration 2 - 2025-01-20 16:45:00
**Type:** Feedback Integration
**Input Files:** 3 new, 2 modified, 1 removed
**Conflicts:** 1 critical conflict resolved (OAuth → SAML)
**Quality Score:** 91/100
**Status:** Pending customer review
```

#### Changelog Generation
```markdown
# Changelog: Iteration 1 → Iteration 2

## Conflicts Resolved (1)
- **Authentication Method**: OAuth 2.0 → SAML 2.0
  - **Resolution:** Accept new requirement
  - **Rationale:** Compliance requirements non-negotiable
  - **Impact:** Authentication architecture redesign

## Requirements Changes
### Added Requirements (5)
- **FR-015**: Payment Processing with Stripe API v2
- **FR-016**: Multi-factor Authentication

### Modified Requirements (3)
- **FR-001**: User Authentication
  - Before: OAuth 2.0 authentication
  - After: SAML 2.0 authentication with enterprise SSO
  - Rationale: Customer compliance requirements
```

## Orchestration Patterns

### Session Management Coordination
- **Execution Mode Detection**: New session, continuation, or recovery
- **Context Capture**: Customer goals, technical preferences, organizational context
- **State Initialization**: Workflow state and customer context files
- **Handoff Protocols**: Seamless workflow progression across stages

### Project Analysis Coordination
- **Input Assessment**: Existing documents vs scratch vs mixed scenarios
- **Complexity Assessment**: Document analysis and categorization
- **Strategy Recommendation**: Execution mode and session management guidance
- **Risk Identification**: Early identification of potential challenges

### Requirements Generation Coordination
- **Multi-Category Input Management**: Systematic processing across project-context, technical-knowledge, organization-context, and project-code folders
- **Context Classification**: Automatic separation of project requirements, external integrations, organizational constraints, and legacy considerations
- **Integration Requirements Extraction**: Analysis of external reference materials to derive integration needs without misinterpretation as build targets
- **Policy Application**: Consistent application of organizational standards, naming conventions, and compliance requirements
- **Brownfield Analysis**: Systematic reference system assessment and integration evaluation with compatibility planning
- **Structure Adherence**: Category-specific requirements package frameworks with clear traceability
- **Foundation Establishment**: Stable multi-category requirements foundation for architecture design 

### Architecture Generation Coordination
- **Path Selection**: Intelligence Hub availability assessment and path determination
- **Path A Execution**: Deep research decision, job submission, expert insights integration with multi-category requirements
- **Path B Execution**: Guidance selection, reference architecture analysis, context-aware design incorporating all four input categories
- **Path Convergence**: Common architecture activities integrating project requirements, external integrations, organizational policies, and reference system constraints
- **Multi-Category Design Integration**: Architecture aligned with requirements from all four input categories
- **Policy Enforcement**: Automatic application of organizational standards throughout architecture design
- **Decision Documentation**: Category-specific influence traceability in ADRs showing which input category influenced each decision
- **Comprehensive Validation**: Requirements coverage across all categories, integration feasibility, service limits, organizational compliance
- **Service Limits Assessment**: Proactive AWS quota analysis with organizational constraint consideration

### Holistic Quality Assessment Coordination
- **Cross-Domain Optimization**: Requirements and architecture improved together
- **Assessment Management**: Multi-dimensional quality evaluation
- **Progress Tracking**: Score progression and issue resolution
- **Quality Threshold Enforcement**: Mandatory 90/100 standard

### Security Assessment Coordination
- **Context Integration**: Complete specification information for threat modeling
- **Standards Compliance**: AWS security requirements and BSC mapping
- **Mitigation Focus**: Actionable security controls and implementation guidance
- **Testing Framework**: Concrete security test cases and validation procedures

### Output Organization Coordination
- **Structure Validation**: Folder structure compliance with defined requirements
- **Iteration Management**: Sequential specification packages with proper naming
- **Content Organization**: Threat model, supplement material, score sheets
- **Handoff Preparation**: Executive summary and final deliverable packaging

### Modular Task Coordination
- **Clear Organization**: Each workflow stage organized in focused modules
- **Session Management**: Consistent handoff protocols across modules
- **Progress Tracking**: Unified progress tracking across modular tasks
- **Context Sources**: Standardized context loading from workflow state files

## Quality Assurance Framework

### Multi-Dimensional Assessment
Each specification package evaluated across 5 weighted categories with detailed scoring and feedback for systematic improvement.

### Iteration Management
- Standalone score sheets for transparency
- Complete specification packages for each iteration
- Clear improvement tracking and issue resolution
- Maximum 5 iterations to reach quality threshold

### Implementation Readiness Validation
- Minimum 90/100 quality score achieved
- All critical issues addressed and resolved
- Comprehensive security posture defined
- Stakeholder and development team approval

## Success Criteria

### Process Success
- Complete specification package with all components
- 90/100+ quality score across all dimensions
- Comprehensive threat model with actionable mitigations
- Clear audit trail of improvements and decisions

### Implementation Readiness
- Requirements traceable to business objectives
- Architecture decisions with rationale and alternatives
- User stories with implementation guidance
- Security controls mapped to specific threats
- Development team validation of feasibility

## Escalation Triggers

**PAUSE AND Escalate to user When**:
- Critical information gaps prevent quality assessment
- Fundamental architectural or feasibility issues identified
- Security requirements conflict with functional constraints
- Quality threshold not achievable within iteration limits
- Stakeholder requirements conflict with technical limitations