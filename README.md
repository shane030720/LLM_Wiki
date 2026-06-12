# LLM Wiki — 강의자료 AI 학습 도우미

강의자료(PDF)를 넣으면 AI 에이전트가 wiki 페이지를 자동 생성하고,
자연어 질문 답변 · 퀴즈 출제 · 채점까지 한 화면에서 처리하는 로컬 웹 서비스입니다.

```
raw/{과목}/파일.pdf  →  Edit Agent  →  wiki/pages/ 자동 생성
                                              ↓
                              Wiki Agent (Q&A) / Quiz Agent (출제·채점)
                                              ↓
                              tools/wiki_mcp.py  ←  MCP 표준 접근
```

---

## 시작하기

```bash
git clone https://github.com/shane030720/LLM_Wiki.git
cd LLM_Wiki
python -m venv .venv && source .venv/bin/activate
pip install -r backend/requirements.txt
cp .env.example .env          # .env 열어서 LLM_MODEL 설정
bash setup.sh                 # 최초 1회
bash start.sh                 # 서버 시작 → http://localhost:8000
```

PDF는 `raw/{과목}/` 폴더에 넣으면 됩니다. 웹 UI에서 파일을 선택하면 Edit Agent가 자동으로 wiki 페이지를 생성합니다.

---

## LLM 설정

`.env` 파일의 `LLM_MODEL` 한 줄로 LLM을 전환합니다.

| 방식 | 설정값 | 비고 |
|------|--------|------|
| Claude CLI | `claude-cli` | Claude Pro 구독, API 키 불필요 |
| Gemini CLI | `gemini-cli` | 무료 티어, Gemini CLI 설치 필요 |
| Claude API | `anthropic/claude-sonnet-4-6` | `ANTHROPIC_API_KEY` 필요 |
| OpenAI | `openai/gpt-4o` | `OPENAI_API_KEY` 필요 |
| Gemini API | `gemini/gemini-1.5-flash` | `GOOGLE_API_KEY` 필요 |
| Ollama (로컬) | `ollama/llama3` | 완전 무료, Ollama 설치 필요 |

> API 키는 `.env`에만 입력하세요. `.env`는 `.gitignore`에 포함되어 있습니다.

---

## 첫 wiki 페이지 만들기

1. PDF를 `raw/` 하위 과목 폴더에 복사합니다.

```bash
mkdir -p raw/자료구조
cp ~/Downloads/week01.pdf raw/자료구조/
```

2. 브라우저에서 `http://localhost:8000` 접속 → 좌측 네비게이션에서 **자료구조 → week01.pdf** 클릭
3. Edit Agent가 PDF를 읽어 wiki 페이지를 `wiki/pages/concepts/` 아래에 자동 생성합니다.
4. 생성된 페이지는 **위키 에이전트** 탭에서 질문하거나 **퀴즈** 탭에서 문제를 생성할 수 있습니다.

또는 CLI에서 일괄 처리:

```bash
python agents/edit_agent.py --ingest
```

Claude Code를 사용한다면 `/ingest` slash command로 동일하게 실행할 수 있습니다.

---

## 시스템 구조

```
웹 브라우저 (wiki_gui.html)
        │  HTTP / SSE 스트리밍
        ▼
FastAPI 서버 (localhost:8000)
        │
        ├── Edit Agent    — raw/ PDF → wiki 페이지 생성
        ├── Wiki Agent    — 질문 답변 (강의 노트 + wiki + 웹 검색)
        ├── Quiz Agent    — 문제 출제 · 채점
        └── Back Agent    — wiki 유지보수 점검 · log.md 기록
        │
        └── tools/wiki_mcp.py  ← MCP 서버 (에이전트 표준 접근)
```

### 에이전트

| 에이전트 | 역할 | 트리거 |
|----------|------|--------|
| **Edit Agent** | PDF → wiki 페이지 자동 생성 | 파일 선택 / `--ingest` |
| **Wiki Agent** | 개념·원리 Q&A | 위키 에이전트 탭 |
| **Quiz Agent** | 문제 출제·채점·대화형 요청 | 퀴즈 탭 |
| **Back Agent** | 파일 감지·점검·log.md 기록 | 서버 시작 / Stop hook |

---

## MCP 서버 (`tools/wiki_mcp.py`)

에이전트가 `wiki/pages/`에 직접 접근하는 대신 MCP 표준 인터페이스를 경유합니다.
Claude Code에서 `mcp__llm-wiki__*` 형태로 직접 호출 가능합니다.

| Tool | 파라미터 | 설명 |
|------|----------|------|
| `search_wiki` | `query: str, top_k: int = 5` | 키워드로 wiki 페이지 검색, 점수순 반환 |
| `get_page` | `page_name: str` | slug 또는 제목으로 페이지 전체 내용 반환 |
| `add_page` | `title, content, category, slug?` | 새 페이지 생성 + index.md 자동 갱신 |
| `update_page` | `title: str, content: str` | 기존 페이지 수정 + index.md 갱신 |
| `list_pages` | `subject?: str` | 과목·카테고리별 페이지 목록 반환 |

MCP 서버 연결은 `.claude/settings.json`에 사전 설정되어 있습니다.

---

## Hook & Skill

### Hook (`.claude/settings.json`)

| Hook | 동작 |
|------|------|
| **Stop** | 세션 종료 시 Back Agent가 wiki 상태 체크 → `wiki/log.md` 자동 기록 |
| **PreToolUse** | `wiki/pages/` 직접 Edit/Write 시도 차단 → MCP 도구 사용 안내 |

### Skill (`.claude/commands/ingest.md`)

| 명령 | 동작 |
|------|------|
| `/ingest` | `raw/` 전체 미처리 PDF → Edit Agent 일괄 실행 |
| `/ingest 자료구조` | 특정 과목 폴더만 처리 |

---

## 서버 제어

```bash
bash start.sh                                        # 시작
bash stop.sh                                         # 종료
journalctl --user -u llm-wiki.service -f             # 로그
curl http://localhost:8000/api/health                # 상태 확인
python agents/edit_agent.py --ingest                 # 미처리 PDF 일괄 ingest
python agents/back_agent.py --no-ingest              # wiki 점검 (ingest 없이)
```

---

## 디렉토리 구조

```
LLM_Wiki/
├── agents/
│   ├── edit_agent.py       — Edit Agent
│   ├── quiz_agent.py       — Quiz Agent
│   └── back_agent.py       — Back Agent
├── backend/
│   └── app/
│       ├── main.py
│       └── routers/
│           └── agents.py   — Wiki Agent + API 엔드포인트
├── tools/
│   ├── wiki_mcp.py         — MCP 서버
│   └── wiki_client.py      — 에이전트용 Python 래퍼
├── raw/                    — 강의자료 원본 (gitignored)
│   └── {과목}/
├── wiki/
│   ├── index.md            — 전체 페이지 목록
│   ├── log.md              — 작업 이력
│   └── pages/
│       ├── concepts/       — 개념·이론 정의
│       ├── entities/       — 도구·알고리즘·시스템
│       └── syntheses/      — 비교·분석
├── .claude/
│   ├── settings.json       — MCP 서버 등록 + Hook 설정
│   └── commands/
│       └── ingest.md       — /ingest Skill
├── llm_provider.py         — 멀티 LLM 추상화 (LiteLLM + CLI)
├── AGENTS.md               — 에이전트 운영 플레이북
├── LLM.md                  — wiki 페이지 스키마
├── domain.md               — 지식 도메인 정의
├── .env.example            — 환경변수 템플릿
└── wiki_gui.html           — 웹 UI
```

---

## 참고 문서

| 문서 | 내용 |
|------|------|
| [`AGENTS.md`](AGENTS.md) | 에이전트 시스템 프롬프트 및 운영 규칙 |
| [`LLM.md`](LLM.md) | wiki 페이지 스키마 및 형식 규칙 |
| [`domain.md`](domain.md) | 지식 도메인 정의 (과목, 처리 방식) |
| [`의사결정문서.md`](의사결정문서.md) | 아키텍처 설계 결정 기록 |
| [`PRD.md`](PRD.md) | 제품 요구사항 및 Acceptance Criteria |
