# Task 8+: Incorporate Feedback (Iteration N)

Generate dynamic improvement tasks based on stakeholder feedback documents.

## Before Starting

**CRITICAL DISTINCTION**: This task creates NEW PROJECT FOLDERS only for stakeholder feedback iterations, NOT quality improvement iterations.

**Quality Iterations** (within same project):
- specification-package-iteration-1, specification-package-iteration-2, etc.
- Handled by Task 4 (Holistic Quality Assessment)
- Stay within same project folder: `generated/design/[project-name]/`

**Feedback Iterations** (new project folders):
- Only when stakeholder provides feedback documents in `project-doc/feedback/iteration-N/`
- Creates new project folders: `[project-name]-feedback-iteration-1/`, `[project-name]-feedback-iteration-2/`, etc.
- Complete project regeneration based on feedback collected from the feedback folder

The feedback iteration number is **computed by counting existing feedback folders** in `project-doc/feedback/`. Count existing `iteration-*` folders and add 1 for the next iteration.

## Step 1: Change Detection and Analysis

**Step 1.1: Load Processing History**
```bash
# Load previous processing history if exists
if [ -f ".workflow-state/processing-history.md" ]; then
    echo "Loading previous processing history..."
    # Extract previous file fingerprints and processing metadata
else
    echo "No processing history found - treating as initial feedback iteration"
fi
```

**Processing History File Format** (`.workflow-state/processing-history.md`):
```markdown
# Processing History

## Iteration 1 - 2025-01-15 14:30:00
**Type:** Initial Generation
**Files Processed:** 12
**Total Fingerprints:** 12

### File Fingerprints
- `project-doc/project-context/requirements.md`: sha256:abc123def456...
- `project-doc/technical-knowledge/api-docs.md`: sha256:def456ghi789...
- `project-doc/organization-context/security-policy.md`: sha256:ghi789jkl012...

## Iteration 2 - 2025-01-20 16:45:00
**Type:** Feedback Integration
**Files Processed:** 5 (3 new, 2 modified)
**Files Reused:** 10 (unchanged)
**Conflicts Resolved:** 1 critical
**Processing Time:** 45 minutes (vs 120 minutes full regeneration)

### Change Summary
**New Files:**
- `project-doc/feedback/iteration-2/customer-meeting.md`: sha256:mno345pqr678...

**Modified Files:**
- `project-doc/project-context/requirements.md`: sha256:stu901vwx234... (was abc123def456...)

**Removed Files:**
- `project-doc/project-code/legacy-system/old-api.md`: (removed)

### File Fingerprints (Current)
[Complete list of all current file fingerprints...]
```

**Step 1.2: Scan Current Inputs and Generate Fingerprints**
```bash
# Count existing feedback folders to determine current iteration
ITERATION=$(find project-doc/feedback/ -maxdepth 1 -type d -name "iteration-*" 2>/dev/null | wc -l)
ITERATION=$((ITERATION + 1))
FEEDBACK_DIR="project-doc/feedback/iteration-${ITERATION}"

# Alternative method: Count existing feedback tasks in design-handoff.md
# ITERATION=$(grep -o '"taskName": "Feedback Iteration [0-9]*"' .workflow-state/design-handoff.md | wc -l)
# ITERATION=$((ITERATION + 1))

# Generate SHA-256 fingerprints for all input files
find project-doc/ -type f -exec sha256sum {} \; > .workflow-state/current-fingerprints.tmp

# List all feedback files
find "$FEEDBACK_DIR" -type f
```

**Step 1.3: Categorize Changes**
```bash
# Compare current fingerprints against processing history
# Categorize as: NEW, MODIFIED, REMOVED, UNCHANGED
```

**Current Fingerprints File Format** (`.workflow-state/current-fingerprints.tmp`):
```
abc123def456ghi789jkl012mno345pqr678stu901vwx234  project-doc/project-context/requirements.md
def456ghi789jkl012mno345pqr678stu901vwx234yza567  project-doc/technical-knowledge/api-docs.md
ghi789jkl012mno345pqr678stu901vwx234yza567bcd890  project-doc/organization-context/security-policy.md
jkl012mno345pqr678stu901vwx234yza567bcd890efg123  project-doc/feedback/iteration-2/stakeholder-review.md
```
**Note:** This is a temporary file generated during processing and cleaned up after change categorization is complete.

**Step 1.4: Generate Change Summary**
Create `.workflow-state/change-summary-iteration-${ITERATION}.md` documenting:
- New files discovered
- Modified files with fingerprint changes
- Removed files no longer present
- Processing strategy (incremental vs full)
- Estimated time savings

**Change Summary File Format** (`.workflow-state/change-summary-iteration-N.md`):
```markdown
# Change Summary - Iteration N

## Processing Strategy
**Mode:** Incremental Processing
**Previous Iteration:** Iteration N-1 (2025-01-15 14:30:00)
**Current Iteration:** Iteration N (2025-01-20 16:45:00)

## Change Detection Results

### New Files (3)
- `project-doc/feedback/iteration-N/stakeholder-review.md`
  - **Size:** 2.4 KB
  - **Fingerprint:** sha256:abc123def456...
  - **Analysis:** Full analysis required

### Modified Files (2)
- `project-doc/project-context/requirements.md`
  - **Previous:** sha256:def456ghi789...
  - **Current:** sha256:ghi789jkl012...
  - **Analysis:** Differential analysis required

### Removed Files (1)
- `project-doc/project-code/legacy-system/old-api.md`
  - **Impact:** Remove related integration requirements

### Unchanged Files (15)
- Files with matching fingerprints - reuse cached analysis

## Processing Efficiency
- **Files to Process:** 5 (3 new + 2 modified)
- **Files to Reuse:** 15 (cached analysis)
- **Estimated Time Savings:** 65% (45 min vs 120 min full regeneration)
- **Cache Hit Rate:** 75%
```

**Expected feedback types:**
- Stakeholder review comments
- Technical review feedback
- Security assessment findings
- Business requirement clarifications
- Architecture improvement suggestions
- User story refinements

## Step 2: Conflict Detection and Analysis

**Step 2.1: Load Previous Specifications**
```bash
# Identify most recent project iteration folder
LATEST_ITERATION=$(ls -1 generated/design/ | grep "project-name-iteration-" | sort -V | tail -1)
echo "Loading specifications from: $LATEST_ITERATION"

# Load all specification documents:
# - Requirements documents
# - Architecture specifications  
# - ADRs (Architecture Decision Records)
# - Quality assessment results
# - Security threat model
```

**Step 2.2: Incremental Feedback Processing**
For each feedback document, perform incremental analysis:
- **New Files**: Full analysis and integration with existing analysis
- **Modified Files**: Differential analysis to extract only new/changed information
- **Unchanged Files**: Reuse cached analysis from previous iteration

**Step 2.3: Semantic Conflict Detection**
Compare new feedback against existing requirements and decisions:

### Conflict Types to Detect:
- **Direct Contradiction**: New feedback explicitly contradicts previous requirement
- **Implicit Conflict**: New feedback implies different approach than existing architecture  
- **Scope Conflict**: New feedback changes project boundaries
- **Technical Conflict**: New feedback requires incompatible technology choices

### Conflict Analysis Process:
1. Extract requirements and constraints from new feedback
2. Compare against existing requirements using semantic analysis
3. Identify contradictions using pattern matching
4. Classify conflict severity: CRITICAL, MAJOR, MINOR

**Step 2.4: Generate Conflict Report**
Create `.workflow-state/conflicts-iteration-${ITERATION}.md` with:
- Detailed conflict descriptions
- Original vs new requirements
- Resolution options with pros/cons
- Recommended resolution with rationale
- Impact analysis for each conflict

**Conflict Report File Format** (`.workflow-state/conflicts-iteration-N.md`):
```markdown
# Conflicts Report - Iteration N

## Executive Summary
- **Total Conflicts:** 2
- **Critical:** 1, **Major:** 1, **Minor:** 0
- **Estimated Resolution Time:** 2 hours
- **Architecture Impact:** Yes

## Conflict Details

### Conflict 1: Authentication Method [CRITICAL]

#### Original Decision (Iteration 1)
**Requirement:** FR-001 - Users shall authenticate using OAuth 2.0
**Source:** project-doc/project-context/requirements.md (line 45)
**Rationale:** Customer requested social login integration
**Stakeholder:** Product Manager (John Smith)

#### New Feedback (Iteration N)
**Requirement:** Users shall authenticate using SAML 2.0 for enterprise SSO
**Source:** project-doc/feedback/iteration-N/stakeholder-review.md (line 12)
**Rationale:** IT security requires SAML for compliance
**Stakeholder:** Security Team (Jane Doe)

#### Conflict Analysis
- **Type:** Direct Contradiction
- **Severity:** CRITICAL
- **Root Cause:** Conflicting authentication requirements
- **Affected Components:**
  - Requirements: FR-001, FR-002, FR-003
  - Architecture: Identity Management Component
  - ADRs: ADR-003 (superseded)
  - Security: Authentication flow, session management

#### Resolution Options

##### Option 1: Accept New (SAML 2.0)
**Description:** Replace OAuth with SAML authentication
**Pros:**
- Meets compliance requirements
- Enterprise SSO integration
**Cons:**
- Requires authentication redesign
- Delays implementation timeline
**Effort:** HIGH (2 weeks)
**Risk:** MEDIUM
**Timeline Impact:** 2 weeks delay

##### Option 2: Keep Original (OAuth 2.0)
**Description:** Maintain OAuth, document SAML consideration
**Pros:**
- No rework required
- Maintains current timeline
**Cons:**
- Doesn't meet compliance requirements
- May block enterprise deployment
**Effort:** LOW (documentation only)
**Risk:** HIGH (compliance failure)
**Timeline Impact:** No delay

##### Option 3: Merge Both (Hybrid Authentication)
**Description:** Support both OAuth and SAML authentication
**Pros:**
- Maximum flexibility
- Satisfies all stakeholders
**Cons:**
- Increased complexity
- Higher maintenance overhead
**Effort:** HIGH (3 weeks)
**Risk:** MEDIUM
**Timeline Impact:** 3 weeks delay

#### Recommended Resolution
**Option 1: Accept New (SAML 2.0)**
**Rationale:** Compliance requirements are non-negotiable for enterprise deployment
**Critical Success Factors:** 
- SAML IdP integration planning
- Authentication flow redesign
- Security testing framework update

#### User Decision Required
**Status:** PENDING USER RESOLUTION
**Options:** [1/2/3/Custom]
**Custom Resolution:** [User input field]
```

## Step 3: Comprehensive Feedback Analysis

Read ALL feedback documents to understand requested improvements. Categorize feedback by:

### Category 1: Requirements Changes
- New functional requirements
- Modified acceptance criteria
- Clarified user stories
- Updated business constraints

### Category 2: Architecture Modifications
- System design changes
- Component additions/removals
- Integration pattern updates
- Technology stack changes

### Category 3: Security Enhancements
- New threat mitigations
- Security control additions
- Compliance requirement updates
- Data protection improvements

### Category 4: Quality Improvements
- Performance optimizations
- Scalability enhancements
- Reliability improvements
- Cost optimization suggestions

## Step 4: Conflict Resolution (User Interaction)

**CRITICAL**: If conflicts were detected in Step 2.4, the workflow MUST pause here for user resolution.

**Step 4.1: Present Conflicts to User**
For each conflict identified:
1. Display conflict details clearly
2. Show original decision vs new feedback
3. Present resolution options with impact analysis
4. Highlight recommended resolution with rationale

**Step 4.2: Collect User Decisions**
For each conflict, prompt user to select resolution option:
- **Accept New**: Replace original with new requirement
- **Keep Original**: Preserve original, document feedback consideration
- **Merge Both**: Integrate both requirements (if feasible)
- **Custom Resolution**: User-defined resolution approach

**Step 4.3: Document Resolution Decisions**
Record user decisions with rationale in conflict resolution log.

**Conflict Resolution Log File Format** (`.workflow-state/conflict-resolution-log-iteration-N.md`):
```markdown
# Conflict Resolution Log - Iteration N

## Resolution Session
**Date:** 2025-01-20 16:45:00
**Decision Maker:** [Name/Role]
**Total Conflicts:** 2
**Resolution Time:** 45 minutes

## Conflict Resolutions

### Conflict 1: Authentication Method
**Decision:** Option 1 - Accept New (SAML 2.0)
**Decision Maker:** Technical Lead (Alice Johnson)
**Timestamp:** 2025-01-20 16:30:00
**Rationale:** "Compliance requirements are non-negotiable for enterprise deployment. The 2-week delay is acceptable given the business impact of compliance failure."
**Implementation Notes:** 
- Schedule SAML IdP integration planning session
- Update authentication component design
- Revise security threat model
- Plan comprehensive testing approach

### Conflict 2: Scalability Requirements
**Decision:** Option 1 - Accept New (10,000 concurrent users)
**Decision Maker:** Product Manager (Bob Smith)
**Timestamp:** 2025-01-20 16:40:00
**Rationale:** "Market research shows we need this capacity for enterprise customers. The architecture investment is justified."
**Implementation Notes:**
- Add auto-scaling components to architecture
- Implement caching layer
- Update performance testing requirements

## Impact Summary
**Total Conflicts Resolved:** 2
**Critical Decisions:** 1
**Architecture Changes Required:** Yes
**Estimated Additional Effort:** 3 weeks
**Quality Score Impact:** Minimal (expected 91/100)
**Next Steps:** Proceed with specification updates based on resolutions
```

**Step 4.4: Apply Conflict Resolutions**
Update requirements and specifications based on user decisions before proceeding.

## Step 5: Change Impact Analysis

**Step 5.1: Analyze Requirements Impact**
Identify affected requirements:
- New requirements to be added
- Modified requirements with changes
- Removed requirements (out of scope)
- Dependent requirements affected by changes

**Step 5.2: Analyze Architecture Impact**
Identify affected architecture components:
- Components requiring redesign
- Components requiring updates
- Components no longer needed
- New components required

**Step 5.3: Analyze Security Impact**
Identify affected security elements:
- Threats requiring updates
- Security controls requiring changes
- New threats introduced
- Mitigations no longer applicable

**Step 5.4: Classify Severity and Estimate Effort**
For each impacted component:
- **Severity**: Critical/Major/Minor/Informational
- **Effort**: Low/Medium/High
- **Risk**: Low/Medium/High

**Step 5.5: Generate Impact Report**
Create `.workflow-state/change-impact-iteration-${ITERATION}.md` with:
- Executive summary of changes
- Detailed impact analysis per component
- Cumulative impact assessment
- Effort estimates and timeline impact
- Risk assessment and mitigation strategies

**Change Impact Report File Format** (`.workflow-state/change-impact-iteration-N.md`):
```markdown
# Change Impact Analysis - Iteration N

## Executive Summary
- **Total Changes:** 5 new requirements, 3 modified, 1 removed
- **Severity Distribution:** 1 Critical, 2 Major, 2 Minor
- **Estimated Effort:** HIGH (3-4 weeks additional work)
- **Architecture Redesign Required:** Yes (authentication component)
- **Quality Score Impact:** Minimal (expected 91/100)
- **Timeline Impact:** 3 weeks delay

## Critical Impacts (Severity: Critical)

### Impact 1: Authentication Architecture Redesign
**Trigger:** Conflict resolution - Switch from OAuth to SAML
**Affected Components:**
- Requirements: FR-001, FR-002, FR-003
- Architecture: Identity Management Component, API Gateway
- ADRs: ADR-003 (superseded), ADR-015 (new)
- Security: TM-001, SC-001

**Changes Required:**
1. Redesign authentication flow for SAML
2. Update API Gateway authorizer configuration
3. Revise security threat model for SAML flows
4. Update integration requirements with IdP

**Effort Estimate:** HIGH (2 weeks)
**Risk Level:** MEDIUM
**Risk Factors:**
- SAML IdP integration complexity
- Authentication flow testing requirements
**Mitigation Strategies:**
- Phased implementation approach
- Comprehensive testing framework
- IdP vendor support engagement

## Major Impacts (Severity: Major)

### Impact 2: Scalability Requirements Update
**Trigger:** New requirement - 10x user capacity increase
**Affected Components:**
- Architecture: Load balancing, database scaling
- Requirements: NFR-002, NFR-003
- Infrastructure: Auto-scaling configuration

**Changes Required:**
1. Add auto-scaling components
2. Update database architecture for horizontal scaling
3. Implement caching layer

**Effort Estimate:** MEDIUM (1 week)
**Risk Level:** LOW

## Cumulative Impact Assessment
- **Requirements Document:** 8 sections affected
- **Architecture Specification:** 3 components redesigned
- **ADRs:** 1 superseded, 2 new
- **Security Threat Model:** 4 threats updated
- **Quality Score:** Re-assessment required

## Timeline and Resource Impact
- **Critical Path:** Authentication redesign (2 weeks)
- **Parallel Work:** Scalability improvements (1 week)
- **Total Additional Effort:** 3 weeks
- **Resource Requirements:** 
  - Senior architect (authentication design)
  - Security specialist (threat model update)
  - DevOps engineer (scaling implementation)

## Risk Assessment
- **Overall Risk Level:** MEDIUM
- **Key Risk Factors:**
  - SAML integration complexity
  - Timeline pressure
  - Resource availability
- **Mitigation Strategies:**
  - Vendor support engagement
  - Phased rollout approach
  - Contingency planning

## Success Criteria
- Authentication redesign completed and tested
- Scalability requirements validated
- Quality score maintained above 90/100
- All conflicts resolved with stakeholder approval
```

## Step 6: Generate Improvement Tasks

**CRITICAL**: All improvement tasks must follow the **copy-then-update pattern** for complete project regeneration.

### **Task Generation Requirements**

1. **First Task: Complete Project Copy**
   - **Task Name**: "Create new complete project iteration folder"
   - **Purpose**: Copy entire existing project to new feedback iteration folder
   - **Process**: 
     - Identify source project: `generated/design/[project-name]/`
     - Copy to new folder: `generated/design/[project-name]-feedback-iteration-N/`
     - **Copy latest specification package only**: Find highest numbered `specification-package-iteration-X/` and copy as `specification-package/`
     - **Copy all other files**: README.md, executive-summary.md, score-sheet-iteration-X.md (latest only), threat-model/, supplement-material/

2. **Latest Specification Package Selection**
   - **Find highest numbered**: `specification-package-iteration-1/`, `specification-package-iteration-2/`, etc.
   - **Copy only the latest**: If iteration-3 exists, copy only that one
   - **Rename to specification-package**: In feedback folder, use simple naming without iteration numbers
   - **Skip older iterations**: Don't copy iteration-1, iteration-2 if iteration-3 exists

3. **Subsequent Tasks: Selective Updates**
   - **Update Pattern**: Only modify files affected by feedback
   - **Naming Convention**: Updated files get "-updated" suffix
   - **Preserve Originals**: Keep original files alongside updated versions
   - **Examples**:
     - `architecture/system-architecture-updated.md`
     - `requirements/functional-requirements-updated.md`

### **Task Breakdown Guidelines**

1. **Improvement Areas**: What aspects of the design need updates?
   - Requirements, Architecture, Security, Documentation, etc.
   - Prioritize by impact and dependencies

2. **Task Organization**: How should improvements be structured?
   - **Task 1**: Always "Create new complete project iteration folder"
   - **Task 2+**: Specific updates with "-updated" file naming
   - Group related changes together
   - Ensure each task has clear scope

3. **Reference Mapping**: Link tasks to feedback sources
   - Trace back to specific feedback documents
   - Reference original specification sections being updated
   - Maintain audit trail

4. **Implementation Notes**: Capture key guidance
   - Rationale for changes
   - Impact on existing specifications
   - Dependencies between tasks
   - File naming conventions ("-updated" suffix)

## Step 7: Populate design-handoff.md

Update `.workflow-state/design-handoff.md` by **adding your generated improvement tasks as subtasks** to the current Feedback Iteration task.

**IMPORTANT**: The first subtask should always be "Create new complete project iteration folder" which will:
1. **Copy from source project**: `generated/design/[project-name]/` 
2. **To new feedback iteration folder**: `generated/design/[project-name]-feedback-iteration-N/`
3. **Copy latest specification package only**: Find highest numbered `specification-package-iteration-X/` and copy as `specification-package/`
4. **Copy all other files**: README.md, executive-summary.md, latest score-sheet-iteration-X.md, threat-model/, supplement-material/
5. **Then subsequent tasks update only changed files** with "-updated" suffix

### IMPORTANT: Add as Subtasks, Not Top-Level Tasks

Find the current "Feedback Iteration N" task in the taskDetails array and **append your generated tasks to its subtasks array**. Do NOT create new top-level tasks.

### Task Structure Example

If the current task is "Task 8: Feedback Iteration 1" with subtasks 8.1-8.4, you should add your generated tasks as 8.5, 8.6, 8.7, etc.:

```json
{
  "taskDetails": [
    {
      "taskNumber": "8",
      "taskName": "Feedback Iteration 1",
      "status": "current",
      "referenceDocuments": ["project-doc/feedback/iteration-1/"],
      "implementationNotes": "Review feedback and generate improvement tasks, then create new complete project iteration folder",
      "subtasks": [
        {
          "taskNumber": "8.1",
          "taskName": "Change detection and conflict analysis",
          "status": "complete"
        },
        {
          "taskNumber": "8.2",
          "taskName": "Conflict resolution and impact analysis",
          "status": "current"
        },
        {
          "taskNumber": "8.3",
          "taskName": "Generate feedback implementation tasks",
          "status": "not_started"
        },
        {
          "taskNumber": "8.4",
          "taskName": "Populate design-handoff.md with generated feedback tasks",
          "status": "not_started"
        },
        {
          "taskNumber": "8.5",
          "taskName": "Create new complete project iteration folder",
          "status": "not_started",
          "referenceDocuments": [
            "generated/design/[project-name]/"
          ],
          "implementationNotes": "Copy from [project-name]/ to [project-name]-feedback-iteration-1/: latest specification-package-iteration-X/ as specification-package/, README.md, executive-summary.md, latest score-sheet, threat-model/, supplement-material/"
        },
        {
          "taskNumber": "8.6",
          "taskName": "Update Requirements Based on Stakeholder Feedback",
          "status": "not_started",
          "referenceDocuments": [
            "project-doc/feedback/iteration-1/stakeholder-review.md",
            "generated/design/[project-name]-feedback-iteration-1/specification-package/requirements/"
          ],
          "implementationNotes": "Update authentication requirements with SAML 2.0, create functional-requirements-updated.md with MFA requirements per stakeholder feedback"
        },
        {
          "taskNumber": "8.7",
          "taskName": "Revise Architecture for Scalability",
          "status": "not_started",
          "referenceDocuments": [
            "project-doc/feedback/iteration-1/technical-review.md",
            "generated/design/[project-name]-feedback-iteration-1/specification-package/architecture/"
          ],
          "implementationNotes": "Create system-architecture-updated.md with auto-scaling and caching layer to handle 10x traffic growth per technical review"
        },
        {
          "taskNumber": "8.8",
          "taskName": "Enhance Security Controls",
          "status": "not_started",
          "referenceDocuments": [
            "project-doc/feedback/iteration-1/security-review.md",
            "generated/design/[project-name]-feedback-iteration-1/threat-model/"
          ],
          "implementationNotes": "Create threat-analysis-updated.md and security-controls-updated.md with encryption at rest per security review"
        }
      ]
    }
  ]
}
```

### Required Fields for Each Generated Subtask

- **taskNumber**: Use format `N.X` where N is the feedback task number and X is sequential (8.5, 8.6, 8.7, etc.)
- **taskName**: Clear, descriptive name indicating what will be updated
- **status**: Always "not_started" initially
- **referenceDocuments**: Array of feedback docs and specification sections being updated
- **implementationNotes**: Brief summary of changes and rationale

### Important: Task Numbering

If the current task is "Task 8: Feedback Iteration 1" with existing subtasks 8.1-8.4:
- **Task 8.1**: Review and analyze feedback (already exists)
- **Task 8.2**: Generate improvement tasks (already exists - this task)
- **Task 8.3**: Populate design-handoff.md (already exists)
- **Task 8.4**: Create new complete project iteration folder (already exists)
- **Task 8.5+**: Your generated improvement subtasks (add these)

### Guidelines for Task Generation

1. **Logical Grouping**: Group related improvements together (e.g., all requirements changes in one subtask)
2. **Clear Scope**: Each subtask should update specific specification sections
3. **Traceability**: Link back to feedback documents and original specs
4. **Completeness**: Ensure all feedback is addressed
5. **Dependencies**: Order subtasks by dependencies (requirements before architecture)
6. **Flat Structure**: Do NOT create nested subtasks - keep all generated tasks at the same level (8.5, 8.6, 8.7, etc.)

## Step 8: Validation & Completion

Before marking Task 8.2 complete:

1. **Verify Coverage**: Does your plan address all feedback?
2. **Check Dependencies**: Are subtasks ordered correctly?
3. **Validate References**: Do all referenced documents exist?
4. **Review Scope**: Is the plan appropriate for the feedback received?
5. **Confirm Structure**: Are all generated tasks added as subtasks (8.5+) to the Feedback Iteration task?

## After Completion

Update `.workflow-state/design-handoff.md`:
- Mark Task 8.2 as "complete"
- Update lastUpdated timestamp
- Add note summarizing your analysis:
  - Number of improvement subtasks generated
  - Key feedback themes identified
  - Specification areas being updated
  - Any concerns or clarifications needed

**Version History File Format** (`.workflow-state/version-history.md`):
```markdown
# Specification Version History

## Iteration 1 - 2025-01-15 14:30:00
**Type:** Initial Generation
**Trigger:** New project specification request
**Input Files:** 12 files processed
**Quality Score:** 92/100
**Status:** Approved by customer
**Deliverables:** `generated/design/project-name/`
**Processing Time:** 120 minutes

## Iteration 2 - 2025-01-20 16:45:00
**Type:** Feedback Integration
**Trigger:** Stakeholder feedback from customer meeting
**Input Files:** 3 new, 2 modified, 1 removed
**Feedback Sources:**
- `project-doc/feedback/iteration-2/stakeholder-review.md`
- `project-doc/feedback/iteration-2/technical-review.md`
**Conflicts:** 1 critical conflict resolved (OAuth → SAML)
**Changes:**
- 5 new requirements added
- 3 requirements modified
- 1 requirement removed
- Authentication architecture redesigned
**Quality Score:** 91/100
**Status:** Pending customer review
**Deliverables:** `generated/design/project-name-feedback-iteration-1/`
**Processing Time:** 45 minutes (62% time savings)
**Efficiency Metrics:**
- Cache hit rate: 75%
- Files reused: 15
- Incremental processing: Successful
```

**Example completion:**
```json
{
  "lastUpdated": "2025-11-14T15:30:00Z",
  "note": "Task 8.2 complete. Generated 3 improvement subtasks (8.5-8.7) based on stakeholder and technical feedback. Main areas: authentication requirements (MFA), scalability architecture (auto-scaling + caching), security enhancements (encryption at rest). Ready to proceed to Task 8.3.",
  "taskDetails": [
    {
      "taskNumber": "8",
      "taskName": "Feedback Iteration 1",
      "status": "current",
      "subtasks": [
        {
          "taskNumber": "8.2",
          "taskName": "Generate feedback implementation tasks",
          "status": "complete"
        },
        {
          "taskNumber": "8.3",
          "taskName": "Populate design-handoff.md with generated feedback tasks",
          "status": "not_started"
        }
      ]
    }
  ]
}
```

## Troubleshooting

**If no feedback documents found:**
- Verify the iteration folder exists
- Check if user cancelled feedback process
- Confirm feedback documents are in correct location

**If feedback is unclear or contradictory:**
- Document ambiguities in implementationNotes
- Create tasks to clarify requirements with stakeholders
- Flag conflicting feedback for resolution

**If feedback requires major redesign:**
- Break down into manageable incremental changes
- Prioritize critical changes first
- Document scope of changes clearly
- Consider creating multiple complete project iteration folders
