---
title: Gratuitous ARP
category: concept
tags: [arp, link-layer, address-resolution, network]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Gratuitous ARP(GARP)는 호스트가 자신의 IP 주소를 대상으로 ARP request를 전송하는 특수 ARP 동작이다. 다른 호스트의 MAC 주소를 알아내기 위한 일반적인 ARP와 달리, IP 주소 충돌 감지 및 브로드캐스트 도메인 내 ARP 캐시 갱신을 목적으로 사용된다. 이름의 "gratuitous(불필요한)"는 응답을 기대하지 않는 ARP request라는 의미에서 비롯된다.

## How It Works

호스트가 네트워크 인터페이스를 활성화하는 bootstrap 시점에 다음 절차(RFC 5227)를 수행한다.

1. **ARP Probe 전송**: Sender's Protocol (IP) Address 필드를 0으로 설정한 ARP request를 브로드캐스트한다. IP를 0으로 설정하는 이유는 다른 호스트의 ARP 캐시를 오염시키지 않기 위함이다. 동시 부팅 혼잡(simultaneous power-on congestion)을 피하기 위해 무작위 지연 알고리즘을 적용하여 3회 전송한다.
2. **충돌 감지**: 브로드캐스트 도메인 내 다른 호스트가 동일한 IP 주소를 사용 중이라면 ARP reply를 보낸다. 충돌이 발견되면 주소 설정을 중단한다.
3. **ARP Announcement**: 충돌이 없으면 자신의 실제 IP 주소를 Sender IP로 설정한 ARP announcement 패킷을 2초 간격으로 2회 브로드캐스트한다. 이를 통해 도메인 내 모든 호스트의 기존 ARP 캐시 항목이 갱신된다.

아래는 Windows 호스트 부팅 시 캡처된 GARP 예시다.

```
Linux# tcpdump -e -n arp
1 0.0 0:0:c0:6f:2d:40 ff:ff:ff:ff:ff:ff arp 60:
arp who-has 10.0.0.56 tell 10.0.0.56
```

## Key Properties

- Sender IP = 자신의 IP (ARP announcement) 또는 0 (ARP probe)
- 브로드캐스트 주소(FF:FF:FF:FF:FF:FF)로 전송
- 두 가지 목적: (1) IP 주소 충돌 감지, (2) 다른 호스트의 ARP 캐시 갱신
- MAC 주소 변경(예: NIC 교체 후 재부팅) 후 인접 호스트들의 오래된 캐시 항목을 최신화하는 데 유용
- Linux-HA에서 장애 서버를 대체하는 백업 서버가 GARP를 이용해 자신의 MAC 주소를 알림(failover 용도)

## Relationships

- [[arp]] (Gratuitous ARP의 기반이 되는 Address Resolution Protocol)
- [[proxy-arp]] (또 다른 ARP 변형 동작)
- [[mac-address]] (ARP 캐시에 저장되는 링크 계층 주소)

## Open Questions

- RFC 1122는 ARP 캐시 타임아웃을 항목이 사용 중일 때도 적용해야 한다고 명시하지만, 많은 구현이 이를 따르지 않아 실제 캐시 유효 기간이 불일치할 수 있다.
- ARP probe 무작위 지연 알고리즘의 구체적 파라미터는 구현마다 다를 수 있어, 대규모 동시 부팅 환경에서의 실제 효과에 대한 검증이 필요하다.

## Sources

- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
