from careeros.reconcile import extract_line_candidates, normalize_for_comparison


def test_line_candidates_preserve_exact_source_text_and_locations():
    staging = {
        "source_id": "SRC-001",
        "snapshot_id": "snap-a",
        "extracted_text": "Founder & Product Lead\n\nMay 2020 - Present "
    }
    result = extract_line_candidates(staging)
    assert [item["source_text"] for item in result] == [
        "Founder & Product Lead", "May 2020 - Present "
    ]
    assert [item["source_locator"]["value"] for item in result] == ["1", "3"]
    assert all(item["verification_status"] == "unverified" for item in result)
    assert all(item["adjudication_status"] == "unreviewed" for item in result)
    assert all(item["visibility"] == "private" for item in result)


def test_candidate_ids_are_deterministic_for_same_source_snapshot_and_line():
    staging = {"source_id": "SRC-001", "snapshot_id": "snap-a", "extracted_text": "A claim"}
    assert extract_line_candidates(staging) == extract_line_candidates(staging)


def test_candidate_ids_change_when_source_snapshot_changes():
    base = {"source_id": "SRC-001", "snapshot_id": "snap-a", "extracted_text": "A claim"}
    changed = {**base, "snapshot_id": "snap-b"}
    assert extract_line_candidates(base)[0]["item_id"] != extract_line_candidates(changed)[0]["item_id"]


def test_missing_source_identity_is_rejected():
    try:
        extract_line_candidates({"extracted_text": "A claim"})
    except ValueError as exc:
        assert "source_id" in str(exc)
    else:
        raise AssertionError("Expected missing source identity to fail")


def test_comparison_normalization_does_not_rewrite_source_text():
    assert normalize_for_comparison("  Senior  Product\nManager ") == "senior product manager"
