---
title: Internet Control Message Protocol (ICMP)
category: concept
tags: [network, protocol, icmp, error-reporting, diagnostics]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
ICMP(Internet Control Message Protocol)는 호스트와 라우터가 네트워크 레벨의 정보를 주고받기 위해 사용하는 프로토콜로, 오류 보고(error reporting)와 진단(diagnostics) 기능을 제공한다. IP 계층 "위"에 위치하며, ICMP 메시지는 IP 데이터그램 안에 캡슐화되어 전송된다. 메시지 구조는 Type(1 byte), Code(1 byte), Checksum(2 bytes) 및 오류를 유발한 원본 IP 데이터그램의 첫 8바이트를 포함한다.

## How It Works

### 주요 ICMP 메시지 유형 (ICMPv4)

| Type | Code | 설명 |
|------|------|------|
| 0 | 0 | Echo Reply (ping 응답) |
| 3 | 0 | Destination Network Unreachable |
| 3 | 1 | Destination Host Unreachable |
| 3 | 2 | Destination Protocol Unreachable |
| 3 | 3 | Destination Port Unreachable |
| 3 | 4 | Fragmentation Required but DF bit is set |
| 3 | 6 | Destination Network Unknown |
| 3 | 7 | Destination Host Unknown |
| 3 | 13 | Communication Administratively Prohibited |
| 4 | 0 | Source Quench (혼잡 제어용, 현재 미사용) |
| 8 | 0 | Echo Request (ping 요청) |
| 9 | 0 | Router Advertisement |
| 10 | 0 | Router Discovery |
| 11 | 0 | TTL Expired |
| 12 | 0 | Bad IP Header |

### Echo Request / Reply (ping)
- 호스트 또는 라우터가 echo-request(type 8)를 전송하고, 수신자가 echo-reply(type 0)로 응답
- 목적지 호스트의 도달 가능성(reachability) 테스트에 활용
- `ping` 명령어가 이 메커니즘을 사용

### Destination Unreachable (type 3)
- **Network Unreachable (code 0)**: 라우팅 테이블에 경로 없음, 기본 경로 없음
- **Host Unreachable (code 1)**: 최종 목적지 호스트에 도달 불가; 호스트 또는 라우터가 생성
- **Protocol Unreachable (code 2)**: 목적지 호스트에서 특정 프로토콜 사용 불가
- **Port Unreachable (code 3)**: 목적지 호스트에서 특정 포트 사용 불가
- **Fragmentation Required but DF set (code 4)**: MTU보다 큰 데이터그램이 DF 비트 설정 상태로 라우터에 도착; 라우터가 폐기 후 송신측에 통보
- **Communication Administratively Prohibited (code 13)**: 방화벽 등 운용 정책에 의해 통신 차단; 방화벽이 오류 메시지를 보내지 않는 경우가 일반적

### Redirect 메시지
- 라우터가 같은 로컬 네트워크의 호스트에게 더 나은 경로(대체 라우터)를 알리는 메시지
- 호스트의 라우팅 정보를 동적으로 갱신하는 데 사용

### Time Exceeded (type 11)
- **Code 0**: 라우터가 TTL이 0이 된 패킷을 폐기할 때 생성
- **Code 1**: 목적지 호스트에서 단편화된 모든 조각이 일정 시간 내에 도착하지 않을 때 생성

### Parameter Problem (type 12)
- 라우터 또는 목적지 호스트가 잘못된 IP 헤더를 발견했을 때 생성
- Byte offset(pointer) 필드가 첫 번째 문제 필드의 위치를 가리킴

### Traceroute와 ICMP
1. 출발지가 TTL=1부터 시작하여 순차적으로 증가시켜 UDP 세그먼트를 목적지로 전송
2. n번째 라우터는 TTL이 0이 되면 패킷을 폐기하고 ICMP Time Exceeded(type 11, code 0)를 출발지로 반환; 메시지에 라우터 이름과 IP 주소 포함 가능
3. 목적지 호스트에 도달하면 ICMP Port Unreachable(type 3, code 3) 반환
4. 출발지는 각 홉의 RTT(Round Trip Time)를 기록하고 경로를 재구성
- 각 TTL 값에 대해 3개의 probe를 전송

## Key Properties
- **IP 계층 위에 위치**: ICMP 메시지는 IP 데이터그램에 캡슐화되어 전달
- **오류 보고 전용**: 데이터 전송 기능 없음; 제어 및 진단 용도
- **메시지 구조**: Type + Code + Checksum + 추가 필드 + 원본 IP 헤더와 데이터 앞 8바이트
- **Source Quench(type 4)**: 혼잡 제어 목적으로 설계되었으나 현재는 사용하지 않음
- **ICMPv6**: IPv6에서는 별도의 ICMPv6를 사용하며 기능이 확장됨 (NDP 포함)
- **방화벽 차단 문제**: 방화벽이 ICMP를 차단하면 Path MTU Discovery 등이 실패할 수 있음

## Relationships
- [[ipv4-datagram]] (ICMP 메시지는 IP 데이터그램에 캡슐화되어 전달)
- [[network-layer]] (ICMP는 네트워크 계층에서 오류 제어 및 진단 역할 담당)
- [[ipv4-fragmentation]] (type 3 code 4: Fragmentation Required but DF set 관련)
- [[path-mtu-discovery]] (DF 비트와 ICMP Fragmentation Required 메시지를 활용)
- [[arp]] (ARP와 마찬가지로 IP 계층 정상 동작을 보조하는 보조 프로토콜)
- [[tcp-congestion-control]] (Source Quench는 혼잡 제어를 위해 설계되었으나 현재 미사용)

## Open Questions
- 방화벽이 ICMP를 전면 차단할 때 발생하는 black hole 현상과 Path MTU Discovery 실패를 어떻게 해결하는가?
- ICMPv4와 ICMPv6의 주요 구조적·기능적 차이는 무엇인가?
- Traceroute에서 UDP 기반(Unix 기본)과 ICMP Echo 기반(Windows 기본) 구현 방식의 차이와 각각의 장단점은?

## Sources
- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
