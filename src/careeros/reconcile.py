"""Deterministic candidate extraction for human-reviewed source reconciliation."""
from __future__ import annotations

import hashlib
import re
from typing import Any


def extract_line_candidates(
    staging_record: dict[str, Any],
    *,
    source_id: str | None = None,
    snapshot_id: str | None = None,
) -> list[dict[str, Any]]:
    """Turn non-empty source lines into unverified candidates without rewriting them.

    This deliberately performs no semantic inference, deduplication, verification,
    or promotion. Each candidate retains its exact line and one-based line locator.
    """
    resolved_source_id = source_id or staging_record.get("source_id")
    if not isinstance(resolved_source_id, str) or not resolved_source_id:
        raise ValueError("A source_id is required")
    resolved_snapshot_id = snapshot_id or staging_record.get("snapshot_id") or staging_record.get("source_sha256")
    if not isinstance(resolved_snapshot_id, str) or not resolved_snapshot_id:
        raise ValueError("A snapshot_id or source hash is required")
    text = staging_record.get("extracted_text")
    if not isinstance(text, str):
        raise ValueError("staging_record.extracted_text must be a string")

    candidates: list[dict[str, Any]] = []
    for line_number, raw_line in enumerate(text.splitlines(), start=1):
        if not raw_line.strip():
            continue
        candidate_id = hashlib.sha256(
            f"{resolved_source_id}\0{resolved_snapshot_id}\0{line_number}\0{raw_line}".encode("utf-8")
        ).hexdigest()[:20]
        candidates.append({
            "item_id": f"cand-{candidate_id}",
            "claim_type": "other",
            "source_id": resolved_source_id,
            "source_snapshot_id": resolved_snapshot_id,
            "source_locator": {"kind": "line", "value": str(line_number)},
            "source_text": raw_line,
            "verification_status": "unverified",
            "adjudication_status": "unreviewed",
            "visibility": "private",
        })
    return candidates


def normalize_for_comparison(text: str) -> str:
    """Conservative comparison key; never use this value as source wording."""
    return re.sub(r"\s+", " ", text).strip().casefold()
