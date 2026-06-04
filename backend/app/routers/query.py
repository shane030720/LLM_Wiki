from __future__ import annotations

import json
from typing import Optional

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from sse_starlette.sse import EventSourceResponse

from app.services.retriever import retrieve
from app.services.llm import stream_answer, generate_exam, _source_list

router = APIRouter()


class QueryRequest(BaseModel):
    question: str
    subject: Optional[str] = None
    top_k: int = 5


class ExamRequest(BaseModel):
    subject: str
    topic: str
    difficulty: str = "중"
    count: int = 5


@router.post("/query")
async def query_rag(req: QueryRequest):
    """SSE streaming RAG answer."""
    chunks = retrieve(req.question, subject=req.subject, top_k=req.top_k)

    async def event_generator():
        # First, send source metadata
        sources = _source_list(chunks)
        yield {"event": "sources", "data": json.dumps(sources, ensure_ascii=False)}

        # Then stream the answer tokens
        async for token in stream_answer(req.question, chunks):
            yield {"event": "token", "data": token}

        yield {"event": "done", "data": ""}

    return EventSourceResponse(event_generator())


@router.post("/query/exam")
async def query_exam(req: ExamRequest):
    """Generate exam questions (non-streaming)."""
    chunks = retrieve(req.topic, subject=req.subject if hasattr(req, "subject") else req.subject, top_k=8)
    text = await generate_exam(req.subject, req.topic, req.difficulty, chunks, req.count)
    sources = _source_list(chunks)
    return {"answer": text, "sources": sources}


@router.get("/health")
def health():
    return {"status": "ok"}


@router.get("/stats")
def stats():
    from app.db.chroma import get_collection
    col = get_collection()
    return {"total_chunks": col.count()}
