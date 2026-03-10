---
inclusion: manual
---

# Input Assessment Analysis Methodology

## Overview

This methodology provides a focused approach for conducting input assessment analysis as the foundation for specification package generation. The assessment ensures understanding of key project context, identifies critical information gaps, and establishes generation readiness.

## Purpose and Objectives

### Primary Purpose
Conduct focused analysis of available project documents to establish a foundation for specification package generation, ensuring critical information is captured and key stakeholder requirements are understood.

### Key Objectives
- **Document Summary**: Summarize key project documents and their relevance
- **Context Extraction**: Extract essential business, technical, and user context
- **Critical Gap Identification**: Identify missing information that could block generation
- **Key Stakeholder Mapping**: Document primary stakeholders and their core requirements
- **Generation Readiness**: Assess readiness to proceed with specification package generation

## Input Assessment Framework

### 1. Document Inventory and Cataloging

#### Document Classification
Systematically catalog all project documents by type and relevance:

**Primary Documents** (Direct project scope and requirements):
- Statement of Work (SOW)
- Opportunity Quality Review (OQR) 
- Business Requirements Documents (BRD)
- Technical Requirements Documents (TRD)
- Project proposals and contracts

**Secondary Documents** (Supporting context and background):
- Meeting notes and email threads
- Stakeholder briefing documents
- Presentation materials
- Technical assessments
- Market analysis and competitive intelligence

**Reference Documents** (Standards and guidelines):
- Compliance requirements
- Security standards
- Technical architecture guidelines
- Organizational policies and procedures

#### Document Analysis Template
For each document, capture:

```markdown
### Document: [Document Name]
- **Type**: [Primary/Secondary/Reference]
- **Pages/Size**: [Document length]
- **Date**: [Creation/modification date]
- **Author/Source**: [Document creator or source]
- **Relevance**: [High/Medium/Low relevance to project]
- **Key Content**: [Summary of key information]
- **Critical Information**: [Essential details for specification generation]
- **Gaps Identified**: [Missing information noted]
```

### 2. Business Context Analysis

#### Organizational Overview
- **Customer**: [Organization name and industry]
- **Project Scope**: [High-level project description]
- **Key Stakeholders**: [Primary decision makers and users]
- **Business Objectives**: [Top 3-5 business goals]
- **Success Criteria**: [How success will be measured]
- **Timeline & Budget**: [Key constraints and milestones]

### 3. Technical Context Analysis

#### Current State Assessment
Document existing technical environment and constraints:

**System Architecture**:
- Current technology stack and platforms
- Existing system integrations and dependencies
- Data architecture and information flows
- Security controls and compliance frameworks
- Performance characteristics and limitations

**Technical Constraints**:
- Legacy system dependencies and limitations
- Integration requirements and compatibility issues
- Performance and scalability requirements
- Security and compliance mandates
- Technology preferences and standards

#### Proposed Solution Context
Extract technical solution details from project documents:

**Solution Architecture**:
- Proposed system design and components
- Technology stack selections and rationale
- Integration patterns and data flows
- Security architecture and controls
- Deployment and operational considerations

**Implementation Approach**:
- Development methodology and practices
- Testing strategy and quality assurance
- Deployment pipeline and release management
- Monitoring and operational support
- Knowledge transfer and training requirements

### 4. Information Gap Analysis

#### Gap Identification Framework
Identify missing information across all categories:

**Critical Gaps** (Must be resolved before generation):
- Essential functional requirements missing
- Key stakeholder requirements unclear
- Technical constraints not documented
- Security and compliance requirements undefined
- Success criteria and acceptance criteria missing

**Important Gaps** (Should be clarified during generation):
- Detailed workflow specifications needed
- Performance and scalability targets unclear
- Integration specifications incomplete
- User experience requirements undefined
- Testing and validation criteria missing

**Nice-to-Have Gaps** (Can be addressed during implementation):
- Optimization opportunities not documented
- Future enhancement possibilities unclear
- Advanced feature specifications missing
- Detailed operational procedures undefined

#### Gap Impact Assessment
For each identified gap, assess:

```markdown
### Gap: [Gap Description]
- **Category**: [Critical/Important/Nice-to-Have]
- **Impact on Generation**: [High/Medium/Low impact on specification quality]
- **Resolution Approach**: [How to address this gap]
- **Assumptions**: [What assumptions can be made if gap remains]
```

### 5. Generation Readiness Assessment

#### Readiness Criteria Framework
Evaluate readiness across multiple dimensions:

**Information Completeness** (0-100 scale):
- Business context understanding: [Score]/100
- Technical requirements clarity: [Score]/100
- User needs documentation: [Score]/100
- Stakeholder alignment: [Score]/100
- Constraint identification: [Score]/100

**Quality of Available Information** (0-100 scale):
- Document quality and detail: [Score]/100
- Information consistency: [Score]/100
- Stakeholder validation: [Score]/100
- Technical accuracy: [Score]/100
- Traceability to sources: [Score]/100

#### Readiness Decision Matrix
Based on assessment scores, determine generation readiness:

**Ready to Proceed** (Average score ≥ 80):
- Sufficient information available for high-quality specification generation
- Minor gaps can be addressed during generation process
- Stakeholder requirements well understood and documented

**Proceed with Caution** (Average score 60-79):
- Adequate information available but some important gaps exist
- Additional clarification may be needed during generation
- Some assumptions will need to be documented and validated

**Additional Discovery Required** (Average score < 60):
- Significant information gaps that could impact specification quality
- Additional stakeholder engagement and document collection needed
- Generation should be delayed until critical gaps are addressed

## Output Generation Guidelines

### Input Assessment Analysis Document Structure

```markdown
# Task 1.1: Input Assessment Analysis

## Document Inventory
[Complete catalog of all available project documents]

## Business Context Analysis
[Comprehensive organizational and strategic context]

## Technical Context Analysis
[Current state and proposed solution technical details]

## Information Gaps and Constraints
[Identified gaps with impact assessment and resolution approach]

## Generation Readiness Assessment
[Readiness evaluation with scores and recommendations]
```

### Quality Standards for Input Assessment

**Completeness Criteria**:
- All available documents cataloged and analyzed
- Business and tectnical context extracted
- All stakeholders identified with requirements mapped
- Information gaps systematically identified and assessed
- Generation readiness objectively evaluated

**Accuracy Standards**:
- Information extracted accurately from source documents
- Context analysis reflects actual project situation
- Stakeholder requirements correctly interpreted
- Gap analysis identifies real missing information
- Readiness assessment based on objective criteria

**Actionability Requirements**:
- Clear recommendations for proceeding with generation
- Specific guidance on addressing identified gaps
- Actionable next steps for stakeholder engagement
- Concrete assumptions documented for unclear areas
- Risk mitigation strategies for proceeding with gaps

## Integration with Specification Generation

### Handoff to Generation Process
The input assessment analysis provides essential foundation for specification generation:

**Context Foundation**:
- Business context informs requirements prioritization
- Technical context guides architecture decisions
- User context shapes user story development
- Stakeholder mapping ensures comprehensive coverage

**Gap Management**:
- Critical gaps addressed before generation begins
- Important gaps documented as assumptions
- Nice-to-have gaps noted for future consideration
- Risk mitigation strategies implemented

**Quality Assurance**:
- Generation readiness confirmed before proceeding
- Information quality validated and documented
- Stakeholder alignment verified and maintained
- Traceability established from source to specification

### Continuous Validation
Throughout the specification generation process:

**Assumption Validation**:
- Document assumptions made due to information gaps
- Validate assumptions with stakeholders when possible
- Update specifications as new information becomes available
- Maintain traceability from assumptions to requirements

**Gap Resolution**:
- Continue to address information gaps during generation
- Engage stakeholders for clarification as needed
- Document new information and update analysis
- Ensure specification quality is not compromised by gaps

## Success Metrics

### Process Metrics
- **Completeness**: Percentage of available documents analyzed
- **Coverage**: Percentage of stakeholder requirements captured
- **Gap Resolution**: Percentage of critical gaps addressed
- **Readiness Score**: Overall generation readiness assessment

### Quality Metrics
- **Accuracy**: Correctness of context extraction and analysis
- **Consistency**: Alignment between different information sources
- **Traceability**: Clear linkage from source documents to analysis
- **Actionability**: Usefulness of recommendations and next steps

### Outcome Metrics
- **Generation Success**: Quality of resulting specification package
- **Stakeholder Satisfaction**: Stakeholder approval of analysis accuracy
- **Implementation Success**: Effectiveness of specifications for development
- **Risk Mitigation**: Success in identifying and addressing project risks