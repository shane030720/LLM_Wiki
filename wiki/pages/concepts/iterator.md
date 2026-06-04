---
title: Iterator (반복자)
category: concept
tags: [iterator, linked-list, ADT, abstraction, position]
sources: [raw/자료구조/CSE2112_02_week06_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Iterator(반복자)는 컨테이너(container)의 내부 구현(포인터, 인덱스 등)을 숨기면서(hiding) 원소에 순차적으로 접근하고 앞뒤로 탐색할 수 있게 해주는 추상화 인터페이스다. Doubly linked list에서는 내부 `Node*` 포인터를 캡슐화하여, 사용자가 포인터 연산 없이 위치(position) 기반으로 리스트를 탐색할 수 있도록 한다.

## How It Works

### 내부 구조

Iterator 객체는 현재 가리키는 노드의 포인터 `ref (Node*)`를 내부에 보유한다.

```
Iterator
  └── ref ──► Node [ prev | elem | next ]
```

### 주요 연산자 오버로딩

| 연산자 | 동작 | 구현 |
|--------|------|------|
| `operator*()` | 현재 노드의 원소 참조 반환 | `return ref->elem` |
| `operator==(other)` | 두 iterator가 같은 노드를 가리키는지 비교 | `return ref == other.ref` |
| `operator!=(other)` | 두 iterator가 다른 노드를 가리키는지 비교 | `return ref != other.ref` |
| `operator++()` | 다음 노드로 전진 | `ref = ref->next; return *this` |
| `operator--()` | 이전 노드로 후진 | `ref = ref->prev; return *this` |

### begin() / end() 경계

- `begin()`: `header->next`를 가리키는 Iterator 반환 (첫 번째 실제 원소)
- `end()`: `trailer`를 가리키는 Iterator 반환 (마지막 원소 다음의 가상 sentinel 위치)

```
header ──► [A] ──► [B] ──► [C] ──► trailer
           ↑                         ↑
         begin()                   end()
```

### 사용 예시

```cpp
Iterator p = begin();
for (int i = 0; i < n; i++) { ++p; }  // n번째 위치로 이동
```

## Key Properties

- **캡슐화(Encapsulation)**: 내부 포인터를 숨겨 사용자가 구현 세부사항을 알 필요 없음
- **양방향 탐색**: `operator++`(전진)과 `operator--`(후진) 모두 O(1)
- **Sentinel 노드 활용**: `header`와 `trailer`는 실제 원소가 아닌 경계 표시용 더미 노드; `end()`는 유효하지 않은 원소를 가리키므로 역참조(`*`) 금지
- **참조 반환**: `operator++`와 `operator--`는 `*this`를 반환하여 체이닝(chaining) 가능
- **포인터 비교**: `operator==`은 ref 포인터 주소 비교로 동일 노드 여부 판단

## Relationships

- [[doubly-linked-list]] (Iterator는 doubly linked list의 노드 포인터를 캡슐화함)
- [[tree-data-structure]] (Tree ADT도 position 기반 접근에 동일한 추상화 원리 적용)
- [[vector-vs-list]] (List는 position/iterator로 원소를 참조하고, Vector는 인덱스로 참조함)

## Open Questions

- `operator++(int)` (후위 증가, post-increment)와 `operator++()` (전위 증가, pre-increment)의 차이를 이 구현에서 어떻게 처리해야 하는가?
- Iterator가 가리키는 노드가 삭제된 경우(dangling iterator), 이를 탐지하거나 방지하는 방법은?
- C++ STL의 `std::list::iterator`와 이 강의의 구현 사이의 주요 차이점은?

## Sources

- raw/자료구조/CSE2112_02_week06_1.pdf (pp.4–8)
