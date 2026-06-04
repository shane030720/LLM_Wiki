---
title: Contract-Driven Iteration
category: concept
tags: [agent-pattern, harness, workflow, quality-assurance]
sources: [raw/시스템 분析 실습/7. Harness and Skills.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트가 `TASK.md`의 Done-when 기준을 모두 충족할 때까지 반복 실행하는 루프 패턴. "계약(Contract)"이 완료 조건을 명시하고 에이전트는 그 계약을 이행할 때까지 작업한다. Harness Engineering의 Contract 컴포넌트의 실천 방법이다.

## How It Works

**TASK.md 구조:**

```markdown
# TASK.md
## Status: IN_PROGRESS
## Goal
사용자 인증 모듈을 구현한다.

## Done-when
- [ ] JWT 토큰 발급 기능 구현
- [ ] 단위 테스트 커버리지 80% 이상
- [ ] API 문서 업데이트
- [ ] 코드 리뷰 승인

## Log
- 2026-05-26 10:00: 시작, JWT 라이브러리 분석
- 2026-05-26 10:30: 토큰 발급 구현 완료
- 2026-05-26 11:00: 테스트 커버리지 72% — 미충족, 추가 테스트 작성 중
```

**반복 실행 루프:**

```python
def contract_driven_loop(task_file, agent):
    while True:
        task = read_task(task_file)
        
        if all_done_when_satisfied(task):
            update_status(task_file, "COMPLETED")
            break
        
        # 미충족 기준 식별
        pending = get_pending_criteria(task)
        
        # 에이전트 실행
        result = run_agent(agent, pending)
        
        # 로그 업데이트
        append_log(task_file, result)
```

**Status 전환:**

```
PENDING → IN_PROGRESS → COMPLETED
                     ↘ FAILED (max_attempts 초과)
```

**핵심 격언:**
- "Contract 없는 Procedure는 무한 루프이고, Procedure 없는 Contract는 죽은 문서"
- Contract(TASK.md)와 Procedure(Skill)는 반드시 함께 존재해야 함

## Key Properties

- **완료 조건 명시** — "충분히 잘 됐다"는 주관적 판단 대신 체크리스트로 완료 정의
- **자기 수정 루프** — 에이전트가 스스로 미충족 기준을 식별하고 재시도
- **감사 추적** — Log 섹션에 모든 시도와 결과가 기록되어 진행 상황 추적 가능
- **인간 개입 지점** — TASK.md를 직접 수정하여 기준 추가/변경 가능

## Limitations

- Done-when 기준을 에이전트가 자동으로 평가하기 어려운 주관적 항목(예: "코드 품질 우수") 포함 시 루프 종료 불가
- Max_attempts 없이 루프를 실행하면 비용과 시간이 무한 증가
- 기준 간 의존 관계가 복잡하면 루프 순서 최적화 어려움

## Relationships

- [[harness-engineering]] (Contract-Driven Iteration이 Harness의 Contract 컴포넌트 구현)
- [[skill]] (TASK.md의 Done-when을 달성하기 위해 에이전트가 Skill을 사용)
- [[plan-mode]] (Plan Mode 산출물(Plan.md, TODO.md)이 TASK.md의 Done-when 기준이 됨)
- [[loop]] (Contract-Driven Iteration이 Loop의 한 형태; 종료 조건이 명확한 루프)
- [[agent-pool]] (Orchestrator가 TASK.md 상태를 기반으로 에이전트를 선택·실행)

## Open Questions

- Done-when 기준을 자동으로 생성하고 검증하는 LLM 기반 방법은?
- TASK.md의 버전 관리와 변경 이력 추적을 어떻게 구조화하는가?

## Sources

- raw/7. Harness and Skills.pdf
