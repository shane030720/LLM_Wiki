# LLM Wiki — 강의자료 AI 학습 도우미

강의자료(PDF·PPT·MD)를 넣으면 AI 에이전트가 자동으로 정리하고,
자연어 질문 답변 · 시험 문제 출제 · 채점까지 한 화면에서 처리하는 **로컬 웹 서비스**입니다.

```
raw/{과목}/파일.pdf  →  Edit Agent  →  정리 노트 + Wiki 페이지 자동 생성
                                              ↓
                              Wiki Agent (Q&A) / Quiz Agent (출제·채점)
```

> **강의자료 관리 방식**
> 교수가 배포한 강의자료를 직접 다운로드해 **자신의 OneDrive 또는 Google Drive**에 보관하고,
> LLM Wiki가 그 드라이브에서 로컬로 동기화합니다.
> 드라이브 연동 없이 `raw/` 폴더에 직접 파일을 넣어도 동일하게 작동합니다.

---

## 주요 기능

| 기능 | 설명 |
|------|------|
| 📄 **강의자료 자동 정리** | 파일 선택 시 Edit Agent가 PDF를 읽어 마크다운 요약으로 실시간 스트리밍 |
| 🧠 **위키 에이전트 Q&A** | 강의 내용 기반 자연어 질문 답변. DuckDuckGo 웹 검색 자동 fallback |
| 📝 **퀴즈 자동 출제·채점** | 정리 노트 기반 문제 생성, 정답 숨김 아코디언(클릭 시 공개), 오답 노트 |
| 🔄 **Wiki 자동 갱신** | 새 파일 추가 시 Back Agent가 감지 → wiki 페이지 자동 생성 |
| ☁️ **Drive 폴더 선택 동기화** | UI에서 OneDrive·Google Drive 탐색 → 원하는 폴더만 `raw/`에 가져오기 |
| 🤖 **멀티 LLM 지원** | `.env` 한 줄로 Claude / OpenAI / Gemini / Ollama 전환 |
| 📋 **AgentMEMO 연동** | 에이전트 작업 상태 실시간 관찰, 뷰어에서 Ingest 직접 실행 |

---

## 빠른 시작

```bash
# 서버 시작 (systemd 서비스)
bash start.sh

# 브라우저에서 열기
http://localhost:8000
```

서버가 이미 실행 중이면 `start.sh`가 자동 감지합니다.

### 강의자료 추가

**방법 1: 직접 복사**
```
raw/
├── 자료구조/
│   └── week01.pdf   ← 여기에 복사
└── 알고리즘/
```

**방법 2: Drive에서 가져오기 (UI)**
1. 웹 UI 좌측 헤더의 **☁️ Drive** 버튼 클릭
2. OneDrive 또는 Google Drive 선택
3. 강의자료 폴더 탐색 → 선택
4. 과목명 입력 → **가져오기** 클릭

파일 추가 후 좌측 네비게이션에서 파일을 클릭하면 Edit Agent가 정리를 시작합니다.

---

## LLM 설정

`.env` 파일의 `LLM_MODEL` 한 줄만 바꾸면 원하는 LLM으로 전환됩니다.

```bash
# .env

# Claude (Anthropic)
LLM_MODEL=anthropic/claude-sonnet-4-6
ANTHROPIC_API_KEY=sk-ant-...

# OpenAI
LLM_MODEL=openai/gpt-4o
OPENAI_API_KEY=sk-...

# Gemini (무료 티어 있음)
LLM_MODEL=gemini/gemini-1.5-flash
GOOGLE_API_KEY=...

# 로컬 Ollama (API 키 불필요, 완전 무료)
LLM_MODEL=ollama/llama3
```

---

## 사용 도구

### 1. Filesystem (현재 사용 중)

| 항목 | 내용 |
|------|------|
| **역할** | 로컬 `raw/` PDF 파일을 에이전트가 읽음 |
| **작동 방식** | pypdf로 텍스트 추출 → LiteLLM으로 정리 프롬프트 전달 |

```
Edit Agent → pypdf.read(raw/과목/파일.pdf)
           → llm_provider.stream(prompt, system=EDIT_SYSTEM_PROMPT)
           → 마크다운 정리 노트 스트리밍
```

### 2. DuckDuckGo 웹 검색 (현재 사용 중)

| 항목 | 내용 |
|------|------|
| **역할** | 강의자료·wiki 페이지에서 답을 못 찾을 때 보완 |
| **특징** | API 키 불필요, 모든 LLM에서 동일하게 동작 |

```
Wiki Agent 컨텍스트 우선순위:
  1순위: 현재 열람 중인 강의 노트
  2순위: wiki/pages/ 키워드 검색
  3순위: DuckDuckGo 웹 검색 (fallback)
```

### 3. 클라우드 드라이브 동기화 (rclone 기반, 선택)

내 OneDrive / Google Drive에 보관한 강의자료를 `raw/`로 자동 동기화합니다.

```
내 Drive/강의자료/자료구조/week01.pdf
        ↓  rclone (변경분만)
  raw/자료구조/week01.pdf
        ↓
  ChromaDB 재임베딩
```

#### OneDrive 설정

```bash
curl https://rclone.org/install.sh | sudo bash
python pipeline/onedrive.py --auth   # 브라우저 Microsoft 로그인
python pipeline/onedrive.py --whoami # 연결 확인
python pipeline/refresh_pipeline.py --provider onedrive
```

#### Google Drive 설정

```bash
curl https://rclone.org/install.sh | sudo bash
python pipeline/gdrive.py --auth     # 브라우저 Google 로그인
python pipeline/gdrive.py --whoami   # 연결 확인
python pipeline/refresh_pipeline.py --provider gdrive
```

#### UI에서 특정 폴더만 선택

웹 UI의 **☁️ Drive** 버튼 → 폴더 탐색 → 선택 → 가져오기

#### API로 동기화 트리거

```bash
curl -X POST http://localhost:8000/api/sync \
  -H "Content-Type: application/json" \
  -d '{"provider": "gdrive"}'

# 특정 폴더만
curl -X POST http://localhost:8000/api/sync/pull \
  -H "Content-Type: application/json" \
  -d '{"provider": "gdrive", "drive_folder": "/강의자료/자료구조", "subject": "자료구조"}'
```

### 4. AgentMEMO (현재 사용 중)

Back Agent가 점검·ingest 작업을 수행하면서 SQLite에 메모를 기록합니다.
`/agentmemo` 뷰어에서 실시간으로 확인하고 직접 실행할 수 있습니다.

```
Back Agent 점검 → SQLite 메모 기록
                       ↓
          /agentmemo 뷰어 (2초 자동 갱신)
          [⬇️ Ingest 실행] [📦 모든 Ingest 실행] [🔍 점검 재실행]
```

| 버튼 | 동작 |
|------|------|
| ⬇️ Ingest 실행 | `edit_agent --ingest` 실행, stderr 실시간 메모 업데이트 |
| 📦 모든 Ingest 실행 | 미처리 파일 하나씩 처리, N/전체 진행 표시 |
| 🔍 점검 재실행 | raw/ 스캔 후 미처리 파일 목록을 메모로 기록 |

LLM Wiki 타이틀바의 **📋 AgentMEMO** 버튼으로 새 탭에서 바로 열 수 있습니다.

---

## 시스템 구조

```
웹 브라우저 (wiki_gui.html)
        │  HTTP / SSE 스트리밍
        ▼
FastAPI 서버 (localhost:8000)   ← systemd 사용자 서비스
        │
        ├── Edit Agent  ──── LiteLLM (llm_provider)
        ├── Wiki Agent  ──── LiteLLM + DuckDuckGo (fallback)
        ├── Quiz Agent  ──── LiteLLM
        ├── Back Agent  ──── LiteLLM + AgentMEMO SQLite
        │
        ├── /agentmemo  ──── AgentMEMO 뷰어 (SQLite 직접 읽기)
        ├── ChromaDB    ──── 벡터 인덱스 (로컬 퍼시스턴트)
        └── SentenceTransformers ── paraphrase-multilingual-MiniLM-L12-v2

               ↕  LiteLLM
  Claude / OpenAI / Gemini / Ollama / 그 외 100+ 모델

클라우드 드라이브 (선택)
  내 OneDrive / Google Drive  →  rclone  →  raw/{과목}/  →  ChromaDB
```

---

## 요구 환경 및 설치

### 시스템 요구사항

| 항목 | 최소 사양 |
|------|----------|
| OS | Ubuntu 22.04 / WSL2 |
| Python | 3.10 이상 |
| 저장 공간 | 2GB 이상 (ChromaDB + 모델) |
| RAM | 4GB 이상 권장 |

### 설치

```bash
# 1. 가상환경 생성 및 패키지 설치
python -m venv .venv
source .venv/bin/activate
pip install -r backend/requirements.txt

# 2. .env 설정
cp .env.example .env
# → LLM_MODEL, ANTHROPIC_API_KEY (또는 다른 LLM API 키) 입력

# 3. 서비스 등록 및 시작
bash setup.sh
```

---

## 사용 방법

### 강의자료 열람

1. 좌측 네비게이션에서 과목 폴더 → 파일 선택
2. Edit Agent가 PDF를 마크다운으로 실시간 변환
3. 별표(`★`) 내용은 `[중요]` 태그로 강조

### 위키 에이전트 질문

1. 우측 **🧠 위키 에이전트** 탭
2. 질문 입력 → Enter
3. 현재 열람 파일 → wiki 페이지 → 웹 검색 순으로 컨텍스트 활용

> 퀴즈 요청 시 "📝 퀴즈 탭에서 이용해 주세요" 안내

### 퀴즈 풀기

1. 강의자료 선택 후 **📝 퀴즈** 탭
2. 문제 수 설정 → **문제 생성**
3. **▶ 정답 확인** 클릭 → 정답·해설 펼침
4. 답변 입력 → **채점하기** → 오답 노트

> 개념 설명 요청 시 "🧠 위키 에이전트 탭에서 해주세요" 안내

### 서버 제어

```bash
bash start.sh   # 시작
bash stop.sh    # 종료

journalctl --user -u llm-wiki.service -f   # 로그
curl http://localhost:8000/api/health       # 상태
```

### 새 학기 서버

```bash
bash new-semester.sh 8001
# → ~/LLM_Wiki_8001/ 생성, http://localhost:8001 에서 실행
# → 코드만 복사 (강의자료·DB 제외, 빈 상태로 시작), API 키 자동 재사용
# → 기존 서버(8000)는 그대로 유지
```

---

## 에이전트 요약

| 에이전트 | 역할 | 트리거 |
|----------|------|--------|
| **Edit Agent** | 교육자료 정리, wiki 생성 | 파일 선택 / `--ingest` |
| **Wiki Agent** | 개념·원리 Q&A | 우측 채팅 |
| **Quiz Agent** | 문제 출제, 채점 | 퀴즈 탭 |
| **Back Agent** | 파일 감지, 점검, AgentMEMO 기록 | 서버 시작 시 자동 |

---

## 문서 목록

| 문서 | 내용 |
|------|------|
| [`LLM.md`](LLM.md) | wiki 페이지 스키마 및 형식 규칙 |
| [`AGENTS.md`](AGENTS.md) | 현재 적용 중인 에이전트 시스템 프롬프트 |
| [`knowledge_domain.md`](knowledge_domain.md) | 지식 도메인 범위 및 분류 체계 |
| [`PRD.md`](PRD.md) | 제품 요구사항 + 의사결정 저널 |
| [`domain.md`](domain.md) | 도메인 구조, 데이터 흐름, 기술 스택 |
| [`의사결정문서.md`](의사결정문서.md) | 아키텍처 결정 이유 (ADR) |
| [`plan_final.md`](plan_final.md) | 구현 현황 및 향후 계획 |
