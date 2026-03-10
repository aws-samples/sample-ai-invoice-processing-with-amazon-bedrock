---
inclusion: manual
---

# OQR 2.0 Self-Inspection Checklist for Implementation Planning

## Overview

This checklist ensures all implementation plans undergo thorough self-inspection before delivery, following the OQR 2.0 methodology. Use this as a quality gate to identify and mitigate risks proactively.

## Pre-Inspection Requirements

### Team Composition (Mandatory)
- [ ] **Minimum 2 Contributors**: Never complete inspection alone
- [ ] **Opportunity Owner**: Primary stakeholder responsible for delivery
- [ ] **Technical Lead**: Subject matter expert with deep technical knowledge
- [ ] **Optional**: Additional team members based on complexity

### Documentation Readiness
- [ ] **SFDC Opportunity**: Complete and up-to-date opportunity record
- [ ] **Customer Proposal**: Detailed proposal with scope and deliverables
- [ ] **Level of Effort (LoE)**: Resource planning and effort estimates
- [ ] **Customer Business Outcomes**: Documented and validated CBOs

## Technical Expertise Assessment

### Customer Environment Understanding
**Confidence Level Scale (1-5):**
- **Level 1**: Minimal/no formal information about customer environment
- **Level 3**: General understanding with some unclear aspects
- **Level 5**: Complete understanding with mutual customer agreement

**Required Actions by Confidence Level:**
- **Level 1-2**: Conduct additional discovery sessions before proceeding
- **Level 3**: Document specific areas requiring clarification
- **Level 4-5**: Proceed with documented assumptions and validations

### Technical Complexity Indicators
- [ ] **Architecture Deliverables**: Code, infrastructure as code, or architecture components
- [ ] **Production Readiness**: Operational readiness reviews planned if moving to production
- [ ] **Principal Engagement**: Review Principal Engagement Guidance for complex opportunities
- [ ] **Partner Supervision**: 8% ProServe technical lead allocation for partner oversight

## Security and Compliance Validation

### Critical Security Checkpoints
- [ ] **Production Access**: Any access to customer production environments identified
- [ ] **Regulated Data**: PII, PHI, CUI, or compliance-regulated information handling
- [ ] **Security Staffing**: Minimum 8% of total effort allocated to security resources
- [ ] **Special Requirements**: Background checks, citizenship, or clearance requirements
- [ ] **Work Location**: Restricted location or specific work site requirements

### AI/ML Specific Requirements
- [ ] **AI/ML Services**: GenAI or AI/ML use cases identified and documented
- [ ] **RAIR Approval**: Responsible AI Reviews completed for AI/ML implementations
- [ ] **Training Data**: Custom-trained models and customer data requirements assessed
- [ ] **EU AI Act Compliance**: Compliance validation for applicable AI implementations

## Project Management Excellence

### Delivery Framework
- [ ] **Sprint 0 PMT**: ProServe Sprint 0 project management package included
- [ ] **Customer Business Outcomes**: CBOs identified, aligned, and documented
- [ ] **Testing Strategy**: UAT, functional, and infrastructure testing scope defined
- [ ] **Non-Standard Terms**: Contractual requirements identified and addressed

### Risk Management
- [ ] **AWS Dependencies**: Service/feature availability and region deployment risks
- [ ] **Partner Dependencies**: Clear work distribution and responsibility documentation
- [ ] **Resource Availability**: Technical skills and experience depth confirmed
- [ ] **Timeline Risks**: Realistic delivery schedules with buffer considerations

## Quality Assurance Gates

### Documentation Standards
- [ ] **Completeness**: All required documentation present and current
- [ ] **Clarity**: Unambiguous requirements and acceptance criteria
- [ ] **Traceability**: Clear mapping from business objectives to technical deliverables
- [ ] **Consistency**: Aligned messaging across all project documents

### Stakeholder Alignment
- [ ] **Customer Expectations**: Mutual understanding of scope and deliverables
- [ ] **Internal Alignment**: Team consensus on approach and resource allocation
- [ ] **Partner Coordination**: Clear responsibilities and communication protocols
- [ ] **Executive Visibility**: Appropriate escalation paths and reporting structures

## Risk Scoring Factors

### Automatic High-Risk Triggers
Any single factor triggers enhanced review:
- [ ] **Large Deal Size**: TCV + AI > $5M USD
- [ ] **Large Fixed Price**: FFP > $500K USD
- [ ] **Low Risk Premium**: FFP with < 15% risk premium
- [ ] **Thin Prime**: Partner delivery > 50% of total hours
- [ ] **Production Access**: Any production environment access
- [ ] **Regulated Data**: Any regulated information handling
- [ ] **Low Security Staffing**: < 8% security resource allocation
- [ ] **Missing AI Approval**: AI/ML without completed RAIR approval

### Delivery Risk Indicators
- [ ] **Customer Cloud Experience**: Limited production cloud experience
- [ ] **Technical Understanding**: Low confidence in environment knowledge
- [ ] **Documentation Gaps**: Missing or incomplete technical specifications
- [ ] **Resource Constraints**: Skill gaps or availability concerns
- [ ] **External Dependencies**: Third-party or AWS service dependencies

## Self-Inspection Outcomes

### Completion Criteria
- [ ] **All Questions Answered**: Complete response to all applicable questions
- [ ] **Evidence Provided**: Supporting documentation for all claims
- [ ] **Risk Assessment**: Honest evaluation of delivery risks and challenges
- [ ] **Mitigation Plans**: Specific actions for identified risks

### Next Steps Based on Outcome

#### OQR Completed (Low Risk)
- [ ] Proceed with implementation planning
- [ ] Monitor for material changes requiring re-inspection
- [ ] Maintain quality standards throughout delivery

#### Bar Raiser Inspection Required (High Risk)
- [ ] Schedule inspection using EnCORE tool
- [ ] Prepare comprehensive documentation package
- [ ] Include all required stakeholders in review process
- [ ] Address recommendations before proceeding

## Material Change Monitoring

### Re-Inspection Triggers
Monitor throughout project lifecycle for:
- [ ] **Contract Value**: ±25% change in total contract value
- [ ] **Billing Type**: Change from T&M to FFP
- [ ] **Partner Role**: Change to thin prime or super thin prime
- [ ] **Production Access**: Addition of production environment access
- [ ] **Regulated Data**: Addition of regulated data handling
- [ ] **AI/ML Scope**: Addition of GenAI or AI/ML services

### Change Management Process
1. **Identify Change**: Recognize material change occurrence
2. **Assess Impact**: Evaluate effect on risk profile and delivery approach
3. **Re-Inspect**: Complete new self-inspection if required
4. **Update Documentation**: Revise all affected project documents
5. **Communicate**: Notify all stakeholders of changes and implications

## Quality Confidence Assessment

### Self-Assessment Scale
Rate your confidence in the inspection responses:
- **90-100%**: Certain these are correct answers
- **70-89%**: Pretty sure or educated guess
- **40-69%**: Best guess with uncertainty
- **0-39%**: No knowledge, just guessing

### Confidence Improvement Actions
- **Below 70%**: Conduct additional discovery and validation
- **70-89%**: Document assumptions and validation plans
- **90-100%**: Proceed with documented confidence rationale
