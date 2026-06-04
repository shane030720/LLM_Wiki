# domain.md — LLM Wiki 도메인 정의서

## 1. 도메인 개요

LLM Wiki는 대학교 1학기 전공 강의자료를 자연어로 검색·학습·시험 준비할 수 있도록 설계된 **LLM 기반 개인 학습 위키**다.

핵심 가치:
- 교수의 슬라이드·강의노트를 학생이 직접 가공 없이 즉시 활용
- 단순 파일 검색이 아닌 의미 기반 질의(RAG)로 맥락 있는 답변 제공
- 시험 직전 자동 출제·채점으로 자기 진단 가능

---

## 2. 도메인 행위자

| 행위자 | 역할 | 접근 방법 |
|--------|------|-----------|
| **학생** | 질문, 자료 열람, 퀴즈 풀기 | 웹 브라우저 (localhost:8000) |
| **Edit Agent** | 교육자료를 읽고 정리 노트로 변환 | 파일 선택 시 자동 실행 |
| **Wiki Agent** | 개념 질문에 강의자료 기반 답변 | 우측 패널 채팅 |
| **Quiz Agent** | 문제 출제, 채점, 오답 노트 작성 | 우측 패널 퀴즈 탭 |
| **Back Agent** | 위키 상태 점검, 미처리 파일 ingest 트리거 | 서버 시작 시 자동 실행 |

---

## 3. 핵심 개념

### 3-1. raw/ (원본 자료)
- 교수가 제공한 PDF·PPT·MD 파일을 `raw/{과목명}/` 에 보관
- **불변(immutable)**: 절대 수정하지 않음
- 현재 등록 과목: 데이터베이스, 알고리즘, 자료구조, 컴퓨터네트워크, 시스템 분석 이론, 시스템 분석 실습

### 3-2. wiki/ (합성 지식)
- Edit Agent 또는 Back Agent가 raw/ 파일을 분석해 생성하는 마크다운 페이지
- `concepts/`, `entities/`, `syntheses/` 3가지 카테고리로 분류
- `index.md`(목차)와 `log.md`(변경 이력) 자동 유지

### 3-3. ChromaDB (벡터 인덱스)
- raw/ 파일 청크를 임베딩(`paraphrase-multilingual-MiniLM-L12-v2`)해 저장
- 질문이 들어오면 코사인 유사도로 관련 청크 Top-K 검색 (RAG)
- 현재 28개 파일 인덱싱 완료

### 3-4. 에이전트 실행 방식
- 모든 에이전트는 `claude -p <prompt>` CLI를 **subprocess**로 호출
- Claude가 직접 파일을 읽거나 코드를 실행하지 않음 — Python이 컨텍스트를 구성해 프롬프트로 전달
- systemd 사용자 서비스(`llm-wiki.service`)로 상시 실행

---

## 4. 데이터 흐름

### 4-1. 자료 등록 흐름

```
학생이 raw/{과목}/ 에 PDF 추가
        │
        ▼
Back Agent (서버 시작 시 실행)
  → ingest_status.json 대조
  → 미처리 파일 발견
  → edit_agent.py --ingest 자동 호출
        │
        ▼
Edit Agent
  → PDF 파싱 (pypdf)
  → Claude에게 정리 요청 (claude -p)
  → wiki/pages/{category}/*.md 생성
  → wiki/index.md, wiki/log.md 업데이트
  → ChromaDB에 청크 임베딩 upsert
```

### 4-2. 강의자료 열람 흐름

```
학생이 좌측 네비게이션에서 파일 클릭
        │
        ▼
POST /api/agents/edit  (스트리밍)
  → edit_agent.py 실행
  → PDF → Claude 정리 → 스트리밍 출력
        │
        ▼
중앙 패널에 마크다운 렌더링
(currentNotes 변수에 저장 → Wiki/Quiz Agent에 컨텍스트로 전달)
```

### 4-3. Wiki Agent 질문 흐름

```
학생이 질문 입력
        │
        ▼
POST /api/agents/wiki
  1. currentNotes (현재 열람 중인 강의자료) 컨텍스트 추가
  2. 키워드로 wiki/pages/ 검색 → 관련 페이지 추가
  3. 컨텍스트 없으면 WebSearch fallback
        │
        ▼
claude -p [시스템프롬프트 + 컨텍스트 + 질문]
  → 스트리밍 응답
```

### 4-4. Quiz Agent 흐름

```
학생이 [문제 생성] 클릭
        │
        ▼
POST /api/agents/quiz/generate
  → currentNotes를 임시 파일로 저장
  → quiz_agent.py generate 실행
  → 문제 + QUIZ_ANSWER/QUIZ_EXPLAIN 마커 포함 출력
        │
        ▼
프론트엔드 preProcessQuiz()
  → QUIZ_ANSWER/QUIZ_EXPLAIN 마커를 <details> 아코디언으로 변환
  → 학생이 클릭하기 전까지 정답 숨김

학생이 답변 입력 후 [채점하기]
        │
        ▼
POST /api/agents/quiz/grade
  → notes + 문제 + 학생 답변 → Claude 채점
  → 오답 노트 형식 출력
```

---

## 5. 에이전트 역할 경계

| 요청 유형 | 담당 에이전트 |
|-----------|--------------|
| 개념 설명, 원리 질문, 비교 분석 | Wiki Agent |
| 문제 출제, 채점, 오답 노트, 추가 문제 | Quiz Agent |
| 교육자료 → 정리 노트 변환, wiki 페이지 생성 | Edit Agent |
| wiki 상태 점검, 미처리 파일 감지 | Back Agent |

> **역할 경계 강제**: 각 에이전트의 시스템 프롬프트 첫 번째 섹션에 역할 외 요청 처리 방법이 명시되어 있다. Wiki Agent는 퀴즈 요청을, Quiz Agent는 개념 질문을 거절하고 상대 탭으로 안내한다.

---

## 6. 기술 스택

| 레이어 | 기술 |
|--------|------|
| **프론트엔드** | 단일 HTML 파일 (wiki_gui.html), marked.js, 바닐라 JS |
| **백엔드** | FastAPI (Python), uvicorn |
| **벡터 DB** | ChromaDB (로컬 퍼시스턴트) |
| **임베딩** | sentence-transformers `paraphrase-multilingual-MiniLM-L12-v2` |
| **LLM** | Anthropic Claude (claude CLI subprocess) |
| **PDF 파싱** | pypdf |
| **서비스 관리** | systemd 사용자 서비스 |
| **OS** | Ubuntu / WSL2 |
