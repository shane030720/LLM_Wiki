---
title: Stack
category: concept
tags: [stack, data-structure, lifo, abstract-data-type, array, linked-list]
sources: [raw/자료구조/CSE2112_02_week04_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Stack은 Last-In-First-Out (LIFO) 원칙에 따라 원소를 삽입하고 제거하는 추상 자료구조(ADT)다. 가장 최근에 삽입된(마지막) 원소만 제거할 수 있다. 최근 방문한 웹사이트 뒤로 가기, 텍스트 편집기의 실행 취소(Undo) 기능이 대표적인 실사용 예시다.

## How It Works

### 주요 연산 (Main Operations)
- **push(e)**: 스택의 top에 원소 e를 삽입
- **pop()**: 스택의 top 원소를 제거

### 보조 연산 (Supporting Operations)
- **top()**: top 원소를 제거하지 않고 반환
- **size()**: 스택에 저장된 원소 수 반환
- **empty()**: 스택이 비어 있으면 true, 아니면 false 반환

### 예외 (Exceptions)
- **StackEmpty**: 빈 스택에서 `top()` 또는 `pop()` 호출 시 발생
- **StackFull**: 배열 기반 구현에서 가득 찬 스택에 `push()` 호출 시 발생

### Array-based Stack 구현

```cpp
template <typename E>
class ArrayStack {
  enum { DEF_CAPACITY = 100 };
public:
  ArrayStack(int capacity = DEF_CAPACITY);
  int size() const;
  bool empty() const;
  const E& top() const throw(StackEmpty);
  void push(const E& e) throw(StackFull);
  void pop() throw(StackEmpty);
private:
  E* S;        // 배열
  int capacity; // 최대 용량
  int t;        // top 원소의 인덱스 (초기값 -1)
};
```

- `t`를 -1로 초기화하여 빈 스택을 표현
- push: `t`를 1 증가 후 `S[t]`에 원소 저장
- pop: `t`를 1 감소
- 연산 예시: push(5) → push(3) → pop() → push(7) → pop() → top()=5 → pop() → empty()=true

### Linked List-based Stack 구현

```cpp
typedef string Elem;
class LinkedStack {
public:
  LinkedStack();
  int size() const;
  bool empty() const;
  const Elem& top() const throw(StackEmpty);
  void push(const Elem& e);
  void pop() throw(StackEmpty);
private:
  SLinkedList<Elem> S;
  int n; // 원소 수 (초기값 0)
};
```

- head가 top 역할을 수행; head는 nullptr로 초기화
- push → `addFront` (연결 리스트의 head에 삽입)
- pop → `removeFront` (연결 리스트의 head에서 제거)
- 동적 메모리 할당이므로 StackFull 예외 없음

### 구현 방식 비교

| 항목 | Array-based | Linked List-based |
|------|-------------|-------------------|
| 용량 제한 | 있음 (capacity) | 없음 (동적 할당) |
| top 추적 | 인덱스 `t` (초기값 -1) | 포인터 `head` (초기값 nullptr) |
| StackFull 예외 | 있음 | 없음 |
| StackEmpty 예외 | 있음 | 있음 |
| 구현 복잡도 | 단순 | 포인터 관리 필요 |

## Key Properties

- LIFO 순서: 가장 최근에 삽입된 원소가 먼저 제거됨
- top 단일 지점에서 삽입(push)·삭제(pop) 모두 발생
- 배열 기반: 용량 고정, 인덱스로 top 추적, 인덱스 오버플로우 주의
- 연결 리스트 기반: 용량 제한 없음, head가 top 역할
- [[queue]]의 FIFO와 대비되는 LIFO 구조

## Relationships

- [[queue]] (FIFO 원칙을 따르는 대비되는 자료구조; Queue는 rear/front 양 끝에서 삽입·삭제, Stack은 top 단일 지점)
- [[linked-list]] (Linked List-based Stack 구현의 기반; `addFront`·`removeFront` 연산 활용)

## Open Questions

- 배열 기반과 연결 리스트 기반의 시간·공간 복잡도 트레이드오프 (강의에서 구조만 비교, 성능 분석 미제공)
- 실제 함수 호출 스택(call stack), 재귀와의 관계 (강의에서 미언급)
- 동적 배열(vector)을 사용한 Stack 구현의 장단점

## Sources

- raw/자료구조/CSE2112_02_week04_1.pdf
