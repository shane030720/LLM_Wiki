# Wiki Operation Log

Append-only chronological record of all wiki operations.

> **LLM instruction:** Never edit past entries. Append new entries at the **bottom** of this file. Each entry header must follow the format `## [YYYY-MM-DD] <operation> | <short description>`.

Valid operations: `ingest` | `query` | `lint` | `schema-update` | `recovery`

---

## [2026-05-26] schema-update | Initial wiki scaffold created

- **Changed:** Repository initialized with CLAUDE.md, AGENTS.md, wiki/index.md, wiki/log.md, and wiki/pages/ directory structure
- **Reason:** First-time setup of LLM Wiki following Karpathy's pattern
- **Pages migrated:** none — wiki is empty; raw/ contains 9 PDF sources pending ingest

---

## [2026-05-26] ingest | Initial ingest of all 9 PDF sources (Agentic Coding Basics)

- **Source(s):**
  - raw/1. Vibe coding and Agent coding.pdf
  - raw/2. SDLC pipeline in Vibe coding.pdf
  - raw/3. Agents subprocess calling.pdf
  - raw/4. Plan_mode Sequential and Parallel agents.pdf
  - raw/5. Agent Specifications.pdf
  - raw/6. Agent pool and Orchestrator.pdf
  - raw/7. Harness and Skills.pdf
  - raw/8. Model Context Protocol.pdf
  - raw/9. Loop and Hooks.pdf
- **Pages created:**
  - Concepts (18): [[vibe-coding]], [[agentic-coding]], [[sdlc]], [[spec-driven-development]], [[subprocess]], [[plan-mode]], [[handoff]], [[sequential-agent]], [[parallel-agent]], [[system-prompt]], [[agent-pool]], [[harness-engineering]], [[contract-driven-iteration]], [[skill]], [[agentic-coding-patterns]], [[mcp]], [[hook]], [[loop]]
  - Entities (3): [[claude-code]], [[codex-cli]], [[gemini-cli]]
  - Syntheses (2): [[vibe-vs-agentic-coding]], [[pipeline-design-patterns]]
- **Pages updated:** wiki/index.md (전체 카탈로그 초기 작성)
- **Contradictions flagged:** none
- **Notes:** CSE3308 Practical Session 01~12 강의 자료 기반. 모든 개념 페이지는 한국어로 작성. 미해결 링크([[open-questions-*]] 등)는 향후 ingest 대상 마커로 유지.

파일 시스템에 직접 접근은 제한되어 있지만, 제공된 점검 데이터만으로 충분히 보고서를 작성할 수 있습니다. 데이터를 분석하겠습니다.

**분석 결과:**
- raw/ 실제 PDF: 9종 (Zone.Identifier 제외)
- Zone.Identifier 파일: 9개 (Windows 다운로드 메타데이터, raw/에 혼재)
- wiki 페이지 미생성 raw 파일: 5건 (한국어 과목 파일들)
- 날짜 계산: 데이터베이스·알고리즘·자료구조 (88~90일 경과), 시스템분석·컴퓨터네트워크 (1일 경과)

---

## [2026-06-01] back-check | 유지보수 점검

- **raw/ 신규 파일 (wiki 미생성):** 5건
  - `데이터베이스` (수정: 2026-03-03, **90일 미처리**)
  - `알고리즘` (수정: 2026-03-05, **88일 미처리**)
  - `자료구조` (수정: 2026-03-05, **88일 미처리**)
  - `시스템분석` (수정: 2026-05-31, 1일 경과)
  - `컴퓨터네트워크` (수정: 2026-05-31, 1일 경과)

- **오래된 wiki 페이지:** 이상 없음

- **깨진 링크:** 이상 없음

- **비정상 파일 (raw/ 혼재):** Zone.Identifier 파일 9건 검출
  - Windows 다운로드 보안 메타데이터 파일로, raw/ 디렉토리 내 PDF 원본과 동명으로 쌍으로 존재
  - 해당 파일들은 CLAUDE.md 스키마 상 처리 대상 원본 문서가 아님
  - 예시: `1. Vibe coding and Agent coding.pdf:Zone.Identifier`, 외 8건

- **종합:** 업데이트 필요 항목 **6건**
  1. `데이터베이스`, `알고리즘`, `자료구조` — 88~90일 경과, Ingest 우선 처리 권장
  2. `시스템분석`, `컴퓨터네트워크` — 신규 추가 (1일), Ingest 대기
  3. Zone.Identifier 파일 9건 — 담당자 확인 후 raw/ 에서 정리 권장 (삭제 또는 별도 보관)

## [2026-06-01] ingest | ER model.pdf, Indexing.pdf, Intermediate SQL.pdf...

- **Source(s):**
  - raw/데이터베이스/ER model.pdf
  - raw/데이터베이스/Indexing.pdf
  - raw/데이터베이스/Intermediate SQL.pdf
  - raw/데이터베이스/Query Processing.pdf
  - raw/데이터베이스/Relational DB Design (1).pdf
  - raw/데이터베이스/Relational Model 2.pdf
  - raw/데이터베이스/SQL Basics.pdf
  - raw/데이터베이스/Storage and File Structure (1).pdf
  - raw/시스템분석/ch01-1.pdf
  - raw/시스템분석/ch02-1.pdf
  - raw/시스템분석/ch04-2.pdf
  - raw/시스템분석/ch05-1.pdf
- **Pages created:** [[entity-relationship-model]], [[er-attributes]], [[mapping-cardinality]], [[weak-entity-set]], [[er-to-relational-schema]], [[database-index]], [[ordered-index]], [[b-plus-tree]], [[b-tree]], [[sql-join-expressions]], [[sql-views]], [[sql-transactions]], [[sql-integrity-constraints]], [[sql-data-types-and-schemas]], [[query-processing]], [[external-merge-sort]], [[hash-join]], [[join-algorithm-comparison]], [[functional-dependency]], [[database-normalization]], [[bcnf]], [[third-normal-form]], [[relational-model]], [[relational-algebra]], [[sql]], [[sql-ddl]], [[sql-select-query]], [[sql-aggregate-functions]], [[sql-subqueries]], [[sql-null-values]], [[sql-dml]], [[storage-hierarchy]], [[external-memory-model]], [[record-structure]], [[file-organization]], [[buffer-manager]], [[postgresql-storage]], [[systems-analyst]], [[systems-development-life-cycle]], [[business-process-management]], [[feasibility-analysis]], [[project-selection]], [[sdlc-methodology-selection]], [[structured-systems-development]], [[rapid-application-development]], [[agile-development-methodology]], [[project-estimation-and-planning]], [[use-case]], [[use-case-formats]], [[process-model]], [[data-flow-diagram]], [[dfd-elements]]
- **Pages updated:** 없음
- **Contradictions flagged:** 없음
- **Notes:** edit_agent.py --ingest 자동 처리

## [2026-06-02] ingest | CH02 자료의 추상화와 기본 자료 구조.pdf, CH04 정렬.pdf, CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf...

- **Source(s):**
  - raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf
  - raw/알고리즘/CH04 정렬.pdf
  - raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf
  - raw/알고리즘/CH13 NP-완전 문제.pdf
  - raw/자료구조/(참고자료) Week13_Graphs (1).pdf
  - raw/자료구조/CSE2112_02_week01_2.pdf
  - raw/자료구조/CSE2112_02_week02_1.pdf
  - raw/자료구조/CSE2112_02_week03_1.pdf
  - raw/자료구조/CSE2112_02_week03_2.pdf
  - raw/자료구조/CSE2112_02_week04_1.pdf
  - raw/자료구조/CSE2112_02_week04_2.pdf
  - raw/자료구조/CSE2112_02_week05_1.pdf
  - raw/자료구조/CSE2112_02_week05_2.pdf
  - raw/자료구조/CSE2112_02_week06_1.pdf
  - raw/자료구조/CSE2112_02_week06_2.pdf
  - raw/자료구조/CSE2112_02_week07_1.pdf
  - raw/자료구조/CSE2112_02_week07_2.pdf
  - raw/자료구조/CSE2112_02_week09_1.pdf
  - raw/자료구조/CSE2112_02_week09_2.pdf
  - raw/자료구조/CSE2112_02_week10_1.pdf
  - raw/자료구조/CSE2112_02_week10_2.pdf
  - raw/자료구조/CSE2112_02_week11_1.pdf
  - raw/자료구조/CSE2112_02_week11_2.pdf
  - raw/자료구조/CSE2112_02_week12_1.pdf
  - raw/자료구조/CSE2112_02_week12_2.pdf
  - raw/자료구조/CSE2112_02_week13_1 (1).pdf
  - raw/자료구조/CSE2112_02_week13_2.pdf
  - raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf
- **Pages created:** [[abstract-data-type]], [[tree-data-structure]], [[binary-tree]], [[stack]], [[queue]], [[priority-queue]], [[union-find]], [[dictionary-adt]], [[divide-and-conquer]], [[insertion-sort]], [[quick-sort]], [[mergesort]], [[heapsort]], [[radix-sort]], [[sorting-algorithm-comparison]], [[greedy-algorithm]], [[minimum-spanning-tree]], [[prims-algorithm]], [[kruskals-algorithm]], [[dijkstras-algorithm]], [[class-p]], [[class-np]], [[np-completeness]], [[np-complete-problems]], [[graph]], [[adjacency-matrix]], [[algorithm-analysis]], [[big-oh-notation]], [[pseudocode]], [[big-oh-notation]], [[asymptotic-bounds]], [[time-complexity-classes]], [[stack]], [[singly-linked-list]], [[abstract-data-type]], [[stack]], [[array-based-stack]], [[linked-list-based-stack]], [[stack-implementation-comparison]], [[queue]], [[stack]], [[queue]], [[deque]], [[vector-array-list]], [[queue]], [[vector-adt]], [[list-adt]], [[sequence-adt]], [[vector-vs-list]], [[array-based-vector]], [[list-adt]], [[iterator]], [[sequence-adt]], [[vector-vs-list]], [[tree-data-structure]], [[iterator]], [[vector-vs-list]], [[tree-data-structure]], [[tree-traversal]], [[tree-cpp-implementation]], [[tree-data-structure]], [[binary-tree]], [[tree-traversal]], [[binary-tree]], [[binary-tree-traversal]], [[binary-tree-implementation]], [[priority-queue]], [[pq-sort]], [[priority-queue]], [[pq-sort]], [[selection-sort]], [[insertion-sort]], [[priority-queue]], [[heap]], [[heap-sort]], [[heap]], [[heap-sort]], [[bottom-up-heap-construction]], [[map-adt]], [[binary-search-tree]], [[avl-tree]], [[map-adt]], [[binary-search-tree]], [[avl-tree]], [[hash-table]], [[map-implementation-comparison]], [[hash-table]], [[hash-function]], [[collision-handling]], [[dictionary-adt]], [[hash-collision-handling]], [[dictionary-adt]], [[binary-search]], [[graph]], [[graph-representations]], [[graph]], [[graph-representations]], [[depth-first-search]], [[breadth-first-search]], [[graph-representation]], [[depth-first-search]], [[breadth-first-search]], [[directed-acyclic-graph]], [[topological-sorting]], [[computer-network]], [[internet]], [[network-protocol]], [[internet-standards]]
- **Pages updated:** 없음
- **Contradictions flagged:** 없음
- **Notes:** edit_agent.py --ingest 자동 처리

## [2026-06-02] ingest | CSE2112_02_week05_2_updated.pdf, CSE2112_02_week09_1.pdf, CSE2112_02_week11_1.pdf

- **Source(s):**
  - raw/자료구조/CSE2112_02_week05_2_updated.pdf
  - raw/자료구조/CSE2112_02_week09_1.pdf
  - raw/자료구조/CSE2112_02_week11_1.pdf
- **Pages created:** [[doubly-linked-list]], [[entry-adt]], [[trinode-restructuring]]
- **Pages updated:** 없음
- **Contradictions flagged:** 없음
- **Notes:** edit_agent.py --ingest 자동 처리

AGENTS.md 파일 읽기 권한이 필요합니다. 우선 시스템 프롬프트의 보고서 출력 형식과 CLAUDE.md의 `wiki/log.md` 형식을 기반으로 유지보수 보고서를 작성하겠습니다.

---

## [2026-06-03] back-check | 유지보수 점검

- **점검 일자:** 2026-06-03
- **현재 wiki 페이지 수:** 186개

---

### raw/ 신규 파일 (ingest 대기)

총 **62개** 파일이 처리 대기 중입니다.

| 분류 | 파일 | 수량 |
|------|------|------|
| LLM / Agent | `raw/1. Vibe coding and Agent coding.pdf` ~ `raw/9. Loop and Hooks.pdf` | 9개 |
| 데이터베이스 | `raw/데이터베이스/ER model.pdf` 외 8개 | 9개 |
| 시스템분석 | `raw/시스템분석/ch01-1.pdf` 외 4개 | 5개 |
| 알고리즘 | `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf` 외 10개 | 11개 |
| 자료구조 | `raw/자료구조/CSE2112_02_week01_2.pdf` 외 21개 | 22개 |
| 컴퓨터네트워크 | `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf` 외 10개 | 11개 |

<details>
<summary>전체 목록 펼치기</summary>

**LLM / Agent (9개)**
- `raw/1. Vibe coding and Agent coding.pdf`
- `raw/2. SDLC pipeline in Vibe coding.pdf`
- `raw/3. Agents subprocess calling.pdf`
- `raw/4. Plan_mode Sequential and Parallel agents.pdf`
- `raw/5. Agent Specifications.pdf`
- `raw/6. Agent pool and Orchestrator.pdf`
- `raw/7. Harness and Skills.pdf`
- `raw/8. Model Context Protocol.pdf`
- `raw/9. Loop and Hooks.pdf`

**데이터베이스 (9개)**
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

**시스템분석 (5개)**
- `raw/시스템분석/ch01-1.pdf`
- `raw/시스템분석/ch02-1.pdf`
- `raw/시스템분석/ch04-2.pdf`
- `raw/시스템분석/ch05-1.pdf`
- `raw/시스템분석/ch06-1.pdf`

**알고리즘 (11개)**
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`

**자료구조 (22개)**
- `raw/자료구조/CSE2112_02_week01_2.pdf` ~ `raw/자료구조/CSE2112_02_week13_2.pdf` (주차별 강의자료)

**컴퓨터네트워크 (11개)**
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf` ~ `raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf`
- `raw/컴퓨터네트워크/hjroh_Network Programming Labs - Easy Version_20260326.pdf`

</details>

---

### re-ingest 필요 (raw 갱신)

- 없음

---

### 깨진 링크

총 **16건**의 참조 오류가 감지되었습니다. 해당 페이지들은 아직 생성되지 않은 슬러그를 참조하고 있습니다.

| 출처 페이지 | 깨진 참조 슬러그 | 비고 |
|-------------|-----------------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 자료구조 — 인접 리스트 페이지 미생성 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 알고리즘 — 다익스트라 페이지 미생성 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 자료구조 — 연결 리스트 페이지 미생성 |
| `binary-tree-implementation.md` | `[[array]]` | 자료구조 — 배열 페이지 미생성 |
| `binary-tree-traversal.md` | `[[tree]]` | 자료구조 — 트리 페이지 미생성 |
| `binary-tree.md` | `[[tree]]` | 자료구조 — 트리 페이지 미생성 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | DB — 튜플 관계 해석 페이지 미생성 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | DB — 도메인 관계 해석 페이지 미생성 |
| `relational-model.md` | `[[normalization-theory]]` | DB — 정규화 이론 페이지 미생성 |
| `stack.md` | `[[linked-list]]` | 자료구조 — 연결 리스트 페이지 미생성 |
| `use-case-formats.md` | `[[functional-requirements]]` | 시스템분석 — 기능 요구사항 페이지 미생성 |
| `use-case-formats.md` | `[[test-case]]` | 시스템분석 — 테스트 케이스 페이지 미생성 |
| `use-case.md` | `[[functional-requirements]]` | 시스템분석 — 기능 요구사항 페이지 미생성 |
| `use-case.md` | `[[event-response-list]]` | 시스템분석 — 이벤트-응답 목록 페이지 미생성 |
| `use-case.md` | `[[data-model]]` | 시스템분석 — 데이터 모델 페이지 미생성 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 알고리즘 — 다익스트라 페이지 미생성 |

> **참고:** `[[dijkstra-algorithm]]`은 2개 페이지에서, `[[linked-list]]`는 2개 페이지에서, `[[functional-requirements]]`는 2개 페이지에서 각각 중복 참조되고 있으므로, 해당 페이지 생성 시 우선순위를 높이는 것을 권장합니다.

---

### wiki 페이지 업데이트 필요

- 이상 없음

---

### 종합

| 항목 | 상태 |
|------|------|
| raw/ 신규 파일 | **62개** ingest 대기 |
| re-ingest 필요 | 이상 없음 |
| 깨진 링크 | **16건** (고유 슬러그 기준 **11개** 미생성 페이지) |
| wiki 페이지 업데이트 | 이상 없음 |

> **업데이트 필요 항목: 2종 78건**
> 1. **Ingest 작업** — 62개 raw 파일을 wiki 페이지로 변환 필요
> 2. **깨진 링크 해소** — 신규 ingest 후 자동 해소될 가능성이 높은 슬러그(`[[linked-list]]`, `[[tree]]`, `[[dijkstra-algorithm]]`, `[[array]]` 등) 포함. ingest 완료 후 재점검 권장

AGENTS.md와 log.md를 읽으려 했으나 권한이 없어 접근하지 못했습니다. 제공해주신 점검 데이터와 CLAUDE.md의 log.md 형식 규칙을 기반으로 보고서를 작성하겠습니다.

---

## [2026-06-03] back-check | 유지보수 점검

- **점검 일자:** 2026-06-03
- **전체 wiki 페이지 수:** 186개

---

### raw/ 신규 파일 (ingest 대기)

총 **62개** 파일이 ingest 처리를 기다리고 있습니다.

| 분류 | 파일 수 | 파일 목록 |
|------|---------|---------|
| LLM / Agent | 9 | `1. Vibe coding and Agent coding.pdf`, `2. SDLC pipeline in Vibe coding.pdf`, `3. Agents subprocess calling.pdf`, `4. Plan_mode Sequential and Parallel agents.pdf`, `5. Agent Specifications.pdf`, `6. Agent pool and Orchestrator.pdf`, `7. Harness and Skills.pdf`, `8. Model Context Protocol.pdf`, `9. Loop and Hooks.pdf` |
| 데이터베이스 | 9 | `ER model.pdf`, `Indexing.pdf`, `Intermediate SQL.pdf`, `Intro to databases.pdf`, `Query Processing.pdf`, `Relational DB Design (1).pdf`, `Relational Model 2.pdf`, `SQL Basics.pdf`, `Storage and File Structure (1).pdf` |
| 시스템분석 | 5 | `ch01-1.pdf`, `ch02-1.pdf`, `ch04-2.pdf`, `ch05-1.pdf`, `ch06-1.pdf` |
| 알고리즘 | 11 | `CH01~CH13` 시리즈 11개 |
| 자료구조 | 22 | `CSE2112_02_week01_2.pdf` ~ `week13_2.pdf` 외 참고자료 포함 22개 |
| 컴퓨터네트워크 | 12 | `Week 01~11` 시리즈 및 `Network Programming Labs.pdf` 포함 12개 |

> ⚠️ **조치 필요:** 62개 파일 전체에 대해 Ingest 작업을 수행해야 합니다. 신규 도메인(데이터베이스, 시스템분석, 알고리즘, 자료구조, 컴퓨터네트워크) 다수 포함으로 관련 wiki 페이지 신규 생성이 대규모로 수반될 예정입니다.

---

### re-ingest 필요 (raw 갱신)

- **이상 없음**

---

### 깨진 링크

총 **16건**의 참조 오류가 확인되었습니다.

| 원본 페이지 | 깨진 링크 | 비고 |
|------------|---------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 페이지 미생성 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[array]]` | 페이지 미생성 |
| `binary-tree-traversal.md` | `[[tree]]` | 페이지 미생성 |
| `binary-tree.md` | `[[tree]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | 페이지 미생성 |
| `relational-model.md` | `[[normalization-theory]]` | 페이지 미생성 |
| `stack.md` | `[[linked-list]]` | 페이지 미생성 (중복) |
| `use-case-formats.md` | `[[functional-requirements]]` | 페이지 미생성 |
| `use-case-formats.md` | `[[test-case]]` | 페이지 미생성 |
| `use-case.md` | `[[functional-requirements]]` | 페이지 미생성 (중복) |
| `use-case.md` | `[[event-response-list]]` | 페이지 미생성 |
| `use-case.md` | `[[data-model]]` | 페이지 미생성 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 (중복) |

> **참고:** `[[linked-list]]`, `[[functional-requirements]]`, `[[dijkstra-algorithm]]`은 복수의 페이지에서 중복 참조됩니다. Ingest 우선순위 고려를 권장합니다.

---

### wiki 페이지 업데이트 필요

- **이상 없음**

---

### 종합

| 항목 | 상태 |
|------|------|
| raw/ 신규 파일 | ⚠️ **62개** ingest 대기 |
| re-ingest 필요 | ✅ 이상 없음 |
| 깨진 링크 | ⚠️ **16건** 참조 오류 |
| wiki 페이지 업데이트 | ✅ 이상 없음 |

**업데이트 필요 항목: 총 78건 (ingest 대기 62건 + 깨진 링크 16건)**

> 💡 **권장 작업 순서:**
> 1. 자료구조·알고리즘 도메인 Ingest 먼저 수행 → `[[linked-list]]`, `[[tree]]`, `[[array]]`, `[[dijkstra-algorithm]]` 등 깨진 링크 다수 해소 가능
> 2. 데이터베이스 도메인 Ingest → `[[normalization-theory]]`, `[[tuple-relational-calculus]]`, `[[domain-relational-calculus]]` 해소 가능
> 3. 시스템분석 도메인 Ingest → `[[functional-requirements]]`, `[[test-case]]`, `[[event-response-list]]`, `[[data-model]]` 해소 가능
> 4. LLM/Agent 도메인 Ingest → 기존 wiki 보강
> 5. 컴퓨터네트워크 도메인 Ingest

AGENTS.md 파일 읽기 권한이 필요합니다. 권한을 허용해 주시면 파일 형식을 확인 후 보고서를 작성할 수 있습니다.

그 전에, 제공된 점검 데이터를 바탕으로 CLAUDE.md의 `wiki/log.md` 형식 규칙에 따라 보고서를 작성하겠습니다:

---

## [2026-06-03] back-check | 유지보수 점검

- **점검일:** 2026-06-03
- **wiki 총 페이지 수:** 186개

---

### raw/ 신규 파일 (ingest 대기)

총 **62개** 파일이 ingest되지 않은 상태입니다.

| 분류 | 파일 수 | 파일 목록 |
|------|---------|-----------|
| LLM/Agent 관련 | 9 | `1. Vibe coding and Agent coding.pdf`, `2. SDLC pipeline in Vibe coding.pdf`, `3. Agents subprocess calling.pdf`, `4. Plan_mode Sequential and Parallel agents.pdf`, `5. Agent Specifications.pdf`, `6. Agent pool and Orchestrator.pdf`, `7. Harness and Skills.pdf`, `8. Model Context Protocol.pdf`, `9. Loop and Hooks.pdf` |
| 데이터베이스 | 9 | `ER model.pdf`, `Indexing.pdf`, `Intermediate SQL.pdf`, `Intro to databases.pdf`, `Query Processing.pdf`, `Relational DB Design (1).pdf`, `Relational Model 2.pdf`, `SQL Basics.pdf`, `Storage and File Structure (1).pdf` |
| 시스템분석 | 5 | `ch01-1.pdf`, `ch02-1.pdf`, `ch04-2.pdf`, `ch05-1.pdf`, `ch06-1.pdf` |
| 알고리즘 | 11 | `CH01~CH13` 시리즈 11개 |
| 자료구조 | 21 | `CSE2112_02` 시리즈 및 참고자료 21개 |
| 컴퓨터네트워크 | 12 | `Week 01~11` 시리즈 및 네트워크 프로그래밍 실습 자료 12개 |

---

### re-ingest 필요 (raw 갱신)

- **없음**

---

### 깨진 링크

총 **16건**의 미해결 참조 오류가 발견되었습니다.

| 출처 페이지 | 깨진 링크 | 비고 |
|-------------|-----------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 페이지 미생성 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[array]]` | 페이지 미생성 |
| `binary-tree-traversal.md` | `[[tree]]` | 페이지 미생성 |
| `binary-tree.md` | `[[tree]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | 페이지 미생성 |
| `relational-model.md` | `[[normalization-theory]]` | 페이지 미생성 |
| `stack.md` | `[[linked-list]]` | 페이지 미생성 |
| `use-case-formats.md` | `[[functional-requirements]]` | 페이지 미생성 |
| `use-case-formats.md` | `[[test-case]]` | 페이지 미생성 |
| `use-case.md` | `[[functional-requirements]]` | 페이지 미생성 |
| `use-case.md` | `[[event-response-list]]` | 페이지 미생성 |
| `use-case.md` | `[[data-model]]` | 페이지 미생성 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 |

> 💡 `[[linked-list]]`는 2개 페이지에서, `[[functional-requirements]]`·`[[dijkstra-algorithm]]`은 각각 2개 페이지에서 반복 참조됨 — 해당 페이지 생성 시 다수 링크가 동시에 복구됨.

---

### wiki 페이지 업데이트 필요

- **이상 없음**

---

### 종합

| 항목 | 상태 |
|------|------|
| raw/ 신규 파일 | ⚠️ **62개** ingest 대기 |
| re-ingest 필요 | ✅ 이상 없음 |
| 깨진 링크 | ⚠️ **16건** (미생성 페이지 참조) |
| wiki 페이지 업데이트 | ✅ 이상 없음 |

**업데이트 필요 항목 총 78건** (ingest 62건 + 깨진 링크 16건)

#### 권장 처리 순서
1. **우선순위 1 — 깨진 링크 복구용 핵심 페이지 생성** (8개 slug): `[[linked-list]]`, `[[tree]]`, `[[array]]`, `[[dijkstra-algorithm]]`, `[[functional-requirements]]`, `[[normalization-theory]]`, `[[tuple-relational-calculus]]`·`[[domain-relational-calculus]]`, `[[event-response-list]]`·`[[data-model]]`·`[[test-case]]`
2. **우선순위 2 — LLM/Agent 관련 9개 raw 파일 ingest** (기존 wiki 주제와 직결)
3. **우선순위 3 — 학과 과목 자료 대량 ingest** (데이터베이스·알고리즘·자료구조·컴퓨터네트워크·시스템분석, 53개)

AGENTS.md 파일에 직접 접근할 수 없어 CLAUDE.md의 로그 형식과 시스템에 정의된 보고 형식을 기반으로 보고서를 작성합니다.

---

## [2026-06-03] back-check | 유지보수 점검

### 기본 현황
- **점검 일자:** 2026-06-03
- **전체 wiki 페이지 수:** 248개

---

### raw/ 신규 파일 (ingest 대기)

총 **56개** 파일이 ingest 대기 중입니다.

#### 에이전트 / LLM 관련 (9개)
- `raw/1. Vibe coding and Agent coding.pdf`
- `raw/2. SDLC pipeline in Vibe coding.pdf`
- `raw/3. Agents subprocess calling.pdf`
- `raw/4. Plan_mode Sequential and Parallel agents.pdf`
- `raw/5. Agent Specifications.pdf`
- `raw/6. Agent pool and Orchestrator.pdf`
- `raw/7. Harness and Skills.pdf`
- `raw/8. Model Context Protocol.pdf`
- `raw/9. Loop and Hooks.pdf`

#### 데이터베이스 (9개)
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

#### 시스템분석 (5개)
- `raw/시스템분석/ch01-1.pdf`
- `raw/시스템분석/ch02-1.pdf`
- `raw/시스템분석/ch04-2.pdf`
- `raw/시스템분석/ch05-1.pdf`
- `raw/시스템분석/ch06-1.pdf`

#### 알고리즘 (11개)
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`

#### 자료구조 (20개)
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`
- `raw/자료구조/CSE2112_02_week01_2.pdf`
- `raw/자료구조/CSE2112_02_week02_1.pdf`
- `raw/자료구조/CSE2112_02_week03_1.pdf`
- `raw/자료구조/CSE2112_02_week03_2.pdf`
- `raw/자료구조/CSE2112_02_week04_1.pdf`
- `raw/자료구조/CSE2112_02_week04_2.pdf`
- `raw/자료구조/CSE2112_02_week05_1.pdf`
- `raw/자료구조/CSE2112_02_week05_2.pdf`
- `raw/자료구조/CSE2112_02_week06_1.pdf`
- `raw/자료구조/CSE2112_02_week06_2.pdf`
- `raw/자료구조/CSE2112_02_week07_1.pdf`
- `raw/자료구조/CSE2112_02_week07_2.pdf`
- `raw/자료구조/CSE2112_02_week09_2.pdf`
- `raw/자료구조/CSE2112_02_week10_1.pdf`
- `raw/자료구조/CSE2112_02_week10_2.pdf`
- `raw/자료구조/CSE2112_02_week11_2.pdf`
- `raw/자료구조/CSE2112_02_week12_1.pdf`
- `raw/자료구조/CSE2112_02_week12_2.pdf`
- `raw/자료구조/CSE2112_02_week13_1 (1).pdf`
- `raw/자료구조/CSE2112_02_week13_2.pdf`

#### 컴퓨터네트워크 (1개)
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf`

---

### re-ingest 필요 (raw 갱신)

이상 없음

---

### 오래된 wiki 페이지

이상 없음

---

### 깨진 링크 (총 20건, 15개 파일)

| 파일 | 참조 오류 슬러그 | 비고 |
|------|----------------|------|
| `adjacency-matrix.md` | [[adjacency-list]] | 자료구조 — 미작성 페이지 |
| `all-pairs-shortest-paths.md` | [[dijkstra-algorithm]] | 알고리즘 — 미작성 페이지 |
| `binary-tree-implementation.md` | [[linked-list]] | 자료구조 — 미작성 페이지 |
| `binary-tree-implementation.md` | [[array]] | 자료구조 — 미작성 페이지 |
| `binary-tree-traversal.md` | [[tree]] | 자료구조 — 미작성 페이지 |
| `binary-tree.md` | [[tree]] | 자료구조 — 미작성 페이지 |
| `relational-algebra.md` | [[tuple-relational-calculus]] | DB — 미작성 페이지 |
| `relational-algebra.md` | [[domain-relational-calculus]] | DB — 미작성 페이지 |
| `relational-model.md` | [[normalization-theory]] | DB — 미작성 페이지 |
| `stack.md` | [[linked-list]] | 자료구조 — 미작성 페이지 |
| `tcp-header.md` | [[udp]] | 네트워크 — 미작성 페이지 |
| `tcp-three-way-handshake.md` | [[tcp-options]] | 네트워크 — 미작성 페이지 |
| `transport-layer-demultiplexing.md` | [[udp]] | 네트워크 — 미작성 페이지 |
| `use-case-formats.md` | [[functional-requirements]] | 시스템분석 — 미작성 페이지 |
| `use-case-formats.md` | [[test-case]] | 시스템분석 — 미작성 페이지 |
| `use-case.md` | [[functional-requirements]] | 시스템분석 — 미작성 페이지 |
| `use-case.md` | [[event-response-list]] | 시스템분석 — 미작성 페이지 |
| `use-case.md` | [[data-model]] | 시스템분석 — 미작성 페이지 |
| `floyd-warshall-algorithm.md` | [[dijkstra-algorithm]] | 알고리즘 — 미작성 페이지 |
| `tcp.md` | [[udp]] | 네트워크 — 미작성 페이지 |

> ℹ️ 미작성 페이지 참조는 CLAUDE.md 규약상 허용되는 **지식 공백 마커**입니다. 단, ingest 이후 해당 페이지가 생성되면 자동 해소 여부를 재점검해야 합니다.

---

### 종합

- **raw/ 신규 파일:** 56건 (ingest 대기)
- **re-ingest 필요:** 없음
- **오래된 wiki 페이지:** 없음
- **깨진 링크:** 20건 (15개 파일, 전부 미작성 페이지 참조)
- **wiki 페이지 업데이트 필요:** 없음

> **업데이트 필요 항목 총 76건** — ingest 우선 실행 권장. 특히 자료구조·알고리즘·데이터베이스 도메인 raw가 대거 유입되어 있어, ingest 완료 시 깨진 링크 20건 중 상당수(추정 12~15건)가 자동 해소될 가능성이 높습니다.

---

**권장 액션 순서:**
1. **Ingest** — 56개 raw 파일을 도메인별로 순차 처리 (자료구조 20건 → 알고리즘 11건 → 데이터베이스 9건 → 에이전트/LLM 9건 → 시스템분석 5건 → 컴퓨터네트워크 1건)
2. **링크 재점검** — ingest 완료 후 깨진 링크 20건 재검사
3. **잔여 링크 처리** — ingest 후에도 해소되지 않은 슬러그는 stub 페이지 생성 또는 참조 수정

AGENTS.md 파일 읽기 권한이 필요합니다. 권한을 허용해 주시면 정확한 형식에 맞춰 작성하겠습니다. 그 사이, 제공된 점검 데이터와 CLAUDE.md의 로그 형식을 기반으로 보고서를 작성합니다.

---

## [2026-06-03] back-check | 유지보수 점검

- **점검 일시:** 2026-06-03
- **Wiki 총 페이지 수:** 248개

---

### 📥 raw/ 신규 파일 (ingest 대기)

총 **55개** 파일이 ingest되지 않은 상태입니다.

| 분류 | 파일 수 | 파일 목록 |
|------|---------|-----------|
| 데이터베이스 | 9 | `ER model.pdf`, `Indexing.pdf`, `Intermediate SQL.pdf`, `Intro to databases.pdf`, `Query Processing.pdf`, `Relational DB Design (1).pdf`, `Relational Model 2.pdf`, `SQL Basics.pdf`, `Storage and File Structure (1).pdf` |
| 시스템 분석 실습 | 9 | `1. Vibe coding and Agent coding.pdf`, `2. SDLC pipeline in Vibe coding.pdf`, `3. Agents subprocess calling.pdf`, `4. Plan_mode Sequential and Parallel agents.pdf`, `5. Agent Specifications.pdf`, `6. Agent pool and Orchestrator.pdf`, `7. Harness and Skills.pdf`, `8. Model Context Protocol.pdf`, `9. Loop and Hooks.pdf` |
| 시스템 분석 이론 | 5 | `ch01-1.pdf`, `ch02-1.pdf`, `ch04-2.pdf`, `ch05-1.pdf`, `ch06-1.pdf` |
| 알고리즘 | 10 | `CH01 알고리즘과 문제의 분석 (2).pdf`, `CH02 자료의 추상화와 기본 자료 구조.pdf`, `CH04 정렬.pdf`, `CH06 동적 집합과 탐색.pdf`, `CH07 그래프와 그래프 운행 1.pdf`, `CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`, `CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`, `CH10 동적 계획법.pdf`, `CH11 스트링 매칭.pdf`, `CH13 NP-완전 문제.pdf` |
| 자료구조 | 21 | `(참고자료) Week13_Graphs (1).pdf`, `CSE2112_02_week01_2.pdf` ~ `CSE2112_02_week13_2.pdf` (주차별 20개) |
| 컴퓨터네트워크 | 1 | `Week 01 Overview of Computer Networks (1).pdf` |

---

### 🔄 re-ingest 필요 (raw 갱신)

**없음** — 기존 소스 파일 변경 없음.

---

### 🔗 깨진 링크 (총 20건)

자동 수정하지 않음. 아래 항목은 존재하지 않는 페이지를 참조 중입니다.

| 참조 위치 | 깨진 링크 | 비고 |
|-----------|-----------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 페이지 미생성 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[array]]` | 페이지 미생성 |
| `binary-tree-traversal.md` | `[[tree]]` | 페이지 미생성 |
| `binary-tree.md` | `[[tree]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | 페이지 미생성 |
| `relational-model.md` | `[[normalization-theory]]` | 페이지 미생성 |
| `stack.md` | `[[linked-list]]` | 페이지 미생성 (중복 참조) |
| `tcp-header.md` | `[[udp]]` | 페이지 미생성 |
| `tcp-three-way-handshake.md` | `[[tcp-options]]` | 페이지 미생성 |
| `transport-layer-demultiplexing.md` | `[[udp]]` | 페이지 미생성 (중복 참조) |
| `use-case-formats.md` | `[[functional-requirements]]` | 페이지 미생성 |
| `use-case-formats.md` | `[[test-case]]` | 페이지 미생성 |
| `use-case.md` | `[[functional-requirements]]` | 페이지 미생성 (중복 참조) |
| `use-case.md` | `[[event-response-list]]` | 페이지 미생성 |
| `use-case.md` | `[[data-model]]` | 페이지 미생성 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 (중복 참조) |
| `tcp.md` | `[[udp]]` | 페이지 미생성 (중복 참조) |

> **참고:** `[[linked-list]]`, `[[udp]]`, `[[dijkstra-algorithm]]`, `[[functional-requirements]]` 는 복수의 페이지에서 참조 중인 **고우선순위 미생성 페이지**입니다. 해당 페이지 생성 시 다수의 깨진 링크가 일괄 해소됩니다.

---

### 📝 wiki 페이지 업데이트 필요

**이상 없음** — 기존 wiki 페이지 중 raw 파일 대비 갱신이 필요한 항목 없음.

---

### 📊 종합

| 항목 | 상태 |
|------|------|
| raw/ 신규 파일 | ⚠️ **55개 ingest 대기** |
| re-ingest 필요 | ✅ 이상 없음 |
| 깨진 링크 | ⚠️ **20건** (고우선순위 미생성 페이지 4종 포함) |
| wiki 페이지 업데이트 | ✅ 이상 없음 |

**업데이트 필요 항목: 총 75건 (ingest 55건 + 깨진 링크 20건)**

---

> 🤖 본 보고서는 자동 점검 결과를 기반으로 작성되었으며, 수정 작업은 수행되지 않았습니다. Ingest 및 링크 복구는 별도 세션에서 명시적으로 지시 후 수행 바랍니다.

AGENTS.md 파일 접근 권한이 제한되어 있지만, CLAUDE.md에 명시된 `wiki/log.md` 포맷과 시스템 지시사항의 back-check 형식을 기반으로 보고서를 작성합니다.

---

## [2026-06-04] back-check | 유지보수 점검

> **현황:** wiki 페이지 총 **255개** 관리 중

---

### raw/ 신규 파일 (ingest 대기)

총 **52개** 파일, 6개 과목 분류에서 신규 확인됨:

| 분류 | 파일 수 | 대표 파일명 |
|------|--------|------------|
| 데이터베이스 | 9 | ER model.pdf, Indexing.pdf, Intermediate SQL.pdf 외 6건 |
| 시스템 분석 실습 | 6 | 4. Plan_mode Sequential and Parallel agents.pdf 외 5건 |
| 시스템 분석 이론 | 5 | ch01-1.pdf, ch02-1.pdf, ch04-2.pdf 외 2건 |
| 알고리즘 | 10 | CH01 알고리즘과 문제의 분석 (2).pdf 외 9건 |
| 자료구조 | 21 | CSE2112_02_week01_2.pdf 외 20건 |
| 컴퓨터네트워크 | 1 | Week 01 Overview of Computer Networks (1).pdf |

<details>
<summary>전체 파일 목록 펼치기</summary>

**데이터베이스 (9건)**
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

**시스템 분석 실습 (6건)**
- `raw/시스템 분석 실습/4. Plan_mode Sequential and Parallel agents.pdf`
- `raw/시스템 분석 실습/5. Agent Specifications.pdf`
- `raw/시스템 분석 실습/6. Agent pool and Orchestrator.pdf`
- `raw/시스템 분석 실습/7. Harness and Skills.pdf`
- `raw/시스템 분석 실습/8. Model Context Protocol.pdf`
- `raw/시스템 분석 실습/9. Loop and Hooks.pdf`

**시스템 분석 이론 (5건)**
- `raw/시스템 분석 이론/ch01-1.pdf`
- `raw/시스템 분석 이론/ch02-1.pdf`
- `raw/시스템 분석 이론/ch04-2.pdf`
- `raw/시스템 분석 이론/ch05-1.pdf`
- `raw/시스템 분석 이론/ch06-1.pdf`

**알고리즘 (10건)**
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`

**자료구조 (21건)**
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`
- `raw/자료구조/CSE2112_02_week01_2.pdf` ~ `week13_2.pdf` (20건)

**컴퓨터네트워크 (1건)**
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf`

</details>

---

### re-ingest 필요 (raw 갱신)

- **이상 없음**

---

### 깨진 링크

총 **20건** 참조 오류, **14개** 미생성 페이지 슬러그 확인됨:

**자료구조 도메인 (5건 참조, 4개 미생성 슬러그)**

| 참조 위치 | 깨진 링크 |
|----------|----------|
| `adjacency-matrix.md` | `[[adjacency-list]]` |
| `binary-tree-implementation.md` | `[[linked-list]]` |
| `binary-tree-implementation.md` | `[[array]]` |
| `binary-tree-traversal.md` | `[[tree]]` |
| `binary-tree.md` | `[[tree]]` |

**알고리즘 도메인 (2건 참조, 1개 미생성 슬러그)**

| 참조 위치 | 깨진 링크 |
|----------|----------|
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` |

**데이터베이스 도메인 (3건 참조, 3개 미생성 슬러그)**

| 참조 위치 | 깨진 링크 |
|----------|----------|
| `relational-algebra.md` | `[[tuple-relational-calculus]]` |
| `relational-algebra.md` | `[[domain-relational-calculus]]` |
| `relational-model.md` | `[[normalization-theory]]` |

**컴퓨터네트워크 도메인 (4건 참조, 2개 미생성 슬러그)**

| 참조 위치 | 깨진 링크 |
|----------|----------|
| `tcp-header.md` | `[[udp]]` |
| `tcp-three-way-handshake.md` | `[[tcp-options]]` |
| `transport-layer-demultiplexing.md` | `[[udp]]` |
| `tcp.md` | `[[udp]]` |

**시스템 분석 도메인 (6건 참조, 4개 미생성 슬러그)**

| 참조 위치 | 깨진 링크 |
|----------|----------|
| `use-case-formats.md` | `[[functional-requirements]]` |
| `use-case-formats.md` | `[[test-case]]` |
| `use-case.md` | `[[functional-requirements]]` |
| `use-case.md` | `[[event-response-list]]` |
| `use-case.md` | `[[data-model]]` |
| `stack.md` | `[[linked-list]]` |

---

### wiki 페이지 업데이트 필요

- **이상 없음**

---

### 종합

| 항목 | 상태 | 건수 |
|------|------|------|
| raw/ 신규 ingest 대기 | ⚠️ 처리 필요 | 52건 (6개 과목) |
| re-ingest 필요 | ✅ 이상 없음 | 0건 |
| 깨진 링크 | ⚠️ 처리 필요 | 20건 참조 오류 / 14개 미생성 슬러그 |
| wiki 페이지 업데이트 | ✅ 이상 없음 | 0건 |
| **총 처리 필요 항목** | | **72건** |

> **권장 처리 순서:**
> 1. **깨진 링크 선처리** — 자료구조(`[[linked-list]]`, `[[tree]]`, `[[array]]`)·알고리즘(`[[dijkstra-algorithm]]`)·네트워크(`[[udp]]`) 슬러그는 ingest 예정 raw 파일들과 연관이 높아 ingest 시 자연히 해소될 가능성 큼. `[[stack-linked-list]]`·`[[functional-requirements]]`·`[[test-case]]` 등 독립적 슬러그는 별도 생성 검토 필요.
> 2. **Ingest 일괄 처리** — 과목 단위(데이터베이스 → 자료구조 → 알고리즘 → 시스템 분석 이론/실습 → 컴퓨터네트워크) 순으로 처리 권장.

파일 접근 권한이 없어, 제공된 점검 결과와 CLAUDE.md에 명시된 `wiki/log.md` 로그 형식을 기준으로 유지보수 보고서를 작성합니다.

---

## [2026-06-04] back-check | 유지보수 점검

- **점검 일시:** 2026-06-04
- **wiki 총 페이지 수:** 272개

---

### 1. raw/ 신규 파일 (ingest 대기)

총 **42건** 미처리 원본 파일이 확인됨.

| 카테고리 | 파일명 |
|----------|--------|
| 데이터베이스 | `ER model.pdf` |
| 데이터베이스 | `Indexing.pdf` |
| 데이터베이스 | `Intermediate SQL.pdf` |
| 데이터베이스 | `Intro to databases.pdf` |
| 데이터베이스 | `Query Processing.pdf` |
| 데이터베이스 | `Relational DB Design (1).pdf` |
| 데이터베이스 | `Relational Model 2.pdf` |
| 데이터베이스 | `SQL Basics.pdf` |
| 데이터베이스 | `Storage and File Structure (1).pdf` |
| 시스템 분석 이론 | `ch06-1.pdf` |
| 알고리즘 | `CH01 알고리즘과 문제의 분석 (2).pdf` |
| 알고리즘 | `CH02 자료의 추상화와 기본 자료 구조.pdf` |
| 알고리즘 | `CH04 정렬.pdf` |
| 알고리즘 | `CH06 동적 집합과 탐색.pdf` |
| 알고리즘 | `CH07 그래프와 그래프 운행 1.pdf` |
| 알고리즘 | `CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf` |
| 알고리즘 | `CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf` |
| 알고리즘 | `CH10 동적 계획법.pdf` |
| 알고리즘 | `CH11 스트링 매칭.pdf` |
| 알고리즘 | `CH13 NP-완전 문제.pdf` |
| 자료구조 | `(참고자료) Week13_Graphs (1).pdf` |
| 자료구조 | `CSE2112_02_week01_2.pdf` |
| 자료구조 | `CSE2112_02_week02_1.pdf` |
| 자료구조 | `CSE2112_02_week03_1.pdf` |
| 자료구조 | `CSE2112_02_week03_2.pdf` |
| 자료구조 | `CSE2112_02_week04_1.pdf` |
| 자료구조 | `CSE2112_02_week04_2.pdf` |
| 자료구조 | `CSE2112_02_week05_1.pdf` |
| 자료구조 | `CSE2112_02_week05_2.pdf` |
| 자료구조 | `CSE2112_02_week06_1.pdf` |
| 자료구조 | `CSE2112_02_week06_2.pdf` |
| 자료구조 | `CSE2112_02_week07_1.pdf` |
| 자료구조 | `CSE2112_02_week07_2.pdf` |
| 자료구조 | `CSE2112_02_week09_2.pdf` |
| 자료구조 | `CSE2112_02_week10_1.pdf` |
| 자료구조 | `CSE2112_02_week10_2.pdf` |
| 자료구조 | `CSE2112_02_week11_2.pdf` |
| 자료구조 | `CSE2112_02_week12_1.pdf` |
| 자료구조 | `CSE2112_02_week12_2.pdf` |
| 자료구조 | `CSE2112_02_week13_1 (1).pdf` |
| 자료구조 | `CSE2112_02_week13_2.pdf` |
| 컴퓨터네트워크 | `Week 01 Overview of Computer Networks (1).pdf` |

---

### 2. re-ingest 필요 (raw 갱신)

이상 없음.

---

### 3. 깨진 링크

총 **19건** 미존재 페이지 참조 오류 확인됨.

| 출처 페이지 | 깨진 참조 | 비고 |
|-------------|-----------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 대상 페이지 미생성 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 대상 페이지 미생성 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 대상 페이지 미생성 |
| `binary-tree-implementation.md` | `[[array]]` | 대상 페이지 미생성 |
| `binary-tree-traversal.md` | `[[tree]]` | 대상 페이지 미생성 |
| `binary-tree.md` | `[[tree]]` | 대상 페이지 미생성 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | 대상 페이지 미생성 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | 대상 페이지 미생성 |
| `relational-model.md` | `[[normalization-theory]]` | 대상 페이지 미생성 |
| `stack.md` | `[[linked-list]]` | 대상 페이지 미생성 |
| `tcp-header.md` | `[[udp]]` | 대상 페이지 미생성 |
| `tcp-three-way-handshake.md` | `[[tcp-options]]` | 대상 페이지 미생성 |
| `transport-layer-demultiplexing.md` | `[[udp]]` | 대상 페이지 미생성 |
| `use-case-formats.md` | `[[functional-requirements]]` | 대상 페이지 미생성 |
| `use-case-formats.md` | `[[test-case]]` | 대상 페이지 미생성 |
| `use-case.md` | `[[functional-requirements]]` | 대상 페이지 미생성 |
| `use-case.md` | `[[data-model]]` | 대상 페이지 미생성 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 대상 페이지 미생성 |
| `tcp.md` | `[[udp]]` | 대상 페이지 미생성 |

> **참고:** `[[udp]]`, `[[linked-list]]`, `[[tree]]`, `[[dijkstra-algorithm]]`, `[[functional-requirements]]` 는 복수의 페이지에서 참조 중이므로 ingest 우선 처리 권장.

---

### 4. wiki 페이지 업데이트 필요

이상 없음.

---

### 5. 종합

| 항목 | 건수 | 상태 |
|------|------|------|
| ingest 대기 raw 파일 | 42건 | ⚠️ 처리 필요 |
| re-ingest 필요 | 0건 | ✅ 이상 없음 |
| 깨진 링크 | 19건 | ⚠️ 처리 필요 |
| wiki 페이지 갱신 | 0건 | ✅ 이상 없음 |

> **업데이트 필요 항목 총 61건** — ingest 42건 + 깨진 링크 19건.
> 깨진 링크 중 다수는 ingest 완료 시 자동 해소될 가능성이 있으므로, **ingest 선행 후 링크 재점검**을 권장합니다.

## [2026-06-04] ingest | ch06-1.pdf

- **Source(s):**
  - raw/시스템 분석 이론/ch06-1.pdf
- **Pages created:** [[modality]], [[intersection-entity]], [[crud-matrix]]
- **Pages updated:** 없음
- **Contradictions flagged:** 없음
- **Notes:** edit_agent.py --ingest 자동 처리

파일 접근 권한이 제한되어 있지만, 시스템 프롬프트의 보고서 형식과 제공된 점검 결과를 토대로 보고서를 작성하겠습니다.

---

## [2026-06-04] back-check | 유지보수 점검

### 기본 현황

- **점검 일자:** 2026-06-04
- **wiki 총 페이지 수:** 275개

---

### raw/ 신규 파일 (ingest 대기)

총 **41개** 파일이 ingest 대기 중입니다.

#### 📁 데이터베이스 (9개)
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

#### 📁 알고리즘 (10개)
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`

#### 📁 자료구조 (21개)
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`
- `raw/자료구조/CSE2112_02_week01_2.pdf`
- `raw/자료구조/CSE2112_02_week02_1.pdf`
- `raw/자료구조/CSE2112_02_week03_1.pdf`
- `raw/자료구조/CSE2112_02_week03_2.pdf`
- `raw/자료구조/CSE2112_02_week04_1.pdf`
- `raw/자료구조/CSE2112_02_week04_2.pdf`
- `raw/자료구조/CSE2112_02_week05_1.pdf`
- `raw/자료구조/CSE2112_02_week05_2.pdf`
- `raw/자료구조/CSE2112_02_week06_1.pdf`
- `raw/자료구조/CSE2112_02_week06_2.pdf`
- `raw/자료구조/CSE2112_02_week07_1.pdf`
- `raw/자료구조/CSE2112_02_week07_2.pdf`
- `raw/자료구조/CSE2112_02_week09_2.pdf`
- `raw/자료구조/CSE2112_02_week10_1.pdf`
- `raw/자료구조/CSE2112_02_week10_2.pdf`
- `raw/자료구조/CSE2112_02_week11_2.pdf`
- `raw/자료구조/CSE2112_02_week12_1.pdf`
- `raw/자료구조/CSE2112_02_week12_2.pdf`
- `raw/자료구조/CSE2112_02_week13_1 (1).pdf`
- `raw/자료구조/CSE2112_02_week13_2.pdf`

#### 📁 컴퓨터네트워크 (1개)
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf`

---

### re-ingest 필요 (raw 갱신)

**없음**

---

### 오래된 wiki 페이지

**없음** — wiki 페이지 업데이트 지연 항목 없음

---

### 깨진 링크 (총 19건, 13개 페이지)

| 페이지 | 깨진 링크 | 비고 |
|--------|-----------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 자료구조 계열 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 알고리즘 계열 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 자료구조 계열 |
| `binary-tree-implementation.md` | `[[array]]` | 자료구조 계열 |
| `binary-tree-traversal.md` | `[[tree]]` | 자료구조 계열 |
| `binary-tree.md` | `[[tree]]` | 자료구조 계열 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | 데이터베이스 계열 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | 데이터베이스 계열 |
| `relational-model.md` | `[[normalization-theory]]` | 데이터베이스 계열 |
| `stack.md` | `[[linked-list]]` | 자료구조 계열 |
| `tcp-header.md` | `[[udp]]` | 네트워크 계열 |
| `tcp-three-way-handshake.md` | `[[tcp-options]]` | 네트워크 계열 |
| `transport-layer-demultiplexing.md` | `[[udp]]` | 네트워크 계열 |
| `use-case-formats.md` | `[[functional-requirements]]` | 소프트웨어공학 계열 |
| `use-case-formats.md` | `[[test-case]]` | 소프트웨어공학 계열 |
| `use-case.md` | `[[functional-requirements]]` | 소프트웨어공학 계열 |
| `use-case.md` | `[[data-model]]` | 소프트웨어공학 계열 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 알고리즘 계열 |
| `tcp.md` | `[[udp]]` | 네트워크 계열 |

> 💡 **패턴 분석:** `[[udp]]`, `[[linked-list]]`, `[[dijkstra-algorithm]]`, `[[functional-requirements]]`, `[[tree]]` 등은 다수의 페이지에서 공통 참조되는 미작성 페이지입니다. 해당 페이지를 우선 생성하면 복수의 깨진 링크를 한 번에 해소할 수 있습니다.

---

### 종합

- **raw/ 신규 파일:** 업데이트 필요 **41건** (데이터베이스 9, 알고리즘 10, 자료구조 21, 컴퓨터네트워크 1)
- **오래된 wiki 페이지:** 이상 없음
- **깨진 링크:** **19건** (13개 페이지)
- **re-ingest 대상:** 이상 없음
- **전체 업데이트 필요 항목:** **60건** (ingest 41 + 깨진 링크 19)

#### 권장 처리 순서
1. **[높음]** 깨진 링크 해소 — 신규 raw ingest 시 자동 생성될 가능성 있는 페이지(`[[linked-list]]`, `[[tree]]`, `[[dijkstra-algorithm]]` 등)는 ingest 후 재점검
2. **[높음]** 자료구조/알고리즘/데이터베이스 raw 파일 ingest — 연계된 깨진 링크 해소 기대
3. **[보통]** 컴퓨터네트워크 신규 파일 ingest (`[[udp]]`, `[[tcp-options]]` 생성 예상)

파일 접근 권한이 없지만, 제공해주신 점검 결과와 시스템에 정의된 형식을 바탕으로 보고서를 작성할게요.

---

## [2026-06-04] back-check | 유지보수 점검

- **wiki 총 페이지 수:** 275개

---

### raw/ 신규 파일 (ingest 대기): 41건

**데이터베이스 (9건)**
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

**알고리즘 (10건)**
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`

**자료구조 (21건)**
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`
- `raw/자료구조/CSE2112_02_week01_2.pdf`
- `raw/자료구조/CSE2112_02_week02_1.pdf`
- `raw/자료구조/CSE2112_02_week03_1.pdf`
- `raw/자료구조/CSE2112_02_week03_2.pdf`
- `raw/자료구조/CSE2112_02_week04_1.pdf`
- `raw/자료구조/CSE2112_02_week04_2.pdf`
- `raw/자료구조/CSE2112_02_week05_1.pdf`
- `raw/자료구조/CSE2112_02_week05_2.pdf`
- `raw/자료구조/CSE2112_02_week06_1.pdf`
- `raw/자료구조/CSE2112_02_week06_2.pdf`
- `raw/자료구조/CSE2112_02_week07_1.pdf`
- `raw/자료구조/CSE2112_02_week07_2.pdf`
- `raw/자료구조/CSE2112_02_week09_2.pdf`
- `raw/자료구조/CSE2112_02_week10_1.pdf`
- `raw/자료구조/CSE2112_02_week10_2.pdf`
- `raw/자료구조/CSE2112_02_week11_2.pdf`
- `raw/자료구조/CSE2112_02_week12_1.pdf`
- `raw/자료구조/CSE2112_02_week12_2.pdf`
- `raw/자료구조/CSE2112_02_week13_1 (1).pdf`
- `raw/자료구조/CSE2112_02_week13_2.pdf`

**컴퓨터네트워크 (1건)**
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf`

---

### re-ingest 필요 (raw 갱신): 이상 없음

---

### 깨진 링크: 19건

| 페이지 | 참조 오류 슬러그 | 비고 |
|--------|----------------|------|
| `adjacency-matrix.md` | [[adjacency-list]] | 미생성 페이지 |
| `all-pairs-shortest-paths.md` | [[dijkstra-algorithm]] | 미생성 페이지 |
| `binary-tree-implementation.md` | [[linked-list]] | 미생성 페이지 |
| `binary-tree-implementation.md` | [[array]] | 미생성 페이지 |
| `binary-tree-traversal.md` | [[tree]] | 미생성 페이지 |
| `binary-tree.md` | [[tree]] | 미생성 페이지 |
| `relational-algebra.md` | [[tuple-relational-calculus]] | 미생성 페이지 |
| `relational-algebra.md` | [[domain-relational-calculus]] | 미생성 페이지 |
| `relational-model.md` | [[normalization-theory]] | 미생성 페이지 |
| `stack.md` | [[linked-list]] | 미생성 페이지 |
| `tcp-header.md` | [[udp]] | 미생성 페이지 |
| `tcp-three-way-handshake.md` | [[tcp-options]] | 미생성 페이지 |
| `transport-layer-demultiplexing.md` | [[udp]] | 미생성 페이지 |
| `use-case-formats.md` | [[functional-requirements]] | 미생성 페이지 |
| `use-case-formats.md` | [[test-case]] | 미생성 페이지 |
| `use-case.md` | [[functional-requirements]] | 미생성 페이지 |
| `use-case.md` | [[data-model]] | 미생성 페이지 |
| `floyd-warshall-algorithm.md` | [[dijkstra-algorithm]] | 미생성 페이지 |
| `tcp.md` | [[udp]] | 미생성 페이지 |

> **패턴 분석:**
> - `[[udp]]` — 3개 페이지에서 반복 참조 (우선순위 높음)
> - `[[dijkstra-algorithm]]` — 2개 페이지에서 반복 참조
> - `[[linked-list]]` — 2개 페이지에서 반복 참조
> - `[[tree]]` — 2개 페이지에서 반복 참조
> - `[[functional-requirements]]` — 2개 페이지에서 반복 참조

---

### wiki 페이지 업데이트 필요: 이상 없음

---

### 종합

| 항목 | 건수 | 상태 |
|------|------|------|
| ingest 대기 (신규 raw) | 41건 | ⚠️ 처리 필요 |
| re-ingest 필요 | 0건 | ✅ 이상 없음 |
| 깨진 링크 | 19건 | ⚠️ 처리 필요 |
| wiki 페이지 업데이트 | 0건 | ✅ 이상 없음 |
| **총 업데이트 필요 항목** | **60건** | ⚠️ **조치 필요** |

> **권고 처리 순서:**
> 1. `[[udp]]`, `[[dijkstra-algorithm]]`, `[[linked-list]]`, `[[tree]]`, `[[functional-requirements]]` 등 중복 참조되는 깨진 링크 페이지 우선 생성
> 2. 자료구조 21건 → 알고리즘 10건 → 데이터베이스 9건 → 컴퓨터네트워크 1건 순으로 ingest 진행
> 3. ingest 완료 후 `wiki/index.md` 및 `wiki/log.md` 갱신

제공된 점검 데이터를 바탕으로 보고서를 작성합니다.

---

## [2026-06-04] back-check | 유지보수 점검

- **점검 시각:** 2026-06-04
- **wiki 총 페이지 수:** 275개

---

### raw/ 신규 파일 (ingest 대기): 41건

**데이터베이스 (9건)**
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

**알고리즘 (10건)**
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`

**자료구조 (21건)**
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`
- `raw/자료구조/CSE2112_02_week01_2.pdf`
- `raw/자료구조/CSE2112_02_week02_1.pdf`
- `raw/자료구조/CSE2112_02_week03_1.pdf`
- `raw/자료구조/CSE2112_02_week03_2.pdf`
- `raw/자료구조/CSE2112_02_week04_1.pdf`
- `raw/자료구조/CSE2112_02_week04_2.pdf`
- `raw/자료구조/CSE2112_02_week05_1.pdf`
- `raw/자료구조/CSE2112_02_week05_2.pdf`
- `raw/자료구조/CSE2112_02_week06_1.pdf`
- `raw/자료구조/CSE2112_02_week06_2.pdf`
- `raw/자료구조/CSE2112_02_week07_1.pdf`
- `raw/자료구조/CSE2112_02_week07_2.pdf`
- `raw/자료구조/CSE2112_02_week09_2.pdf`
- `raw/자료구조/CSE2112_02_week10_1.pdf`
- `raw/자료구조/CSE2112_02_week10_2.pdf`
- `raw/자료구조/CSE2112_02_week11_2.pdf`
- `raw/자료구조/CSE2112_02_week12_1.pdf`
- `raw/자료구조/CSE2112_02_week12_2.pdf`
- `raw/자료구조/CSE2112_02_week13_1 (1).pdf`
- `raw/자료구조/CSE2112_02_week13_2.pdf`

**컴퓨터네트워크 (1건)**
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf`

---

### re-ingest 필요 (raw 갱신): 이상 없음

---

### 깨진 링크: 19건 (미작성 슬러그 13개)

| 참조 페이지 | 깨진 링크 |
|------------|----------|
| `adjacency-matrix.md` | `[[adjacency-list]]` |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` |
| `binary-tree-implementation.md` | `[[linked-list]]`, `[[array]]` |
| `binary-tree-traversal.md` | `[[tree]]` |
| `binary-tree.md` | `[[tree]]` |
| `relational-algebra.md` | `[[tuple-relational-calculus]]`, `[[domain-relational-calculus]]` |
| `relational-model.md` | `[[normalization-theory]]` |
| `stack.md` | `[[linked-list]]` |
| `tcp-header.md` | `[[udp]]` |
| `tcp-three-way-handshake.md` | `[[tcp-options]]` |
| `transport-layer-demultiplexing.md` | `[[udp]]` |
| `use-case-formats.md` | `[[functional-requirements]]`, `[[test-case]]` |
| `use-case.md` | `[[functional-requirements]]`, `[[data-model]]` |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` |
| `tcp.md` | `[[udp]]` |

**미작성 슬러그 목록 (13개):**
`[[adjacency-list]]`, `[[dijkstra-algorithm]]`, `[[linked-list]]`, `[[array]]`, `[[tree]]`, `[[tuple-relational-calculus]]`, `[[domain-relational-calculus]]`, `[[normalization-theory]]`, `[[udp]]`, `[[tcp-options]]`, `[[functional-requirements]]`, `[[test-case]]`, `[[data-model]]`

---

### 오래된 wiki 페이지: 이상 없음

---

### 종합: 업데이트 필요 항목 60건

| 구분 | 건수 | 내용 |
|------|------|------|
| ingest 대기 (신규 raw) | 41건 | 데이터베이스 9, 알고리즘 10, 자료구조 21, 컴퓨터네트워크 1 |
| 깨진 링크 | 19건 | 15개 페이지, 미작성 슬러그 13개 |
| re-ingest 필요 | 0건 | 이상 없음 |
| wiki 페이지 업데이트 | 0건 | 이상 없음 |
| **합계** | **60건** | |

> **권장 처리 순서:** ① 깨진 링크 해소 (13개 슬러그 신규 작성) → ② 신규 raw 41건 ingest (데이터베이스 → 자료구조 → 알고리즘 → 컴퓨터네트워크 순 권장)

AGENTS.md를 확인하려 했지만 권한이 필요합니다. CLAUDE.md의 `log.md` 형식과 제 보고 규칙을 기반으로 점검 결과를 정리하겠습니다.

---

## [2026-06-04] back-check | 유지보수 점검

---

### 기본 현황

- **점검 일자:** 2026-06-04
- **현재 wiki 페이지 수:** 275개
- **re-ingest 필요 항목:** 없음
- **wiki 페이지 업데이트 필요:** 이상 없음

---

### raw/ 신규 파일 (ingest 대기)

총 **41개** 파일이 ingest 되지 않은 상태입니다.

#### 📂 데이터베이스 (9개)
- `raw/데이터베이스/ER model.pdf`
- `raw/데이터베이스/Indexing.pdf`
- `raw/데이터베이스/Intermediate SQL.pdf`
- `raw/데이터베이스/Intro to databases.pdf`
- `raw/데이터베이스/Query Processing.pdf`
- `raw/데이터베이스/Relational DB Design (1).pdf`
- `raw/데이터베이스/Relational Model 2.pdf`
- `raw/데이터베이스/SQL Basics.pdf`
- `raw/데이터베이스/Storage and File Structure (1).pdf`

#### 📂 알고리즘 (10개)
- `raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf`
- `raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf`
- `raw/알고리즘/CH04 정렬.pdf`
- `raw/알고리즘/CH06 동적 집합과 탐색.pdf`
- `raw/알고리즘/CH07 그래프와 그래프 운행 1.pdf`
- `raw/알고리즘/CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`
- `raw/알고리즘/CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`
- `raw/알고리즘/CH10 동적 계획법.pdf`
- `raw/알고리즘/CH11 스트링 매칭.pdf`
- `raw/알고리즘/CH13 NP-완전 문제.pdf`

#### 📂 자료구조 (21개)
- `raw/자료구조/(참고자료) Week13_Graphs (1).pdf`
- `raw/자료구조/CSE2112_02_week01_2.pdf`
- `raw/자료구조/CSE2112_02_week02_1.pdf`
- `raw/자료구조/CSE2112_02_week03_1.pdf`
- `raw/자료구조/CSE2112_02_week03_2.pdf`
- `raw/자료구조/CSE2112_02_week04_1.pdf`
- `raw/자료구조/CSE2112_02_week04_2.pdf`
- `raw/자료구조/CSE2112_02_week05_1.pdf`
- `raw/자료구조/CSE2112_02_week05_2.pdf`
- `raw/자료구조/CSE2112_02_week06_1.pdf`
- `raw/자료구조/CSE2112_02_week06_2.pdf`
- `raw/자료구조/CSE2112_02_week07_1.pdf`
- `raw/자료구조/CSE2112_02_week07_2.pdf`
- `raw/자료구조/CSE2112_02_week09_2.pdf`
- `raw/자료구조/CSE2112_02_week10_1.pdf`
- `raw/자료구조/CSE2112_02_week10_2.pdf`
- `raw/자료구조/CSE2112_02_week11_2.pdf`
- `raw/자료구조/CSE2112_02_week12_1.pdf`
- `raw/자료구조/CSE2112_02_week12_2.pdf`
- `raw/자료구조/CSE2112_02_week13_1 (1).pdf`
- `raw/자료구조/CSE2112_02_week13_2.pdf`

#### 📂 컴퓨터네트워크 (1개)
- `raw/컴퓨터네트워크/Week 01 Overview of Computer Networks (1).pdf`

---

### 깨진 링크 (19건, 15개 페이지)

| 페이지 | 깨진 링크 | 비고 |
|--------|-----------|------|
| `adjacency-matrix.md` | `[[adjacency-list]]` | 페이지 미생성 |
| `all-pairs-shortest-paths.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[linked-list]]` | 페이지 미생성 |
| `binary-tree-implementation.md` | `[[array]]` | 페이지 미생성 |
| `binary-tree-traversal.md` | `[[tree]]` | 페이지 미생성 |
| `binary-tree.md` | `[[tree]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[tuple-relational-calculus]]` | 페이지 미생성 |
| `relational-algebra.md` | `[[domain-relational-calculus]]` | 페이지 미생성 |
| `relational-model.md` | `[[normalization-theory]]` | 페이지 미생성 |
| `stack.md` | `[[linked-list]]` | 페이지 미생성 |
| `tcp-header.md` | `[[udp]]` | 페이지 미생성 |
| `tcp-three-way-handshake.md` | `[[tcp-options]]` | 페이지 미생성 |
| `tcp.md` | `[[udp]]` | 페이지 미생성 |
| `transport-layer-demultiplexing.md` | `[[udp]]` | 페이지 미생성 |
| `floyd-warshall-algorithm.md` | `[[dijkstra-algorithm]]` | 페이지 미생성 |
| `use-case-formats.md` | `[[functional-requirements]]` | 페이지 미생성 |
| `use-case-formats.md` | `[[test-case]]` | 페이지 미생성 |
| `use-case.md` | `[[functional-requirements]]` | 페이지 미생성 |
| `use-case.md` | `[[data-model]]` | 페이지 미생성 |

> ℹ️ CLAUDE.md 스키마상 미생성 링크는 지식 공백(knowledge gap) 마커로 허용됩니다. 단, ingest 이후 해당 페이지가 생성될 가능성이 높은 항목은 ingest 우선순위에 반영 권장합니다.
>
> **ingest 완료 시 자동 해소 예상 링크:** `[[linked-list]]`, `[[array]]`, `[[tree]]`, `[[dijkstra-algorithm]]`, `[[adjacency-list]]`, `[[udp]]` (자료구조·알고리즘 ingest 후), `[[normalization-theory]]`, `[[tuple-relational-calculus]]`, `[[domain-relational-calculus]]` (데이터베이스 ingest 후)

---

### 종합

- **raw/ 신규 파일:** 41건 (데이터베이스 9 · 알고리즘 10 · 자료구조 21 · 컴퓨터네트워크 1)
- **오래된 wiki 페이지:** 이상 없음
- **깨진 링크:** 19건 (15개 페이지) — 대부분 ingest 대기 파일과 연관된 미생성 페이지
- **re-ingest 필요:** 이상 없음
- **종합:** **업데이트 필요 항목 60건** (ingest 41 + 깨진 링크 19)

> 🔧 **권고 조치 순서**
> 1. `자료구조` → `알고리즘` → `데이터베이스` → `컴퓨터네트워크` 순으로 ingest 수행
> 2. ingest 완료 후 깨진 링크 재점검 (다수 자동 해소 예상)
> 3. `[[udp]]`, `[[tcp-options]]`, `[[functional-requirements]]`, `[[test-case]]`, `[[data-model]]` 등 ingest 후에도 잔존하는 링크는 별도 페이지 생성 검토

파일 접근 권한이 제한되어 있지만, CLAUDE.md에 명시된 `log.md` 형식과 시스템에 정의된 보고서 형식을 기반으로 보고서를 작성하겠습니다.

---

## [2026-06-04] back-check | 유지보수 점검

- **wiki 페이지 총 수:** 275개

---

### raw/ 신규 파일 (ingest 대기)

총 **41개** 미처리 파일 확인됨:

| 분류 | 파일 수 | 파일 목록 |
|------|---------|-----------|
| 데이터베이스 | 9 | `ER model.pdf`, `Indexing.pdf`, `Intermediate SQL.pdf`, `Intro to databases.pdf`, `Query Processing.pdf`, `Relational DB Design (1).pdf`, `Relational Model 2.pdf`, `SQL Basics.pdf`, `Storage and File Structure (1).pdf` |
| 알고리즘 | 10 | `CH01 알고리즘과 문제의 분석 (2).pdf`, `CH02 자료의 추상화와 기본 자료 구조.pdf`, `CH04 정렬.pdf`, `CH06 동적 집합과 탐색.pdf`, `CH07 그래프와 그래프 운행 1.pdf`, `CH08 그래프 최적화 문제와 욕심쟁이 방법.pdf`, `CH09 이행 폐쇄와 모든 쌍 최단 경로.pdf`, `CH10 동적 계획법.pdf`, `CH11 스트링 매칭.pdf`, `CH13 NP-완전 문제.pdf` |
| 자료구조 | 21 | `(참고자료) Week13_Graphs (1).pdf`, `CSE2112_02_week01_2.pdf` ~ `CSE2112_02_week13_2.pdf` (주차별 강의자료 21종) |
| 컴퓨터네트워크 | 1 | `Week 01 Overview of Computer Networks (1).pdf` |

---

### re-ingest 필요 (raw 갱신)

- **이상 없음**

---

### 깨진 링크

총 **19건** 참조 오류 확인됨 (고유 미생성 페이지: **13개**):

| 미생성 페이지 | 참조하는 페이지 | 참조 횟수 |
|--------------|----------------|----------|
| `[[udp]]` | `tcp-header.md`, `tcp.md`, `transport-layer-demultiplexing.md` | 3 |
| `[[dijkstra-algorithm]]` | `all-pairs-shortest-paths.md`, `floyd-warshall-algorithm.md` | 2 |
| `[[linked-list]]` | `binary-tree-implementation.md`, `stack.md` | 2 |
| `[[tree]]` | `binary-tree-traversal.md`, `binary-tree.md` | 2 |
| `[[functional-requirements]]` | `use-case-formats.md`, `use-case.md` | 2 |
| `[[adjacency-list]]` | `adjacency-matrix.md` | 1 |
| `[[array]]` | `binary-tree-implementation.md` | 1 |
| `[[tuple-relational-calculus]]` | `relational-algebra.md` | 1 |
| `[[domain-relational-calculus]]` | `relational-algebra.md` | 1 |
| `[[normalization-theory]]` | `relational-model.md` | 1 |
| `[[tcp-options]]` | `tcp-three-way-handshake.md` | 1 |
| `[[test-case]]` | `use-case-formats.md` | 1 |
| `[[data-model]]` | `use-case.md` | 1 |

---

### wiki 페이지 업데이트 필요

- **이상 없음**

---

### 종합

> **업데이트 필요 항목 2종류 · 총 60건**

| 항목 | 건수 | 우선순위 |
|------|------|---------|
| ingest 대기 raw 파일 | 41개 | 🔴 높음 — 데이터베이스·알고리즘·자료구조 강의자료 신규 추가 |
| 깨진 링크 (미생성 페이지 13개) | 19건 | 🟡 중간 — `[[udp]]`, `[[dijkstra-algorithm]]`, `[[linked-list]]` 등 다수 페이지에서 참조 중이므로 우선 생성 권장 |

**권장 조치 순서:**
1. 깨진 링크 중 참조 횟수가 많은 `[[udp]]`(3회), `[[dijkstra-algorithm]]`(2회), `[[linked-list]]`(2회), `[[tree]]`(2회), `[[functional-requirements]]`(2회) 페이지를 먼저 생성
2. 이후 41개 raw 파일 일괄 ingest (데이터베이스 → 자료구조 → 알고리즘 → 컴퓨터네트워크 순서 권장)
