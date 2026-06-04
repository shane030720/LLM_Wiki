---
title: TCP Reset Segment
category: concept
tags: [tcp, reset, rst, connection, abort]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP에서 참조 연결(reference connection)에 올바르지 않은 세그먼트가 도착했을 때 전송되는 특수 제어 세그먼트. RST 플래그가 설정되며, 수신 시 연결의 빠른 해제(fast teardown)를 유발한다.

## How It Works

RST는 TCP 헤더의 RST(Reset) 비트를 설정하여 전송된다. 수신 측은 RST를 받으면 즉시 연결을 종료하고 CLOSED 상태로 전이한다.

**발생 케이스**

**Case 1: 존재하지 않는 포트로의 연결 요청**

- 목적지 포트에서 수신 대기 중인 프로세스가 없을 때 SYN이 도착하면 RST로 응답
- UDP의 경우 ICMP Destination Unreachable (Port Unreachable)을 사용하지만, TCP는 RST를 사용
- 클라이언트는 "Connection refused" 오류를 즉시 수신

```
Linux% telnet localhost 9999
Trying 127.0.0.1...
telnet: connect to address 127.0.0.1: Connection refused
```

**Case 2: 연결 중단 (Abortive Release)**

- 정상적인 종료(orderly release)는 FIN 사용
- RST를 통한 강제 중단(abortive release)도 가능
- Abortive release의 특성:
  1. 큐에 대기 중인 모든 데이터를 폐기하고 즉시 RST 전송
  2. 수신 측은 상대방이 정상 종료 대신 중단을 수행했음을 인식 가능
- Berkeley Sockets API에서 `SO_LINGER` 소켓 옵션의 linger 값을 0으로 설정하여 구현

**Case 3: Half-Open 연결**

- 한쪽 엔드포인트가 다운(크래시 또는 전원 차단)된 상태에서 다른 쪽이 이를 모르고 있는 상황
- 살아있는 쪽이 데이터를 보내면, 재부팅한 상대방은 해당 연결에 대한 정보가 없어 RST로 응답
- 많은 half-open TCP 연결이 서버 호스트에 누적될 수 있음

**Case 4: TIME_WAIT Assassination (TWA) — RFC 1337**

- TIME_WAIT 상태의 클라이언트에게 오래된 세그먼트가 도착하면 TCP는 현재 시퀀스 번호로 ACK 응답
- 서버는 이 ACK를 해당 연결에 대한 정보 없이 수신하므로 RST로 응답
- 이 RST가 클라이언트를 TIME_WAIT → CLOSED로 조기 전이시킴
- 대부분의 시스템은 TIME_WAIT 상태에서 RST 세그먼트를 무시함으로써 해결

## Key Properties

- RST는 정상 FIN-기반 종료와 달리 즉각적이며 데이터 손실을 수반할 수 있음
- RST 수신 시 TCP는 빠른 연결 해제를 수행하고 앱에 오류를 알림
- RST를 이용하면 전통적인 4-way handshake 없이 연결을 즉시 종료 가능
- 위조된 RST 세그먼트를 이용한 TCP 연결 방해 공격이 가능 (유효한 시퀀스 번호만 있으면 됨)
- BGP 등 장기 TCP 세션 보호를 위해 TCP-AO(Authentication Option) 사용 (이전에는 TCP-MD5, RFC 2385)

## Relationships

- [[tcp-three-way-handshake]] (연결 수립 실패 또는 비정상 종료 시 RST가 사용되는 맥락)
- [[tcp-state-machine]] (RST 수신 시 즉시 CLOSED 상태로 전이)
- [[time-wait-state]] (TIME_WAIT Assassination이 RST로 인해 발생)
- [[initial-sequence-number]] (RST 위조 공격이 유효한 시퀀스 번호를 필요로 함)
- [[tcp]] (TCP 오류 처리 메커니즘)

## Open Questions

- 방화벽이 RST 세그먼트를 위조하여 연결을 강제 종료하는 "TCP RST injection" 공격을 탐지하는 효과적인 방법은?
- TCP-AO가 RST 위조를 방지하더라도, 합법적인 연결 재설정 메시지를 어떻게 인증하는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 49–54)
