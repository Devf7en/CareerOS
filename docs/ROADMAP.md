# CareerOS™ Delivery Roadmap
**Version:** 1.0.0  
**Planning status:** Proposed sequence; completion requires evidence and tests.

## P0 — Trustworthy foundation
- [ ] Repository conventions, versioning and contribution guidance
- [ ] Architecture decision record template
- [ ] Data classification and public/private boundary
- [ ] Canonical profile schema and validation rules
- [ ] Evidence model with provenance and verification status
- [ ] Skills and competency model
- [ ] DOCX/PDF import workflow with human review
- [ ] Portable profile and evidence-metadata export
- [ ] Automated schema and integrity tests

**Exit gate:** profile facts are traceable, sensitive material is excluded from public artifacts, and export/import round trips are tested.

## P1 — Career knowledge base
- [ ] Profile editor and career timeline
- [ ] Organizations, positions, projects and achievements
- [ ] Credentials, certifications and language records
- [ ] Evidence vault metadata and access controls
- [ ] Skills inventory, proficiency levels and evidence links
- [ ] Goals and target-role preferences

**Exit gate:** one validated professional source of truth can be maintained.

## P2 — Opportunity and application operations
- [ ] Employer and opportunity records
- [ ] Job-description capture and structured requirements
- [ ] Application pipeline with configurable stages
- [ ] Follow-up reminders and activity history
- [ ] Explainable role-fit analysis
- [ ] Application outcome tracking

**Exit gate:** each opportunity is traceable from discovery through outcome.

## P3 — Career intelligence studio
- [ ] Requirement-to-evidence mapping
- [ ] CV and profile tailoring drafts
- [ ] Cover-letter drafting
- [ ] Interview preparation and STAR evidence library
- [ ] Gap analysis and development recommendations
- [ ] Human approval and revision history

**Exit gate:** generated claims are grounded in approved facts; drafts are never submitted autonomously.

## P4 — Learning, compensation and analytics
- [ ] Learning plans and course records
- [ ] Certification renewal tracking
- [ ] Compensation expectations and offer comparison
- [ ] Pipeline conversion and response analytics
- [ ] Goal and skill progression dashboards
- [ ] Negotiation preparation workspace

**Exit gate:** analytics are traceable and label incomplete data.

## P5 — Integrations and governed agents
- [ ] Calendar and task integration
- [ ] Approved email drafting and follow-up workflows
- [ ] Job-source adapters with attribution and terms review
- [ ] n8n orchestration with scoped credentials
- [ ] Career Agent tool permissions and audit trail
- [ ] Failure handling, retries and human escalation

**Exit gate:** every external action is permissioned, observable and recoverable.

## P6 — Production readiness
- [ ] Threat model and security review
- [ ] Authentication and role-based access control
- [ ] Backup, restore and disaster-recovery tests
- [ ] Retention, export and deletion workflows
- [ ] Accessibility and performance checks
- [ ] Operational runbooks and incident procedures
- [ ] Multi-user tenancy assessment before SaaS enablement

**Exit gate:** production launch waits for security, recovery, privacy and operational acceptance.

## Delivery rules
- Do not mark an item complete without a commit, test or verifiable artifact.
- Keep the first release modular; introduce microservices only when justified.
- Preserve compatibility through versioned schemas and migrations.
- Separate verified facts, user assertions, inferred values and estimates.
- Record material architecture changes in docs/adr/.
- Keep private source documents and credentials out of the public repository.
