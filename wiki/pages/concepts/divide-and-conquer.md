---
title: Divide and Conquer
category: concept
tags: [algorithm, paradigm, recursion, divide-and-conquer]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Divide and Conquer(분할 정복)는 큰 문제를 동일한 유형의 더 작은 부분 문제들로 분할(Divide)하고, 각각을 재귀적으로 해결(Conquer)한 뒤, 부분 해를 결합(Combine)하여 원래 문제의 해를 도출하는 알고리즘 설계 패러다임이다.

## How It Works

알고리즘의 일반적인 구조:

    solve(I)
      n = size(I)
      if (n ≤ smallsize)
        solution = directlySolve(I)
      else
        I를 I1, …, Ik로 분할
        for each i in {1, …, k}
          Si = solve(Ii)
        solution = combine(S1, …, Sk)
      return solution

1. **Divide**: 입력 문제 I를 더 작은 부분 문제 I1, ..., Ik로 나눈다.
2. **Conquer**: 각 부분 문제를 재귀적으로 해결한다. 크기가 충분히 작으면 직접 해결(base case).
3. **Combine**: 부분 해 S1, ..., Sk를 결합하여 원래 문제의 해를 구성한다.

## Key Properties

- 재귀적 구조를 가지며, 부분 문제는 원래 문제와 동일한 유형이다.
- Base case(기저 사례)가 반드시 존재해야 무한 재귀를 방지할 수 있다.
- 부분 문제들이 독립적(non-overlapping)일 때 가장 효과적이다. 부분 문제가 겹치는 경우에는 Dynamic Programming이 더 적합하다.
- 시간 복잡도는 재귀 관계식(recurrence relation)으로 분석하며, Master Theorem 등을 통해 closed form을 유도한다.
- Combine 단계의 비용이 전체 복잡도를 좌우하는 경우가 많다 (예: Mergesort의 merge 단계).

## Relationships

- [[quick-sort]]: pivot을 기준으로 입력을 L/E/G로 분할하는 분할 정복 정렬 알고리즘
- [[mergesort]]: 배열을 균등하게 절반으로 분할하고 병합하는 분할 정복 정렬 알고리즘
- [[heapsort]]: constructHeap과 fixHeapFast 내부에서 분할 정복을 활용
- [[sorting-algorithm-comparison]]: 분할 정복 기반 알고리즘들의 복잡도 비교 분석

## Open Questions

- 분할이 불균형할 경우(예: Quick-Sort worst case) 성능이 O(n²)으로 저하된다. 항상 균형 잡힌 분할을 보장하는 범용적 방법이 존재하는가?
- 분할 정복과 Dynamic Programming의 경계를 overlapping subproblems의 정도로 어떻게 정량적으로 구분할 수 있는가?

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.11, 20, 29–30, 33)
