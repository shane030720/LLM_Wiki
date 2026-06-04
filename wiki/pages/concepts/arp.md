---
title: Address Resolution Protocol (ARP)
category: concept
tags: [network, link-layer, protocol, addressing, arp]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
ARP(Address Resolution Protocol, RFC 826)는 IP 주소(논리 주소)를 해당 링크 계층 하드웨어 주소(예: MAC 주소)로 동적으로 변환하는 프로토콜이다. 동일 서브넷(브로드캐스트 도메인) 내에서 동작하며, 사람의 개입 없이 자동으로 주소 변환을 수행한다. Point-to-point 링크는 ARP를 사용하지 않는다.

## How It Works

### 기본 동작 (Request / Reply)
1. 송신 호스트 A가 목적지 IP 주소를 포함한 ARP 요청(request)을 브로드캐스트(`FF:FF:FF:FF:FF:FF`)로 전송
2. 해당 IP를 가진 호스트 B가 자신의 MAC 주소를 담은 ARP 응답(reply)을 유니캐스트로 반환
3. A는 받은 매핑(IP → MAC)을 ARP 캐시(테이블)에 저장하고 이후 통신에 재사용

### ARP 패킷 포맷 (Ethernet ARP: 28 bytes)
- Ethernet 프레임의 'Length or Type' 필드 = `0x0806` (ARP 식별자)
- 'Prot Type' 필드 = `0x0800` (IPv4)
- IPv4/Ethernet ARP의 경우 (Hard Size, Prot Size) = (6, 4)
- ARP 요청: `Op = 1`, DST = `FF:FF:FF:FF:FF:FF`
- ARP 응답: `Op = 2`

### ARP Cache (테이블)
- 각 호스트와 라우터가 유지하는 최근 IP-MAC 매핑 테이블
- 완성된 항목(completed entry) TTL: **20분** (RFC 1122)
- 미완성 항목(incomplete entry, 응답 없음): **3분** 후 삭제
- 항목 사용 시마다 20분 타임아웃이 재시작되는 구현이 일반적 (RFC 1122 권고와 다름)
- `arp -a` 명령으로 현재 캐시 확인 가능 (Linux/Windows)
- ARP 캐시는 **soft state**의 대표 사례 — 타임아웃 전 갱신되지 않으면 폐기

### 서브넷 간 라우팅에서의 ARP 역할
다른 서브넷으로 패킷을 전달할 때 MAC 주소가 홉마다 교체된다:
1. 호스트 A는 IP 데이터그램의 목적지를 호스트 B의 IP로 설정
2. A는 링크 계층 프레임 목적지를 **라우터(R)의 MAC 주소**로 설정 (ARP로 획득)
3. R이 프레임 수신 → IP 데이터그램 추출 → B의 MAC 주소(ARP로 획득)로 새 프레임 생성
4. IP 주소(source/destination)는 End-to-End 내내 변경되지 않고, MAC 주소만 홉마다 교체

### Proxy ARP (RFC 1027)
- 라우터가 다른 호스트를 대신하여 ARP 요청에 응답하는 방식
- ARP 요청 송신자가 라우터를 목적지 호스트로 착각하게 함
- "Promiscuous ARP" 또는 "ARP hack"으로도 불림
- LAN 경계 보안을 약화시키므로 가능하면 사용 지양

### Gratuitous ARP (GARP)
- 호스트가 **자신의 IP 주소**를 조회하는 ARP 요청을 스스로 전송
- 인터페이스 부팅(bootstrap) 시 수행:
  - **목적 1**: IP 주소 중복 감지(Duplicate Address Detection)
  - **목적 2**: 다른 호스트의 ARP 캐시 갱신 (예: MAC 주소 변경 후)
- Linux-HA에서 백업 서버가 장애 서버를 인수(failover)할 때 활용

### IPv4 Address Conflict Detection (ACD, RFC 5227)
- **ARP probe**: Sender Protocol Address 필드를 0으로 설정한 ARP 요청 (캐시 오염 방지)
- 인터페이스 활성화 시 무작위 지연 후 3개의 probe 전송 (동시 전원 투입 혼잡 방지)
- 충돌 없으면 2초 간격으로 2개의 ARP announcement를 브로드캐스트 도메인에 전송 (기존 캐시 갱신)

## Key Properties
- **브로드캐스트 네트워크 전용**: Point-to-point 링크는 ARP 미사용
- **동적 매핑**: 사람의 개입 없이 자동으로 IP → MAC 주소 변환
- **Soft State**: ARP 캐시는 타임아웃 전에 갱신되지 않으면 자동 폐기
- **인증 없음**: ARP 메시지에 인증 메커니즘이 없어 ARP Spoofing/Poisoning에 취약
- **역방향 RARP** (RFC 903): 반대 방향(MAC → IP) 매핑이나 현재는 거의 미사용
- **ARP는 같은 서브넷 내에서만 직접 사용**: 다른 서브넷은 라우터의 MAC 주소를 경유

## Relationships
- [[mac-address]] (ARP는 IP 주소를 MAC 주소로 매핑하는 프로토콜)
- [[ethernet]] (ARP는 Ethernet 환경에서 가장 일반적으로 사용)
- [[ipv4-datagram]] (ARP는 IPv4 주소 기반 MAC 주소 조회에 활용)
- [[network-layer]] (ARP는 네트워크 계층과 링크 계층 사이의 주소 변환을 담당)
- [[icmp]] (ICMP와 마찬가지로 IP 계층의 정상 동작을 보조하는 프로토콜)
- [[vlan]] (VLAN은 브로드캐스트 도메인을 분리하여 ARP 요청의 전파 범위를 제한)

## Open Questions
- ARP 인증 메커니즘이 없어 ARP Spoofing에 취약한데, 이를 근본적으로 해결하는 방법(예: SARP, DAI)은?
- IPv6에서 ARP를 대체하는 NDP(Neighbor Discovery Protocol)는 어떤 구조적 차이를 가지는가?
- GARP를 악용한 공격 시나리오와 방어 방법은?

## Sources
- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
