---
title: TCP Timestamps Option and PAWS
category: concept
tags: [tcp, timestamps, rtt, paws, options, sequence-number]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

각 TCP 세그먼트에 타임스탬프 값을 포함시키는 옵션(RFC 1323). 두 가지 목적으로 사용된다: (1) RTT의 정밀한 측정, (2) 래핑된 시퀀스 번호로부터 보호(Protection Against Wrapped Sequence Numbers, PAWS).

## How It Works

**Timestamps 옵션 구조**

10바이트 옵션:
- **TSV (Timestamp Value)**: 4바이트, 송신자가 현재 타임스탬프를 설정
- **TSER (Timestamp Echo Reply)**: 4바이트, 수신자가 받은 TSV를 에코

수신자는 TSV 값의 의미나 단위를 해석할 필요 없이 단순히 에코한다. RFC 1323 권고사항: 송신자는 최소 1초마다 TSV를 1 이상 증가시켜야 함.

**RTT 측정**

- 송신자는 세그먼트 전송 시 TSV에 현재 시각 설정
- 수신자가 ACK에 TSER로 에코 반환
- 송신자는 ACK 수신 시각 − TSV = RTT 추정
- TSOPT 이전에는 윈도우당 한 번의 RTT 샘플 획득이 일반적이었으나, TSOPT로 ACK당 샘플 획득 가능 → 더 정확한 재전송 타임아웃(RTO) 계산
- 참고: RFC 1323, RFC 6298

**PAWS (Protection Against Wrapped Sequence Numbers)**

32비트 시퀀스 번호는 고속 네트워크에서 동일 연결 내에서도 재사용(wraparound)될 수 있다. 예를 들어 1GiB 수신 윈도우에서 시퀀스 D가 시퀀스 E와 동일한 번호로 재사용될 수 있다.

PAWS 알고리즘:
- Timestamps 옵션이 32비트 추가 시퀀스 번호 공간으로 기능
- 수신자는 TSV 값이 단조 증가하지 않으면 오래된 세그먼트로 판단하고 폐기
- 창 전송마다 TSV가 1씩 증가한다면, 같은 시퀀스 번호 D와 E를 가진 세그먼트도 TSV 값으로 구분 가능

**Timestamps 옵션과 SACK의 공존**

Timestamps 옵션(10바이트)과 SACK를 함께 사용하면 TCP 헤더의 Options 필드 공간이 제한되어 SACK 블록 수가 최대 3개로 줄어든다.

## Key Properties

- TSV와 TSER 각각 4바이트, 옵션 전체 10바이트
- RTT 측정의 정밀도를 윈도우당 → ACK당 수준으로 향상
- PAWS는 시퀀스 번호 공간이 재사용되어도 오래된 세그먼트를 식별 가능하게 함
- RFC 1323에서 [[tcp-window-scale]]과 함께 정의
- 모든 SYN 세그먼트부터 옵션을 포함해야 하며, 연결 중간에 활성화 불가

## Relationships

- [[tcp-window-scale]] (같은 RFC 1323에서 정의된 관련 옵션)
- [[initial-sequence-number]] (PAWS가 해결하는 시퀀스 번호 재사용 문제)
- [[selective-acknowledgment]] (SACK와 함께 사용 시 헤더 공간 제약)
- [[tcp-three-way-handshake]] (SYN/SYN+ACK에서 Timestamps 옵션이 교환되는 시점)
- [[tcp]] (RTO 계산을 통한 재전송 메커니즘)

## Open Questions

- PAWS는 TSV 값의 단조 증가를 가정하는데, 시스템 재부팅이나 타임스탬프 오버플로우 시 어떻게 처리되는가?
- 송신자와 수신자의 TSV 증가 속도가 다를 때 RTT 계산에 어떤 영향이 있는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 34–37)
