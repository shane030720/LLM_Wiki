---
title: Traceroute
category: entity
tags: [icmp, network, diagnostic, ttl, tool]
sources: [raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Overview

Traceroute는 패킷이 출발지에서 목적지까지 거치는 경로(hop sequence)와 각 구간의 RTT(Round-Trip Time)를 측정하는 네트워크 진단 도구다. IP 헤더의 TTL 필드와 ICMP의 TTL 만료 메시지(type 11)를 조합하여 경로상의 각 라우터를 순차적으로 식별한다. Unix/Linux에서는 `traceroute`, Windows에서는 `tracert` 명령으로 제공된다.

## Capabilities

- 출발지에서 목적지까지의 전체 라우팅 경로(라우터 IP 주소 및 이름) 시각화
- 각 hop에서 3회 프로브(probe)를 전송하여 RTT 측정
- 경로상 병목 구간 또는 장애 발생 위치 파악

**동작 원리 (ICMP + UDP 기반):**

1. 출발지는 TTL=1로 설정된 UDP 세그먼트 집합을 목적지를 향해 전송
2. 첫 번째 라우터에서 TTL이 0이 되면 데이터그램을 폐기하고 ICMP type 11 code 0 (TTL expired) 메시지를 출발지로 반환; 메시지에는 라우터 이름과 IP 주소가 포함될 수 있음
3. 출발지는 ICMP 메시지 수신 시간으로 RTT를 기록
4. TTL을 1씩 증가시키며(TTL=2, 3, ...) 동일한 과정을 반복하여 경로상의 각 라우터를 식별
5. UDP 세그먼트가 최종 목적지에 도달하면 목적지는 ICMP type 3 code 3 (Port Unreachable) 메시지를 반환
6. 출발지가 Port Unreachable 메시지를 수신하면 탐색 종료

```
3 probes (TTL=1) → RTT 측정 → 1번째 라우터 식별
3 probes (TTL=2) → RTT 측정 → 2번째 라우터 식별
...
3 probes (TTL=n) → ICMP Port Unreachable → 종료
```

## Limitations

- 방화벽이 ICMP 또는 고번호 UDP 포트를 차단하면 해당 hop이 `* * *`으로 표시됨
- 비대칭 라우팅 환경에서는 실제 데이터 전송 경로와 traceroute 결과가 다를 수 있음
- 일부 라우터는 ICMP TTL expired 메시지 생성의 우선순위를 낮게 설정하여 RTT가 과대 측정될 수 있음
- load balancing 환경에서 TTL 레벨마다 서로 다른 경로로 패킷이 전달될 수 있어 일관성이 떨어질 수 있음

## Relationships

- [[icmp]] (TTL 만료(type 11) 및 Port Unreachable(type 3 code 3) 메시지를 활용)
- [[ipv4-datagram]] (TTL 필드 감소 메커니즘 기반)
- [[network-performance-metrics]] (RTT 측정 도구로서의 역할)

## Sources

- raw/컴퓨터네트워크/Week 11. ARP, ICMP, and MPLS.pdf
