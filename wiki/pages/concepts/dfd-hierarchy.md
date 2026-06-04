---
title: DFD Hierarchy and Decomposition
category: concept
tags: [process-modeling, dfd, systems-analysis, decomposition, balancing]
sources: [raw/시스템 분석 이론/ch05-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

DFD Hierarchy는 복잡한 비즈니스 프로세스를 표현하기 위해 DFD를 의도적인 계층 구조로 조직화하는 방법이다. 최상위의 Context Diagram에서 시작하여 Level 0, Level 1, Level 2 다이어그램으로 단계적으로 분해(decompose)하며, 각 하위 레벨은 상위 레벨 프로세스의 내부 구조를 더 상세하게 표현한다. 분해는 각 프로세스가 단일 목적을 가진 primitive process가 될 때까지 계속된다.

## How It Works

### 계층 구조와 분해

| 레벨 | 내용 | 번호 예시 |
|------|------|-----------|
| Context Diagram | 전체 시스템 = Process 0, 모든 external entity | 0 |
| Level 0 | Context Diagram의 내부: 주요 프로세스 전체 | 1, 2, 3 |
| Level 1 | Level 0의 각 프로세스를 상세화한 별도 다이어그램 | 1.1, 1.2, 2.1, 2.2 |
| Level 2 | Level 1의 프로세스를 추가 상세화 (필요 시) | 1.1.1, 1.1.2, 1.2.1 |

- Level 0은 Context Diagram에 대응하는 내부 구조이며, 주요 프로세스 간의 data flow와 data store를 추가로 표시한다.
- Level 1은 Level 0의 각 프로세스마다 별도로 작성하며, 해당 프로세스의 내부 sub-process를 표현한다.
- Level 2는 필요한 Level 1 프로세스에 대해서만 작성한다.
- 하나의 parent process가 n개의 child process로 분해되면, 그 n개의 child process들이 parent를 완전히 구성한다.

### 번호 체계 (Diagram Numbering)

올바른 번호 부여는 프로세스가 전체 계층 어디에 위치하는지를 명확히 한다.

- Context Diagram: 항상 Process 0
- Level 0 프로세스: 정수 (1, 2, 3, ...)
- Level 1 프로세스: `부모번호.고유번호` (1.1, 1.2, 1.3, ...)
- Level 2 프로세스: `부모번호.고유번호` 두 개의 점 (1.1.1, 1.1.2, ...)

### Balancing (균형 유지)

Balancing은 한 레벨의 DFD에서 표현된 정보가 다음 레벨 DFD에서도 정확히 반영됨을 보장하는 원칙이다.

- 부모 다이어그램의 data flow는 자식 다이어그램에 그대로 이어진다.
- 자식 다이어그램은 새로운 내부 프로세스와 내부 data flow를 추가한다.
- Balancing 위반은 다이어그램 간 불일치(semantic error)를 유발한다.

### DFD 개발 절차

1. Context Diagram 작성 — external entity와 주요 inflow/outflow 식별
2. 주요 프로세스 식별 — 각 event 또는 use case를 처리하는 프로세스 도출
3. 각 use case별 DFD fragment 작성 — 해당 프로세스와 관련 external entity, data store만 포함한 미니 다이어그램
4. Fragment들을 합쳐 Level 0 다이어그램 구성
5. Level 0의 각 프로세스를 Level 1 다이어그램으로 분해; 필요 시 Level 2까지 분해
6. 사용자와 함께 DFD 검증 (완전성·정확성 확인)

### Use Case와의 통합

DFD는 use case 및 요구사항 정의에서 출발하며, 다음과 같이 연결된다.

- Use case의 이름 → Level 0의 주요 프로세스 이름
- Use case의 각 단계 → Level 1의 sub-process
- Use case의 입력/출력 → Level 1 (및 하위) 레벨의 data flow

## Key Properties

- 하향식(top-down) 분해 방식으로 복잡성을 관리
- 각 레벨은 그 위 레벨에 대해 독립적인 내부 뷰를 제공
- Balancing을 통해 레벨 간 데이터 일관성을 보장
- Dotted-number 번호 체계로 계층 위치를 즉시 파악 가능
- Primitive process에 도달할 때까지 분해를 반복 (종료 조건)
- Use case → DFD의 직접적 매핑으로 요구사항 추적성 확보

## Relationships

- [[context-diagram]] — DFD 계층의 최상위 다이어그램 (Process 0)
- [[dfd-elements]] — 각 레벨 다이어그램을 구성하는 기본 요소
- [[data-flow-diagram]] — DFD Hierarchy는 DFD를 구조화하는 방법
- [[use-case]] — use case 이름과 단계가 DFD 계층 구조로 매핑됨
- [[process-description]] — 분해가 완료된 primitive process에 부여하는 텍스트 기반 상세 설명
- [[process-model]] — DFD Hierarchy는 process model 작성의 핵심 기법

## Open Questions

- 실무에서 몇 레벨까지 분해하는 것이 적절한가에 대한 명확한 기준이 없으며, "단일 목적 primitive process"의 정의가 분석가마다 달라질 수 있다.
- Use case 기반으로 DFD fragment를 생성할 때, 여러 use case가 동일한 data store를 공유하면 Level 0 통합 과정에서 중복 요소 처리 방법이 모호해질 수 있다.
- Agile 개발 환경에서 DFD Hierarchy처럼 사전에 전체 계층을 설계하는 방식이 반복적인 요구사항 변화와 어떻게 조화를 이루는지는 추가 연구가 필요하다.

## Sources

- raw/시스템 분석 이론/ch05-1.pdf (p.12–33)
