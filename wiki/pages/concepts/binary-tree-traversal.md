---
title: Binary Tree Traversal (이진 트리 순회)
category: concept
tags: [binary-tree, traversal, algorithm, recursion, expression-tree]
sources: [raw/자료구조/CSE2112_02_week07_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Binary tree traversal(이진 트리 순회)은 이진 트리의 모든 노드를 정해진 규칙에 따라 빠짐없이 방문하는 알고리즘이다. 노드 방문 시점에 따라 preorder(전위 순회), inorder(중위 순회), postorder(후위 순회), euler tour(오일러 투어 순회)로 분류된다.

## How It Works

### Preorder (전위 순회)

노드를 먼저 방문한 뒤, 왼쪽 서브트리 → 오른쪽 서브트리 순으로 재귀 방문한다.

```cpp
void binaryPreorder(Node* node) {
    cout << node->elem << " ";
    if (node->left  != nullptr) binaryPreorder(node->left);
    if (node->right != nullptr) binaryPreorder(node->right);
}
```

일반 트리의 preorder와 비교: 일반 트리는 `children` 시퀀스를 순서대로 순회하지만, 이진 트리는 left/right 두 포인터만 사용한다.

### Inorder (중위 순회)

왼쪽 서브트리 방문 → 현재 노드 방문 → 오른쪽 서브트리 방문 순으로 진행한다. inorder는 이진 트리에서만 자연스럽게 정의된다 (일반 트리에서는 "중간" 방문의 위치가 모호).

```cpp
void binaryInorder(Node* node) {
    if (node == nullptr) return;
    binaryInorder(node->left);
    cout << node->elem << " ";
    binaryInorder(node->right);
}
```

배열 기반 이진 트리에서의 inorder (rank 인덱스 활용):

```cpp
void arrayBinaryInorder(int idx) {
    if (idx > n) return;
    arrayBinaryInorder(2 * idx);
    cout << tree[idx] << " ";
    arrayBinaryInorder(2 * idx + 1);
}
```

### Postorder (후위 순회)

왼쪽 서브트리 → 오른쪽 서브트리를 먼저 방문한 뒤, 마지막으로 현재 노드를 방문한다. 자식 결과를 모두 확보한 후 부모를 처리하는 bottom-up 특성을 갖는다.

```cpp
void binaryPostorder(Node* node) {
    if (node->left  != nullptr) binaryPostorder(node->left);
    if (node->right != nullptr) binaryPostorder(node->right);
    cout << node->elem << " ";
}
```

**Expression tree 평가 응용:** postorder로 수식 트리를 순회하면, internal node 방문 시 이미 두 서브트리의 값이 확정되어 있으므로 연산자를 적용할 수 있다.

```
Algorithm evalExpression(v):
  if v is internal:
    x <- evalExpression(v.left())
    y <- evalExpression(v.right())
    op <- operator stored at v
    return x op y
  else:
    return v.element()
```

예시: `+` 루트, 왼쪽 서브트리 `2 × (5 - 1) = 8`, 오른쪽 서브트리 `3 × 2 = 6` → 결과 `14`

### Euler Tour (오일러 투어 순회)

트리 외곽을 "한 바퀴 도는" 방식으로, 각 노드를 세 번 방문한다.

| 방문 시점 | 역할 | 산술식 출력 응용 |
|-----------|------|-----------------|
| 왼쪽 진입 시 (preorder) | 전처리 | `"("` 출력 |
| 아래에서 올라올 때 (inorder) | 본 처리 | element 출력 |
| 오른쪽 복귀 시 (postorder) | 후처리 | `")"` 출력 |

```cpp
void eulerTour(Node* node) {
    cout << node->elem << " ";               // 왼쪽 방문
    if (node->left  != nullptr) eulerTour(node->left);
    cout << node->elem << " ";               // 아래에서 방문
    if (node->right != nullptr) eulerTour(node->right);
    cout << node->elem << " ";               // 오른쪽 방문
}
```

**산술식 완전 괄호 출력 응용:** internal node의 왼쪽 방문 시 `(`, 오른쪽 방문 시 `)` 출력하면 수식의 완전 괄호 표현이 생성된다.

- external node에 괄호를 추가하지 않는 버전: `((2 × (5 - 1)) + (3 × 2))`
- 모든 노드에 괄호를 추가하는 버전: `(((2) × (5 - 1)) + ((3) × (2)))`

## Key Properties

- 모든 순회의 시간 복잡도: O(n) (n = 노드 수)
- Preorder: 루트 우선 → 트리 복사, 직렬화(serialization)에 유용
- Inorder: 이진 탐색 트리(BST)에서 오름차순 정렬 순서로 방문
- Postorder: bottom-up 처리 → 수식 평가, 트리 메모리 해제에 유용
- Euler Tour: preorder + inorder + postorder를 하나의 순회로 통합한 일반화 형태; 노드당 3번 방문으로 총 3n번 방문
- 배열 기반에서 부모-자식 인덱스 관계: left = 2×i, right = 2×i+1

## Relationships

- [[binary-tree]] (순회 대상인 이진 트리의 정의와 구조)
- [[binary-tree-implementation]] (linked list 및 array 기반 구현에서 순회 코드가 달라짐)
- [[tree]] (preorder, postorder의 일반 트리 버전 정의)

## Open Questions

- Inorder traversal은 왜 일반 트리에서 자연스럽게 정의되지 않는가? (자식이 3개 이상일 때 "중간" 방문 위치가 복수가 됨)
- Euler Tour의 각 노드 3회 방문 성질을 이용한 LCA(Lowest Common Ancestor) 알고리즘과의 연관성은?
- Postorder를 이용한 expression tree 평가 시 연산자 우선순위를 별도로 처리할 필요가 없는 이유는?

## Sources

- raw/자료구조/CSE2112_02_week07_2.pdf
