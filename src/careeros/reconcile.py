"""Deterministic candidate extraction and private reconciliation staging."""
from __future__ import annotations

import argparse
import hashlib
import json
import re
from pathlib import Path
from typing import Any


def extract_line_candidates(
    staging_record: dict[str, Any],
    *,
    source_id: str | None = None,
    snapshot_id: str | None = None,
) -> list[dict[str, Any]]:
    """Create unverified candidates while preserving exact source lines."""
    resolved_source_id = source_id or staging_record.get("source_id")
    if not isinstance(resolved_source_id, str) or not resolved_source_id:
        raise ValueError("A source_id is required")
    resolved_snapshot_id = snapshot_id or staging_record.get("snapshot_id") or staging_record.get("source_sha256")
    if not isinstance(resolved_snapshot_id, str) or not resolved_snapshot_id:
        raise ValueError("A snapshot_id or source hash is required")
    source_text = staging_record.get("extracted_text")
    if not isinstance(source_text, str):
        raise ValueError("staging_record.extracted_text must be a string")

    candidates = []
    for line_number, raw_line in enumerate(source_text.splitlines(), start=1):
        if not raw_line.strip():
            continue
        digest = hashlib.sha256(
            f"{resolved_source_id}\0{resolved_snapshot_id}\0{line_number}\0{raw_line}".encode("utf-8")
        ).hexdigest()[:20]
        candidates.append({
            "item_id": f"cand-{digest}",
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
    """Return a comparison key; never use it as replacement source wording."""
    return re.sub(r"\s+", " ", text).strip().casefold()


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("staging_record", type=Path, help="Local JSON produced by careeros.ingest")
    parser.add_argument("--source-id", help="Override source ID only when correcting a staging record")
    parser.add_argument("--snapshot-id", help="Stable snapshot ID; defaults to the staging source hash")
    parser.add_argument("--output", type=Path, required=True, help="Output path under private-staging/")
    args = parser.parse_args()
    try:
        if "private-staging" not in args.output.parts:
            parser.error("Output must be stored under private-staging/; do not write private candidates to the public repository")
        staging = json.loads(args.staging_record.read_text(encoding="utf-8"))
        candidates = extract_line_candidates(staging, source_id=args.source_id, snapshot_id=args.snapshot_id)
        args.output.parent.mkdir(parents=True, exist_ok=True)
        args.output.write_text(json.dumps(candidates, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    print(f"Staged {len(candidates)} private, unverified candidates at {args.output}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
