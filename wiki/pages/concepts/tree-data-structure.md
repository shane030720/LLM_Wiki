---
title: Tree Data Structure
category: concept
tags: [tree, data-structure, hierarchical, linked-structure]
sources: [raw/자료구조/CSE2112_02_week07_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Tree는 노드(node)들이 부모-자식(parent-child) 관계로 연결된 계층적(hierarchical) 추상 자료구조다. 하나의 루트(root) 노드에서 시작하며, 각 노드는 0개 이상의 자식 노드를 가질 수 있다. 조직도, 파일 시스템, 프로그래밍 환경 등에서 널리 활용된다.

## How It Works
C++ 연결 구조(linked structure) 기반 구현에서 Tree는 두 클래스로 구성된다.

**Node 클래스:**
- `int elem`: 노드에 저장된 값
- `Node* parent`: 부모 노드 포인터
- `list<Node*> children`: 자식 노드 포인터 리스트
- `list<Node*>::iterator pos_in_seq`: `node_seq` 내 위치 이터레이터
- `list<Node*>::iterator pos_in_parent`: 형제 리스트 내 위치 이터레이터

**Tree 클래스:**
- `Node* root_node`: 루트 노드 포인터
- `list<Node*> node_seq`: 트리 내 모든 노드를 저장하는 전역 시퀀스

**주요 연산:**
- `find(value)`: `node_seq`를 선형 탐색하여 해당 값의 노드 이터레이터 반환 (O(n))
- `insert(parent_val, value)`: 중복 및 부모 존재 여부를 검사한 뒤 새 자식 노드를 추가; 부모의 `children`과 전역 `node_seq` 양쪽에 등록
- `erase(value)`: 재귀적으로 모든 자식을 먼저 삭제한 후 해당 노드를 부모의 `children`과 `node_seq`에서 제거하고 메모리 해제
- `parent(value)`: 해당 노드의 부모 원소 출력
- `children(value)`: 해당 노드의 모든 자식 원소 순서대로 출력
- `depth(value)`: 루트까지 `parent` 포인터를 따라 올라가며 깊이 계산
- `ancestor(value)`: 루트까지의 모든 조상 노드 원소 출력

## Key Properties
- 루트(root): 부모가 없는 유일한 노드
- 내부 노드(internal node): 하나 이상의 자식을 가진 노드
- 외부 노드/리프(external node / leaf): 자식이 없는 노드
- 깊이(depth): 루트로부터의 간선 수 (루트의 depth = 0)
- 높이(height): 루트에서 가장 깊은 리프까지의 간선 수
- `erase`는 서브트리 전체를 재귀적으로 삭제하므로 단일 노드가 아닌 서브트리 전체가 제거됨
- 루트 노드는 `erase` 대상에서 제외

## Relationships
- [[binary-tree]]: Tree를 확장(extend)하여 자식을 최대 2개로 제한한 특수 형태; `left`, `right` 포인터 추가
- [[tree-traversal]]: Preorder, Postorder 등의 순회 알고리즘이 Tree ADT 위에서 동작

## Open Questions
- `node_seq`를 별도로 유지하면 `find`가 O(n) 선형 탐색인데, 해시 맵(`unordered_map`)으로 교체하면 O(1)로 개선 가능하나 이터레이터 캐싱 설계가 달라짐
- Skewed tree(편향 트리)에서 `erase` 재귀 깊이가 노드 수와 같아져 스택 오버플로우 위험이 있음; 반복(iterative) 구현 필요성 검토 필요

## Sources
- raw/자료구조/CSE2112_02_week07_1.pdf
