---
title: EVPN (Ethernet VPN / VXLAN)
category: concept
tags: [vlan, overlay, tunneling, network, data-center, ethernet]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

EVPN(Ethernet Virtual Private Network)은 Layer 2 Ethernet 프레임을 Layer 3 IP 데이터그램 내에 캡슐화하여 전송하는 오버레이 네트워킹 기술이다. VXLAN(Virtual Extensible LAN, RFC 7348)은 EVPN의 대표적인 데이터 플레인 캡슐화 방식으로, 기존 IP 라우팅 인프라(underlay) 위에 Layer 2 네트워크를 논리적으로 확장(stretch)한다. 지리적으로 분리된 데이터센터 간에 동일한 Layer 2 브로드캐스트 도메인을 공유할 수 있게 해준다.

## How It Works

1. 서로 다른 물리적 위치(예: Sunnyvale 데이터센터, Bangalore 데이터센터)에 있는 Layer 2 Ethernet 스위치들이 IP 네트워크를 underlay로 사용하여 논리적으로 연결된다.
2. 출발지 스위치(VTEP: VXLAN Tunnel Endpoint)가 원래 Ethernet 프레임을 IP 데이터그램 페이로드로 캡슐화한다.
3. 캡슐화된 IP 데이터그램이 기존 Layer 3 라우팅 인프라를 통해 목적지 사이트로 전달된다.
4. 목적지 VTEP이 캡슐화를 해제하고 원래 Ethernet 프레임을 복원하여 로컬 스위치로 전달한다.

RFC 7348은 이를 "Layer 2 네트워크를 Layer 3 네트워크 위에 오버레이하는 터널링 방식으로, 기존 네트워킹 인프라 위에서 동작하며 Layer 2 네트워크를 '확장'하는 수단을 제공한다"고 정의한다.

## Key Properties

- Ethernet 프레임이 IP 데이터그램 내에 캡슐화되어 Layer 3 인프라를 통해 전송됨
- Layer 2 네트워크를 물리적 경계를 넘어 확장 가능
- 기존 IP 라우팅 인프라를 underlay로 그대로 활용하므로 별도 물리 인프라 불필요
- 주로 멀티-사이트 데이터센터 연결 및 클라우드 환경에서 활용
- RFC 7348 표준 정의

## Relationships

- [[vlan]] (EVPN은 VLAN의 확장 개념으로, 단일 물리 스위치 내 격리를 넘어 다수의 물리적 위치로 확장)
- [[mpls]] (유사한 레이블 기반 오버레이 터널링 개념과 비교)
- [[protocol-layering]] (Layer 2를 Layer 3 위에 오버레이하는 계층화 원리를 활용)
- [[ipv4-datagram]] (Ethernet 프레임 캡슐화 수단으로 사용)

## Open Questions

- EVPN과 VXLAN의 정확한 관계: VXLAN은 데이터 플레인 캡슐화 방식이고 EVPN은 BGP 기반 컨트롤 플레인 프로토콜로, 개념상 동일하지 않으나 실제로 함께 사용되는 경우가 많다.
- 대규모 배포 시 BUM(Broadcast, Unknown unicast, Multicast) 트래픽을 어떻게 효율적으로 처리할 것인지(멀티캐스트 vs. Ingress Replication 방식 간의 트레이드오프)가 미해결 과제다.
- SDN 환경에서 EVPN/VXLAN과 중앙집중식 컨트롤러의 통합 방식에 대한 표준화가 진행 중이다.

## Sources

- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
