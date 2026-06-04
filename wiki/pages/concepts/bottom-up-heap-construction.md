---
title: Bottom-up Heap Construction
category: concept
tags: [heap, algorithm, construction, optimization]
sources: [raw/자료구조/CSE2112_02_week10_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Bottom-up heap construction은 n개의 주어진 키로부터 [[heap]]을 O(n) 시간에 구성하는 알고리즘이다. n번의 연속적인 insert 연산(O(n log n))보다 점근적으로 우월하며, [[heap-sort]]의 Phase 1(힙 구성 단계)을 가속하는 데 직접 활용된다.

## How It Works

총 log n개의 **phase**로 진행되며, 작은 힙들을 점진적으로 병합하여 하나의 완전한 힙을 완성한다.

### Phase 구조

- **Phase i**: 2^i - 1개의 키를 가진 힙 쌍(pair)들을 2^(i+1) - 1개의 키를 가진 힙으로 각각 병합

### 두 힙의 병합 (Merging Two Heaps)

두 힙 H1, H2와 새 키 k가 주어질 때:
1. k를 루트로 하고 H1, H2를 각각 왼쪽, 오른쪽 서브트리로 하는 새 트리를 구성한다.
2. heap-order 속성 복원을 위해 루트에서 **downheap**을 수행한다.

### 예시 (8개 키: 16, 15, 4, 12, 6, 9, 23, 20)

```
Phase 1 (단일 원소 쌍 병합):
  (16,15) → 15/16    (4,12) → 4/12    (6,9) → 6/9    (23,20) → 20/23

Phase 2 (크기 3짜리 힙 병합, 키 5와 25를 루트로):
  5 + {15/16, 4/12} → downheap → 4/{5/16, 15/12} 형태
  ...

Phase 3 (최종 병합):
  전체 힙 완성, downheap 적용
```

### 시간 복잡도 분석 (Proxy Path 방법)

각 downheap의 worst-case 경로를 **proxy path**로 시각화한다: 루트에서 먼저 오른쪽으로 한 번 이동한 뒤 계속 왼쪽으로 내려가는 경로로 bound한다.

- 각 노드는 최대 2개의 proxy path에 의해 탐색됨
- 따라서 모든 proxy path의 총 노드 수 ≤ 2n = O(n)
- 수식으로 표현:

```
n/2 × 0 + n/4 × 1 + n/8 × 2 + ... + 1 × log n = O(n)
```

## Key Properties

- **시간 복잡도**: O(n) — n번 연속 insert의 O(n log n)보다 점근적으로 우월
- **공간 복잡도**: O(n)
- 각 병합 단계의 핵심 연산은 downheap이며, upheap은 사용하지 않음
- [[heap-sort]]의 Phase 1에 적용 시 첫 단계를 O(n log n)에서 O(n)으로 단축
- 배치(batch) 구성이 가능한 경우에만 적용 가능 (초기 키들이 모두 주어진 상황)

## Relationships

- [[heap]] (구성 대상 자료구조; downheap을 반복적으로 활용)
- [[heap-sort]] (bottom-up construction으로 Phase 1을 가속할 수 있음)

## Open Questions

- O(n) 점근 복잡도에도 불구하고, 작은 n에서는 상수 인자(constant factor) 때문에 n번 insert보다 느릴 수 있다. 실제 crossover point는 어느 정도인가?
- 동적으로 원소가 추가되는 온라인(online) 시나리오에서는 bottom-up construction을 직접 활용할 수 없다. 이런 환경에서 힙을 효율적으로 유지하는 최선의 전략은?
- Proxy path 분석은 worst-case bound를 O(n)으로 증명하지만, 실제 downheap의 평균 경로 길이는 이보다 짧을 수 있다. 평균 케이스 분석 결과는?

## Sources

- raw/자료구조/CSE2112_02_week10_2.pdf
