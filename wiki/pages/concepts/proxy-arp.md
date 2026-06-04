---
title: Proxy ARP
category: concept
tags: [arp, network, router, link-layer, security]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Proxy ARP [RFC 1027]는 라우터(또는 특별히 구성된 시스템)가 다른 호스트를 대신하여 ARP request에 응답하는 기법이다. ARP request 발신자는 라우터가 목적지 호스트인 것으로 착각하게 되며(fool), 실제 목적지 호스트는 별도의 네트워크에 위치하거나 존재하지 않을 수도 있다. "Promiscuous ARP" 또는 "ARP hack"이라고도 불린다.

## How It Works

1. 호스트 A가 목적지 IP 주소에 대한 ARP request를 브로드캐스트한다.
2. Proxy ARP로 구성된 라우터가 해당 IP 주소에 대한 요청을 수신한다.
3. 라우터는 목적지 호스트 대신 자신의 MAC 주소를 포함한 ARP reply를 A에게 전송한다.
4. 호스트 A는 라우터의 MAC 주소를 목적지로 여기고 트래픽을 라우터로 전달한다.
5. 라우터는 실제 목적지 네트워크로 패킷을 포워딩한다.

아래는 SLIP(다이얼업) 링크로 연결된 환경에서 Proxy ARP 라우터가 sun(140.252.1.183)을 대신해 ARP request에 응답하는 예시다.

```
ARP request for 140.252.1.29  →  Telebit NetBlazer (proxy ARP 에이전트)
ARP reply                     ←  라우터가 자신의 MAC으로 응답
```

## Key Properties

- 라우터가 ARP request에 자신의 MAC 주소로 대신 응답
- 발신 호스트가 라우터를 목적지 호스트로 착각하도록 동작
- LAN 경계 보안(LAN perimeter security)을 약화시킴
- 일반적으로 사용이 권장되지 않음
- 역사적 사용 사례: (1) 두 물리 네트워크를 서로에게 숨기기, (2) 서브넷팅을 지원하지 않는 구형 시스템 처리

## Relationships

- [[arp]] (Proxy ARP의 기반 프로토콜)
- [[gratuitous-arp]] (또 다른 ARP 변형 동작)
- [[network-connecting-devices]] (라우터가 Proxy ARP 에이전트 역할을 수행)

## Open Questions

- 현대 클라우드/가상화 환경에서 가상 라우터나 하이퍼바이저가 Proxy ARP를 활용하는 시나리오가 증가하는지 여부
- Proxy ARP 사용 시 LAN 보안 위협(ARP spoofing과의 관계)을 어떻게 완화할 수 있는지

## Sources

- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
