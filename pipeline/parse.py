"""PDF / Markdown document parser → list of {text, source, page}."""
from __future__ import annotations

import os
from pathlib import Path
from typing import Optional


def parse_pdf(path: str) -> list[dict]:
    from pypdf import PdfReader

    reader = PdfReader(path)
    pages = []
    for i, page in enumerate(reader.pages, 1):
        text = page.extract_text() or ""
        text = text.strip()
        if text:
            pages.append({"text": text, "source": os.path.basename(path), "page": str(i)})
    return pages


def parse_markdown(path: str) -> list[dict]:
    text = Path(path).read_text(encoding="utf-8")
    # Split by ## headers into sections, keep each section as one page
    sections, current = [], []
    for line in text.splitlines():
        if line.startswith("## ") and current:
            sections.append("\n".join(current).strip())
            current = [line]
        else:
            current.append(line)
    if current:
        sections.append("\n".join(current).strip())

    return [
        {"text": s, "source": os.path.basename(path), "page": str(i + 1)}
        for i, s in enumerate(sections)
        if s
    ]


def parse_file(path: str) -> list[dict]:
    ext = Path(path).suffix.lower()
    if ext == ".pdf":
        return parse_pdf(path)
    if ext in (".md", ".txt"):
        return parse_markdown(path)
    raise ValueError(f"Unsupported file type: {ext}")


def parse_directory(directory: str, subject: Optional[str] = None) -> list[dict]:
    """Parse all supported files in a directory, attaching subject metadata."""
    results = []
    for fname in sorted(os.listdir(directory)):
        fpath = os.path.join(directory, fname)
        if not os.path.isfile(fpath):
            continue
        ext = Path(fname).suffix.lower()
        if ext not in (".pdf", ".md", ".txt"):
            continue
        try:
            pages = parse_file(fpath)
            for p in pages:
                p["subject"] = subject or ""
            results.extend(pages)
            print(f"  Parsed {fname}: {len(pages)} pages")
        except Exception as e:
            print(f"  [WARN] Failed to parse {fname}: {e}")
    return results
