---
title: Tree C++ Implementation (STL List 기반)
category: entity
tags: [tree, cpp, stl, implementation, linked-structure, iterator]
sources: [raw/자료구조/CSE2112_02_week06_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

C++ STL `std::list`를 활용하여 일반 트리(general tree)를 구현한 자료구조 구현체이다. `Node` 클래스와 `Tree` 클래스로 구성되며, 각 노드는 부모 포인터와 자식 리스트를 보유한다. 트리 전체 노드의 삽입 순서는 별도의 `node_seq` 리스트로 일괄 관리하여 순회 및 메모리 해제를 용이하게 한다. 인하대학교 2026-01학기 자료구조(CSE2112) 강의에서 사용되는 교육용 구현체이다.

## Capabilities

### 자료구조 설계

**Node 클래스:**
```cpp
class Node {
private:
  int elem;                              // 노드가 저장하는 값
  Node* parent;                          // 부모 노드 포인터
  list<Node*> children;                  // 자식 노드 포인터 리스트
  list<Node*>::iterator pos_in_seq;      // node_seq 내 자신의 위치
  list<Node*>::iterator pos_in_parent;   // 부모의 children 내 자신의 위치
  friend class Tree;
};
```

**Tree 클래스:**
```cpp
class Tree {
private:
  Node* root_node;        // 루트 노드 포인터
  list<Node*> node_seq;   // 전체 노드 시퀀스 (삽입 순)
};
```

`pos_in_seq`와 `pos_in_parent`는 `std::list`의 이터레이터를 저장하여 O(1)에 해당 위치 삭제를 가능하게 한다.

### 제공 함수 및 복잡도

| 함수 | 설명 | 시간 복잡도 |
|------|------|------------|
| `find(value)` | 값으로 노드 위치(iterator) 탐색 | O(n) |
| `parent(value)` | 부모 노드의 값 출력 | O(n) |
| `children(value)` | 자식 노드들의 값 출력 | O(n + k), k=자식 수 |
| `ancestor(value)` | 루트까지 모든 조상 출력 | O(n) |
| `size()` | 트리의 노드 수 반환 | O(1) |
| `root()` | 루트 노드의 값 반환 | O(1) |
| `insert(parent, value)` | 특정 노드의 자식으로 새 노드 삽입 | O(n) |
| `erase(node)` | 노드 및 서브트리 전체 재귀 삭제 | O(k), k=서브트리 크기 |
| `getDepth(node)` | 노드의 depth 반환 | O(d), d=depth 값 |
| `depth(value)` | 값으로 노드 탐색 후 depth 출력 | O(n) |
| `preorder()` | 전위순회 출력 (재귀) | O(n) |
| `postorder()` | 후위순회 출력 (재귀) | O(n) |

### insert 동작 상세

1. `find`로 부모 노드 탐색 → iterator 획득
2. 새 `Node` 생성 (부모 포인터 설정)
3. 부모의 `children` 리스트 뒤에 추가 → `pos_in_parent` 이터레이터 저장
4. `node_seq` 리스트 뒤에 추가 → `pos_in_seq` 이터레이터 저장

### erase 동작 상세 (재귀)

1. 현재 노드의 자식이 없을 때까지 `erase(children.front())` 재귀 호출
2. `node_seq`에서 `pos_in_seq`로 O(1) 삭제
3. 부모의 `children`에서 `pos_in_parent`로 O(1) 삭제
4. `delete node`로 메모리 해제

## Limitations

- `find`가 O(n) 선형 탐색이므로 대부분의 연산 병목이 O(n)
- 노드 값이 `int`로 고정되어 있어 제네릭(generic) 자료형 미지원
- 중복 값을 가진 노드에 대한 처리가 정의되지 않음 (`find`는 첫 번째 매칭만 반환)
- `pos_in_parent` 이터레이터는 root 노드에 대해 유효하지 않으므로 `erase(root)`는 별도 처리 필요
- 강의 자료 p.35의 `postorder` 구현에 `postorder` 대신 `preorder`를 재귀 호출하는 오타가 존재함 (버그)

## Relationships

- [[tree-data-structure]] (구현 대상 개념; Root, Depth, Height, Subtree 등 용어 정의)
- [[tree-traversal]] (`preorder()` / `postorder()` 함수로 직접 구현된 순회 개념)

## Sources

- raw/자료구조/CSE2112_02_week06_2.pdf
