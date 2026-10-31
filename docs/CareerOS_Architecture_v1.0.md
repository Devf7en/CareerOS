# CareerOS™ — Career Operating System Architecture
**Version:** 1.0.0  
**Status:** Foundation specification  
**Architecture alignment:** EBMA™ (b3Ɛq Enterprise Bio-Mimetic Architecture™)

## 1. Purpose
CareerOS is a personal career operating system for managing professional identity, evidence, capabilities, opportunities, applications, relationships, learning, compensation and career decisions as one connected system.

It is not simply a résumé builder or job board. It maintains a trustworthy representation of professional value and translates evidence into career outcomes.

## 2. Product principles
1. **Evidence before claims:** material claims trace to evidence, a source, or an explicitly marked estimate.
2. **One professional source of truth:** maintain canonical career facts and generate role-specific views from them.
3. **Human authority:** recommendations and generated materials require review; no application, message or commitment is submitted without authorization.
4. **Privacy by design:** sensitive data, identity documents, private references and private evidence do not belong in public repositories.
5. **Portability:** user data must be exportable in documented formats.
6. **Explainable intelligence:** recommendations expose rationale, evidence and uncertainty.
7. **Continuous learning:** outcomes improve future targeting, positioning and development plans.
8. **Multilingual readiness:** English-first foundation with Spanish support; proficiency remains evidence-based.

## 3. Core capabilities
- Identity & Profile: biography, roles, career timeline, work authorization, languages and positioning.
- Evidence Vault: credentials, certifications, work samples, references, achievements and provenance.
- Skills & Competencies: skill taxonomy, proficiency, recency, evidence and development gaps.
- Portfolio & Projects: products, programmes, case studies, outcomes and attributable contributions.
- Opportunity Intelligence: target roles, employers, markets, job descriptions and fit analysis.
- Application Pipeline: opportunities, tailoring, submissions, follow-ups, interviews and outcomes.
- Interview Studio: role research, question banks, STAR evidence, practice and feedback.
- Learning & Certification: plans, courses, credentials, renewals and skill progression.
- Compensation & Negotiation: expectations, total-reward comparisons and decision records.
- Network & Relationships: contacts, referrals, interactions and follow-up commitments.
- Career Analytics: conversion, skill gaps, response rates, compensation outcomes and goal progress.
- Career Agent: governed assistant for research, analysis, drafting and workflow support.

## 4. Reference architecture
### Experience
Responsive application, accessible dashboards, profile editor, evidence workspace, opportunity board and interview workspace. Nuxt 4 is the preferred application-shell direction, subject to validation.

### Domain/application
Modular domain services own business rules and expose versioned interfaces. Begin as a modular monolith; do not prematurely split into microservices.

### Intelligence
AI-assisted extraction, classification, role matching, evidence-to-requirement mapping, drafting, interview preparation, analytics and recommendations. Python is preferred for AI, analytics and automation workloads.

### Integration and automation
Adapters for job sources, calendars, document storage, email and learning platforms. n8n may orchestrate approved workflows. Integrations use scoped credentials and auditable execution.

### Data
Relational system of record, object/document evidence storage, search index and event/audit history. PostgreSQL is the preferred relational foundation. Support export, backup, restore and retention controls.

### Security and governance
Authentication, authorization, consent, data classification, encryption, secrets management, audit, retention, deletion, model-use controls and human approval gates.

## 5. Canonical domain entities
Person, ProfessionalProfile, CareerPosition, Organization, Project, Product, Achievement, Skill, CompetencyAssessment, EvidenceItem, Credential, Language, CareerGoal, TargetRole, Employer, Opportunity, Application, ApplicationEvent, Interview, Contact, Interaction, LearningPlan, LearningActivity, CompensationExpectation, Offer, Recommendation, ConsentRecord and AuditEvent.

Material claims should support provenance fields: source, evidence reference, date observed, confidence, verification status, owner and visibility classification.

## 6. Core lifecycle
Capture → Verify → Structure → Assess → Position → Discover → Match → Prepare → Apply → Interview → Decide → Learn → Reassess.

An outcome may update strategy and development priorities, but must not silently rewrite verified historical facts.

## 7. AI operating contract
The Career Agent may structure user-provided material, identify missing/conflicting evidence, compare profiles with roles, draft tailored materials, prepare interviews and analyze pipeline/learning data.

It must not invent employment, qualifications, certifications, metrics or achievements; upgrade proficiency without evidence; submit applications or send messages without approval; expose private data to external services without consent; or present estimates as verified facts.

## 8. EBMA™ alignment
CareerOS adopts EBMA™ as its architecture-governance reference. This is a functional mapping for this product, not a claim that every EBMA organ is implemented.

| EBMA-inspired concern | CareerOS responsibility |
|---|---|
| Identity and structure | Person, profile, roles and organizational context |
| Memory and records | Evidence vault, career history and audit trail |
| Sensing and observation | Opportunity feeds, market signals and activity capture |
| Intelligence | Skill analysis, matching and career analytics |
| Decision | Goals, fit assessments and decision records |
| Action | Approved applications, messages and learning actions |
| Coordination | Workflow orchestration and integrations |
| Homeostasis | Goal, workload, pipeline and data-quality monitoring |
| Governance | Consent, access control, provenance and policy enforcement |
| Learning and evolution | Outcome analysis, skill development and system improvement |

System-wide intelligence follows the b3Ɛq pattern: **Observe, Understand, Predict, Recommend, Simulate, Act, Learn**. Actions remain permissioned and auditable.

## 9. Non-functional requirements
Security by least privilege; privacy and user-controlled export/deletion; tested backup/restore; automated domain, authorization and integrity tests; structured logs and audit events; documented APIs; accessibility; locale-aware dates/currencies; versioned schemas and operational runbooks.

## 10. Delivery strategy
1. Establish repository standards, data classification and architecture decisions.
2. Implement identity, profile, evidence and skills as the trusted source of truth.
3. Add opportunity and application pipeline.
4. Add role matching, CV tailoring and interview preparation.
5. Add learning, compensation and analytics.
6. Add controlled integrations and agent workflows.
7. Harden for multi-user SaaS only after single-user security, tenancy and operational controls are reliable.

## 11. Foundation definition of done
Architecture and roadmap are version-controlled; public/private boundaries documented; core entities and provenance defined; AI and human approval boundaries explicit; initial implementation testable without live integrations; no credentials or private identity evidence in the public repository.

## 12. Open decisions
Authentication provider, object storage, search engine, hosting topology, job-source connectors, email/calendar integrations, multi-user tenancy, retention defaults and recovery objectives require validation and an architecture decision record.
