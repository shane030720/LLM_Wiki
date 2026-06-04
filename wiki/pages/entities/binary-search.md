---
title: Binary Search (이진 탐색)
category: entity
tags: [algorithm, search, divide-and-conquer, sorted-array, optimality, decision-tree]
sources: [raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

Binary Search(이진 탐색)는 정렬된(non-decreasing order) 배열에서 분할 정복(Divide-and-Conquer) 전략을 사용하여 목표값 K를 탐색하는 재귀 알고리즘이다. 배열의 중간(mid) 원소와 K를 비교하여 탐색 범위를 절반씩 줄여나가며, 결정 트리(decision tree) 논증을 통해 비교 기반 탐색 알고리즘 클래스에서 최적(optimal)임이 이론적으로 증명된 알고리즘이다.

```
int binarySearch(int[] E, int first, int last, int K)
  if (last < first)
      return -1;
  int mid = (first + last) / 2;
  if (K == E[mid])
      return mid;
  else if (K < E[mid])
      return binarySearch(E, first, mid-1, K);
  else
      return binarySearch(E, mid+1, last, K);
```

## Capabilities

**Worst-Case Complexity**:
- W(n) = ⌊log n⌋ + 1 ∈ Θ(log n)
- 재귀 호출마다 탐색 범위가 절반으로 줄어들어 n/(2^d) ≥ 1을 만족하는 최대 깊이 d ≤ lg(n)번의 재귀 비교와 최초 1번의 비교를 합산한다.

**Average-Case Complexity**:
- A(n) ≈ lg(n+1) − q (q: 탐색 성공 확률)
- 성공 시: Asucc(n) = lg(n+1) − 1 + lg(n+1)/n
- 실패 시: Afail(n) = lg(n+1)
- n = 2^d − 1로 놓으면, 깊이 t에 해당하는 그룹 St의 크기 st = 2^{t-1}이며, Asucc(n) = Σ_{t=1}^{d} t·(st/n)으로 계산된다.

**최적성 증명 (Decision Tree 논증)**:
- Basic operation이 비교(comparison)인 알고리즘 클래스에서 하한을 결정 트리로 증명한다.
- 결정 트리의 각 노드는 비교 대상 배열 인덱스에 대응하며, 올바른 알고리즘의 결정 트리는 반드시 n개 이상의 노드를 포함해야 한다. (노드 i가 없으면, E[i]=K인 경우와 E[i]≠K인 경우를 구별하지 못해 모순 — proof by contradiction)
- 깊이 p인 이진 트리의 노드 수 N ≤ 2^p − 1이므로, 2^p ≥ N+1 ≥ n+1, 따라서 p ≥ log(n+1).
- 즉, 어떤 비교 기반 알고리즘도 최악의 경우 ⌈log(n+1)⌉번 이상의 비교를 반드시 수행해야 한다.
- Binary Search의 W(n) = ⌊log n⌋ + 1 = ⌈log(n+1)⌉이므로, Binary Search는 최적이다.

**개선 과정 요약**:
- 비정렬 배열 탐색 (Algorithm A): W(n) = n ∈ Θ(n) — 해당 문제에서 최적
- 정렬 배열 + Sequential Search (Algorithm B): W(n) = n ∈ Θ(n) — 정렬 정보 미활용
- 정렬 배열 + Modified Sequential Search (Algorithm C): W(n) ≈ n ∈ Θ(n), A(n) ≈ n/2 — 평균 성능 개선
- 정렬 배열 + Binary Search (Algorithm D): W(n) ∈ Θ(log n) — 비교 기반 최적

## Limitations

- 배열이 반드시 정렬(sorted)되어 있어야 한다. 정렬 비용(Θ(n log n))을 포함하면 단일 탐색에는 순차 탐색이 유리할 수 있다.
- 연결 리스트(linked list)처럼 임의 접근(random access)이 불가한 자료구조에는 직접 적용할 수 없다.
- 재귀 구현 시 호출 스택(call stack) 공간을 O(log n) 사용한다.
- 비교 횟수 측면에서 최적이나, 실제 캐시 접근 패턴 등 하드웨어 특성에서는 순차 접근 기반 알고리즘이 유리할 수 있다.

## Relationships

- [[algorithm-analysis]] — worst-case, average-case, 최적성 분석의 대표적 심화 예시; 결정 트리 기반 하한 증명
- [[asymptotic-notation]] — W(n) ∈ Θ(log n)으로 분류됨
- [[sequential-search]] — 동일 정렬 배열 탐색 문제를 Θ(n)에 해결하는 알고리즘; Binary Search가 점근적으로 우월함

## Sources

- raw/알고리즘/CH01 알고리즘과 문제의 분석 (2).pdf
