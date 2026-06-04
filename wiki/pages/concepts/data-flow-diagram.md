---
title: Data Flow Diagram (DFD)
category: concept
tags: [dfd, process-modeling, systems-analysis, decomposition]
sources: [raw/시스템분석/ch05-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Data Flow Diagram(DFD)은 프로세스 모델을 작성하기 위한 대표적인 기법으로, 시스템 내에서 데이터가 어떻게 흐르고 처리되는지를 계층적 다이어그램으로 표현한다. 비즈니스 프로세스의 복잡성을 다루기 위해 Decomposition(분해) 원칙에 따라 여러 레벨의 계층 구조를 사용한다.

## How It Works

### 계층 구조 (DFD Hierarchy)

| 레벨 | 명칭 | 설명 |
|------|------|------|
| 최상위 | Context Diagram (Process 0) | 전체 시스템을 단일 프로세스로 표현, 외부 엔티티와의 관계만 표시 |
| Level 0 | Level 0 Diagram | Context Diagram의 내부 주요 프로세스 분해, Data Store 추가 |
| Level 1 | Level 1 Diagram | Level 0의 각 프로세스를 하위 프로세스로 분해 |
| Level 2 | Level 2 Diagram | Level 1의 프로세스를 필요에 따라 추가 분해 |

분해는 각 프로세스가 단일 목적의 Primitive Process가 될 때까지 계속된다.

### 프로세스 번호 체계 (Diagram Numbering)

계층 내 위치를 명확히 나타내기 위해 점(dot) 구분자를 사용한다:
- Context Diagram: Process 0
- Level 0: 정수 (1, 2, 3, ...)
- Level 1: 부모번호.고유번호 (1.1, 1.2, 1.3, ...)
- Level 2: 부모번호.고유번호.고유번호 (1.1.1, 1.1.2, ...)

### Balancing (균형 원칙)

상위 레벨 DFD와 하위 레벨 DFD 간의 일관성을 보장하는 원칙이다. 부모 다이어그램의 데이터 흐름은 자식 다이어그램에 동일하게 전달되어야 하며, 자식 다이어그램은 새로운 프로세스와 데이터 흐름을 추가로 표현한다.

### DFD 작성 단계

1. Context Diagram 작성: 외부 엔티티와 주요 입출력 데이터 흐름 식별
2. 주요 프로세스 식별: 각 이벤트 / Use Case를 하나의 프로세스로 매핑
3. 각 이벤트 / Use Case에 대한 DFD Fragment(미니 다이어그램) 개별 작성
4. DFD Fragment를 Level 0 다이어그램으로 통합
5. Level 0의 각 프로세스를 Level 1 다이어그램으로 분해, 필요 시 Level 2까지 진행
6. 사용자와 DFD 검증(Validation) — 완전성 및 정확성 확인

### Use Case 통합

DFD는 Use Case와 요구사항 정의로부터 도출된다:
- Use Case 이름 → Level 0의 주요 프로세스 이름
- Use Case의 각 단계 → Level 1의 하위 프로세스
- 입출력 항목 → Level 1 이하의 데이터 흐름

### 공통 오류 유형

- **Syntax Error (구문 오류)**: 모든 Data Flow는 반드시 Process와 연결되어야 함; 모든 Process는 최소 하나의 입력과 출력을 가져야 함
- **Semantics Error (의미 오류)**: 입력이 논리적으로 출력을 생성하기에 충분한지 확인; 일관된 분해 수준 유지; 용어의 일관된 사용

## Key Properties

- 계층적 분해(Hierarchical Decomposition)를 통한 복잡성 관리
- Balancing을 통한 레벨 간 데이터 흐름 일관성 보장
- Use Case와의 직접적 연계로 요구사항-모델 간 추적성 확보
- Alternative Data Flow: 조건(IF 분기)에 따라 다른 데이터 흐름을 함께 표시
- Process Description(Structured English, Decision Tree, Decision Table)으로 복잡한 로직 보완 가능
- CASE 도구를 통해 프로세스 설명 및 다이어그램 작성 자동화 지원

## Relationships

- [[process-model]] — DFD가 구현하는 상위 개념
- [[dfd-elements]] — DFD를 구성하는 네 가지 기본 요소

## Open Questions

- Primitive Process(원자 프로세스)의 정의 기준은 분석가의 판단에 의존하며, 지나친 분해 또는 부족한 분해를 피하기 위한 객관적 기준 정립이 필요하다.
- DFD와 UML Activity Diagram, BPMN 등 다른 프로세스 모델링 표기법과의 적합한 사용 상황 구분에 대한 추가 탐구가 필요하다.

## Sources

- raw/시스템분석/ch05-1.pdf (Dennis, Wixom, Roth — Systems Analysis and Design, 2019, Ch.5)
