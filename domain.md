# domain.md — LLM Wiki 도메인 정의서

## 1. 도메인 개요

LLM Wiki는 강의자료를 자연어로 검색·학습·시험 준비할 수 있도록 설계된 **LLM 기반 개인 학습 위키**다.

핵심 가치:
- 교수의 슬라이드·강의노트를 학생이 직접 가공 없이 즉시 활용
- 단순 파일 검색이 아닌 의미 기반 질의(RAG)로 맥락 있는 답변 제공
- 시험 직전 자동 출제·채점으로 자기 진단 가능
- 에이전트 작업 상태를 AgentMEMO로 실시간 관찰

---

## 2. 도메인 행위자

| 행위자 | 역할 | 접근 방법 |
|--------|------|-----------|
| **학생** | 질문, 자료 열람, 퀴즈 풀기, Ingest 트리거 | 웹 브라우저 (localhost:8000) |
| **Edit Agent** | 교육자료를 읽고 정리 노트·wiki 페이지 생성 | 파일 선택 시 자동 / `--ingest` |
| **Wiki Agent** | 개념 질문에 강의자료 기반 답변 | 우측 패널 채팅 |
| **Quiz Agent** | 문제 출제, 채점, 오답 노트, 대화형 요청 처리 | 우측 패널 퀴즈 탭 |
| **Back Agent** | wiki 상태 점검, 미처리 파일 감지, AgentMEMO 기록 | 서버 시작 시 자동 실행 |
| **AgentMEMO** | 에이전트 작업 메모 저장·조회 (SQLite) | /agentmemo 뷰어 |

---

## 3. 핵심 개념

### 3-1. raw/ (원본 자료)
- 강의자료 PDF·PPT·MD 파일을 `raw/{과목명}/` 에 보관
- **불변(immutable)**: 절대 수정하지 않음
- 직접 복사하거나 웹 UI의 **☁️ Drive** 버튼으로 클라우드에서 가져옴
- 현재 등록 과목 6개: 데이터베이스(10), 알고리즘(10), 자료구조(24), 컴퓨터네트워크(11), 시스템 분석 이론(5), 시스템 분석 실습(9)

### 3-2. wiki/ (합성 지식)
- Edit Agent가 raw/ 파일을 분석해 생성하는 마크다운 페이지
- `concepts/`, `entities/`, `syntheses/` 3가지 카테고리로 분류
- `index.md`(목차)와 `log.md`(변경 이력) 자동 유지

### 3-3. ChromaDB (벡터 인덱스)
- raw/ 파일 청크를 임베딩(`paraphrase-multilingual-MiniLM-L12-v2`)해 저장
- 질문이 들어오면 코사인 유사도로 관련 청크 Top-K 검색 (RAG)

### 3-4. 에이전트 실행 방식 (llm_provider.py)
- 모든 에이전트는 `llm_provider.py`의 공통 인터페이스(`run` / `stream` / `astream`)를 통해 LLM 호출
- **CLI 방식**: `claude-cli` → `claude -p` subprocess (Claude Pro 구독, API 키 불필요) ← 기본값
- **CLI 방식**: `gemini-cli` → `gemini -p` subprocess (Gemini CLI 무료 티어)
- **API 방식**: LiteLLM → Claude API / OpenAI / Gemini API / Ollama 등 (API 키 필요)
- `.env`의 `LLM_MODEL` 한 줄로 전환

### 3-5. AgentMEMO (작업 관찰)
- Back Agent가 SQLite(`data/agentmemo.db`)에 점검 결과를 메모로 기록
- `/agentmemo` 뷰어에서 2초마다 자동 갱신
- 뷰어에서 Ingest 실행·점검 재실행 버튼으로 에이전트 직접 트리거 가능

---

## 4. 데이터 흐름

### 4-1. 강의자료 등록 흐름

```
방법 A: 직접 복사
  raw/{과목}/파일.pdf 에 파일 추가

방법 B: Drive 폴더 선택 (UI)
  ☁️ Drive 버튼 → OneDrive/Google Drive 탐색
  → 폴더 선택 → 과목명 입력 → 가져오기
  → POST /api/sync/pull → raw/{과목}/ 다운로드 + ChromaDB 임베딩

방법 C: 전체 Drive 동기화
  POST /api/sync → DEFAULT_FOLDER_MAP 기준 전체 동기화
        │
        ▼
Back Agent (서버 시작 시 자동 실행)
  → ingest_status.json 대조 → 미처리 파일 감지
  → AgentMEMO에 점검 메모 기록
  → edit_agent.py --ingest 자동 호출
        │
        ▼
Edit Agent
  → PDF 파싱 (pypdf) → llm_provider로 wiki 페이지 생성
  → wiki/pages/{category}/*.md 저장
  → wiki/index.md, wiki/log.md 업데이트
  → ChromaDB 청크 임베딩 upsert
```

### 4-2. 강의자료 열람 흐름

```
파일 클릭 → POST /api/agents/edit (스트리밍)
  → edit_agent.py: pypdf 파싱 → llm_provider.stream() → stdout 스트리밍
  → 중앙 패널 마크다운 렌더링
  → currentNotes 저장 (Wiki·Quiz Agent 컨텍스트로 전달)
```

### 4-3. Wiki Agent 질문 흐름

```
질문 입력 → POST /api/agents/wiki
  1순위: currentNotes (현재 열람 강의자료)
  2순위: wiki/pages/ 키워드 검색 (최대 5페이지)
  3순위: DuckDuckGo 웹 검색 (fallback)
        │
        ▼
llm_provider.astream() → 스트리밍 응답
```

### 4-4. Quiz Agent 흐름

```
[문제 생성] 클릭 → POST /api/agents/quiz/generate
  → currentNotes → quiz_agent.py → llm_provider.run()
  → QUIZ_ANSWER/QUIZ_EXPLAIN 마커 포함 출력
  → preProcessQuiz(): 마커를 <details> 아코디언으로 변환 (정답 숨김)

[채점하기] 또는 대화형 요청 입력 → POST /api/agents/quiz/grade
  → notes + 문제 + 학생 답변(또는 요청) → llm_provider.run()
  → 오답 노트 출력 또는 새 문제 생성 (서술형/난이도 변경 등)
```

### 4-5. AgentMEMO 흐름

```
Back Agent 실행
  → memo_create("Back Agent 점검") [PLAN/IN_PROGRESS]
  → 파일 스캔 결과 memo_append
  → ingest 시작 시 memo_append [IN_PROGRESS]
  → 완료 시 memo_update [CLOSED]
        │
        ▼
/agentmemo 뷰어 (2초 자동 갱신)
  → [⬇️ Ingest 실행]: edit_agent --ingest, 진행 실시간 메모 업데이트
  → [📦 모든 Ingest 실행]: 파일 하나씩 처리, 파일별 N/전체 진행 표시
  → [🔍 점검 재실행]: raw/ 스캔 후 미처리 목록 메모로 기록
```

---

## 5. 에이전트 역할 경계

| 요청 유형 | 담당 에이전트 | 거절 시 안내 |
|-----------|--------------|-------------|
| 개념 설명, 원리 질문, 비교 분석 | Wiki Agent | "퀴즈는 📝 퀴즈 탭에서" (퀴즈 요청 시) |
| 문제 출제, 채점, 오답 노트, 서술형·난이도 변경 | Quiz Agent | "🧠 위키 에이전트 탭에서 해주세요" (개념 질문 시) |
| 교육자료 정리, wiki 페이지 생성 | Edit Agent | — |
| wiki 상태 점검, 미처리 파일 감지 | Back Agent | — |

---

## 6. 기술 스택

| 레이어 | 기술 |
|--------|------|
| **프론트엔드** | 단일 HTML (wiki_gui.html), marked.js, 바닐라 JS |
| **백엔드** | FastAPI (Python), uvicorn |
| **LLM 추상화** | llm_provider.py — CLI(claude-cli/gemini-cli) 또는 LiteLLM API |
| **벡터 DB** | ChromaDB (로컬 퍼시스턴트) |
| **임베딩** | sentence-transformers `paraphrase-multilingual-MiniLM-L12-v2` |
| **PDF 파싱** | pypdf |
| **웹 검색** | duckduckgo-search (API 키 불필요) |
| **클라우드 동기화** | rclone (OneDrive / Google Drive) |
| **에이전트 관찰** | AgentMEMO (SQLite, /agentmemo 뷰어) |
| **서비스 관리** | systemd 사용자 서비스 |
| **OS** | Ubuntu / WSL2 |

---

## 7. 학기별 운영

LLM Wiki는 **한 학기 분량**을 한 서버 인스턴스가 담당한다.

```bash
# 새 학기 서버 생성 (포트만 다르게)
bash new-semester.sh 8001   # 2학기 → ~/LLM_Wiki_8001/
bash new-semester.sh 8002   # 3학기 → ~/LLM_Wiki_8002/
```

- 코드만 복사, 강의자료·벡터DB·wiki는 제외 → 완전히 빈 상태로 시작
- API 키(.env)는 자동 재사용
- 기존 학기 서버는 그대로 유지
