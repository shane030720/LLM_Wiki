---
title: Project Selection and Portfolio Management
category: concept
tags: [project-management, portfolio, sdlc, selection, feasibility]
sources: [raw/시스템분석/ch02-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Project selection은 조직이 수행할 IT 프로젝트를 식별하고 우선순위를 결정하는 과정이다. 승인 위원회(approval committee)는 system request와 feasibility study를 바탕으로 프로젝트를 평가하며, 개별 프로젝트의 타당성뿐 아니라 전체 project portfolio 내에서의 적합성을 함께 고려한다.

## How It Works
프로젝트는 다음 기준으로 분류된다: size, cost, purpose, length, risk, scope, economic value.

승인 위원회는 system request와 feasibility study를 검토한 뒤 아래 절차로 의사결정을 내린다.
1. Project portfolio perspective 적용 — 개별 프로젝트가 전체 포트폴리오에 어떻게 부합하는지 평가한다.
2. 균형 잡힌 project portfolio 구성을 위한 trade-off를 수행한다.
3. 개별적으로는 타당한 프로젝트도 포트폴리오 이슈로 인해 거절(reject) 또는 연기(defer)될 수 있다.

Project Portfolio Management(PPM) 소프트웨어는 진행 중인 프로젝트와 승인 대기 중인 프로젝트의 정보를 수집·관리하며, 다음 기능을 제공한다.
- Project prioritization
- Employee allocation
- Real-time project monitoring
- Cost 및 time variance flagging
- Economic feasibility monitoring

프로젝트 승인 후 project manager는 다음 네 가지 작업을 수행한다.
1. 최적 project methodology 선택
2. Project work plan 수립
3. Staffing plan 수립
4. 프로젝트 조정·통제(coordination and control) 방법 설계

## Key Properties
- 개별 프로젝트의 타당성과 포트폴리오 전체의 균형을 모두 고려한다.
- PPM 소프트웨어를 통해 실시간으로 변화하는 조건에 적응 가능하다.
- 타당한 프로젝트도 포트폴리오 관점에서 거절 또는 연기될 수 있다.
- 프로젝트 선정 기준은 단일 지표가 아니라 복합적 특성(size, cost, risk 등)으로 구성된다.

## Relationships
- [[sdlc-methodology-selection]] (선정된 프로젝트에 적용할 개발 방법론 선택)
- [[project-estimation-and-planning]] (프로젝트 승인 후 work plan 수립 과정)

## Open Questions
- PPM 소프트웨어의 구체적인 도구 선택 기준과 시장 대표 제품은 무엇인가?
- Feasibility study의 구체적 구성 요소(기술적·경제적·운영적 타당성)는 별도 챕터에서 다루어지는가?
- 포트폴리오 균형을 평가하는 정량적 프레임워크가 존재하는가?

## Sources
- raw/시스템분석/ch02-1.pdf (pp. 2–6)
