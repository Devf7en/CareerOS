import hashlib

from careeros.ingest import build_staging_record, sha256_file


def test_sha256_file_matches_standard_digest(tmp_path):
    source = tmp_path / "source.txt"
    source.write_bytes(b"career evidence")
    assert sha256_file(source) == hashlib.sha256(b"career evidence").hexdigest()


def test_unsupported_format_is_rejected(tmp_path):
    source = tmp_path / "source.txt"
    source.write_text("not a CV")
    try:
        build_staging_record(source, "SRC-test")
    except ValueError as exc:
        assert "Supported formats" in str(exc)
    else:
        raise AssertionError("Unsupported file type should be rejected")
