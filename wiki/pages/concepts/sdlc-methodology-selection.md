---
title: SDLC Methodology Selection
category: concept
tags: [sdlc, methodology, project-management, waterfall, agile, rad]
sources: [raw/시스템분석/ch02-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
SDLC(Systems Development Life Cycle) methodology selection은 프로젝트에 가장 적합한 개발 방법론을 선택하는 의사결정 과정이다. Methodology는 SDLC를 구현하기 위한 공식화된 접근법(formalized approach)으로, 수행할 단계들과 산출물(deliverables)의 집합으로 구성된다.

## How It Works
방법론 선택에 영향을 미치는 여섯 가지 요인은 다음과 같다.
1. **Clarity of User Requirements** — 사용자 요구사항의 명확성
2. **Familiarity with Technology** — 팀의 기술 친숙도
3. **System Complexity** — 시스템 복잡도
4. **System Reliability** — 시스템 신뢰성 요구 수준
5. **Time Frame** — 프로젝트 기간 제약
6. **Schedule Visibility** — 일정의 가시성 요구

방법론은 출처에 따라 조직 내부 개발, 컨설팅사, 소프트웨어 벤더, 정부기관 등에서 도입할 수 있다.

### 방법론별 적합성 비교

| 요인 | Waterfall | Parallel | V-Model | Iterative | System Prototyping | Throwaway Prototyping | Agile |
|------|-----------|----------|---------|-----------|--------------------|-----------------------|-------|
| 불명확한 요구사항 | Poor | Poor | Poor | Good | Excellent | Excellent | Excellent |
| 낯선 기술 | Poor | Poor | Poor | Good | Poor | Excellent | Poor |
| 복잡한 시스템 | Good | Good | Good | Good | Poor | Excellent | Poor |
| 신뢰성 요구 | Good | Good | Excellent | Good | Poor | Excellent | Good |
| 짧은 기간 | Poor | Good | Poor | Excellent | Excellent | Good | Excellent |
| 일정 가시성 | Poor | Poor | Poor | Excellent | Excellent | Good | Good |

## Key Properties
- 하나의 방법론이 모든 상황에 최적이지 않으며, 프로젝트 특성에 맞는 선택이 필요하다.
- 방법론은 크게 세 범주로 구분된다: Structured Systems Development, RAD(Rapid Application Development), Agile.
- Throwaway Prototyping은 유일하게 모든 요인에서 Good 이상의 적합도를 보인다.
- 불명확한 요구사항 환경에서는 Structured 계열보다 RAD 또는 Agile이 우수하다.

## Relationships
- [[structured-systems-development]] (Waterfall, Parallel, V-Model을 포함하는 구조적 개발 방법론)
- [[rapid-application-development]] (Iterative, System Prototyping, Throwaway Prototyping을 포함하는 RAD)
- [[agile-development-methodology]] (XP, Scrum 등 Agile 방법론)
- [[project-selection]] (방법론 선택은 프로젝트 승인 직후 첫 번째 작업)

## Open Questions
- 실제 프로젝트에서 여러 방법론을 혼합하는 hybrid approach는 어떻게 평가되는가?
- 방법론 선택을 지원하는 의사결정 지원 도구나 자동화 프레임워크가 존재하는가?
- 조직의 성숙도(maturity)나 팀 규모가 방법론 선택에 어떤 영향을 미치는가?

## Sources
- raw/시스템분석/ch02-1.pdf (pp. 8–27)
