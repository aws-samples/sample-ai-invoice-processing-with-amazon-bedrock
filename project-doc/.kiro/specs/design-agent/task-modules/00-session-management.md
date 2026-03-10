# Session Management and Execution Modes

## Overview

This module handles session management, execution mode detection, and handoff protocols for the Design Agent workflow. It provides the foundation for reliable workflow execution across multiple sessions and user interaction patterns.

**IMPORTANT**: Tasks 0.1, 0.2, and 0.3 are executable tasks that must be completed and documented in design-handoff.md before proceeding to Stage 1. Follow the same BEFORE/AFTER update protocol as other stages.

## Prerequisites

### Required Files
- **Context Files**: `requirements.md` and `design.md` in current folder
- **Progress State**: `.workflow-state/design-handoff.md` 
- **Input Sources**: Project documents in `project-doc/` folder OR user-provided context

## Smart Execution Guide

**CRITICAL**: Follow Task 0.1 → Task 0.2 → Task 0.3 in sequence, updating design-handoff.md BEFORE and AFTER each task.
3. **Handle project input sources** - Support multiple input scenarios
   - **Existing documents**: project-doc folder with files (traditional workflow)
   - **Start from scratch**: Empty or missing project-doc folder with user-provided context
   - **Mixed approach**: Some documents plus additional context from user
   - **If project-doc missing/empty AND no user context**: Ask user to provide project description or create project-doc folder

4. **Extract project name** - Determine project folder name for output organization
   - **From customer context**: Look for project name, system name, or application name
   - **From project documents**: Extract from titles, headers, or file names
   - **Format**: Convert to kebab-case (lowercase with hyphens): `knowledge-base-assistant`
   - **Fallback**: Use `project-specification` if no clear name identified
   - **Document**: Record project name in customer-context.md for later use

## Handoff Update Requirements

**[CRITICAL] YOU MUST UPDATE `.workflow-state/design-handoff.md` TWICE FOR EVERY TASK - NO EXCEPTIONS!**

The progress UI in the extension depends on these updates. If you skip them, users cannot see workflow progress.

### BEFORE Starting ANY Task:
1. Read current design-handoff.md
2. Use `strReplace` to update `<workflow-status>` JSON:
   - **CRITICAL**: Maintain proper markdown format with ```json at start and ``` at end
   - Set current task `status` to `"current"` in `taskDetails` array
   - Update `activeTask` to current task name
   - Update `status` to `"in-progress"` (if not already)
   - Update `lastUpdated` timestamp
3. Verify: JSON is valid, proper markdown formatting maintained, current task shows `"current"`, `activeTask` matches current task

### AFTER Completing ANY Task:
1. Read current design-handoff.md
2. Use `strReplace` to update `<workflow-status>` JSON:
   - **CRITICAL**: Maintain proper markdown format with ```json at start and ``` at end
   - Set completed task `status` to `"complete"` in `taskDetails` array
   - Set NEXT task `status` to `"current"` in `taskDetails` array
   - Increment `overallProgress.completed` by 1
   - Recalculate `overallProgress.percentage` = (completed / total) * 100
   - Update `activeTask` to NEXT task name
   - Update `lastUpdated` timestamp
3. Update other sections (Files Created, Key Insights, etc.)
4. Verify: JSON is valid, proper markdown formatting maintained, completed task shows `"complete"`, next task shows `"current"`, counts and percentage are correct

### Warning: If You Skip These Updates
- Users see "Ready to Start" even though you're working
- No task checkmarks appear
- No loading spinners show
- Users cannot track progress
- **The workflow appears broken to users**

## User Intent Detection & Execution Mode

**ALWAYS check user's current request for execution preference:**
- **"next task", "one task", "just this task"** → Execute single task only
- **"finish", "complete", "run all", "do everything"** → Execute remaining tasks to completion
- **Ambiguous request** → Ask: "Execute just the next task, or run all remaining tasks to completion?"

**Reading design-handoff.md (always exists):**
- Parse JSON status to understand current workflow state
- Read progress and determine next task
- **Respect current user intent** (may be different from previous sessions)
- Apply complexity assessment only for fresh workflows (status: "ready")

**Fresh workflow detection:**
- Assess input complexity and recommend approach
- **Start from scratch**: Empty/missing project-doc folder with user context → Auto proceed with full workflow (simple input)
- **Simple documents**: 1-3 files, mostly text/markdown, <5MB total → Auto proceed with full workflow
- **Moderate documents**: 4-8 files or mixed formats or 5-15MB total → Recommend single task approach, ask preference
- **Complex documents**: 9+ files or large PDFs/presentations or >15MB total → Strongly recommend single task approach (session timeout risk)

## Input Source Handling

**CRITICAL**: The Design Agent workflow supports multiple input scenarios. Always identify and validate input sources before proceeding.

### Input Scenarios

#### 1. **Existing Project Documents** (Traditional)
- **Condition**: project-doc folder exists and contains files
- **Action**: Proceed with document analysis as primary input
- **Complexity Assessment**: Based on file count, types, and sizes
- **Customer Context**: Supplement document analysis with targeted questions

#### 2. **Start From Scratch** (User Context Only)
- **Condition**: Empty/missing project-doc folder + user provides context (description, images, requirements)
- **Action**: Use user-provided context as primary input source
- **Complexity Assessment**: Treat as "Simple" - auto proceed with full workflow
- **Customer Context**: Capture comprehensive context through conversation
- **Example**: "We don't have anything in project-docs, but want to create the POC described in the image below!"

#### 3. **Mixed Input** (Documents + Additional Context)
- **Condition**: Some documents exist + user provides additional context
- **Action**: Combine document analysis with user-provided context
- **Complexity Assessment**: Based on document complexity + context richness
- **Customer Context**: Use documents as baseline, enhance with user input

#### 4. **Insufficient Input** (No Documents, No Context)
- **Condition**: Empty/missing project-doc folder + no meaningful user context
- **Action**: Request clarification from user
- **Options**: "Please either: 1. Add documents to project-doc folder, 2. Describe your project goals and requirements, or 3. Provide images/sketches of what you want to build"

### Input Validation Protocol

**For each session, determine input scenario:**
1. **Check project-doc folder**: Exists? Contains files? What types/sizes?
2. **Analyze user request**: Contains project description? References images? Provides requirements?
3. **Classify scenario**: Existing docs, start from scratch, mixed, or insufficient
4. **Proceed accordingly**: Use appropriate workflow path based on scenario

## Execution Modes

**Single Task:** Execute next task only, update design-handoff.md, tell user how to continue
**Full Workflow:** Execute all remaining tasks, update design-handoff.md after EACH task

## Customer Context Capture

**CRITICAL**: Customer context must be captured and preserved to enable context-aware architecture decisions aligned with Well-Architected Framework principles.

### Context Categories

#### 1. Project Goals & Constraints
**Purpose**: Understand project scope, timeline, and business requirements to inform architecture complexity and trade-off decisions.

**Context to Capture**:
- **Project Type**: POC/Prototype, MVP, Production system, Migration project
- **Timeline Constraints**: Delivery deadlines, milestone requirements, time-to-market pressures
- **Budget Constraints**: Cost optimization priorities, budget limitations, spending flexibility
- **Compliance Requirements**: HIPAA, PCI-DSS, SOC2, FedRAMP, GDPR, industry-specific regulations
- **Availability Requirements**: Uptime targets, disaster recovery needs, business continuity requirements
- **Scale Requirements**: Expected user load, data volume, geographic distribution, growth projections
- **Success Metrics**: Performance targets, user capacity, response times, business KPIs
- **Project Stakeholders**: Business sponsor, technical lead, security/compliance representatives

#### 2. Technical Preferences
**Purpose**: Align technology choices with team expertise and organizational standards to reduce implementation risk.

**Context to Capture**:
- **Infrastructure Preference**: Serverless, Container-based (ECS/EKS), EC2-based, Hybrid approaches
- **Infrastructure as Code (IaC)**: CDK, Terraform, CloudFormation, Pulumi, or no preference
- **Development Stack**: Programming languages, frameworks, existing technology investments
- **Data Storage Preference**: Relational databases, NoSQL, Data lakes, Hybrid data architecture
- **Security Posture**: Standard AWS security, Enhanced security controls, Zero-trust architecture, Compliance-driven security
- **Vendor Preferences**: AWS-native services, Multi-cloud, Avoid specific services/vendors
- **Operational Preferences**: Managed services vs self-managed, automation level, monitoring tools

#### 3. Organizational Context
**Purpose**: Consider team capabilities and organizational maturity to ensure realistic architecture recommendations.

**Context to Capture**:
- **Team Expertise**: AWS experience level, technology stack familiarity, DevOps maturity
- **Operational Maturity**: Monitoring practices, automation level, incident response capabilities
- **Existing Infrastructure**: Current AWS usage, legacy systems, integration requirements
- **Organizational Constraints**: Security policies, approval processes, change management requirements
- **Support Model**: Internal team support, AWS support level, third-party support arrangements
- **Existing Documentation**: Current architecture docs, design decisions, integration constraints

### Context Capture Principles

#### Essential Context Categories
Customer context must cover three critical areas to enable informed architecture decisions:

1. **Project Goals & Constraints** - Business requirements, timeline, and success criteria
2. **Technical Preferences** - Technology choices, infrastructure preferences, and development standards  
3. **Organizational Context** - Team capabilities, operational maturity, and existing infrastructure

Missing context in any category significantly impacts architecture quality and alignment with business needs.

#### Context Validation Questions
**When essential context is unclear or missing, use targeted questions to gather critical information:**

**Essential Questions (Always Ask)**:
- **Project Type (POC vs Production)**: NEVER assume based on context signals. If context suggests a type, read back your interpretation and ask for confirmation. Otherwise, ask directly.
- "Are there specific compliance requirements I should consider (HIPAA, PCI-DSS, etc.)?"
- "Do you have preferences for serverless vs container-based architecture?"
- "What's your team's experience level with AWS services?"
- "Do you have existing AWS infrastructure this needs to integrate with?"

**Clarifying Questions (Ask If Relevant)**:
- "What's more important: cost optimization or performance?" *(if budget concerns mentioned)*
- "Do you prefer CDK, Terraform, or CloudFormation for infrastructure as code?" *(if IaC mentioned)*
- "What are the expected performance requirements (users, throughput, response times)?" *(if scale mentioned)*

**Context to Use If Provided (Don't Actively Ask)**:
- Stakeholder details and organizational approval processes
- Specific technology stack preferences and vendor constraints
- Detailed operational and monitoring preferences

#### Context Documentation Standards
**Customer context should be documented in structured format for consistent reference:**

**IMPORTANT: Handling Compliance Requirements**
- When customer mentions compliance needs (HIPAA, GDPR, SOC 2, PCI-DSS, etc.), document as stated by customer
- DO NOT interpret what the regulation requires
- DO NOT assess whether customer meets compliance requirements
- DO NOT make compliance claims
- Document: "Customer stated requirement for [regulation name]" 
- Note: Customer should consult their own independent legal counsel for specific compliance requirements (per Legal and Compliance Boundaries in collaboration-workflow.md)

```markdown
# Customer Context

## Project Goals & Constraints
- Project Type: [POC/MVP/Production/Migration]
- Timeline: [specific deadlines or constraints]
- Budget: [cost optimization priorities]
- Compliance: [Customer's stated compliance considerations]
- Availability: [uptime targets, DR needs]
- Scale: [user load, data volume, growth]
- Success Metrics: [performance targets, KPIs]
- Stakeholders: [business sponsor, technical lead]

## Technical Preferences  
- Infrastructure: [serverless/containers/EC2/hybrid]
- IaC: [CDK/Terraform/CloudFormation/other]
- Development: [languages, frameworks, existing tech]
- Data Storage: [relational/NoSQL/data lake/hybrid]
- Security: [standard/enhanced/zero-trust/compliance-driven]
- Vendor: [AWS-native/multi-cloud/avoid specific services]

## Organizational Context
- Team Expertise: [AWS experience, technology familiarity]
- Operational Maturity: [monitoring, automation, DevOps practices]
- Existing Infrastructure: [current AWS usage, legacy systems]
- Constraints: [security policies, approval processes]
- Support Model: [internal/AWS/third-party support]
- Documentation: [existing architecture docs, design decisions]
```

#### Context Integration Principles
**Customer context must inform all architecture decisions:**
- Technology selection should align with team expertise and organizational standards
- Architecture complexity should match project type (POC vs Enterprise)
- Trade-off decisions should reflect customer priorities and constraints
- All architecture recommendations should validate against captured context

### Context-Driven Architecture Decisions

Customer context enables informed architectural trade-offs based on business priorities. For example, prioritize resilience recommendations when availability goals are critical, even with cost impact, or choose simpler architectures for POC projects to accelerate validation.

## Session Recovery Protocol

**File Structure Reference**: See main [tasks.md](../tasks.md) "File Structure & Storage Locations" section for complete storage location definitions.

**Prerequisites Verification**:
- Input sources identified (project documents, user context, images, or combination)
- **Customer context captured and documented** in `.workflow-state/customer-context.md`

**CRITICAL: Update `.workflow-state/design-handoff.md` TWICE per task - before starting AND after completing:**

### **STEP 1 - Before Starting Each Task:**
Update the <workflow-status> JSON block using strReplace:
- **"activeTask"**: Set to current task name (e.g., "Task 1.1 - Input Assessment Analysis")
- **"status"**: Set to "in-progress" 
- **"taskDetails"**: Update the specific task status to "current"
- **"lastUpdated"**: Set to current timestamp
- **Purpose**: Shows user that task is actively starting

### **STEP 2 - After Completing Each Task:**
Update multiple sections using strReplace:

**JSON Status Update** (in <workflow-status> tags):
- **"overallProgress"**: Update completed count and percentage
- **"currentStageProgress"**: Update stage-specific progress if stage changes
- **"activeTask"**: Set to NEXT task name (e.g., "Task 1.2 - Package Generation")
- **"taskDetails"**: Update completed task to "complete" and next task to "current"
- **"status"**: Keep as "in-progress" (or "completed" if final task)
- **"lastUpdated"**: Set to current timestamp

**Other Sections**:
- **Task Completion Status**: Mark current task with [X] (keep for human readability)
- **Files Created/Updated**: Add files created during this task
- **Key Insights & Decisions**: Document important findings from this task
- **Issues Encountered**: Note any problems faced and resolutions
- **Next Task Details**: Update with next task information

## TaskDetails Array Management

**When Starting a Task:**
```json
"taskDetails": [
  {
    "taskNumber": "0.1",
    "taskName": "Project Complexity Assessment", 
    "status": "current"  // ← Changed from "not_started"
  }
]
```

**When Completing a Task:**
```json
"taskDetails": [
  {
    "taskNumber": "0.1",
    "taskName": "Project Complexity Assessment",
    "status": "complete"  // ← Changed from "current"
  },
  {
    "taskNumber": "1.1", 
    "taskName": "Input Assessment Analysis",
    "status": "current"   // ← Changed from "not_started"
  }
]
```

**When Restarting a Task:**
```json
"taskDetails": [
  {
    "taskNumber": "1.2",
    "taskName": "Requirements Generation", 
    "status": "current"   // ← Changed from "complete" back to "current"
  },
  {
    "taskNumber": "1.3",
    "taskName": "Basic Completeness Check",
    "status": "not_started"  // ← Reset from "current" back to "not_started"
  }
]
```

## Update Examples

**Example - Before Starting Task 0.1:**
```json
{
  "workflowStage": "Stage 0 - Project Analysis",
  "activeTask": "Task 0.1 - Project Complexity Assessment",
  "overallProgress": {
    "completed": 0,
    "total": 12,
    "percentage": 0
  },
  "taskDetails": [
    {
      "taskNumber": "0.1",
      "taskName": "Project Complexity Assessment",
      "status": "current"
    },
    {
      "taskNumber": "1.1",
      "taskName": "Input Assessment Analysis",
      "status": "not_started"
    }
  ],
  "status": "in-progress",
  "lastUpdated": "2024-03-15T10:30:00Z"
}
```

**Example - After Completing Task 0.1:**
```json
{
  "workflowStage": "Stage 1 - Requirements Generation",
  "activeTask": "Task 1.1 - Input Assessment Analysis",
  "overallProgress": {
    "completed": 1,
    "total": 12,
    "percentage": 8
  },
  "taskDetails": [
    {
      "taskNumber": "0.1",
      "taskName": "Project Complexity Assessment",
      "status": "complete"
    },
    {
      "taskNumber": "1.1",
      "taskName": "Input Assessment Analysis",
      "status": "current"
    },
    {
      "taskNumber": "1.2",
      "taskName": "Requirements Generation",
      "status": "not_started"
    }
  ],
  "status": "in-progress",
  "lastUpdated": "2024-03-15T10:45:00Z"
}
```

## Handling Task Restarts

**When you need to restart or redo a previous task:**

1. **Before Restarting**: Update JSON to revert progress to the actual completion state
2. **Document Reason**: Add explanation in "Issues Encountered" section  
3. **Follow Normal Pattern**: Then use normal before/after update pattern for the restarted task

**Example - Restarting Task 1.2 after it was marked complete:**
```json
{
  "workflowStage": "Stage 1 - Requirements Generation",
  "activeTask": "Task 1.2 - Requirements Generation",
  "overallProgress": {
    "completed": 1,     
    "total": 12,
    "percentage": 8    
  },
  "taskDetails": [
    {
      "taskNumber": "1.1",
      "taskName": "Input Assessment Analysis",
      "status": "complete"
    },
    {
      "taskNumber": "1.2",
      "taskName": "Requirements Generation",
      "status": "current"
    },
    {
      "taskNumber": "1.3",
      "taskName": "Basic Completeness Check",
      "status": "not_started"
    }
  ],
  "currentStageProgress": {
    "stage": 1,
    "stageName": "Requirements Generation",
    "stageCompleted": 1,  
    "stageTotal": 3
  },
  "status": "in-progress",
  "lastUpdated": "2024-03-15T11:30:00Z"
}
```

## Quality Assessment Iterations

**When starting a new quality assessment iteration (Task 3.2):**
- **Do NOT revert progress** - iterations build on previous work
- **Update activeTask** to current iteration task
- **Document iteration number** in task name or Issues Encountered section

**Example - Starting Quality Assessment Iteration 2:**
```json
{
  "workflowStage": "Stage 3 - Holistic Quality Assessment",
  "activeTask": "Task 3.2 - Iterative Improvement (Iteration 2)",
  "overallProgress": {
    "completed": 8,     
    "total": 12,
    "percentage": 67    
  },
  "status": "in-progress",
  "lastUpdated": "2024-03-15T14:30:00Z"
}
```

## Common Restart Scenarios

| Scenario | Action | Progress Impact | Task Status Update |
|----------|--------|-----------------|-------------------|
| **Redo single task** | Revert progress to before that task | Decrease percentage | Set task to "current", later tasks to "not_started" |
| **Quality assessment iteration** | Keep progress, update task name | Maintain percentage | Keep task as "current" |
| **Stage restart** | Revert to beginning of stage | Decrease to stage start | Set stage tasks to "not_started", first to "current" |
| **Complete workflow restart** | Revert to 0% | Reset all progress | Set all tasks to "not_started", Task 0.1 to "current" |

## Session Continuation Messages

**For Single Task mode, also tell user:**
"Task [X] complete. To continue with next task, start a new session using the same prompt you used, or use `Execute resources/internal/config/specs/design-agent/tasks.md` - I'll read design-handoff.md and pick up where we left off."

**Session Recovery:** 
- I'll read .workflow-state/design-handoff.md and continue exactly where we left off

## Task Descriptions

### Task 0.1: Prepare Workflow

**Purpose**: Read workflow context, identify input sources, and understand current progress.

**Actions**:
1. Read `requirements.md` and `design.md` for workflow goals and approach
2. Read `.workflow-state/design-handoff.md` for current progress
3. Parse JSON status to understand current task and progress
4. **Update handoff - mark as current**: Set Task 0 and Task 0.1 to "current", update activeTask
5. Identify and validate input sources (project-doc folder, user context, images, or combination)
6. Classify input scenario (existing docs, start from scratch, mixed, insufficient)
7. Document input scenario in `.workflow-state/design-handoff.md`
8. **Update handoff - mark as complete**: Set Task 0.1 to "complete", Task 0.2 to "current"

**Completion Criteria**:
- Context understood, progress identified
- Input sources identified and scenario classified
- Status updated BEFORE and AFTER
- Ready for Task 0.2

### Task 0.2: Collect Project Information

**Purpose**: Capture customer context and determine execution mode (single task vs full workflow).

**Prerequisites**:
- Workflow context initialized from Task 0.1
- User request analyzed

**Actions**:
1. **Capture Customer Context** (if not already captured):
   - Project goals and constraints (type, timeline, budget, compliance, scale)
   - Technical preferences (infrastructure, IaC, development stack, security)
   - Organizational context (team expertise, operational maturity, existing infrastructure)
   - Document in `.workflow-state/customer-context.md`

2. **Detect User Intent** for execution preference:
   - "next task", "one task", "just this task" → Single task mode
   - "finish", "complete", "run all", "do everything" → Full workflow mode
   - Ambiguous → Ask user preference

3. **Document Execution Mode**: Record determined mode in design-handoff.md

**Completion Criteria**:
- Customer context captured (if needed) and documented
- Execution mode determined and documented
- User expectations set for workflow execution

### Task 0.3: Verify Setup Complete

**Purpose**: Final validation checkpoint before proceeding to Stage 1.

**Prerequisites**:
- Task 0.1 and 0.2 completed

**Validation Checklist**:
1. **Verify Prerequisites Met**:
   - `.workflow-state/design-handoff.md` exists and has valid JSON
   - `.workflow-state/customer-context.md` exists with captured context
   - Execution mode determined and documented

2. **Confirm Handoff Protocol Understanding**:
   - BEFORE/AFTER update requirements understood
   - Cascading rules for parent/subtask status understood
   - JSON structure validation confirmed

3. **Ready for Stage 1**:
   - All Stage 0 setup complete
   - No blockers to proceeding with Project Analysis

**Completion Criteria**:
- All validations passed
- Ready to proceed to Stage 1 (Project Analysis)

### Task Checklist

- [ ] **Task 0.1: Prepare Workflow**
  - [ ] Read `requirements.md` and `design.md` for workflow goals and approach
  - [ ] Read `.workflow-state/design-handoff.md` for current progress
  - [ ] Parse JSON status to understand current task and progress
  - [ ] Identify and validate input sources (project-doc folder, user context, images, or combination)
  - [ ] Classify input scenario (existing docs, start from scratch, mixed, insufficient)
  - [ ] Document input scenario in `.workflow-state/design-handoff.md`

- [ ] **Task 0.2: Collect Project Information**
  - [ ] Capture customer context (if not already captured): project goals, technical preferences, organizational context
  - [ ] Document context in `.workflow-state/customer-context.md`
  - [ ] Detect user intent for execution preference (single task vs full workflow)
  - [ ] Document execution mode in design-handoff.md

- [ ] **Task 0.3: Verify Setup Complete**
  - [ ] Verify `.workflow-state/design-handoff.md` exists and has valid JSON
  - [ ] Verify `.workflow-state/customer-context.md` exists with captured context
  - [ ] Confirm execution mode determined and documented
  - [ ] Confirm BEFORE/AFTER update requirements understood
  - [ ] Confirm ready to proceed to Stage 1 (Project Analysis)
