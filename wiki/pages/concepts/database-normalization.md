---
title: Database Normalization
category: concept
tags: [database, normalization, relational-database, design, lossless-join]
sources: [raw/데이터베이스/Relational DB Design (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Database Normalization(데이터베이스 정규화)은 관계형 스키마를 "좋은 형태(good form)"로 만들기 위해 함수 종속성 이론에 기반하여 릴레이션을 분해(decompose)하는 체계적 설계 과정이다. 목표는 정보 손실 없는 분해(lossless-join decomposition)와 함수 종속성 보존(dependency preservation)을 달성하면서 데이터 중복(redundancy)과 갱신 이상(anomaly)을 제거하는 것이다.

## How It Works

**나쁜 설계의 문제**: big_instructor(ID, name, salary, dept_name, building, budget)처럼 여러 엔티티 정보를 하나의 릴레이션에 합치면 dept_name이 candidate key가 아니어서 (dept_name, building, budget)의 조합이 중복 저장된다. 이는 dept_name → building, budget이라는 FD가 위반됨을 나타낸다.

**First Normal Form (1NF)**: 모든 속성의 도메인이 원자적(atomic)이어야 한다. 집합, 복합 속성, 분해 가능한 식별번호(예: CS101 → 학과 코드 + 번호) 등 비원자적 값은 1NF를 위반한다. 비원자성은 저장 복잡성 증가와 정보의 애플리케이션 레벨 인코딩이라는 나쁜 설계를 야기한다.

**Lossless-Join Decomposition**: R을 R1, R2로 분해할 때 r = ΠR1(r) ⋈ ΠR2(r)이 항상 성립해야 한다. 조건: R1 ∩ R2 → R1 또는 R1 ∩ R2 → R2가 F+에 속하면, 즉 R1 ∩ R2가 R1 또는 R2의 superkey이면 lossless-join이 보장된다. 조건을 만족하지 않으면 lossy decomposition으로 자연 조인 후 원본보다 많은 튜플이 생성되어 정보 손실이 발생한다.

**Dependency Preservation**: 분해된 각 릴레이션 Ri에서 검사 가능한 FD들의 집합 Fi의 closure (F1 ∪ F2 ∪ … ∪ Fn)+가 F+와 동일해야 한다. 보존되지 않으면 FD 검사에 join 연산이 필요하여 비용이 크다.

**설계 목표 우선순위**:
1. BCNF 달성 (최우선)
2. Lossless-join 보장 (필수)
3. Dependency preservation (선호)

모두 달성 불가능한 경우: dependency preservation 포기(BCNF 유지) 또는 중복 허용(3NF 사용) 중 선택.

## Key Properties

- 정규화 이론의 핵심 도구는 Functional Dependency다.
- Lossless-join은 항상 달성 가능하지만 dependency preservation은 BCNF와 양립 불가능한 경우가 존재한다.
- 1NF는 모든 관계형 스키마에 전제되는 최소 조건이다.
- SQL은 superkey 이외의 FD를 직접 선언하는 방법을 제공하지 않으므로, 이론적으로 완전한 정규화를 실제 시스템에서 강제하기 어렵다.

## Relationships

- [[functional-dependency]] — 정규화 판단의 수학적 기반이며 분해 방향을 결정하는 핵심 도구
- [[bcnf]] — 정규화의 최우선 목표인 가장 강한 실용적 정규형
- [[third-normal-form]] — dependency preservation을 보장하기 위해 BCNF를 완화한 정규형

## Open Questions

- BCNF와 dependency preservation을 동시에 달성할 수 없는 경우(예: R=(J,K,L), F={JK→L, L→K}), 어느 쪽을 희생할지는 응용 도메인에 따른 설계 판단의 문제다.
- SQL의 FD 선언 미지원으로 인해 이론적 정규화가 실제 무결성 보장으로 이어지지 않는 간극을 어떻게 메울 것인가?

## Sources

- raw/데이터베이스/Relational DB Design (1).pdf
