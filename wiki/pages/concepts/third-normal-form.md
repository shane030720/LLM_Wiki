---
title: Third Normal Form (3NF)
category: concept
tags: [database, normalization, 3nf, functional-dependency]
sources: [raw/데이터베이스/Relational DB Design (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

3NF(Third Normal Form)는 관계 스키마 R이 FD 집합 F에 대해 만족해야 하는 정규형으로, F+에 속하는 모든 FD α → β에 대해 다음 중 하나가 성립해야 한다: (1) α → β가 trivial(β ⊆ α)이거나, (2) α가 R의 superkey이거나, (3) β - α의 각 속성 A가 R의 어떤 candidate key에 포함된다. 세 번째 조건이 BCNF와의 차이이며, dependency preservation 보장을 위한 최소한의 완화(minimal relaxation)다.

## How It Works

**BCNF와의 비교 예시**: advisor(s_ID, i_ID, dept_name), F = {i_ID → dept_name}
- Candidate keys: (s_ID, i_ID), (s_ID, dept_name)
- i_ID → dept_name에서 i_ID는 superkey가 아니므로 BCNF 위반 → BCNF라면 분해 필요
- dept_name은 candidate key (s_ID, dept_name)에 포함되므로 3NF 조건 3 충족 → 3NF라면 분해 불필요

**Dependency Preservation 보장**: 3NF 분해는 항상 lossless-join과 dependency preservation을 동시에 달성 가능하다. BCNF가 dependency preservation을 포기해야 하는 상황에서 3NF가 현실적 대안이 된다.

**트레이드오프**: 3NF는 BCNF보다 약하므로 조건 3에 해당하는 경우 일부 중복(redundancy)이 남을 수 있다. 위 advisor 예시에서 동일한 (i_ID, dept_name) 쌍이 여러 학생 레코드에 반복 저장될 수 있다.

**정규형 포함 관계**:
- BCNF ⊂ 3NF (BCNF이면 반드시 3NF)
- 3NF 분해: lossless-join + dependency preservation 항상 보장
- BCNF 분해: lossless-join만 항상 보장

## Key Properties

- 3NF의 세 번째 조건은 "prime attribute"(candidate key에 속하는 속성)에 한해 non-superkey 결정자를 허용한다.
- 3NF 분해는 lossless-join과 dependency preservation을 동시에 항상 달성한다.
- BCNF를 달성하면서 dependency preservation이 불가능한 경우 3NF가 차선책이다.
- 3NF를 사용할 경우 중복 허용이라는 비용이 발생한다.

## Relationships

- [[bcnf]] — 3NF보다 강한 정규형; BCNF 불가 시 3NF가 대안
- [[functional-dependency]] — 3NF 정의의 수학적 기반, candidate key 판별에 사용
- [[database-normalization]] — BCNF와 dependency preservation을 동시에 달성할 수 없을 때 3NF로 후퇴

## Open Questions

- 3NF를 선택할 경우 허용되는 중복이 실제 운영 환경에서 어떤 수준의 갱신 이상을 초래하는가?
- BCNF와 3NF 중 선택 기준을 응용 도메인별로 어떻게 체계화할 수 있는가?

## Sources

- raw/데이터베이스/Relational DB Design (1).pdf
