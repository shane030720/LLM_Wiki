---
title: Loop
category: concept
tags: [automation, scheduling, agent-lifecycle, recurring-task]
sources: [raw/시스템 분析 실습/9. Loop and Hooks.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트가 정해진 주기 또는 조건에 따라 반복적으로 작업을 실행하는 자동화 메커니즘. 사람이 개입하지 않아도 에이전트가 정기적으로 특정 태스크를 수행한다. Contract-Driven Iteration이 완료 조건 기반 루프라면, Loop는 시간 또는 이벤트 기반 반복이다.

## How It Works

**두 가지 Loop 구현 방식:**

**1. Claude-Native (CronCreate)**

Claude Code의 내장 `CronCreate` 도구를 사용하여 반복 작업 등록:

```
CronCreate({
  "schedule": "0 9 * * 1-5",  // 평일 오전 9시
  "prompt": "wiki/log.md를 검토하고 이번 주 변경사항을 요약해줘",
  "description": "Weekly wiki review"
})
```

- Claude Code 세션 내에서 관리
- cron 표현식으로 스케줄 설정
- 각 실행마다 새 Claude 세션 시작

**2. OS 스케줄러 (Codex CLI / Gemini CLI)**

Codex와 Gemini CLI는 Claude-native Loop가 없어 OS 스케줄러를 사용:

```bash
# crontab -e
0 9 * * 1-5 codex run "daily_review.md를 처리하고 결과를 report.md에 저장"
0 9 * * 1-5 gemini "analyze log.md and create weekly_summary.md"
```

**Loop 비용 고려사항:**

| 빈도 | 비용 영향 |
|------|-----------|
| 매분 | 극히 높음 — 실시간 모니터링만 정당화 |
| 매시간 | 높음 — 명확한 ROI 필요 |
| 매일 | 적당 — 일반적인 유지보수 태스크에 적합 |
| 매주 | 낮음 — 주간 리뷰·정리에 권장 |

**Loop 태스크 예시:**
- 매일 오전: 새 이슈 분류 및 우선순위 지정
- 매주 월요일: Wiki lint 실행 및 품질 리포트 생성
- 매시간: 모니터링 대시보드 데이터 갱신

**Loop에서 Hook과의 연계:**
```
Loop 실행 시작
  → SessionStart Hook: 이전 상태 로드
  → 태스크 실행
  → PostToolUse Hook: 변경사항 로그
  → Stop Hook: 완료 알림 발송
```

## Key Properties

- **무인 자동화** — 사람이 없어도 정기적 유지보수 작업 수행
- **비용 주의** — 실행마다 Read/Write 비용 발생; 빈도 설정에 주의 필요
- **컨텍스트 단절** — 각 Loop 실행은 새 세션으로 시작 (이전 컨텍스트 없음)
- **幂等性 설계 필요** — 동일 Loop를 여러 번 실행해도 결과가 동일해야 함

## Limitations

- 세션 간 컨텍스트를 공유하려면 파일(Journal)에 상태를 저장해야 함
- Loop 실패 감지와 알림 메커니즘을 별도로 구성해야 함
- 너무 빈번한 Loop는 API 비용과 Rate Limit 문제 유발

## Relationships

- [[hook]] (Loop 실행의 각 단계에서 Hook이 자동 실행)
- [[contract-driven-iteration]] (조건 기반 루프 vs 시간 기반 루프의 상호 보완)
- [[harness-engineering]] (Loop가 Harness의 자동화 실행 컴포넌트)
- [[skill]] (Loop 실행마다 적합한 Skill을 자동 선택하여 실행)

## Open Questions

- Loop 실행 중 오류 발생 시 다음 스케줄까지 기다릴 것인가, 즉시 재시도할 것인가?
- 사람이 Loop를 일시 중지하거나 즉시 실행하는 제어 인터페이스 설계 방법은?

## Sources

- raw/9. Loop and Hooks.pdf
