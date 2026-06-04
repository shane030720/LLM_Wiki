---
title: Linked List-based Stack
category: entity
tags: [stack, linked-list, data-structure, implementation, cpp]
sources: [raw/자료구조/CSE2112_02_week03_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Linked List-based Stack은 [[stack]] ADT를 단일 연결 리스트(singly linked list)로 구현한 방식이다. 연결 리스트의 head를 스택의 top으로 사용하여, 삽입(`push`)은 `addFront`, 삭제(`pop`)는 `removeFront` 연산에 대응된다. C++에서는 `LinkedStack` 클래스로 표현되며, 내부적으로 `SLinkedList<Elem>`을 활용한다. head 포인터는 초기값 nullptr이다.

```cpp
typedef string Elem;
class LinkedStack {
public:
  LinkedStack();
  int size() const;   bool empty() const;
  const Elem& top() const throw(StackEmpty);
  void push(const Elem& e);
  void pop() throw(StackEmpty);
private:
  SLinkedList<Elem> S; // 원소를 저장하는 연결 리스트
  int n;               // 현재 원소 수
};
```

## Capabilities

- **동적 크기**: 사전 용량 정의가 불필요하며, `StackFull` 예외가 발생하지 않음
- **O(1) 시간복잡도**: push(addFront), pop(removeFront), top(front), size, empty 모두 상수 시간 수행

주요 구현:
```cpp
void LinkedStack::push(const Elem& e) {
  ++n;
  S.addFront(e);  // head에 새 노드 삽입
}
void LinkedStack::pop() throw(StackEmpty) {
  if (empty()) throw StackEmpty("Pop from empty stack");
  --n;
  S.removeFront(); // head 노드 제거
}
const Elem& LinkedStack::top() const throw(StackEmpty) {
  if (empty()) throw StackEmpty("Top of empty stack");
  return S.front(); // head 노드 값 반환
}
```

## Limitations

- 각 노드가 데이터 외에 next 포인터를 추가로 저장하므로 노드당 메모리 오버헤드 존재
- 메모리가 비연속적으로 할당되어 배열 기반 대비 캐시 지역성(cache locality)이 낮음
- 빈 스택에서 `top()` 또는 `pop()` 호출 시 `StackEmpty` 예외 발생 (Array-based와 동일)

## Relationships

- [[stack]]: 이 구현체가 따르는 ADT 정의
- [[array-based-stack]]: 고정 용량의 배열 기반 대안 구현체
- [[stack-implementation-comparison]]: 두 구현의 트레이드오프 분석

## Sources

- raw/자료구조/CSE2112_02_week03_2.pdf
