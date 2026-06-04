---
title: TCP Timers
category: concept
tags: [tcp, timer, network, flow-control]
sources: [raw/컴퓨터네트워크/Week 07 TCP Congestion Control.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP는 연결 관리와 신뢰성 있는 데이터 전송을 위해 네 가지 타이머를 사용한다: Retransmission Timer, Persistence Timer, Keepalive Timer, TIME-WAIT Timer. 각 타이머는 서로 다른 비정상 상태(deadlock, idle connection, ACK 손실 등)를 감지하고 복구하는 역할을 한다.

## How It Works

### Retransmission Timer (재전송 타이머)

패킷 손실을 감지하고 재전송을 트리거하는 타이머. 상세 내용은 [[tcp-retransmission-timeout]] 참조.

### Persistence Timer (영속 타이머)

**문제 배경 (교착 상태, Deadlock):**
- TCP flow control에서 수신자는 수신 윈도우 크기(rwnd)를 광고하고, 송신자는 이를 초과하지 않도록 전송을 제한
- 수신자가 rwnd = 0을 광고하면 송신자는 더 이상 데이터를 전송할 수 없음
- 수신자의 버퍼가 비워지면 rwnd > 0인 ACK를 전송해 송신자를 깨워야 하는데, 이 ACK가 손실되면?
- ACK에는 별도의 재전송 메커니즘이 없으므로, 송신자와 수신자 모두 상대방의 행동을 기다리는 교착 상태(deadlock)에 빠짐

**동작 메커니즘:**
1. 송신 TCP가 rwnd = 0인 ACK를 수신하면 Persistence Timer를 시작
2. 타이머 만료 시, 송신자는 **probe segment** (탐색 세그먼트)를 전송
   - 1바이트의 새로운 데이터를 포함
   - 시퀀스 번호를 가지지만, 해당 번호는 ACK되지 않으며 나머지 데이터의 시퀀스 번호 계산에도 반영되지 않음
   - 수신 TCP가 이 probe에 응답하여 현재 rwnd 값이 포함된 ACK를 재전송하도록 유도
3. Persistence Timer의 초기값은 Retransmission Timeout(RTO) 값으로 설정
4. 응답이 없으면 probe를 재전송하며 타이머 값을 두 배로 증가 (지수 백오프)
5. 타이머 값이 임계치(보통 60초)에 도달하면, 그 이후부터는 60초마다 한 번씩 probe를 전송하여 윈도우가 재개방될 때까지 반복

### Keepalive Timer (킵얼라이브 타이머)

**목적:** 오랫동안 유휴 상태인 TCP 연결이 실제로 살아있는지 확인하여 죽은 연결(dead connection)을 식별하고 시스템 자원 낭비를 방지

**동작 메커니즘:**
1. 서버가 클라이언트로부터 2시간 동안 아무 세그먼트도 수신하지 못하면 probe segment를 전송
2. 응답이 없으면 75초 간격으로 최대 10번의 probe를 추가 전송
3. 10번의 probe에도 응답이 없으면 연결을 종료(terminate)

### TIME-WAIT Timer (2MSL Timer)

Active close를 수행한 엔드포인트가 TIME_WAIT 상태에서 유지하는 타이머. 값은 2 × MSL(Maximum Segment Lifetime). 상세 내용은 [[time-wait-state]] 참조.

**역할:**
- 최종 ACK가 손실된 경우 상대방이 timeout 후 FIN을 재전송할 때 ACK를 재전송할 수 있도록 보장
- 네트워크에 잔존하는 오래된 세그먼트가 새로운 연결에 영향을 주지 않도록 방지

## Key Properties

- **Persistence Timer**: rwnd = 0 교착 상태를 해결하기 위한 probe 메커니즘; 지수 백오프 적용, 최대 60초 간격으로 제한
- Persistence Timer의 probe segment는 시퀀스 번호 공간에 영향을 주지 않는 특수 세그먼트
- **Keepalive Timer**: 2시간 유휴 후 활성화; 75초 간격 10회 probe 후 무응답 시 연결 종료
- **TIME-WAIT Timer**: 2 × MSL 유지; 최종 ACK 재전송 가능성 보장
- 네 가지 타이머는 각각 독립적인 비정상 시나리오를 담당하며 상호 보완적으로 동작

## Relationships

- [[tcp-retransmission-timeout]] — Persistence Timer의 초기값 기준이 되며, 재전송 타이머의 상세 동작을 다룸
- [[tcp-flow-control]] — Persistence Timer가 해결하는 rwnd = 0 교착 상태의 발생 맥락
- [[time-wait-state]] — TIME-WAIT Timer(2MSL Timer)의 상세 동작과 목적
- [[tcp-state-machine]] — 각 타이머가 동작하는 TCP 상태 전이 맥락
- [[tcp]] — 네 가지 타이머가 모두 속한 전송 계층 프로토콜

## Open Questions

- Keepalive Timer의 2시간 유휴 임계값은 현대 애플리케이션 환경에서 적절한가? 모바일·클라우드 환경에서는 더 짧은 값이 실용적이지 않은가?
- Persistence Timer의 probe가 시퀀스 번호 공간에 영향을 주지 않는 설계 결정이 구현 복잡성에 어떤 영향을 미치는가?

## Sources

- raw/컴퓨터네트워크/Week 07 TCP Congestion Control.pdf
