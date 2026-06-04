---
title: Queue
category: entity
tags: [queue, data-structure, fifo, linear-structure]
sources: [raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Queue(큐)는 삽입은 항상 한쪽 끝(rear/back)에서, 삭제는 반대쪽 끝(front)에서 이루어지는 선형 자료 구조다. 갱신 정책은 FIFO(First In, First Out) — 가장 먼저 삽입된 원소가 가장 먼저 삭제된다.

## Capabilities

- **Enqueue**: rear에 원소 삽입
- **Dequeue**: front에서 원소 삭제 및 반환
- **Front**: 삭제 없이 front 원소 조회
- 프로세스 스케줄링, BFS(너비 우선 탐색), 네트워크 패킷 버퍼, 프린터 작업 큐 등에 활용

## Limitations

- front와 rear 이외의 위치에 있는 원소에 직접 접근 불가
- 우선순위 기반 처리가 필요한 경우 FIFO 정책 부적합 → [[priority-queue]] 사용 필요
- 배열 기반 구현 시 원형 큐(circular queue) 없이는 앞쪽 공간 낭비 발생

## Relationships

- [[abstract-data-type]] (Queue는 ADT로 정의됨)
- [[stack]] (반대 갱신 정책인 LIFO 선형 구조)
- [[priority-queue]] (Queue의 변형 — 도착 순서 대신 우선순위 기반으로 원소 선택)

## Sources

- raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf (p.7)
