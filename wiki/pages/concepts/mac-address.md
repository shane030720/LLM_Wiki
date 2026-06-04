---
title: MAC Address (Medium Access Control Address)
category: concept
tags: [network, link-layer, addressing, ethernet, hardware]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
MAC(Medium Access Control) 주소는 네트워크 인터페이스 카드(NIC)에 고유하게 부여된 48비트 하드웨어 주소로, 동일 서브넷(LAN) 내에서 한 인터페이스에서 다른 인터페이스로 프레임을 전달하기 위해 사용되는 링크 계층(Layer 2) 주소이다. LAN 주소, 물리 주소, Ethernet 주소라고도 불린다.

## How It Works
- 48비트를 16진수(hexadecimal) 표기법으로 나타냄 (예: `1A-2F-BB-76-09-AD`), 각 "숫자"가 4비트를 표현
- NIC ROM에 burned-in(영구 저장)되어 있으며, 경우에 따라 소프트웨어로 변경 가능
- IEEE가 MAC 주소 공간을 관리하고, 제조사가 주소 공간 일부를 구매하여 유일성을 보장
- IP 주소가 논리적 주소(네트워크 계층)인 반면, MAC 주소는 물리적 주소(링크 계층)
- 브로드캐스트 MAC 주소는 `FF-FF-FF-FF-FF-FF`로, LAN의 모든 노드에 프레임을 전달할 때 사용
- 각 LAN 인터페이스는 유일한 48비트 MAC 주소와 로컬 고유 32비트 IP 주소를 동시에 보유

## Key Properties
- **크기**: 48비트 (대부분의 LAN 환경)
- **표기법**: 16진수, 각 쌍을 하이픈 또는 콜론으로 구분
- **할당 주체**: IEEE가 관리; 제조사가 OUI(Organizationally Unique Identifier) 구매
- **이식성(Portability)**: flat address 구조이므로 LAN 간 이동이 가능 — IP 주소와 달리 서브넷에 종속되지 않음
- **유추**: MAC 주소 ≈ 주민등록번호(고유·불변), IP 주소 ≈ 우편 주소(위치 종속)
- **사용 범위**: 동일 서브넷 내 프레임 전달에만 사용; 서브넷 간에는 라우터에 의해 MAC 주소가 교체됨

## Relationships
- [[arp]] (ARP는 IP 주소에서 MAC 주소로의 동적 매핑을 제공하는 프로토콜)
- [[ethernet]] (Ethernet은 48비트 MAC 주소 체계를 사용하는 대표적 링크 계층 기술)
- [[network-layer]] (네트워크 계층의 IP 주소와 구별되는 링크 계층 주소 체계)
- [[vlan]] (VLAN은 MAC 주소 기반으로도 가상 LAN 멤버십을 정의할 수 있음)

## Open Questions
- 소프트웨어로 MAC 주소를 변경(MAC spoofing)할 수 있는 경우 보안상 어떤 위협이 발생하는가?
- IPv6 환경에서 EUI-64를 사용해 MAC 주소로부터 인터페이스 ID를 생성할 때 프라이버시 문제는 어떻게 완화하는가?

## Sources
- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
