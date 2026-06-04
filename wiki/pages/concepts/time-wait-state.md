---
title: TIME_WAIT State (2MSL Wait)
category: concept
tags: [tcp, connection, state, timewait, 2msl, socket]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP active close를 수행한 엔드포인트가 최종 ACK를 전송한 후 2×MSL(Maximum Segment Lifetime) 시간 동안 머무르는 상태. TIME_WAIT 상태 동안 해당 연결의 4-tuple은 재사용될 수 없다.

## How It Works

**MSL (Maximum Segment Lifetime)**

네트워크에서 어떤 세그먼트가 폐기되기 전까지 존재할 수 있는 최대 시간:
- RFC 793 명세: 2분
- 실제 운영: 30초, 1분, 2분이 일반적으로 사용됨
- Linux 설정: `net.ipv4.tcp_fin_timeout` (초 단위)

**TIME_WAIT 진입 조건**

Active close(먼저 FIN을 보낸 쪽)가 상대방의 FIN+ACK에 대한 최종 ACK를 전송한 후 TIME_WAIT로 전이한다.

**TIME_WAIT의 목적**

1. **최종 ACK 유실 대비**: 최종 ACK가 유실되면 상대방이 FIN을 재전송하고, TIME_WAIT 상태에서 이를 수신하여 ACK를 재전송할 수 있다.
2. **오래된 세그먼트 격리**: 동일 4-tuple로 새 연결이 시작되더라도 이전 연결의 지연 세그먼트가 새 연결에서 유효한 것으로 수락되지 않도록 보장한다.

**포트 재사용 문제**

- TIME_WAIT 동안 해당 4-tuple은 재사용 불가
- **클라이언트**: 일반적으로 임시 포트(ephemeral port)를 사용하므로 큰 문제 없음
- **서버**: well-known 포트를 사용하므로 서버 프로세스를 종료하고 즉시 재시작하면 최대 4분간 "Address already in use" 오류 발생

**우회 방법**

- `SO_REUSEADDR` 소켓 옵션: 특정 TCP 소켓에 대해 이 제한을 우회할 수 있으나, TCP 자체는 여전히 해당 포트의 TIME_WAIT 연결 재사용을 방지

**TIME_WAIT Assassination (TWA)**

RFC 1337에서 정의된 문제:
- TIME_WAIT 상태에서 이전 연결의 오래된 세그먼트가 도착하면 TCP가 현재 시퀀스 번호로 ACK를 응답
- 서버는 이 ACK를 받으면 RST로 응답하여, 클라이언트가 TIME_WAIT에서 CLOSED로 조기 전이
- 대부분의 시스템은 **TIME_WAIT 상태에서 RST 세그먼트를 무시**하여 이 문제를 해결

## Key Properties

- TIME_WAIT는 active close를 수행한 엔드포인트에만 적용됨 (passive close 쪽은 LAST_ACK → CLOSED)
- 지속 시간: 2×MSL (최대 4분)
- 대규모 서버 환경에서 TIME_WAIT 상태의 연결이 다수 누적될 수 있음
- TIME_WAIT 동안 해당 4-tuple로 수신된 데이터는 폐기

## Relationships

- [[tcp-state-machine]] (TIME_WAIT가 TCP FSM에서 차지하는 위치)
- [[tcp-three-way-handshake]] (연결 종료 절차에서 TIME_WAIT 발생 맥락)
- [[tcp-reset-segment]] (TIME_WAIT Assassination은 RST 세그먼트로 인해 발생)
- [[initial-sequence-number]] (TIME_WAIT가 방지하고자 하는 이전 연결의 지연 세그먼트 문제)

## Open Questions

- 고속 서버 환경에서 TIME_WAIT 상태가 대량 누적될 때(`net.ipv4.tcp_tw_reuse` 같은 커널 파라미터를 통해) 안전하게 재사용하는 조건은 무엇인가?
- TIME_WAIT Assassination을 방지하기 위해 RST를 무시하는 방식이 진짜 RST(연결 리셋 필요 상황)도 무시할 가능성이 있는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 47, 54)
