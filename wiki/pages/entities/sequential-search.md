---
title: Sequential Search (순차 탐색)
category: entity
tags: [algorithm, search, linear-search, array, optimality]
sources: [raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

Sequential Search(순차 탐색, 선형 탐색)는 배열의 원소를 처음부터 순서대로 목표값 K와 비교하여 탐색하는 알고리즘이다. 비정렬(unordered) 배열과 정렬(ordered) 배열 모두에 적용 가능하며, 정렬 배열에서는 조기 종료(early termination)를 활용한 변형(Modified Sequential Search)으로 평균 성능을 개선한다. 비정렬 배열 탐색 문제에 대해서는 이론적으로 최적(optimal)임이 증명된 알고리즘이다.

**기본 알고리즘 (비정렬/정렬 배열 공통)**:
```
int seqSearch(int[] E, int n, int K)
  ans = -1;
  for (index = 0; index < n; index++)
      if (K == E[index])
          ans = index; break;
  return ans;
```

**Modified Sequential Search (정렬 배열 전용)**:
```
int seqSearchMod(int[] E, int n, int K)
  ans = -1;
  for (index = 0; index < n; index++)
      if (K > E[index]) continue;
      if (K < E[index]) break;
      // K == E[index]
      ans = index; break;
  return ans;
```

## Capabilities

**비정렬 배열 탐색 (Algorithm A)**:
- Basic operation: K와 배열 원소의 비교
- W(n) = n (K가 마지막 위치에 있거나 배열에 없는 경우)
- A(n) = q·(n+1)/2 + (1-q)·n (q: 탐색 성공 확률)
  - 성공 시 Asucc(n) = (n+1)/2, 실패 시 Afail(n) = n
- **최적성**: 비정렬 배열 탐색의 하한 F(n) = n이므로 이 알고리즘은 최적이다.

**정렬 배열 탐색 — Modified Sequential Search (Algorithm C)**:
- 배열이 정렬되어 있음을 이용하여, K보다 큰 원소 발견 즉시 탐색 실패(-1)를 반환하는 조기 종료 전략 적용
- W(n) = n + 1 ≈ n (최악의 경우 정렬 정보가 거의 활용되지 않음)
- A(n) ≈ n/2 (비정렬 대비 평균 성능 향상)
  - 성공 시 Asucc(n) = (n+1)/2
  - 실패 시 Afail(n) ≈ n/2 (n+1개의 실패 구간에 균등 분포 가정)

## Limitations

- Worst-case가 Θ(n)으로, 대규모 정렬 배열 탐색에서 [[binary-search]]의 Θ(log n)에 비해 비효율적이다.
- Modified Sequential Search도 worst-case는 O(n)으로 정렬 배열에서 비교 기반 최적 알고리즘이 아니다.
- 정렬 배열에서 배열의 정렬 정보를 최악의 경우에 충분히 활용하지 못한다.

## Relationships

- [[algorithm-analysis]] — worst-case W(n) = n, average-case A(n) 분석의 기본 예시이자 최적성 증명 사례
- [[asymptotic-notation]] — W(n) ∈ Θ(n)으로 분류됨
- [[binary-search]] — 동일한 정렬 배열 탐색 문제를 Θ(log n)으로 해결하는 최적 개선 알고리즘

## Sources

- raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf
