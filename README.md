# LLM Wiki — 대학교 1학기 강의자료 AI 학습 도우미

전공 강의자료(PDF·PPT·MD)를 `raw/` 폴더에 넣으면 AI 에이전트가 자동으로 정리하고,
자연어 질문 답변 · 시험 문제 출제 · 채점까지 한 화면에서 처리하는 **로컬 웹 서비스**입니다.

```
raw/{과목}/파일.pdf  →  Edit Agent  →  정리 노트 + Wiki 페이지 자동 생성
                                              ↓
                              Wiki Agent (Q&A) / Quiz Agent (출제·채점)
```

---

## 주요 기능

| 기능 | 설명 |
|------|------|
| 📄 **강의자료 자동 정리** | 파일 선택 시 Edit Agent가 PDF를 읽어 마크다운 요약으로 실시간 스트리밍 |
| 🧠 **위키 에이전트 Q&A** | 강의 내용 기반 자연어 질문 답변. 웹 검색 자동 fallback |
| 📝 **퀴즈 자동 출제·채점** | 정리 노트 기반 문제 생성, 정답 숨김 아코디언, 오답 노트 |
| 🔄 **Wiki 자동 갱신** | 새 파일 추가 시 Back Agent가 감지 → wiki 페이지 자동 생성 |
| ☁️ **OneDrive 연동** | 교수 OneDrive 공유 폴더의 자료를 자동 동기화 |

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

```bash
raw/
├── 자료구조/
│   └── week01.pdf   ← PDF 파일을 여기에
├── 알고리즘/
└── 데이터베이스/
```

파일 추가 후 웹 UI 좌측에서 파일을 클릭하면 Edit Agent가 즉시 정리를 시작합니다.

---

## 사용 MCP 도구

이 프로젝트는 **Claude Code CLI** 환경에서 에이전트들이 여러 MCP(Model Context Protocol) 도구를 활용합니다.

### 1. Filesystem MCP (현재 사용 중)

| 항목 | 내용 |
|------|------|
| **역할** | 로컬 `raw/` 디렉터리의 PDF 파일을 에이전트가 직접 읽음 |
| **작동 방식** | Edit Agent가 pypdf로 PDF 텍스트를 추출 → Claude에 정리 프롬프트로 전달 |
| **설정** | Claude Code 기본 내장 (별도 설정 불필요) |

```
Edit Agent
  → pypdf.read(raw/과목/파일.pdf)
  → claude -p "[시스템프롬프트]\n\n[추출된 텍스트]"
  → 마크다운 정리 노트 출력
```

### 2. Web Search MCP (현재 사용 중)

| 항목 | 내용 |
|------|------|
| **역할** | Wiki Agent가 강의자료·wiki 페이지에서 답을 못 찾을 때 웹 검색으로 보완 |
| **작동 방식** | `claude --allowed-tools WebSearch -p [프롬프트]` 로 fallback 실행 |
| **트리거** | 현재 열람 강의노트도 없고 관련 wiki 페이지도 없을 때 자동 활성화 |

```
Wiki Agent 컨텍스트 우선순위:
  1순위: 현재 열람 중인 강의 노트 (currentNotes)
  2순위: wiki/pages/ 키워드 검색 결과
  3순위: WebSearch MCP (fallback)
```

### 3. OneDrive MCP (연동 구현 완료, 환경 변수 필요)

| 항목 | 내용 |
|------|------|
| **역할** | 교수가 OneDrive에 올린 강의자료를 자동 동기화 |
| **작동 방식** | `pipeline/refresh_pipeline.py`가 OneDrive API를 통해 변경 파일 감지 → `raw/{과목}/`에 다운로드 → ChromaDB 재임베딩 |
| **인증** | Microsoft OAuth2 (서비스 계정, `.env`에 설정 필요) |
| **API** | `POST /api/sync` — 전체 동기화 트리거 |

```bash
# .env에 추가
ONEDRIVE_CLIENT_ID=...
ONEDRIVE_CLIENT_SECRET=...
ONEDRIVE_TENANT_ID=...
```

OneDrive 설정 없이도 수동으로 `raw/` 폴더에 파일을 추가하면 동일하게 작동합니다.

### 4. AgentMEMO MCP (계획 중)

| 항목 | 내용 |
|------|------|
| **역할** | 에이전트가 작업 메모를 생성·갱신하여 학생이 실시간으로 에이전트 상태 확인 |
| **작동 방식** | Back Agent가 점검 결과를 `memo.create/update`로 AgentMEMO DB에 기록 → GUI에서 읽기 전용 뷰어로 확인 |
| **상태** | AgentMEMO MCP 서버 구현 완료 후 연동 예정 |

---

## 시스템 구조

```
웹 브라우저 (wiki_gui.html)
        │  HTTP / SSE 스트리밍
        ▼
FastAPI 서버 (localhost:8000)   ← systemd 사용자 서비스로 상시 실행
        │
        ├── Edit Agent  ──── claude CLI subprocess ──── Filesystem MCP
        ├── Wiki Agent  ──── claude CLI subprocess ──── WebSearch MCP (fallback)
        ├── Quiz Agent  ──── claude CLI subprocess
        ├── Back Agent  ──── claude CLI subprocess ──── 서버 시작 시 자동 실행
        │
        ├── ChromaDB  ────── 벡터 인덱스 (로컬 퍼시스턴트, chroma_db/)
        └── SentenceTransformers ── paraphrase-multilingual-MiniLM-L12-v2
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

### 의존성 설치

```bash
# 1. 가상환경 생성 및 활성화
python -m venv .venv
source .venv/bin/activate

# 2. Python 패키지 설치
pip install -r backend/requirements.txt

# 3. Claude Code CLI 설치 (Node.js 필요)
npm install -g @anthropic-ai/claude-code

# 4. Claude 인증
claude login
```

### 최초 설정

```bash
# setup.sh 실행 (systemd 서비스 등록 포함)
bash setup.sh
```

또는 수동으로:

```bash
# systemd 서비스 등록
systemctl --user enable llm-wiki.service
systemctl --user start llm-wiki.service
```

### OneDrive 연동 (선택)

```bash
# 프로젝트 루트에 .env 생성
cat > .env << EOF
ONEDRIVE_CLIENT_ID=your_client_id
ONEDRIVE_CLIENT_SECRET=your_client_secret
ONEDRIVE_TENANT_ID=your_tenant_id
EOF
```

---

## 사용 방법

### 강의자료 열람

1. 좌측 네비게이션에서 과목 폴더 클릭 → 파일 선택
2. Edit Agent가 PDF를 분석해 마크다운으로 실시간 변환
3. 별표(`★`) 내용은 `[중요]` 태그로 강조

### 위키 에이전트 질문

1. 우측 패널 **🧠 위키 에이전트** 탭
2. 질문 입력 → Enter 또는 전송 버튼
3. 현재 열람 파일 → wiki 페이지 → 웹 검색 순으로 컨텍스트 활용

### 퀴즈 풀기

1. 강의자료 먼저 선택 (Edit Agent로 정리 노트 로드)
2. **📝 퀴즈** 탭 → 문제 수 설정 → **문제 생성**
3. 각 문제 하단 **▶ 정답 확인** 클릭 → 정답·해설 펼침
4. 답변 입력 → **채점하기** → 오답 노트 자동 생성

> **역할 경계**: 위키 에이전트에 퀴즈를 요청하면 퀴즈 탭으로, 퀴즈 에이전트에 개념 설명을 요청하면 위키 탭으로 안내합니다.

### 서버 제어

```bash
bash start.sh    # 시작 (이미 실행 중이면 알림)
bash stop.sh     # 종료

# 로그 확인
journalctl --user -u llm-wiki.service -f

# 상태 확인
curl http://localhost:8000/api/health
```

---

## 에이전트 요약

| 에이전트 | 역할 | 트리거 | 프롬프트 위치 |
|----------|------|--------|--------------|
| **Edit Agent** | 교육자료 정리, wiki 자동 생성 | 파일 선택 / `--ingest` | `agents/edit_agent.py` |
| **Wiki Agent** | 개념·원리 Q&A | 우측 패널 채팅 | `routers/agents.py` |
| **Quiz Agent** | 문제 출제, 채점 | 퀴즈 탭 | `agents/quiz_agent.py` |
| **Back Agent** | 미처리 파일 감지, 상태 점검 | 서버 시작 시 자동 | `agents/back_agent.py` |

---

## 문서 목록

| 문서 | 내용 |
|------|------|
| [`CLAUDE.md`](CLAUDE.md) | wiki 페이지 스키마 및 형식 규칙 |
| [`AGENTS.md`](AGENTS.md) | 현재 적용 중인 에이전트 시스템 프롬프트 (단일 진실 출처) |
| [`knowledge_domain.md`](knowledge_domain.md) | 지식 도메인 범위, 과목 목록, 분류 체계 |
| [`PRD.md`](PRD.md) | 제품 요구사항 + 에이전트 의사결정 저널 |
| [`domain.md`](domain.md) | 도메인 구조, 데이터 흐름, 기술 스택 |
| [`의사결정문서.md`](의사결정문서.md) | 아키텍처 결정 이유 (ADR 형식) |
| [`plan_final.md`](plan_final.md) | 구현 현황 및 향후 계획 |
