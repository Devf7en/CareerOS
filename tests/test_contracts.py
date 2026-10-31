import json
from pathlib import Path

import pytest
from jsonschema import Draft202012Validator

ROOT = Path(__file__).resolve().parents[1]


def schema(name):
    data = json.loads((ROOT / "schemas" / name).read_text(encoding="utf-8"))
    Draft202012Validator.check_schema(data)
    return data


def test_all_schemas_are_valid_json_schema():
    for name in ("professional-profile.schema.json", "evidence-item.schema.json", "skill.schema.json", "source-snapshot.schema.json", "reconciliation-item.schema.json"):
        schema(name)


def test_profile_template_validates():
    profile = json.loads((ROOT / "examples" / "profile.template.json").read_text(encoding="utf-8"))
    errors = list(Draft202012Validator(schema("professional-profile.schema.json")).iter_errors(profile))
    assert errors == []


@pytest.mark.parametrize("record", [
    {"evidence_id": "ev-1", "kind": "resume", "label": "CV source", "source": {"source_type": "url", "reference": "https://example.invalid/cv"}, "verification_status": "unverified", "visibility": "private"},
])
def test_valid_evidence_item(record):
    validator = Draft202012Validator(schema("evidence-item.schema.json"))
    assert list(validator.iter_errors(record)) == []


def test_evidence_requires_visibility_and_provenance():
    record = {"evidence_id": "ev-2", "kind": "certificate", "label": "Certificate"}
    errors = list(Draft202012Validator(schema("evidence-item.schema.json")).iter_errors(record))
    assert errors


def test_skill_contract_accepts_unassessed_skill():
    record = {"skill_id": "sk-1", "name": "Product discovery", "category": "product", "proficiency_status": "not_assessed", "verification_status": "unverified", "visibility": "private"}
    errors = list(Draft202012Validator(schema("skill.schema.json")).iter_errors(record))
    assert errors == []


def test_skill_contract_rejects_unsubstantiated_proficiency_label():
    record = {"skill_id": "sk-2", "name": "Example skill", "category": "other", "proficiency_status": "world-class", "verification_status": "unverified", "visibility": "private"}
    errors = list(Draft202012Validator(schema("skill.schema.json")).iter_errors(record))
    assert errors


def test_multi_hat_profile_identity_is_supported():
    profile = json.loads((ROOT / "examples" / "profile.template.json").read_text(encoding="utf-8"))
    profile["professional_hats"] = [
        {"hat_id": "hat-founder", "label": "Founder"},
        {"hat_id": "hat-architect", "label": "Enterprise Architect"}
    ]
    errors = list(Draft202012Validator(schema("professional-profile.schema.json")).iter_errors(profile))
    assert errors == []


def test_reconciliation_item_cannot_be_accepted_while_unverified():
    item = {
        "item_id": "cand-1", "claim_type": "role", "source_id": "SRC-001",
        "source_snapshot_id": "snap-1",
        "source_locator": {"kind": "line", "value": "4"},
        "source_text": "Founder and Product Lead",
        "verification_status": "unverified", "adjudication_status": "accepted",
        "visibility": "private"
    }
    errors = list(Draft202012Validator(schema("reconciliation-item.schema.json")).iter_errors(item))
    assert errors
