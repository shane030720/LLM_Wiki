---
title: Use Case Formats
category: concept
tags: [use-case, casual-format, fully-dressed, requirements, systems-analysis]
sources: [raw/시스템분석/ch04-2.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Use Case Format은 use case를 문서화하는 상세 수준(level of detail)과 구조를 결정하는 작성 방식이다. 크게 casual format(간략 형식)과 fully-dressed format(완전 서술 형식)으로 구분되며, 프로젝트의 복잡도, 위험도, 사용자 참여 수준, 팀 구성 등에 따라 적절한 형식을 선택한다.

## How It Works

두 형식은 공통적으로 use case의 기본 구성요소(이름, 번호, 설명, actor, trigger, normal course, preconditions, postconditions)를 포함한다. 차이는 alternative courses(대안 흐름), 각 단계별 입출력 명세, 전체 입출력 요약 등의 추가 섹션 포함 여부에 있다.

**Casual Format**:
- 기본 구성요소만으로 구성된 간략한 형식
- 사용자와 개발팀이 긴밀히 협력하는 환경에 적합
- 빠른 작성과 유연한 수정이 가능

**Fully-Dressed Format**:
- 매우 철저하고 상세하며 고도로 구조화된 형식
- Alternative courses(대안 흐름) 섹션 추가
- 각 단계별 입출력(inputs and outputs) 명세
- 전체 입출력 요약(summary inputs and outputs) 포함

## Key Properties

- **Fully-Dressed 적용 상황**:
  - 사용자가 개발팀과 긴밀하게 협력하기 어려운 환경
  - 프로젝트의 복잡도(complexity)와 위험도(risk)가 높은 경우
  - 테스트 케이스를 완전하게 기술해야 하는 경우
  - 원격에서 협업하는 팀 간에 상세하고 공유된 사용자 요구사항 이해가 필요한 경우
- **점진적 정제(Gradual Refinement)**: casual format으로 시작해 필요에 따라 fully-dressed로 발전시킬 수 있다.
- **두 독자층 고려**: 사용자(user)와 개발자(developer) 모두가 이해할 수 있도록 작성해야 한다.
- **필요 시에만 작성**: 시스템이 무엇을 해야 하는지 사용자 관점에서 명확히 해야 할 때만 use case를 생성한다.

## Relationships

- [[use-case]] — use case format은 use case를 문서화하는 방식이며, 기본 개념과 구성요소를 따른다
- [[functional-requirements]] — fully-dressed format의 상세 내용은 보다 완전하고 서술적인 functional requirements 도출에 직접 활용된다
- [[test-case]] — fully-dressed format은 테스트 케이스의 완전한 기술을 지원한다

## Open Questions

- Casual format과 fully-dressed format 사이에 중간 단계의 표준화된 형식이 필요한 경우는 어떻게 대응하는가? 실무에서 조직마다 커스터마이즈된 형식을 사용하는 것이 일반적인가?
- Fully-dressed format을 적용하는 기준("high complexity and high risk")의 측정 방법이 교재에서 구체적으로 제시되지 않는다. 위험도와 복잡도를 정량적으로 평가하는 방법론과 연계하면 어떠한가?

## Sources

- raw/시스템분석/ch04-2.pdf — Dennis, Wixom, Roth, *Systems Analysis and Design*, 2019, Chapter 4-2: Use Case Analysis
