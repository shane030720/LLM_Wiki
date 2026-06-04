---
title: Binary Search Tree
category: concept
tags: [bst, tree, data-structure, search, map]
sources: [raw/자료구조/CSE2112_02_week11_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Binary Search Tree(이진 탐색 트리, BST)는 각 내부 노드 v에 대해 왼쪽 서브트리의 모든 키가 v의 키보다 작거나 같고, 오른쪽 서브트리의 모든 키가 v의 키보다 크거나 같은 이진 트리이다. 이 BST 속성 덕분에 탐색·삽입·삭제를 트리 높이 h에 비례한 시간에 수행할 수 있다.

## How It Works

### In-order Traversal
왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리 순으로 방문하면 키가 오름차순으로 나열된다. 즉 key(u) ≤ key(v) ≤ key(w) (u: v의 왼쪽, w: v의 오른쪽).

### Search (find)
루트에서 시작해 아래 방향으로 경로를 추적한다.

```
Algorithm TreeSearch(k, v):
  if v.isExternal(): return v          // 리프 도달 → 키 없음
  if k < v.key():  return TreeSearch(k, v.left())
  else if k = v.key(): return v        // 탐색 성공
  else:            return TreeSearch(k, v.right())
```

반복적(iterative) 구현에서는 root에서 시작해 nullptr에 도달할 때까지 비교를 반복하며, 일치하면 해당 Node* 반환, 아니면 nullptr 반환한다.

### Insertion (put)
TreeSearch로 key k를 탐색하여 탐색이 끝나는 리프(외부 노드) w에 새 노드를 삽입하고 내부 노드로 확장한다. 이미 존재하는 key이면 삽입하지 않고 false를 반환한다.

### Deletion (erase)
삭제 대상 노드 v를 탐색한 뒤 두 경우로 처리한다.

- **Case 1 — v의 자식 중 하나가 리프(외부 노드)인 경우**: v와 해당 리프 자식 w를 함께 제거(removeExternal(w)).
- **Case 2 — v의 두 자식이 모두 내부 노드인 경우**: In-order successor w(v 다음으로 큰 키를 가진 내부 노드)를 찾아 key(w)와 value(w)를 v에 복사한 뒤, w와 w의 왼쪽 리프 자식 z를 removeExternal(z)로 제거한다.

삭제 후 남은 단일 자식(child_node)을 부모 노드에 연결하고 노드를 메모리에서 해제한다.

## Key Properties
- BST 속성: 왼쪽 서브트리 키 ≤ 현재 키 ≤ 오른쪽 서브트리 키
- 공간 복잡도: O(n)
- find, put, erase 모두 O(h) 시간 (h = 트리 높이)
- 최선의 경우 h = O(log n) (균형 트리), 최악의 경우 h = O(n) (편향 트리)
- 삽입·삭제 후 균형이 자동으로 유지되지 않음

## Relationships
- [[map-adt]] (BST가 구현하는 추상 자료형)
- [[avl-tree]] (BST에 높이 균형 조건을 추가한 자기 균형 변형; 최악 O(log n) 보장)
- [[hash-table]] (Map의 대안 구현체; 정렬 순서 미보장, 평균 O(1))
- [[map-implementation-comparison]] (세 구현체 성능 비교 분석)

## Open Questions
- 최악의 경우 O(n)을 어떻게 피할 수 있는가? → [[avl-tree]] 참조
- In-order successor(get_successor) 탐색의 구체적 구현 방법은 강의 자료에 명시되지 않음
- 중복 키 처리 정책(허용 여부, 처리 방식)은 구현에 따라 달라짐

## Sources
- raw/자료구조/CSE2112_02_week11_2.pdf
