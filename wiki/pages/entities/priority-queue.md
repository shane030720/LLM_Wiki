---
title: Priority Queue
category: entity
tags: [priority-queue, data-structure, heap, ordering]
sources: [raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Priority Queue(우선순위 큐)는 FIFO 큐의 일부 특성을 가지면서, 원소의 처리 순서가 도착 시간이 아닌 각 원소의 priority(우선순위)에 따라 결정되는 자료 구조다. 항상 현재 구조 내에서 가장 중요한 원소만을 조회하고 삭제할 수 있다.

## Capabilities

- **Insert**: 원소와 우선순위를 함께 삽입
- **Find-Min / Find-Max**: 우선순위가 가장 높은 원소 조회 (삭제 없음)
- **Delete-Min / Delete-Max**: 우선순위가 가장 높은 원소 삭제 및 반환
- **비용 관점(cost viewpoint)**: 우선순위 값이 가장 작은 원소(최소 비용)를 먼저 처리
- **이익 관점(profit viewpoint)**: 우선순위 값이 가장 큰 원소(최대 이익)를 먼저 처리
- Dijkstra 최단 경로, Prim MST, Heap Sort, 작업 스케줄링 등에 활용

## Limitations

- 임의의 원소에 직접 접근 불가 — 항상 최우선 원소에만 접근 가능
- 우선순위가 동일한 원소 간의 처리 순서는 구현에 따라 다르며 FIFO 보장 없음
- 이진 힙 기반 구현 시 삽입·삭제가 O(log n); 임의 원소의 삭제나 우선순위 갱신에는 추가 자료 구조 필요

## Relationships

- [[abstract-data-type]] (Priority Queue는 ADT로 정의됨)
- [[queue]] (FIFO 큐의 변형 — 도착 순서 대신 우선순위로 원소 선택)
- [[binary-tree]] (이진 힙은 완전 이진 트리를 이용한 Priority Queue 구현)

## Sources

- raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf (p.8)
