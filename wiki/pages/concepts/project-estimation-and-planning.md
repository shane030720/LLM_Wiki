---
title: Project Estimation and Planning
category: concept
tags: [project-management, estimation, work-breakdown-structure, scope, timeboxing]
sources: [raw/시스템분석/ch02-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Project estimation and planning은 프로젝트의 시간과 노력에 대한 예측값을 도출하고, 이를 바탕으로 work plan을 수립하며 범위(scope)를 관리하는 일련의 프로젝트 관리 활동이다. 프로젝트 관리자는 scope, time, cost 간의 균형(balancing act)을 지속적으로 조율해야 하며, 이 세 요소 중 하나를 변경하면 나머지도 조정해야 한다.

## How It Works

### Project Estimation
추정의 주요 출처는 사용 방법론, 과거 실제 프로젝트, 경험 있는 개발자 세 가지다. 추정은 처음에는 범위(range)로 시작하여 프로젝트가 진행될수록 점차 구체화된다.

산업 표준 비율(industry standard percentages) 활용 예시:
- Planning: 15%, Analysis: 20%, Design: 35%, Implementation: 30%
- 계산 예: Planning에 4개월 소요 시 → 전체 프로젝트 기간 = 4 ÷ 0.15 ≈ 26.66개월

Function point estimation(부록 2A)도 대안적 추정 기법으로 언급된다.

### Identifying Tasks
태스크 식별에는 네 가지 접근법이 사용된다.
1. 기존 방법론의 가이드라인 활용
2. 이전 프로젝트와의 유사성(analogy) 활용
3. Top-down approach: 상위 작업을 더 작고 상세한 작업으로 분해
4. Work Breakdown Structure(WBS)로 구성

### Managing Scope
Scope creep(범위의 점진적·비공식적 확대)은 프로젝트 실패의 주요 원인이다. 관리 방법은 다음과 같다.
- Prototyping을 통해 scope creep 압력 최소화
- 공식적인 변경 승인 프로세스(formal change approval process) 구현
- 추가 요구사항은 미래 시스템 개선(future enhancements)으로 연기

### Timeboxing
프로젝트가 가용 시간보다 더 많은 시간을 요구할 때 사용하는 기법이다.
1. 타이트하지만 현실적인 데드라인을 설정한다.
2. 핵심적이고 필수적인 기능 요구사항(core, essential functional requirements)을 식별한다.
3. 팀은 핵심 기능에만 집중하며 높은 품질을 유지한다.
4. 나머지 기능은 이후 반복(iteration)에서 추가한다.

## Key Properties
- 프로젝트 관리는 scope, time, cost 간의 지속적인 trade-off를 포함한다.
- 추정은 단일 값이 아닌 범위로 시작하며, 프로젝트 진행에 따라 정확도가 높아진다.
- WBS(Work Breakdown Structure)는 태스크를 계층적으로 구성하는 핵심 도구다.
- Scope creep은 능동적·공식적 관리가 필요한 위험 요소다.
- Timeboxing은 시간 제약을 긍정적으로 활용하여 핵심 가치를 조기에 제공하는 기법이다.

## Relationships
- [[project-selection]] (프로젝트 선정 후 계획 수립으로 이어짐)
- [[sdlc-methodology-selection]] (방법론 선택이 산업 표준 비율 및 추정 기반을 제공)
- [[agile-development-methodology]] (Timeboxing은 Agile의 sprint 개념과 밀접하게 연관)
- [[structured-systems-development]] (산업 표준 비율은 Waterfall의 단계 구성과 연관)

## Open Questions
- Function point estimation의 구체적 계산 방법과 산업 표준 비율 대비 정확도 차이는?
- Work plan의 표준 구성 요소(task, duration, dependency, resource 등)의 세부 정의는?
- Timeboxing 적용 시 핵심 기능 요구사항 선별의 객관적 기준은 무엇인가?
- Scope creep을 조기에 탐지하기 위한 실무적 지표(indicator)는 무엇인가?

## Sources
- raw/시스템분석/ch02-1.pdf (pp. 29–36)
