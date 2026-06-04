---
title: Virtual Local Area Network (VLAN)
category: concept
tags: [network, link-layer, vlan, switching, isolation, 802.1q]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
VLAN(Virtual Local Area Network)은 단일 물리적 스위치 인프라 위에 여러 가상 LAN을 구성하는 기술로, 포트 그룹화 또는 MAC 주소 기반으로 브로드캐스트 도메인을 논리적으로 분리한다. 물리적 위치와 무관하게 논리적 네트워크 소속을 유지할 수 있으며, 확장성·보안·프라이버시 문제를 해결한다.

## How It Works

### VLAN의 동기
단일 브로드캐스트 도메인에서 발생하는 문제:
- **확장성**: ARP, DHCP, unknown MAC 등 Layer 2 브로드캐스트가 전체 LAN에 전파
- **보안/프라이버시**: 부서 간 트래픽이 물리적으로 동일 네트워크를 공유
- **관리**: 사용자가 물리적으로 이동해도 논리적 네트워크 소속 유지 필요

### Port-based VLAN
- 스위치 포트를 그룹으로 묶어 각 그룹이 독립적인 가상 스위치처럼 동작
- 예: 포트 1-8 → EE 부서 VLAN, 포트 9-15 → CS 부서 VLAN
- 동일 VLAN 포트 간에만 프레임 교환; VLAN 간 통신은 반드시 라우터를 경유
- MAC 주소 기반으로도 VLAN 멤버십 정의 가능 (엔드포인트의 물리적 포트에 독립적)

### 트래픽 격리 및 동적 멤버십
- **트래픽 격리**: 특정 VLAN의 트래픽은 같은 VLAN 내에서만 전달
- **동적 멤버십**: 포트를 관리 소프트웨어로 VLAN 간 동적 재할당 가능
- **VLAN 간 통신**: 라우터(또는 Layer 3 스위치)를 통해야만 가능; 벤더는 스위치+라우터 통합 제품 판매

### VLAN Spanning (복수 스위치 간 VLAN)
- **Trunk Port**: 여러 물리적 스위치에 걸쳐 정의된 VLAN의 프레임을 전달하는 특수 포트
- Trunk port를 통해 전달되는 프레임은 vanilla 802.1 프레임이 아닌 VLAN ID 정보를 포함해야 함
- **802.1Q 프로토콜**: Trunk port 간 전달 시 프레임에 VLAN 태그를 추가하고, 수신 측에서 제거

### 802.1Q 프레임 포맷
기존 802.1 Ethernet 프레임에 4바이트 태그를 삽입:

| 필드 | 크기 | 값/설명 |
|------|------|---------|
| Tag Protocol Identifier | 2 bytes | `0x81-00` (802.1Q 식별) |
| Tag Control Information | 2 bytes | 12비트 VLAN ID + 3비트 우선순위(IP TOS 유사) |

CRC는 태그 삽입 후 재계산됨.

### EVPN (Ethernet VPN) / VXLAN
- **VXLAN (Virtual Extensible LAN, RFC 7348)**: Layer 2 Ethernet 프레임을 Layer 3 IP 데이터그램에 캡슐화하는 터널링 기술
- Layer 3 네트워크 위에 Layer 2 네트워크를 오버레이하여 데이터센터 간 Layer 2 도메인을 논리적으로 "확장(stretch)"
- Layer 2 스위치들이 IP underlay를 통해 논리적으로 직접 연결된 것처럼 동작

## Key Properties
- **논리적 분리**: 물리적 스위치는 하나이지만 복수의 독립 브로드캐스트 도메인으로 분할
- **확장성**: 브로드캐스트 도메인 축소로 ARP, DHCP 트래픽 억제
- **보안/프라이버시**: 부서 간 트래픽 격리로 보안 정책 적용 용이
- **유연한 관리**: 사용자가 물리적으로 이동해도 논리적 VLAN 소속 유지 가능
- **VLAN 간 통신**: 라우터 필수 경유 — 격리의 핵심 메커니즘
- **802.1Q VLAN ID**: 12비트 → 최대 4094개 VLAN 지원 (대규모 클라우드 환경에서는 한계)
- **VXLAN**: 24비트 VNI(VXLAN Network Identifier) → 최대 약 1600만 개 가상 네트워크

## Relationships
- [[ethernet]] (VLAN은 Ethernet 스위치 인프라 위에 구성되며 802.1Q는 Ethernet 프레임을 확장)
- [[mac-address]] (Port-based VLAN 외에 MAC 주소 기반으로도 VLAN 멤버십 정의 가능)
- [[arp]] (VLAN은 브로드캐스트 도메인을 제한하여 ARP 요청의 전파 범위를 축소)
- [[network-connecting-devices]] (스위치가 VLAN 기능 제공; VLAN 간 통신은 라우터 또는 Layer 3 스위치 필요)
- [[mpls]] (VXLAN/EVPN은 MPLS와 유사하게 하위 계층 네트워크 위에 상위 계층을 오버레이하는 개념 공유)

## Open Questions
- 802.1Q VLAN ID가 12비트(최대 4094 VLAN)인데, 대규모 클라우드/데이터센터 환경에서 이 한계를 어떻게 극복하는가? (VXLAN의 24비트 VNI가 해결책인가?)
- VXLAN에서 BUM(Broadcast, Unknown unicast, Multicast) 트래픽을 어떻게 처리하는가?
- VLAN과 VRF(Virtual Routing and Forwarding)의 역할 차이는 무엇이며, 언제 각각을 선택해야 하는가?

## Sources
- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
