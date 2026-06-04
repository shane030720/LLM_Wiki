---
title: IPv6 Tunneling
category: concept
tags: [networking, IPv6, transition, tunneling, encapsulation]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
IPv6 Tunneling(IPv6 터널링)은 IPv4 네트워크 인프라를 통해 IPv6 데이터그램을 전달하기 위해 IPv6 패킷을 IPv4 패킷의 페이로드로 캡슐화하는 전환(transition) 기법이다. IPv4와 IPv6 라우터가 혼재하는 환경에서 점진적 IPv6 전환을 가능하게 한다 ("no flag days" 원칙).

## How It Works
- IPv4만 지원하는 라우터로 이루어진 구간에서, 양 끝의 IPv6/IPv4 듀얼 스택 라우터가 터널을 구성한다.

**캡슐화(Encapsulation)**:
진입 듀얼 스택 라우터(B)가 IPv6 데이터그램 전체를 IPv4 데이터그램의 페이로드로 감싸고, IPv4 출발지/목적지 주소를 터널 양 끝 라우터의 IPv4 주소로 설정하여 IPv4 네트워크로 전송

**역캡슐화(Decapsulation)**:
출구 듀얼 스택 라우터(E)가 IPv4 헤더를 제거하고 원래의 IPv6 데이터그램을 복원하여 IPv6 네트워크로 전달

```
물리적 경로:
A(IPv6) → B(IPv6/IPv4) → C(IPv4) → D(IPv4) → E(IPv6/IPv4) → F(IPv6)

논리적 경로:
A → B === IPv4 터널 === E → F
(터널 내부: IPv6 inside IPv4)
```

IPv6 데이터그램의 출발지(A)와 목적지(F) 주소는 터널 통과 후에도 변경되지 않으며, 오직 외부 IPv4 헤더의 주소만 B와 E의 주소를 사용한다.

## Key Properties
- "packet within a packet" 구조: IPv4 안에 IPv6 캡슐화
- 인터넷 전체를 동시에 업그레이드하지 않아도 IPv6 연결성 확보 가능 (점진적 전환)
- IPv6 데이터그램의 원본 출발지/목적지 주소는 터널 통과 중 불변
- 4G/5G, MPLS, VPN 등 다른 맥락에서도 터널링이 광범위하게 활용됨
- 2023년 기준 Google 클라이언트의 ~40%가 IPv6 접근; 배포 시작 후 25년 이상 소요 중
- 미국 정부(NIST) 기준 전체 도메인의 1/3이 IPv6 지원

## Relationships
- [[ipv4-datagram]] — 터널링 시 IPv6를 감싸는 외부 IPv4 캡슐 구조
- [[network-layer]] — 터널링이 동작하는 계층
- [[protocol-layering]] — 동일 계층 프로토콜의 캡슐화를 보여주는 사례
- [[network-address-translation]] — IPv4 주소 부족 문제에 대한 다른 대응 기법 (NAT와 터널링은 공존)

## Open Questions
- IPv6 전환이 25년이 지나도 완료되지 않은 이유는 무엇인가? NAT의 존재가 IPv6 전환 인센티브를 약화시키는가? IPv6 전환은 언제 임계점(tipping point)에 도달할 것인가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
