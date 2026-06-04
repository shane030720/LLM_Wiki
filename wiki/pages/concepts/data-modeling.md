---
title: Data Modeling
category: concept
tags: [data-model, systems-analysis, logical-model, physical-model, erd]
sources: [raw/시스템분석/ch06-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Data Model이란 비즈니스 시스템이 사용하고 생성하는 데이터를 공식적으로 표현하는 방법이다. 데이터가 포착되는 사람(person), 장소(place), 사물(thing)과 그들 간의 관계(relationship)를 시각적으로 표현한다. 두 가지 유형으로 구분된다.

- **Logical Data Model**: 데이터가 저장·생성·조작되는 방식은 나타내지 않고, 데이터의 논리적 조직만 표현한다.
- **Physical Data Model**: 데이터가 실제로 데이터베이스나 파일에 어떻게 저장될지를 나타낸다.

## How It Works

데이터 모델링은 분석(Analysis) 단계에서 수행되며, 반복적인(iterative) 시행-수정 과정을 통해 구축된다. 주요 절차는 다음과 같다.

1. **Entity 식별**: 시스템 내 주요 정보 범주(data stores, 외부 엔터티, use case 입출력)를 검토하여 entity를 도출한다. 반드시 복수의 인스턴스가 존재해야 entity로 인정된다.
2. **Attribute 추가**: 프로세스 모델 저장소, 요구사항 정의서, 사용자 인터뷰, 기존 양식 분석 등을 통해 각 entity에 관련 속성을 부여한다. Identifier(식별자)의 최종 결정은 설계(Design) 단계로 미룰 수 있다.
3. **Relationship 연결**: entity 간 관련 있는 쌍을 연결하고, 적절한 동사 구문으로 관계를 기술한다. 비즈니스 규칙 논의를 통해 Cardinality와 Modality를 결정한다.

데이터 모델과 프로세스 모델(DFD)은 균형(balance)을 이루어야 하며, CRUD Matrix를 사용해 entity와 프로세스 간 상호작용을 검증한다.

## Key Properties

- **안정성**: 데이터 구조와 속성은 데이터를 사용하는 프로세스보다 훨씬 안정적이고 영속적이다.
- **공유성**: 데이터는 가능한 한 많은 프로세스가 공유할 자원으로 취급되어야 한다.
- **유연성**: 데이터 조직은 예측되지 않은 비즈니스 요구사항에도 유연하고 적응 가능해야 한다.
- **경제성**: 데이터 모델은 프로세스 모델보다 규모가 작고 더 신속하게 구성된다.
- **합의 도구**: 데이터 모델 구성 과정에서 분석가와 사용자가 비즈니스 용어와 규칙에 대한 합의에 빠르게 도달하게 해준다.
- **기존 시스템 유사성**: 신규 시스템의 데이터 모델은 대부분 기존 시스템과 유사하다.

## Relationships

- [[entity-relationship-diagram]] — Data Model을 표현하는 가장 대표적인 다이어그램 기법
- [[normalization]] — 논리적 데이터 모델의 품질을 검증하고 개선하는 기법
- DFD (Data Flow Diagram) — 프로세스 모델로서, 데이터 모델과 균형을 이루어야 하는 상호보완적 산출물

## Open Questions

- Logical Data Model에서 확정되지 않은 identifier는 Design 단계로 미룰 수 있다고 명시되어 있으나, 어떤 기준으로 Analysis 단계에서 결정할 것인지에 대한 구체적 가이드라인이 불명확하다.
- Physical Data Model로의 변환 시점과 책임 주체(분석가 vs 설계자)에 대한 경계가 명확히 정의되어 있지 않다.

## Sources

- raw/시스템분석/ch06-1.pdf — Dennis, Wixom, and Roth, *Systems Analysis and Design*, 2019, Chapter 6
