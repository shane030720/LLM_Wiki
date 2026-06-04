---
title: Red-Black Tree
category: entity
tags: [tree, data-structure, balanced-tree, search, algorithm]
sources: [raw/알고리즘/CH06 동적 집합과 탐색.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

Red-Black Tree(레드-블랙 트리)는 각 노드에 Red 또는 Black 색상을 부여하는 4가지 속성으로 균형을 자동 유지하는 이진 탐색 트리다. n개의 항목을 저장할 때 높이가 O(log n)임이 보장되므로, 탐색·삽입·삭제 모두 최악의 경우에도 O(log n) 시간을 달성한다.

## Capabilities

**4가지 Red-Black 속성:**

1. **Root Property:** 루트 노드는 반드시 Black이다.
2. **External Property:** 모든 리프(빈 트리, nil 노드)는 Black이다.
3. **Internal Property:** Red 노드의 자식은 반드시 Black이다 (Red 노드가 연속으로 이어질 수 없음).
4. **Depth Property:** 모든 리프는 동일한 Black Depth를 가진다.

**탐색:** BST와 동일한 알고리즘을 사용하며, 높이 보장에 의해 O(log n)이다.

**삽입 알고리즘 (3단계):**

1. BST 삽입 알고리즘으로 삽입 위치 z를 찾는다 — O(log n)
2. 노드 z를 Red로 색칠한다 (루트인 경우 Black 유지) — O(1)
3. Double Red(Internal Property 위반) 발생 시 아래 두 경우로 처리한다 — O(log n)

| 상황 | 해결 기법 | 효과 |
|------|-----------|------|
| 형제 노드 w가 **Black** | Restructuring (회전) | Internal Property 복원, 전파 없음 |
| 형제 노드 w가 **Red** | Recoloring (재색칠) | v, w → Black / 조부모 u → Red, 위로 전파 가능 |

**Restructuring:** 4가지 회전 구성(LL, LR, RL, RR)이 존재하며 각 O(1)이다. 한 번만 수행된다.

**Recoloring:** O(log n)회 반복될 수 있으나 각 O(1)이므로 전체 O(log n)이다.

## Limitations

- 삽입 시 최대 O(log n)회의 Recoloring이 필요하여 구현이 [[binary-search-tree]]보다 복잡하다.
- 삭제 연산은 삽입보다 더 많은 경우의 수를 처리해야 한다 (본 자료에서는 다루지 않음).
- 포인터 조작과 색상 관리로 인해 상수 계수(constant factor)가 단순 BST보다 크다.

## Relationships

- [[binary-search-tree]] (레드-블랙 트리가 확장하는 기반 자료구조로, BST Property를 그대로 유지함)
- [[amortized-analysis]] (삽입 연산의 Recoloring 비용 분석에 상각 분석 관점 적용 가능)

## Sources

- raw/알고리즘/CH06 동적 집합과 탐색.pdf
