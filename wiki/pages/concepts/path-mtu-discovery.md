---
title: Path MTU Discovery (PMTUD)
category: concept
tags: [tcp, mtu, pmtud, icmp, fragmentation, smss]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

두 호스트 간의 경로(path) 상에서 가장 작은 MTU(Path MTU)를 발견하여 IP 단편화(fragmentation)를 피하기 위한 메커니즘. TCP는 전송할 세그먼트 크기를 스스로 결정할 수 있어 PMTUD를 효과적으로 활용할 수 있다.

## How It Works

**기본 원리**

Path MTU = 현재 경로의 모든 네트워크 세그먼트 중 최소 MTU 값. PMTUD는 이 값을 동적으로 탐색한다.

**TCP의 표준 PMTUD 절차 (RFC 1191, RFC 1981)**

1. **초기 SMSS 결정**: 송신 최대 세그먼트 크기(SMSS)는 다음 중 작은 값으로 결정:
   - 송신자의 발신 링크 MTU
   - 상대방이 광고한 MSS

2. **DF 비트 설정**: TCP가 생성하는 모든 IPv4 데이터그램에 **Don't Fragment(DF) 비트**를 설정. IP 레이어가 데이터그램을 분할하지 않도록 강제.

3. **PTB 수신 및 크기 조정**: 경로 상의 라우터가 패킷을 처리할 수 없을 만큼 크면, ICMP **Packet Too Big(PTB)** 메시지를 송신자에게 반환. TCP는 PTB를 수신하면:
   - 세그먼트 크기를 감소시킴 (일반적으로 next-hop MTU − IP 헤더 − TCP 헤더)
   - 줄어든 크기로 재전송

4. **주기적 크기 증가 시도**: 라우팅 경로는 동적으로 변할 수 있으므로, 마지막 크기 감소 이후 일정 시간(RFC 1191/1981 권고: 10분)이 지나면 더 큰 크기(초기 SMSS까지)를 다시 시도.

**대안: PLPMTUD (Packetization Layer Path MTU Discovery, RFC 4821)**

ICMP를 사용하지 않고 패킷화 계층(TCP 또는 다른 전송 프로토콜)에서 PMTUD를 수행하는 방법. ICMP 차단 방화벽 환경에서 유용하나, 이 강의에서는 상세 설명을 생략.

## Key Properties

- TCP는 바이트 스트림 추상화를 구현하며 세그먼트 크기를 직접 제어하므로, UDP보다 PMTUD 활용에 유리
- DF 비트 설정이 PMTUD의 핵심: 라우터가 분할할 수 없어 PTB를 반환하도록 강제
- ICMP PTB 메시지가 방화벽에 의해 차단되면 PMTUD가 실패("Black Hole" 문제)
- 경로 변경 후 10분 주기로 더 큰 크기를 재시도하여 최적 SMSS를 유지
- IPv4는 RFC 1191, IPv6는 RFC 1981 참조

## Relationships

- [[maximum-segment-size]] (SMSS 결정에 사용되는 MSS 옵션과의 관계)
- [[tcp]] (PMTUD가 TCP 세그멘테이션 크기 결정에 사용되는 맥락)
- [[network-protocol]] (ICMP PTB 메시지를 통한 피드백 메커니즘)
- [[tcp-three-way-handshake]] (초기 SMSS가 MSS 옵션 교환을 통해 결정되는 시점)

## Open Questions

- ICMP 차단 방화벽이 일반화된 환경에서 표준 PMTUD의 신뢰성이 낮은데, PLPMTUD가 이를 완전히 대체할 수 있는가?
- 경로 MTU가 빈번하게 변경되는 SD-WAN 또는 ECMP 환경에서 PMTUD의 10분 재시도 주기는 적절한가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 40–41)
