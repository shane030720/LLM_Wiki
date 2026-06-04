---
title: Initial Sequence Number (ISN)
category: concept
tags: [tcp, sequence-number, security, isn, randomness]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP 연결을 시작할 때 각 엔드포인트가 자신의 SYN 세그먼트에 포함시켜 전송하는 초기 시퀀스 번호(Initial Sequence Number). 동일한 4-tuple로 생성된 서로 다른 연결(incarnation) 간의 시퀀스 번호 중복을 방지하고, 세그먼트 위조 공격을 어렵게 만들기 위해 신중하게 선택되어야 한다.

## How It Works

**RFC 0793의 원래 명세**

- ISN은 4μs마다 1씩 증가하는 32비트 카운터로 정의
- 목적: 동일 4-tuple의 서로 다른 연결 인스턴스(incarnation) 간에 시퀀스 번호가 겹치지 않도록 보장

**현대적 ISN 선택 방식 (준무작위 방식)**

보안 취약점 때문에 현대 시스템은 예측 불가능한 ISN을 생성한다:

**Linux의 ISN 생성 과정**:
1. 클록 기반 스킴을 사용하되, 각 연결에 대해 무작위 오프셋으로 시작
2. 무작위 오프셋 = 연결 식별자(4-tuple)에 대한 **암호학적 해시 함수** 출력값
3. 해시 함수의 비밀 입력값은 5분마다 변경
4. 32비트 ISN 구성: 상위 8비트 = 비밀값의 시퀀스 번호, 나머지 24비트 = 해시 출력
5. 결과: 예측이 어렵지만 시간에 따라 단조 증가

**Windows**의 경우 RC4 기반 유사 방식을 사용한다고 알려져 있다.

최신 명세는 RFC 6528 및 RFC 9293 Section 3.4.1 참조.

**ISN 위조 공격 (Forging ISN)**

유효한 TCP 세그먼트를 위조하기 위해 필요한 정보:
1. 연결 4-tuple (로컬/원격 IP 주소와 포트 번호)
2. 현재 수신 윈도우 내의 유효한 시퀀스 번호

위의 두 정보만 있으면 누구든 TCP 세그먼트를 위조하여 연결을 방해할 수 있다 (RFC 5961). 방어 방법:
- ISN 예측 어렵게 만들기 (현대 구현의 기본 접근)
- 임시 포트 번호를 무작위화 (RFC 6056)
- 암호화 (TLS 등)

**시퀀스 번호 랩어라운드 문제**

시퀀스 번호 필드는 32비트이므로 매우 높은 전송 속도에서 동일 연결 내에서도 시퀀스 번호가 재사용될 수 있다. 이 문제는 [[tcp-timestamps]] (PAWS 알고리즘)로 해결된다.

## Key Properties

- ISN은 연결별로 달라야 하며, 동일 4-tuple의 이전 연결과 겹쳐서는 안 됨
- 오래된 지연 세그먼트가 새 연결에서 유효한 것으로 잘못 수락되는 것을 방지하는 것이 핵심 목적
- 현대 구현은 암호학적 해시를 이용해 예측 어렵고(security) 단조 증가(correctness)를 모두 달성
- 관련 보안 권고: CERT Advisory CA-2001-09

## Relationships

- [[tcp-three-way-handshake]] (ISN이 SYN 세그먼트에 포함되어 교환되는 과정)
- [[tcp-timestamps]] (시퀀스 번호 랩어라운드를 PAWS로 방어하는 메커니즘)
- [[tcp]] (ISN이 TCP의 신뢰성 있는 전송을 지원하는 방식)

## Open Questions

- RFC 6528의 ISN 생성 방식이 타이밍 사이드채널 공격에 취약할 수 있는가?
- 5분마다 비밀값이 바뀌는 Linux 방식에서, 비밀값 교체 직전/직후에 생성된 ISN 간의 예측 가능성 갭이 존재하는가?
- 시퀀스 번호 공간이 32비트인데, 400Gbps 이상 네트워크에서 랩어라운드 문제를 PAWS만으로 완전히 해결할 수 있는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (pp. 15–18)
