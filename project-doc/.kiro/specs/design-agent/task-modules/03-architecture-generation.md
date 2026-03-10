# Stage 3: Architecture Generation

## Overview

**Objective**: Generate production-ready architecture design using either expert-guided Intelligence Hub analysis or systematic architecture generation with reference architecture integration.

**Dependencies**: 
- Requirements generation marked as complete in `.workflow-state/design-handoff.md`
- Complete requirements package available in project specification directory
- `core-methodology/architecture-generation-guide.md` (architecture principles and Intelligence Hub standards)
- `core-methodology/architecture-guidance-selection.md` (guidance selection framework for standard path)
- `core-methodology/architecture-integration-validation-guide.md` (comprehensive validation frame work for Task 3.4)

**Persona Focus**: Technical Lead / Solution Architect

**Critical Design Philosophy**: This stage provides two mutually exclusive architecture generation paths that converge into common architecture activities. Path selection is determined by Intelligence Hub availability, ensuring optimal architecture quality regardless of tooling constraints.

## Prerequisites

### Required Inputs
- **Requirements Completion**: Requirements generation marked as complete in `.workflow-state/design-handoff.md`
- **Functional Requirements**: Complete functional requirements documentation in project specification directory
- **Non-Functional Requirements**: Complete non-functional requirements documentation in project specification directory
- **Customer Context**: Available in `.workflow-state/customer-context.md` (captured during session management or project analysis)

### System Requirements
- **Intelligence Hub MCP Server**: Configuration checked for availability determination
- **Project Structure**: `generated/design/specification-package-iteration-1/` directory established
- **Workflow State**: `.workflow-state/` directory for context and reference storage

### Knowledge Dependencies
- **Architecture Generation Guide**: Core methodology and Intelligence Hub integration standards
- **Architecture Guidance Selection**: Framework for systematic guidance selection when Intelligence Hub unavailable
- **Customer Context**: Project characteristics and constraints for context-aware architecture design

## Task Descriptions

### Task 3.1: Check Intelligence Hub Availability

**Purpose**: Determine architecture generation path based on Intelligence Hub availability and establish execution parameters.

**Critical First Step**: Before any architecture generation activities, perform Intelligence Hub availability assessment:

#### MCP Configuration Verification
1. **Configuration Check**: Examine MCP configuration for Intelligence Hub server entry
   - Locate `"intelligence-hub"` server in MCP configuration
   - Verify `"disabled"` status (false = available, true = disabled)
   - Document configuration state

2. **Connection Validation**: If enabled in configuration, verify actual server availability
   - Attempt connection to Intelligence Hub MCP server
   - Test basic connectivity and response
   - Document connection status and any error conditions

3. **Path Selection Decision**: Based on availability assessment results
   - **Available**: Intelligence Hub server configured, enabled, and responsive → Path A
   - **Unavailable**: Server disabled, not configured, or connection failed → Path B

4. **Document Path Selection in Workflow State**: Update `.workflow-state/design-handoff.md`
   - Check the appropriate box in "Architecture Generation Path Selection" section
   - Path A: Check if Intelligence Hub available
   - Path B: Check if Intelligence Hub unavailable
   - Document path selection rationale explaining why this path was chosen
   - **CRITICAL**: This documentation ensures Task 3.2 follows the correct path

#### Execution Parameters Setup
- **Timeout Configuration**: Set appropriate timeouts based on selected path
- **User Communication**: Prepare user for expected execution timeline
- **Fallback Planning**: Document fallback procedures if primary path fails

### Task 3.2: Generate Architecture Design

**Purpose**: Execute architecture generation using the determined path, ensuring complete architecture design regardless of tooling availability.

**CRITICAL FIRST STEP**: Before executing any architecture generation activities:
1. **Read `.workflow-state/design-handoff.md`** to verify which path was selected in Task 3.1
2. **Check the "Architecture Generation Path Selection" section** to see which box is checked
3. **If path is not documented**, STOP and complete Task 3.1 first

**MANDATORY PATH CONFIRMATION** (Display in chat before proceeding):

Based on the selected path, you MUST:
1. **Read the corresponding path section** in the Task Checklist below (PATH A or PATH B)
2. **Identify all step numbers** for the selected path (e.g., A1, A2, A3 or B1, B2, B3, B4, B5)
3. **Create a summary** listing each step by its step number and description
4. **Display the summary in chat** using this format:

```
✓ Path [A/B] Selected: [Path Name]

I will execute the following Path [A/B] steps in order:
- Step [A/B]1: [Step name and brief description]
- Step [A/B]2: [Step name and brief description]
- Step [A/B]3: [Step name and brief description]
[Continue for all steps in the path]

Proceeding with Path [A/B] execution starting with Step [A/B]1...
```

**Example for Path A:**
```
✓ Path A Selected: Intelligence Hub Integration

I will execute the following Path A steps in order:
- Step A1: Prerequisites Verification and Deep Research Decision (verify hub, prompt user, document choice)
- Step A2: Intelligence Hub Job Execution (submit job, monitor status, retrieve results)
- Step A3: Expert Insights Integration (analyze rankings, review recommendations, document influence)

Proceeding with Path A execution starting with Step A1...
```

**Example for Path B:**
```
✓ Path B Selected: Standard Architecture Generation

I will execute the following Path B steps in order:
- Step B1: Prerequisites Verification (document unavailability, load context)
- Step B2: Architecture Guidance Selection (apply framework, display decision tree, document decision)
- Step B3: Reference Architecture Analysis (download references, follow instructions, gap analysis)
- Step B4: Reference Architecture Integration Design (design integration, plan customization, document specifications)
- Step B5: Context-Aware Architecture Design (apply appropriate mode, complete design, validate)

Proceeding with Path B execution starting with Step B1...
```

**CRITICAL**: After displaying the confirmation, execute ONLY the steps for the selected path in the exact order listed (A1→A2→A3 or B1→B2→B3→B4→B5). Do NOT skip any steps. Do NOT skip ahead to Task 3.3 until ALL path-specific steps are complete and verified.

#### Path A: Intelligence Hub Integration (When Available)

**EXECUTION PROTOCOL**: Execute each step below in order. Do NOT skip to the next step until the current step is complete and verified.

**Step A1: Prerequisites Verification and Deep Research Decision**

Execute these actions:
1. Verify Intelligence Hub MCP server is available and responsive
2. Verify requirements package is ready (check `.workflow-state/design-handoff.md`)
3. Present deep research decision protocol to user (see below)
4. Wait for explicit user response (y/n)
5. Document user choice for audit trail

**Deep Research Decision Protocol** (display to user):
```
MANDATORY USER CONSULTATION:

"Intelligence Hub supports deep research analysis which provides additional
expert insights and recommendations but takes longer to complete
(up to 1 hour vs. standard 10-15 minutes).

Deep research includes:
- Extended expert analysis with additional insights and alternative approaches
- Additional architectural guidance with trade-off analysis
- Review of industry standards, patterns, and best practices
- Risk analysis with mitigation strategies
- Implementation recommendations with step-by-step guidance

Would you like to enable deep research for this architecture generation? (y/n)"

EXECUTION RULES:
- ALWAYS prompt user before job submission
- WAIT for explicit user response before proceeding
- Document user choice for audit trail
- Set timeout expectations based on user choice
```

**Verification checkpoint**: Display in chat:
```
✓ Step A1 Complete: Prerequisites Verified and Deep Research Decision Made
- Intelligence Hub available: [yes/no]
- Requirements package ready: [yes/no]
- User deep research choice: [yes/no]
- Timeout expectation: [15 min / 60 min]
- Ready to proceed to Step A2
```

**Step A2: Intelligence Hub Job Execution**

Execute these actions:
1. **Job Submission**: Use `mcp_intelligence_hub_submit_job` with complete requirements
   - Submit functional requirements from project specification directory
   - Submit non-functional requirements from project specification directory
   - Apply user's deep research choice (`enable_deep_research: true/false`)
   - Capture and display Job ID to user for tracking

2. **Status Monitoring with Enhanced Polling**:
   ```
   POLLING PROTOCOL:
   - Poll interval: Every 60 seconds (1 minute)
   - Status progression: SUBMITTED → PROCESSING → EXPERT_COMPLETED → COMPLETED
   - Timeout limits: 15 minutes (standard) / 60 minutes (deep research)
   - User updates: Display Job ID and current status during polling
   
   CRITICAL STATUS HANDLING:
   - NEVER call get_result() on EXPERT_COMPLETED status
   - ONLY call get_result() when status is COMPLETED
   - Continue polling through EXPERT_COMPLETED to COMPLETED
   - Block workflow progression until completion or timeout
   
   TIMEOUT HANDLING:
   - Document timeout occurrence and duration
   - Inform user of timeout and fallback approach
   - Proceed with Path B methodology if timeout occurs
   ```

3. **Results Retrieval and Storage**:
   - Use `mcp_intelligence_hub_get_result` when job status is COMPLETED
   - Save complete JSON response to `generated/design/specification-package-iteration-[n]/architecture/intelligence-hub-response.md`
   - Format as markdown with JSON code block for IDE preview compatibility
   - Include all response data: expert evaluations, asset rankings, deep research results, metadata

**Verification checkpoint**: Display in chat:
```
✓ Step A2 Complete: Intelligence Hub Job Executed
- Job ID: [job-id]
- Job status: [COMPLETED]
- Results saved to: [file path]
- Ready to proceed to Step A3
```

**Step A3: Expert Insights Integration**

Execute these actions:
1. Analyze asset rankings and apply 60% threshold for technology shortlisting
2. Review expert recommendations from Intelligence Hub response
3. Incorporate deep research findings if available
4. Document Intelligence Hub influence on architecture decisions

**Verification checkpoint**: Display in chat:
```
✓ Step A3 Complete: Expert Insights Integrated
- Asset rankings analyzed: [yes/no]
- Expert recommendations reviewed: [yes/no]
- Deep research incorporated: [yes/no if applicable]
- Intelligence Hub influence documented: [yes/no]
- Ready to proceed to Task 3.3 (Common Architecture Activities)
```

#### Path B: Standard Architecture Generation (When Intelligence Hub Unavailable)

**EXECUTION PROTOCOL**: Execute each step below in order. Do NOT skip to the next step until the current step is complete and verified.

**Step B1: Prerequisites Verification**

Execute these actions:
1. Document Intelligence Hub unavailability reason in chat (e.g., "Intelligence Hub disabled in MCP configuration")
2. Read `.workflow-state/customer-context.md` and display key project characteristics in chat
3. Verify customer context is sufficient for architecture decisions

**Verification checkpoint**: Display in chat:
```
✓ Step B1 Complete: Prerequisites Verified
- Intelligence Hub unavailability: [reason]
- Customer context loaded: [key characteristics]
- Ready to proceed to Step B2
```

**Step B2: Architecture Guidance Selection**

Execute these actions:
1. Read `core-methodology/architecture-guidance-selection.md` to understand the framework
2. Apply decision hierarchy evaluation using customer context from Step 1
3. Display decision tree output in chat showing:
   - Each guidance type evaluation (MATCH/NO MATCH/SUPPLEMENTARY)
   - Specific reasons for each decision
   - Final selected guidance approach
4. Document decision in `.workflow-state/design-handoff.md` under "Key Insights & Decisions" section
5. **Extract and Document Repository Links** (if selected guidance references git repositories):
   - Read the selected guidance documents to identify any git repository references
   - Extract repository URLs, clone commands, and setup instructions
   - Display repository links in chat for user visibility
   - Document in `.workflow-state/design-handoff.md` under "Reference Architecture Repositories" section:
     ```markdown
     ## Reference Architecture Repositories
     
     The following repositories were identified from selected guidance:
     
     - **[Guidance Name]**: `[git clone command]`
       - Purpose: [brief description from guidance doc]
       - Setup Instructions: [path to instructions file if available, e.g., notes-for-q.md]
     ```
   - If no repositories are referenced, document "No reference architecture repositories identified"

**Verification checkpoint**: Display in chat:
```
✓ Step B2 Complete: Guidance Selection Decided
- Decision tree evaluation: [displayed above]
- Selected guidance: [guidance type]
- Repository links extracted: [count or "none"]
- Documented in design-handoff.md: [yes/no]
- Ready to proceed to Step B3
```

**Step B3: Reference Architecture Analysis** (Execute ONLY if reference code exists in .workflow-state/reference-architectures)
Execute these actions:
1. **Analyze Existing Codebases** (from Task 2.1 codebase analysis):
   - Review existing codebases copied to `.workflow-state/reference-architectures/[project-name]/` during requirements generation
   - Read `PROJECT_ANALYSIS.md` files for each existing codebase to understand current state
   - Analyze existing architecture patterns, technical debt, and constraints
   - Document current system capabilities and limitations
2. **Download External References** (from guidance selection):
   - Read repository links from `.workflow-state/design-handoff.md` "Reference Architecture Repositories" section
   - For each documented repository: Use `git clone [repo-url] .workflow-state/reference-architectures/[folder-name]/`
   - Use meaningful folder names that reflect the repository purpose (e.g., `solution-xyz`,`prescriptive-guidance-xyz`)
   - If git clone fails: Ask user how to proceed (retry with refreshed auth or use available MCP tools)
3. **Read Reference Instructions**:
   - Check "Setup Instructions" paths from design-handoff.md 
   - Also check standard documentation files (README.md, CONTRIBUTING.md)
   - Display key setup guidance in chat for user awareness
4. **Comprehensive Gap Analysis** (existing systems + external references vs. requirements):
   - Compare existing codebase capabilities against project requirements
   - Assess external reference architecture fit for filling gaps
   - Identify what can be preserved vs. what needs integration/replacement
   - Document integration strategy for existing systems with new architecture

**Required Deliverable**: `generated/design/supplement-material/gap-analysis.md`

**Gap Analysis Document Structure** (adapt sections as needed for project context):
- **Executive Summary**: Fit assessment and recommendation (existing systems + external references)
- **Current State Analysis**: Existing codebase capabilities, technical debt, and constraints
- **Reference Architecture Analysis**: External reference component capability review with requirements matching
- **Gap Identification**: Missing capabilities comparing current state + references vs. requirements
- **Integration Strategy**: Phased approach for incorporating reference architecture with existing systems
- **Technical Debt Management**: Plan for addressing legacy constraints and technical debt
- **Risk Assessment**: Technical risks and mitigation plans for brownfield projects
- **Conclusion**: Overall fit assessment and implementation roadmap

**Verification checkpoint**: Display in chat:
```
✓ Step B3 Complete: Reference Architecture Analyzed
- References downloaded: [list folders with repo names]
- Download method: [git clone / MCP fallback / other]
- Setup instructions reviewed: [list instruction files found]
- Gap analysis completed: [summary]
- Gap analysis saved to: supplement-material/gap-analysis.md
- Ready to proceed to Step B4
```

## Reference Architecture Step Enforcement

### Critical Rule: B3/B4 Step Execution
**MANDATORY EXECUTION**: If Step B2 selects ANY reference architectures (solutions, prescriptive guidance with repositories), then Steps B3 AND B4 MUST be executed.

**Cannot Skip When**:
- Solutions selected → B3 and B4 are MANDATORY  
- Prescriptive guidance with repositories selected → B3 and B4 are MANDATORY
- Existing codebases present in `.workflow-state/reference-architectures/` → B3 and B4 are MANDATORY

**Can Skip Only When**:
- Step B2 selected purely documentation-based guidance (Well-Architected Framework, AWS documentation)
- No reference architectures or code repositories were selected
- No existing codebases exist in the project

### Step B3 Requirements
**Must Execute**: Reference architecture analysis with gap assessment
**Must Deliver**: `supplement-material/gap-analysis.md`
**Must Include**: Fit assessment, capability review, gap identification, integration strategy

### Step B4 Requirements  
**Must Execute**: Integration design for selected reference architectures
**Must Deliver**: `supplement-material/integration-design.md`
**Must Include**: Integration architecture, customization requirements, deployment sequence

### Enforcement Validation
Before proceeding to Step B5, verify:
- [ ] If reference architectures selected in B2, both B3 and B4 were executed
- [ ] Required deliverables created (gap-analysis.md, integration-design.md)
- [ ] No skipping occurred when reference architectures were selected

---

**If no reference architectures selected, display**: "Step B3 Skipped: No reference architectures selected in Step B2. Proceeding to Step B5."

**Step B4: Reference Architecture Integration Design** 

**MANDATORY EXECUTION RULE**: This step MUST be executed if Step B3 was executed.

**Cannot Skip When**:
- Step B3 was executed → B4 is MANDATORY
- Reference architectures were analyzed → B4 is MANDATORY
- Gap analysis was completed → B4 is MANDATORY

**Can Skip Only When**:
- Step B3 was skipped (no reference architectures selected)
- No reference architectures or code repositories exist

Execute these actions:
1. Design integration approach for selected solutions as architecture foundation
2. Plan customization strategy based on gap analysis results from Step B3
3. Design combination strategy when multiple reference architectures are required
4. Document integration architecture and customization specifications

**Required Deliverable**: `generated/design/supplement-material/integration-design.md`

**Integration Design Document Structure** (adapt sections as needed for project context):
- **Integration Architecture Overview**: Visual diagram showing how existing systems, reference architectures, and new components integrate
- **Legacy System Integration**: How existing codebases integrate with new architecture (APIs, code integration, service boundaries)
- **Component Integration Specifications**: Detailed integration approach per component (preserve existing, extend legacy, use reference as-is, build custom)
- **Customization Requirements**: Specific code changes, configuration updates, and extensions needed for existing and reference systems
- **Deployment Sequence**: Phased deployment approach with dependencies, considering existing system constraints
- **Configuration Management**: Environment variables, shared configuration, secrets management across existing and new systems
- **Testing Strategy**: Integration testing approach including legacy system validation and testing
- **Success Criteria**: Clear definition of integration completion 

**Verification checkpoint**: Display in chat:
```
✓ Step B4 Complete: Integration Design Documented
- Integration approach: [summary]
- Customization strategy: [summary]
- Integration design saved to: supplement-material/integration-design.md
- Ready to proceed to Step B5
```

**If Step B3 was skipped, display**: "Step B4 Skipped: No reference architectures to integrate. Proceeding to Step B5."

**Step B5: Context-Aware Architecture Design**

Execute these actions:
1. Read `.workflow-state/customer-context.md` to determine appropriate mode:
   - POC Mode: Streamlined architecture, focus on core functionality validation
   - Production Mode: Enterprise considerations (scalability, availability, security)
   - Compliance Mode: Integrate compliance requirements and regulatory controls
   - Budget-Conscious Mode: Optimize for cost-effectiveness
2. Apply selected mode to architecture design approach
3. Complete architecture design with mode-appropriate complexity
4. Document architecture approach and validation strategy

**Verification checkpoint**: Display in chat:
```
✓ Step B5 Complete: Architecture Design Finished
- Mode applied: [POC/Production/Compliance/Budget-Conscious]
- Architecture design completed: [yes/no]
- Approach documented: [yes/no]
- Ready to proceed to Task 3.3 (Common Architecture Activities)
```

### Task 3.3: Create Architecture Diagrams and Specifications

**Purpose**: Create comprehensive architecture documentation including diagrams, ADRs, and technical specifications (both Path A and Path B converge here).

**MANDATORY PRE-CONVERGENCE VERIFICATION**:

Before proceeding with common architecture activities, verify path-specific work is complete:

**If Path A was executed:**
- [ ] Intelligence Hub job submitted and completed
- [ ] Expert evaluation results saved to `architecture/intelligence-hub-response.md`
- [ ] Expert insights documented and ready for integration

**If Path B was executed:**
- [ ] Architecture Guidance Selection Framework applied
- [ ] Decision tree output displayed in chat
- [ ] Guidance selection decision documented in design-handoff.md
- [ ] Reference architectures downloaded (if applicable)
- [ ] Gap analysis completed (if reference architectures used)
- [ ] Integration design documented (if reference architectures used)

**If any verification item is incomplete, STOP and complete it before proceeding to common architecture activities.**

#### System Architecture Design
1. **High-Level System Architecture**:
   - Design overall system components and their interactions
   - Define data flow patterns and integration approaches
   - Select technology stack with detailed rationale
   - Plan deployment architecture and infrastructure requirements

2. **Component Specifications**:
   - Define service boundaries and interfaces with precision
   - Document data models and schemas completely
   - Create API specifications and contracts
   - Integrate security architecture throughout all components

#### Architecture Decision Records (ADRs)
**Critical Documentation Standard**: Create individual ADR files for each significant architecture decision

**ADR Structure and Naming**:
- Location: `architecture-decision-records/` folder within specification package
- Naming convention: `ADR-XXX-[descriptive-title].md` (e.g., `ADR-001-database-selection.md`)
- Content requirements for each ADR:
  - **Decision Context**: Requirements and constraints that drove the decision
  - **Considered Alternatives**: All options evaluated with trade-off analysis
  - **Selected Approach**: Chosen solution with detailed rationale
  - **Implementation Implications**: Impact on development, operations, and maintenance
  - **Intelligence Hub Influence**: How expert insights influenced decision (if Path A used)
  - **Deep Research Impact**: How deep research findings influenced decision (if available)
  - **Repository Access**: Include git clone commands for any reference architectures or code repositories used

#### Technical Specifications
1. **Component Documentation**:
   - Detailed component specifications with interfaces
   - Data architecture with flow diagrams
   - Security controls integration throughout system
   - Performance and scalability considerations

2. **Implementation Planning**:
   - Development strategy with phases and milestones
   - Technology stack and tooling requirements
   - Team structure and skill requirements assessment
   - Risk assessment with mitigation strategiesß

### Task 3.4: Validate Architecture Completeness

**Purpose**: Validate architecture completeness, integration, and technical feasibility before advancing to holistic quality assessment using comprehensive validation framework. 

**Required Deliverable**: `generated/design/supplement-material/architecture-integration-validation.md`
1. **Load Validation Guide**: Read `core-methodology/architecture-integration-validation-guide.md` completely to understand the comprehensive validation framework

2. **Validation Report Document Structure** (adapt sections as needed for project context):
- Executive Summary**: Validation status, key findings, overall quality score
- Architecture Completeness Verification**: Requirements coverage analysis with traceability matrix
- Component Integration Validation**: Interface compatibility matrix and data flow validation
- Service Limits Impact Assessment**: AWS service inventory with quota analysis and mitigation strategies
- Technical Feasibility Assessment**: Technology stack validation and implementation complexity assessment
- Documentation Completeness Review**: Verification of all architecture documentation and ADRs
- Validation Summary**: Scoring breakdown and readiness assessment
- Recommendations**: Critical actions and optional enhancements before next stage

#### Validation Framework Application
1. **Load Validation Guide**: Read `core-methodology/architecture-integration-validation-guide.md` completely to understand the comprehensive validation framework
2. **Apply Validation Criteria**: Execute all validation steps defined in the guide:
   - Architecture Completeness Verification (Requirements Coverage Analysis)
   - Component Integration Validation (Interface Compatibility, Data Flow, Integration Patterns)
   - Service Limits Impact Assessment (Service Inventory, Limits Research, Mitigation Planning)
   - Technical Feasibility Assessment (Technology Stack, Implementation Complexity, Resource Requirements)
   - Documentation Completeness Review (Architecture Documentation, ADRs)

#### Architecture Integration Validation Report Generation
**MANDATORY OUTPUT**: Generate `architecture-integration-validation.md` in supplement material folder following the exact report structure from the validation guide:

1. **Report Structure Compliance**: Follow the complete report structure defined in the validation guide:
   - Executive Summary with validation status and key findings
   - Architecture Completeness Verification with requirements coverage tables
   - Component Integration Validation with interface matrices and data flow validation
   - Service Limits Impact Assessment with complete service analysis and mitigation strategies
   - Technical Feasibility Assessment with technology validation and complexity analysis
   - Documentation Completeness Review with quality assessment
   - Validation Summary with scoring and readiness determination

2. **Quality Standards Application**: Apply all quality standards from the validation guide:
   - Complete data tables for all assessments
   - Clear pass/fail determinations with supporting evidence
   - Specific recommendations for any identified gaps
   - Risk assessments with mitigation strategies
   - Overall validation score calculation (0-100)

3. **Validation Examples Integration**: Use the validation examples from the guide as templates for:
   - Requirements coverage tables with architectural solutions
   - Service limits analysis with risk levels and mitigation strategies
   - Quality scoring matrix with weighted calculations
   - Interface compatibility matrices
   - Technical feasibility assessments

#### Critical Validation Activities
**Execute these validation steps systematically**:

1. **Requirements Coverage Analysis**:
   - Create complete traceability matrix (functional, non-functional, user stories)
   - Verify 95%+ coverage threshold for functional and non-functional requirements
   - Document architectural solutions for each requirement
   - Validate user story implementation paths

2. **Component Integration Validation**:
   - Create interface compatibility matrix for all component interactions
   - Validate data flow patterns and integration approaches
   - Confirm integration patterns are appropriate and consistent
   - Test integration assumptions and document dependencies

3. **Service Limits Impact Assessment**:
   - Extract complete AWS service inventory from architecture
   - Research current service limits using AWS documentation MCP tools
   - Perform usage estimation for POC and production scenarios
   - Identify high-risk limits and document mitigation strategies
   - Plan service limit increase requests where needed

4. **Technical Feasibility Assessment**:
   - Validate all technology choices for maturity and team expertise
   - Assess implementation complexity and effort estimates
   - Confirm resource requirements are realistic and available
   - Identify technical risks and mitigation approaches

5. **Documentation Completeness Review**:
   - Verify all required architecture documentation is complete
   - Validate ADR completeness and quality
   - Confirm implementation guidance is actionable
   - Assess overall documentation quality against standards

#### Validation Success Criteria
**Apply these success criteria from the validation guide**:
- Overall validation score ≥85/100 (minimum pass threshold)
- No critical validation failures
- All high-risk service limits have mitigation strategies
- Requirements coverage ≥95% for functional and non-functional requirements
- All component interfaces properly defined and compatible
- Technical feasibility confirmed for all architecture decisions

**DELIVERABLE**: Complete `architecture-integration-validation.md` report with validation status (PASSED/CONDITIONAL/FAILED) and clear readiness determination for holistic quality assessment.

### Task 3.5: Validate AI Agent Architecture with AgentCore MCP (Optional)

**Purpose**: Provide additional architecture validation layer using Amazon Bedrock AgentCore MCP server for AI agent architectures and AWS service integration patterns.

**When to Execute**: This task is optional and should be executed when:
- Architecture includes AI agents, conversational interfaces, or ML components
- Architecture uses AWS Bedrock services or AI/ML workflows
- Architecture includes agentic patterns or autonomous system components

**Dependencies**: 
- Amazon Bedrock AgentCore MCP server configured and available
- Architecture documentation includes AI/ML or agent components

#### AgentCore MCP Server Availability Assessment

**MCP Configuration Check**:
1. **Server Configuration Verification**: Check MCP configuration for AgentCore server entry
   ```json
   "awslabs.amazon-bedrock-agentcore-mcp-server": {
     "command": "uvx",
     "args": ["awslabs.amazon-bedrock-agentcore-mcp-server@latest"],
     "disabled": false
   }
   ```
2. **Connection Validation**: Test server availability and tool access
   - Verify `search_agentcore_docs` tool availability
   - Verify `fetch_agentcore_doc` tool availability
   - Test basic connectivity and response

3. **Skip Condition**: If AgentCore MCP server is unavailable or architecture doesn't include AI/ML components, document skip reason and proceed to holistic quality stage

#### AgentCore Architecture Analysis

**Architecture Pattern Validation**:
1. **AI/ML Component Analysis**: 
   - Identify AI agents, ML models, or conversational interfaces in architecture
   - Validate integration patterns with AWS Bedrock services
   - Review agent orchestration and workflow patterns
   - Assess runtime and gateway integration approaches

2. **AgentCore Compatibility Assessment**:
   - Use `search_agentcore_docs` to research relevant patterns for identified components
   - Use `fetch_agentcore_doc` to get detailed documentation for specific integration approaches
   - Validate architecture alignment with AgentCore best practices
   - Assess transformation requirements for AgentCore Runtime compatibility

3. **Service Integration Validation**:
   - Review AWS service integration patterns for AI/ML workloads
   - Validate IAM roles and permissions for Bedrock AgentCore services
   - Assess ECR repository requirements and container deployment patterns
   - Review gateway integration patterns for tool communication

#### AgentCore Validation Report Generation

**Required Deliverable**: `generated/design/supplement-material/agentcore-architecture-validation.md`

**Report Structure**:
```markdown
# AgentCore Architecture Validation Report

## Executive Summary
- **Validation Status**: [APPLICABLE/NOT_APPLICABLE/PASSED/NEEDS_IMPROVEMENT]
- **AI/ML Components Identified**: [Count and types]
- **AgentCore Compatibility**: [Assessment summary]
- **Key Recommendations**: [Top 3-5 recommendations]

## AI/ML Architecture Analysis
### Identified Components
- [List of AI agents, ML models, conversational interfaces]
- [Integration patterns and workflows]
- [Runtime and deployment requirements]

### AgentCore Compatibility Assessment
- **Runtime Integration**: [Compatibility analysis]
- **Gateway Integration**: [Tool communication patterns]
- **Deployment Patterns**: [Container and ECR requirements]
- **Security Configuration**: [IAM roles and permissions]

## Service Integration Validation
### AWS Bedrock Integration
- [Service usage patterns and configurations]
- [Authentication and authorization approaches]
- [Scaling and performance considerations]

### Infrastructure Requirements
- [ECR repository setup requirements]
- [Lambda function configurations for gateway tools]
- [VPC and networking considerations for agent communication]

## Recommendations
### Critical Improvements
- [Must-have changes for AgentCore compatibility]

### Optimization Opportunities  
- [Performance and efficiency improvements]

### Implementation Guidance
- [Specific steps for AgentCore transformation]
- [Deployment sequence recommendations]
- [Testing and validation approaches]

## Conclusion
- **Overall Assessment**: [Summary of architecture readiness]
- **Next Steps**: [Recommended actions before implementation]
```

#### AgentCore Integration Recommendations

**Architecture Enhancement Suggestions**:
1. **Agent Transformation Guidance**: Provide specific recommendations for making agents compatible with AgentCore Runtime
2. **Tool Integration Patterns**: Suggest optimal patterns for AgentCore Gateway tool integration
3. **Deployment Strategy**: Recommend deployment approaches for agent infrastructure
4. **Testing Framework**: Suggest testing approaches for agent validation and integration testing

#### Validation Success Criteria

**AgentCore Validation Passes When**:
- All AI/ML components have clear AgentCore integration paths
- Service integration patterns align with AgentCore best practices
- Security configurations meet AgentCore requirements
- Deployment strategy is feasible and well-documented
- Testing approach validates complete agent workflows

**Skip Criteria**:
- Architecture contains no AI/ML or agent components
- AgentCore MCP server is unavailable
- Customer explicitly requests to skip AgentCore validation

**DELIVERABLE**: Complete `agentcore-architecture-validation.md` report with validation status and specific recommendations for AI/ML architecture components.

## Task Checklist

- [ ] **Task 3.1: Check Intelligence Hub Availability**
  - [ ] **MCP Configuration Verification**
    - [ ] Examine MCP configuration for Intelligence Hub server entry
    - [ ] Verify "disabled" status and document configuration state
    - [ ] Test server connection if enabled in configuration
    - [ ] Document connection status and any error conditions
  - [ ] **Path Selection Decision**
    - [ ] Determine optimal path based on availability assessment
    - [ ] Document path selection rationale (Available → Path A, Unavailable → Path B)
    - [ ] Set execution parameters and timeout configurations
    - [ ] Prepare user communication for expected timeline
  - [ ] **Document Path Selection in Workflow State**
    - [ ] Update `.workflow-state/design-handoff.md` "Architecture Generation Path Selection" section
    - [ ] Check appropriate box (Path A or Path B) based on availability assessment
    - [ ] Document path selection rationale explaining why this path was chosen
    - [ ] Verify documentation is complete before proceeding to Task 3.2

- [ ] **Task 3.2: Generate Architecture Design**
  - [ ] **CRITICAL FIRST STEP: Verify Path Selection**
    - [ ] Read `.workflow-state/design-handoff.md` to check which path was selected in Task 3.1
    - [ ] Check "Architecture Generation Path Selection" section for checked box
    - [ ] Confirm path is documented before proceeding (if not, complete Task 3.1 first)
  - [ ] **MANDATORY PATH CONFIRMATION**
    - [ ] Read the corresponding path section (PATH A or PATH B) in the Task Checklist below
    - [ ] Create a summary of the top-level checklist items for the selected path
    - [ ] Display the summary in chat using the format specified in task description
    - [ ] Verify user can see what checklist items will be executed before proceeding
  - [ ] **Execute ONLY the path documented in workflow state** (do not skip ahead to Task 3.3)
  - [ ] **PATH A: Intelligence Hub Integration** (Execute ONLY if Intelligence Hub available)
    - [ ] **Step A1: Prerequisites Verification and Deep Research Decision**
      - [ ] Verify Intelligence Hub MCP server is available and responsive
      - [ ] Verify requirements package is ready (check `.workflow-state/design-handoff.md`)
      - [ ] Present deep research decision protocol to user
      - [ ] Wait for explicit user response (y/n)
      - [ ] Document user choice and set timeout expectations (15 min standard / 60 min deep research)
      - [ ] Display Step A1 verification checkpoint in chat
    - [ ] **Step A2: Intelligence Hub Job Execution**
      - [ ] Submit job using `mcp_intelligence_hub_submit_job` with complete requirements and user's deep research choice
      - [ ] Capture and display Job ID to user for tracking purposes
      - [ ] Implement enhanced polling protocol (60-second intervals, proper status progression handling)
      - [ ] Monitor status until COMPLETED (not EXPERT_COMPLETED) or timeout occurs
      - [ ] Retrieve results using `mcp_intelligence_hub_get_result` when status is COMPLETED
      - [ ] Save complete JSON response to `architecture/intelligence-hub-response.md`
      - [ ] Format response as markdown with JSON code block for IDE preview compatibility
      - [ ] Display Step A2 verification checkpoint in chat
    - [ ] **Step A3: Expert Insights Integration**
      - [ ] Analyze asset rankings and apply 60% threshold for technology shortlisting
      - [ ] Review expert recommendations from Intelligence Hub response
      - [ ] Incorporate deep research findings if available
      - [ ] Document Intelligence Hub influence on all architecture choices
      - [ ] Display Step A3 verification checkpoint in chat

  - [ ] **PATH B: Standard Architecture Generation** (Execute ONLY if Intelligence Hub unavailable)
    - [ ] **Step B1: Prerequisites Verification**
      - [ ] Document Intelligence Hub unavailability reason in chat
      - [ ] Read `.workflow-state/customer-context.md` and display key project characteristics in chat
      - [ ] Verify customer context is sufficient for architecture decisions
      - [ ] Display Step B1 verification checkpoint in chat
    - [ ] **Step B2: Architecture Guidance Selection**
      - [ ] Read `core-methodology/architecture-guidance-selection.md` to understand the framework
      - [ ] Apply decision hierarchy evaluation using customer context from Step B1
      - [ ] Display decision tree output in chat showing guidance type evaluations and reasoning
      - [ ] Document decision in `.workflow-state/design-handoff.md` under "Key Insights & Decisions"
      - [ ] Extract and document repository links if selected guidance references git repositories
      - [ ] Display repository links in chat and document in design-handoff.md "Reference Architecture Repositories" section
      - [ ] Display Step B2 verification checkpoint in chat
    - [ ] **Step B3: Reference Architecture Analysis** (MANDATORY if reference architectures selected OR existing codebases exist)
      - [ ] **ENFORCEMENT CHECK**: Verify execution is required
        - [ ] Check if Step B2 selected solutions, or prescriptive guidance with repositories
        - [ ] Check if existing codebases exist in `.workflow-state/reference-architectures/`
        - [ ] If either condition is true, B3 execution is MANDATORY
        - [ ] If neither condition is true, B3 can be skipped
      - [ ] **Analyze Existing Codebases** (from Task 2.1 codebase analysis)
        - [ ] Review existing codebases copied to `.workflow-state/reference-architectures/[project-name]/` during requirements generation
        - [ ] Read `PROJECT_ANALYSIS.md` files for each existing codebase to understand current state
        - [ ] Analyze existing architecture patterns, technical debt, and integration constraints
        - [ ] Document current system capabilities and limitations
      - [ ] **Download External References** (from guidance selection)
        - [ ] Read repository links from `.workflow-state/design-handoff.md` "Reference Architecture Repositories" section
        - [ ] Download each documented repository using git clone to `.workflow-state/reference-architectures/[meaningful-folder-name]/`
        - [ ] If git clone fails, ask user how to proceed
        - [ ] Read reference-specific instructions from documented setup paths and standard documentation files
        - [ ] Display key setup guidance in chat for user awareness
      - [ ] **Comprehensive Gap Analysis** (existing systems + external references vs. requirements)
        - [ ] Compare existing codebase capabilities against project requirements
        - [ ] Assess external reference architecture fit for filling gaps
        - [ ] Identify what can be preserved vs. what needs integration/replacement from existing systems
        - [ ] Document integration strategy for existing systems with new architecture
        - [ ] Plan integration path from current state to target architecture
      - [ ] **Create enhanced gap analysis document**: `generated/design/supplement-material/gap-analysis.md` with sections: Executive Summary, Current State Analysis, Reference Architecture Analysis, Gap Identification, Integration Strategy, Technical Debt Management, Risk Assessment, Conclusion
      - [ ] Display Step B3 verification checkpoint in chat (or skip message if not applicable)
    - [ ] **Step B4: Reference Architecture Integration Design** (MANDATORY if Step B3 was executed)
      - [ ] **ENFORCEMENT CHECK**: Verify execution is required
        - [ ] Check if Step B3 was executed
        - [ ] If B3 was executed, B4 execution is MANDATORY
        - [ ] If B3 was skipped, B4 can be skipped
      - [ ] **Legacy System Integration Design**
        - [ ] Design integration approach for existing systems with new architecture
        - [ ] Plan integration strategy from current state to target architecture
        - [ ] Design integration and consistency strategies
        - [ ] Plan service boundaries between existing and new components
      - [ ] **Reference Architecture Integration Design**
        - [ ] Design integration approach for selected solutions as architecture foundation
        - [ ] Plan customization strategy based on gap analysis results from Step B3
        - [ ] Design combination strategy when multiple reference architectures are required
      - [ ] **Comprehensive Integration Strategy**
        - [ ] Document integration architecture combining existing systems, reference architectures, and new components
        - [ ] Plan phased integration approach with rollback strategies
        - [ ] Design testing strategy for legacy system integration validation
      - [ ] **Create enhanced integration design document**: `generated/design/supplement-material/integration-design.md` with sections: Integration Architecture Overview, Legacy System Integration, Component Integration Specifications,  Customization Requirements, Deployment Sequence, Configuration Management, Testing Strategy, Rollback Strategy, Success Criteria
      - [ ] Display Step B4 verification checkpoint in chat (or skip message if not applicable)
    - [ ] **Step B5: Context-Aware Architecture Design**
      - [ ] Determine appropriate mode (POC/Production/Compliance/Budget-Conscious) based on customer context
      - [ ] Apply selected mode to architecture design approach
      - [ ] Complete architecture design with mode-appropriate complexity
      - [ ] Document architecture approach and validation strategy
      - [ ] Display Step B5 verification checkpoint in chat

- [ ] **Task 3.3: Create Architecture Diagrams and Specifications**
  - [ ] **MANDATORY PRE-CONVERGENCE VERIFICATION**
    - [ ] Verify all path-specific work is complete (Path A: Intelligence Hub results saved; Path B: guidance selection, reference analysis, gap analysis complete)
    - [ ] Confirm no steps were skipped in the selected path
    - [ ] If any verification fails, STOP and complete missing steps before proceeding
  - [ ] **System Architecture Design**
    - [ ] Design high-level system components and their interactions with clear boundaries
    - [ ] Define data flow patterns and integration approaches throughout the system
    - [ ] Select technology stack with detailed rationale and trade-off analysis
    - [ ] Plan deployment architecture and infrastructure requirements completely
  - [ ] **Component Specifications**
    - [ ] Define service boundaries and interfaces with precision and compatibility verification
    - [ ] Document data models and schemas completely with relationships and constraints
    - [ ] Create API specifications and contracts with detailed interface definitions
    - [ ] Integrate security architecture throughout all components and data flows
  - [ ] **Architecture Decision Records (ADRs)**
    - [ ] Create individual ADR files in `architecture-decision-records/` folder for each significant decision
    - [ ] Use naming convention `ADR-XXX-[descriptive-title].md` for all ADR files
    - [ ] Include decision context, considered alternatives, selected approach, and implementation implications in each ADR
    - [ ] Document Intelligence Hub influence on decisions (if Path A used) or systematic analysis rationale (if Path B used)
    - [ ] Include deep research impact on decisions if deep research was available and completed
  - [ ] **Technical Specifications and Implementation Planning**
    - [ ] Document detailed component specifications with interfaces and dependencies
    - [ ] Create complete data architecture with flow diagrams and security controls
    - [ ] Develop implementation strategy with phases, milestones, and resource requirements
    - [ ] Complete risk assessment with mitigation strategies and contingency plans

- [ ] **Task 3.4: Validate Architecture Completeness**
  - [ ] **Architecture Completeness Verification**
    - [ ] Read `core-methodology/architecture-integration-validation-guide.md` completely
    - [ ] Verify all functional requirements have corresponding architectural solutions
    - [ ] Confirm non-functional requirements are adequately addressed in architecture design
    - [ ] Validate user stories are supported by architecture components and interfaces
    - [ ] Create and validate requirements traceability matrix for complete coverage
  - [ ] **Component Integration Validation**
    - [ ] Verify component interfaces are properly defined, documented, and compatible
    - [ ] Validate data flow between components is documented, feasible, and secure
    - [ ] Confirm integration patterns are appropriate for requirements and scalable
    - [ ] Test integration assumptions and validate component dependencies
  - [ ] **Service Limits Impact Assessment**
    - [ ] Extract complete inventory of AWS services from proposed architecture
    - [ ] Research current service quotas and limits using official AWS documentation
    - [ ] Document soft limits, hard limits, and regional variations for all identified services
    - [ ] Estimate service usage for both deployment and production scenarios
    - [ ] Identify potential quota constraints, system bottlenecks, and scaling limitations
    - [ ] Develop mitigation strategies including quota increase requests and alternatives
    - [ ] Document service limits considerations and recommendations for implementation planning
  - [ ] **Technical Feasibility Assessment**
    - [ ] Confirm technology choices are appropriate, mature, and suitable for stated requirements
    - [ ] Assess implementation complexity is reasonable, achievable, and within team capabilities
    - [ ] Validate resource requirements are realistic, available, and within project constraints
    - [ ] Identify potential technical risks and develop detailed mitigation approaches
  - [ ] **Documentation Completeness Review**
    - [ ] Verify architecture diagrams and specifications are complete, accurate, and up-to-date
    - [ ] Confirm decision records provide adequate rationale and traceability for all major decisions
    - [ ] Validate implementation guidance is complete, actionable, and sufficient for development teams
    - [ ] Ensure architecture package meets quality standards and is ready for holistic quality assessment
    - [ ] Verify Intelligence Hub JSON response is saved for debugging and audit trail (if Path A used)
    - [ ] Confirm deep research findings are properly documented and integrated (if deep research was completed)
  - [ ] **Create validation report**: `generated/design/supplement-material/architecture-integration-validation.md` with sections: Executive Summary, Architecture Completeness Verification, Component Integration Validation, Service Limits Impact Assessment, Technical Feasibility Assessment, Documentation Completeness Review, Validation Summary, Recommendations
- [ ] **Task 3.5: Validate AI Agent Architecture with AgentCore MCP (Optional)**
  - [ ] **AgentCore MCP Server Availability Assessment**
    - [ ] Check MCP configuration for `awslabs.amazon-bedrock-agentcore-mcp-server` entry
    - [ ] Verify server is enabled (`"disabled": false`) and test connectivity
    - [ ] Verify `search_agentcore_docs` and `fetch_agentcore_doc` tools are available
    - [ ] Document server availability status
  - [ ] **Architecture Applicability Assessment**
    - [ ] Identify AI agents, ML models, or conversational interfaces in architecture
    - [ ] Assess if architecture includes AWS Bedrock services or AI/ML workflows
    - [ ] Determine if architecture includes agentic patterns or autonomous systems
    - [ ] Document applicability decision (APPLICABLE/NOT_APPLICABLE)
  - [ ] **AgentCore Architecture Analysis** (if applicable and server available)
    - [ ] Use `search_agentcore_docs` to research relevant patterns for identified AI/ML components
    - [ ] Use `fetch_agentcore_doc` to get detailed documentation for specific integration approaches
    - [ ] Validate architecture alignment with AgentCore best practices
    - [ ] Assess transformation requirements for AgentCore Runtime compatibility
    - [ ] Review AWS service integration patterns for AI/ML workloads
    - [ ] Validate IAM roles and permissions for Bedrock AgentCore services
  - [ ] **Generate AgentCore Validation Report**
    - [ ] Create `supplement-material/agentcore-architecture-validation.md` following report structure
    - [ ] Include Executive Summary with validation status (APPLICABLE/NOT_APPLICABLE/PASSED/NEEDS_IMPROVEMENT)
    - [ ] Document AI/ML components analysis and AgentCore compatibility assessment
    - [ ] Provide specific recommendations for AgentCore integration and transformation
    - [ ] Include implementation guidance and testing approaches for agent workflows
