---
title: Array-based Stack
category: entity
tags: [stack, array, data-structure, implementation, cpp]
sources: [raw/자료구조/CSE2112_02_week03_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Array-based Stack은 [[stack]] ADT를 고정 크기 배열(array)로 구현한 방식이다. 배열 S와 top 인덱스 t(초기값 -1)를 핵심 멤버로 사용하며, t가 -1이면 스택이 비어 있음을 의미한다. C++에서는 `ArrayStack<E>` 템플릿 클래스로 표현된다.

```cpp
template <typename E>
class ArrayStack {
  enum { DEF_CAPACITY = 100 };
public:
  ArrayStack(int capacity = DEF_CAPACITY);
  int size() const;   bool empty() const;
  const E& top() const throw(StackEmpty);
  void push(const E& e) throw(StackFull);
  void pop() throw(StackEmpty);
private:
  E* S;        // 스택 원소를 저장하는 배열
  int capacity; // 배열 최대 크기
  int t;        // top 원소의 인덱스 (초기값 -1)
};
```

## Capabilities

모든 연산이 O(1) 시간복잡도로 수행된다.

| 연산 | 알고리즘 | 설명 |
|------|----------|------|
| `size()` | return t + 1 | 현재 원소 수 반환 |
| `empty()` | return (t < 0) | 비어 있는지 확인 |
| `push(e)` | size()==N → StackFull; else t←t+1, S[t]←e | top에 원소 삽입 |
| `pop()` | empty() → StackEmpty; else t←t−1, return S[t+1] | top 원소 제거 |
| `top()` | empty() → StackEmpty; else return S[t] | top 원소 조회 |

공간복잡도는 O(N)이며, 실제 원소 수 n에 무관하게 배열 크기 N에 종속된다.

C++ 사용 예시:
```cpp
ArrayStack<int> A;     // A = [], size = 0
A.push(7);             // A = [7*]
A.push(13);            // A = [7, 13*]
cout << A.top();       // 13
A.pop();               // A = [7*]
```

## Limitations

- 스택의 최대 크기(capacity)를 생성 시점에 반드시 정의해야 하며 실행 중 변경 불가
- 배열이 가득 찬 상태(size() == N)에서 push 호출 시 `StackFull` 예외 발생 (Stack ADT 고유의 제약이 아닌 구현상의 한계)
- 실제 원소 수 n이 적더라도 배열 크기 N만큼 메모리를 점유하여 공간 낭비 가능

## Relationships

- [[stack]]: 이 구현체가 따르는 ADT 정의
- [[linked-list-based-stack]]: StackFull 예외가 없는 동적 크기 대안 구현체
- [[stack-implementation-comparison]]: 두 구현의 트레이드오프 분석

## Sources

- raw/자료구조/CSE2112_02_week03_2.pdf
