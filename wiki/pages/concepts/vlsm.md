---
title: Variable-Length Subnet Mask (VLSM)
category: concept
tags: [networking, IP, subnet, addressing]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Variable-Length Subnet Mask (VLSM, RFC1878)은 [[subnet-addressing]] 의 확장으로, 동일한 상위 네트워크 블록 내에서 서브넷마다 서로 다른 길이의 서브넷 마스크를 허용하는 기법이다. 원래의 고정 길이 서브넷 마스크는 모든 서브넷이 동일한 호스트 수를 가져야 했지만, VLSM은 이 제약을 제거하여 주소 공간을 훨씬 효율적으로 활용할 수 있게 한다.

## How It Works
1. 상위 네트워크 블록(예: 14.24.74.0/24)이 조직에 할당된다.
2. 서브넷별 필요 호스트 수에 따라 다른 prefix 길이를 적용한다.
   - 128개 주소가 필요하면 /25 마스크 사용 (2^7 = 128)
   - 64개 주소가 필요하면 /26 마스크 사용 (2^6 = 64)
   - 16개 주소가 필요하면 /28 마스크 사용 (2^4 = 16)
3. 각 서브블록의 크기는 반드시 2의 거듭제곱이어야 한다.
4. 각 서브블록의 시작 주소는 블록 크기의 배수 조건(alignment)을 만족해야 한다.
5. 할당은 일반적으로 가장 큰 서브블록부터 순서대로 진행하며, 나머지 주소는 예비(reserve)로 남긴다.

예시 (14.24.74.0/24, 256개 주소):
- 120개 요청 → 128개 할당, /25, 14.24.74.0/25 ~ 14.24.74.127/25
- 60개 요청 → 64개 할당, /26, 14.24.74.128/26 ~ 14.24.74.191/26
- 10개 요청 → 16개 할당, /28, 14.24.74.192/28 ~ 14.24.74.207/28
- 나머지 48개: 14.24.74.208 ~ 14.24.74.255 (예비)

## Key Properties
- 서브넷별로 다른 마스크 길이 적용 가능 (site-local 범위에서 유효)
- 주소 낭비를 최소화하여 IPv4 주소 공간 효율 개선
- 각 서브블록 크기는 2의 거듭제곱이어야 함
- 시작 주소는 블록 크기의 배수 조건 필수
- [[cidr]] 의 선행 개념이며, CIDR은 VLSM을 인터넷 전체 라우팅 시스템으로 확장한 것

## Relationships
- [[subnet-addressing]] — VLSM이 확장하는 기반 개념; 고정 길이 마스크의 한계를 극복
- [[cidr]] — VLSM을 인터넷 규모로 일반화한 Classless Inter-Domain Routing
- [[classful-addressing]] — VLSM이 극복하려는 고정 클래스 체계
- [[network-addressing]] — 상위 IP 주소 지정 체계

## Open Questions
- VLSM 환경에서 라우팅 프로토콜이 서브넷 마스크 정보를 올바르게 전파해야 한다. RIPv1 같은 classful 라우팅 프로토콜은 VLSM을 지원하지 않아 VLSM 도입 시 라우팅 프로토콜도 함께 교체해야 하는 문제가 있다.

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
