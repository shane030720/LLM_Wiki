---
title: Stack
category: entity
tags: [stack, data-structure, lifo, linear-structure]
sources: [raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Overview

Stack(스택)은 삽입과 삭제가 항상 한쪽 끝인 top에서만 이루어지는 선형 자료 구조다. 갱신 정책은 LIFO(Last In, First Out) — 가장 마지막에 삽입된 원소가 가장 먼저 삭제된다.

## Capabilities

- **Push**: top에 원소 삽입
- **Pop**: top에서 원소 삭제 및 반환
- **Peek / Top**: 삭제 없이 top 원소 조회
- 함수 호출 스택(call stack), 괄호 유효성 검사, 후위 표기법(Postfix) 계산, 역순 출력, DFS(깊이 우선 탐색) 등 다양한 알고리즘에 활용

## Limitations

- top 이외의 위치에 있는 원소에 직접 접근 불가
- LIFO 정책으로 인해 임의 순서 접근이 필요한 경우 부적합
- 배열 기반 구현에서는 고정 크기로 인해 오버플로우(overflow) 발생 가능

## Relationships

- [[abstract-data-type]] (Stack은 ADT로 정의됨)
- [[queue]] (반대 갱신 정책인 FIFO 선형 구조)

## Sources

- raw/알고리즘/CH02 자료의 추상화와 기본 자료 구조.pdf (p.6)
