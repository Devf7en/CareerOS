from careeros.integrity import validate_profile_references


def test_valid_cross_references_pass():
    profile = {"claims": [{"claim_id": "cl-1", "provenance": {"evidence_ids": ["ev-1"]}}], "skills": [{"evidence_ids": ["ev-1"]}], "projects": []}
    evidence = [{"evidence_id": "ev-1", "related_claim_ids": ["cl-1"]}]
    assert validate_profile_references(profile, evidence) == []


def test_unresolved_profile_evidence_reference_is_reported():
    profile = {"claims": [{"claim_id": "cl-1", "provenance": {"evidence_ids": ["missing"]}}]}
    assert "claims/0/provenance/evidence_ids: evidence ID 'missing' is unresolved" in validate_profile_references(profile, [])


def test_unresolved_evidence_claim_reference_is_reported():
    profile = {"claims": []}
    evidence = [{"evidence_id": "ev-1", "related_claim_ids": ["missing"]}]
    assert "evidence/0/related_claim_ids: claim ID 'missing' is unresolved" in validate_profile_references(profile, evidence)


def test_duplicate_ids_are_reported():
    profile = {"claims": [{"claim_id": "cl-1"}, {"claim_id": "cl-1"}]}
    evidence = [{"evidence_id": "ev-1"}, {"evidence_id": "ev-1"}]
    errors = validate_profile_references(profile, evidence)
    assert "claim_id: duplicate ID 'cl-1'" in errors
    assert "evidence_id: duplicate ID 'ev-1'" in errors
