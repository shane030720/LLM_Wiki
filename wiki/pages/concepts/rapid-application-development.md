---
title: Rapid Application Development (RAD)
category: concept
tags: [rad, prototyping, iterative, methodology, sdlc, case-tool]
sources: [raw/시스템분석/ch02-1.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Rapid Application Development(RAD)은 특수 기법과 도구(CASE tools, visual programming languages, code generators)를 활용하여 시스템의 일부를 빠르게 개발하고 사용자에게 전달하는 것을 목표로 하는 개발 방법론 범주다. Iterative Development, System Prototyping, Throwaway Prototyping 세 가지 접근법이 포함된다.

## How It Works

### Iterative Development
시스템을 순차적인 버전(version) 시리즈로 개발한다. 사용자는 초기 버전을 빠르게 사용하고, 실제 경험을 바탕으로 추가 요구사항을 식별하여 이후 버전에 반영한다.

- 강점: 사용자가 시스템을 빨리 사용 가능; 실제 경험 기반으로 추가 요구 식별 가능
- 약점: 사용자가 미완성 시스템을 일시적으로 사용해야 함; 완전한 기능의 시스템을 기다려야 함

### System Prototyping
시스템의 거친 버전(rough version)을 빠르게 생성하고, 반복적 정제(repetitive refinement)를 통해 최종 시스템으로 "성장"시킨다.

- 강점: 사용자가 prototype을 매우 빠르게 사용; 피드백 사이클을 통해 실제 요구사항 파악 및 정제
- 약점: 피상적 분석이 문제를 야기할 수 있음; 초기 설계 결정이 잘못될 수 있음; 누락된 기능을 나중에 추가하기 어려울 수 있음

### Throwaway Prototyping
설계 옵션을 실험적으로 탐색하는 데 중점을 둔다. 다양한 설계 옵션 prototype을 만들어 실험하지만, prototype 자체는 버리고(throw away) 학습한 내용을 최종 설계에 반영한다.

- 강점: 불확실성 최소화; 최종 시스템 구축 전 중요한 이슈를 충분히 이해
- 약점: System Prototyping에 비해 더 오랜 시간이 소요될 수 있음

## Key Properties
- CASE tools, visual programming languages, code generators 등 특수 도구를 활용한다.
- 빠른 가시적 결과물 제공이 핵심 목적이다.
- 불명확한 사용자 요구사항 환경에서 특히 효과적이다(Good~Excellent).
- Throwaway Prototyping은 낯선 기술 환경에서 유일하게 Excellent 적합도를 보인다.
- System Prototyping은 복잡한 시스템에서 Poor한 적합도를 보여 한계가 있다.

## Relationships
- [[sdlc-methodology-selection]] (RAD 선택 기준 및 타 방법론과의 비교)
- [[structured-systems-development]] (RAD가 보완하는 전통적 구조적 방법론)
- [[agile-development-methodology]] (RAD와 유사하게 빠른 사이클을 추구하지만, Agile은 완전한 제품 단위로 사이클을 구성)

## Open Questions
- System Prototyping과 Throwaway Prototyping의 실무적 선택 기준은 무엇인가?
- CASE tools와 code generators의 현대적 대응 도구(예: low-code/no-code 플랫폼)와의 관계는?
- RAD와 Agile의 개념적 경계는 어디인가?

## Sources
- raw/시스템분석/ch02-1.pdf (pp. 17–24)
