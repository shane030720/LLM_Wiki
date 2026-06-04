---
title: Scope Creep
category: concept
tags: [project-management, scope, risk, sdlc]
sources: [raw/시스템 분석 이론/ch02-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Scope Creep(범위 잠식)은 프로젝트 진행 중 초기에 정의되지 않은 요구사항이나 기능이 공식적인 변경 검토 없이 점진적으로 추가되어 프로젝트 범위가 통제되지 않게 확장되는 현상이다. 개별 추가는 사소해 보이지만 누적되면 일정 지연, 비용 초과, 품질 저하를 초래하는 주요 프로젝트 위험 요소다.

## How It Works

1. **비공식 요구사항 추가**: 이해관계자가 개발 과정에서 "작은" 기능 추가를 공식 절차 없이 비공식적으로 요청한다.
2. **점진적 누적**: 개별 추가는 사소해 보이지만 반복되면 상당한 범위 확장으로 이어진다.
3. **삼중 제약 파괴**: 증가된 범위를 기존 예산과 일정 안에서 완수해야 한다는 압박이 발생하여 범위·시간·비용의 균형이 무너진다.
4. **품질 저하 연쇄**: 추가 기능을 수용하기 위해 설계 결정을 서두르거나 검토를 생략하게 되어 시스템 품질이 저하된다.

## Key Properties

- **점진성(Incremental Nature)**: 한 번에 눈에 띄게 나타나지 않고 서서히 누적되어 인지가 어려움
- **비공식성(Informal Origin)**: 공식 변경 통제 프로세스(formal change approval process)를 우회하여 발생
- **삼중 제약 영향**: 범위(Scope), 시간(Time), 비용(Cost) 세 요소 모두에 부정적 영향을 미침
- **예방 가능성**: 적절한 변경 통제 프로세스와 명확한 요구사항 관리로 예방 가능
- **압력 기반 발생**: 사용자나 이해관계자의 선의에서 비롯된 추가 요청이 누적되어 발생하는 경우가 많음

## Relationships

- [[timeboxing]] — Timeboxing은 범위 증가 압력에 구조적으로 대응하는 핵심 기법이다
- [[project-estimation-and-planning]] — Scope Creep은 초기 추정 및 계획을 무력화하는 주요 위험 요소다
- [[rapid-application-development]] — 프로토타이핑은 초기에 실제 요구사항을 명확히 하여 범위 잠식 압력을 최소화한다
- [[requirement-engineering]] — 명확하고 완전한 요구사항 정의는 Scope Creep 예방의 기초다
- [[agile-development-methodology]] — 애자일은 짧은 반복 주기와 백로그 관리로 Scope Creep을 구조적으로 제어하지만, 동시에 변경 유연성으로 인해 발생 가능성도 존재한다
- [[project-portfolio-management]] — PPM은 포트폴리오 수준에서 범위 변경이 전체 자원 배분에 미치는 영향을 추적한다

## Open Questions

- 완전히 새로운 요구사항인지 아니면 기존 요구사항의 정당한 명확화인지를 어떻게 일관성 있게 구분하는가?
- 고객 관계를 유지하면서도 Scope Creep 요청을 거부하려면 어떤 접근이 효과적인가?
- 애자일 방법론에서 변경 수용(agility)과 범위 통제(scope control)의 경계는 어떻게 설정하는가?

## Sources

- raw/시스템 분석 이론/ch02-1.pdf (p. 35)
