"""
LLM Provider 추상화 — LiteLLM 기반

.env 의 LLM_MODEL 한 줄만 바꾸면 Claude / OpenAI / Gemini / Ollama 등 전환 가능.

지원 모델 예시:
  anthropic/claude-sonnet-4-6   → Claude  (ANTHROPIC_API_KEY 필요)
  openai/gpt-4o                 → OpenAI  (OPENAI_API_KEY 필요)
  gemini/gemini-1.5-flash       → Gemini  (GOOGLE_API_KEY 필요, 무료 티어 있음)
  ollama/llama3                 → 로컬     (API 키 불필요)
"""
from __future__ import annotations

import os
from pathlib import Path
from typing import AsyncIterator, Iterator

import litellm
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

LLM_MODEL   = os.environ.get("LLM_MODEL", "anthropic/claude-sonnet-4-6")
LLM_TIMEOUT = int(os.environ.get("LLM_TIMEOUT", "300"))

litellm.set_verbose = False


def _messages(system: str | None, prompt: str) -> list[dict]:
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})
    return msgs


# ── 동기 호출 (CLI 에이전트용) ────────────────────────────────────────────────

def run(prompt: str, system: str | None = None) -> str:
    """단발 호출, 결과 문자열 반환."""
    response = litellm.completion(
        model=LLM_MODEL,
        messages=_messages(system, prompt),
        timeout=LLM_TIMEOUT,
    )
    return response.choices[0].message.content or ""


def stream(prompt: str, system: str | None = None) -> Iterator[str]:
    """동기 스트리밍 — stdout에 chunk 단위로 출력할 때 사용."""
    response = litellm.completion(
        model=LLM_MODEL,
        messages=_messages(system, prompt),
        stream=True,
        timeout=LLM_TIMEOUT,
    )
    for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ── 비동기 스트리밍 (FastAPI StreamingResponse용) ─────────────────────────────

async def astream(prompt: str, system: str | None = None) -> AsyncIterator[str]:
    """비동기 스트리밍 — FastAPI 라우터에서 직접 사용."""
    response = await litellm.acompletion(
        model=LLM_MODEL,
        messages=_messages(system, prompt),
        stream=True,
        timeout=LLM_TIMEOUT,
    )
    async for chunk in response:
        delta = chunk.choices[0].delta.content
        if delta:
            yield delta


# ── 웹 검색 (모든 LLM에서 동작, API 키 불필요) ───────────────────────────────

def web_search(query: str, max_results: int = 5) -> str:
    """DuckDuckGo 검색 결과를 텍스트로 반환."""
    try:
        from duckduckgo_search import DDGS
        with DDGS() as ddgs:
            results = list(ddgs.text(query, max_results=max_results))
        if not results:
            return "검색 결과 없음"
        parts = []
        for r in results:
            parts.append(
                f"**{r.get('title', '')}**\n{r.get('body', '')}\n출처: {r.get('href', '')}"
            )
        return "\n\n---\n\n".join(parts)
    except ImportError:
        return "웹 검색 불가 (duckduckgo-search 미설치)"
    except Exception as e:
        return f"웹 검색 실패: {e}"
