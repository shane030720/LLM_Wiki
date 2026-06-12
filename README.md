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
              search_wiki / get_page / add_page / update_page / list_pages
```

### 에이전트

| 에이전트 | 역할 | 트리거 |
|----------|------|--------|
| **Edit Agent** | PDF → wiki 페이지 자동 생성 | 파일 선택 / `--ingest` |
| **Wiki Agent** | 개념·원리 Q&A | 위키 에이전트 탭 |
| **Quiz Agent** | 문제 출제·채점·대화형 요청 | 퀴즈 탭 |
| **Back Agent** | 파일 감지·점검·log.md 기록 | 서버 시작 / Stop hook |

### MCP 서버 (`tools/wiki_mcp.py`)

에이전트가 `wiki/pages/`에 직접 접근하는 대신 MCP 표준 인터페이스를 경유합니다.

| Tool | 설명 |
|------|------|
| `search_wiki(query, top_k)` | 키워드로 wiki 페이지 검색 |
| `get_page(page_name)` | 특정 페이지 전체 내용 반환 |
| `add_page(title, content, category)` | 새 페이지 생성 + index.md 갱신 |
| `update_page(title, content)` | 기존 페이지 수정 + index.md 갱신 |
| `list_pages(subject)` | 과목/카테고리별 페이지 목록 |

Claude Code에서 MCP 서버 연결은 `.claude/settings.json`에 자동 설정되어 있습니다.

### Hook

| Hook | 동작 |
|------|------|
| **Stop** | 세션 종료 시 Back Agent가 wiki 상태 체크 → `wiki/log.md` 자동 기록 |
| **PreToolUse** | `wiki/pages/` 직접 Edit/Write 시도 차단 → MCP 도구 사용 안내 |

### Skill (Slash Command)

Claude Code에서 `/ingest [과목명]` 을 입력하면 실행됩니다.

| 명령 | 동작 |
|------|------|
| `/ingest` | `raw/` 전체 미처리 PDF → Edit Agent 일괄 실행 |
| `/ingest 자료구조` | 특정 과목 폴더만 처리 |

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
│           └── agents.py   — Wiki Agent (웹) + API 엔드포인트
├── tools/
│   ├── wiki_mcp.py         — MCP 서버
│   ├── wiki_client.py      — 에이전트용 Python 래퍼
│   └── requirements.txt
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
│   └── settings.json       — MCP 서버 등록 + Hook 설정
├── AGENTS.md               — 에이전트 운영 플레이북
├── LLM.md                  — wiki 페이지 스키마
├── .env.example            — 환경변수 템플릿
├── start.sh / stop.sh
└── wiki_gui.html           — 웹 UI
```

---

## LLM 설정 전체 옵션

| 방식 | 설정값 | 비고 |
|------|--------|------|
| Claude CLI | `claude-cli` | Claude Pro 구독, API 키 불필요 |
| Gemini CLI | `gemini-cli` | 무료 티어, Gemini CLI 설치 필요 |
| Claude API | `anthropic/claude-sonnet-4-6` | `ANTHROPIC_API_KEY` 필요 |
| OpenAI | `openai/gpt-4o` | `OPENAI_API_KEY` 필요 |
| Gemini API | `gemini/gemini-1.5-flash` | `GOOGLE_API_KEY` 필요 |
| Ollama (로컬) | `ollama/llama3` | 완전 무료, Ollama 설치 필요 |

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

## 참고 문서

| 문서 | 내용 |
|------|------|
| [`AGENTS.md`](AGENTS.md) | 에이전트 시스템 프롬프트 및 운영 규칙 |
| [`LLM.md`](LLM.md) | wiki 페이지 스키마 및 형식 규칙 |
| [`domain.md`](domain.md) | 도메인 구조 및 기술 스택 |
| [`PRD.md`](PRD.md) | 제품 요구사항 및 의사결정 이력 |
