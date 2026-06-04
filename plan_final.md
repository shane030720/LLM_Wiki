# plan_final.md — LLM Wiki 구현 현황 및 향후 계획

최종 업데이트: 2026-06-04

---

## 1. 구현 완료 항목

### 1-1. 인프라

- [x] FastAPI 백엔드 서버 (`backend/app/main.py`)
- [x] systemd 사용자 서비스 (`llm-wiki.service`) — 부팅 시 자동 시작, 크래시 복구
- [x] ChromaDB 로컬 퍼시스턴트 벡터 인덱스 (`chroma_db/`)
- [x] sentence-transformers 임베딩 (`paraphrase-multilingual-MiniLM-L12-v2`)
- [x] OneDrive 동기화 파이프라인 (`pipeline/refresh_pipeline.py`)

### 1-2. 에이전트

| 에이전트 | 파일 | 상태 | 비고 |
|----------|------|------|------|
| Edit Agent | `agents/edit_agent.py` | ✅ 완료 | PDF 파싱, 정리 노트 생성, wiki auto-ingest |
| Wiki Agent (웹) | `routers/agents.py` | ✅ 완료 | 스트리밍, 강의노트+wiki 컨텍스트, 웹 검색 fallback |
| Wiki Agent (CLI) | `agents/wiki_agent.py` | ✅ 완료 | 독립 실행, wiki 키워드 검색 |
| Quiz Agent | `agents/quiz_agent.py` | ✅ 완료 | 문제 출제, 채점, 오답 노트 |
| Back Agent | `agents/back_agent.py` | ✅ 완료 | 상태 점검, 미처리 파일 auto-ingest 트리거 |

### 1-3. API 엔드포인트

| 엔드포인트 | 메서드 | 기능 |
|-----------|--------|------|
| `/` | GET | 웹 GUI 서빙 |
| `/api/health` | GET | 서버 상태 확인 |
| `/api/subjects` | GET | 과목·파일 목록 |
| `/api/agents/edit` | POST | Edit Agent 스트리밍 |
| `/api/agents/wiki` | POST | Wiki Agent 스트리밍 |
| `/api/agents/quiz/generate` | POST | 퀴즈 문제 생성 |
| `/api/agents/quiz/grade` | POST | 퀴즈 채점 |
| `/api/query` | POST | ChromaDB RAG 검색 (SSE) |
| `/api/sync` | POST | OneDrive 동기화 트리거 |
| `/api/sync/status` | GET | 동기화 상태 |

### 1-4. 웹 UI (wiki_gui.html)

- [x] 3패널 레이아웃 (네비게이션 / 본문 / 에이전트)
- [x] 좌측: 과목 폴더·파일 트리, 검색 필터
- [x] 중앙: Edit Agent 스트리밍 렌더링, 마크다운 뷰어
- [x] 우측 위키 탭: 스트리밍 채팅, 대화 초기화
- [x] 우측 퀴즈 탭: 문제 생성, 정답 아코디언 숨김, 답변 입력, 채점
- [x] 다크 테마 (Tokyo Night 계열), 가독성 색상 체계 정비
- [x] API 연결 상태 표시 (온라인/오프라인)
- [x] 오프라인 fallback 응답

### 1-5. 에이전트 역할 경계

- [x] Quiz Agent: 개념 질문 거절 → 위키 에이전트 탭 안내
- [x] Wiki Agent: 퀴즈 요청 거절 → 퀴즈 탭 안내
- [x] 프롬프트 최우선 섹션에 역할 경계 명시

### 1-6. 데이터

- [x] 6개 과목 강의자료 등록 (데이터베이스, 알고리즘, 자료구조, 컴퓨터네트워크, 시스템 분석 이론/실습)
- [x] 28개 파일 ChromaDB 인덱싱 완료
- [x] wiki/pages/ 생성 완료 (concepts/, entities/, syntheses/)

---

## 2. 알려진 제한 사항

| 항목 | 내용 | 영향도 |
|------|------|--------|
| Claude 세션 한도 | CLI 호출이 세션 사용량에 포함됨 | 중 — 장시간 사용 시 한도 도달 가능 |
| 동시 요청 | 에이전트 subprocess 동시 실행 시 성능 저하 | 중 — 1인 로컬 도구이므로 현재 허용 |
| 역할 경계 | 시스템 프롬프트 기반이라 LLM이 가끔 무시 가능 | 낮음 |
| PDF 손글씨 | pypdf는 손글씨 인식 불가, 별표 메모 포함 시 필터링 의존 | 낮음 |
| 오프라인 fallback | 내장 오프라인 응답은 하드코딩된 기본 개념만 커버 | 낮음 |
| OneDrive 인증 | .env에 ONEDRIVE_CLIENT_ID 없으면 sync API 비활성 | 낮음 (선택 기능) |

---

## 3. 향후 개선 계획

### 단기 (다음 세션)

- [ ] **퀴즈 대화형 입력**: 채점 결과에서 "다른 문제 내줘", "서술형으로 바꿔줘" 요청을 별도 입력창 없이 처리하는 UX 개선
- [ ] **퀴즈 히스토리**: 세션 내 출제된 문제·오답 기록 보존
- [ ] **Edit Agent 진행 표시**: 긴 PDF 처리 중 페이지 단위 진행률 표시
- [ ] **wiki 페이지 연결**: 중앙 패널에서 wiki 페이지도 열람 가능하도록

### 중기

- [ ] **과목별 통계**: 강의자료 파일 수, 청크 수, 마지막 업데이트 시각 표시
- [ ] **퀴즈 점수 추적**: 과목·일자별 정답률 차트
- [ ] **다중 파일 퀴즈**: 여러 파일에 걸친 통합 퀴즈 출제
- [ ] **프롬프트 캐싱**: Anthropic API 직접 호출로 전환 시 prompt cache 적용

### 장기

- [ ] **인증**: 인하대 이메일 기반 접근 제한 (현재 로컬 전용이므로 불필요)
- [ ] **모바일 UI**: 반응형 레이아웃
- [ ] **WebSocket**: SSE 대신 WebSocket으로 실시간 다중 에이전트 협업

---

## 4. 파일 구조 (현재 상태)

```
LLM_Wiki/
├── LLM.md                   ← 스키마 (wiki 페이지 형식 정의)
├── AGENTS.md                   ← 에이전트 운영 플레이북
├── domain.md                   ← 도메인 정의서 (이 문서들 중 하나)
├── 의사결정문서.md               ← 아키텍처 결정 기록
├── plan_final.md               ← 구현 현황 및 계획 (이 파일)
├── README.md                   ← 프로젝트 소개
├── wiki_gui.html               ← 단일 파일 프론트엔드
├── start.sh / stop.sh          ← systemd 서비스 시작/종료 스크립트
├── setup.sh                    ← 최초 환경 설정
│
├── agents/
│   ├── edit_agent.py           ← 교육자료 정리 + wiki auto-ingest
│   ├── wiki_agent.py           ← 질문 답변 (CLI 독립 실행용)
│   ├── quiz_agent.py           ← 문제 출제 + 채점
│   └── back_agent.py           ← 유지보수 점검
│
├── backend/
│   └── app/
│       ├── main.py             ← FastAPI 앱, lifespan에서 Back Agent 실행
│       ├── routers/
│       │   ├── agents.py       ← 에이전트 API 엔드포인트
│       │   ├── subjects.py     ← 과목/파일 목록 API
│       │   ├── query.py        ← RAG 검색 API (SSE)
│       │   └── sync.py         ← OneDrive 동기화 API
│       ├── services/
│       │   ├── llm.py          ← Claude CLI 스트리밍 래퍼
│       │   └── retriever.py    ← ChromaDB 벡터 검색
│       └── db/
│           └── chroma.py       ← ChromaDB 클라이언트
│
├── pipeline/
│   ├── refresh_pipeline.py     ← OneDrive 동기화 파이프라인
│   ├── embed.py                ← 임베딩 배치 처리
│   ├── parse.py                ← PDF/PPTX 파서
│   ├── chunk.py                ← 청킹 로직
│   └── onedrive.py             ← OneDrive API 클라이언트
│
├── raw/                        ← 원본 강의자료 (immutable)
│   ├── 데이터베이스/
│   ├── 알고리즘/
│   ├── 자료구조/
│   ├── 컴퓨터네트워크/
│   ├── 시스템 분석 이론/
│   └── 시스템 분석 실습/
│
├── wiki/
│   ├── index.md                ← 전체 wiki 페이지 목록
│   ├── log.md                  ← 변경 이력 (append-only)
│   ├── ingest_status.json      ← raw 파일 처리 상태 추적
│   └── pages/
│       ├── concepts/           ← 개념 정의 페이지
│       ├── entities/           ← 도구·모델·프레임워크 페이지
│       └── syntheses/          ← 비교·분석·종합 페이지
│
└── chroma_db/                  ← ChromaDB 인덱스 (자동 생성)
```
