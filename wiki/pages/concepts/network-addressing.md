---
title: Network Addressing
category: concept
tags: [networking, addressing, mac, ip, port, physical-address, logical-address, unicast]
sources: [raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

Network Addressing은 네트워크 상의 장치 또는 프로세스를 고유하게 식별하기 위한 체계이다. TCP/IP 프로토콜 스위트에서는 Physical Address(MAC 주소), Logical Address(IP 주소), Port Address(포트 번호)의 세 계층으로 구성되며, 각각 데이터 링크 계층, 네트워크 계층, 전송 계층에 대응한다. 패킷이 출발지에서 목적지로 이동하는 과정에서 물리 주소는 홉(hop)마다 교체되지만, 논리 주소는 원칙적으로 변경되지 않는다.

## How It Works

**Physical Address (MAC Address):**
- 링크 계층에서 사용; 동일 물리 매체에 연결된 노드 간 식별에 사용
- NIC(Network Interface Card) 제조사가 부여하여 하드웨어에 저장 → burned-in address, hardware address라고도 불림
- IEEE 802 네트워킹 기술(Ethernet, Wi-Fi, Bluetooth 등)에서 사용
- 현재 대부분 48비트이나 64비트 MAC 주소도 존재
- 표기 형식 (48비트 예시):
  ```
  ad:12:13:fc:14:ee   // 콜론 구분, 소문자
  AD:12:13:FC:14:EE   // 콜론 구분, 대문자
  ad-12-13-fc-14-ee   // 대시 구분
  ad1213fc14ee        // 구분자 없음
  ```
- Private MAC Address: 프라이버시 향상을 위해 Wi-Fi 네트워크별로 다른(랜덤화된) MAC 주소 사용 가능 (Apple, Samsung 등 지원); 따라서 burned-in MAC 주소가 항상 고정된 것은 아님

**Logical Address (IP Address):**
- 네트워크 계층에서 사용; 인터넷 전반의 종단간(end-to-end) 식별에 사용
- 각 NIC는 고유 IP 주소를 가짐 (단, 사설 IP 주소는 중복 가능: 예 192.168.0.1)
- 패킷 전달 중 원칙적으로 변경되지 않음 (실제로는 NAT 등으로 변경될 수 있음)
- MAC 주소와 마찬가지로 유니캐스트, 멀티캐스트, 브로드캐스트 주소로 분류

**Port Address (포트 번호):**
- 전송 계층에서 사용; 프로세스-투-프로세스 메시지 전달에 사용
- 네트워크 애플리케이션은 하나 이상의 포트 번호를 가짐

**패킷 전달 과정에서의 주소 변화:**

```
[출발지 A] ──Link1──> [라우터 R1] ──Link2──> [라우터 R2] ──Link3──> [목적지 B]
```

- 논리 주소(IP): 전 구간에서 변경되지 않음 (A의 IP → B의 IP 고정)
- 물리 주소(MAC): 각 링크 구간마다 다음 홉의 MAC 주소로 교체됨
  - Link1: 출발지 A의 MAC → 라우터 R1의 MAC
  - Link2: 라우터 R1의 MAC → 라우터 R2의 MAC
  - Link3: 라우터 R2의 MAC → 목적지 B의 MAC
- 각 라우터는 목적지 논리 주소(IP)와 다음 홉의 논리 주소, 다음 홉의 물리 주소(MAC) 매핑 테이블을 유지

**주소 유형 분류:**
- Unicast: 단일 수신자에게 전달
- Multicast: 수신자 그룹에게 전달
- Broadcast: 네트워크 내 모든 시스템에게 전달

## Key Properties

- 수신자 판별: 링크 계층에서 프레임의 목적지 주소와 일치하는 노드만 프레임을 수락하고, 나머지 노드는 폐기(discard)
- 프레임 헤더 구성: 일부 L2 프로토콜은 처리 속도 향상을 위해 목적지 주소를 출발지 주소보다 먼저 전송
- 모든 네트워크가 멀티캐스트/브로드캐스트를 지원하지는 않음 → 지원하지 않는 경우 유니캐스트 다중 전송으로 대체
- 논리 주소(IP)와 물리 주소(MAC) 간 매핑 필요 → ARP(Address Resolution Protocol)로 해결 (이후 강의에서 다룸)

## Relationships

- [[osi-reference-model]] — Physical Address는 Layer 2(Data Link), Logical Address는 Layer 3(Network), Port Address는 Layer 4(Transport)에 대응
- [[tcp-ip-architecture]] — TCP/IP의 각 계층에서 사용하는 주소 체계; Hourglass 모델의 각 계층에 해당
- [[protocol-layering]] — 각 계층은 자신의 주소 체계로 피어를 식별하며, 패킷 전달 시 계층별 주소가 encapsulation 구조를 형성
- [[computer-network]] — 네트워크에서 장치를 식별하고 데이터를 전달하기 위한 기본 메커니즘

## Open Questions

- 논리 주소(IP)와 물리 주소(MAC)의 동적 매핑은 어떻게 이루어지는가? (ARP 프로토콜 — 이후 강의에서 다룸)
- Private MAC Address(랜덤 MAC)의 도입이 네트워크 관리(DHCP, 접근 제어)와 보안(공격자 추적)에 미치는 상충 관계(trade-off)는?
- IPv6 주소(128비트)와 기존 48비트 MAC 주소 구조 간의 관계에서, EUI-64 방식으로 MAC에서 IPv6 주소를 자동 생성하는 방식의 프라이버시 함의는?
- NAT(Network Address Translation)가 "논리 주소는 전달 중 변경되지 않는다"는 원칙을 실질적으로 파괴하는데, 이를 어떻게 아키텍처적으로 이해할 것인가?

## Sources

- raw/컴퓨터네트워크/Week 02 OSI Reference Model.pdf
