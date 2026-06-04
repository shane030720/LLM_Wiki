"""Sliding-window chunker for parsed pages."""
from __future__ import annotations

import re
import uuid


def _split_sentences(text: str) -> list[str]:
    """Split text into sentences on Korean/English sentence boundaries."""
    # Split on period/question/exclamation followed by space or newline
    parts = re.split(r"(?<=[.!?。])\s+", text)
    return [p.strip() for p in parts if p.strip()]


def chunk_page(
    page: dict,
    max_chars: int = 800,
    overlap_chars: int = 150,
) -> list[dict]:
    """
    Split one page dict into overlapping chunks.
    Each chunk inherits source/subject/page metadata.
    """
    text = page["text"]
    if len(text) <= max_chars:
        return [
            {
                "id": str(uuid.uuid4()),
                "text": text,
                "source": page.get("source", ""),
                "subject": page.get("subject", ""),
                "page": page.get("page", ""),
            }
        ]

    sentences = _split_sentences(text)
    chunks = []
    buf, buf_len = [], 0
    overlap_buf: list[str] = []

    for sent in sentences:
        slen = len(sent)
        if buf_len + slen > max_chars and buf:
            chunk_text = " ".join(buf)
            chunks.append(
                {
                    "id": str(uuid.uuid4()),
                    "text": chunk_text,
                    "source": page.get("source", ""),
                    "subject": page.get("subject", ""),
                    "page": page.get("page", ""),
                }
            )
            # Build overlap window from tail of current buffer
            overlap_buf = []
            overlap_len = 0
            for s in reversed(buf):
                if overlap_len + len(s) > overlap_chars:
                    break
                overlap_buf.insert(0, s)
                overlap_len += len(s)
            buf = overlap_buf[:]
            buf_len = overlap_len

        buf.append(sent)
        buf_len += slen

    if buf:
        chunks.append(
            {
                "id": str(uuid.uuid4()),
                "text": " ".join(buf),
                "source": page.get("source", ""),
                "subject": page.get("subject", ""),
                "page": page.get("page", ""),
            }
        )

    return chunks


def chunk_pages(pages: list[dict], **kwargs) -> list[dict]:
    chunks = []
    for page in pages:
        chunks.extend(chunk_page(page, **kwargs))
    return chunks
