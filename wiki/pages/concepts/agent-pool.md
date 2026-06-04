---
title: Agent Pool
category: concept
tags: [agent-pattern, orchestrator, multi-agent, management]
sources: [raw/시스템 분析 실습/6. Agent pool and Orchestrator.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트 설정(JSON)을 파일 시스템에 저장하고 Orchestrator가 필요에 따라 동적으로 선택·실행하는 에이전트 관리 패턴. 하드코딩된 파이프라인 대신 유연한 에이전트 구성을 가능하게 한다.

## How It Works

**디렉토리 구조:**

```
pool/
  planner.json
  reviewer.json
  implementer.json
  tester.json
  ...
```

**에이전트 JSON 스키마:**

```json
{
  "id": "planner",
  "role": "작업 분해 및 단계별 계획 수립",
  "system_prompt": "당신은 소프트웨어 계획 전문가입니다...",
  "input": {
    "description": "사용자 요청 또는 PRD",
    "format": "markdown",
    "source": "user_request.md"
  },
  "output": {
    "description": "단계별 구현 계획",
    "format": "markdown",
    "files": ["00_planning.md"]
  },
  "tools": ["Read", "Write", "WebSearch"],
  "constraints": {
    "max_attempts": 3,
    "timeout_seconds": 300,
    "sandbox": true
  }
}
```

**Orchestrator 동작 방식:**

```python
def orchestrate(task):
    # 1. Pool에서 에이전트 목록 로드
    agents = load_pool("pool/*.json")
    
    # 2. 태스크에 적합한 에이전트 선택
    selected = select_agent(agents, task)
    
    # 3. 에이전트 실행
    result = run_agent(selected, task.input)
    
    # 4. 상태 업데이트
    update_dashboard(selected.id, status="completed")
    
    return result
```

**에이전트 상태 대시보드:**

| 에이전트 | 상태 | 시작 시간 | 소요 시간 |
|----------|------|-----------|-----------|
| planner | completed | 10:01 | 45s |
| reviewer | running | 10:02 | - |
| implementer | idle | - | - |
| tester | failed | 10:03 | 12s |

**Orchestrator 선택 규칙:**
- 태스크 타입과 에이전트 `role` 매핑
- 현재 상태(idle/running/completed/failed) 기반 필터링
- 실패한 에이전트의 재시도 로직 (`max_attempts` 기준)

## Key Properties

- **동적 확장** — pool에 JSON 파일 추가만으로 새 에이전트 등록 (코드 수정 불필요)
- **선언적 설정** — 에이전트 행동이 JSON으로 명시되어 인간이 검토·수정 가능
- **상태 추적** — 각 에이전트의 실행 상태를 중앙에서 모니터링
- **재사용성** — 동일 에이전트를 다른 파이프라인에서 재사용 가능

## Limitations

- Orchestrator에 선택 로직이 집중되어 복잡도 증가
- 에이전트 간 의존 관계를 pool 설정만으로 표현하기 어려움
- 대규모 pool에서 최적 에이전트 선택 알고리즘이 복잡해짐

## Relationships

- [[sequential-agent]] (Orchestrator가 pool에서 sequential 파이프라인 에이전트를 순서대로 선택)
- [[parallel-agent]] (Orchestrator가 pool에서 여러 에이전트를 동시에 선택하여 병렬 실행)
- [[system-prompt]] (pool의 각 JSON에 system_prompt 필드가 에이전트 동작 정의)
- [[handoff]] (pool 에이전트 간 데이터 전달에 handoff 파일 사용)
- [[agentic-coding]] (agent pool이 대규모 agentic coding의 에이전트 관리 기반)
- [[harness-engineering]] (agent pool JSON이 Preference 컴포넌트의 구체적 구현)

## Open Questions

- Orchestrator가 실패한 에이전트를 자동으로 대체 에이전트로 교체하는 패턴은?
- 에이전트 pool의 버전 관리와 롤백 전략은?

## Sources

- raw/6. Agent pool and Orchestrator.pdf
