---
title: Functional Dependency
category: concept
tags: [database, relational-database, functional-dependency, normalization]
sources: [raw/데이터베이스/Relational DB Design (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Functional Dependency(함수 종속)는 관계형 스키마 R에서 속성 집합 α와 β 사이의 제약으로, 어떤 두 튜플 t1, t2가 α 값이 동일하면 반드시 β 값도 동일해야 함을 의미한다. 표기: α → β. superkey 개념의 일반화이며, 합법적인 관계 인스턴스 전체(legal relations)에 대한 스키마 수준 제약을 표현한다.

## How It Works

**Superkey와의 관계**: K → R이면 K는 R의 superkey. K의 어떤 진부분집합도 R을 함수적으로 결정하지 못하면 candidate key.

**Trivial FD**: β ⊆ α이면 α → β는 trivial(자명한) 함수 종속으로, 모든 인스턴스에서 항상 성립한다.

**Closure of F (F+)**: FD 집합 F로부터 논리적으로 도출 가능한 모든 FD의 집합. Armstrong's Axioms를 반복 적용하여 계산한다.
- Reflexivity(반사성): β ⊆ α이면 α → β
- Augmentation(증강): α → β이면 γα → γβ
- Transitivity(이행성): α → β이고 β → γ이면 α → γ

위 세 공리에서 다음 규칙을 추가로 도출할 수 있다.
- Union: α → β이고 α → γ이면 α → βγ
- Decomposition: α → βγ이면 α → β이고 α → γ
- Pseudotransitivity: α → β이고 γβ → δ이면 αγ → δ

**Attribute Closure (α+)**: F 하에서 α로부터 함수적으로 결정되는 모든 속성의 집합. 알고리즘: result := α; F의 각 β → γ에 대해 β ⊆ result이면 result := result ∪ γ; 변화 없을 때까지 반복.

**Attribute Closure의 활용**:
- Superkey 검사: α+ ⊇ R이면 α는 superkey
- FD 검사: α → β가 F+에 속하는지 확인하려면 β ⊆ α+인지 검사
- F+ 계산: 각 α ⊆ R에 대해 α+를 구하고, 각 S ⊆ α+에 대해 α → S를 출력

## Key Properties

- FD는 스키마 수준의 제약이다. 특정 인스턴스가 우연히 FD를 만족해도 그것이 스키마에서 FD가 성립함을 의미하지 않는다.
- Armstrong's Axioms는 sound(실제 성립하는 FD만 생성)하고 complete(성립하는 모든 FD를 생성)하다.
- F+는 F의 superset이다.
- Attribute closure 알고리즘은 superkey 검사와 FD 검사 모두에 활용할 수 있는 단순하고 저렴한 절차다.

## Relationships

- [[database-normalization]] — FD를 기반으로 정규화 여부를 판단하고 분해 방법을 결정한다.
- [[bcnf]] — BCNF 정의는 F+ 내의 FD가 superkey 조건을 만족하는지를 기준으로 한다.
- [[third-normal-form]] — 3NF 정의도 FD와 candidate key의 관계를 핵심 기준으로 사용한다.

## Open Questions

- 실제 SQL 데이터베이스 시스템은 superkey(PRIMARY KEY, UNIQUE) 이외의 FD를 직접 선언·검사하는 기능을 표준적으로 지원하지 않는다. assertion으로 표현은 가능하나 비용이 크고 현재 주요 DBMS에서는 미지원이다.
- 어떤 FD가 스키마에 "성립한다"고 판단하는 기준(도메인 지식 vs. 데이터 관찰)은 설계자의 해석에 의존한다.

## Sources

- raw/데이터베이스/Relational DB Design (1).pdf
