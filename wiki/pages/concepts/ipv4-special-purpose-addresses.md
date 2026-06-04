---
title: IPv4 Special-Purpose Addresses
category: concept
tags: [networking, IPv4, addressing, broadcast, loopback]
sources: [raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
IPv4 Special-Purpose Addresses(IPv4 특수 목적 주소)는 일반 유니캐스트 주소 할당에 사용되지 않고 특정 기능을 위해 예약된 IPv4 주소 범위이다 [RFC6890]. 이 주소들은 로컬 네트워크 통신, 자기 참조(loopback), 브로드캐스트, 조직 내부 전용 통신 등에 사용된다.

## How It Works
주요 특수 목적 주소와 용도:

| 주소/범위 | 이름 | 용도 |
|---|---|---|
| 0.0.0.0 | This host, this network | 아직 IP가 없을 때 출발지 주소 (DHCP 요청 등) |
| 255.255.255.255 | Limited broadcast | 동일 링크의 모든 호스트 브로드캐스트 (라우터 전달 안 됨) |
| 127.0.0.0/8 | Loopback | 자기 자신 참조; 패킷이 네트워크 밖으로 나가지 않음 |
| 네트워크주소.호스트올1 | Directed broadcast | 특정 서브넷의 모든 호스트에게 브로드캐스트 |
| 10/8, 172.16/12, 192.168/16 | Private addresses | 조직 내부 전용; 인터넷에서 라우팅 안 됨 |

**0.0.0.0 사용 예**: 호스트가 DHCP를 통해 IP를 얻기 전, 출발지 주소를 0.0.0.0으로 설정하고 목적지를 255.255.255.255로 설정하여 브로드캐스트 요청을 전송한다.

**Loopback 동작**: 127.x.y.z로 향하는 IP 데이터그램은 네트워크 밖으로 나가지 않으며, 루프백 인터페이스가 처리한다. 같은 호스트 내 프로세스 간 통신(IPC)에 활용된다. 외부에서는 관찰 불가.

**Limited broadcast vs. Directed broadcast**:
- Limited broadcast(255.255.255.255): 현재 링크 범위 내 브로드캐스트, 라우터가 전달하지 않음
- Directed broadcast(예: 221.45.71.255/24): 특정 네트워크의 모든 호스트로 전달 가능하나, 보안상 이유로 대부분의 라우터에서 차단

## Key Properties
- 특수 목적 주소는 일반 유니캐스트 목적으로 할당되지 않음 (RFC6890)
- Private 주소(10/8, 172.16/12, 192.168/16)는 [[network-address-translation]] 과 함께 인터넷 연결에 사용
- Limited broadcast는 link-local 범위에 한정 (라우터를 넘지 않음)
- Loopback 주소를 통한 트래픽은 호스트 외부에서 관찰 불가능
- Directed broadcast는 smurf attack 등 DDoS에 악용 가능하여 대부분 ISP가 차단

## Relationships
- [[network-address-translation]] — private 주소를 공인 주소로 변환하는 NAT
- [[ipv4-datagram]] — 특수 목적 주소가 포함되는 IPv4 데이터그램 구조
- [[network-addressing]] — 전반적인 IP 주소 지정 체계
- [[cidr]] — 특수 목적 주소 블록도 CIDR 표기법으로 정의됨

## Open Questions
- Directed broadcast는 보안 위협으로 인해 사실상 폐기 상태이나, RFC에서 공식 deprecated 처리는 복잡한 호환성 문제를 야기한다. 어디까지가 "특수 목적"이고 어디서부터가 "일반 사용"인지 기준은 어떻게 진화해야 하는가?

## Sources
- raw/컴퓨터네트워크/Week 10 Internet Protocol (2).pdf
