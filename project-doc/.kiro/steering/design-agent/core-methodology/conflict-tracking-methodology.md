---
inclusion: manual
---

# Conflict Tracking and Resolution Methodology

## Overview

This methodology provides systematic approaches for detecting, analyzing, and resolving conflicts between new stakeholder feedback and existing specification decisions. It ensures specification consistency while enabling iterative refinement through intelligent change management.

## Core Principles

### Automated Conflict Detection
**Principle**: Use semantic analysis and content fingerprinting to automatically identify contradictions between new feedback and existing decisions.

**Application Guidelines**:
- **Content Fingerprinting**: SHA-256 hashing for precise change detection
- **Semantic Analysis**: Pattern matching and constraint analysis for conflict identification
- **Categorization**: Systematic classification of conflict types and severity levels
- **Early Detection**: Identify conflicts before specification updates to prevent inconsistencies

### User-Guided Resolution
**Principle**: Present conflicts to users with clear options and impact analysis for informed decision-making.

**Resolution Standards**:
- **Clear Presentation**: Conflicts presented with original vs new requirements side-by-side
- **Resolution Options**: Multiple resolution paths with pros/cons analysis
- **Impact Assessment**: Detailed analysis of consequences for each resolution option
- **Rationale Documentation**: Complete record of resolution decisions and reasoning

### Incremental Processing Efficiency
**Principle**: Process only changed inputs to minimize execution time while maintaining quality standards.

**Efficiency Standards**:
- **Target Performance**: <50% of full regeneration time for feedback iterations
- **Change Detection**: Accurate identification of NEW, MODIFIED, REMOVED, UNCHANGED files
- **Cache Utilization**: Reuse previous analysis results for unchanged inputs
- **Selective Processing**: Analyze only files that have changed since last iteration

## Conflict Detection Framework

### Change Detection Engine

**Content Fingerprinting System**:
```markdown
# Processing History Format

## Iteration N - YYYY-MM-DD HH:MM:SS

### project-doc/project-context/
- `requirements.md`: sha256:abc123... (processed)
- `meeting-notes.md`: sha256:def456... (processed)

### project-doc/technical-knowledge/
- `api-documentation.md`: sha256:ghi789... (processed)

### project-doc/organization-context/
- `security-policy.md`: sha256:jkl012... (processed)

### project-doc/feedback/
- `iteration-N/customer-feedback.md`: sha256:mno345... (processed)
```

**Change Categorization Logic**:
- **NEW**: Files present in current execution but not in processing history
- **MODIFIED**: Files with different fingerprints than processing history
- **REMOVED**: Files in processing history but not present in current execution
- **UNCHANGED**: Files with matching fingerprints (reuse cached analysis)

### Semantic Conflict Detection

**Conflict Types**:

#### Direct Contradiction
- **Definition**: New feedback explicitly contradicts previous requirement
- **Example**: Original: "Users SHALL authenticate using OAuth 2.0" vs New: "Users SHALL authenticate using SAML 2.0"
- **Detection Pattern**: Opposite requirements (SHALL vs SHALL NOT), mutually exclusive technology choices

#### Implicit Conflict
- **Definition**: New feedback implies different approach than existing architecture
- **Example**: Original: "System designed for 100 concurrent users" vs New: "System must handle enterprise-scale load"
- **Detection Pattern**: Incompatible assumptions, conflicting design implications

#### Scope Conflict
- **Definition**: New feedback changes project boundaries or objectives
- **Example**: Original: "Web application only" vs New: "Must include mobile app"
- **Detection Pattern**: Boundary changes, new platform requirements, scope expansion/reduction

#### Technical Conflict
- **Definition**: New feedback requires incompatible technology choices
- **Example**: Original: "Use PostgreSQL database" vs New: "Must use NoSQL for scalability"
- **Detection Pattern**: Incompatible technology stacks, conflicting technical constraints

### Conflict Analysis Process

**Step 1: Extract Requirements from Feedback**
```markdown
# Feedback Analysis - customer-meeting-2025-01-20.md

## Extracted Requirements
- REQ-NEW-001: Users shall authenticate using SAML 2.0 for enterprise SSO
- REQ-NEW-002: System shall support 10,000 concurrent users
- REQ-NEW-003: Payment processing shall use Stripe API v2

## Extracted Constraints
- CONSTRAINT-001: Must comply with SOC 2 Type II
- CONSTRAINT-002: Maximum response time 100ms
```

**Step 2: Compare Against Existing Specifications**
```markdown
# Conflict Detection Results

## Potential Conflicts Identified (3)

### Conflict 1: Authentication Method [CRITICAL]
- **Original**: FR-001 - OAuth 2.0 authentication
- **New**: REQ-NEW-001 - SAML 2.0 authentication
- **Type**: Direct Contradiction
- **Severity**: CRITICAL (affects core architecture)

### Conflict 2: Scalability Requirements [MAJOR]
- **Original**: NFR-002 - 1,000 concurrent users
- **New**: REQ-NEW-002 - 10,000 concurrent users
- **Type**: Implicit Conflict (architecture implications)
- **Severity**: MAJOR (requires architecture scaling)
```

## Conflict Resolution Framework

### Resolution Options Framework

**Standard Resolution Options**:

#### Option 1: Accept New Requirement
- **Description**: Replace original requirement with new requirement
- **When to Use**: New requirement is more accurate or reflects updated business needs
- **Pros**: Aligns with current stakeholder needs
- **Cons**: May require significant rework
- **Impact Assessment**: Full impact analysis of changes required

#### Option 2: Keep Original Requirement
- **Description**: Preserve original requirement, document new feedback as considered but not adopted
- **When to Use**: Original requirement is still valid and new feedback is not critical
- **Pros**: No rework required, maintains current design
- **Cons**: May not meet evolving stakeholder needs
- **Impact Assessment**: Minimal impact, document rationale

#### Option 3: Merge Both Requirements
- **Description**: Find a solution that satisfies both original and new requirements
- **When to Use**: Both requirements have merit and can be technically integrated
- **Pros**: Maximum stakeholder satisfaction
- **Cons**: Increased complexity and implementation effort
- **Impact Assessment**: Complexity analysis required

#### Option 4: Custom Resolution
- **Description**: User-defined resolution approach
- **When to Use**: Standard options don't adequately address the conflict
- **Process**: User provides specific resolution approach
- **Documentation**: Detailed rationale and implementation approach required

### Conflict Report Generation

**Report Format**:
```markdown
# Conflicts Report - Iteration X

## Executive Summary
- Total Conflicts: X
- Critical: X, Major: X, Minor: X
- Estimated Resolution Time: X hours
- Architecture Impact: [Yes/No]

## Conflict Details

### Conflict 1: [Title] [SEVERITY]

#### Original Decision (Iteration Y)
**Requirement:** [Original requirement text]
**Source:** [Source document and location]
**Rationale:** [Why original decision was made]
**Stakeholder:** [Who requested/approved original]

#### New Feedback (Iteration X)
**Requirement:** [New requirement text]
**Source:** [Feedback document and location]
**Rationale:** [Why new requirement is needed]
**Stakeholder:** [Who provided new feedback]

#### Conflict Analysis
- **Type:** [Direct Contradiction/Implicit Conflict/Scope Conflict/Technical Conflict]
- **Severity:** [CRITICAL/MAJOR/MINOR]
- **Root Cause:** [Why conflict exists]
- **Affected Components:**
  - Requirements: [List affected requirements]
  - Architecture: [List affected components]
  - ADRs: [List affected decisions]
  - Security: [List affected security elements]

#### Resolution Options

##### Option 1: Accept New ([Technology/Approach])
**Description:** [What this resolution entails]
**Pros:**
- [Benefit 1]
- [Benefit 2]
**Cons:**
- [Drawback 1]
- [Drawback 2]
**Effort:** [LOW/MEDIUM/HIGH]
**Risk:** [LOW/MEDIUM/HIGH]
**Timeline Impact:** [X days/weeks]

##### Option 2: Keep Original ([Technology/Approach])
**Description:** [What this resolution entails]
**Pros:**
- [Benefit 1]
- [Benefit 2]
**Cons:**
- [Drawback 1]
- [Drawback 2]
**Effort:** [LOW/MEDIUM/HIGH]
**Risk:** [LOW/MEDIUM/HIGH]
**Timeline Impact:** [X days/weeks]

##### Option 3: Merge Both ([Hybrid Approach])
**Description:** [What this resolution entails]
**Pros:**
- [Benefit 1]
- [Benefit 2]
**Cons:**
- [Drawback 1]
- [Drawback 2]
**Effort:** [LOW/MEDIUM/HIGH]
**Risk:** [LOW/MEDIUM/HIGH]
**Timeline Impact:** [X days/weeks]

#### Recommended Resolution
**Option X: [Selected Option]**
**Rationale:** [Why this option is recommended]
**Critical Success Factors:** [What must go right]
**Risk Mitigation:** [How to address risks]

#### User Decision Required
Please select resolution option: [1/2/3/Custom]
Custom resolution (if selected): [User input field]
```

### Resolution Workflow Process

**Step 1: Conflict Presentation**
- Display conflicts in order of severity (Critical → Major → Minor)
- Present one conflict at a time for focused decision-making
- Provide complete context and impact analysis
- Highlight recommended resolution with clear rationale

**Step 2: User Decision Collection**
- Prompt for resolution option selection
- Collect rationale for decision (especially for non-recommended options)
- Validate decision completeness before proceeding
- Document timestamp and decision maker

**Step 3: Resolution Application**
- Apply selected resolution to specifications
- Update affected requirements, architecture, ADRs, security elements
- Create new ADRs for significant architectural changes
- Mark superseded decisions with clear references

**Step 4: Resolution Documentation**
```markdown
# Conflict Resolution Log - Iteration X

## Conflict 1: Authentication Method
**Decision:** Option 1 - Accept New (SAML 2.0)
**Decision Maker:** [Name/Role]
**Timestamp:** 2025-01-20 16:45:00
**Rationale:** Compliance requirements are non-negotiable for enterprise deployment
**Implementation Notes:** 
- Redesign authentication component
- Update API Gateway authorizer
- Revise security threat model
- Plan SAML IdP integration

## Impact Summary
**Total Conflicts Resolved:** 3
**Critical Decisions:** 1
**Architecture Changes Required:** Yes
**Estimated Additional Effort:** 3-4 weeks
**Quality Score Impact:** Minimal (expected 91/100)
```

## Change Impact Analysis Framework

### Impact Dimensions

**Requirements Impact Analysis**:
- **New Requirements**: Count and categorization of additions
- **Modified Requirements**: Changes to existing requirements with rationale
- **Removed Requirements**: Requirements no longer applicable with justification
- **Dependent Requirements**: Requirements affected by changes to others

**Architecture Impact Analysis**:
- **Component Redesign**: Components requiring fundamental changes
- **Component Updates**: Components requiring minor modifications
- **New Components**: Components to be added
- **Deprecated Components**: Components no longer needed

**Security Impact Analysis**:
- **Threat Model Updates**: New threats or modified threat scenarios
- **Security Control Changes**: Updates to security implementations
- **Compliance Impact**: Changes affecting regulatory compliance
- **Risk Assessment**: New risks introduced or mitigated

**Implementation Impact Analysis**:
- **Development Effort**: Estimated additional work required
- **Timeline Impact**: Effect on project schedule
- **Resource Requirements**: Additional skills or resources needed
- **Testing Impact**: Additional testing required

### Severity Classification

**Critical Impact**:
- **Definition**: Fundamental architecture changes required
- **Examples**: Core technology stack changes, major component redesign
- **Effort**: HIGH (>2 weeks)
- **Risk**: MEDIUM-HIGH
- **Approval**: Requires stakeholder approval

**Major Impact**:
- **Definition**: Significant component redesign needed
- **Examples**: New integration requirements, substantial feature additions
- **Effort**: MEDIUM (1-2 weeks)
- **Risk**: MEDIUM
- **Approval**: Technical lead approval recommended

**Minor Impact**:
- **Definition**: Localized updates required
- **Examples**: Configuration changes, minor feature modifications
- **Effort**: LOW (<1 week)
- **Risk**: LOW
- **Approval**: Standard development process

**Informational Impact**:
- **Definition**: Documentation updates only
- **Examples**: Clarifications, additional context
- **Effort**: MINIMAL (<1 day)
- **Risk**: NONE
- **Approval**: Not required

### Impact Report Generation

**Report Structure**:
```markdown
# Change Impact Analysis - Iteration X

## Executive Summary
- **Total Changes:** X new requirements, Y modified, Z removed
- **Severity Distribution:** X Critical, Y Major, Z Minor, W Informational
- **Estimated Effort:** [LOW/MEDIUM/HIGH] (X weeks additional work)
- **Architecture Redesign Required:** [Yes/No]
- **Quality Score Impact:** [Expected change]
- **Timeline Impact:** [X weeks delay/no impact]

## Critical Impacts (Severity: Critical)

### Impact 1: [Component/Area] Redesign
**Trigger:** [Conflict resolution or new requirement]
**Affected Components:**
- Requirements: [List with IDs]
- Architecture: [List components]
- ADRs: [List affected decisions]
- Security: [List affected elements]

**Changes Required:**
1. [Specific change 1]
2. [Specific change 2]
3. [Specific change 3]

**Effort Estimate:** [X weeks]
**Risk Level:** [LOW/MEDIUM/HIGH]
**Risk Factors:**
- [Risk factor 1]
- [Risk factor 2]

**Mitigation Strategies:**
- [Mitigation 1]
- [Mitigation 2]

## Cumulative Impact Assessment
- **Requirements Document:** X sections affected
- **Architecture Specification:** Y components redesigned
- **ADRs:** Z superseded, W new
- **Security Threat Model:** X threats updated
- **Quality Score:** Re-assessment required

## Recommendations
1. [Priority recommendation 1]
2. [Priority recommendation 2]
3. [Priority recommendation 3]

## Success Criteria
- [Measurable success criterion 1]
- [Measurable success criterion 2]
- [Measurable success criterion 3]
```

## Version Management and Audit Trail

### Processing History Management

**History File Structure** (`.workflow-state/processing-history.md`):
```markdown
# Processing History

## Iteration 1 - 2025-01-15 14:30:00
**Type:** Initial Generation
**Files Processed:** 12
**Total Fingerprints:** 12

### File Fingerprints
- `project-doc/project-context/requirements.md`: sha256:abc123...
- `project-doc/technical-knowledge/api-docs.md`: sha256:def456...
[... all files with fingerprints ...]

## Iteration 2 - 2025-01-20 16:45:00
**Type:** Feedback Integration
**Files Processed:** 5 (3 new, 2 modified)
**Files Reused:** 10 (unchanged)
**Conflicts Resolved:** 1 critical
**Processing Time:** 45 minutes (vs 120 minutes full regeneration)

### Change Summary
**New Files:**
- `project-doc/feedback/iteration-2/customer-meeting.md`: sha256:ghi789...
- `project-doc/project-context/updated-requirements.md`: sha256:jkl012...

**Modified Files:**
- `project-doc/project-context/requirements.md`: sha256:mno345... (was abc123...)
- `project-doc/organization-context/security-policy.md`: sha256:pqr678... (was def456...)

**Removed Files:**
- `project-doc/project-code/legacy-system/`: (directory removed)

### File Fingerprints (Current)
[... updated fingerprint list ...]
```

### Version History Tracking

**Version History Format** (`.workflow-state/version-history.md`):
```markdown
# Specification Version History

## Iteration 1 - 2025-01-15 14:30:00
**Type:** Initial Generation
**Trigger:** New project specification request
**Input Files:** 12 files processed
**Quality Score:** 92/100
**Status:** Approved by customer
**Deliverables:** `project-name-iteration-1/`

## Iteration 2 - 2025-01-20 16:45:00
**Type:** Feedback Integration
**Trigger:** Customer meeting feedback
**Input Files:** 3 new, 2 modified, 1 removed
**Feedback Sources:**
- `project-doc/feedback/iteration-2/customer-meeting.md`
**Conflicts:** 1 critical conflict resolved (OAuth → SAML)
**Changes:**
- 5 new requirements added
- 3 requirements modified
- 1 requirement removed
- Authentication architecture redesigned
**Quality Score:** 91/100
**Status:** Pending customer review
**Deliverables:** `project-name-iteration-2/`
**Processing Time:** 45 minutes (62% time savings)
```

### Changelog Generation

**Changelog Format** (`changelog-iteration-X-to-Y.md`):
```markdown
# Changelog: Iteration X → Iteration Y

## Conflicts Resolved (1)

### Authentication Method Conflict
**Original:** OAuth 2.0 authentication (FR-001)
**New:** SAML 2.0 authentication for enterprise SSO
**Resolution:** Accept New (Option 1)
**Rationale:** Compliance requirements non-negotiable
**Impact:** Authentication architecture redesign required

## Requirements Changes

### Added Requirements (5)
- **FR-015:** Payment Processing with Stripe API v2
  - **Source:** project-doc/feedback/iteration-2/customer-meeting.md
  - **Rationale:** Customer requested payment integration
- **FR-016:** Multi-factor Authentication
  - **Source:** project-doc/feedback/iteration-2/customer-meeting.md
  - **Rationale:** Enhanced security requirement

### Modified Requirements (3)
- **FR-001:** User Authentication
  - **Before:** OAuth 2.0 authentication
  - **After:** SAML 2.0 authentication with enterprise SSO
  - **Rationale:** Customer compliance requirements
  - **Impact:** Authentication component redesign

### Removed Requirements (1)
- **FR-008:** Legacy System A Integration
  - **Rationale:** System being decommissioned
  - **Impact:** Remove integration component

## Architecture Changes

### Components Redesigned (3)
- **Identity Management Component:** OAuth → SAML
- **API Gateway Authorizer:** JWT validation → SAML assertion validation
- **Session Store:** Token storage → Assertion cache

### New Components (2)
- **Payment Gateway Integration:** Stripe API v2 connector
- **Audit Logger:** Centralized audit trail system

### Deprecated Components (1)
- **Legacy System A Adapter:** No longer needed

## Quality Score Impact
- **Previous:** 92/100
- **Current:** 91/100
- **Change:** -1 point (minor decrease due to increased complexity)
- **Assessment:** Quality maintained within acceptable range

## Effort Impact
- **Estimated Additional Work:** 3-4 weeks
- **Critical Path Impact:** Authentication redesign
- **Risk Level:** MEDIUM
- **Mitigation:** Phased implementation approach
```

## Performance Optimization

### Incremental Processing Optimization

**Caching Strategy**:
- **Analysis Cache**: Store previous input assessment results
- **Component Cache**: Cache unchanged specification components
- **Fingerprint Cache**: Maintain file fingerprint database
- **Resolution Cache**: Store conflict resolution patterns

**Processing Efficiency Targets**:
- **Change Detection**: <30 seconds for typical project
- **Conflict Analysis**: <5 minutes for typical feedback iteration
- **Overall Processing**: <50% of full regeneration time
- **Cache Hit Rate**: >80% for unchanged files

**Memory Management**:
- **Lazy Loading**: Load only necessary previous iteration data
- **Streaming**: Process large files without full memory load
- **Garbage Collection**: Release cached data after use
- **Compression**: Compress stored fingerprints and cache data

### Error Handling and Recovery

**Error Scenarios and Responses**:

#### Corrupted Processing History
- **Detection**: Invalid fingerprints or missing metadata
- **Response**: Fallback to full regeneration mode
- **Recovery**: Regenerate processing history from scratch
- **User Communication**: Notify of fallback mode activation

#### Unresolvable Conflicts
- **Detection**: No viable resolution options
- **Response**: Pause workflow and escalate to user
- **Recovery**: Request explicit user guidance
- **Documentation**: Record escalation and resolution path

#### Quality Degradation
- **Detection**: Quality score drops below threshold
- **Response**: Identify root cause and present options
- **Recovery**: Accept, improve, or revert based on user decision
- **Documentation**: Record quality trade-offs and rationale

#### Missing Dependencies
- **Detection**: Referenced files or components not found
- **Response**: Identify missing dependencies and impact
- **Recovery**: Request user guidance on handling missing items
- **Documentation**: Record dependency resolution approach

## Success Metrics

### Process Efficiency Metrics
- **Processing Time Reduction**: Target <50% of full regeneration
- **Change Detection Accuracy**: 100% accuracy (no false negatives)
- **Conflict Detection Rate**: >95% of actual conflicts identified
- **User Resolution Time**: <30 minutes average per conflict

### Quality Maintenance Metrics
- **Quality Score Stability**: Maintain 90/100+ across iterations
- **Traceability Completeness**: 100% of changes linked to sources
- **Documentation Completeness**: All conflicts and resolutions documented
- **Audit Trail Integrity**: Complete version history maintained

### User Experience Metrics
- **Conflict Presentation Clarity**: User feedback on conflict reports
- **Resolution Option Completeness**: All viable options presented
- **Decision Confidence**: User confidence in resolution decisions
- **Process Transparency**: Clear understanding of changes and impacts

