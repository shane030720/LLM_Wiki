---
title: Queue
category: concept
tags: [queue, data-structure, fifo, adt]
sources: [raw/자료구조/CSE2112_02_week05_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Queue는 First-In-First-Out(FIFO) 원칙을 따르는 선형 추상 자료형(ADT)이다. 먼저 삽입된 요소가 먼저 제거되며, 삽입은 rear에서, 제거는 front에서 이루어진다. Stack의 Last-In-First-Out(LIFO) 방식과 대비된다.

## How It Works

**주요 연산:**
- `enqueue(e)`: rear에 요소 e 삽입
- `dequeue()`: front의 요소 제거 및 반환
- `front()`: front 요소를 제거하지 않고 반환
- `size()`: 큐의 요소 수 반환
- `empty()`: 큐가 비어있으면 true 반환

**Circular Array 구현:**
크기 N인 배열을 원형으로 사용하여 불필요한 요소 이동을 없앤다. front_index와 rear_index를 관리하며, 인덱스 갱신 시 모듈러 연산을 사용한다.
- enqueue: `rear_index = (rear_index + 1) % N`
- dequeue: `front_index = (front_index + 1) % N`

**Linked List 구현:**
단방향 또는 이중 연결 리스트로 구현한다.
- enqueue → `addBack(e)` (tail에 삽입)
- dequeue → `removeFront()` (head에서 제거)

## Key Properties
- FIFO 순서 보장: 먼저 들어온 요소가 먼저 나감
- Circular Array 구현: 배열 요소 이동 없이 enqueue/dequeue 모두 O(1)
- Linked List 구현: 동적 크기, O(1) enqueue/dequeue
- Stack과 달리 front와 rear 두 포인터를 동시에 관리

## Relationships
- [[stack]] (LIFO 방식의 대응 자료구조; Queue의 front/rear 대신 단일 top 사용)
- [[sequence-adt]] (Queue를 일반화한 상위 ADT로 완전히 대체 가능)
- [[list-adt]] (Linked List 기반 Queue 구현의 토대)

## Open Questions
- Circular Array 구현에서 배열이 완전히 찬(full) 상태와 완전히 빈(empty) 상태를 `front_index == rear_index` 조건만으로 구별할 수 없는 문제를 어떻게 해결하는가?

## Sources
- raw/자료구조/CSE2112_02_week05_1.pdf
