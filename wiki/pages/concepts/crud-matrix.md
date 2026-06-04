---
title: CRUD Matrix
category: concept
tags: [data-modeling, validation, process-model, systems-analysis, erd]
sources: [raw/시스템 분석 이론/ch06-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

CRUD Matrix는 시스템의 프로세스(또는 유스케이스)와 데이터 엔티티를 교차 참조하여 각 프로세스가 각 엔티티에 대해 수행하는 연산(Create, Read, Update, Delete)을 기록하는 검증 도구다. 데이터 모델(ERD)과 프로세스 모델(DFD)의 균형(balancing)을 확인하는 데 사용된다.

## How It Works

CRUD Matrix는 2차원 표 형태로 구성된다.

- **행(Row)**: 시스템 내 프로세스 또는 유스케이스
- **열(Column)**: ERD에서 도출된 데이터 엔티티
- **셀(Cell)**: 해당 프로세스가 해당 엔티티에 수행하는 연산 — C(Create), R(Read), U(Update), D(Delete) 또는 조합

**분석 과정**:
1. 각 프로세스가 어떤 엔티티를 어떤 방식으로 사용하는지 셀을 채운다.
2. 모든 열에 최소 하나의 C(Create) 연산이 존재하는지 확인한다 — 없으면 해당 엔티티에 데이터를 생성하는 프로세스가 누락된 것이다.
3. 열 전체가 공백인 엔티티는 사용되지 않는 불필요한 엔티티일 가능성이 있다.
4. 행 전체가 R만 있거나 C/U/D가 없는 프로세스는 데이터 생성/변경 책임이 불명확한 것이다.

**식별 가능한 결함**:
- 데이터는 존재하지만 이를 생성하는 프로세스 없음 → 프로세스 누락
- 프로세스는 존재하지만 필요한 데이터 엔티티 없음 → 엔티티 누락
- 엔티티가 어떤 프로세스에서도 참조되지 않음 → 불필요한 엔티티

## Key Properties

- ERD(엔티티)와 DFD(프로세스)의 완전성(completeness)과 일관성(consistency)을 교차 검증한다.
- 각 엔티티에 대해 반드시 C(Create) 연산을 수행하는 프로세스가 하나 이상 존재해야 한다.
- 데이터 소유권(ownership)과 책임 소재를 명확히 한다.
- 많은 CASE 도구가 CRUD Matrix를 자동으로 생성하거나 불균형을 탐지하는 기능을 제공한다.
- 분석 단계의 검증 산출물로, 설계 단계 진입 전 데이터 모델의 품질을 높인다.

## Relationships

- [[entity-relationship-diagram]] — CRUD Matrix의 열은 ERD에서 도출된 엔티티로 구성됨
- [[data-flow-diagram]] — CRUD Matrix의 행은 DFD의 프로세스와 대응됨
- [[data-modeling]] — CRUD Matrix는 논리 데이터 모델 검증의 핵심 기법
- [[use-case]] — 유스케이스를 행으로 사용하는 변형 CRUD Matrix도 활용됨
- [[database-normalization]] — CRUD Matrix 검증 이후 정규화를 통해 데이터 모델을 추가로 정제함

## Open Questions

- CRUD Matrix에서 하나의 셀에 여러 연산(예: CRU)이 동시에 발생하는 경우, 우선순위 또는 조건부 논리를 어떻게 표현해야 하는가?
- 마이크로서비스 아키텍처처럼 데이터 소유권이 서비스 경계로 분산된 환경에서 CRUD Matrix를 어떻게 적용할 수 있는가?

## Sources

- raw/시스템 분석 이론/ch06-1.pdf (pp. 38–39)
