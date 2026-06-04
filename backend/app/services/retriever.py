from __future__ import annotations

from functools import lru_cache
from typing import Optional

from sentence_transformers import SentenceTransformer

from app.db.chroma import get_collection

MODEL_NAME = "paraphrase-multilingual-MiniLM-L12-v2"


@lru_cache(maxsize=1)
def _get_model() -> SentenceTransformer:
    return SentenceTransformer(MODEL_NAME)


def embed_texts(texts: list[str]) -> list[list[float]]:
    model = _get_model()
    return model.encode(texts, normalize_embeddings=True).tolist()


def retrieve(
    query: str,
    subject: Optional[str] = None,
    top_k: int = 5,
) -> list[dict]:
    """Return top_k chunks most relevant to query."""
    collection = get_collection()
    if collection.count() == 0:
        return []

    query_embedding = embed_texts([query])[0]

    where = {"subject": subject} if subject else None

    results = collection.query(
        query_embeddings=[query_embedding],
        n_results=min(top_k, collection.count()),
        where=where,
        include=["documents", "metadatas", "distances"],
    )

    chunks = []
    for doc, meta, dist in zip(
        results["documents"][0],
        results["metadatas"][0],
        results["distances"][0],
    ):
        chunks.append(
            {
                "text": doc,
                "source": meta.get("source", ""),
                "subject": meta.get("subject", ""),
                "page": meta.get("page", ""),
                "score": round(1 - dist, 4),
            }
        )

    return chunks
