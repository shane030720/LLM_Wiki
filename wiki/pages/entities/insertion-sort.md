---
title: Insertion Sort
category: entity
tags: [sort, algorithm, comparison-sort, in-place]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Insertion Sort(삽입 정렬)는 배열의 각 원소를 이미 정렬된 부분 배열의 적절한 위치에 삽입하는 단순한 비교 기반 정렬 알고리즘이다. 첫 번째 원소를 정렬된 세그먼트로 간주하고, 이후 원소를 하나씩 올바른 위치에 삽입해 나간다.

핵심 서브루틴 `shiftVacRec`는 삽입 위치를 재귀적으로 탐색하면서 원소들을 한 칸씩 오른쪽으로 밀어낸다:

    shiftVacRec(E, vacant, x):
      if vacant == 0: return 0
      else if E[vacant-1].key ≤ x: return vacant
      else:
        E[vacant] = E[vacant-1]
        return shiftVacRec(E, vacant-1, x)

## Capabilities

- **In-place 정렬**: 추가적인 메모리 공간을 필요로 하지 않는다.
- **Worst-case 복잡도**: θ(n²) — 역순 정렬된 입력에서 발생하며, W(n) = Σ(i=1 to n-1) i = n(n-1)/2.
- **Average-case 복잡도**: ~n²/4 비교 — 각 i에 대해 평균 비교 횟수가 약 i/2이므로 A(n) ≈ n²/4.
- **인접 원소 교환 알고리즘 중 최적**: Theorem 4.1에 의해 하한이 증명됨.

## Limitations

- Worst case와 average case 모두 O(n²)으로, 대규모 데이터에 부적합하다.
- 한 번의 비교로 최대 1개의 inversion(역전 쌍)만 제거한다.
- **Theorem 4.1**: 키 비교로 정렬하며 각 비교 후 최대 1개의 inversion을 제거하는 알고리즘은 worst case에서 최소 n(n-1)/2번, average에서 최소 n(n-1)/4번 비교를 수행해야 한다. 즉, 동작 방식 자체가 이 하한에 묶여 있다.
- "locally"(인접 원소만 교환)하게 동작하는 알고리즘 중 최적이지만, 전체 정렬 알고리즘 중 최선은 아니다.

## Relationships

- [[divide-and-conquer]]: 분할 정복을 사용하지 않는다는 점에서 [[quick-sort]], [[mergesort]]와 근본적으로 다른 접근 방식
- [[sorting-algorithm-comparison]]: 비교 기반 정렬 알고리즘 중 가장 단순하지만 가장 느린 알고리즘으로 비교 분석

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.4–9)
