---
title: Tree Traversal (트리 순회)
category: concept
tags: [traversal, tree, binary-tree, algorithm, recursion, preorder, postorder, inorder]
sources: [raw/자료구조/CSE2112_02_week07_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition
Tree Traversal(트리 순회)은 트리의 모든 노드를 정해진 순서에 따라 빠짐없이 방문하는 알고리즘이다. 방문 순서에 따라 Preorder, Postorder, Inorder, Euler Tour로 나뉘며, 각각 다른 문제 유형에 적합하다. 모든 기본 순회는 재귀(recursion)로 자연스럽게 표현된다.

## How It Works

**1. Preorder Traversal (전위 순회)**
현재 노드를 방문한 뒤 각 자식 서브트리를 재귀적으로 순회한다. 루트가 항상 가장 먼저 출력된다.
```
Algorithm preorder(v)
  visit(v)
  for each child w of v
    preorder(w)
```
Binary Tree 특화:
```
Algorithm binaryPreorder(v)
  visit(v)
  if v is internal then
    binaryPreorder(v.left())
    binaryPreorder(v.right())
```

**2. Postorder Traversal (후위 순회)**
모든 자식 서브트리를 먼저 순회한 뒤 현재 노드를 방문한다. 의존 관계 해소 및 산술식 계산에 활용된다.
```
Algorithm postorder(v)
  for each child w of v
    postorder(w)
  visit(v)
```
산술식 평가(Arithmetic Expression Tree) 적용:
```
Algorithm evalExpression(v)
  if v is internal then
    x <- evalExpression(v.left())
    y <- evalExpression(v.right())
    op <- operator stored at v
    return x op y
  else
    return v.element()
```
예: `((2 × 5 − 1) + (3 × 2))`를 순서대로 평가하면 최종값 14 반환.

**3. Inorder Traversal (중위 순회)**
Binary Tree 전용. 왼쪽 서브트리 → 현재 노드 → 오른쪽 서브트리 순으로 방문한다.
```
Algorithm inOrder(v)
  if v has left child
    inOrder(v.left())
  visit(v)
  if v has right child
    inOrder(v.right())
```
응용: Binary Tree를 2D 평면에 그릴 때 `x(p) = inorder rank of p`, `y(p) = depth of p`로 좌표 결정.

**4. Euler Tour Traversal**
트리 주위를 "걷는" 방식으로 각 노드를 세 번 방문한다: 왼쪽(preorder 시점), 아래(inorder 시점), 오른쪽(postorder 시점). Preorder, Inorder, Postorder를 하나의 프레임워크로 통합한다.
```
Algorithm eulerTour(v)
  visit v on the left         // preorder
  if v is internal then
    eulerTour(v.left())
  visit v from below          // inorder
  if v is internal then
    eulerTour(v.right())
  visit v from the right      // postorder
```
산술식 출력 응용: 왼쪽 방문 시 `"("`, 아래 방문 시 연산자/피연산자 출력, 오른쪽 방문 시 `")"` 출력 → 완전히 괄호가 갖춰진 중위 표기식 생성.

## Key Properties
- 모든 순회의 시간 복잡도는 O(n) (n = 노드 수)
- Preorder: 루트 우선 → 디렉터리 구조 출력, 트리 복사에 적합
- Postorder: 자식 우선 → 산술식 계산, 디렉터리 용량 합산에 적합
- Inorder: Binary Tree 전용 → BST에서 오름차순 출력 보장
- Euler Tour: 단일 순회로 세 시점을 모두 활용 가능한 가장 범용적인 방법
- 재귀 구현이 자연스럽지만, 트리 높이에 비례한 호출 스택을 사용

## Relationships
- [[tree-data-structure]]: Preorder, Postorder 순회가 일반 트리 위에서 정의됨
- [[binary-tree]]: Inorder traversal 및 Euler Tour는 Binary Tree에 특화된 순회 방법
- [[binary-search-tree]] (미작성): Inorder traversal 시 정렬된 원소 순서로 방문된다는 성질이 핵심적으로 활용됨

## Open Questions
- 재귀 기반 순회는 편향 트리(skewed tree)에서 O(n) 깊이의 콜 스택을 사용하므로 스택 오버플로우 위험이 있음; 명시적 스택(explicit stack)을 사용하는 반복(iterative) 구현으로 어떻게 대체할 수 있는가?
- Euler Tour의 세 방문 시점을 활용한 응용(예: LCA 계산, 구간 쿼리)이 강의 범위 밖에서 어떻게 확장되는가?

## Sources
- raw/자료구조/CSE2112_02_week07_1.pdf
