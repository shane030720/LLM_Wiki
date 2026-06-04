"""
AgentMEMO 뷰어 엔드포인트

GET  /agentmemo               — 다크 테마 HTML 뷰어 (새 탭에서 열림)
GET  /api/agentmemo/memos     — JSON 메모 목록 (뷰어가 2초마다 폴링)
POST /api/agentmemo/ingest    — edit_agent --ingest 백그라운드 실행
POST /api/agentmemo/backcheck — Back Agent 점검 재실행
"""
from __future__ import annotations

import os
import sqlite3
import sys
from datetime import datetime, UTC
from pathlib import Path

from fastapi import APIRouter, BackgroundTasks
from fastapi.responses import HTMLResponse, JSONResponse

router = APIRouter()

ROOT = Path(__file__).resolve().parent.parent.parent.parent
AGENTS_DIR = ROOT / "agents"
_DB_PATH = Path(os.environ.get("AGENTMEMO_DB_PATH", str(ROOT / "data" / "agentmemo.db")))

sys.path.insert(0, str(ROOT))


# ── DB 헬퍼 ──────────────────────────────────────────────────────────────────

def _now_iso() -> str:
    return datetime.now(UTC).isoformat()

def _db():
    conn = sqlite3.connect(str(_DB_PATH))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA journal_mode=WAL")
    return conn

def _ensure_schema():
    _DB_PATH.parent.mkdir(parents=True, exist_ok=True)
    with _db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS memos (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                created_at TEXT NOT NULL, updated_at TEXT NOT NULL,
                type TEXT NOT NULL, state TEXT NOT NULL,
                header TEXT NOT NULL, contents TEXT NOT NULL DEFAULT ''
            );
        """)

def _memo_create(header: str, contents: str = "", type: str = "IMPLEMENT", state: str = "IN_PROGRESS") -> int:
    _ensure_schema()
    now = _now_iso()
    with _db() as conn:
        cur = conn.execute(
            "INSERT INTO memos (created_at,updated_at,type,state,header,contents) VALUES (?,?,?,?,?,?)",
            (now, now, type, state, header, contents)
        )
        return cur.lastrowid

def _memo_update(memo_id: int, contents: str, state: str):
    with _db() as conn:
        conn.execute(
            "UPDATE memos SET updated_at=?, contents=?, state=? WHERE id=?",
            (_now_iso(), contents, state, memo_id)
        )


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


def _ingest_with_progress(memo_id: int, files: list | None = None):
    """edit_agent.py --ingest 를 실행하며 stderr을 실시간으로 메모에 기록."""
    import subprocess
    cmd = [sys.executable, str(AGENTS_DIR / "edit_agent.py"), "--ingest"]
    if files:
        # 특정 파일만 처리 (개별 study-notes 모드 → 상태 직접 기록)
        pass  # 아래 ingest-all 전용 로직 사용

    proc = subprocess.Popen(
        cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.PIPE,
        text=True,
    )

    log_lines: list[str] = []
    for raw in proc.stderr:
        line = raw.rstrip()
        if not line:
            continue
        log_lines.append(line)
        # 5줄마다 또는 중요 키워드 포함 시 메모 업데이트
        if len(log_lines) % 5 == 0 or any(k in line for k in ("처리 중:", "완료:", "오류", "✓")):
            _memo_update(memo_id, "\n".join(log_lines[-30:]), state="IN_PROGRESS")

    proc.wait()
    ok = proc.returncode == 0
    _memo_update(
        memo_id,
        "\n".join(log_lines[-50:]) + f"\n\n{'✅ 완료' if ok else '❌ 오류 (returncode=' + str(proc.returncode) + ')'}",
        state="CLOSED" if ok else "OPEN",
    )


@router.post("/api/agentmemo/ingest")
async def trigger_ingest(background_tasks: BackgroundTasks):
    """edit_agent --ingest 를 백그라운드로 실행하고 stderr 진행 상황을 실시간으로 메모에 기록."""
    memo_id = _memo_create(
        header=f"Ingest 실행 — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        contents="**Ingest 시작** — 미처리 파일을 처리합니다...",
        type="IMPLEMENT",
        state="IN_PROGRESS",
    )
    background_tasks.add_task(_ingest_with_progress, memo_id)
    return {"memo_id": memo_id, "message": "Ingest 시작됨 — AgentMEMO에서 진행 상황을 확인하세요."}


@router.post("/api/agentmemo/ingest-all")
async def trigger_ingest_all(background_tasks: BackgroundTasks):
    """미처리 파일을 하나씩 순서대로 처리하며 파일별 진행 상황을 메모에 기록."""
    import json as _json

    # 미처리 파일 목록 수집
    raw_dir = ROOT / "raw"
    status_file = ROOT / "wiki" / "ingest_status.json"
    ext = {".pdf", ".md", ".txt", ".pptx"}
    status: dict = {}
    if status_file.exists():
        try:
            status = _json.loads(status_file.read_text())
        except Exception:
            pass

    unprocessed = []
    if raw_dir.exists():
        for f in sorted(raw_dir.rglob("*")):
            if f.is_file() and f.suffix.lower() in ext and ":Zone.Identifier" not in f.name:
                rel = str(f.relative_to(ROOT))
                if rel not in status:
                    unprocessed.append(f)

    if not unprocessed:
        return {"message": "미처리 파일이 없습니다.", "count": 0}

    memo_id = _memo_create(
        header=f"전체 Ingest — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        contents=f"**총 {len(unprocessed)}개 파일 처리 예정**\n\n" +
                 "\n".join(f"- `{f.name}`" for f in unprocessed[:10]) +
                 (f"\n- *(외 {len(unprocessed)-10}개)*" if len(unprocessed) > 10 else ""),
        type="IMPLEMENT",
        state="IN_PROGRESS",
    )

    def _run():
        import subprocess
        done, failed = 0, 0
        total = len(unprocessed)

        for i, pdf in enumerate(unprocessed, 1):
            rel = str(pdf.relative_to(ROOT))
            _memo_update(
                memo_id,
                f"**진행: {i-1}/{total}** — `{pdf.name}` 처리 중...",
                state="IN_PROGRESS",
            )

            proc = subprocess.run(
                [sys.executable, str(AGENTS_DIR / "edit_agent.py"), str(pdf)],
                capture_output=True, text=True,
                # 타임아웃 없음 — 파일당 LLM 호출 시간이 다를 수 있음
            )

            if proc.returncode == 0 and proc.stdout.strip():
                # study-notes 출력을 wiki 페이지로 저장하는 건 edit_agent가 담당
                # 여기서는 상태 파일에 done 기록
                done += 1
                try:
                    s = _json.loads(status_file.read_text()) if status_file.exists() else {}
                    s[rel] = {"status": "done", "processed_at": _now_iso()}
                    status_file.write_text(_json.dumps(s, ensure_ascii=False, indent=2))
                except Exception:
                    pass
            else:
                failed += 1

        _memo_update(
            memo_id,
            f"**완료: {done}/{total}개 처리** {'✅' if failed == 0 else f'⚠️ {failed}개 실패'}\n\n"
            f"- 성공: {done}개\n- 실패: {failed}개",
            state="CLOSED",
        )

    background_tasks.add_task(_run)
    return {"memo_id": memo_id, "message": f"{len(unprocessed)}개 파일 전체 Ingest 시작됨.", "count": len(unprocessed)}


@router.post("/api/agentmemo/backcheck")
async def trigger_backcheck(background_tasks: BackgroundTasks):
    """raw/ 파일 상태를 스캔해 메모로 기록 (LLM 호출 없음)."""
    memo_id = _memo_create(
        header=f"Back Agent 재점검 — {datetime.now().strftime('%Y-%m-%d %H:%M')}",
        contents="**점검 시작** — wiki 상태를 확인합니다...",
        type="PLAN",
        state="IN_PROGRESS",
    )

    def _run():
        import json as _json
        raw_dir = ROOT / "raw"
        status_file = ROOT / "wiki" / "ingest_status.json"

        status = {}
        if status_file.exists():
            try:
                status = _json.loads(status_file.read_text())
            except Exception:
                pass

        new_files, ext = [], {".pdf", ".md", ".txt", ".pptx"}
        if raw_dir.exists():
            for f in sorted(raw_dir.rglob("*")):
                if f.is_file() and f.suffix.lower() in ext and ":Zone.Identifier" not in f.name:
                    rel = str(f.relative_to(ROOT))
                    if rel not in status:
                        new_files.append(rel)

        lines = []
        if new_files:
            lines.append(f"**미처리 파일 {len(new_files)}개**")
            for p in new_files[:10]:
                lines.append(f"- `{p}`")
            if len(new_files) > 10:
                lines.append(f"- *(외 {len(new_files)-10}개)*")
            lines.append("\n**→ Ingest 실행 버튼으로 처리할 수 있습니다.**")
        else:
            lines.append("✅ 미처리 파일 없음 — 모든 파일이 처리되었습니다.")

        _memo_update(memo_id, "\n".join(lines), state="CLOSED")

    background_tasks.add_task(_run)
    return {"memo_id": memo_id, "message": "Back Agent 점검 시작됨."}


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

.actions { display: flex; align-items: center; gap: 8px; margin-bottom: 16px; }
.action-btn {
  padding: 6px 14px; border-radius: 6px; border: none;
  font-size: 12px; font-weight: 600; cursor: pointer; transition: all .12s;
}
.action-btn:disabled { opacity: .5; cursor: not-allowed; }
.ingest-btn      { background: #1e3a5f; color: #7aa2f7; }
.ingest-btn:hover:not(:disabled)      { background: #2a4d7f; }
.ingest-all-btn  { background: #1a3a2a; color: #9ece6a; }
.ingest-all-btn:hover:not(:disabled)  { background: #244d38; }
.check-btn       { background: #22233a; color: #a9b1d6; border: 1px solid #2a2b3d; }
.check-btn:hover:not(:disabled)       { background: #2d2e45; }
.action-msg  { font-size: 11px; color: #9ece6a; }
</style>
</head>
<body>
<header>
  <div>
    <div class="title">📋 AgentMEMO</div>
    <div class="subtitle">에이전트 작업 메모 뷰어</div>
  </div>
  <div style="display:flex;align-items:center;gap:8px">
    <div class="status">
      <div class="pulse"></div>
      <span id="status-text">연결 중...</span>
    </div>
  </div>
</header>

<div class="actions">
  <button class="action-btn ingest-btn" onclick="runAction('ingest')" id="btn-ingest">
    ⬇️ Ingest 실행
  </button>
  <button class="action-btn ingest-all-btn" onclick="runAction('ingest-all')" id="btn-ingest-all">
    📦 모든 Ingest 실행
  </button>
  <button class="action-btn check-btn" onclick="runAction('backcheck')" id="btn-backcheck">
    🔍 점검 재실행
  </button>
  <span id="action-msg" class="action-msg"></span>
</div>

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

async function runAction(type) {
  const btnId = type === 'ingest' ? 'btn-ingest'
              : type === 'ingest-all' ? 'btn-ingest-all'
              : 'btn-backcheck';
  const btn = document.getElementById(btnId);
  const msg = document.getElementById('action-msg');
  btn.disabled = true;
  msg.textContent = '';

  try {
    const res = await fetch(`/api/agentmemo/${type}`, { method: 'POST' });
    const data = await res.json();
    msg.textContent = data.message || '실행 시작됨';
    setTimeout(() => { msg.textContent = ''; }, 5000);
  } catch {
    msg.style.color = '#f7768e';
    msg.textContent = '실행 실패';
  }

  setTimeout(() => { btn.disabled = false; }, 3000);
}
</script>
</body>
</html>
"""
