---
title: NP-Completeness (NP-완전성)
category: concept
tags: [np-complete, np-hard, reduction, complexity, circuit-sat]
sources: [raw/알고리즘/CH13 NP-완전 문제.pdf]
created: 2026-06-02
updated: 2026-06-02
---

## Definition

NP-Complete(NP-완전)는 [[class-np]]에 속하면서 동시에 NP-Hard인 문제들의 클래스다. 어떤 문제 Q가 **NP-Hard**이면 NP 내의 모든 문제가 Q로 다항 시간에 환원(reduction) 가능하다. NP-Complete 문제는 NP에서 "가장 어려운" 문제들이며, 그 중 하나라도 다항 시간에 풀린다면 P = NP가 성립한다.

## How It Works

**다항 시간 환원(Polynomial Reduction, P ≤p Q)**:

문제 P가 문제 Q로 환원 가능하다는 것은 다음을 의미한다:
- 다항 시간에 계산 가능한 변환 함수 T가 존재한다.
- x가 P의 "yes" 입력이면 T(x)는 Q의 "yes" 입력이다.
- x가 P의 "no" 입력이면 T(x)는 Q의 "no" 입력이다.
- 환원 관계는 **전이적(transitive)**이다: P ≤p Q이고 Q ≤p R이면 P ≤p R.

즉, Q를 푸는 알고리즘이 있으면 T를 통해 P도 풀 수 있다.

**NP-Complete 증명 절차**:
1. 해당 문제가 NP에 속함을 보인다 (다항 시간 검증 알고리즘 제시).
2. 이미 알려진 NP-Complete 문제에서 다항 시간 환원이 가능함을 보인다.

**최초의 NP-Complete 문제 — CIRCUIT-SAT**:
- AND, OR, NOT 게이트로 구성된 불리언 회로에서 출력이 1이 되는 입력 조합이 존재하는가?
- Cook-Levin Theorem에 의해 최초로 NP-Complete임이 증명되었다.
- 모든 후속 NP-Complete 증명의 출발점 역할을 한다.

## Key Properties

- NP-Complete = NP ∩ NP-Hard
- NP-Complete 문제 하나를 다항 시간에 풀 수 있으면 모든 NP 문제를 다항 시간에 풀 수 있다 (P = NP)
- 환원 체인(reduction chain)을 통해 새로운 NP-Complete 문제를 증명한다
- "내가 다항 시간 알고리즘을 못 찾은 게 아니라, 수많은 영리한 사람들도 못 찾았다"는 집단적 증거로서의 의미를 갖는다
- 어려운 문제에 맞닥뜨렸을 때 할 수 있는 일: (1) 하한 증명, (2) NP-Complete 증명으로 집단적 어려움 공유

## Relationships

- [[class-np]] — NP-Complete는 NP의 부분집합
- [[class-p]] — P = NP이면 P = NP = NP-Complete가 된다
- [[np-complete-problems]] — 구체적인 NP-Complete 문제들의 목록과 환원 관계

## Open Questions

- P = NP인지의 여부: NP-Complete 문제가 실제로 다항 시간에 풀릴 수 있는가?
- NP-Complete 문제에 대한 근사 알고리즘(approximation algorithm)의 이론적 한계는?
- 양자 컴퓨팅(quantum computing)이 NP-Complete 문제를 효율적으로 풀 수 있는가?

## Sources

- raw/알고리즘/CH13 NP-완전 문제.pdf (p.12–p.14, p.21)
