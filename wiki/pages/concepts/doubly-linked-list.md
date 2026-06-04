---
title: Doubly Linked List
category: concept
tags: [linked-list, data-structure, list, pointer, sentinel-node]
sources: [raw/자료구조/CSE2112_02_week05_2_updated.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Doubly linked list(이중 연결 리스트)는 각 노드가 원소(element)와 함께 이전 노드를 가리키는 포인터(prev)와 다음 노드를 가리키는 포인터(next), 두 개의 링크를 저장하는 연결 리스트 자료구조다. [[list-adt]]의 자연스러운 구현체로 사용되며, 양방향 순회를 O(1)에 지원한다.

## How It Works

### Node 구조

각 노드는 세 개의 필드를 가진다.

```
+------+------+------+
| prev | elem | next |
+------+------+------+
```

C++ 구현:

```cpp
class Node {
public:
    Node(int e) : elem(e), prev(nullptr), next(nullptr) {}
private:
    int elem;   // element value
    Node* prev; // previous node
    Node* next; // next node
    friend class List;
};
```

### Header/Trailer Sentinel Node

리스트의 양 끝에 실제 원소를 저장하지 않는 sentinel node(초병 노드)인 `header`와 `trailer`를 배치한다. 이렇게 하면 삽입/삭제 시 경계 조건(맨 앞, 맨 뒤) 처리를 일반 케이스와 동일하게 처리할 수 있어 구현이 단순해진다.

```
header ↔ [node1] ↔ [node2] ↔ ... ↔ [nodeN] ↔ trailer
```

초기화:

```cpp
List::List() : n(0), header(new Node(-1)), trailer(new Node(-1)) {
    header->next = trailer;
    trailer->prev = header;
}
```

### Iterator

노드에 직접 접근하는 대신 [[iterator]] 패턴을 사용해 내부 구현을 숨기고(hiding) 위치(position)를 추상화한다. C++에서는 연산자 오버로딩으로 구현한다.

```cpp
class Iterator {
public:
    int& operator*();           // 원소에 대한 참조 반환
    bool operator==(Iterator& other);
    bool operator!=(Iterator& other);
    Iterator& operator++();     // 다음 위치로 이동
    Iterator& operator--();     // 이전 위치로 이동
private:
    Node* ref;                  // 현재 노드를 가리키는 포인터
    Iterator(Node* node);
    friend class List;
};
```

구현 예:

```cpp
int& List::Iterator::operator*() {
    return ref->elem;
}
List::Iterator& List::Iterator::operator++() {
    ref = ref->next;
    return *this;
}
List::Iterator& List::Iterator::operator--() {
    ref = ref->prev;
    return *this;
}
```

### begin() / end()

- `begin()`: header의 다음 노드를 가리키는 Iterator 반환 (첫 번째 원소)
- `end()`: trailer를 가리키는 Iterator 반환 (마지막 원소 다음의 가상 위치)

```cpp
Iterator List::begin() { return Iterator(header->next); }
Iterator List::end()   { return Iterator(trailer); }
```

### insert(p, e)

Iterator p가 가리키는 위치 앞에 새 원소 e를 삽입한다.

```cpp
void insert(Iterator p_itr, int e) {
    Node* new_node = new Node(e);
    new_node->next = p_itr.ref;
    new_node->prev = p_itr.ref->prev;
    p_itr.ref->prev->next = new_node;
    p_itr.ref->prev = new_node;
    ++n;
}
```

sentinel node 덕분에 경계 처리 없이 동일한 로직으로 맨 앞/뒤 삽입도 처리된다.

### erase(p)

Iterator p가 가리키는 노드를 제거한다.

```cpp
void erase(Iterator p_itr) {
    Node* erase_node = p_itr.ref;
    erase_node->prev->next = erase_node->next;
    erase_node->next->prev = erase_node->prev;
    delete erase_node;
    --n;
}
```

### 편의 메서드

```cpp
void insertFront(int value) { insert(begin(), value); }
void insertBack(int value)  { insert(end(), value); }
void removeFront()          { erase(begin()); }
void removeBack()           { erase(--end()); }
```

## Key Properties

- 각 노드는 prev, elem, next 세 필드를 가짐
- header와 trailer sentinel node로 경계 조건을 통합 처리
- 위치(position)가 알려진 경우 삽입/삭제 모두 O(1)
- 공간 복잡도 O(n) — 실제 원소 수에 비례 (vector의 O(N)와 달리 낭비 없음)
- 인덱스 기반 임의 접근 불가 — i번째 원소 접근은 O(n)
- begin(), end(), insertFront(), insertBack(), removeFront(), removeBack() 모두 O(1)
- [[iterator]]를 통한 위치 추상화로 내부 구현 은닉

## Relationships

- [[list-adt]] — doubly linked list가 구현하는 ADT
- [[singly-linked-list]] — prev 포인터가 없는 단방향 연결 리스트; 역방향 탐색 불가
- [[iterator]] — 노드 위치를 추상화하는 객체; doubly linked list 탐색에 사용
- [[vector-vs-list]] — array 기반 vector와의 시간/공간 복잡도 비교
- [[sequence-adt]] — List ADT와 Vector ADT를 통합한 상위 ADT; `atIndex(i)`, `indexOf(p)` 연산 제공

## Open Questions

- sentinel node 대신 `nullptr` 체크로 구현할 때 코드 복잡도 차이는 얼마나 되는가?
- C++의 `std::list`는 이 구조와 어떻게 다른가? (allocator, exception safety 등)
- doubly linked list의 캐시 지역성(cache locality) 문제를 완화하는 실제 기법은 무엇인가?

## Sources

- raw/자료구조/CSE2112_02_week05_2_updated.pdf
