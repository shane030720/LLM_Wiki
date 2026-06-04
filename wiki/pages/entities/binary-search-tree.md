---
title: Binary Search Tree
category: entity
tags: [tree, data-structure, search, algorithm]
sources: [raw/알고리즘/CH06 동적 집합과 탐색.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

Binary Search Tree(이진 탐색 트리, BST)는 순서 있는(ordered) 집합에서 키를 저장하고 효율적으로 탐색하기 위한 이진 트리 자료구조다. 각 노드의 키는 왼쪽 서브트리의 모든 키보다 크고 오른쪽 서브트리의 모든 키보다 작거나 같다는 BST Property를 만족한다. Inorder Traversal(중위 순회)을 수행하면 키의 정렬된 목록이 생성된다.

## Capabilities

- **탐색(Search):** 루트에서 시작해 키 비교를 통해 재귀적으로 탐색한다.
  - `K == root.key` → 탐색 성공
  - `K < root.key` → 왼쪽 서브트리 재귀 탐색
  - `K > root.key` → 오른쪽 서브트리 재귀 탐색
- **정렬된 순회:** Inorder Traversal로 정렬된 키 목록을 O(n) 시간에 생성한다.
- **삽입/삭제:** BST Property를 유지하면서 노드를 추가하거나 제거할 수 있다.
- 균형 잡힌 트리에서 탐색·삽입·삭제 모두 **O(log n)** 시간 복잡도를 달성한다.

## Limitations

- 삽입 순서에 따라 트리가 한쪽으로 치우친 체인(chain) 구조가 될 수 있다.
- 최악의 경우(완전한 체인 구조) 탐색 비용이 **Θ(n)**으로 선형 시간에 달한다.
- 균형을 자동으로 유지하지 않으므로, 최선의 성능을 위해서는 별도의 균형 기법이 필요하다.
- Binary Tree Rotation(이진 트리 회전) 등의 기법으로 균형을 보완해야 한다.

## Relationships

- [[red-black-tree]] (BST의 확장으로, BST Property를 유지하면서 자동으로 균형을 보장하는 자료구조)
- [[amortized-analysis]] (BST 연산의 평균적 비용 분석에 활용 가능)

## Sources

- raw/알고리즘/CH06 동적 집합과 탐색.pdf
