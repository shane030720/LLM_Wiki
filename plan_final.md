# plan_final.md — LLM Wiki 구현 현황 및 향후 계획

최종 업데이트: 2026-06-04

---

## 1. 구현 완료 항목

### 1-1. 인프라

- [x] FastAPI 백엔드 서버 (`backend/app/main.py`)
- [x] systemd 사용자 서비스 (`llm-wiki.service`) — 부팅 자동 시작, 크래시 복구
- [x] ChromaDB 로컬 퍼시스턴트 벡터 인덱스 (`chroma_db/`)
- [x] sentence-transformers 임베딩 (`paraphrase-multilingual-MiniLM-L12-v2`)
- [x] LiteLLM 추상화 레이어 (`llm_provider.py`) — Claude/OpenAI/Gemini/Ollama 지원
- [x] DuckDuckGo 웹 검색 fallback (API 키 불필요)
- [x] rclone 기반 클라우드 동기화 (OneDrive / Google Drive)
- [x] AgentMEMO 연동 (SQLite, `/agentmemo` 뷰어)
- [x] 새 학기 서버 초기화 스크립트 (`new-semester.sh`)

### 1-2. 에이전트

| 에이전트 | 파일 | 상태 | 비고 |
|----------|------|------|------|
| Edit Agent | `agents/edit_agent.py` | ✅ | PDF 파싱, 정리 노트, wiki auto-ingest |
| Wiki Agent (웹) | `routers/agents.py` | ✅ | 스트리밍, DuckDuckGo fallback |
| Wiki Agent (CLI) | `agents/wiki_agent.py` | ✅ | 독립 실행 |
| Quiz Agent | `agents/quiz_agent.py` | ✅ | 출제, 채점, 정답 아코디언 숨김 |
| Back Agent | `agents/back_agent.py` | ✅ | 점검, auto-ingest 트리거, AgentMEMO 기록 |

### 1-3. API 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|-----------|--------|------|
| `/` | GET | 웹 GUI 서빙 |
| `/api/health` | GET | 서버 상태 |
| `/api/subjects` | GET | 과목·파일 목록 |
| `/api/agents/edit` | POST | Edit Agent 스트리밍 |
| `/api/agents/wiki` | POST | Wiki Agent 스트리밍 |
| `/api/agents/quiz/generate` | POST | 퀴즈 문제 생성 |
| `/api/agents/quiz/grade` | POST | 퀴즈 채점 |
| `/api/query` | POST | ChromaDB RAG 검색 (SSE) |
| `/api/sync` | POST | 전체 드라이브 동기화 |
| `/api/sync/browse` | GET | Drive 폴더 탐색 |
| `/api/sync/pull` | POST | 선택 Drive 폴더 → raw/ 동기화 |
| `/api/sync/status` | GET | 마지막 동기화 결과 |
| `/api/sync/log` | GET | 동기화 로그 |
| `/agentmemo` | GET | AgentMEMO HTML 뷰어 |
| `/api/agentmemo/memos` | GET | AgentMEMO 메모 목록 (JSON) |
| `/api/agentmemo/ingest` | POST | Ingest 실행 (진행 실시간 기록) |
| `/api/agentmemo/ingest-all` | POST | 전체 미처리 파일 순서대로 처리 |
| `/api/agentmemo/backcheck` | POST | raw/ 스캔 후 미처리 파일 목록 메모 |

### 1-4. 웹 UI (wiki_gui.html)

- [x] 3패널 레이아웃 (네비게이션 / 본문 / 에이전트)
- [x] 좌측 헤더: 과목수·파일수 카운터 + **☁️ Drive** 폴더 선택 버튼
- [x] Drive 탐색 모달: OneDrive/Google Drive 폴더 탐색, 선택, 과목명 입력, 가져오기
- [x] 중앙: Edit Agent 스트리밍 렌더링
- [x] 우측 위키 탭: 스트리밍 채팅
- [x] 우측 퀴즈 탭: 문제 생성, **▶ 정답 확인** 아코디언, 채점
- [x] 타이틀바: **📋 AgentMEMO** 버튼 (새 탭으로 열림)
- [x] 다크 테마 — 4단계 색상 체계 (`#c0caf5` / `#a9b1d6` / `#8892b0` / `#7c88b0`)
- [x] API 연결 상태 표시

### 1-5. AgentMEMO 뷰어 (`/agentmemo`)

- [x] 2초마다 자동 갱신
- [x] 메모 타입별 색상 (PLAN=파랑, IMPLEMENT=초록, RESEARCH=보라, REVIEW=주황)
- [x] 상태별 표시 (OPEN/IN_PROGRESS/CLOSED)
- [x] 타입·상태 필터, 마크다운 본문 아코디언
- [x] **⬇️ Ingest 실행** — `edit_agent --ingest` 실행, stderr 실시간 메모 업데이트
- [x] **📦 모든 Ingest 실행** — 파일 하나씩 처리, N/전체 진행 표시
- [x] **🔍 점검 재실행** — raw/ 스캔 후 미처리 목록 메모

### 1-6. 데이터 현황 (2026-06-04 기준)

| 과목 | 파일 수 |
|------|---------|
| 자료구조 | 24 |
| 컴퓨터네트워크 | 11 |
| 데이터베이스 | 10 |
| 알고리즘 | 10 |
| 시스템 분석 실습 | 9 |
| 시스템 분석 이론 | 5 |
| **합계** | **69** |

---

## 2. 알려진 제한 사항

| 항목 | 내용 | 영향도 |
|------|------|--------|
| LLM API 한도 | 각 provider의 rate limit 적용 | 중 — 플랜별 확인 필요 |
| 동시 요청 | edit_agent subprocess 동시 실행 시 성능 저하 | 중 — 1인 로컬 도구라 현재 허용 |
| 역할 경계 | 시스템 프롬프트 기반 — LLM이 가끔 무시 가능 | 낮음 |
| PDF 손글씨 | pypdf는 손글씨 인식 불가 | 낮음 |
| ingest 시간 | 파일당 LLM 1회 호출 — 41개 파일이면 수십 분 소요 | 낮음 (백그라운드) |
| rclone 미설치 | Drive 연동 사용 전 rclone 설치 필요 | 낮음 (선택 기능) |

---

## 3. 향후 개선 계획

### 단기

- [ ] **ingest 병렬 처리** — 파일 여러 개를 동시에 LLM 호출 (현재 순차)
- [ ] **wiki 페이지 브라우저** — 중앙 패널에서 wiki/pages/ 직접 열람
- [ ] **퀴즈 히스토리** — 세션 내 오답 누적 및 약점 분석

### 중기

- [ ] **과목별 통계** — 파일 수, 청크 수, 마지막 업데이트 시각
- [ ] **퀴즈 점수 추적** — 과목·일자별 정답률 차트
- [ ] **다중 파일 퀴즈** — 여러 파일에 걸친 통합 퀴즈

### 장기

- [ ] **AgentMEMO MCP 서버 정식 연동** — HTTP MCP 서버(포트 8765)로 에이전트 연결
- [ ] **WebSocket** — SSE 대신 WebSocket으로 다중 에이전트 실시간 협업

---

## 4. 파일 구조 (현재 상태)

```
LLM_Wiki/
├── LLM.md                   ← wiki 페이지 스키마
├── AGENTS.md                ← 에이전트 시스템 프롬프트 (단일 진실 출처)
├── domain.md                ← 도메인 정의서
├── 의사결정문서.md            ← 아키텍처 결정 기록 (ADR)
├── plan_final.md            ← 구현 현황 및 계획 (이 파일)
├── README.md                ← 프로젝트 소개 및 실행 방법
├── PRD.md                   ← 제품 요구사항 + 의사결정 저널
├── knowledge_domain.md      ← 지식 도메인 범위
├── wiki_gui.html            ← 단일 파일 프론트엔드
├── llm_provider.py          ← LiteLLM 추상화 (run/stream/astream/web_search)
├── start.sh / stop.sh       ← 서비스 제어
├── setup.sh                 ← 최초 환경 설정
├── new-semester.sh          ← 새 학기 서버 초기화
│
├── agents/
│   ├── edit_agent.py        ← 교육자료 정리 + wiki auto-ingest
│   ├── wiki_agent.py        ← 질문 답변 (CLI 독립 실행)
│   ├── quiz_agent.py        ← 문제 출제 + 채점
│   └── back_agent.py        ← 유지보수 점검 + AgentMEMO 기록
│
├── backend/
│   └── app/
│       ├── main.py
│       ├── routers/
│       │   ├── agents.py    ← Edit/Wiki/Quiz Agent API
│       │   ├── agentmemo.py ← AgentMEMO 뷰어 + Ingest/점검 트리거
│       │   ├── subjects.py  ← 과목/파일 목록
│       │   ├── query.py     ← RAG 검색 (SSE)
│       │   └── sync.py      ← Drive 동기화 (browse/pull 포함)
│       ├── services/
│       │   ├── llm.py       ← LiteLLM RAG 스트리밍
│       │   └── retriever.py ← ChromaDB 검색
│       └── db/chroma.py
│
├── pipeline/
│   ├── refresh_pipeline.py  ← 드라이브 동기화 (onedrive|gdrive)
│   ├── onedrive.py          ← OneDrive rclone 클라이언트
│   ├── gdrive.py            ← Google Drive rclone 클라이언트
│   ├── embed.py / chunk.py / parse.py
│   └── onedrive.py
│
├── raw/                     ← 원본 강의자료 (immutable, gitignore)
├── wiki/                    ← AI 생성 wiki 페이지
│   ├── index.md / log.md
│   └── pages/ (concepts/ entities/ syntheses/)
├── chroma_db/               ← 벡터 인덱스 (gitignore)
└── data/                    ← 동기화 로그, AgentMEMO DB (gitignore)
```
