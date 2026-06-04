"""
LLM Provider 추상화

.env 의 LLM_MODEL 한 줄만 바꾸면 전환 가능.

CLI 방식 (API 키 불필요):
  claude-cli   → claude -p subprocess  (Claude Pro 구독)
  gemini-cli   → gemini -p subprocess  (Gemini CLI 무료 티어)

API 방식 (LiteLLM, API 키 필요):
  anthropic/claude-sonnet-4-6   → Claude  (ANTHROPIC_API_KEY)
  openai/gpt-4o                 → OpenAI  (OPENAI_API_KEY)
  gemini/gemini-1.5-flash       → Gemini  (GOOGLE_API_KEY, 무료 티어 있음)
  ollama/llama3                 → 로컬    (API 키 불필요)
"""
from __future__ import annotations

import codecs
import os
import shutil
import subprocess
import sys
from pathlib import Path
from typing import AsyncIterator, Iterator

import litellm
from dotenv import load_dotenv

load_dotenv(Path(__file__).resolve().parent / ".env")

LLM_MODEL   = os.environ.get("LLM_MODEL", "claude-cli")
LLM_TIMEOUT = int(os.environ.get("LLM_TIMEOUT", "300"))

litellm.set_verbose = False

# Claude CLI 경로 (nvm 등 비표준 경로 대응)
_CLAUDE_BIN = (
    shutil.which("claude")
    or os.path.expanduser("~/.nvm/versions/node/v24.14.0/bin/claude")
)
_GEMINI_BIN = shutil.which("gemini") or "gemini"
_CLI_ENV = {**os.environ, "PATH": f"{os.path.dirname(_CLAUDE_BIN or '')}:{os.environ.get('PATH', '')}"}

# CLI 모드 여부
_CLI_MODELS = {"claude-cli", "gemini-cli"}


def _is_cli() -> bool:
    return LLM_MODEL in _CLI_MODELS


# ── CLI 방식 ──────────────────────────────────────────────────────────────────

def _cli_cmd(prompt: str, system: str | None = None) -> list[str]:
    if LLM_MODEL == "claude-cli":
        cmd = [_CLAUDE_BIN, "-p", prompt]
        if system:
            cmd = [_CLAUDE_BIN, "--system-prompt", system, "-p", prompt]
        return cmd
    else:  # gemini-cli
        full = f"{system}\n\n{prompt}" if system else prompt
        return [_GEMINI_BIN, "-p", full]


def _cli_run(prompt: str, system: str | None = None) -> str:
    result = subprocess.run(
        _cli_cmd(prompt, system),
        capture_output=True, text=True,
        timeout=LLM_TIMEOUT, env=_CLI_ENV,
    )
    if result.returncode != 0:
        raise RuntimeError(result.stderr.strip() or f"CLI 오류 (exit {result.returncode})")
    return result.stdout.strip()


def _cli_stream(prompt: str, system: str | None = None) -> Iterator[str]:
    proc = subprocess.Popen(
        _cli_cmd(prompt, system),
        stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
        env=_CLI_ENV,
    )
    decoder = codecs.getincrementaldecoder("utf-8")("replace")
    while True:
        chunk = proc.stdout.read(256)
        if not chunk:
            tail = decoder.decode(b"", final=True)
            if tail:
                yield tail
            break
        text = decoder.decode(chunk)
        if text:
            yield text
    proc.wait()


async def _cli_astream(prompt: str, system: str | None = None) -> AsyncIterator[str]:
    import asyncio
    proc = await asyncio.create_subprocess_exec(
        *_cli_cmd(prompt, system),
        stdout=asyncio.subprocess.PIPE,
        stderr=asyncio.subprocess.DEVNULL,
        env=_CLI_ENV,
    )
    decoder = codecs.getincrementaldecoder("utf-8")("replace")
    while True:
        chunk = await proc.stdout.read(256)
        if not chunk:
            tail = decoder.decode(b"", final=True)
            if tail:
                yield tail
            break
        text = decoder.decode(chunk)
        if text:
            yield text
    await proc.wait()


# ── LiteLLM API 방식 ──────────────────────────────────────────────────────────

def _messages(system: str | None, prompt: str) -> list[dict]:
    msgs = []
    if system:
        msgs.append({"role": "system", "content": system})
    msgs.append({"role": "user", "content": prompt})
    return msgs


# ── 공통 인터페이스 ───────────────────────────────────────────────────────────

def run(prompt: str, system: str | None = None) -> str:
    """단발 호출, 결과 문자열 반환."""
    if _is_cli():
        return _cli_run(prompt, system)
    response = litellm.completion(
        model=LLM_MODEL,
        messages=_messages(system, prompt),
        timeout=LLM_TIMEOUT,
    )
    return response.choices[0].message.content or ""


def stream(prompt: str, system: str | None = None) -> Iterator[str]:
    """동기 스트리밍."""
    if _is_cli():
        yield from _cli_stream(prompt, system)
        return
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


async def astream(prompt: str, system: str | None = None) -> AsyncIterator[str]:
    """비동기 스트리밍 — FastAPI StreamingResponse용."""
    if _is_cli():
        async for token in _cli_astream(prompt, system):
            yield token
        return
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


# ── 웹 검색 ───────────────────────────────────────────────────────────────────

def web_search(query: str, max_results: int = 5) -> str:
    """DuckDuckGo 검색 결과를 텍스트로 반환. API 키 불필요."""
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
