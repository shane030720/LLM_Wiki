---
title: Abstract Data Type (ADT)
category: concept
tags: [adt, abstraction, data-structure, interface]
sources: [raw/자료구조/CSE2112_02_week03_1.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

Abstract Data Type(ADT, 추상 자료형)은 자료구조의 추상화(abstraction)다. ADT는 구체적인 구현 방법을 숨기고, **저장되는 데이터**, **데이터에 대한 연산**, **연산과 관련된 오류 조건** 세 가지만을 명세한다. "what"을 정의하되 "how"는 정의하지 않는다.

## How It Works

ADT는 세 가지 구성 요소로 명세된다:

| 구성 요소 | 설명 | 예시 (주식 거래 시스템) |
|-----------|------|------------------------|
| Data stored | 저장되는 데이터의 종류 | 매수/매도 주문(order) |
| Operations | 지원하는 연산의 시그니처 | `order buy(stock, shares, price)`, `order sell(...)`, `void cancel(order)` |
| Error conditions | 연산 실패 조건 | 존재하지 않는 주식 매수/매도, 존재하지 않는 주문 취소 |

C++에서는 순수 가상 함수(pure virtual function)를 가진 추상 클래스나 인터페이스 클래스로 ADT를 표현한다. 구현은 ADT를 상속받은 구체적 클래스(concrete class)에서 이루어진다.

## Key Properties

- **구현 독립성(Implementation independence)**: 동일한 ADT를 배열, 연결 리스트, 트리 등 다양한 방식으로 구현할 수 있다
- **인터페이스와 구현의 분리**: 사용자는 내부 구현을 몰라도 ADT의 연산을 사용할 수 있다
- **오류 조건 명세**: 유효하지 않은 연산 호출에 대한 동작을 미리 정의한다 (예외 발생 등)
- **타입 추상화**: 저장되는 데이터의 타입을 제네릭(generic)하게 정의할 수 있다

## Relationships

- [[stack]] — Stack은 ADT의 대표적 예시로, push/pop/top/size/empty 연산과 StackEmpty 오류 조건을 명세한다
- [[singly-linked-list]] — Singly Linked List는 구체적(concrete) 자료구조로, ADT의 한 가지 구현체다
- Queue (미작성) — Stack과 함께 대표적인 선형 ADT이며, FIFO 원칙을 따른다

## Open Questions

- C++에서 ADT를 표현하는 방법(순수 가상 함수, 개념(concept), 덕 타이핑)들 사이의 트레이드오프는 무엇인가?
- ADT의 오류 조건을 예외(exception)로 처리하는 방식 vs 반환값(error code)으로 처리하는 방식 중 현대 C++ 설계에서 어느 것이 더 선호되는가?

## Sources

- raw/자료구조/CSE2112_02_week03_1.pdf (Week 03 – Lecture 01, 슬라이드 30)
