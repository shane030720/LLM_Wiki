---
title: Map 구현체 성능 비교: BST vs AVL Tree vs Hash Table
category: synthesis
tags: [map, bst, avl-tree, hash-table, performance, comparison]
sources: [raw/자료구조/CSE2112_02_week11_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Thesis
Map ADT를 구현하는 세 가지 주요 자료구조 — BST, AVL Tree, Hash Table — 는 평균·최악 시간 복잡도와 기능적 특성 면에서 뚜렷한 트레이드오프를 가지며, 어떤 단일 구현체도 모든 시나리오에서 최선이 아니다.

## Evidence

강의 자료에 제시된 성능 비교표:

| 구현체 | 평균 | 최악 |
|--------|------|------|
| Binary Search Tree | Θ(log n) | O(n) |
| AVL Tree | Θ(log n) | O(log n) |
| Hash Table | Θ(1) | O(n) |

- **[[binary-search-tree]]**: 높이 h에 따라 O(h) 성능. 입력이 정렬되어 있거나 편향 패턴이면 h = O(n)으로 저하됨. In-order traversal로 정렬된 순서 제공.
- **[[avl-tree]]**: 높이 균형 속성으로 항상 h = O(log n) 보장. Trinode restructuring 비용 O(1)이지만 삽입·삭제마다 균형 점검 오버헤드 발생. 최악 성능이 O(log n)으로 세 구현체 중 유일하게 보장됨.
- **[[hash-table]]**: Collision이 적을 때 상수 시간 접근. Hash function 품질과 load factor에 따라 성능 변동. 정렬 순서를 보장하지 않으며 separate chaining 시 추가 메모리 필요.

## Counterevidence
- Hash Table의 평균 Θ(1)은 이론적 수치로, 실제 성능은 hash function 품질과 collision 빈도에 크게 의존한다. 최악 O(n)은 AVL Tree의 최악 O(log n)보다 열위이다.
- AVL Tree의 O(log n) 보장은 상수 계수(constant factor)를 무시한 것이며, 실제 데이터에서는 균형 유지 오버헤드로 인해 Hash Table보다 느릴 수 있다.
- BST는 입력 분포가 무작위에 가깝다면 실용적 성능이 O(log n)에 근접한다.

## Conclusion
- **최악 성능 보장이 필요하고 정렬 순서가 중요한 경우**: AVL Tree — 유일하게 최악 O(log n) 보장
- **정렬 순서가 불필요하고 빠른 평균 접근이 우선인 경우**: Hash Table — 평균 Θ(1)
- **구현 단순성이 중요하고 입력이 무작위에 가까운 경우**: BST — 균형 유지 오버헤드 없음
- 범위 검색(range query)이나 순위 기반 연산이 필요하면 Hash Table은 부적합하며 트리 계열을 선택해야 한다.

## Sources
- raw/자료구조/CSE2112_02_week11_2.pdf
