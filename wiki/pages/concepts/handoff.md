---
title: Handoff (Handoff File)
category: concept
tags: [agent-communication, pipeline, multi-agent, workflow]
sources: [raw/시스템 분析 실습/4. Plan_mode Sequential and Parallel agents.pdf, raw/5. Agent Specifications.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

멀티 에이전트 파이프라인에서 한 에이전트의 출력을 다음 에이전트의 입력으로 전달하는 마크다운 파일. 에이전트 간 공유 메모리 역할을 하며, 파이프라인의 각 단계가 명확하게 분리되고 추적 가능하도록 한다.

## How It Works

**명명 규칙:**

```
00_planning.md      → 첫 번째 단계 출력
01_review.md        → 두 번째 단계 출력
02_revision.md      → 세 번째 단계 출력
...
04_final_report.md  → 최종 단계 출력
```

숫자 접두사로 파이프라인 순서를 명시하여 의존 관계를 명확히 표현한다.

**파이프라인 내 흐름:**

```
[Planner Agent]
  읽기: user_request.md
  쓰기: 00_planning.md
      ↓
[Reviewer Agent]
  읽기: 00_planning.md
  쓰기: 01_review.md
      ↓
[Reviser Agent]
  읽기: 00_planning.md + 01_review.md
  쓰기: 02_revision.md
      ↓
[Final Reporter]
  읽기: 02_revision.md
  쓰기: 04_final_plan_report.md
```

**Handoff 파일 구조 예시 (`00_planning.md`):**

```markdown
# Planning Output
## Task Analysis
...
## Decomposed Steps
1. ...
2. ...
## Constraints
...
## Next Agent Instructions
...
```

**Agent Specification과의 연계:**

Agent Spec의 `input.source`와 `output.files` 필드가 handoff 파일 경로를 명시한다:

```json
{
  "input": {
    "source": "00_planning.md"
  },
  "output": {
    "files": ["01_review.md"]
  }
}
```

## Key Properties

- **추적 가능성** — 각 단계의 중간 산출물이 파일로 보존되어 파이프라인 디버깅 가능
- **비동기 안전** — 에이전트가 종료된 후에도 출력물이 파일로 남아 다음 에이전트가 언제든 읽기 가능
- **재시작 용이** — 특정 단계 실패 시 해당 handoff 파일부터 재실행 가능 (전체 파이프라인 재실행 불필요)
- **인간 개입 지점** — 숫자 접두사 구조로 어느 단계에서든 사람이 파일을 수정하여 개입 가능

## Limitations

- 파일 I/O로 인한 성능 오버헤드 (메모리 내 전달보다 느림)
- 에이전트 간 파일 경로 규칙을 사전에 합의해야 함
- 파일이 많아지면 디렉토리 관리 복잡도 증가

## Relationships

- [[sequential-agent]] (handoff 파일이 sequential 파이프라인의 데이터 전달 메커니즘)
- [[agent-pool]] (orchestrator가 handoff 파일 경로를 에이전트 선택 기준으로 사용)
- [[plan-mode]] (Plan.md, Review.md, TODO.md가 사실상 handoff 파일의 특수 형태)
- [[harness-engineering]] (handoff 파일 구조가 harness의 Journal 컴포넌트 역할 수행)
- [[contract-driven-iteration]] (TASK.md의 Log 섹션이 handoff 파일과 유사한 역할)

## Open Questions

- Handoff 파일의 크기가 커질 경우(수만 토큰) 다음 에이전트의 컨텍스트 윈도우 초과를 어떻게 처리하는가?
- 병렬 에이전트가 동일한 handoff 파일을 쓰는 race condition을 방지하는 패턴은?

## Sources

- raw/4. Plan_mode Sequential and Parallel agents.pdf
- raw/5. Agent Specifications.pdf
