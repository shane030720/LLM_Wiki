---
title: Query Processing
category: concept
tags: [database, query, optimization, relational-algebra, selection, index]
sources: [raw/데이터베이스/Query Processing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Query processing은 SQL로 작성된 질의를 실제 데이터로 변환하는 일련의 과정이다. Parsing과 translation, optimization, evaluation의 세 단계로 구성되며, 동등한 evaluation plan 중 최소 비용의 것을 선택하는 것이 핵심 목표다. 비용은 주로 디스크 block transfer 횟수로 측정한다.

## How It Works

### 기본 처리 단계

1. **Parsing and translation**: SQL 질의를 relational algebra expression으로 변환
2. **Optimization**: 동등한 evaluation plan 중 cost가 가장 낮은 것을 선택
   - Database catalog의 통계 정보(튜플 수, 튜플 크기 등)를 사용해 비용 추정
3. **Evaluation**: 선택된 plan을 실행하여 결과 반환

### I/O Complexity Model

Query cost는 디스크 block transfer 횟수로 측정하며 CPU cost와 seek cost는 단순화를 위해 무시한다.

- **M**: 메인 메모리에 올릴 수 있는 튜플 수 (메모리 크기)
- **B**: 한 블록에 담을 수 있는 튜플 수 (블록 크기)
- **N**: 릴레이션의 튜플 수

| 패턴 | I/O 복잡도 |
|------|-----------|
| Linear I/O | O(N/B) |
| Logarithmic I/O | O(log_B N) |

실제 가용 메모리는 실행 시점에만 알 수 있으므로 worst-case 기준(최소 필요 메모리)으로 추정한다.

### Selection Operation 알고리즘

**File scan:**
- **A1 (Linear search)**: 모든 파일 블록을 순차 스캔하여 조건 검사. I/O Cost = O(N/B). 인덱스 유무·레코드 순서·조건 종류에 무관하게 항상 적용 가능.

**Index scan — primary B+-tree:**
- **A2 (equality on key)**: 단일 레코드 검색. I/O Cost = O(log_B N)
- **A3 (equality on non-key)**: T개의 동일 search-key 레코드 검색. I/O Cost = O(log_B N + T/B)

**Index scan — secondary index:**
- **A4 (equality on nonkey)**: 매칭 T개 레코드가 각기 다른 블록에 존재할 수 있음. I/O Cost = O(log_B N + T). 레코드당 random I/O가 발생하여 매우 비쌀 수 있다.

**Comparison 기반 selection:**
- **A5 (primary index, comparison)**: 릴레이션이 정렬된 경우, 인덱스로 시작점을 찾아 순차 스캔
- **A6 (secondary index, comparison)**: leaf page를 순차 스캔하며 포인터 수집 후 레코드 접근. 레코드당 I/O 발생으로 linear file scan(A1)이 오히려 유리할 수 있음

## Key Properties

- 디스크 접근이 지배적 비용 요인이며 CPU 비용은 부차적
- M > N이면 모든 튜플을 메모리에 올릴 수 있으나 N/B 블록 읽기는 여전히 필요
- Secondary index의 range selection은 레코드당 random I/O가 발생하여 selectivity가 낮을수록 linear scan 대비 불리
- Primary index는 레코드가 물리적으로 정렬되어 있어 순차 접근 가능; secondary index는 논리적 순서만 보장

## Relationships

- [[external-merge-sort]] (많은 relational operation이 정렬된 입력을 필요로 함; merge-join의 전처리)
- [[hash-join]] (equi-join에 최적화된 join 알고리즘)
- [[join-algorithm-comparison]] (join 알고리즘 전체 비교 분석)

## Open Questions

- Secondary index를 이용한 range selection이 linear scan보다 비효율적인 정확한 임계 selectivity는?
- CPU cost와 seek cost를 포함한 실제 비용 모델에서 알고리즘 선택이 어떻게 달라지는가?
- 동일한 query에 대해 optimizer가 여러 equivalent plan을 생성할 때 탐색 공간의 크기를 어떻게 제어하는가?

## Sources

- raw/데이터베이스/Query Processing.pdf
