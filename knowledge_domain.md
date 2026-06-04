# knowledge_domain.md — LLM Wiki 지식 도메인 정의서

이 문서는 LLM Wiki가 다루는 지식 도메인의 범위, 출처, 분류 기준을 정의한다.

---

## 1. 대상 도메인

**대학교 1학기 전공 교과목**

LLM Wiki는 특정 분야의 모든 지식을 다루는 범용 위키가 아니다.
사용자가 `raw/` 폴더에 넣은 1학기 분량 강의자료를 1차 출처로 하며,
해당 강의에서 다루는 개념·알고리즘·시스템·도구를 지식 범위로 한정한다.

### 범위 내 (In-scope)

- 강의 슬라이드(PDF)에 명시된 개념, 정의, 알고리즘, 예제
- 교수가 별표(★)로 강조한 시험 출제 범위
- 강의자료에서 참조하는 표준 교재 내용 (강의자료를 통해 간접 인용)

### 범위 외 (Out-of-scope)

- 강의자료에 없는 외부 지식 (웹 검색 fallback은 허용하되, wiki 페이지 생성 대상 아님)
- 손글씨 필기, 수업 중 구두 발언
- "시험 안나옴" 표시된 내용
- 다른 학교/학과 강의 자료

---

## 2. 등록 과목 및 교재

| 과목명 | 영문명 | 현재 파일 수 | 주요 키워드 |
|--------|--------|-------------|------------|
| **자료구조** | Data Structures | 21개 | ADT, List, Stack, Queue, Tree, Heap, Graph, Hash |
| **알고리즘** | Algorithms | 10개 | 정렬, 그래프 탐색, DP, 탐욕, 문자열 매칭, NP-완전 |
| **데이터베이스** | Database | 9개 | ER 모델, 관계 대수, SQL, 정규화, 쿼리 처리, 인덱스 |
| **컴퓨터네트워크** | Computer Networks | 1개+ | TCP/IP, HTTP, 라우팅, DNS, 소켓 |
| **시스템 분석 이론** | Systems Analysis Theory | 다수 | SDLC, DFD, ERD, 요구공학, UML, 유스케이스 |
| **시스템 분석 실습** | Agentic Coding Practice | 9개 | Vibe Coding, Agentic Coding, MCP, Claude Code, Hook, Skill |

> 시스템 분석 실습은 LLM·AI 에이전트 개발을 실습 주제로 다루는 과목으로, wiki 자체의 도메인과 메타적으로 겹친다.

---

## 3. 지식 분류 체계

CLAUDE.md 스키마에 따라 wiki 페이지는 3가지 카테고리로 분류한다.

### concepts/ — 개념 정의

무언가가 **무엇인지(WHAT)**를 다룬다. 하나의 개념·기술·원리에 대한 정밀한 정의.

```
abstract-data-type.md   — ADT란 무엇인가
tcp-three-way-handshake.md — 3-way handshake 과정
dynamic-programming.md  — DP의 원리와 적용 조건
```

필수 섹션: `Definition` / `How It Works` / `Key Properties` / `Relationships` / `Open Questions` / `Sources`

### entities/ — 구체적 존재

실제로 **존재하는 것(WHO/WHAT EXISTS)**을 다룬다. 특정 알고리즘, 도구, 시스템, 구현체.

```
dijkstras-algorithm.md  — Dijkstra 알고리즘 구체 구현
postgresql.md           — PostgreSQL DBMS
claude-code.md          — Claude Code CLI 도구
```

필수 섹션: `Overview` / `Capabilities` / `Limitations` / `Relationships` / `Sources`

### syntheses/ — 교차 분석

여러 개념·엔티티를 **비교하거나 종합(SYNTHESIS)**한다. 단일 개념으로 분류할 수 없는 관계 분석.

```
sorting-algorithm-comparison.md   — 정렬 알고리즘 성능 비교
join-algorithm-comparison.md      — Hash Join vs Merge Join
vibe-vs-agentic-coding.md         — Vibe Coding과 Agentic Coding 차이
```

필수 섹션: `Thesis` / `Evidence` / `Counterevidence` / `Conclusion` / `Sources`

---

## 4. 현재 지식 현황 (2026-06-04 기준)

| 분류 | 페이지 수 | 주요 과목 |
|------|-----------|----------|
| concepts/ | ~220개 | 전 과목 |
| entities/ | ~45개 | 자료구조, 알고리즘, 네트워크, AI 도구 |
| syntheses/ | ~11개 | 알고리즘 비교, DB 설계, 코딩 패러다임 |
| **합계** | **~275개** | |

### 미처리 파일 (ingest 대기)

| 과목 | 파일 수 | 상태 |
|------|---------|------|
| 자료구조 | 21개 | Back Agent가 감지, edit_agent --ingest 실행 예정 |
| 알고리즘 | 10개 | 동일 |
| 데이터베이스 | 9개 | 동일 |
| 컴퓨터네트워크 | 1개+ | 동일 |

---

## 5. 지식 표현 원칙

### 언어 정책

- **본문**: 한국어로 작성 (학생이 한국어로 공부하기 때문)
- **전문 용어**: 영어 원문 유지 (번역 시 의미 손실 발생)
- 예: "연결 지향 프로토콜 TCP" → OK / "티씨피" → NG

### 출처 추적성

모든 페이지는 frontmatter `sources:` 필드에 원본 PDF 경로를 명시한다.
출처 없는 지식은 wiki 페이지로 생성하지 않는다.

### 모순 표기

두 출처가 상충할 경우 반드시 표기한다:

```markdown
> ⚠️ **Contradiction:** [출처 A]는 X라 하지만 [출처 B]는 Y라 한다.
```

### 지식 공백 마커

아직 wiki 페이지가 없는 개념은 `[[slug]]` 링크로 남긴다.
이는 오류가 아니라 향후 ingest 대상을 표시하는 공백 마커다.

---

## 6. 도메인 확장 기준

새로운 과목/분야를 추가할 때 다음 기준을 따른다:

1. `raw/{새과목명}/` 폴더 생성 후 PDF 추가
2. Back Agent가 다음 실행 시 자동 감지
3. Edit Agent가 wiki 페이지 자동 생성
4. `wiki/index.md`에 자동 등록

별도의 스키마 변경 없이 폴더 구조만으로 도메인 확장 가능.
