---
title: Maximum Segment Size (MSS)
category: concept
tags: [tcp, mss, mtu, options, fragmentation, ethernet]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP가 피어로부터 수신하겠다는 최대 세그먼트 크기. TCP 데이터 바이트만 계산하며 TCP 헤더나 IP 헤더의 크기는 포함하지 않는다 (RFC 879). 연결 수립 시 SYN/SYN+ACK 세그먼트의 MSS 옵션으로 교환된다.

## How It Works

**MTU와 MSS의 관계**

```
MSS = MTU − IP 헤더 크기 − TCP 헤더 크기
```

- **MTU (Maximum Transmission Unit)**: 네트워크 인터페이스가 전송 가능한 최대 패킷 크기
  - 표준 이더넷 MTU: 1,500바이트 (초기 이더넷의 NIC 버퍼 비용과 전송 지연 균형을 위해 설정)
  - Jumbo Frame: 최대 약 9,000바이트 (하드웨어 호환성 및 방화벽 설정 문제로 보급 미흡)
- **표준 MSS 값**:
  - TCP/IPv4 + Ethernet: **1,460바이트** (1500 − 20 − 20)
  - TCP/IPv6 + Ethernet: **1,440바이트** (1500 − 40 − 20)
  - 기본값 (MSS 옵션 없을 때): **536바이트** (576바이트 IPv4 데이터그램 − 최소 헤더)
  - IPv6 Jumbogram: MSS = 65535 (특수값), 실제 SMSS = PMTU − 60바이트

**MSS 옵션 형식**

- 연결 수립 시 SYN (및 SYN+ACK) 세그먼트에만 포함
- 16비트로 MSS 값 표현 (최대 65,535바이트)
- MSS 옵션이 없을 경우 기본값 536바이트 적용 (현재는 매우 드문 상황)

**MSS는 협상이 아니라 한계치**

MSS 옵션은 "나는 이 크기보다 큰 세그먼트를 수락하지 않겠다"는 의사 표시이지, 상호 합의를 통한 협상이 아니다. 송신자는 상대방의 MSS 값을 초과하는 세그먼트를 보내서는 안 된다.

**SMSS (Sender Maximum Segment Size)**

실제 송신에 사용하는 최대 세그먼트 크기로, 다음 중 작은 값으로 결정:
- 상대방이 광고한 MSS
- 송신자 측 PMTU에서 헤더를 뺀 값

## Key Properties

- MSS는 TCP 데이터만 계산 (헤더 제외)
- 연결 수립 시 한 번만 교환되며 이후 변경 불가
- MTU보다 클 수 없으며, 경로 MTU 발견(PMTUD)에 의해 더 제한될 수 있음
- Jumbo Frame 미지원 환경에서는 1,460바이트(IPv4)가 표준
- TCP offload, Large Segment Offload 등의 NIC 기능이 1,500 MTU 프레임의 성능 한계를 보완

## Relationships

- [[path-mtu-discovery]] (PMTUD를 통해 경로 MSS가 동적으로 조정되는 과정)
- [[tcp-three-way-handshake]] (MSS 옵션이 SYN/SYN+ACK에서 교환되는 시점)
- [[tcp-header]] (MSS 옵션이 위치하는 TCP 헤더의 Options 필드)
- [[tcp]] (MSS가 TCP 세그멘테이션에 미치는 영향)

## Open Questions

- Jumbo Frame(9,000바이트 MTU)이 데이터센터 환경에서는 광범위하게 사용되는데, 일반 인터넷 경로에서도 채택되지 않는 근본적인 이유는 무엇인가?
- TCP offload 기능이 MSS 협상과 상호작용하는 방식은? NIC가 세그멘테이션을 대신 처리할 때 OS 레벨의 MSS는 어떻게 적용되는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 27–29)
