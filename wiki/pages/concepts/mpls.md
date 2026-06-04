---
title: Multiprotocol Label Switching (MPLS)
category: concept
tags: [network, routing, mpls, traffic-engineering, label-switching]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
MPLS(Multiprotocol Label Switching)는 MPLS 가능 라우터 네트워크에서 최장 프리픽스 매칭(longest prefix matching) 대신 고정 길이 레이블(label)을 사용하여 패킷을 고속으로 전달하는 기술이다. Virtual Circuit(VC) 방식의 아이디어를 차용하면서도 IP 데이터그램 내의 IP 주소는 그대로 유지한다.

## How It Works

### MPLS 헤더 구조 (4 bytes)
Ethernet 헤더와 IP 헤더 사이에 삽입:

| 필드 | 크기 | 설명 |
|------|------|------|
| Label | 20 bits | 패킷 전달에 사용하는 고정 길이 식별자 |
| Exp | 3 bits | 실험적 용도 (QoS 등에 활용) |
| S (Bottom-of-Stack) | 1 bit | 레이블 스택의 마지막 레이블 표시 |
| TTL | 8 bits | Time To Live |

### Label-Switched Router (LSR)
- MPLS 가능 라우터를 LSR(label-switched router)이라 함
- IP 주소를 검사하지 않고 **레이블 값만으로** 출력 인터페이스 결정
- MPLS 전달 테이블(forwarding table)은 IP 전달 테이블과 별도로 유지

### 동작 흐름
1. **진입 라우터(Ingress/Entry Router)**: IP 패킷에 MPLS 레이블을 부착하여 MPLS 도메인에 진입
2. **중간 LSR**: 수신된 레이블을 새 레이블로 교체(label swapping)하면서 전달
3. **출구 라우터(Egress Router)**: MPLS 레이블을 제거하고 일반 IP 전달로 복귀

### MPLS vs IP 경로 비교
- **IP 라우팅**: 목적지 주소만으로 경로 결정 — 동일 목적지에는 항상 동일 경로
- **MPLS 라우팅**: 목적지 주소 + 출발지 주소 + 기타 필드를 조합하여 경로 결정 가능
  - **Traffic Engineering**: 같은 목적지라도 출발지에 따라 다른 경로로 전달
  - **Fast Reroute**: 링크 장애 발생 시 미리 계산된 백업 경로로 즉시 전환

### MPLS Signaling
- OSPF, IS-IS 링크 상태 flood 프로토콜을 수정하여 MPLS 라우팅 정보 전달 (링크 대역폭, 예약 대역폭 등)
- **RSVP-TE (Resource Reservation Protocol - Traffic Engineering)**: 진입 MPLS 라우터가 하위 라우터들에 MPLS 전달 설정을 위해 사용하는 시그널링 프로토콜

### MPLS 전달 테이블
각 LSR은 `(입력 레이블) → (출력 레이블, 목적지, 출력 인터페이스)` 매핑 테이블을 유지하며, 레이블 값만으로 O(1)에 가까운 조회가 가능하다.

## Key Properties
- **고속 조회**: 고정 길이 레이블로 IP 주소 기반 최장 프리픽스 매칭보다 빠른 전달
- **IP 주소 보존**: 데이터그램 내 IP 주소는 변경되지 않음
- **유연한 경로 설정**: 출발지 주소 등 다양한 기준으로 트래픽 엔지니어링 가능
- **Fast Reroute**: 링크 장애 시 미리 계산된 백업 경로로 즉시 전환; IP 재수렴보다 빠름
- **멀티프로토콜**: IP 외 다른 프로토콜도 레이블 기반 전달 가능 (이름의 유래)
- **Generalized Forwarding의 선구자**: 현대 SDN의 일반화된 전달 개념을 약 10년 앞서 구현

## Relationships
- [[network-layer]] (MPLS는 네트워크 계층에서 동작하는 고속 전달 기술)
- [[router-architecture]] (LSR은 MPLS 전달 테이블을 사용하는 특수 라우터)
- [[ip-forwarding]] (MPLS는 IP 포워딩을 레이블 기반으로 대체·보완)
- [[longest-prefix-matching]] (MPLS는 최장 프리픽스 매칭의 대안으로 고정 길이 레이블 사용)
- [[vlan]] (VXLAN/EVPN은 MPLS와 유사하게 Layer 2를 Layer 3 위에 오버레이하는 접근)

## Open Questions
- SDN(Software Defined Networking) 및 Segment Routing(SR)의 등장으로 MPLS의 역할이 어떻게 변화하고 있는가?
- MPLS Fast Reroute와 IP 수준 Fast Reroute(LFA 등)의 failover 속도 차이는 얼마인가?
- MPLS 레이블 스택(label stacking)을 활용하는 계층적 트래픽 엔지니어링은 어떻게 동작하는가?

## Sources
- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
