---
title: Singly Linked List
category: concept
tags: [linked-list, data-structure, pointer, node, dynamic]
sources: [raw/자료구조/CSE2112_02_week03_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Singly Linked List는 노드(node)의 시퀀스로 구성된 구체적(concrete) 자료구조다. 각 노드는 데이터 원소(element)와 다음 노드를 가리키는 단일 링크(pointer)를 저장한다. 배열과 달리 사전에 정해진 고정 크기가 없으며, 메모리상에서 불연속적으로 배치된다.

## How It Works

리스트 전체는 **head** 포인터(첫 번째 노드)와 **tail** 포인터(마지막 노드)로 관리된다.

```cpp
struct Node {
    int data;
    Node* next;
    Node(int val) : data(val), next(nullptr) {}
};

class LinkedList {
public:
    LinkedList();
    ~LinkedList();
    int size();
    bool empty();
    int front();
    int back();
    void addFront(int x);
    void addBack(int x);
    void removeFront();
    void removeBack();
    void print();
private:
    Node* head;
    Node* tail;
    int n;
};
```

**Head에 삽입 (O(1)):**
1. 새 노드 할당
2. 원소 삽입
3. 새 노드의 `next`가 기존 head를 가리키도록 설정
4. head를 새 노드로 업데이트

**Tail에 삽입 (O(1)):**
1. 새 노드 할당
2. 원소 삽입
3. 새 노드의 `next`를 `nullptr`로 설정
4. 기존 마지막 노드의 `next`가 새 노드를 가리키도록 설정
5. tail을 새 노드로 업데이트

**Head에서 제거 (O(1)):**
1. head를 다음 노드로 업데이트
2. 기존 첫 번째 노드 메모리 해제

**Tail에서 제거 (비효율적, O(n)):**
- Singly linked list에서는 tail 이전 노드를 상수 시간에 찾을 방법이 없다
- 이전 노드를 찾기 위해 head부터 순차 탐색이 필요하므로 O(n) 시간이 소요된다

## Key Properties

- **동적 크기(Dynamic size)**: 원소 추가/제거에 따라 크기가 변한다 (배열은 고정 크기)
- **불연속 메모리(Discontinuous memory)**: 각 노드는 힙에 개별 할당되며 메모리상 연속적이지 않다
- **순차 접근(Sequential access)**: 임의 원소에 접근하려면 head부터 순서대로 탐색해야 한다 (배열은 인덱스로 직접 접근 가능)
- **효율적 head 삽입/삭제**: O(1)
- **비효율적 tail 삭제**: O(n) — singly linked의 구조적 한계
- **단방향 순회**: 각 노드는 다음 노드로만 이동 가능하다

## Relationships

- [[stack]] — Singly linked list의 head를 top으로 사용하여 Stack을 구현할 수 있다
- Doubly Linked List — 각 노드가 앞뒤 양방향 링크를 가지며, tail 삭제가 O(1)로 가능하다
- Circular Linked List — tail의 next가 head를 가리키는 순환 구조의 변형이다
- Array — 연속 메모리·고정 크기·직접 접근이 특징이며, Linked List와 상호 보완적 트레이드오프를 가진다
- C++ `vector` — 동적 배열로, 연속 메모리를 유지하면서 용량이 부족하면 2배로 재할당한다 (Linked List와는 메모리 모델이 다르다)

## Open Questions

- Tail 삭제의 비효율성을 해결하기 위한 doubly linked list와 singly linked list의 메모리 오버헤드 트레이드오프는 어떻게 평가해야 하는가?
- C++의 `std::list`(doubly linked list)와 `std::forward_list`(singly linked list) 중 선택 기준은 무엇인가?

## Sources

- raw/자료구조/CSE2112_02_week03_1.pdf (Week 03 – Lecture 01, 슬라이드 7–26)
