# CareerOS™ Source Register
**Version:** 1.0.0  
**Purpose:** Track source material used to construct and maintain the canonical professional profile.

## Source inventory

| Source ID | Source | Type | Current status | Intended use |
|---|---|---|---|---|
| SRC-001 | User-supplied `CV6_Senior_Product_Manager_OSLondon_v1.0.docx` | Primary document | Available in originating conversation; not stored publicly | Profile facts, career chronology, skills, education and product portfolio |
| SRC-002 | User-supplied `CV6_Senior_Product_Manager_OSLondon_v1.0.pdf` | Primary document | Available in originating conversation; not stored publicly | Cross-check designed CV presentation and content |
| SRC-003 | `https://me.f7en.com` | User-identified online résumé/profile | Identified by user; retrieval not yet verified | Priority source for professional profile reconciliation |
| SRC-004 | `https://www.linkedin.com/in/solomonlondon` | Professional network profile | Known profile URL; contents not yet reconciled in this release | Career history, certifications, public professional evidence |
| SRC-005 | `https://github.com/Devf7en` | Public code portfolio | Known profile URL; repository evidence requires project-by-project review | Technical artefacts, contributions and project evidence |

## SRC-003 — me.f7en.com verification record
The user explicitly identified me.f7en.com as a résumé source. It was not included in the initial CV transcription. A web retrieval attempt on 2026-10-31 did not return readable page content. Search results did not provide a reliable indexed résumé page.

**Status:** Pending source access and review.  
**Do not infer:** page contents, currentness, completeness, ownership, or agreement with uploaded CV.  
**Next action:** retrieve the page through an accessible browser/session or obtain an export/snapshot from the user. Then record retrieval date, page title, content hash, extracted claims and discrepancies.

## Reconciliation policy
1. Preserve every source separately; do not overwrite source facts during reconciliation.
2. Normalize dates, organization names and role titles only in derived fields, retaining original wording.
3. Record conflicts explicitly with both source references.
4. Ask the user to adjudicate material conflicts; do not silently choose a version.
5. Assign claim status: verified, user_confirmed, inferred, estimated or unverified.
6. Maintain source URL/file reference, retrieval timestamp and evidence item IDs for each material claim.
7. Treat third-party search snippets and data-broker pages as leads, not authoritative career evidence.

## Public release
The CareerOS repository is public. Do not commit private CV exports, direct personal contact details, identity records, private references or confidential employment evidence. Publish only an intentionally reviewed public profile edition.
