---
title: Route Aggregation
category: concept
tags: [networking, routing, IP, scalability, hierarchy]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Route Aggregation(경로 집약, Supernetting이라고도 함)은 인접한 여러 IP prefix를 하나의 짧은 단일 prefix(집약 경로, aggregate 또는 summary)로 합치는 기법이다. 이를 통해 라우팅 테이블의 엔트리 수를 줄이고 인터넷 라우팅 시스템의 확장성을 높인다.

## How It Works
1. **계층적 라우팅의 원리**: 네트워크 토폴로지가 트리 구조이고 주소가 토폴로지를 반영하여 할당되면, 매우 작은 라우팅 테이블로도 최단 경로 라우팅이 가능하다 (Kleinrock & Kamoun, 1977).
2. **집약 조건**: 인접한 prefix들이 동일한 상위 prefix를 공유해야 집약 가능하다.
   - 예: 200.23.16.0/23, 200.23.18.0/23, ..., 200.23.30.0/23 (8개) → 200.23.16.0/20 으로 집약
3. **효과**: 하위 네트워크를 담당하는 ISP는 외부 인터넷에 단 하나의 짧은 prefix만 광고하면 된다.
4. [[cidr]] 기반 주소 할당과 결합하여 계층적 라우팅 구조를 형성한다.
5. [[longest-prefix-matching]] 에 의해 집약된 경로와 구체적 경로가 공존할 때 더 구체적인(긴) prefix가 우선된다.

집약 전/후 비교:
- 집약 전: 라우터가 8개의 /23 엔트리 보유
- 집약 후: 라우터가 1개의 /20 엔트리만 보유 → 테이블 크기 감소

## Key Properties
- 여러 adjacent prefix → 하나의 shorter prefix
- 라우팅 테이블 크기 감소 (확장성 향상)
- 주소가 토폴로지를 반영하여 할당되어야 효과적 (주소 계층성 필요)
- "Hierarchical routing is the only proven mechanism for scaling routing to the current size of the Internet." (Rekhter & Li, RFC 2008, 1996)
- 집약된 prefix가 커버하는 주소 공간에 실제 할당되지 않은 구멍(holes)이 존재할 수 있음

## Relationships
- [[cidr]] — route aggregation의 기반이 되는 가변 길이 prefix 체계
- [[longest-prefix-matching]] — 집약 경로와 구체적 경로 간 우선순위 결정
- [[classful-addressing]] — 계층적 라우팅의 초기 형태 (클래스 A/B/C 자체가 일종의 집약)
- [[ip-forwarding]] — 집약된 경로를 사용하는 라우터의 포워딩 과정
- [[network-layer]] — route aggregation이 적용되는 계층

## Open Questions
- 집약이 불가능한 경우(비연속 주소 블록, 멀티호밍 등), 라우팅 테이블이 비대해지는 문제는 여전히 미해결 상태이다. 주소 이식성(portability)과 집약 가능성은 충돌하는 경우가 많다.

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
