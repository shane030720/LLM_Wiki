---
title: Entry ADT
category: concept
tags: [adt, key-value, priority-queue, data-structure]
sources: [raw/자료구조/CSE2112_02_week09_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Entry는 key와 value의 쌍(pair)으로 구성된 추상 자료형(ADT)이다. Key는 해당 항목을 식별하거나 순위를 매기는 데 사용되는 값이며, value는 항목이 실제로 담고 있는 데이터를 나타낸다. Priority Queue, Map, Dictionary 등 key 기반 자료구조의 기본 저장 단위로 활용된다.

## How It Works

- 하나의 Entry는 `(key, value)` 쌍으로 표현된다.
- Key는 비교 연산이 가능하도록 **전순서 관계(total order relation)** 를 만족해야 한다 (예: Key1 < Key2, Key1 ≤ Key2).
- 자료구조는 Entry를 삽입(insert)하거나 key를 기준으로 탐색·제거하는 방식으로 동작한다.
- 동일한 key를 가진 여러 Entry가 공존할 수 있다 (non-unique key 허용).

## Key Properties

- Key-value 쌍으로 이루어진 단일 단위
- Key는 단순 정수값일 수도 있고, 복잡한 복합 속성일 수도 있다
- 동일 key를 가진 복수의 Entry 허용 (Priority Queue, Dictionary 등에서)
- Key 비교를 위해 전순서 관계(total order)가 반드시 정의되어야 한다
- Priority Queue에서 key는 곧 우선순위(priority)를 의미한다

## Relationships

- [[priority-queue]] — Entry를 저장하는 대표적인 자료구조; key가 우선순위를 나타내며 `min()`, `removeMin()` 연산의 기준이 된다
- [[map-adt]] — Entry를 저장하는 자료구조; key가 고유 식별자 역할을 하며 중복 key를 허용하지 않는다
- [[dictionary-adt]] — Entry를 저장하며 동일 key를 가진 복수 항목을 허용한다
- [[pq-sort]] — Priority Queue에 Entry를 insert한 뒤 `removeMin()`으로 추출해 정렬하는 알고리즘
- [[heap]] — Priority Queue를 효율적으로 구현하기 위해 Entry를 트리 구조로 관리하는 자료구조

## Open Questions

- Key의 동등성(equality)과 동일성(identity)을 어떻게 구분하는지는 구현 언어와 자료구조에 따라 달라질 수 있다.
- 복합 속성(complex property)을 key로 사용할 때 전순서 관계를 어떻게 정의하는가는 응용마다 설계 결정이 필요하다.

## Sources

- raw/자료구조/CSE2112_02_week09_1.pdf
