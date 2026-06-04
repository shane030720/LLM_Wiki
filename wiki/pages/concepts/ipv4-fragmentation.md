---
title: IPv4 Fragmentation
category: concept
tags: [ip, ipv4, fragmentation, mtu, reassembly, flags]
sources: [raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

IPv4 Fragmentation(IPv4 단편화)은 IP 데이터그램 크기가 링크의 MTU(Maximum Transfer Unit)를 초과할 때, 라우터가 데이터그램을 여러 개의 작은 단편(fragment)으로 분할하는 메커니즘이다. 단편들은 각각 독립적인 IP 데이터그램으로 전달되며, 오직 최종 수신 호스트에서만 원본 데이터그램으로 재조립(reassembly)된다.

## How It Works

### MTU와 단편화 필요성

- 인터넷을 구성하는 각 링크 유형은 서로 다른 MTU를 가짐 (예: Ethernet 기본 MTU = 1500바이트)
- IP 데이터그램이 특정 링크의 MTU를 초과하면 해당 라우터가 단편화 수행
- 단편 재조립은 중간 라우터가 아닌 최종 목적지 호스트에서만 수행

### 제어 필드

IPv4 헤더의 3비트 **Flags** 필드:
- **Bit 0 (Reserved)**: 예약됨, 항상 0
- **Bit 1 — DF (Don't Fragment)**: 1이면 라우터가 단편화 금지; 데이터그램이 MTU 초과 시 폐기하고 ICMP 메시지를 송신자에게 전송
- **Bit 2 — MF (More Fragments)**: 1이면 이후 단편이 더 존재; 마지막 단편만 0

13비트 **Fragment Offset** 필드:
- 해당 단편이 원본 데이터그램의 어느 위치에서 시작하는지를 8바이트 단위로 표시
- 8바이트 단위를 사용하는 이유: 오프셋 필드 13비트에 맞추기 위해 최하위 3비트(= Flags 필드)를 생략

### 단편화 예시

원본 4000바이트 데이터그램, MTU = 1500바이트인 링크 통과 시:

| 단편 | ID | Offset | MF | Length |
|------|----|--------|----|--------|
| Fragment 1 | x | 0 | 1 | 1500 (헤더 20B + 데이터 1480B) |
| Fragment 2 | x | 185 (=1480÷8) | 1 | 1500 |
| Fragment 3 | x | 370 (=2960÷8) | 0 | 1040 |

- 세 단편 모두 동일한 Identification 값(x)을 공유
- Total Length 필드는 각 단편의 크기를 나타냄

### 재단편화

이미 단편화된 단편이 더 작은 MTU를 가진 링크를 만나면 추가로 단편화될 수 있다. 각 단편은 독립적인 IP 데이터그램으로 처리되므로, 원래 오프셋을 기준으로 계산된 서브-오프셋이 적용된다.

### IPv6에서의 차이

- IPv6는 중간 라우터에서의 단편화를 **허용하지 않음**
- 종단 호스트만이 IPv6 단편 확장 헤더(Fragment Extension Header)를 사용하여 단편화 가능
- 라우터는 DF=1인 IPv4 패킷과 유사하게 MTU 초과 패킷을 폐기하고 ICMPv6 메시지를 반환
- Path MTU Discovery를 통해 송신 호스트가 경로상 최소 MTU를 미리 파악하여 단편화 자체를 회피

## Key Properties

- 단편화는 라우터에서 수행되지만 재조립은 수신 호스트에서만 수행 (중간 라우터 재조립 없음)
- 동일한 Identification 필드 값을 가진 단편들이 하나의 원본 데이터그램에 속함
- Fragment Offset은 8바이트 단위; 데이터 필드 크기는 항상 8의 배수여야 함 (마지막 단편 제외)
- DF 비트 설정 시 MTU 초과 데이터그램은 라우터에서 폐기됨
- IPv6는 라우터 단편화 금지로 라우터 처리 부담 경감

## Relationships

- [[ipv4-datagram]] — Identification·Flags·Fragment Offset 필드를 포함하는 헤더 구조
- [[path-mtu-discovery]] — DF 비트와 ICMP를 활용하여 경로 MTU를 탐색, 단편화 회피
- [[network-layer]] — 단편화가 수행되는 계층
- [[maximum-segment-size]] — TCP 레벨에서 단편화가 발생하지 않도록 MSS를 조정하는 메커니즘
- [[ethernet]] — 일반적인 MTU 1500바이트를 제공하는 대표적인 링크 계층 프로토콜

## Open Questions

- 단편 손실 시 전체 데이터그램을 재전송해야 하는 비효율성이 실제 성능에 미치는 영향은 얼마나 큰가?
- IPv6에서 종단 호스트 전담 단편화 모델이 모바일 환경(MTU 변동 잦음)에서 실제로 효율적인가?
- 단편화를 이용한 방화벽 우회 공격(Tiny Fragment Attack 등)은 현재 어떻게 방어되는가?

## Sources

- raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf
