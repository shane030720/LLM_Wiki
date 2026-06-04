---
title: Double-Ended Queue (Deque)
category: concept
tags: [deque, queue, data-structure, double-ended]
sources: [raw/자료구조/CSE2112_02_week04_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Deque(Double-Ended Queue)는 앞(front)과 뒤(rear) 양쪽에서 모두 삽입과 제거가 가능한 큐의 확장형 자료구조다. 일반 Queue가 rear에서만 삽입하고 front에서만 제거하는 것과 달리, Deque은 양방향 입출력을 모두 허용한다.

## How It Works

일반 Queue의 연산 집합을 포함하면서 다음 연산을 추가로 제공한다:

| 연산 | 설명 |
|------|------|
| `insertFront(e)` | front에 요소 e 삽입 |
| `insertBack(e)` | rear에 요소 e 삽입 |
| `eraseFront()` | front에서 요소 제거 |
| `eraseBack()` | rear에서 요소 제거 |
| `front()` | front 요소 반환 (제거하지 않음) |
| `back()` | rear 요소 반환 (제거하지 않음) |
| `size()` | 요소 수 반환 |
| `empty()` | 비어있는지 여부 반환 |

Queue의 `enqueue(e)` / `dequeue()`는 각각 `insertBack(e)` / `eraseFront()`에 대응한다. Deque을 front-only 또는 rear-only 방식으로 사용하면 Stack 또는 Queue의 동작을 그대로 재현할 수 있다.

## Key Properties

- Queue와 Stack의 기능을 포괄하는 일반화된 선형 자료구조
- 앞·뒤 양쪽에서 삽입/제거 모두 O(1) 가능 (연결 리스트 구현 기준)
- C++ STL에서 `std::deque`로 제공됨
- Queue에 비해 유연성이 높은 대신 인터페이스가 복잡함

## Relationships

- [[queue]] (단방향 입출력만 지원하는 Deque의 특수한 형태)
- [[stack]] (LIFO 방식; Deque을 rear-only로 사용하면 Stack과 동일)

## Open Questions

- 배열 기반 Deque에서 양방향 확장을 O(1) amortized로 지원하는 효율적인 구현 방법은 무엇인가?
- C++ `std::deque`의 내부 구현(세그먼트 배열)이 단순 원형 배열과 성능상 어떻게 다른가?

## Sources

- raw/자료구조/CSE2112_02_week04_2.pdf
