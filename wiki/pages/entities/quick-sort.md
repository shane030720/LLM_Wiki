---
title: Quick-Sort
category: entity
tags: [sort, algorithm, comparison-sort, divide-and-conquer, randomized]
sources: [raw/알고리즘/CH04 정렬.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Quick-Sort(퀵 정렬)는 [[divide-and-conquer]] 패러다임에 기반한 랜덤화 비교 정렬 알고리즘이다. 임의로 선택한 pivot 원소를 기준으로 입력을 세 파티션으로 분할하고, 두 파티션을 재귀적으로 정렬한 뒤 합친다.

**분할 결과**:
- L: pivot보다 작은 원소들
- E: pivot과 같은 원소들
- G: pivot보다 큰 원소들

**In-place Partitioning**: 두 인덱스 j(왼쪽에서 오른쪽 스캔, pivot보다 큰 원소 탐색)와 k(오른쪽에서 왼쪽 스캔, pivot보다 작은 원소 탐색)를 사용하여 교환을 반복한다. j와 k가 교차하면 종료.

## Capabilities

- **Partition 단계 복잡도**: O(n) — 각 원소를 한 번씩 처리하므로
- **Average-case 복잡도**: O(n log n) — 랜덤 pivot 선택으로 균형 잡힌 분할을 기대
- **In-place 구현 가능**: 추가 메모리 없이 두 인덱스만으로 파티셔닝 가능
- **Combine 단계**: trivial — L, E, G를 순서대로 이어 붙이기만 하면 됨

## Limitations

- **Worst-case 복잡도**: O(n²) — pivot이 최솟값 또는 최댓값일 때 발생
  - 한쪽 파티션 크기 n-1, 다른 쪽 크기 0이 되어 재귀 깊이가 n-1까지 증가
  - 총 비교 횟수: n + (n-1) + ... + 2 + 1 = n(n+1)/2
- 랜덤화로 평균 성능은 보장하지만 최악의 경우를 완전히 배제할 수 없다.

## Relationships

- [[divide-and-conquer]]: Quick-Sort가 채택하는 핵심 설계 패러다임; Divide 단계가 핵심이고 Combine이 trivial한 것이 특징
- [[mergesort]]: 동일하게 분할 정복 기반이나, Mergesort는 Divide가 균등·trivial하고 Combine(merge)이 핵심
- [[heapsort]]: 둘 다 worst case보다 실용적 성능이 중요하지만, Heapsort는 worst case를 2n log n으로 보장
- [[sorting-algorithm-comparison]]: 실용적으로 빠르지만 worst case를 보장하지 못하는 알고리즘으로 비교

## Sources

- raw/알고리즘/CH04 정렬.pdf (pp.12–16)
