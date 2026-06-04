---
title: Software Engineering Evolution
category: concept
tags: [software-engineering, history, AI, paradigm-shift, intelligent-systems]
sources: [raw/시스템 분석 실습/1. Vibe coding and Agent coding.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Software Engineering Evolution(소프트웨어 엔지니어링의 진화)은 소프트웨어 개발 패러다임이 역사적으로 거쳐온 세 단계의 전환을 가리킨다. 하드웨어 종속 단계, 추상화·프레임워크 단계를 거쳐 2024년 이후 자연어·의도 기반의 지능형 시스템 시대로 진입하였다. 각 단계는 지배적인 추상화 수준의 변화로 정의되며, 현재의 AI-Assisted 개발 패러다임은 세 번째 단계의 산물이다.

## How It Works

각 단계는 사용 가능한 추상화 도구의 수준이 높아질수록 개발자가 다루는 문제의 차원이 달라진다는 원리로 전환된다.

### 1단계: 하드웨어 종속 단계 (Hardware-Dependent Era, 1940s~)

- 물리 회로, 천공 카드, 어셈블리 언어
- 개발자가 하드웨어 명령어 수준에서 직접 작업
- 추상화 없이 기계의 언어로 사고해야 함

### 2단계: 추상화·프레임워크 단계 (Abstraction/Framework Era, ~2024)

- 컴파일 언어(C, Java 등), 인터프리터 언어(Python, JavaScript 등)
- 후기: 클라우드 인프라, 프레임워크, 패키지 생태계
- 인간이 구문(syntax)과 로직을 직접 작성하고, 컴파일·테스트로 반복 개선
- 기계보다는 개념 수준에서 작업하나, 여전히 코드 작성이 중심

### 3단계: 지능형 시스템 시대 (Intelligent Systems Era, 2024~)

- 자연어·의도 기반 프로그래밍(Natural Language / Intent-based Programming)
- AI-Assisted 개발 + 자동화
- 개발자는 목표와 제약을 자연어로 기술하고, LLM이 코드를 생성
- Vibe Coding(2024 4Q~2025 3Q)과 Agentic Coding(2025 4Q~)이 이 시대의 대표 패턴

참조 문헌: "The End of Programming as We Know It" (O'Reilly), Dario Amodei (CEO of Anthropic)

## Key Properties

- 단방향 진행성: 각 단계는 이전 단계를 대체하는 방향으로 진행, 역행 사례 없음
- 추상화 수준 상승: 단계가 높아질수록 개발자가 다루는 추상화 수준이 올라감
- 역할 전환: 코드 작성자(coder)에서 명세 작성자(specifier)·검증자(verifier)로 엔지니어 역할이 이동
- 기술 부채 위험: 3단계 초기(Vibe Coding)에는 생성 코드의 일관성·검증 문제로 기술 부채가 빠르게 축적되는 부작용이 나타남
- SDLC 재통합: Agentic Coding 등장으로 코딩 에이전트를 통해 SDLC가 보장되는 개발 프로세스 수행이 가능해짐

## Relationships

- [[vibe-coding]] (3단계 초기를 대표하는 자연어 기반 개발 패턴, 2024 4Q~2025 3Q)
- [[agentic-coding]] (3단계 성숙기 패턴으로 SDLC 보장을 목표로 함, 2025 4Q~)
- [[vibe-vs-agentic-coding]] (두 패턴의 차이를 비교하는 분석 페이지)
- [[sdlc]] (2단계의 핵심 개발 방법론, 3단계에서도 에이전트에 의해 재활용됨)
- [[spec-driven-development]] (3단계에서 명세가 개발의 중심이 되는 패러다임)
- [[agentic-coding-patterns]] (지능형 시스템 시대에 등장한 구체적 개발 패턴들)

## Open Questions

- "The End of Programming as We Know It"이 의미하는 바가 프로그래밍의 완전한 종말인가, 아니면 추상화 수준 상승에 따른 역할 재정의인가?
- 3단계에서 소프트웨어 엔지니어에게 요구되는 핵심 역량은 무엇인가? 구문 지식 없이 시스템 설계 능력만으로 충분한가?
- Agentic Coding이 SDLC를 보장한다고 하나, 에이전트가 만든 산출물에 대한 책임 소재는 어떻게 결정되는가?

## Sources

- raw/시스템 분석 실습/1. Vibe coding and Agent coding.pdf (p.6~p.9)
