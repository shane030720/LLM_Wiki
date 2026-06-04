import chromadb
from chromadb.config import Settings
import os

_client: chromadb.ClientAPI | None = None
_collection = None

CHROMA_DIR = os.path.join(os.path.dirname(__file__), "..", "..", "..", "chroma_db")
COLLECTION_NAME = "wiki_chunks"


def init_chroma():
    global _client, _collection
    os.makedirs(CHROMA_DIR, exist_ok=True)
    _client = chromadb.PersistentClient(path=CHROMA_DIR)
    _collection = _client.get_or_create_collection(
        name=COLLECTION_NAME,
        metadata={"hnsw:space": "cosine"},
    )
    return _collection


def get_collection():
    if _collection is None:
        init_chroma()
    return _collection
