---
title: TCP State Machine
category: concept
tags: [tcp, state-machine, finite-state-machine, connection, transition]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP의 연결 수립, 데이터 전송, 연결 종료 단계에서 발생하는 모든 이벤트를 추적하기 위해 TCP를 유한 상태 기계(Finite State Machine)로 명세한 것. 각 엔드포인트는 독립적으로 자신의 TCP 상태를 유지한다.

## How It Works

TCP 상태는 전송/수신 이벤트에 따라 전이(transition)되며, 주요 상태와 의미는 다음과 같다:

| 상태 | 의미 |
|------|------|
| CLOSED | 연결 없음. 초기 상태 |
| LISTEN | 서버가 passive open 후 SYN 대기 중 |
| SYN_SENT | 클라이언트가 SYN을 보내고 SYN+ACK 대기 중 |
| SYN_RCVD | 서버가 SYN을 수신하고 SYN+ACK를 보낸 후 ACK 대기 중 |
| ESTABLISHED | 연결이 수립되어 데이터 전송 가능한 정상 상태 |
| FIN_WAIT_1 | Active close 측이 FIN을 보내고 ACK 대기 중 |
| FIN_WAIT_2 | FIN에 대한 ACK를 받고 상대방의 FIN 대기 중 |
| CLOSE_WAIT | Passive close 측이 FIN을 받고 자신의 FIN 전송 대기 중 |
| CLOSING | 양쪽이 동시에 FIN을 보낸 경우, 상대방의 FIN에 대한 ACK 대기 |
| LAST_ACK | Passive close 측이 자신의 FIN을 보내고 최종 ACK 대기 중 |
| TIME_WAIT | Active close 측이 최종 ACK를 보낸 후 2MSL 대기 중 |

**연결 수립 전이 경로 (클라이언트)**:
CLOSED → SYN_SENT → ESTABLISHED

**연결 수립 전이 경로 (서버)**:
CLOSED → LISTEN → SYN_RCVD → ESTABLISHED

**연결 종료 전이 경로 (Active close)**:
ESTABLISHED → FIN_WAIT_1 → FIN_WAIT_2 → TIME_WAIT → CLOSED

**연결 종료 전이 경로 (Passive close)**:
ESTABLISHED → CLOSE_WAIT → LAST_ACK → CLOSED

`netstat` 명령어의 `-t` 옵션으로 현재 시스템의 모든 TCP 엔드포인트 상태를 확인할 수 있다.

## Key Properties

- 각 TCP 엔드포인트는 독립적인 상태 기계를 운영
- TCP 상태 기계는 연결 수립, 데이터 전송, 연결 종료를 하나의 통합된 명세로 표현
- TIME_WAIT 상태는 active close를 수행한 쪽만 진입 (passive close 쪽은 LAST_ACK → CLOSED)
- Simultaneous open 시: CLOSED → SYN_SENT → SYN_RCVD → ESTABLISHED (4 세그먼트 교환)
- Simultaneous close 시: ESTABLISHED → FIN_WAIT_1 → CLOSING → TIME_WAIT → CLOSED

## Relationships

- [[tcp-three-way-handshake]] (CLOSED→ESTABLISHED 전이를 유발하는 3-way handshake)
- [[time-wait-state]] (active close 후 진입하는 TIME_WAIT/2MSL 상태의 상세)
- [[tcp-reset-segment]] (RST 수신 시 즉시 CLOSED로 전이되는 경우)
- [[tcp]] (TCP 프로토콜 전반 개요)

## Open Questions

- SYN_RCVD 상태가 SYN Flood 공격의 주요 타겟인데, TCP 상태 기계 수준에서 이를 방어하는 SYN Cookie 메커니즘은 어떻게 동작하는가?
- CLOSE_WAIT 상태에서 앱이 `close()`를 호출하지 않아 계속 머무르는 경우(CLOSE_WAIT leak), 진단과 해결 방법은?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 43–47)
