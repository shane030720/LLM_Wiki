---
title: Packet Switching
category: concept
tags: [packet-switching, networking, routing, queueing, store-and-forward]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Packet Switching은 데이터를 패킷(packet) 단위로 분할하여 네트워크를 통해 전달하는 방식이다. 각 패킷은 헤더에 목적지 주소를 포함하고, 라우터는 이를 기반으로 독립적으로 다음 홉(next-hop)으로 전달한다. Circuit Switching과 달리 전용 경로를 사전 예약하지 않고 링크 자원을 공유한다.

## How It Works
**Store-and-Forward:**
- 라우터는 패킷 전체를 수신한 후(store) 다음 링크로 전달(forward)
- N홉 경로에서의 총 전송 지연 = N × L/R (L: 패킷 크기, R: 링크 속도)

**Queueing과 Packet Loss:**
- 인터넷의 IP 계층에서 패킷이 생성되어 gateway router로 전달됨
- Burst 도착에 대비해 라우터는 출력 링크마다 버퍼(queue) 유지
- 일반적으로 FIFO(First-In First-Out) 방식으로 패킷 처리
- 패킷 도착률이 출력 링크 속도를 초과하면 queueing 발생
- 큐가 가득 차면 이후 도착 패킷은 폐기(packet loss)

**Circuit Switching과 비교:**

| 특성 | Packet Switching | Circuit Switching |
|------|-----------------|------------------|
| 자원 할당 | 공유(shared) | 전용(dedicated) |
| 전달 방식 | 목적지 주소 기반 | 중앙 제어 방식 |
| 성능 보장 | 없음 | 보장됨 |
| 유휴 시 효율 | 높음 | 낮음(낭비) |
| 대표 적용 | 인터넷 | 전통 PSTN |

## Key Properties
- 인터넷은 packet switching 기반으로 동작
- Bursty 트래픽에 Circuit Switching보다 효율적
- Packet scheduling 알고리즘(FIFO 외 WFQ, Priority Queue 등)에 따라 처리 순서 결정 가능
- Packetization: 대용량 메시지를 분할하면 파이프라인 전송이 가능해 전체 지연 감소

## Relationships
- [[packet-delay]] — packet switching 환경에서 발생하는 4가지 지연 요소
- [[multiplexing]] — 공유 링크에서의 자원 공유 메커니즘
- [[network-performance-metrics]] — throughput과 RTT는 packet switching 성능의 핵심 지표
- [[network-connecting-devices]] — 라우터가 packet switching의 핵심 장치로 동작

## Open Questions
- FIFO 외 패킷 스케줄링 알고리즘(WFQ, Priority Queue)은 QoS 요구사항을 어떻게 충족시키는가?
- 패킷 손실 발생 시 TCP의 재전송 메커니즘은 어떻게 동작하는가?

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
