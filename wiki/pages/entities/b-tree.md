---
title: B-Tree Index
category: entity
tags: [b-tree, index, tree, data-structure, database]
sources: [raw/데이터베이스/Indexing.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Overview

B-Tree는 1970년 Rudolf Bayer와 E. McCreight가 발표한 "Organization and Maintenance of Large Ordered Indexes"에서 소개된 자기 균형 트리 자료구조다. [[b-plus-tree]]와 달리 비리프 노드(non-leaf node)에도 레코드 포인터(Bi)를 저장함으로써 각 검색 키가 트리 전체에서 단 한 번만 나타나도록 설계되었다. B+-Tree의 전신(前身)에 해당하며, 현재 실용적인 시스템에서는 B+-Tree에 비해 채택 빈도가 낮다.

## Capabilities

### 구조적 특징

**리프 노드 (a)**:
- B+-Tree의 리프 노드와 동일한 구조

**비리프 노드 (b)**:
- B+-Tree와 달리 각 검색 키 Ki에 대해 레코드 포인터 Bi가 추가로 포함됨
- 검색 키가 비리프 노드에 나타나면 리프 노드에는 중복 저장하지 않음 — 검색 키의 중복 저장 제거

### B+-Tree 대비 장점

- 중복 저장 제거로 경우에 따라 더 적은 트리 노드 사용 가능
- 일부 조회에서 리프 노드에 도달하기 전에 비리프 노드의 레코드 포인터를 통해 검색 완료 가능 — 평균 탐색 경로 단축 가능성

## Limitations

- 조기 탐색 완료가 가능한 검색 키는 전체 중 소수에 불과해 실질적 이득이 제한적
- 비리프 노드가 레코드 포인터(Bi)를 추가로 저장하므로 노드 크기가 커지고 Fan-out 감소 → B+-Tree보다 트리 깊이가 더 깊어져 탐색 비용 증가
- 삽입/삭제 알고리즘이 B+-Tree보다 복잡하고 구현 난이도가 높음
- 대부분의 실용적 상황에서 장점이 단점을 능가하지 못함 — B+-Tree가 사실상 표준

## Relationships

- [[b-plus-tree]] — B-Tree보다 더 널리 사용되는 변형 구조로, 모든 검색 키를 리프 노드에 집중시켜 Fan-out을 높이고 구현을 단순화함
- [[database-index]] — B-Tree가 구현하는 인덱스 개념의 상위 범주

## Sources

- raw/데이터베이스/Indexing.pdf
