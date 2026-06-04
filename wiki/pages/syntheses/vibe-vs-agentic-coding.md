---
title: Vibe Coding vs Agentic Coding — 언제 무엇을 선택하는가
category: synthesis
tags: [coding-paradigm, comparison, decision-framework]
sources: [raw/시스템 분析 실습/1. Vibe coding and Agent coding.pdf, raw/2. SDLC pipeline in Vibe coding.pdf]
created: 2026-05-26
updated: 2026-05-26
---

## Thesis

Vibe Coding과 Agentic Coding은 연속선 위의 두 점이 아니라 근본적으로 다른 패러다임이다. 작업 규모와 품질 요구사항에 따라 명확히 구분하여 선택해야 하며, 잘못된 선택은 어느 쪽이든 불필요한 비용을 유발한다.

## Evidence

**Vibe Coding이 우위인 영역:**
- 단일 대화 세션으로 완성되는 소규모 도구 (Quick Sort Viewer 등)
- 프로토타이핑: 아이디어의 빠른 시각적 검증이 목적인 경우
- 일회성 스크립트: 유지보수가 필요 없는 단발성 자동화
- PRD 없이도 사용자 의도가 단순명확한 경우
- Karpathy 본인이 명명했으며, 소규모 도구에서 개발자 생산성을 크게 향상시킴

**Agentic Coding이 필요한 영역:**
- 여러 모듈이 상호작용하는 중·대규모 애플리케이션
- 팀 협업이 필요하고 코드 일관성이 요구되는 경우
- SDLC의 각 단계(Planning→Analysis→Design→Implementation)를 명시적으로 보장해야 하는 경우
- 장기적으로 유지보수되는 프로덕트 (기술 부채 누적 방지 필요)
- 2025년 4분기부터 주류 패러다임으로 부상

**수렴 지점 — Spec-Driven Development:**
- Vibe Coding에 PRD/SRS를 추가하면 LLM 출력 품질이 월등히 향상됨
- 작은 프로젝트에서도 Spec First 원칙을 적용하면 Vibe Coding의 한계를 상당 부분 보완 가능
- Spec-Driven Development는 두 패러다임 사이의 가교

## Counterevidence

- Karpathy 자신이 Vibe Coding의 "Accept All" 방식을 비판했지만, 이는 무분별한 사용에 대한 경고이지 Vibe Coding 자체를 부정하지 않음
- Agentic Coding이 항상 더 나은 것은 아님 — 간단한 작업에 Multi-Agent 파이프라인을 구성하면 오버엔지니어링이 됨
- 두 패러다임의 경계는 작업 규모가 아닌 **유지보수 필요 여부**가 더 정확한 기준일 수 있음

## Conclusion

**선택 기준 (Decision Framework):**

| 조건 | 권장 패러다임 |
|------|--------------|
| 완성까지 1~2시간 예상, 일회성 | Vibe Coding |
| 유지보수 예정, 타인이 이어받을 코드 | Agentic Coding |
| 소규모지만 품질이 중요한 경우 | Vibe Coding + Spec-Driven |
| 복수 모듈, 팀 협업 필요 | Agentic Coding |
| 불확실한 요구사항 탐색 | Vibe Coding (프로토타입) → Agentic Coding (본 구현) |

가장 실용적인 접근: **Vibe Coding으로 프로토타이핑 → 가치가 검증되면 Agentic Coding으로 재구현**.

## Sources

- raw/1. Vibe coding and Agent coding.pdf
- raw/2. SDLC pipeline in Vibe coding.pdf
