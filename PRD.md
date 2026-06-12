# PRD — LLM Wiki 제품 요구사항

---

## Goal

강의자료(PDF)를 `raw/` 폴더에 넣으면 AI 에이전트가 자동으로 wiki 페이지를 생성하고,
자연어 질문 답변 · 퀴즈 출제 · 채점까지 한 화면에서 처리하는 로컬 웹 서비스를 만든다.

사용자는 강의자료를 직접 정리하거나 검색할 필요 없이, 대화형 인터페이스로 학습할 수 있어야 한다.

---

## Constraints

| 제약 | 이유 |
|------|------|
| 로컬 실행 (서버 외부 의존 없음) | 개인 학습 자료를 외부 서비스에 올리지 않음 |
| API 키 없이도 동작 가능 | Claude Pro 구독자는 `claude-cli`, Gemini 사용자는 `gemini-cli`로 무료 사용 |
| 단일 HTML 파일 프론트엔드 | 별도 빌드 없이 브라우저에서 바로 열림 |
| 강의자료 원본 내용만 wiki에 포함 | 에이전트가 임의 내용 추가 시 학습 신뢰성 저하 |
| 손글씨 처리 없음 | OCR 의존성 최소화, 한국어 손글씨 인식 품질 불안정 |

---

## 구현된 기능

### 핵심 파이프라인

- `raw/{과목}/파일.pdf` 배치 → Edit Agent → `wiki/pages/` 마크다운 자동 생성
- ingest_status.json으로 처리 이력 추적, 중복 재처리 방지
- MCP 서버(`tools/wiki_mcp.py`)를 통한 표준화된 wiki 접근 인터페이스

### 에이전트

| 에이전트 | 구현 파일 | 기능 |
|----------|-----------|------|
| Edit Agent | `agents/edit_agent.py` | PDF 정리 노트 생성 / `--ingest` 자동 wiki 변환 |
| Wiki Agent | `backend/app/routers/agents.py` | 강의 노트 + wiki + 웹검색 기반 Q&A |
| Quiz Agent | `agents/quiz_agent.py` | 객관식 출제 / 채점 / 오답 노트 |
| Back Agent | `agents/back_agent.py` | 미처리 파일 감지 / wiki 점검 / log.md 기록 |

### MCP 서버 (`tools/wiki_mcp.py`)

| Tool | 기능 |
|------|------|
| `search_wiki(query, top_k)` | 키워드로 wiki 페이지 검색 |
| `get_page(page_name)` | 특정 페이지 전체 내용 반환 |
| `add_page(title, content, category)` | 새 페이지 생성 + index.md 갱신 |
| `update_page(title, content)` | 기존 페이지 수정 + index.md 갱신 |
| `list_pages(subject)` | 과목/카테고리별 페이지 목록 |

### 하네스 (Claude Code 연동)

| 구성요소 | 파일 | 기능 |
|----------|------|------|
| MCP 서버 등록 | `.claude/settings.json` | Claude Code에서 wiki 도구 직접 사용 |
| Stop Hook | `.claude/settings.json` | 세션 종료 시 back_agent `--log-check` 자동 실행 |
| PreToolUse Hook | `.claude/settings.json` | wiki/pages/ 직접 수정 시도 차단 → MCP 사용 안내 |
| `/ingest` SKILL | `.claude/commands/ingest.md` | 미처리 PDF 일괄 처리 slash command |

### 멀티 LLM 지원 (`llm_provider.py`)

| 방식 | 설정값 |
|------|--------|
| Claude CLI (API 키 불필요) | `LLM_MODEL=claude-cli` |
| Gemini CLI (API 키 불필요) | `LLM_MODEL=gemini-cli` |
| Claude API | `LLM_MODEL=anthropic/claude-sonnet-4-6` |
| OpenAI | `LLM_MODEL=openai/gpt-4o` |
| Gemini API | `LLM_MODEL=gemini/gemini-1.5-flash` |
| Ollama (로컬) | `LLM_MODEL=ollama/llama3` |

### 기타

- 퀴즈 정답 숨김: `QUIZ_ANSWER:` / `QUIZ_EXPLAIN:` 마커를 `<details>` 아코디언으로 변환
- AgentMEMO: Back Agent 점검 결과를 SQLite DB에 기록하는 메모 시스템
- Back Agent 자동 ingest 트리거: 미처리 파일 발견 시 Edit Agent subprocess 실행
- 새 학기 서버: `bash new-semester.sh [포트]`로 독립 인스턴스 생성

---

## TODO

- [ ] 이미지 전용 PDF OCR 처리 (한국어 손글씨 포함)
- [ ] wiki 페이지 간 관계 그래프 시각화
- [ ] 퀴즈 결과 이력 저장 및 오답 패턴 분석
- [ ] Google Drive 자동 동기화 (현재는 수동 트리거)
- [ ] 다중 사용자 지원 (현재는 단일 로컬 사용자 기준)

---

## Acceptance Criteria

| 기준 | 검증 방법 |
|------|-----------|
| PDF 1개를 `raw/` 에 넣으면 wiki 페이지가 자동 생성된다 | `raw/자료구조/test.pdf` 배치 후 `wiki/pages/` 확인 |
| Wiki Agent가 강의 내용 질문에 출처를 포함해 답변한다 | 웹 UI에서 개념 질문 후 `**출처**` 섹션 확인 |
| Quiz Agent가 wiki 내용 기반으로 객관식 문제를 출제한다 | 퀴즈 탭에서 문제 생성 후 `QUIZ_ANSWER` 마커 확인 |
| 채점 시 오답 노트와 참고 페이지가 제공된다 | 틀린 답 제출 후 오답 노트 항목 확인 |
| 세션 종료 시 `wiki/log.md`에 자동으로 상태가 기록된다 | Claude Code 세션 종료 후 log.md 마지막 항목 확인 |
| `wiki/pages/` 직접 Edit 시도가 차단된다 | Claude Code에서 wiki 파일 직접 수정 시도 → 훅 경고 확인 |
| API 키 없이 `claude-cli` 모드로 동작한다 | `.env`에 `LLM_MODEL=claude-cli` 설정 후 ingest 실행 |
| `/ingest` slash command로 미처리 PDF 일괄 처리된다 | Claude Code에서 `/ingest` 실행 후 페이지 생성 확인 |
