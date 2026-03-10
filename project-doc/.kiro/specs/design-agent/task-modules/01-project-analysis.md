# Stage 1: Project Analysis

## Overview

**Objective**: Assess project complexity and provide workflow recommendations
**Dependencies**: Input sources (project documents, user context, images, or combination)

This stage provides the foundation for the entire workflow by analyzing project complexity and recommending appropriate execution strategies.

## Task 1.1: Assess Project Complexity

**Status**: Not Started
**Dependencies**: Input sources (project documents, user context, images, or combination)

**Description**: Analyze available input sources to assess project complexity and provide workflow recommendations

**Required Deliverable**: Complexity assessment documented in `.workflow-state/design-handoff.md` with recommendations

**File Structure Reference**: See main [tasks.md](../tasks.md) "File Structure & Storage Locations" section for complete storage location definitions.

### Key Activities

- **Input Source Analysis**: Analyze available input sources (documents, user context, images)
- **Code Project Detection and Ingestion**: Detect and ingest any code projects from `project-doc/` folder
- **Complexity Categorization**: Determine if project is Simple/Moderate/Complex based on:
  - **Start from scratch**: User context only (images, descriptions) → Simple
  - **Simple documents**: 1-3 files, mostly text/markdown, <5MB total → Simple
  - **Moderate documents**: 4-8 files or mixed formats or 5-15MB total → Moderate
  - **Complex documents**: 9+ files or large PDFs/presentations or >15MB total → Complex
- **Time Estimation**: Provide realistic time estimate based on complexity
- **Workflow Recommendations**: Suggest single task vs full workflow approach
- **Session Guidance**: Recommend break points and session management strategies

### Complexity Assessment Framework

#### Simple Projects
- **Characteristics**: Start from scratch (user context only) OR 1-3 files, mostly text/markdown, <5MB total
- **Time Estimate**: 2-3 hours total workflow time
- **Recommendation**: Auto-proceed with full workflow
- **Session Strategy**: Single session execution recommended
- **Examples**: POC from image description, small text-based requirements, basic project concepts

#### Moderate Projects  
- **Characteristics**: 4-8 files or mixed formats or 5-15MB total
- **Time Estimate**: 4-6 hours total workflow time
- **Recommendation**: Ask user preference (single task vs full workflow)
- **Session Strategy**: Consider breaking at stage boundaries

#### Complex Projects
- **Characteristics**: 9+ files or large PDFs/presentations or >15MB total
- **Time Estimate**: 6+ hours total workflow time
- **Recommendation**: Strongly recommend single task approach
- **Session Strategy**: Execute one task per session to avoid timeouts

### Assessment Process

1. **Input Source Inventory**:
   - **Check `project-doc/` folder**: Count files, calculate total size, identify file types (if folder exists and contains files)
   - **Review `.workflow-state/customer-context.md`**: Analyze captured user context from session management
   - **Analyze current user prompt**: Extract additional context, images, requirements from current request
   - **Identify input scenario**: Existing documents, start from scratch, mixed, or insufficient

2. **Code Project Detection and Ingestion** (Execute when project-code folder exists and is not empty):
   - **Check for Code Projects**: Verify if `project-doc/project-code/` folder exists and contains files
   - **If folder exists and is not empty**: Proceed with detection and ingestion
   - **If folder is empty or doesn't exist**: Skip this step and document in handoff
   - **Scan Code Sources**: Look for existing codebases in:
     - **`project-doc/project-code/` folder**: Primary location for code projects
   - **Detect Code Project Indicators**:
     - `.git/` directories (indicating git repositories)
     - Common project structure patterns (`src/`, `lib/`, `components/`, `app/`, etc.)
     - Package management files (`package.json`, `requirements.txt`, `pom.xml`, `Gemfile`, etc.)
     - Infrastructure as Code files (`*.tf`, `cdk.json`, CloudFormation templates, `docker-compose.yml`)
     - Configuration files (`.env`, `config/`, `settings.py`, `application.properties`)
     - Build files (`Makefile`, `build.gradle`, `webpack.config.js`, `tsconfig.json`)
     - README files with project descriptions
   - **Project Classification**: Classify detected projects by type and purpose:
     - **Legacy System**: Production codebase for reference or codebase requiring migration or integration
     - **Current Development**: Active development codebase needing enhancement
     - **Reference Implementation**: Example code or templates for guidance
     - **Infrastructure Project**: Contains IaC files (Terraform, CDK, CloudFormation)
     - **Application Project**: Contains application code and dependencies
     - **Microservices**: Multiple service directories in single repository
     - **Monorepo**: Single repository containing multiple projects
     - **Documentation Project**: Contains primarily documentation files
   - **Brownfield Analysis**: For existing codebases, perform additional analysis:
     - **Architecture Pattern Detection**: Identify MVC, microservices, serverless, monolithic patterns
     - **Technology Stack Analysis**: Identify languages, frameworks, databases, cloud services
     - **Technical Debt Assessment**: Identify outdated dependencies, deprecated patterns, security issues
     - **Integration Points**: Identify APIs, databases, external services, and dependencies
     - **Migration Complexity**: Assess effort required for modernization or cloud migration (if migration is needed)
   - **Automatic Ingestion** (when code projects are detected):
     - Copy ALL detected code projects to `.workflow-state/reference-architectures/[project-name]/`
     - Preserve original folder structure within each project
     - Include all files (code, configs, documentation, IaC files)
   - **Generate Analysis** (for each ingested project):
     - Create `PROJECT_ANALYSIS.md` for each ingested project with:
       - Project type and classification
       - Technology stack and architecture patterns
       - Technical debt assessment
       - Integration requirements and constraints
       - Recommended modernization approach
   - **Update Status** (MANDATORY): Document ingestion status in `.workflow-state/design-handoff.md` with:
     - **If project-code folder exists and has content**: Number of code projects detected and ingested, list of project names and locations
     - **If project-code folder is empty or doesn't exist**: Explicit statement "No code projects provided in project-doc/project-code/"

3. **Complexity Analysis**:
   - **For documents**: Assess document complexity and density, identify parsing challenges
   - **For user context**: Evaluate scope and detail level of provided information
   - **For mixed input**: Combine document and context complexity assessment
   - **For code projects**: Include ingested code projects in complexity assessment
   - Estimate processing time requirements

4. **Risk Assessment**:
   - Identify session timeout risks based on input complexity
   - Assess potential memory constraints
   - Consider context window limitations

5. **Recommendation Generation**:
   - Provide clear complexity categorization
   - Suggest optimal execution strategy
   - Recommend session management approach

### Acceptance Criteria

- **Complexity Level**: Clear categorization (Simple/Moderate/Complex) documented
- **Input Analysis**: Input sources identified and analyzed (documents, user context, images)
- **Code Project Ingestion**: 
  - **If project-code folder has content**: All code projects copied to `.workflow-state/reference-architectures/` with PROJECT_ANALYSIS.md files generated
  - **If project-code folder is empty/missing**: Explicit documentation in handoff stating no code projects provided
  - **Validation**: `.workflow-state/design-handoff.md` must contain explicit statement about code project detection results
- **Time Estimate**: Realistic time estimate provided (e.g., "2-3 hours", "4-6 hours")
- **Recommendations**: Specific guidance on workflow approach and session management
- **Progress Update**: Project analysis task marked complete, requirements generation task set as current in `.workflow-state/design-handoff.md`
### Output Documentation

Document the following in `.workflow-state/design-handoff.md`:

```markdown
## Project Complexity Assessment

**Complexity Level**: [Simple/Moderate/Complex]

**Input Analysis**:
- Input Scenario: [Existing documents/Start from scratch/Mixed input/Insufficient/Brownfield]
- Documents (project-doc/ folder): [X] files, [X] MB, [file types] (if applicable)
- User Context (from .workflow-state/customer-context.md): [Description of captured context]
- Additional Context (from current prompt): [Images, descriptions, requirements provided]

**Code Project Detection** (MANDATORY - must be documented):
- Project-Code Folder Status: [Exists with content / Empty / Does not exist]
- Code Projects Detected: [X] projects OR "No code projects provided"
- Ingestion Status: [X projects copied to .workflow-state/reference-architectures/ OR "Skipped - no code projects"]

**Codebase Analysis** (if code projects were detected):
- Detected Projects: [List of project names and types]
- Technology Stacks: [Summary of languages, frameworks, databases identified]
- Architecture Patterns: [Monolithic, microservices, serverless, etc.]
- Technical Debt Level: [Low/Medium/High assessment]
- Integration Complexity: [Assessment of modernization effort required]

**Time Estimate**: [X-Y] hours total workflow time

**Recommendations**:
- Execution Strategy: [Single task/Full workflow/User choice]
- Session Management: [Single session/Stage boundaries/Task-by-task]
- Risk Factors: [Any identified risks or constraints]

**Next Steps**: [Specific guidance for proceeding]
```

### Integration Points

- **Session Management**: Feeds into execution mode selection
- **Requirements Generation**: Informs approach and depth of analysis
- **Quality Assessment**: Sets expectations for iteration strategy
- **Security Assessment**: Influences threat modeling scope

### Task Checklist

- [ ] **Task 1.1: Project Complexity Assessment**
  - [ ] **Input Source Analysis**
    - [ ] Identify input scenario (existing documents, start from scratch, mixed, insufficient, brownfield)
    - [ ] Analyze `project-doc/` folder (if exists): count files, calculate size, identify types
    - [ ] Analyze `project-doc/` folder (if exists): detect existing codebases and legacy systems
    - [ ] Review `.workflow-state/customer-context.md` for captured user context
    - [ ] Analyze current user prompt: descriptions, images, requirements provided
    - [ ] Assess input complexity and density based on available sources
    - [ ] Identify potential parsing challenges for documents (if applicable)
  - [ ] **Code Project Detection and Ingestion** (Execute when project-code folder is not empty)
    - [ ] Check if `project-doc/project-code/` folder exists and contains files
    - [ ] **If folder exists and is not empty**:
      - [ ] Scan `project-doc/project-code/` folder for code projects
      - [ ] Detect code project indicators (git repos, package files, build configs, IaC files, etc.)
      - [ ] Classify projects by type and purpose (Legacy, Current, Reference, Infrastructure, Application, etc.)
      - [ ] Perform brownfield analysis (architecture patterns, technology stack, technical debt, integration points)
      - [ ] Copy ALL detected code projects to `.workflow-state/reference-architectures/[project-name]/`
      - [ ] Preserve original folder structure and include all files
      - [ ] Generate `PROJECT_ANALYSIS.md` for each project with classification, tech stack, debt assessment, and modernization recommendations
      - [ ] Document ingestion status in `.workflow-state/design-handoff.md` with number of projects and locations
    - [ ] **If folder is empty or doesn't exist**:
      - [ ] Document "No code projects provided in project-doc/project-code/" in `.workflow-state/design-handoff.md`
      - [ ] Skip ingestion and analysis steps
  - [ ] **Complexity Assessment**
    - [ ] Estimate processing time requirements based on input complexity
    - [ ] Determine complexity level (Simple/Moderate/Complex)
    - [ ] Apply complexity assessment framework to input scenario
    - [ ] Document categorization rationale
  - [ ] **Risk Assessment**
    - [ ] Identify session timeout risks
    - [ ] Assess potential memory constraints
    - [ ] Consider context window limitations
  - [ ] **Recommendation Generation**
    - [ ] Provide clear execution strategy recommendation
    - [ ] Suggest optimal session management approach
    - [ ] Document time estimates and risk factors
  - [ ] **Documentation and Handoff**
    - [ ] Update `.workflow-state/design-handoff.md` with assessment results
    - [ ] Mark project analysis task as complete and set requirements geneneration task as current