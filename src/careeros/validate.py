"""Validate CareerOS JSON records against versioned JSON Schema contracts."""
from __future__ import annotations

import argparse
import json
from pathlib import Path
from typing import Any

from jsonschema import Draft202012Validator, FormatChecker

ROOT = Path(__file__).resolve().parents[2]
SCHEMAS = {
    "profile": ROOT / "schemas" / "professional-profile.schema.json",
    "evidence": ROOT / "schemas" / "evidence-item.schema.json",
    "skill": ROOT / "schemas" / "skill.schema.json",
}


def load_json(path: Path) -> Any:
    with path.open("r", encoding="utf-8") as stream:
        return json.load(stream)


def validate_record(kind: str, record: Any) -> list[str]:
    """Return deterministic, human-readable validation errors."""
    if kind not in SCHEMAS:
        raise ValueError(f"Unsupported record kind: {kind}")
    schema = load_json(SCHEMAS[kind])
    validator = Draft202012Validator(schema, format_checker=FormatChecker())
    errors = sorted(validator.iter_errors(record), key=lambda error: list(map(str, error.path)))
    return [f"{'/'.join(map(str, error.path)) or '$'}: {error.message}" for error in errors]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("kind", choices=sorted(SCHEMAS))
    parser.add_argument("record", type=Path)
    args = parser.parse_args()
    try:
        record = load_json(args.record)
        errors = validate_record(args.kind, record)
    except (OSError, json.JSONDecodeError, ValueError) as exc:
        parser.error(str(exc))
    if errors:
        print("\n".join(errors))
        return 1
    print(f"Valid CareerOS {args.kind} record: {args.record}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
