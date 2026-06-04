---
title: Binary Tree ADT
category: entity
tags: [binary-tree, tree, data-structure, adt]
sources: [raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Binary Tree(이진 트리)는 각 노드가 최대 두 개의 자식 노드(왼쪽 서브트리 L, 오른쪽 서브트리 R)를 가지는 트리 자료 구조의 ADT다. 재귀적으로 정의되며, 공집합(empty set)이거나 루트 노드 r과 두 개의 분리된(disjoint) 이진 서브트리 L, R로 구성된다. L은 T의 left subtree, R은 right subtree라 불린다.

## Capabilities

- **재귀적 분할**: 임의의 이진 트리를 루트 + 왼쪽 서브트리 + 오른쪽 서브트리로 분해 가능
- **깊이 d에서의 최대 노드 수**: 2^d 개
- **높이 h인 이진 트리의 최대 노드 수**: 2^(h+1) - 1 개
- **n개 노드 이진 트리의 최소 높이**: ⌈log₂(n+1)⌉ - 1
- 이진 탐색 트리(BST), 힙(Heap), AVL 트리, 레드-블랙 트리 등 다양한 특수 구조의 기반으로 활용

## Limitations

- 높이가 최악의 경우 O(n)까지 증가 가능 (편향 트리, skewed tree)
- 균형을 보장하지 않으면 탐색·삽입·삭제가 최악 O(n)
- 각 노드가 최대 2개의 자식만 가질 수 있어 일반 n-ary 트리를 직접 표현 불가

## Relationships

- [[tree-data-structure]] (이진 트리는 일반 트리의 특수화 — 최대 차수 2)
- [[abstract-data-type]] (이진 트리는 ADT로 정의됨)
- [[priority-queue]] (이진 힙은 완전 이진 트리를 기반으로 구현됨)

## Sources

- raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf (p.5)
