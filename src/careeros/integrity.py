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
        check_refs(f"claims/{index}/provenance/evidence_ids", claim.get("provenance", {}).get("evidence_ids", []))
    for collection in ("skills", "projects"):
        for index, item in enumerate(profile.get(collection, [])):
            check_refs(f"{collection}/{index}/evidence_ids", item.get("evidence_ids", []))
    for index, item in enumerate(evidence_items):
        for value in sorted(set(item.get("related_claim_ids", []))):
            if value not in known_claims:
                errors.append(f"evidence/{index}/related_claim_ids: claim ID '{value}' is unresolved")
    return sorted(errors)


def validate_reconciliation_references(
    items: list[dict[str, Any]], snapshots: list[dict[str, Any]]
) -> list[str]:
    """Validate snapshot references and explicit, reciprocal conflict links."""
    errors: list[str] = []
    item_ids = [item.get("item_id") for item in items]
    for value, count in Counter(item_ids).items():
        if value is not None and count > 1:
            errors.append(f"item_id: duplicate ID '{value}'")
    snapshot_keys = {(s.get("source_id"), s.get("snapshot_id")) for s in snapshots}
    known_ids = {value for value in item_ids if isinstance(value, str)}
    by_id = {item.get("item_id"): item for item in items if isinstance(item.get("item_id"), str)}

    for index, item in enumerate(items):
        key = (item.get("source_id"), item.get("source_snapshot_id"))
        if key not in snapshot_keys:
            errors.append(f"reconciliation/{index}: source snapshot reference {key!r} is unresolved")
        links = item.get("conflicts_with", [])
        if item.get("item_id") in links:
            errors.append(f"reconciliation/{index}: item cannot conflict with itself")
        for linked_id in links:
            if linked_id not in known_ids:
                errors.append(f"reconciliation/{index}: conflict item '{linked_id}' is unresolved")
                continue
            linked = by_id[linked_id]
            if item.get("item_id") not in linked.get("conflicts_with", []):
                errors.append(f"reconciliation/{index}: conflict link to '{linked_id}' is not reciprocal")
            group = item.get("conflict_group_id")
            if not group or linked.get("conflict_group_id") != group:
                errors.append(f"reconciliation/{index}: conflict link to '{linked_id}' must share a conflict_group_id")
    return sorted(errors)
