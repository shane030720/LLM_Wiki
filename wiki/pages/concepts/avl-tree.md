---
title: AVL Tree
category: concept
tags: [avl-tree, balanced-tree, rotation, data-structure, map]
sources: [raw/자료구조/CSE2112_02_week11_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
AVL Tree는 Adel'son-Vel'ski와 Landis가 고안한 자기 균형 이진 탐색 트리(self-balancing BST)이다. 모든 내부 노드 v에 대해 두 자식의 높이 차이가 최대 1인 **높이 균형 속성(Height-Balance Property)**을 유지함으로써 트리 높이를 항상 O(log n)으로 보장한다.

## How It Works

### Height-Balance Property
모든 내부 노드 v에 대해 |height(v.left) - height(v.right)| ≤ 1을 만족해야 한다. 이 조건이 위반된 노드를 "unbalanced node"라 한다.

### Insertion
1. 일반 BST 삽입과 동일하게 외부 노드를 확장하여 새 키를 삽입한다.
2. 삽입 후 높이가 증가하면서 균형이 깨진 첫 번째 조상 노드 z를 탐색한다.
3. Trinode Restructuring으로 균형을 복원한다. 삽입의 경우 단 1회의 restructuring으로 전체 균형이 복원된다.

### Trinode Restructuring
불균형 노드 z, z의 무거운 쪽(높이가 큰) 자식 y, y의 무거운 쪽 자식 x를 in-order 순서로 (a, b, c)로 나열한 뒤 b를 세 노드의 최상위 노드로 만든다.

- **Case 1 (b = y): Single Rotation**
  - z에 대해 왼쪽 회전(left rotation)
  - y가 새 루트, a(=z)는 y의 왼쪽 자식, c(=x)는 y의 오른쪽 자식
  - 서브트리 T0, T1은 a 아래, T2, T3는 c 아래 재배치

- **Case 2 (b = x): Double Rotation**
  - c(=y)에 대해 오른쪽 회전 후 a(=z)에 대해 왼쪽 회전
  - x가 새 루트, a(=z)는 x의 왼쪽 자식, c(=y)는 x의 오른쪽 자식

두 경우 모두 restructuring 후 서브트리 루트의 높이가 삽입 전과 동일해져 상위 노드의 균형은 자동으로 유지된다.

### Removal
1. 일반 BST 삭제와 동일하게 수행하여 빈 외부 노드를 생성한다.
2. 삭제된 노드의 부모 w에서 루트 방향으로 올라가며 첫 번째 불균형 노드 z를 탐색한다.
3. z의 높이가 더 큰 자식 y, y의 높이가 더 큰 자식 x를 찾아 restructure(x)를 수행한다.
4. 삭제는 단 1회의 restructuring으로 부족할 수 있어, 루트에 도달할 때까지 균형 확인을 반복한다.

## Key Properties
- 높이 균형 속성: 모든 내부 노드에서 자식 높이 차이 ≤ 1
- 트리 높이: 항상 O(log n) 보장 (최악의 경우 포함)
- Single restructure 비용: O(1) (linked-structure binary tree 기준)
- find: O(log n) — restructuring 불필요
- put: O(log n) — 초기 탐색 O(log n) + 최대 1회 restructuring
- erase: O(log n) — 초기 탐색 O(log n) + 루트까지 restructuring O(log n)
- 삽입은 1회 restructuring으로 충분, 삭제는 여러 번 필요할 수 있음

## Relationships
- [[binary-search-tree]] (AVL Tree가 확장한 기반 자료구조; BST 속성 상속)
- [[map-adt]] (AVL Tree가 구현하는 추상 자료형)
- [[hash-table]] (Map 대안 구현체; 평균 O(1) vs AVL O(log n))
- [[map-implementation-comparison]] (세 구현체 성능 비교 분석)

## Open Questions
- Red-Black Tree 등 다른 자기 균형 BST 대비 AVL Tree의 장단점은?
- 삭제 후 여러 번의 restructuring이 필요한 구체적 조건과 최대 횟수는?
- 실용적인 구현에서 높이 정보를 노드에 저장하는 방식과 갱신 비용은?

## Sources
- raw/자료구조/CSE2112_02_week11_2.pdf
