"""Extract source text into a local, private review package; never alter source files."""
from __future__ import annotations

import argparse
import hashlib
import json
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


SUPPORTED = {".docx", ".pdf"}


def sha256_file(path: Path) -> str:
    digest = hashlib.sha256()
    with path.open("rb") as stream:
        for chunk in iter(lambda: stream.read(1024 * 1024), b""):
            digest.update(chunk)
    return digest.hexdigest()


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".docx":
        try:
            from docx import Document
        except ImportError as exc:
            raise RuntimeError("Install the 'ingest' extra: pip install -e '.[ingest]'") from exc
        document = Document(str(path))
        chunks = [paragraph.text for paragraph in document.paragraphs if paragraph.text.strip()]
        for table in document.tables:
            for row in table.rows:
                chunks.append(" | ".join(cell.text.replace("\\n", " ").strip() for cell in row.cells))
        return "\\n".join(chunks).strip()
    if suffix == ".pdf":
        try:
            from pypdf import PdfReader
        except ImportError as exc:
            raise RuntimeError("Install the 'ingest' extra: pip install -e '.[ingest]'") from exc
        reader = PdfReader(str(path))
        return "\\n\\n".join((page.extract_text() or "") for page in reader.pages).strip()
    raise ValueError(f"Unsupported file type: {suffix}")


def build_staging_record(path: Path, source_id: str) -> dict[str, Any]:
    resolved = path.expanduser().resolve(strict=True)
    if not resolved.is_file():
        raise ValueError(f"Not a file: {resolved}")
    if resolved.suffix.lower() not in SUPPORTED:
        raise ValueError(f"Supported formats: {', '.join(sorted(SUPPORTED))}")
    return {
        "staging_version": "1.0.0",
        "source_id": source_id,
        "source_name": resolved.name,
        "source_format": resolved.suffix.lower().lstrip("."),
        "source_sha256": sha256_file(resolved),
        "extracted_at": datetime.now(timezone.utc).isoformat(),
        "review_status": "pending_human_review",
        "extraction_warning": "Text extraction may omit layout, images, scanned text, annotations, headers or footers. Review against the original.",
        "text": extract_text(resolved),
    }


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("source", type=Path)
    parser.add_argument("--source-id", required=True)
    parser.add_argument("--output", type=Path, required=True)
    args = parser.parse_args()
    try:
        record = build_staging_record(args.source, args.source_id)
        output = args.output.expanduser()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(record, ensure_ascii=False, indent=2) + "\\n", encoding="utf-8")
    except (OSError, ValueError, RuntimeError) as exc:
        parser.error(str(exc))
    print(f"Created private review staging file: {output}")
    print("No claims were verified or promoted. Review the extracted text against its original source.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
