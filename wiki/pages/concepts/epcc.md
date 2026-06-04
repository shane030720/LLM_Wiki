---
title: EPCC Pattern
category: concept
tags: [pattern, agentic-coding, coding-workflow, harness]
sources: [raw/시스템 분석 실습/7. Harness and Skills.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Definition

EPCC (Explore → Plan → Code → Commit)는 AI 에이전트가 코딩 작업을 수행할 때 따르는 4단계 순차적 워크플로우 패턴이다. 핵심 원칙은 "바로 코딩하지 않고 먼저 읽고 계획한다"는 것으로, 탐색과 계획을 구현 이전에 반드시 선행한다.

## How It Works

1. **Explore (탐색)**: 관련 코드, 파일 구조, 의존성을 먼저 읽고 파악한다. 추측보다 탐색이 우선이며, 이 단계를 생략하면 엉뚱한 파일을 수정하는 실패 패턴이 발생한다.
2. **Plan (계획)**: 탐색 결과를 바탕으로 구현 계획을 수립한다. 어떤 파일을 어떻게 수정할지 명확히 하고, [[harness-engineering]] 의 TASK.md 체크리스트 중 가장 위의 미완료 항목 단 한 개를 선택한다.
3. **Code (구현)**: 계획에 따라 최소한의 변경만 구현한다. 한 번에 하나의 작업만 처리하며, Done when 조건을 만족시키는 최소 변경에 집중한다.
4. **Commit (커밋)**: 테스트·린트·타입 체크 등 자동화된 검증을 통과한 뒤 커밋한다. 커밋 메시지에는 "무엇을"이 아니라 "왜"를 기록한다.

단일 EPCC 사이클이 끝나면 에이전트는 종료하고, 다음 작업은 새 사이클(또는 새 에이전트 세션)에서 처리한다.

## Key Properties

- **선탐색 원칙**: 코드 작성 전 반드시 기존 코드를 읽는다. Plan 없이 Code에 진입하면 엉뚱한 파일 수정 실패가 발생한다.
- **단일 작업 원칙**: 하나의 EPCC 사이클에서 하나의 작업만 처리한다. 한 반복에 두 개 이상의 작업을 처리하는 것은 금지 패턴이다.
- **검증 필수**: Code와 Commit 사이에 반드시 자동화된 검증(pytest, npm test, lint, build 등)을 수행한다. 실패한 테스트를 주석 처리하거나 skip하는 것은 금지된다.
- **저널 기록**: Commit 후 journal에 한 줄 요약(무엇을 했는가, 왜 했는가, 결과)을 append-only로 기록한다.
- **3회 실패 중단 원칙**: 동일한 접근을 3회 실패하면 계속 시도하지 않고 멈추고 사용자에게 보고한다.

## Relationships

- [[harness-engineering]] (EPCC는 하네스 엔지니어링의 Procedure 구성 요소를 구체화한 반복 실행 패턴)
- [[contract-driven-iteration]] (EPCC 각 사이클은 TASK.md의 Contract를 읽고 Done when 조건을 만족시키는 방식으로 Contract-Driven Iteration과 결합됨)
- [[agentic-coding-patterns]] (EPCC는 코딩에 특화된 워크플로우 패턴으로, 5가지 기본 에이전틱 코딩 패턴과 함께 분류됨)
- [[skill]] (Skill 파일은 EPCC의 Explore 및 Plan 단계를 보조하는 절차 정의 역할을 수행)
- [[spec-driven-development]] (Explore 단계는 specs/ 폴더의 명세서와 기존 구현체를 비교하는 것을 포함)

## Open Questions

- EPCC 사이클과 TDD (Red → Green → Refactor)를 통합할 때, Explore 단계에서 실패 테스트를 먼저 작성하는 방식이 표준인가, 아니면 Code 단계에서 테스트와 구현을 함께 진행하는가?
- 대규모 리팩토링처럼 Plan 단계에서 전체 변경 범위를 파악하기 어려운 경우, EPCC의 단일 작업 원칙을 어떻게 유지하는가?
- 멀티 에이전트 환경에서 EPCC를 사용할 때, 각 에이전트가 독립적으로 Explore를 수행하는가, 아니면 Orchestrator가 탐색 결과를 Worker에게 전달하는가?

## Sources

- raw/시스템 분석 실습/7. Harness and Skills.pdf
