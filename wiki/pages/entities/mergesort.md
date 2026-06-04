---
title: Mergesort
category: entity
tags: [sort, algorithm, comparison-sort, divide-and-conquer]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Mergesort(병합 정렬)는 [[divide-and-conquer]] 패러다임을 사용하는 비교 기반 정렬 알고리즘이다. 배열을 중간 인덱스를 기준으로 절반씩 재귀적으로 분할하고, 두 정렬된 부분 배열을 병합(merge)하여 전체를 정렬한다.

**핵심 서브루틴 `merge(A, B, C)`**: 두 정렬된 시퀀스 A, B를 하나의 정렬된 시퀀스 C로 합친다. A의 첫 원소와 B의 첫 원소를 비교하여 작은 것을 C의 앞에 배치하는 과정을 재귀적으로 반복한다.

    merge(A, B, C):
      if A is empty: rest of C = rest of B
      else if B is empty: rest of C = rest of A
      else if first(A) ≤ first(B):
        first(C) = first(A); merge(rest(A), B, rest(C))
      else:
        first(C) = first(B); merge(A, rest(B), rest(C))

**재귀 관계식**:
- W(1) = 0
- W(n) = 2·W(n/2) + W_merge(n), W_merge(n) = n - 1
- W(n) ∈ θ(n log n)

## Capabilities

- **Guaranteed worst-case**: θ(n log n) — 항상 균등하게 n/2씩 분할하기 때문에 불균형이 발생하지 않음
- **Merge 단계 비교 횟수**: W_merge(n) = n - 1 (두 시퀀스를 한 번씩 순회)
- 안정 정렬(stable sort)로 구현하기 용이하다 (동일 키 원소의 상대 순서 보존)

## Limitations

- **추가 메모리 필요**: merge 과정에서 O(n) 추가 공간이 요구되어 진정한 in-place 구현이 어렵다.
- [[quick-sort]]에 비해 실용적 상수 인자가 클 수 있다 — 캐시 효율 측면에서 불리할 수 있음.
- Divide 단계는 trivial(단순 인덱스 계산)하지만, Combine(merge) 단계가 복잡도를 결정한다.

## Relationships

- [[divide-and-conquer]]: Mergesort의 핵심 설계 패러다임; 균등 분할(n/2)이 θ(n log n) 보장의 근거
- [[quick-sort]]: 둘 다 분할 정복 기반이나, Quick-Sort는 Divide가 복잡(pivot 선택·파티셔닝)하고 Combine이 trivial한 반면, Mergesort는 그 반대
- [[heapsort]]: 동일하게 worst case θ(n log n)(혹은 2n log n) 범주이나 메모리 사용 방식이 다름
- [[sorting-algorithm-comparison]]: worst case가 θ(n log n)으로 보장되는 비교 기반 정렬로 비교 분석

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.18–21)
