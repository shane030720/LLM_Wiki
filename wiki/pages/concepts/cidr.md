---
title: Classless Inter-Domain Routing (CIDR)
category: concept
tags: [networking, IP, routing, addressing, scalability]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Classless Inter-Domain Routing (CIDR, RFC4632)은 1990년대 초 인터넷의 [[classful-addressing]] 체계를 대체하기 위해 도입된 IP 주소 지정 및 라우팅 방식이다. CIDR은 주소 클래스(A/B/C)의 개념을 제거하고 가변 길이 prefix를 사용하여 IP 주소 블록을 정의한다. CIDR 마스크(prefix 길이)는 글로벌 라우팅 시스템에서 반드시 명시되고 처리되어야 한다.

## How It Works
- IP 주소는 `주소/prefix_길이` 형식(슬래시 표기, CIDR notation)으로 표기한다. 예: 192.168.1.0/24
- Classful 체계와 달리, 동일한 IP 주소라도 prefix 길이가 다르면 서로 다른 블록에 속할 수 있다.
  - 예: 230.8.24.56은 230.0.0.0/8에도, 230.8.0.0/16에도, 230.8.24.0/24에도 속할 수 있다.
- 주소만으로는 어떤 블록에 속하는지 알 수 없으므로, prefix 길이 정보가 항상 함께 전달되어야 한다.
- 라우터는 [[longest-prefix-matching]] 알고리즘을 사용하여 포워딩 결정을 내린다.
- [[vlsm]] (Variable-Length Subnet Mask)을 site-local 범위에서 인터넷 전체로 확장한 개념이다.
- [[route-aggregation]] 과 결합하여 라우팅 테이블 크기를 크게 줄인다.

## Key Properties
- 클래스(A/B/C) 경계를 제거, 임의 길이의 prefix 사용 가능
- CIDR notation: `<주소>/<prefix 길이>` (예: 14.24.74.0/24)
- prefix 길이 없이는 어떤 블록에 속하는지 결정 불가능
- 인터넷 라우팅 테이블 폭발 문제(routing table explosion)를 해결하는 핵심 기술
- [[route-aggregation]] 과 함께 계층적 라우팅을 가능하게 함
- 현재 인터넷의 모든 라우팅은 CIDR 기반

## Relationships
- [[classful-addressing]] — CIDR이 대체한 기존 클래스 기반 주소 체계
- [[vlsm]] — CIDR의 선행 개념 (site-local 범위의 가변 마스크)
- [[route-aggregation]] — CIDR 기반 경로 집약으로 라우팅 테이블 최소화
- [[longest-prefix-matching]] — CIDR 라우팅에서 필수적으로 사용되는 포워딩 알고리즘
- [[subnet-addressing]] — CIDR 도입 이전의 서브넷 마스크 기반 체계
- [[ip-forwarding]] — CIDR prefix를 사용하는 포워딩 과정

## Open Questions
- CIDR 도입 이후에도 인터넷 BGP 라우팅 테이블은 계속 증가하고 있다 (2024년 기준 ~100만 엔트리). 주소 이식성(portability)과 집약 가능성이 충돌하는 문제는 어떻게 해결해야 하는가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
