---
title: Selective Acknowledgment (SACK)
category: concept
tags: [tcp, sack, acknowledgment, retransmission, options]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP 수신자가 연속적이지 않게(out-of-sequence) 수신된 데이터 블록의 범위를 송신자에게 알려, 송신자가 실제로 유실된 세그먼트만 선택적으로 재전송할 수 있게 하는 TCP 옵션 쌍.

## How It Works

**배경: 누적 ACK의 한계**

TCP는 기본적으로 누적 ACK(cumulative ACK)를 사용한다. 수신자는 연속적으로 받은 데이터의 다음 바이트만 ACK할 수 있으므로, 중간 세그먼트 유실 시 이미 올바르게 받은 이후 세그먼트들을 재전송해야 하는 비효율이 발생한다. 이를 수신 데이터 큐의 "홀(hole)"이라 한다.

**SACK의 동작 방식**

1. **SACK-Permitted 옵션**: 연결 수립 시 SYN (또는 SYN+ACK) 세그먼트에 포함. 피어가 SACK 정보를 광고할 능력이 있음을 알림. 양쪽 모두 이 옵션을 교환해야 SACK 활성화.

2. **SACK 옵션**: 순서가 어긋난 데이터를 수신했을 때, 수신자가 이미 받은 데이터 블록의 범위(시퀀스 번호 범위)를 ACK 세그먼트에 포함하여 전송.

**SACK 블록 형식**

- 각 SACK 블록 = 32비트 시작 시퀀스 번호 + 32비트 종료 시퀀스 번호 = 8바이트
- n개의 SACK 블록을 포함한 옵션 = **(8n + 2)바이트** (kind 1바이트 + length 1바이트 + 블록 데이터)
- Timestamps 옵션도 함께 사용하는 현대 TCP에서는 **n ≤ 3** (헤더 공간 제한)

**세그먼트 중복 수신 (D-SACK)**

세그먼트가 중복 수신된 경우, 중복 블록을 SACK 목록의 첫 번째에 배치하여 송신자에게 알린다.

**일반적인 SACK 동작 예시**

- 세그먼트 1, 3, 4가 도착하고 2가 유실된 경우:
  - ACK = 2번째 세그먼트 시작 시퀀스 번호 (누적 ACK)
  - SACK 블록 = [3번째 시작, 4번째 종료] (이미 받은 범위)
  - 송신자는 2번 세그먼트만 선택적으로 재전송

## Key Properties

- SACK는 두 개의 옵션으로 구성: SACK-Permitted(능력 광고)와 SACK(실제 블록 정보)
- SACK-Permitted는 SYN/SYN+ACK에서만 교환
- SACK 옵션은 데이터 전송 중 언제든 포함 가능
- 누적 ACK보다 네트워크 효율적 — 실제 유실된 세그먼트만 재전송
- 현대 TCP 구현에서 SACK는 사실상 표준 기능으로 활성화

## Relationships

- [[tcp-three-way-handshake]] (SACK-Permitted 옵션이 SYN/SYN+ACK에서 교환되는 시점)
- [[tcp-header]] (SACK 옵션이 위치하는 TCP 헤더 Options 필드)
- [[tcp-timestamps]] (SACK와 함께 사용 시 가능한 SACK 블록 수가 제한됨)
- [[tcp]] (재전송 메커니즘 전반)

## Open Questions

- SACK 정보를 이용한 reordering 공격(송신자가 실제로 필요하지 않은 세그먼트를 재전송하도록 유도)이 가능한가?
- D-SACK를 통해 중복 수신을 감지하면 송신자의 congestion control 알고리즘(예: CUBIC, BBR)은 어떻게 반응해야 하는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 30–32)
