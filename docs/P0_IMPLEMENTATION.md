# CareerOS™ P0 Implementation Record
**Version:** 0.1.0  
**Date:** 2026-10-31  
**Status:** Initial contract implementation committed; CI execution pending GitHub Actions result.

## Implemented in repository
- JSON Schema contracts for professional profiles, evidence items and skills.
- A non-personal profile template with private visibility as its default.
- Python package skeleton and a JSON Schema validation CLI.
- Pytest contract tests covering schema validity, template validity, evidence provenance/visibility requirements, controlled skill proficiency labels, and cross-record profile/evidence reference integrity.
- Cross-record integrity checker for duplicate claim/evidence IDs, unresolved profile-to-evidence references, and unresolved evidence-to-claim references (`src/careeros/integrity.py`), integrated into the validation CLI with `--evidence-file`.
- Development dependencies and package configuration.
- GitHub Actions workflow to run contract tests on pushes to main, pull requests and manual dispatch.
- Source register identifying the uploaded CV files, me.f7en.com, LinkedIn and GitHub portfolio as distinct sources.

## Local validation commands
```bash
python -m venv .venv
source .venv/bin/activate
python -m pip install -e ".[dev]"
python -m pytest -q
python -m careeros.validate profile examples/profile.template.json

# Install optional document parsers and extract a source into a local review file:
python -m pip install -e ".[ingest]"
python -m careeros.ingest /path/to/source.docx --source-id SRC-001 --output private-staging/SRC-001.staging.json
python -m careeros.ingest /path/to/source.pdf --source-id SRC-002 --output private-staging/SRC-002.staging.json
python -m careeros.validate profile path/to/profile.json --evidence-file path/to/evidence.json
```

On Windows PowerShell, activate with `.venv\\Scripts\\Activate.ps1`.

## What is not yet complete
- The workflow has been committed but its first run has not yet been observed; do not claim CI is passing until GitHub reports a successful run.
- The profile schema is an initial contract and needs further domain review before production use.
- Evidence binary storage, authenticated access, encryption, retention and deletion are not implemented.
- DOCX/PDF text extraction is available as an optional local staging CLI. Source reconciliation, OCR for scanned PDFs, and claim-level extraction remain incomplete.
- No personal profile data has yet been migrated into a canonical JSON record; the public template is intentionally generic.
- The me.f7en.com page is registered as a priority source but has not yet been retrieved or verified.

## Acceptance sequence
1. Observe first CI run and fix any failures.
2. Cross-record profile/evidence reference checks have been implemented; next, integrate them into a stable import/validation command and review the separate skill registry versus embedded profile skill projection.
3. Implement safe import staging that preserves original source files and extracted text separately.
4. Reconcile me.f7en.com, DOCX, PDF, LinkedIn and selected GitHub evidence without silent conflict resolution.
5. Generate private canonical profile data only in a suitably private storage location.
6. Generate a reviewed public profile edition from approved public claims.


## P0.3 — Provenance-first reconciliation contracts

### Added contracts
- `schemas/source-snapshot.schema.json` records a captured source independently from the claims later derived from it. It includes source identity, snapshot ID, capture timestamp and method, SHA-256, review status, visibility and limitations.
- `schemas/reconciliation-item.schema.json` records one candidate claim with its source snapshot, exact source wording, locator, optional normalized wording, verification status, adjudication status and conflict links.

### Non-negotiable reconciliation rules
1. Exact source wording is retained in `source_text`; normalization is a separate optional field.
2. A candidate claim is not a verified fact merely because it was extracted or appears in multiple documents.
3. An item can be accepted only when its status is `verified` or `user_confirmed`; inferred, estimated, unverified and disputed items cannot be silently promoted.
4. Conflicts are linked through a conflict-group identifier and explicit item references. They remain open until reviewed.
5. Every item inherits a source snapshot reference and a locator; source provenance is not optional.
6. Visibility defaults operationally to private. A public repository must not contain personal source snapshots or private claim inventories.

### Hat-aware professional identity
CareerOS must model a multi-hat professional as one coherent identity with many concurrent or sequential roles, capability clusters and evidence relationships. A role-specific CV is a derived presentation, not a replacement for the canonical profile. Role labels must not be collapsed into one headline when doing so loses meaningful scope; nor should breadth be exaggerated into unsupported titles or claims.

### Current implementation boundary
These are data contracts only. A reconciliation parser, conflict-group integrity validator, reviewer workflow, private snapshot store and source capture automation remain to be implemented. The me.f7en.com source remains pending actual readable retrieval. No new personal source material has been committed.
