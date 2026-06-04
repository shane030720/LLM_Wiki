#!/usr/bin/env python3
"""
Embedding pipeline — parse → chunk → embed → upsert to ChromaDB.

Usage:
  python pipeline/embed.py --subject 자료구조 --dir raw/자료구조/
  python pipeline/embed.py --subject 시스템분석이론 --dir raw/
  python pipeline/embed.py --all   # processes raw/ with auto subject detection
"""
from __future__ import annotations

import argparse
import os
import sys

# Allow imports from project root
sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "backend"))

from pipeline.parse import parse_directory
from pipeline.chunk import chunk_pages

BATCH_SIZE = 64


def get_embedder():
    from sentence_transformers import SentenceTransformer
    print("Loading embedding model...")
    return SentenceTransformer("paraphrase-multilingual-MiniLM-L12-v2")


def embed_and_upsert(chunks: list[dict], model, collection):
    texts = [c["text"] for c in chunks]
    ids   = [c["id"] for c in chunks]
    metas = [{"source": c["source"], "subject": c["subject"], "page": c["page"]} for c in chunks]

    for i in range(0, len(texts), BATCH_SIZE):
        batch_t = texts[i : i + BATCH_SIZE]
        batch_i = ids[i : i + BATCH_SIZE]
        batch_m = metas[i : i + BATCH_SIZE]

        embeddings = model.encode(batch_t, normalize_embeddings=True).tolist()
        collection.upsert(
            ids=batch_i,
            documents=batch_t,
            embeddings=embeddings,
            metadatas=batch_m,
        )
        print(f"  Upserted {i + len(batch_t)}/{len(texts)} chunks")


def run(directory: str, subject: str):
    import chromadb

    chroma_dir = os.path.join(os.path.dirname(__file__), "..", "chroma_db")
    os.makedirs(chroma_dir, exist_ok=True)
    client = chromadb.PersistentClient(path=chroma_dir)
    collection = client.get_or_create_collection(
        "wiki_chunks", metadata={"hnsw:space": "cosine"}
    )

    print(f"\n=== Ingesting: {directory} (subject={subject}) ===")
    pages = parse_directory(directory, subject=subject)
    print(f"Parsed {len(pages)} pages total")

    chunks = chunk_pages(pages)
    print(f"Generated {len(chunks)} chunks")

    model = get_embedder()
    embed_and_upsert(chunks, model, collection)
    print(f"Done. Total chunks in DB: {collection.count()}\n")


def main():
    parser = argparse.ArgumentParser(description="Embed documents into ChromaDB")
    parser.add_argument("--dir", default="raw", help="Directory with source documents")
    parser.add_argument("--subject", default="시스템분석이론", help="Subject label")
    args = parser.parse_args()

    run(args.dir, args.subject)


if __name__ == "__main__":
    main()
