# CareerOS™ Privacy and Data Governance
**Version:** 1.0.0  
**Scope:** Repository publication and future CareerOS data handling.

## 1. Data classes
| Class | Examples | Public repository policy |
|---|---|---|
| Public professional | Approved biography, public portfolio links, selected achievements | Allowed after review |
| Personal contact | Personal email, phone, home address, private social accounts | Do not publish by default |
| Confidential career evidence | Employment letters, private references, contracts, payslips, assessments | Prohibited |
| Identity and legal | Passport, immigration documents, government identifiers | Prohibited |
| Credentials and secrets | Passwords, API keys, tokens, recovery codes | Prohibited |
| Derived analysis | Role-fit scores, salary analysis, private notes | Private by default |

## 2. Repository rule
CareerOS is a public GitHub repository. Treat every committed file, commit history, issue, discussion and workflow log as potentially visible and copied. Only publish material explicitly reviewed for public release. Deleting a file in a later commit does not erase its earlier appearance in Git history or third-party copies.

## 3. Source-document handling
The supplied CV source files include direct contact information. The public Markdown profile was prepared without reproducing those details. Original DOCX/PDF files should remain outside this public repository until the exact publication content is reviewed, unnecessary personal data is removed, metadata and embedded content are checked, and public release is deliberately approved.

Preferred pattern: public professional portfolio repository plus private evidence storage with access controls.

## 4. Provenance and accuracy
Classify each professional claim as:
- **Verified:** supported by reviewed evidence.
- **User-confirmed:** explicitly confirmed by the user; evidence not independently checked.
- **Inferred:** derived from other facts and requiring confirmation.
- **Estimated:** approximate value with method disclosed.
- **Unverified:** source or accuracy not yet established.

Never silently promote inferred, estimated or unverified claims to verified.

## 5. AI and external processing
Before sending profile or evidence data to an external model, job platform or integration, disclose the data categories and obtain appropriate authorization. Minimize payloads. Do not send identity documents, private references or credentials unless a specific, necessary and consented workflow exists.

## 6. Access and lifecycle controls
The application design must support least-privilege access, explicit evidence visibility, secure secrets handling, audit records, user export, correction/deletion workflows and documented retention/backup policies.

Deletion from the live application must be distinguished from retention in backups and immutable audit records; those policies require explicit design and disclosure.

## 7. Incident response
If sensitive information is published: restrict access where possible; revoke exposed credentials; assess Git history, forks, caches and copies; rotate secrets; notify affected parties where appropriate; record corrective actions. Do not claim complete erasure merely because a file was deleted from the latest branch.
