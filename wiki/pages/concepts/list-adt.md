---
title: List ADT (Doubly Linked List 구현)
category: concept
tags: [list, doubly-linked-list, data-structure, adt, node]
sources: [raw/자료구조/CSE2112_02_week05_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

List ADT는 요소를 Position으로 참조하는 추상 자료형이다. 이중 연결 리스트(Doubly Linked List)로 자연스럽게 구현되며, 각 노드(Node)는 요소 값(`elem`), 이전 노드 포인터(`prev`), 다음 노드 포인터(`next`)를 저장한다. 리스트 양 끝에는 실제 데이터를 갖지 않는 sentinel 노드인 `header`와 `trailer`를 배치하여 경계 조건 처리를 단순화한다.

## How It Works

**Node 구조**:
```cpp
class Node {
  int elem;
  Node* prev;
  Node* next;
};
```

**List 초기화**: 생성자에서 `header->next = trailer`, `trailer->prev = header`로 연결하여 빈 리스트를 구성한다. `n = 0`으로 초기화.

**핵심 연산**:
- `insert(p, e)`: position p 앞에 새 노드를 삽입. 신규 노드의 prev/next와 인접 노드의 포인터 4개를 재연결 → O(1)
- `erase(p)`: position p의 노드를 제거. 앞뒤 노드의 포인터를 서로 연결 후 해당 노드 메모리 해제 → O(1)
- `insertFront(e)` / `insertBack(e)`: `insert(begin(), e)` / `insert(end(), e)`로 위임
- `removeFront()` / `removeBack()`: `erase(begin())` / `erase(--end())`로 위임

**탐색**: [[iterator]] 객체를 반환하는 `begin()`(header 다음 노드)과 `end()`(trailer)를 통해 순회한다.

## Key Properties

- 요소 참조 방식: Position ([[iterator]] 객체)
- 삽입/삭제: O(1) — position을 이미 알고 있을 때
- 임의 위치 접근: O(n) — 처음부터 순차 탐색 필요
- 공간 복잡도: O(n) — 실제 요소 수만큼만 노드 할당
- sentinel 노드(header, trailer)로 경계 예외 처리 불필요
- 비연속 메모리 배치로 cache locality 불리

## Relationships

- [[iterator]] (List 탐색 및 position 표현에 사용되는 Iterator)
- [[array-based-vector]] (대안적 구현 — 인덱스 기반, 연속 배열 사용)
- [[vector-vs-list]] (두 구현의 시간·공간 복잡도 비교)
- [[sequence-adt]] (List에 index 접근을 추가하면 Sequence ADT가 됨)

## Open Questions

- `header`와 `trailer` sentinel 노드를 사용하지 않을 경우 insert/erase 코드가 얼마나 복잡해지는가?
- 단일 연결 리스트(Singly Linked List)와 비교해 이중 연결 리스트의 추가 포인터 메모리 비용은 언제 정당화되는가?
- `removeBack()`에서 `--end()`를 사용하는 것이 안전한 이유는 trailer sentinel의 존재 때문인가?

## Sources

- raw/자료구조/CSE2112_02_week05_2.pdf (Week 05 Lecture 02, slides 10, 12–25)
