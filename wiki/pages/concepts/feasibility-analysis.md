---
title: Feasibility Analysis
category: concept
tags: [feasibility, analysis, project, economics, risk]
sources: [raw/시스템분석/ch01-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Feasibility Analysis(타당성 분석)는 제안된 정보시스템 프로젝트가 실제로 추진할 가치가 있는지를 기술적·경제적·조직적 관점에서 평가하는 프로세스다. Planning Phase에서 작성되어 프로젝트의 공식적인 비즈니스 케이스(business case)를 구성하며, 프로젝트 전 기간에 걸쳐 지속적으로 재평가해야 한다.

## How It Works

타당성 분석은 세 가지 차원에서 수행된다:

### 1. Technical Feasibility — "Can We Build It?"
기술적으로 구현 가능한지를 평가한다. 주요 기술적 위험 요인:
- 비즈니스 애플리케이션 영역에 대한 사용자·분석가의 친숙도 부족
- 기술 자체에 대한 낮은 친숙도 (사용 경험 여부, 기술의 신규성)
- 프로젝트 규모 (참여 인원 수, 기간, 기능 범위)
- 기존 시스템과의 호환성 및 통합 필요 정도

### 2. Economic Feasibility — "Should We Build It?"
비용 대비 편익이 충분한지를 평가한다:
- 비용과 편익 식별 및 화폐 가치 환산
- 현금 흐름(cash flow) 산정
- 재무적 타당성 지표 평가:
  - ROI (Return on Investment)
  - 손익분기점(Break Even Point)
  - NPV (Net Present Value) — 할인 현금 흐름(discounted cash flow) 방법이 선호됨
- 비용: 개발 비용(development costs) + 운영 비용(operational costs)
- 편익: 유형 편익(tangible benefits) + 무형 편익(intangible benefits)

### 3. Organizational Feasibility — "If We Build It, Will They Come?"
조직이 이 시스템을 실제로 수용할 수 있는지를 평가한다:
- 전략적 정합성(strategic alignment): 프로젝트 목표와 비즈니스 전략의 일치 여부
- 이해관계자 그룹 분석:
  - 강력하고 영향력 있는 프로젝트 챔피언(project champion) 존재 여부
  - 조직 경영진의 광범위한 지원 여부
  - 시스템 사용자의 수용 또는 저항 성향
- 수용성 제고 방법: 편익 발표, 개인적 이익 강조, 프로토타입 제시, 사용자 실질 참여

## Key Properties

- 세 차원(기술·경제·조직)을 반드시 모두 평가해야 함
- 경제적 타당성에서는 할인 현금 흐름 기반의 NPV 방법이 선호됨
- 타당성 분석은 프로젝트 초기뿐 아니라 전 기간에 걸쳐 재평가해야 함 (critically important to reassess)
- 분석 결과는 Feasibility Study 문서로 집약됨
- 조직적 타당성에서 전략적 정합성이 높을수록 프로젝트 성공 가능성이 높아짐

## Relationships

- [[systems-development-life-cycle]] (Planning Phase의 핵심 산출물이며, 이후 단계에서도 재평가됨)
- [[systems-analyst]] (타당성 분석을 수행하고 Feasibility Study를 작성하는 주체)
- [[business-process-management]] (BPM에서 도출된 비즈니스 필요가 타당성 분석의 입력이 됨)

## Open Questions

- 무형 편익(intangible benefits)의 화폐 가치 환산은 어떤 기준으로 수행하는가?
- 세 가지 타당성 차원 간에 트레이드오프가 발생할 경우(예: 기술적으로는 가능하나 경제적 타당성이 낮음) 어떤 우선순위를 적용해야 하는가?
- 애자일 방법론 환경에서 타당성 분석은 스프린트 단위로 어떻게 재평가하는가?

## Sources

- raw/시스템분석/ch01-1.pdf (pp. 21–28)
