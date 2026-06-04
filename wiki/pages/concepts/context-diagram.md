---
title: Context Diagram
category: concept
tags: [process-modeling, dfd, systems-analysis, context]
sources: [raw/시스템 분석 이론/ch05-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Context Diagram은 모든 process model에서 최상위에 위치하는 DFD이다. 전체 시스템을 하나의 단일 프로세스(Process 0)로 표현하고, 시스템과 상호작용하는 모든 external entity 및 주요 data flow를 보여줌으로써 시스템이 위치한 비즈니스 맥락(context)을 정의한다.

## How It Works

Context Diagram을 작성하는 절차는 다음과 같다.

1. 시스템 전체를 하나의 원(Process 0)으로 표현한다.
2. 시스템에 데이터를 공급하거나 시스템으로부터 데이터를 수신하는 모든 external entity를 식별하여 다이어그램 외곽에 배치한다.
3. 각 external entity와 Process 0 사이의 주요 data flow(inflow/outflow)를 화살표로 표시한다.
4. Data store와 내부 프로세스는 포함하지 않는다. 내부 구조는 [[dfd-hierarchy]]의 Level 0 다이어그램 이하에서 표현된다.

Context Diagram이 완성되면 이는 [[dfd-hierarchy]]에서 Level 0 다이어그램으로 분해(decompose)되는 출발점이 된다.

## Key Properties

- 전체 시스템을 단 하나의 Process(Process 0)로 표현
- 모든 external entity를 빠짐없이 포함해야 함
- Data store를 포함하지 않음 (내부 저장 구조를 숨김)
- 내부 프로세스 분리 없이 시스템 경계(system boundary)만 명시
- 시스템의 입력 및 출력 데이터를 전체적으로 조망하는 가장 추상화된 뷰

## Relationships

- [[dfd-hierarchy]] — Context Diagram은 DFD 계층 구조의 최상위이며, Level 0 다이어그램으로 분해됨
- [[dfd-elements]] — 작성에 사용되는 Process, Data Flow, External Entity 요소 정의
- [[data-flow-diagram]] — Context Diagram은 DFD의 한 종류
- [[process-model]] — Context Diagram이 포함되는 더 넓은 개념 틀

## Open Questions

- Context Diagram에 control flow(dashed-line)를 포함해야 하는지, 아니면 data flow만으로 제한해야 하는지에 대한 관행이 교재마다 다를 수 있다.
- 동일한 external entity가 여러 주요 data flow를 가질 때, Context Diagram에서 모든 flow를 개별적으로 표시해야 하는지 또는 집약적으로 표시해야 하는지는 프로젝트 규모에 따라 판단이 달라진다.

## Sources

- raw/시스템 분석 이론/ch05-1.pdf (p.16)
