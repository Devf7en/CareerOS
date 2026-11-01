from careeros.integrity import validate_reconciliation_references


def snapshot(source="SRC-001", snapshot="snap-1"):
    return {"source_id": source, "snapshot_id": snapshot}


def item(item_id, links=None, group=None, source="SRC-001", snapshot_id="snap-1"):
    return {"item_id": item_id, "source_id": source, "source_snapshot_id": snapshot_id,
            "conflicts_with": links or [], "conflict_group_id": group}


def test_snapshot_reference_must_resolve():
    errors = validate_reconciliation_references([item("a", source="SRC-002")], [snapshot()])
    assert any("snapshot reference" in error for error in errors)


def test_reciprocal_conflict_group_passes():
    items = [item("a", ["b"], "grp-1"), item("b", ["a"], "grp-1")]
    assert validate_reconciliation_references(items, [snapshot()]) == []


def test_nonreciprocal_or_mismatched_conflict_is_reported():
    items = [item("a", ["b"], "grp-1"), item("b", [], "grp-2")]
    errors = validate_reconciliation_references(items, [snapshot()])
    assert any("not reciprocal" in error for error in errors)
    assert any("conflict_group_id" in error for error in errors)


def test_duplicate_item_ids_are_reported():
    errors = validate_reconciliation_references([item("a"), item("a")], [snapshot()])
    assert "item_id: duplicate ID 'a'" in errors
