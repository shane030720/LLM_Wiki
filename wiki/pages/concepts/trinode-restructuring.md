---
title: Trinode Restructuring
category: concept
tags: [tree, avl-tree, rotation, balancing, algorithm]
sources: [raw/자료구조/CSE2112_02_week11_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Trinode Restructuring은 AVL 트리에서 불균형이 발생했을 때 세 노드 (x, y, z)를 재배치하여 높이 균형 속성(height-balance property)을 복원하는 국소적 재구조화 연산이다. 단일 회전(single rotation) 또는 이중 회전(double rotation) 중 하나를 선택적으로 적용하며, 연산 후 세 노드 중 중간값 노드 b가 해당 서브트리의 루트가 된다.

## How It Works

**노드 선택 (Node Selection)**

삽입 또는 삭제 후 루트 방향으로 올라가면서 다음 순서로 세 노드를 식별한다.

- z: 불균형이 처음 발생한 조상 노드 (first unbalanced ancestor)
- y: z의 자식 중 높이가 더 큰 쪽 (child of z on heavy path)
- x: y의 자식 중 높이가 더 큰 쪽 (child of y on heavy path)

그리고 (x, y, z)를 in-order 순서로 나열하여 (a, b, c)를 얻는다.

**목표: b를 세 노드의 서브트리 루트로 만든다.**

**Case 1 — b = y (단일 회전, Single Rotation)**

z → y → x 경로가 일직선(같은 방향)일 때 발생한다.

- z에 대해 단일 회전(left rotation 또는 right rotation) 적용
- y가 서브트리의 새 루트가 되고, z는 y의 자식이 된다.
- 네 서브트리 T0, T1, T2, T3가 in-order를 유지하며 재배치된다.

예시 (left rotation about z):
```
    z(a)                b(y)
   /    \    →         /    \
  T0   y(b)         a(z)   c(x)
       / \          /  \   /  \
      T1  x(c)    T0   T1 T2  T3
          / \
         T2  T3
```

**Case 2 — b = x (이중 회전, Double Rotation)**

z → y → x 경로가 꺾인(지그재그) 형태일 때 발생한다.

- y에 대해 1차 회전, 이후 z에 대해 2차 회전 적용 (방향은 경우에 따라 다름)
- x(= b)가 서브트리의 새 루트가 된다.

예시 (right rotation about y, then left rotation about z):
```
    z(a)              b(x)
   /    \    →       /    \
  T0   y(c)        a(z)   c(y)
       /  \        / \    / \
     x(b) T3      T0 T1  T2  T3
     / \
    T1  T2
```

**삽입 시 동작**

- 삽입 후 불균형이 발생한 노드를 찾아 단 한 번의 restructure로 전체 트리 균형을 복원할 수 있다.

**삭제 시 동작**

- 삭제 후 삭제된 노드의 부모 w에서 시작해 루트 방향으로 올라가며 불균형 노드 z를 찾는다.
- restructure(x)를 수행하지만, 이 연산이 상위 트리의 균형을 깨뜨릴 수 있으므로 루트에 도달할 때까지 반복적으로 확인한다.

## Key Properties

- 단일 restructure 연산은 O(1) 시간에 수행된다 (링크 기반 이진 트리 구조 사용 시).
- 삽입의 경우: 최대 한 번의 restructure로 충분하다.
- 삭제의 경우: 루트까지 O(log n)번의 restructure가 필요할 수 있다.
- In-order 순서 (a ≤ b ≤ c)는 restructure 전후로 항상 보존된다.
- Case 1(단일 회전)과 Case 2(이중 회전)는 각각 좌/우 대칭 형태가 존재하므로 총 4가지 구성이 있다.
- 연산 후 서브트리의 높이는 삽입 전과 동일하게 복원된다 (삽입 경우).

## Relationships

- [[avl-tree]] — trinode restructuring이 AVL 트리의 핵심 재균형 메커니즘으로 사용됨
- [[binary-search-tree]] — AVL 트리는 BST의 확장이며, trinode restructuring은 BST 구조를 유지하면서 균형을 맞춤
- [[binary-tree-traversal]] — in-order 순서 개념이 노드 (a, b, c) 배치 결정에 사용됨
- [[red-black-tree]] — 다른 자가 균형 BST로, 다른 방식의 회전 및 색 변환으로 균형을 유지함

## Open Questions

- Trinode restructuring을 반복 적용할 때 (삭제 후 O(log n)번) 상수 계수 측면에서 red-black tree의 삭제보다 실제로 느린가?
- 메모리 효율을 위해 배열 기반 힙처럼 배열 기반 AVL 트리를 구현할 경우 trinode restructuring의 포인터 업데이트 비용은 어떻게 달라지는가?
- 삽입 시 단 한 번의 restructure로 충분하다는 것은 수학적으로 어떻게 증명되는가?

## Sources

- raw/자료구조/CSE2112_02_week11_1.pdf (p.28–36, p.40–41)
