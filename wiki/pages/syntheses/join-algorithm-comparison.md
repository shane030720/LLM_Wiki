---
title: Join Algorithm Comparison
category: synthesis
tags: [database, join, algorithm, performance, optimization, cost-model]
sources: [raw/데이터베이스/Query Processing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Thesis

데이터베이스의 5가지 주요 join 알고리즘(nested-loop join, block nested-loop join, indexed nested-loop join, merge-join, hash-join)은 각각 고유한 I/O cost 특성과 적용 조건을 가진다. 최적 알고리즘 선택은 릴레이션 크기, 메모리 크기, 인덱스 유무, 데이터 정렬 여부에 따라 달라지며, 단일 알고리즘이 모든 상황에서 최적이지 않다.

## Evidence

### 알고리즘별 I/O Cost 요약

| 알고리즘 | 최악 I/O Cost | 최선 I/O Cost | 적용 가능 join 종류 |
|---------|-------------|-------------|-----------------|
| Nested-Loop Join | O(N²/B) | O(N/B) (내부 릴레이션이 메모리에 적재 가능 시) | 모든 조건 |
| Block Nested-Loop Join | O(N²/B²) | O(N/B) | 모든 조건 |
| Block Nested-Loop (메모리 M 활용) | O(N²/BM) | O(N/B) | 모든 조건 |
| Indexed Nested-Loop Join | O(N log_B N) | O(N log_B N) | Equi-join, inner relation에 인덱스 존재 |
| Merge-Join | O(N/B) + 정렬 비용 | O(N/B) (이미 정렬된 경우) | Equi-join, natural join |
| Hash-Join | O(N/B) | O(N/B) | Equi-join, natural join |

*N_r, N_s가 크게 다를 경우 outer/inner relation 선택이 비용에 중요한 영향을 미침.*

### 구체적 비용 비교 예시 (student ⋈ takes)

- student: 5,000 튜플, 100 블록 (N_r/B = 100)
- takes: 10,000 튜플, 400 블록 (N_s/B = 400)

| 알고리즘 | Block Transfers | 비고 |
|---------|---------------|------|
| Nested-Loop (student outer) | 5,000 × 400 + 100 = 2,000,100 | worst case |
| Nested-Loop (takes outer) | 10,000 × 100 + 400 = 1,000,400 | outer를 큰 쪽으로 선택하면 더 불리 |
| Block Nested-Loop (worst) | 100 × 400 + 100 = 40,100 | student outer |
| Indexed Nested-Loop (B+-tree 높이 4+1) | 100 + 5,000 × 5 = 25,100 | takes에 primary B+-tree index 존재 시 |

- Hash join (instructor ⋈ teaches, 메모리 20블록): 3 × (100 + 400) = 1,500 block transfers

### 각 알고리즘의 강점

- **Nested-Loop Join**: 구현 단순, 모든 join 조건 지원, 내부 릴레이션이 메모리에 들어오면 O(N/B)로 단순화
- **Block Nested-Loop Join**: buffer 활용도 개선; LRU 교체 정책과 결합 시 inner 블록 재활용 가능
- **Indexed Nested-Loop Join**: 이미 존재하는 B+-tree index를 활용하면 join을 위한 별도 정렬 불필요; equi-join에서 O(N log_B N) 달성
- **Merge-Join**: 두 릴레이션이 이미 정렬된 경우 추가 비용 없이 O(N/B) 달성; hybrid merge-join으로 한쪽 릴레이션이 B+-tree를 가질 때도 효율적 처리 가능
- **Hash-Join**: 사전 정렬 불필요, 대용량 비정렬 릴레이션에서 O(N/B) 달성, 병렬 처리에 자연스럽게 적합

## Counterevidence

- Hash join과 merge-join은 equi-join에만 적용 가능; inequality join (A > B, A != B)은 nested-loop 또는 정렬 후 merge-join만 지원
- Merge-join은 정렬되지 않은 릴레이션에 [[external-merge-sort]] 비용 O((N/B) log_{M/B}(N/B))가 추가되나, 이후 다른 연산도 정렬된 입력을 필요로 한다면 정렬 비용이 분산됨
- Indexed nested-loop join은 인덱스 구축 비용이 있으나 이미 존재하는 인덱스 활용 시 hash join보다 우수할 수 있음
- Hash join은 partition skew가 심각하거나 대량 중복값이 존재하는 경우 overflow로 인해 block nested-loop join으로 fallback 필요
- 메모리가 충분히 크다면 (내부 릴레이션 전체 적재 가능) 단순 nested-loop join조차 O(N/B)로 동작하므로 복잡한 알고리즘 불필요

## Conclusion

실무 query optimizer의 알고리즘 선택 기준:

| 상황 | 권장 알고리즘 |
|------|-------------|
| Inner relation에 B+-tree index 존재 | Indexed nested-loop join |
| 두 릴레이션이 이미 join attribute로 정렬됨 | Merge-join (정렬 비용 없음) |
| 대용량 비정렬 릴레이션, equi-join | Hash-join (build input으로 작은 릴레이션 선택) |
| Inequality join (>, <, !=) | Nested-loop join 또는 sort 후 merge-join |
| 내부 릴레이션이 메모리에 완전히 적재 가능 | Nested-loop join (O(N/B)로 단순화) |

Hash-join이 범용 최적이라는 인식이 있으나, 인덱스가 존재하거나 이미 정렬된 경우에는 indexed nested-loop 또는 merge-join이 우위를 가질 수 있다. 실제 query optimizer는 이러한 cost estimate를 database catalog 통계와 결합하여 최적 plan을 자동 선택한다.

## Sources

- raw/데이터베이스/Query Processing.pdf
