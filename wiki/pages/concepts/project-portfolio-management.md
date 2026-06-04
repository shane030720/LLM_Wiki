---
title: Project Portfolio Management
category: concept
tags: [project-management, portfolio, planning, sdlc]
sources: [raw/시스템 분석 이론/ch02-1.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

Project Portfolio Management(PPM)은 조직 내 모든 프로젝트(진행 중인 것과 승인 대기 중인 것)를 하나의 포트폴리오로 통합하여 관리하는 접근법이다. 개별 프로젝트를 독립적으로 평가하는 대신, 전체 포트폴리오 관점에서 균형 잡힌 프로젝트 조합을 선택하고 유지하는 것을 목표로 한다. 타당성이 충분한 프로젝트도 포트폴리오 균형을 이유로 기각되거나 연기될 수 있다.

## How It Works

1. **정보 수집**: PPM 소프트웨어가 진행 중인 프로젝트와 승인 대기 프로젝트 전체에 대한 정보를 수집·관리한다.
2. **프로젝트 평가**: 승인 위원회(approval committee)는 [[system-request]](시스템 요청서)와 [[feasibility-analysis]](타당성 분석)를 활용하여 각 프로젝트를 포트폴리오 관점에서 평가한다.
3. **포트폴리오 균형 결정**: 개별 프로젝트의 타당성뿐 아니라 전체 포트폴리오 내에서의 적합성(크기, 위험, 목적, 경제적 가치의 균형)을 고려하여 선택, 연기, 또는 기각을 결정한다.
4. **지속적 적응**: 변화하는 비즈니스 환경에 맞춰 포트폴리오를 실시간으로 모니터링하고 조정한다.

## Key Properties

- **프로젝트 우선순위 결정(Project Prioritization)**: 자원 제약 하에서 가장 가치 있는 프로젝트를 우선 선택
- **인력 배분(Employee Allocation)**: 포트폴리오 전체에 걸쳐 인력 자원을 효율적으로 분배
- **실시간 모니터링(Real-time Monitoring)**: 진행 중인 프로젝트 상태를 지속적으로 추적
- **분산 지표 감지(Variance Flagging)**: 비용 및 일정 편차를 자동으로 감지하고 경고
- **경제적 타당성 추적**: 승인 이후에도 프로젝트의 경제적 가치를 지속 모니터링
- **트레이드오프 수용**: 타당성이 충분한 프로젝트도 포트폴리오 균형을 위해 기각하거나 연기 가능

## Relationships

- [[project-selection]] — PPM은 프로젝트 선택 프로세스의 상위 개념으로, 개별 선택 결정을 포트폴리오 수준에서 조율한다
- [[feasibility-analysis]] — 타당성 분석 결과는 PPM 승인 위원회의 핵심 입력 자료로 사용된다
- [[system-request]] — 시스템 요청서는 PPM 위원회가 프로젝트를 평가하는 기초 문서다
- [[project-estimation-and-planning]] — PPM은 개별 프로젝트의 추정 및 계획 정보를 집계하여 포트폴리오 수준에서 분석한다
- [[sdlc]] — PPM은 SDLC 시작점인 프로젝트 선택 단계를 포트폴리오 관점에서 지원한다

## Open Questions

- PPM 소프트웨어 인프라가 없는 소규모 조직은 어떤 방식으로 포트폴리오 균형을 관리하는가?
- 경제적 가치가 높은 프로젝트가 포트폴리오 균형 이유로 기각될 때, 그 결정의 객관적 기준은 무엇인가?
- 애자일 환경에서 PPM은 짧은 반복 주기의 프로젝트들을 어떻게 동적으로 포트폴리오에 편입시키는가?

## Sources

- raw/시스템 분석 이론/ch02-1.pdf (pp. 3–5)
