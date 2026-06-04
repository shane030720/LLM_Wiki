"""
AgentMEMO 뷰어 엔드포인트

GET /agentmemo          — 다크 테마 HTML 뷰어 (새 탭에서 열림)
GET /api/agentmemo/memos — JSON 메모 목록 (뷰어가 2초마다 폴링)
"""
from __future__ import annotations

import json
import os
import sqlite3
from pathlib import Path

from fastapi import APIRouter
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter()

ROOT = Path(__file__).resolve().parent.parent.parent.parent
_DB_PATH = Path(os.environ.get("AGENTMEMO_DB_PATH", str(ROOT / "data" / "agentmemo.db")))


def _read_memos() -> list[dict]:
    if not _DB_PATH.exists():
        return []
    try:
        conn = sqlite3.connect(str(_DB_PATH))
        conn.row_factory = sqlite3.Row
        rows = conn.execute(
            "SELECT * FROM memos ORDER BY updated_at DESC LIMIT 100"
        ).fetchall()
        conn.close()
        return [dict(r) for r in rows]
    except Exception:
        return []


@router.get("/api/agentmemo/memos")
def get_memos():
    return JSONResponse(_read_memos())


@router.get("/agentmemo", response_class=HTMLResponse)
def agentmemo_viewer():
    return HTMLResponse(_VIEWER_HTML)


_VIEWER_HTML = """<!DOCTYPE html>
<html lang="ko">
<head>
<meta charset="UTF-8">
<title>AgentMEMO</title>
<script src="https://cdn.jsdelivr.net/npm/marked@9/marked.min.js"></script>
<style>
* { margin:0; padding:0; box-sizing:border-box; }
body {
  font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', 'Noto Sans KR', sans-serif;
  background: #1a1b26; color: #c0caf5;
  min-height: 100vh; padding: 20px;
}
header {
  display: flex; align-items: center; justify-content: space-between;
  margin-bottom: 20px; padding-bottom: 12px;
  border-bottom: 1px solid #2a2b3d;
}
.title { font-size: 16px; font-weight: 700; color: #c0caf5; }
.subtitle { font-size: 12px; color: #7c88b0; margin-top: 2px; }
.status { font-size: 11px; color: #7c88b0; display: flex; align-items: center; gap: 6px; }
.pulse { width: 7px; height: 7px; border-radius: 50%; background: #9ece6a; animation: pulse 2s infinite; }
@keyframes pulse { 0%,100%{opacity:1} 50%{opacity:.4} }

.filters { display: flex; gap: 8px; margin-bottom: 16px; flex-wrap: wrap; }
.filter-btn {
  padding: 3px 10px; border-radius: 100px; border: 1px solid #2a2b3d;
  background: transparent; color: #7c88b0; font-size: 11px; cursor: pointer;
  transition: all .12s;
}
.filter-btn:hover { border-color: #4a5078; color: #a9b1d6; }
.filter-btn.active { background: #22233a; color: #c0caf5; border-color: #4a5078; }

.grid { display: flex; flex-direction: column; gap: 10px; }
.empty { text-align: center; color: #4a5078; font-size: 13px; padding: 60px 0; }

.card {
  background: #16172a; border: 1px solid #2a2b3d;
  border-radius: 8px; overflow: hidden;
  transition: border-color .12s;
}
.card:hover { border-color: #4a5078; }
.card-head {
  display: flex; align-items: center; gap: 8px;
  padding: 10px 14px; cursor: pointer; user-select: none;
}
.card-head:hover { background: #1e1f32; }
.badge-type {
  font-size: 10px; font-weight: 600; padding: 2px 7px;
  border-radius: 100px; flex-shrink: 0;
}
.type-PLAN      { background: #1e3a5f; color: #7aa2f7; }
.type-RESEARCH  { background: #2d1b5e; color: #bb9af7; }
.type-IMPLEMENT { background: #1a3a2a; color: #9ece6a; }
.type-REVIEW    { background: #3a2a1a; color: #ff9e64; }

.badge-state {
  font-size: 10px; padding: 2px 7px; border-radius: 100px; flex-shrink: 0;
}
.state-OPEN        { background: #22233a; color: #7c88b0; }
.state-IN_PROGRESS { background: #3a2e00; color: #e0af68; }
.state-CLOSED      { background: #1a3a2a; color: #9ece6a; }

.card-header { flex: 1; font-size: 13px; font-weight: 600; color: #c0caf5; }
.card-time { font-size: 10px; color: #4a5078; flex-shrink: 0; }
.card-arrow { font-size: 9px; color: #4a5078; transition: transform .15s; }
.card.open .card-arrow { transform: rotate(90deg); }

.card-body { display: none; padding: 12px 14px; border-top: 1px solid #2a2b3d; }
.card.open .card-body { display: block; }
.md-content { color: #a9b1d6; font-size: 12.5px; line-height: 1.7; }
.md-content h1,.md-content h2,.md-content h3 { color: #c0caf5; margin: 10px 0 5px; }
.md-content p { margin-bottom: 6px; }
.md-content ul,.md-content ol { padding-left: 18px; margin-bottom: 6px; }
.md-content li { margin-bottom: 2px; }
.md-content code { background: #1a1b26; color: #7dcfff; padding: 1px 5px; border-radius: 3px; font-size: 11px; }
.md-content pre { background: #1a1b26; padding: 10px; border-radius: 6px; overflow-x: auto; margin: 8px 0; }
.md-content pre code { background: none; padding: 0; }
.md-content strong { color: #c0caf5; }
.md-content blockquote { border-left: 3px solid #2a2b3d; padding-left: 10px; color: #7c88b0; }
.empty-body { color: #4a5078; font-size: 12px; font-style: italic; }
</style>
</head>
<body>
<header>
  <div>
    <div class="title">📋 AgentMEMO</div>
    <div class="subtitle">에이전트 작업 메모 뷰어</div>
  </div>
  <div class="status">
    <div class="pulse"></div>
    <span id="status-text">연결 중...</span>
  </div>
</header>

<div class="filters">
  <button class="filter-btn active" data-filter="ALL" onclick="setFilter('ALL', this)">전체</button>
  <button class="filter-btn" data-filter="OPEN"        onclick="setFilter('OPEN', this)">OPEN</button>
  <button class="filter-btn" data-filter="IN_PROGRESS" onclick="setFilter('IN_PROGRESS', this)">진행 중</button>
  <button class="filter-btn" data-filter="CLOSED"      onclick="setFilter('CLOSED', this)">완료</button>
  <button class="filter-btn" data-filter="PLAN"        onclick="setFilter('PLAN', this)">PLAN</button>
  <button class="filter-btn" data-filter="IMPLEMENT"   onclick="setFilter('IMPLEMENT', this)">IMPLEMENT</button>
  <button class="filter-btn" data-filter="RESEARCH"    onclick="setFilter('RESEARCH', this)">RESEARCH</button>
  <button class="filter-btn" data-filter="REVIEW"      onclick="setFilter('REVIEW', this)">REVIEW</button>
</div>

<div class="grid" id="grid"></div>

<script>
let memos = [], activeFilter = 'ALL', openIds = new Set();

function setFilter(f, el) {
  activeFilter = f;
  document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
  el.classList.add('active');
  render();
}

function relativeTime(iso) {
  const diff = Math.floor((Date.now() - new Date(iso)) / 1000);
  if (diff < 60) return `${diff}초 전`;
  if (diff < 3600) return `${Math.floor(diff/60)}분 전`;
  if (diff < 86400) return `${Math.floor(diff/3600)}시간 전`;
  return `${Math.floor(diff/86400)}일 전`;
}

function toggleCard(id) {
  openIds.has(id) ? openIds.delete(id) : openIds.add(id);
  render();
}

function render() {
  const grid = document.getElementById('grid');
  const filtered = memos.filter(m => {
    if (activeFilter === 'ALL') return true;
    return m.state === activeFilter || m.type === activeFilter;
  });

  if (!filtered.length) {
    grid.innerHTML = '<div class="empty">메모가 없습니다</div>';
    return;
  }

  grid.innerHTML = filtered.map(m => {
    const isOpen = openIds.has(m.id);
    const body = m.contents
      ? `<div class="md-content">${marked.parse(m.contents)}</div>`
      : `<div class="empty-body">내용 없음</div>`;
    return `
      <div class="card ${isOpen ? 'open' : ''}" id="card-${m.id}">
        <div class="card-head" onclick="toggleCard(${m.id})">
          <span class="badge-type type-${m.type}">${m.type}</span>
          <span class="badge-state state-${m.state}">${m.state}</span>
          <span class="card-header">${m.header}</span>
          <span class="card-time">${relativeTime(m.updated_at)}</span>
          <span class="card-arrow">▶</span>
        </div>
        <div class="card-body">${body}</div>
      </div>`;
  }).join('');
}

async function poll() {
  try {
    const res = await fetch('/api/agentmemo/memos');
    memos = await res.json();
    document.getElementById('status-text').textContent =
      `${memos.length}개 메모 · ${new Date().toLocaleTimeString('ko-KR')}`;
    render();
  } catch {
    document.getElementById('status-text').textContent = '연결 오류';
  }
}

poll();
setInterval(poll, 2000);
</script>
</body>
</html>
"""
