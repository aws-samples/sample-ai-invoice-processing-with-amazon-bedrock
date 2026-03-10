---
inclusion: manual
---

# Requirements Generation Methodology

## Overview

This methodology provides a systematic approach for transforming project documents into structured requirements packages that serve as the foundation for architecture design. The methodology focuses on the Engineering Manager (EM) / Requirements Engineer persona and ensures consistent quality, completeness, and traceability across all requirements components.

## Requirements Package Components

A complete requirements package includes:
- **Functional Requirements** with clear acceptance criteria
- **Non-Functional Requirements** with measurable targets
- **Requirements Traceability Matrix** linking to source documents
- **User Stories** with detailed acceptance criteria
- **Requirements organization** for architecture design

---

## Input Document Processing

### Supported Input Types
- **Statement of Work (SOW)** - Project scope, deliverables, timelines
- **Opportunity Quality Review (OQR)** - Business case, technical requirements
- **Business Requirements Documents** - Functional specifications
- **Meeting Notes** - Stakeholder discussions, decisions
- **Technical Assessments** - Current state analysis, constraints

### Document Analysis Framework
When processing input documents, extract and categorize information into:

1. **Business Context**
   - Project objectives and success criteria
   - Stakeholder requirements and constraints
   - Market context and competitive landscape
   - Budget and timeline parameters

2. **Technical Context**
   - Current system architecture and limitations
   - Technology stack preferences and constraints
   - Integration requirements and dependencies
   - Performance and scalability requirements

3. **User Context**
   - Target user segments and personas
   - User workflows and pain points
   - Accessibility and usability requirements
   - User experience expectations

---

## Requirements Documentation Structure

### 1. Functional Requirements (FR)
Structure each functional requirement as:

```markdown
### FR-[ID]: [Requirement Title]
- **Description**: Clear, concise description of what the system must do
- **Business Justification**: Why this requirement is necessary
- **Acceptance Criteria**:
  - Specific, testable conditions that must be met
  - Include happy path and edge case scenarios
  - Define input/output specifications
- **Priority**: High/Medium/Low based on business impact
- **Dependencies**: Other requirements this depends on
- **Assumptions**: Any assumptions made about this requirement
```

### 2. Non-Functional Requirements (NFR)
Structure each non-functional requirement as:

```markdown
### NFR-[ID]: [Requirement Category]
- **Performance Requirements**:
  - Response time targets (e.g., 95% of requests under 200ms)
  - Throughput requirements (e.g., 1000 concurrent users)
  - Resource utilization limits
- **Scalability Requirements**:
  - Expected growth patterns
  - Scaling triggers and mechanisms
  - Capacity planning considerations
- **Security Requirements**:
  - Authentication and authorization mechanisms
  - Data encryption standards (at rest and in transit)
  - Compliance requirements (GDPR, HIPAA, etc.)
- **Availability Requirements**:
  - Uptime SLA targets (e.g., 99.9% availability)
  - Disaster recovery requirements
  - Maintenance window specifications
```

### 3. Requirements Traceability Matrix
The RTM serves as the authoritative record of requirement origins, conflicts, resolutions, and implementation status, ensuring complete visibility into how project background information informs the specification package. Structure the matrix as:

#### Requirement Identification Section
```markdown
| Req ID | Requirement Title | Requirement Type | Priority | Status | Source Document | Source Location |
|--------|------------------|------------------|----------|---------|-----------------|-----------------|
| BR-001 | [Business Requirement Title] | Business | High | Active | SOW v2.1 | Page 12, Section 3.2 |
| FR-001 | [Functional Requirement Title] | Functional | Medium | Active | BRD v1.2 | Page 8, Section 2.1 |
| NFR-001 | [Non-Functional Requirement Title] | Non-Functional | High | Active | Technical Assessment | Page 15, Performance Section |
```

#### Source Traceability Section
```markdown
| Req ID | Primary Source | Secondary Sources | Page/Section | Stakeholder | Date |
|--------|---------------|-------------------|--------------|-------------|------|
| BR-001 | SOW v2.1 | Meeting Notes 03/15, OQR | Page 12, Section 3.2 | John Smith (PM) | 2024-03-15 |
```

#### Conflict Documentation Section
```markdown
| Req ID | Conflict Description | Conflicting Sources | Conflict Location | Impact Level | Resolution Status | Resolution Details |
|--------|---------------------|-------------------|------------------|--------------|------------------|-------------------|
| FR-001 | Timeline discrepancy: SOW says 6 months, OQR says 4 months | SOW v2.1 vs OQR v1.3 | SOW Page 5, Section 1.3 vs OQR Page 3, Timeline Section | High | Resolved | Stakeholder meeting 03/20: Agreed on 5-month timeline |
```

#### Implementation Mapping Section
```markdown
| Req ID | User Story ID | Epic | Sprint | Implementation Status | Test Case ID | Acceptance Status |
|--------|---------------|------|--------|----------------------|--------------|------------------|
| FR-001 | US-001, US-002 | Epic-1 | Sprint 3 | In Progress | TC-001, TC-002 | Pending |
```

---

## User Stories with Acceptance Criteria

### Standardized User Story Structure

User stories must follow this standardized format to ensure consistency, completeness, and traceability across all projects:

#### Epic Organization
Structure user stories within epics that represent major functional areas:

```markdown
## Epic Overview

### Epic [N]: [Epic Name]
[Brief description of the epic's purpose and business value]

### Epic [N+1]: [Next Epic Name]
[Brief description of the next epic's purpose and business value]

---

## Epic [N]: [Epic Name]

### US-[ID]: [User Story Title]
**As a** [specific user type/persona]
**I want** [specific functionality/capability]
**So that** [clear business/user value]

#### Acceptance Criteria:
- **Given** [initial context/state]
  **When** [action taken]
  **Then** [expected outcome]
- **Given** [edge case context]
  **When** [edge case action]
  **Then** [expected edge case handling]
- **Given** [additional scenario]
  **When** [additional action]
  **Then** [additional expected outcome]

#### Definition of Done:
- [ ] [Specific deliverable 1]
- [ ] [Specific deliverable 2]
- [ ] [Specific deliverable 3]
- [ ] [Quality gate requirement]
- [ ] [Compliance requirement if applicable]

#### Story Points: [Estimation]
#### Dependencies: [Related story IDs or external dependencies]
```

### Required User Story Components

Each user story MUST include all of the following components:

1. **Unique Identifier**: US-[3-digit number] (e.g., US-001, US-002)
2. **Descriptive Title**: Clear, action-oriented title
3. **Standard Format**: As a/I want/So that structure
4. **Comprehensive Acceptance Criteria**: Multiple Given/When/Then scenarios covering:
   - Happy path scenarios
   - Edge cases and error conditions
   - Performance requirements where applicable
   - Security requirements where applicable
5. **Detailed Definition of Done**: Specific, measurable completion criteria
6. **Story Point Estimation**: Relative sizing using Fibonacci sequence
7. **Dependencies**: Clear identification of prerequisite stories or external dependencies

### Epic Structure Requirements

Organize user stories into logical epics with:

1. **Epic Overview Section**: High-level summary of all epics
2. **Individual Epic Sections**: Detailed breakdown of stories within each epic
3. **Story Prioritization**: Clear priority levels within and across epics
4. **Sprint Planning Section**: Recommended grouping for iterative development

### Story Prioritization Framework

Include a prioritization section with:

```markdown
## Story Prioritization and Sprint Planning

### Sprint [N] ([Sprint Theme] - [Timeframe])
**Priority [Level] - [Priority Description]**
- US-[ID]: [Story Title] ([Points] points)
- US-[ID]: [Story Title] ([Points] points)
- **Total: [X] points**

### Sprint [N+1] ([Sprint Theme] - [Timeframe])
**Priority [Level] - [Priority Description]**
- US-[ID]: [Story Title] ([Points] points)
- US-[ID]: [Story Title] ([Points] points)
- **Total: [X] points**

### Future Backlog ([Priority Description])
**Priority [Level] - [Priority Description]**
- US-[ID]: [Story Title] ([Points] points)
```

### Quality Assurance Framework

Include standardized quality sections:

```markdown
## Acceptance Criteria Summary

### Definition of Ready Checklist
- [ ] User story follows INVEST criteria
- [ ] Acceptance criteria are specific and testable
- [ ] Dependencies are identified and resolved
- [ ] Story points estimated by team
- [ ] Business value clearly articulated

### Definition of Done Checklist
- [ ] All acceptance criteria met
- [ ] Code review completed
- [ ] Unit tests written and passing
- [ ] Integration testing completed
- [ ] Documentation updated
- [ ] Accessibility requirements verified
- [ ] Security review completed (where applicable)
- [ ] Performance requirements met
- [ ] Stakeholder acceptance obtained

## Traceability to Requirements

### Functional Requirements Coverage
- FR-[ID] → US-[ID], US-[ID]
- FR-[ID] → US-[ID]

### Non-Functional Requirements Coverage
- NFR-[ID] → US-[ID], US-[ID]
- NFR-[ID] → All stories ([description])

## Success Metrics

### User Experience Metrics
- [Metric name] > [Target value]
- [Metric name] < [Target value]

### Technical Performance Metrics
- [Metric name] < [Target value]
- [Metric name] > [Target value]

### Business Success Metrics
- [Metric name] < [Target value]
- [Metric name] > [Target value]
```

### User Story Quality Standards

Ensure each user story meets these quality criteria:

- **INVEST Compliance**: Independent, Negotiable, Valuable, Estimable, Small, Testable
- **Clear Personas**: Specific user types, not generic "user"
- **Measurable Outcomes**: Quantifiable acceptance criteria where possible
- **Business Value**: Clear connection to business objectives
- **Technical Feasibility**: Realistic scope for development team
- **Testable Criteria**: Acceptance criteria that can be automated or manually verified

## Requirements Package Structure

Structure the requirements package as:

```
requirements/
├── functional-requirements.md
├── non-functional-requirements.md
└── requirements-traceability-matrix.md 
user-stories/
└── user-stories.md
```

### User Stories Document Template

The user-stories.md file must follow this standardized structure:

```markdown
# User Stories

## Epic Overview
### Epic 1: [Epic Name]
[Epic description and business value]

### Epic 2: [Epic Name]
[Epic description and business value]

---

## Epic 1: [Epic Name]

### US-001: [Story Title]
**As a** [persona]
**I want** [functionality]
**So that** [business value]

#### Acceptance Criteria:
- **Given** [context] **When** [action] **Then** [outcome]
- **Given** [context] **When** [action] **Then** [outcome]

#### Definition of Done:
- [ ] [Specific deliverable]
- [ ] [Quality requirement]
- [ ] [Compliance requirement]

#### Story Points: [Number]
#### Dependencies: [Story IDs or external dependencies]

---

## Story Prioritization and Sprint Planning
[Organized by sprints with point totals]

## Acceptance Criteria Summary
[Definition of Ready and Done checklists]

## Traceability to Requirements
[Mapping to functional and non-functional requirements]

## Success Metrics
[Measurable success criteria organized by category]
```

## Content Quality Standards

- **Clarity**: Use clear, unambiguous language that technical and non-technical stakeholders can understand
- **Completeness**: Ensure all aspects of the project requirements are covered without gaps
- **Consistency**: Maintain consistent terminology, formatting, and structure throughout
- **Traceability**: Ensure requirements can be traced from business objectives through to user stories
- **Testability**: Provide specific, testable acceptance criteria for all requirements

## Requirements Organization for Architecture Design

### Grouping Requirements by Domain
Organize requirements to facilitate architecture design:

1. **User Interface Requirements**
   - User experience and interaction requirements
   - Accessibility and usability requirements
   - Interface integration requirements

2. **Business Logic Requirements**
   - Core business process requirements
   - Business rule and validation requirements
   - Workflow and process requirements

3. **Data Requirements**
   - Data model and structure requirements
   - Data processing and transformation requirements
   - Data integration and migration requirements

4. **Integration Requirements**
   - External system integration requirements
   - API and service interface requirements
   - Third-party service requirements

5. **Infrastructure Requirements**
   - Performance and scalability requirements
   - Security and compliance requirements
   - Operational and maintenance requirements

### Requirements Dependencies
Document requirement dependencies to inform architecture design:

```markdown
## Requirement Dependencies

### Critical Path Dependencies
- FR-001 (User Authentication) → FR-005 (User Profile Management)
- FR-002 (Data Import) → FR-008 (Data Processing)
- NFR-001 (Performance) → NFR-003 (Scalability)

### Integration Dependencies
- FR-010 (External API Integration) requires NFR-005 (Security Standards)
- FR-015 (Reporting) depends on FR-003 (Data Storage)

### Constraint Dependencies
- All security requirements must align with NFR-006 (Compliance Standards)
- Performance requirements must consider NFR-004 (Infrastructure Constraints)
```

## Stakeholder-Specific Views

Generate tailored views for different stakeholders:

- **Business Stakeholder Summary**: High-level requirements overview focusing on business value and outcomes
- **Technical Team Requirements**: Detailed functional and non-functional requirements for architecture design
- **QA Testing Requirements**: Acceptance criteria and test scenarios for quality assurance
- **Project Manager Requirements**: Priority, dependencies, and scope information for project planning

## Continuous Improvement Framework

### Feedback Integration Process
- Establish regular review cycles with stakeholders
- Create feedback collection mechanisms for each requirements document through structured `project-doc/feedback/iteration-N/` folders
- Implement systematic feedback analysis and dynamic improvement task generation
- Implement version control for requirements updates with complete project folder iterations
- Maintain change logs for all requirements modifications with complete traceability to feedback sources

### Requirements Metrics
Track requirements effectiveness through:
- **Requirements Clarity**: Number of clarification requests during architecture design
- **Requirements Stability**: Frequency and impact of requirements changes across feedback iterations
- **Traceability Coverage**: Percentage of requirements traced to source documents and feedback inputs
- **Stakeholder Satisfaction**: Feedback scores from architecture team and business stakeholders
- **Feedback Integration Effectiveness**: Quality score improvements across complete project folder iterations
- **Iteration Cycle Time**: Time from feedback collection to updated complete project folder delivery