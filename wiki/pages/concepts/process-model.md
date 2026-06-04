---
title: Process Model
category: concept
tags: [process-modeling, systems-analysis, design]
sources: [raw/시스템분석/ch05-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Process Model은 비즈니스 프로세스가 어떻게 운영되는지를 공식적으로 표현하는 방법이다. 수행되는 활동(activity)과 활동 사이에서 데이터가 어떻게 이동하는지를 시각적으로 나타낸다. 크게 두 가지 관점으로 구분된다: 구현 방식을 배제하고 "무엇을" 하는지만 기술하는 Logical Process Model과, 구체적인 구현 정보를 포함하는 Physical Process Model.

## How It Works

- **Logical Process Model**: 프로세스의 논리적 역할과 데이터 변환만 표현하며, 단순히 데이터를 이동시키거나 라우팅하는 프로세스는 생략한다.
- **Physical Process Model**: 기술 스택, 처리 절차 등 구현 수준의 세부사항을 포함한다.

Logical Process Model에 포함되는 프로세스 유형:
- 계산 수행 (예: 평균 학점 계산)
- 의사결정 (예: 주문 상품 가용성 판단)
- 데이터 정렬, 필터링, 요약 (예: 연체 인보이스 식별)
- 데이터를 유용한 정보로 구성 (예: 보고서 생성, 질의 응답)
- 다른 프로세스 트리거 (예: 자동화 명령 전송)
- 저장 데이터 사용 (CRUD 작업)

## Key Properties

- 비즈니스 프로세스를 활동과 데이터 흐름 중심으로 공식화
- Logical / Physical의 이중 관점 제공 — 분석 단계에서는 Logical, 설계·구현 단계에서는 Physical 모델 사용
- Data Flow Diagramming(DFD)이 대표적인 작성 기법
- 시스템 분석가와 사용자 간의 커뮤니케이션 도구로 활용

## Relationships

- [[data-flow-diagram]] — Process Model을 작성하는 대표적인 다이어그램 기법
- [[dfd-elements]] — Process Model을 구성하는 네 가지 기본 요소

## Open Questions

- Logical Model과 Physical Model의 전환 시점(분석 단계 종료 기준)은 프로젝트와 조직마다 다를 수 있으며, 명확한 전환 기준 수립이 필요하다.
- 단순 라우팅 프로세스를 Logical Model에서 생략하는 기준이 분석가의 주관에 따라 달라질 수 있다.

## Sources

- raw/시스템분석/ch05-1.pdf (Dennis, Wixom, Roth — Systems Analysis and Design, 2019, Ch.5)
