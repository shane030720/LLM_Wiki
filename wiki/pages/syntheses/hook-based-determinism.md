---
title: Hook-based Determinism in AI Agents
category: synthesis
tags: [hook, agent, determinism, automation, reliability]
sources: [raw/시스템 분석 실습/9. Loop and Hooks.pdf]
created: 2026-06-04
updated: 2026-06-04
---

## Thesis

AI 에이전트는 본질적으로 확률적(probabilistic)으로 동작하므로 매 결정마다 틀릴 가능성이 존재한다. [[hook]] (에이전트 생애 주기의 특정 시점에 자동 실행되는 스크립트)을 전략적으로 배치하면, 확률에 의존하는 결정 지점을 결정론적(deterministic) 검증 및 강제 실행으로 대체할 수 있다. 이것이 Hook의 주된 존재 이유다.

## Evidence

- **Hook 이벤트 시점별 결정론 주입 패턴:**
  - `Stop` 이벤트: 에이전트가 turn을 종료하려 할 때 셸 스크립트를 실행하여 exit code로 작업 완료 여부를 _확정적으로_ 검증 (timeout 10s 등 명시적 조건 사용)
  - `PostToolUse` 이벤트: 에이전트가 도구 사용 사실을 기록에 남길지 여부를 에이전트 판단에 맡기지 않고, 도구 실행 직후 자동 LOG 강제 기록
  - `UserPromptSubmit` 이벤트: 사용자 지시가 `/docs` 등 기존 지식 베이스에 이미 존재하는지 에이전트가 검색할지 말지를 선택하게 두는 대신, 제출 시점에 자동으로 체크하거나 추가 프롬프트를 강제 주입
  - `PreToolUse` / `PermissionRequest` / `SessionStart` 이벤트: 도구 사용 전 사전 검증, 권한 요청 가로채기, 세션 초기화 시 환경 설정 자동화 등에 활용

- **결정론적 제어가 필요한 이유:** 에이전트는 동일한 상황에서도 다른 선택을 내릴 수 있다. 작업 완료 보고, 로그 기록, 다른 에이전트 트리거 같은 _반드시 실행되어야 하는_ 사이드 이펙트는 에이전트의 자율 판단에 맡길 수 없다.

- **[[loop]]와의 결합:** Loop는 [[hook]]의 `Stop`과 연계하여, 주기적으로 상태를 체크하고 다음 에이전트 체인을 트리거하는 자동화 파이프라인 구성에 사용된다. 특히 Loop는 Claude에서 거의 독점적으로 지원되며, Codex 및 Gemini CLI에서는 OS 수준의 Scheduler(cron 등)로 대체해야 한다.

- **비용 제어 전략:** Loop가 Read/Write를 수반하면 주기마다 비용이 발생한다. 고가 요금제가 아닌 경우, Loop는 단순 Status Checking 위주로 한정하고, 실제 action은 로컬 모델(vllm, Ollama를 통한 Qwen 등)을 API로 호출하여 상용 LLM 비용을 절감할 수 있다. 이 패턴은 "trigger(상용 LLM) + action(로컬 LLM)" 분리 구조다.

## Counterevidence

- Hook 스크립트 자체가 잘못 작성되거나 side effect를 완전히 정의하지 못하면, 결정론적 제어는 오히려 잘못된 동작을 반복하는 결과를 낳는다. 즉 결정론은 _정확성을 보장하지 않고 일관성만 보장한다_.
- Loop의 비용 절감을 위한 로컬 모델 활용은 GPU 자원과 모델 운영 역량을 전제로 한다. 일반 사용자에게는 진입 장벽이 높다.

## Conclusion

Hook은 단순한 이벤트 핸들러가 아니라, 확률적 AI 에이전트 시스템에 _결정론적 레이어를 삽입하는 아키텍처 기법_이다. 에이전트가 자율적으로 판단하면 놓칠 수 있는 감사(logging), 검증(validation), 연쇄 트리거(chaining) 등을 Hook으로 고정함으로써, 에이전트 행동의 신뢰성을 높인다. Loop와 결합하면 주기적 자동화 파이프라인이 되며, 로컬 LLM을 action 실행자로 분리하는 하이브리드 구조를 통해 비용 효율화도 가능하다. 이 패턴은 [[harness-engineering]] 및 [[agent-session-control]]과 함께 신뢰 가능한 에이전트 시스템 설계의 핵심 원칙을 구성한다.

## Sources

- raw/시스템 분석 실습/9. Loop and Hooks.pdf
