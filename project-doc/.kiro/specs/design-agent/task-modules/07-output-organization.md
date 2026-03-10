# Output Organization Requirements

## Overview

This module defines the mandatory folder structure and organization requirements for all Design Agent workflow outputs. Proper organization ensures consistency, traceability, and ease of handoff to development teams.

## Project Folder Structure

**CRITICAL**: All workflow outputs must be organized in a SINGLE project folder with quality iteration subfolders:

```
generated/design/
└── [project-name]/                     (SINGLE project folder - name extracted from customer context)
    ├── README.md                           # This navigation guide
    ├── executive-summary.md                # Business-focused project summary
    ├── score-sheet-iteration-1.md         # Quality assessment results (initial)
    ├── score-sheet-iteration-2.md         # Quality assessment results (if quality iterations needed)
    ├── specification-package-iteration-1/  # Complete specification package (initial)
    │   ├── requirements/                   # Business and technical requirements
    │   │   ├── functional-requirements.md
    │   │   ├── non-functional-requirements.md
    │   │   └── requirements-traceability-matrix.md
    │   ├── user-stories/                   # Development stories and acceptance criteria
    │   │   └── user-stories.md
    │   ├── architecture/                   # System design and technical specifications
    │   │   ├── system-architecture.md
    │   │   └── technical-specifications.md
    │   └── architecture-decision-records/  # Architecture decisions and rationale
    │       ├── ADR-001-[decision-name].md
    │       └── ADR-00X-[decision-name].md
    ├── specification-package-iteration-2/  # Quality-improved package (if needed)
    │   ├── requirements/                   # Business and technical requirements
    │   │   ├── functional-requirements.md
    │   │   ├── non-functional-requirements.md
    │   │   └── requirements-traceability-matrix.md
    │   ├── user-stories/                   # Development stories and acceptance criteria
    │   │   └── user-stories.md
    │   ├── architecture/                   # System design and technical specifications
    │   │   ├── system-architecture.md
    │   │   └── technical-specifications.md
    │   └── architecture-decision-records/  # Architecture decisions and rationale
    │       ├── ADR-001-[decision-name].md
    │       └── ADR-00X-[decision-name].md
    ├── threat-model/                       # Security assessment and controls
    │   ├── threat-analysis.md              # STRIDE-based threat identification
    │   ├── security-controls.md            # Security implementation requirements
    │   ├── testing-framework.md            # Security testing procedures
    │   └── implementation-guidance.md      # Security implementation guidance
    └── supplement-material/                # Supporting analysis and guidance
        ├── input-assessment-analysis.md    # Analysis of input sources
        ├── tools-prescriptive-guidance.md  # Development tools recommendations (MCPs and Skills)
        ├── project-risk-analysis.md        # Project delivery risk assessment
        └── [additional analysis files]
```

**IMPORTANT DISTINCTION**:
- **Quality Iterations**: specification-package-iteration-1, specification-package-iteration-2, etc. (within same project)
- **Feedback Iterations**: Only create NEW project folders when stakeholder feedback requires complete project regeneration (Task 8+)

## Organization Rules

### Project Name Extraction
- **Source**: Extract project name from `.workflow-state/customer-context.md` or project documents
- **Format**: Use kebab-case (lowercase with hyphens): `knowledge-base-assistant`, `payment-system`, `user-portal`
- **Fallback**: If no clear project name, use `project-specification` as default
- **Validation**: Ensure name is filesystem-safe and descriptive

### Single Project Folder Structure
- **Container Principle**: All deliverables must be contained within the `generated/design/[project-name]/` folder
- **No Scattered Files**: No deliverables should be created outside the project folder structure
- **Consistent Path**: Project folder path is always `generated/design/[project-name]/`
- **Quality Iterations**: Multiple specification-package-iteration-X folders within same project folder

### Quality Iteration Numbering (Within Same Project)
- **Specification Packages**: specification-package-iteration-1, specification-package-iteration-2, etc.
- **Score Sheets**: score-sheet-iteration-1.md, score-sheet-iteration-2.md, etc.
- **Quality Threshold**: Continue iterations until 90/100 quality score achieved
- **Final Deliverables**: executive-summary.md, threat-model/, supplement-material/ created once at project level

### Feedback Iteration Numbering (New Project Folders - Task 8+ Only)
- **New Project Folders**: Only when stakeholder feedback requires complete project regeneration
- **Naming**: [project-name]-feedback-iteration-1/, [project-name]-feedback-iteration-2/, etc.
- **Trigger**: Explicit stakeholder feedback documents in project-doc/feedback/iteration-N/
- **Complete Regeneration**: Each feedback iteration creates entirely new project folder

### Score Sheet Placement
- **Project Root Level**: Score sheets placed at project root level: `generated/design/[project-name]/`
- **Iteration Numbering**: score-sheet-iteration-1.md, score-sheet-iteration-2.md, etc.
- **Standalone Documents**: Each score sheet provides comprehensive feedback for that quality iteration
- **Audit Trail**: Complete progression of scores maintained at project level for audit purposes

### Threat Model Folder
- **Dedicated Folder**: Dedicated folder for all security assessment deliverables
- **Comprehensive Coverage**: All threat modeling outputs contained within this folder
- **Structured Organization**: Logical organization of threat model components
- **Implementation Ready**: Security guidance ready for development team use

### Executive Summary
- **Project Root Level**: Single executive summary at project root: `generated/design/[project-name]/executive-summary.md`
- **Final Document**: Created after achieving 90/100 quality threshold
- **Comprehensive Overview**: Synthesizes final specification package with quality progression
- **Stakeholder Communication**: Professional document suitable for executive and stakeholder review
- **Implementation Readiness**: Clear assessment of final readiness and next steps

### README.md Navigation Guide
- **Project Root Level**: Navigation guide at project root: `generated/design/[project-name]/README.md`
- **Purpose**: Provides clear navigation and overview of all project deliverables
- **Content**: Project overview, folder structure explanation, key deliverables summary
- **Stakeholder Friendly**: Easy entry point for stakeholders to understand project organization
- **Implementation Ready**: Clear guidance for development teams on where to find specific information

### Supplement Material
- **Supporting Documentation**: Supporting documentation including input assessment analysis
- **MCP Prescriptive Guidance**: Comprehensive MCP server inventory and project-specific recommendations
- **Project Risk Analysis**: Comprehensive project delivery risk assessment and mitigation strategies
- **Reference Materials**: Additional reference materials and analysis documents
- **Traceability**: Source analysis and supporting evidence for specification generation
- **Historical Record**: Maintains record of analysis and decision-making process

## File Naming Conventions

### Project Folder
- **Format**: `generated/design/[project-name]/`
- **Name Source**: Extract from customer context or project documents
- **Format**: kebab-case (lowercase with hyphens)
- **Single Folder**: One project folder contains all deliverables

### Specification Packages (Quality Iterations)
- **Format**: `specification-package-iteration-X/` within project folder
- **Sequential**: X = 1, 2, 3, etc. until 90/100 quality achieved
- **Complete**: Each contains complete specification package
- **Quality Focus**: Each iteration improves quality based on assessment

### Score Sheets (Quality Iterations)
- **Format**: `score-sheet-iteration-X.md` at project root level
- **Sequential**: X = 1, 2, 3, etc. matching specification package iterations
- **Standalone**: Each score sheet is complete and standalone
- **Quality Tracking**: Shows progression toward 90/100 threshold

### Change Documentation
- **Format**: `changelog-from-iteration-X.md` (where X is the previous iteration number)
- **Feedback Traceability**: Documents specific changes made based on feedback received
- **Impact Analysis**: Explains how feedback influenced specification updates
- **Decision Rationale**: Provides rationale for changes made or feedback not incorporated

### Threat Model Components
- **threat-analysis.md**: Core threat analysis and STRIDE assessment
- **security-controls.md**: Security controls mapping and implementation
- **testing-framework.md**: Security testing framework and procedures
- **implementation-guidance.md**: Implementation guidance and best practices

### Executive Summary
- **executive-summary.md**: Comprehensive project overview and quality assessment summary for that iteration
- **Iteration Folder Level**: Placed within each project iteration folder for easy stakeholder access
- **Professional Format**: Suitable for executive and stakeholder presentation
- **Iteration Context**: Includes information about changes made in that iteration (for iterations 2+)

### README.md Navigation Guide
- **README.md**: Project navigation guide and overview at project root level
- **Content**: Project summary, folder structure, deliverables overview, implementation guidance
- **Format**: Professional markdown suitable for stakeholders and development teams
- **Purpose**: Single entry point for understanding complete project organization

### Supporting Documents
- **input-assessment-analysis.md**: Core input assessment analysis
- **tools-prescriptive-guidance.md**: MCP server inventory and project-specific recommendations (renamed from mcp-prescriptive-guidance.md)
- **project-risk-analysis.md**: Project delivery risk assessment and mitigation strategies
- **[descriptive-name].md**: Additional supporting documents with descriptive names
- **Clear Naming**: File names should clearly indicate content and purpose

## Quality Assurance Requirements

### Structure Validation
- **Folder Structure**: Validate folder structure matches defined requirements
- **File Presence**: Ensure all required files and folders present
- **Naming Compliance**: Verify file naming conventions followed
- **Organization Logic**: Confirm logical organization and navigation

### Content Organization
- **Complete Packages**: Each iteration contains complete specification package
- **Audit Trail**: Complete audit trail of improvements and decisions maintained
- **Traceability**: Clear traceability from inputs to outputs maintained
- **Integration**: All components properly integrated and cross-referenced

### Handoff Readiness
- **Development Ready**: Organization supports easy development team handoff
- **Stakeholder Friendly**: Structure supports stakeholder review and approval
- **Maintenance Ready**: Organization supports ongoing maintenance and updates
- **Audit Ready**: Structure supports audit and compliance requirements

## Implementation Guidelines

### Folder Creation
1. **Project Folder**: Create project folder at `generated/design/`
2. **Initial Structure**: Create initial folder structure at workflow start
3. **Progressive Build**: Build structure progressively as workflow advances
4. **Validation**: Validate structure at each major milestone

### File Management
1. **Iteration Management**: Create new iteration folders as needed
2. **File Copying**: Copy unchanged files from previous iterations
3. **Version Control**: Use "-improved" suffix for modified files
4. **Cleanup**: Ensure no orphaned or misplaced files

### Quality Control
1. **Structure Check**: Regular validation of folder structure compliance
2. **Content Review**: Ensure content properly organized and accessible
3. **Navigation Test**: Verify easy navigation and document discovery
4. **Handoff Preparation**: Prepare structure for clean handoff

## Benefits of Proper Organization

### Development Team Benefits
- **Clear Structure**: Easy to understand and navigate
- **Complete Information**: All necessary information in logical locations
- **Audit Trail**: Clear progression and decision history
- **Implementation Ready**: Ready for immediate development use

### Stakeholder Benefits
- **Professional Presentation**: Well-organized and professional appearance
- **Easy Review**: Logical organization supports efficient review
- **Quality Evidence**: Clear evidence of quality process and outcomes
- **Decision Support**: Complete information for decision-making

### Project Management Benefits
- **Progress Tracking**: Clear evidence of progress and completion
- **Quality Assurance**: Structured approach to quality validation
- **Risk Management**: Complete documentation for risk assessment
- **Handoff Management**: Smooth transition to development phase

### Compliance Benefits
- **Audit Ready**: Structure supports audit and compliance requirements
- **Traceability**: Complete traceability from requirements to implementation
- **Documentation**: Comprehensive documentation for regulatory compliance
- **Quality Evidence**: Clear evidence of quality processes and outcomes

### Task Checklist

- [ ] **Task 7.1: Create Project Folders**
  - [ ] **Project Name Extraction**
    - [ ] Extract project name from `.workflow-state/customer-context.md` or project documents
    - [ ] Convert to kebab-case format (lowercase with hyphens)
    - [ ] Use `project-specification` as fallback if no clear name found
  - [ ] **Project Folder Creation**
    - [ ] Create single project folder at `generated/design/[project-name]/`
    - [ ] Create initial folder structure within project folder
    - [ ] Validate folder structure matches defined requirements
  - [ ] **Initial Organization Setup**
    - [ ] Create specification-package-iteration-1/ folder within project folder with complete subfolder structure:
      - [ ] requirements/ (functional-requirements.md, non-functional-requirements.md, requirements-traceability-matrix.md)
      - [ ] user-stories/ (user-stories.md)
      - [ ] architecture/ (system-architecture.md, technical-specifications.md)
      - [ ] architecture-decision-records/ (ADR-001-[decision-name].md, etc.)
    - [ ] Create threat-model/ folder with security assessment structure:
      - [ ] threat-analysis.md, security-controls.md, testing-framework.md, implementation-guidance.md
    - [ ] Create supplement-material/ folder for supporting documents
    - [ ] Establish file naming conventions and organization rules

- [ ] **Task 7.2: Organize Deliverables**
  - [ ] **Iteration Management**
    - [ ] Create additional iteration folders as needed (iteration-2, iteration-3, etc.)
    - [ ] Copy unchanged files from previous iterations
    - [ ] Use "-improved" suffix for modified files in iterations
    - [ ] Maintain complete packages in each iteration folder
  - [ ] **Score Sheet Management**
    - [ ] Place score sheets in project root folder with iteration numbering
    - [ ] Use score-sheet-iteration-X.md naming format
    - [ ] Ensure each score sheet is complete and standalone
    - [ ] Maintain audit trail of quality progression

- [ ] **Task 7.3: Structure Specialized Content**
  - [ ] **Threat Model Organization**
    - [ ] Create dedicated threat-model folder
    - [ ] Organize threat model components within folder (threat-analysis.md, security-controls.md, etc.)
    - [ ] Ensure all security assessment deliverables contained within
  - [ ] **Supplement Material Organization**
    - [ ] Place input-assessment-analysis.md in supplement-material folder
    - [ ] Place tools-prescriptive-guidance.md in supplement-material folder
    - [ ] Place project-risk-analysis.md in supplement-material folder
    - [ ] Organize additional supporting documents with descriptive names
    - [ ] Maintain traceability and reference materials

- [ ] **Task 7.4: Prepare Final Package**
  - [ ] **Quality Validation**
    - [ ] Validate folder structure compliance with defined requirements
    - [ ] Ensure all required files and folders present
    - [ ] Verify file naming conventions followed consistently
    - [ ] Confirm logical organization and navigation
  - [ ] **README.md Creation**
    - [ ] Create comprehensive README.md at project root level
    - [ ] Include project overview and navigation guide
    - [ ] Document folder structure and deliverables
    - [ ] Provide implementation guidance for development teams
    - [ ] Ensure professional presentation for stakeholders
  - [ ] **Handoff Preparation**
    - [ ] Verify executive summary is present at project root level
    - [ ] Confirm tools-prescriptive-guidance.md is in supplement-material folder
    - [ ] Verify project-risk-analysis.md is in supplement-material folder
    - [ ] Ensure complete audit trail of iterations and improvements
    - [ ] Validate implementation readiness and development team handoff
    - [ ] Confirm structure supports stakeholder review and approval