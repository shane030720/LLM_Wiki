---
title: Relational Algebra
category: concept
tags: [database, query-language, algebra, operator, sql]
sources: [raw/데이터베이스/Relational Model 2.pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition

Relational Algebra는 relation을 입력으로 받아 새로운 relation을 출력하는 연산들의 집합으로 구성된 함수형(functional) 질의 언어다. SQL의 이론적 기반이 되며, 6개의 기본 연산(Select, Project, Union, Set Difference, Cartesian Product, Rename)으로 이루어진다. 각 연산은 하나 또는 두 개의 relation을 입력으로 받아 항상 단일 relation을 결과로 반환한다(closure property).

## How It Works

모든 연산은 relation을 입력·출력으로 사용하므로 연산 결과를 다른 연산의 입력으로 사용하는 **합성(composition)**이 가능하다. 아래 6개의 기본 연산과 파생 연산인 Natural Join이 핵심이다.

### 기본 연산

| 연산 | 기호 | 설명 |
|------|------|------|
| Select | σ | 조건을 만족하는 tuple 선택 (행 필터링) |
| Project | Π | 지정한 attribute만 선택 (열 필터링, 중복 제거) |
| Union | ∪ | 두 relation의 합집합 |
| Set Difference | − | 첫 번째 relation에만 있는 tuple |
| Cartesian Product | × | 두 relation의 모든 tuple 조합 |
| Rename | ρ | 결과 relation 또는 attribute에 새 이름 부여 |

### Select (σ)

조건 술어(predicate)를 만족하는 tuple만 반환한다.

```
σ salary >= 85000 (instructor)
```

→ salary가 85,000 이상인 instructor tuple들을 반환한다.

### Project (Π)

지정한 attribute 목록만 남기며, 결과에서 중복 tuple은 제거된다.

```
Π ID, salary (instructor)
```

→ instructor relation에서 ID와 salary 두 열만 추출한다.

### 합성 예시

Select와 Project를 합성하면 행·열을 동시에 필터링할 수 있다.

```
Π ID, salary (σ salary >= 85000 (instructor))
```

### Cartesian Product (×)

두 relation r, s의 모든 tuple 조합을 생성한다. 단독으로는 의미 없는 조합이 포함될 수 있으므로 보통 σ와 함께 사용하거나 Natural Join으로 대체한다.

### Natural Join (⋈)

두 relation R, S에서 공통 attribute의 값이 같은 tuple들을 결합한다. 결과 schema는 R ∪ S이며, 공통 attribute는 한 번만 나타난다. 교환 법칙(commutative)과 결합 법칙(associative)이 성립한다.

```
Π name, title (σ dept_name="Comp. Sci." (instructor ⋈ teaches ⋈ course))
```

**Theta Join**: `r ⋈_θ s = σ_θ (r × s)` — Cartesian Product에 임의 조건 θ를 적용한 것이다.

### Union (∪) / Set Difference (−)

두 연산 모두 **union-compatible** 조건(같은 arity, 대응 attribute의 domain 호환)을 요구한다.

### Rename (ρ)

```
ρ_x (E)            → 표현식 E의 결과를 x로 명명
ρ_{x(A1,A2,...,An)} (E) → 이름과 attribute 모두 변경
```

같은 relation을 두 번 참조해야 할 때 필수적이다. 예: 자신보다 급여가 높은 instructor ID 조회:

```
Π i.ID (σ i.salary > j.salary (ρ_i(instructor) × σ_{j.id=12121}(ρ_j(instructor))))
```

## Key Properties

- **Closure**: 모든 연산의 결과는 relation이므로 연산을 자유롭게 합성할 수 있다
- **Functional(절차적)**: 연산 적용 순서를 명시하는 절차적 언어이다 (tuple/domain relational calculus는 선언적)
- **SQL의 이론적 기반**: SQL의 SELECT-FROM-WHERE 구조는 Relational Algebra 연산에 대응된다
- Natural Join은 **교환 법칙**과 **결합 법칙**을 모두 만족한다
- Rename은 동일 relation의 self-join 시 이름 충돌을 해결하는 수단이다

## Relationships

- [[relational-model]] — Relational Algebra가 동작하는 데이터 모델
- [[sql]] — Relational Algebra를 기반으로 설계된 실용 질의 언어 (아직 페이지 미작성)
- [[tuple-relational-calculus]] — 동일 표현력을 가진 선언적 질의 언어 (아직 페이지 미작성)
- [[domain-relational-calculus]] — 또 다른 선언적 질의 언어 (아직 페이지 미작성)

## Open Questions

- Relational Algebra의 6개 기본 연산 외에 Intersection, Division 등의 연산은 어떻게 파생되는가?
- Tuple Relational Calculus와 Relational Algebra의 표현 능력(expressive power)은 동등한가?
- Cartesian Product와 Natural Join의 성능 차이는 실제 DBMS 최적화에 어떤 영향을 미치는가?

## Sources

- raw/데이터베이스/Relational Model 2.pdf (p.9–p.24)
