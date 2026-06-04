---
title: Map ADT
category: concept
tags: [map, adt, data-structure, key-value]
sources: [raw/자료구조/CSE2112_02_week11_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Map(맵)은 key-value 쌍(entry)을 저장하는 추상 자료형(Abstract Data Type)이다. 각 key는 유일한 식별자(unique identifier)이며, key를 통해 대응하는 value를 검색한다. 중복 key를 허용하는 Dictionary와 달리 Map은 key의 유일성을 보장한다.

## How It Works
Map은 세 가지 핵심 연산을 제공한다.

- **find(k)**: key k에 해당하는 entry (k, v)를 가리키는 iterator를 반환한다. 해당 key가 없으면 end iterator를 반환한다.
- **put(k, v)**: entry (k, v)를 삽입한다. key k를 가진 entry가 이미 존재하면 value를 v로 교체한다.
- **erase(k)**: key k를 가진 entry를 제거한다.

이 세 연산의 시간 복잡도는 구현 방식에 따라 달라진다.

## Key Properties
- Key는 유일한 식별자 — 동일한 key를 가진 entry는 최대 하나
- Dictionary와의 차이: Dictionary는 중복 key 허용, Map은 불허
- Iterator를 통해 entry에 접근
- 구현체(BST, AVL Tree, Hash Table)에 따라 성능 특성이 크게 달라짐

## Relationships
- [[binary-search-tree]] (Map의 트리 기반 구현체; in-order traversal로 정렬 순서 제공)
- [[avl-tree]] (균형 보장 BST 기반 Map 구현체; 최악도 O(log n))
- [[hash-table]] (배열 기반 Map 구현체; 평균 O(1) 접근)

## Open Questions
- 정렬된 순서로 순회가 필요한 경우와 그렇지 않은 경우 어떤 구현체를 선택해야 하는가?
- 최악 성능 보장이 중요한 시나리오에서 AVL Tree와 Hash Table 중 무엇이 적합한가?

## Sources
- raw/자료구조/CSE2112_02_week11_2.pdf
