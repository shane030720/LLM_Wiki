---
title: Binary Tree (이진 트리)
category: concept
tags: [binary-tree, tree, data-structure, graph-theory]
sources: [raw/자료구조/CSE2112_02_week07_2.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Binary Tree(이진 트리)는 각 노드가 최대 두 개의 자식 노드를 갖는 트리 자료구조이다. 각 자식은 left child(왼쪽 자식) 또는 right child(오른쪽 자식)으로 구분되며, 이 순서쌍은 좌→우로 고정된 ordered pair이다. Proper binary tree(정 이진 트리, full binary tree라고도 함)는 모든 internal node(내부 노드)가 정확히 두 개의 자식을 갖는 경우를 말한다. 반면 하나 이상의 internal node가 자식을 하나만 갖는 경우를 improper binary tree라 한다.

## How It Works

각 노드는 element(데이터), parent(부모), left child(왼쪽 자식), right child(오른쪽 자식) 참조를 저장한다. 루트 노드는 parent가 없는 유일한 노드이며, external node(leaf node, 단말 노드)는 자식이 없는 노드이다.

Decision tree(결정 트리)는 binary tree의 대표적 응용으로, 각 internal node에 Yes/No 질문을 대응시키고 그 답에 따라 왼쪽 또는 오른쪽 서브트리로 분기한다.

### Proper Binary Tree의 수학적 성질

높이 h인 proper binary tree에서 각 수량의 범위는 다음과 같다.

| 대상 | 최솟값 | 최댓값 |
|------|--------|--------|
| 전체 노드 수 n | 2h + 1 | 2^(h+1) - 1 |
| External node 수 nE | h + 1 | 2^h |
| Internal node 수 nI | h | 2^h - 1 |

- 최솟값: 각 레벨에서 정확히 한 노드만 두 자식을 갖고 나머지는 없는 "한 줄" 형태일 때
- 최댓값: 모든 internal node가 두 자식을 갖는 완전히 채워진 형태일 때

등비급수 합 공식(a(r^n - 1) / (r - 1))을 적용하면:
- 최대 internal node 수: 2^0 + 2^1 + ... + 2^(h-1) = 2^h - 1
- 최대 전체 노드 수: 2^0 + 2^1 + ... + 2^h = 2^(h+1) - 1
- 최소 external node 수: 각 레벨당 1개씩 + 마지막 레벨 1개 = h + 1

높이 h의 범위로 역산하면: log2(n+1) - 1 <= h <= (n-1)/2

## Key Properties

- 각 노드의 자식 수는 0, 1, 2 중 하나 (일반 트리와 달리 최대 2개로 제한)
- Left child와 right child는 구분된 ordered pair (왼쪽과 오른쪽은 교환 불가)
- Proper binary tree: 모든 internal node의 자식 수 = 정확히 2
- Improper binary tree: 하나 이상의 internal node의 자식 수 = 1
- 높이 h일 때 노드 수는 최소 O(h) (선형), 최대 O(2^h) (지수적)
- nE = nI + 1 (proper binary tree에서 외부 노드 수는 내부 노드 수보다 항상 1 많음)

## Relationships

- [[binary-tree-traversal]] (이진 트리의 순회 알고리즘 — preorder, inorder, postorder, euler tour)
- [[binary-tree-implementation]] (연결 리스트 및 배열 기반 이진 트리 구현)
- [[tree]] (binary tree의 상위 개념인 일반 트리)

## Open Questions

- Improper binary tree에서 노드 수 범위의 일반 공식은 어떻게 도출하는가?
- nE = nI + 1 성질은 proper binary tree에서만 성립하는가? (귀납법 증명)
- 균형 이진 트리(balanced binary tree)의 조건은 무엇이며, 어떻게 자동 유지하는가?

## Sources

- raw/자료구조/CSE2112_02_week07_2.pdf
