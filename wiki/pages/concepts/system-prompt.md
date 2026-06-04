---
title: System Prompt
category: concept
tags: [agent-design, prompt-engineering, context, llm]
sources: [raw/시스템 분析 실습/5. Agent Specifications.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트의 역할, 입출력 형식, 제약 조건을 정의하는 지시문. 대화 시작 전 LLM에게 주입되며 에이전트의 전체 행동 방식을 결정한다. Agent Specification의 핵심 구성 요소이자 에이전트 품질을 결정하는 가장 중요한 단일 요소.

## How It Works

**System Prompt 3단계 구조:**

```
1. 분석 (Analysis)   — 입력을 어떻게 이해할 것인가
2. 처리 (Processing) — 어떤 작업을 수행할 것인가
3. 출력 (Output)     — 결과를 어떤 형식으로 반환할 것인가
```

**Planner Agent 시스템 프롬프트 예시:**

```
당신은 소프트웨어 개발 작업을 분석하고 단계별 계획을 수립하는 Planner입니다.

[분석]
주어진 요청에서 다음을 파악하세요:
- 핵심 목표와 제약 조건
- 필요한 기술 스택
- 잠재적 위험 요소

[처리]
다음 구조로 계획을 수립하세요:
1. 작업 분해 (최대 5단계)
2. 각 단계의 입출력 명세
3. 의존 관계 매핑

[출력]
반드시 다음 마크다운 구조로 출력하세요:
## Task Analysis
## Decomposed Steps
## Dependencies
```

**Reviewer Agent 시스템 프롬프트 예시:**

```
당신은 계획의 완전성과 실행 가능성을 검토하는 Reviewer입니다.

[분석]
제공된 계획에서 다음을 평가하세요:
- 누락된 엣지 케이스
- 비현실적인 가정
- 의존 관계 오류

[처리]
1~10점 척도로 품질 점수를 매기고 근거를 제시하세요.
점수 8점 미만이면 구체적 개선 사항을 목록으로 제시하세요.

[출력]
## Score: X/10
## Issues Found
## Recommendations
```

**CLI 에이전트에 시스템 프롬프트 전달:**

```python
cmd = ["claude", "--system-prompt", system_prompt_text]
# 또는 파일로 전달
cmd = ["claude", "--system-prompt-file", "planner_prompt.md"]
```

## Key Properties

- **역할 경계 정의** — 에이전트가 무엇을 해야 하고 무엇을 하지 말아야 하는지 명확히 지정
- **출력 형식 강제** — 다음 에이전트가 파싱 가능한 구조화된 형식으로 출력 유도
- **컨텍스트 압축** — PRD/SRS 전체 대신 핵심 지시만 주입하여 컨텍스트 효율화
- **재사용성** — 동일 시스템 프롬프트로 여러 입력에 대해 일관된 동작 보장

## Limitations

- 시스템 프롬프트가 너무 길면 컨텍스트 윈도우를 과도하게 점유
- 엄격한 출력 형식 강제가 창의적 문제 해결을 제한할 수 있음
- 프롬프트 인젝션 공격에 취약할 수 있음 (외부 입력이 시스템 프롬프트를 덮어쓰는 경우)

## Relationships

- [[agent-pool]] (pool의 각 에이전트 JSON 스키마에 system_prompt 필드가 포함됨)
- [[sequential-agent]] (각 단계의 에이전트는 역할별 시스템 프롬프트로 행동이 구분됨)
- [[harness-engineering]] (시스템 프롬프트가 Preference 컴포넌트의 핵심 내용)
- [[agentic-coding]] (에이전트별 역할 분리의 기반이 되는 시스템 프롬프트)

## Open Questions

- 시스템 프롬프트와 user 턴 프롬프트의 역할 분리 최적 기준은?
- 에이전트의 시스템 프롬프트를 자동으로 최적화하는 방법은?

## Sources

- raw/5. Agent Specifications.pdf
