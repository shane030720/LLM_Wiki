---
title: Skill
category: concept
tags: [harness, agent-design, reusability, procedure]
sources: [raw/시스템 분析 실습/7. Harness and Skills.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Definition

에이전트가 특정 반복 가능한 작업을 수행하는 방법을 정의한 마크다운 파일. SKILL.md와 보조 파일들로 하나의 폴더를 구성하며, 에이전트가 상황에 맞는 Skill을 자동으로 선택하여 실행한다. Harness Engineering의 Procedure 컴포넌트 구현이다.

## How It Works

**Skill 폴더 구조:**

```
skills/
  ingest/
    SKILL.md         ← 주 정의 파일
    template.md      ← 출력 템플릿
    checklist.md     ← 완료 기준
  query/
    SKILL.md
    search-strategy.md
  lint/
    SKILL.md
    rules.md
```

**SKILL.md 구조:**

```markdown
# Skill: [이름]
## Trigger
어떤 상황에서 이 Skill이 활성화되는가

## Input
- 형식: markdown / json / text
- 소스: 어디서 입력을 받는가

## Procedure
1. 첫 번째 단계
2. 두 번째 단계
3. ...

## Output
- 형식: markdown / json
- 위치: 어디에 결과를 저장하는가

## Done-when
- [ ] 완료 조건 1
- [ ] 완료 조건 2
```

**에이전트의 Skill 자동 선택:**

```
태스크 분석
  → "새 PDF를 처리해야 한다" 감지
  → skills/ingest/SKILL.md 선택
  → SKILL.md의 Procedure 실행
  → Done-when 확인
  → 완료 또는 재시도
```

**LLM Wiki Skill 예시:**

| Skill 이름 | Trigger | Output |
|------------|---------|--------|
| ingest | raw/ 파일 수신 | wiki/pages/*.md |
| query | 사용자 질문 | 검색 결과 요약 |
| lint | 정기 검토 요청 | 품질 리포트 |

## Key Properties

- **재사용성** — 동일 Skill을 다른 프로젝트나 에이전트에서 재사용
- **자동 선택** — 에이전트가 컨텍스트를 기반으로 적합한 Skill 자동 활성화
- **버전 관리 가능** — 파일 기반이므로 git으로 Skill 변경 이력 추적
- **인간 가독성** — 마크다운 형식으로 인간이 직접 읽고 수정 가능

## Limitations

- Skill 수가 많아지면 에이전트의 Skill 선택이 오작동할 수 있음 (Context Explosion과 유사)
- Skill 간 의존 관계나 충돌을 자동으로 감지하기 어려움
- 복잡한 Skill은 마크다운 단일 파일로 표현하기 한계 있음

## Relationships

- [[harness-engineering]] (Skill이 Harness의 Procedure 컴포넌트)
- [[contract-driven-iteration]] (TASK.md의 Done-when을 달성하기 위해 Skill을 실행)
- [[agent-pool]] (pool의 각 에이전트가 특정 Skill 집합과 연계됨)
- [[mcp]] (MCP가 Skill에서 사용할 수 있는 외부 도구 연결을 표준화)

## Open Questions

- 에이전트가 Skill을 자동으로 생성하거나 수정하는 메타-Skill 패턴은 가능한가?
- 조직 전체에서 Skill을 공유하고 발견하는 레지스트리 패턴은?

## Sources

- raw/7. Harness and Skills.pdf
