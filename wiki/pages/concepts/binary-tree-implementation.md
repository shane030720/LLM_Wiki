---
title: Binary Tree Implementation (이진 트리 구현)
category: concept
tags: [binary-tree, implementation, linked-list, array, data-structure]
sources: [raw/자료구조/CSE2112_02_week07_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

이진 트리는 크게 두 가지 방식으로 구현한다. 포인터 기반의 linked structure(연결 구조)는 노드 객체들이 포인터로 연결된 position-based 표현이며, index 기반의 array(배열)는 노드를 배열에 저장하고 rank 공식으로 부모-자식 관계를 계산하는 index-based 표현이다.

## How It Works

### Linked List 기반 구현

각 노드 객체가 다음 네 가지 필드를 저장한다.

| 필드 | 역할 |
|------|------|
| `elem` | 노드의 데이터 |
| `parent` | 부모 노드 포인터 |
| `left` | 왼쪽 자식 포인터 |
| `right` | 오른쪽 자식 포인터 |

```cpp
class Node {
private:
    int elem;
    Node* parent;
    Node* left;
    Node* right;
    list<Node*>::iterator pos_in_seq;  // 전체 노드 시퀀스 내 위치
    friend class Tree;
};

class Tree {
private:
    Node* root_node;
    list<Node*> node_seq;  // 모든 노드를 순차 참조하기 위한 보조 구조
};
```

`pos_in_seq`는 Position ADT 구현을 위해 해당 노드가 `node_seq` 리스트 내 어느 위치에 있는지를 O(1)에 접근하기 위해 저장한다. 일반 트리와 이진 트리의 Node 구조 차이: 일반 트리는 `children` 시퀀스를 저장하지만, 이진 트리는 `left`와 `right` 두 포인터만 사용한다.

### Array 기반 구현

노드를 배열 A에 저장하고, 각 노드의 rank(인덱스)를 다음 규칙으로 결정한다.

| 조건 | rank 계산 공식 |
|------|----------------|
| root | rank = 1 |
| 왼쪽 자식 | rank(node) = 2 × rank(parent) |
| 오른쪽 자식 | rank(node) = 2 × rank(parent) + 1 |

이 공식에서 부모 인덱스 역산은 `parent = rank / 2` (정수 나눗셈)이다.

시각적 예시 (8개 노드 트리):

```
        A(1)
       /    \
     B(2)   C(3)
    /   \   /  \
  D(4) E(5) F(6) G(7)
  /  \
H(8) I(9)

Index: 0  1  2  3  4  5  6  7  8  9  ...
Value: -  A  B  C  D  E  F  G  H  I  ...
```

(인덱스 0은 사용하지 않고 1부터 시작)

배열 기반 inorder traversal 구현:

```cpp
void arrayBinaryInorder(int idx) {
    if (idx > n) return;
    arrayBinaryInorder(2 * idx);       // 왼쪽 자식
    cout << tree[idx] << " ";
    arrayBinaryInorder(2 * idx + 1);   // 오른쪽 자식
}
```

불균형 트리에서의 배열 낭비 예시 (오른쪽 자식만 있는 3레벨 트리):

```
Index: 1  2  3  4  5  6  7
Value: A  -  B  -  -  -  C
```

rank 3(B)의 오른쪽 자식 C는 rank 7에 저장되고, rank 2, 4, 5, 6은 비어 있다.

## Key Properties

**Linked List 기반:**
- 임의의 트리 형태를 유연하게 표현 가능
- 노드 삽입/삭제 시 포인터 변경만으로 O(1) 처리 가능
- 각 노드마다 parent + left + right = 3개 포인터의 추가 메모리 필요
- 포인터 역참조(dereference) 비용 존재 (cache locality 낮음)

**Array 기반:**
- rank 공식으로 부모/자식 인덱스를 O(1)에 계산 (곱셈/덧셈만 사용)
- 완전 이진 트리(complete binary tree)에서 메모리 낭비 없이 효율적
- 불균형 트리에서 빈 슬롯이 많아 메모리 낭비 발생 (worst case O(2^n))
- 동적 크기 조정이 어렵고 배열 재할당 시 비용 큼
- 연속 메모리 배치로 cache locality 높음

## Relationships

- [[binary-tree]] (구현 대상인 이진 트리의 정의와 성질)
- [[binary-tree-traversal]] (linked list 기반과 array 기반에서 순회 코드 형태 비교)
- [[linked-list]] (linked structure 구현의 기반 자료구조)
- [[array]] (array 기반 구현의 기반 자료구조)

## Open Questions

- Array 기반 구현에서 rank를 0부터 시작하면 공식이 어떻게 바뀌는가? (left = 2×i+1, right = 2×i+2, parent = (i-1)/2)
- 불균형 트리를 배열로 표현할 때 메모리 낭비를 줄이는 방법은? (예: 왼쪽 자식-오른쪽 형제 표현)
- `pos_in_seq` 이터레이터를 Node에 저장하는 이유가 단순히 O(1) 접근 때문인가, 아니면 Position ADT의 다른 요구사항 때문인가?
- 힙(heap) 자료구조가 array 기반 binary tree를 활용하는 대표 사례인데, 불균형 문제를 어떻게 회피하는가?

## Sources

- raw/자료구조/CSE2112_02_week07_2.pdf
