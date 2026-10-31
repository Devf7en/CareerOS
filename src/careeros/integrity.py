from __future__ import annotations

from collections import Counter
from typing import Any


def validate_profile_references(profile: dict[str, Any], evidence_items: list[dict[str, Any]]) -> list[str]:
    """Check profile/evidence IDs and cross-document references after schema validation."""
    errors: list[str] = []
    evidence_ids = [item.get("evidence_id") for item in evidence_items]
    claim_ids = [claim.get("claim_id") for claim in profile.get("claims", [])]
    for label, values in (("evidence_id", evidence_ids), ("claim_id", claim_ids)):
        for value, count in Counter(values).items():
            if value is not None and count > 1:
                errors.append(f"{label}: duplicate ID '{value}'")
    known_evidence = {value for value in evidence_ids if isinstance(value, str)}
    known_claims = {value for value in claim_ids if isinstance(value, str)}

    def check_refs(path: str, refs: list[str]) -> None:
        for value in sorted(set(refs)):
            if value not in known_evidence:
                errors.append(f"{path}: evidence ID '{value}' is unresolved")

    for index, claim in enumerate(profile.get("claims", [])):
        refs = claim.get("provenance", {}).get("evidence_ids", [])
        check_refs(f"claims/{index}/provenance/evidence_ids", refs)
    for collection in ("skills", "projects"):
        for index, item in enumerate(profile.get(collection, [])):
            check_refs(f"{collection}/{index}/evidence_ids", item.get("evidence_ids", []))
    for index, item in enumerate(evidence_items):
        for value in sorted(set(item.get("related_claim_ids", []))):
            if value not in known_claims:
                errors.append(f"evidence/{index}/related_claim_ids: claim ID '{value}' is unresolved")
    return sorted(errors)
