---
title: IPv4 Options
category: concept
tags: [ip, ipv4, options, record-route, source-route, timestamp, network-layer]
sources: [raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

IPv4 Options는 IPv4 헤더의 선택적(optional) 필드로, 데이터그램 단위로 특수 처리를 지정할 수 있게 하는 확장 메커니즘이다. 가변 길이(최대 40바이트)이며 32비트 경계를 맞추기 위해 NOP(No Operation)와 EOP(End of Option) 패딩 옵션을 사용한다. 현재는 대부분의 표준화된 옵션이 거의 사용되지 않으며, 기업 네트워크 방화벽에서 일반적으로 차단 또는 제거된다.

## How It Works

### 옵션 포맷

멀티바이트 옵션의 공통 구조:

```
[Type: 8bits][Length: 8bits][Value: variable]
```

**Type 필드 구성 (8비트):**
- **Copy 비트 (1비트)**: 0=단편화 시 첫 번째 단편에만 복사, 1=모든 단편에 복사
- **Class (2비트)**: `00`=데이터그램 제어, `01`=예약, `10`=디버깅·관리, `11`=예약
- **Number (5비트)**: 옵션 종류 식별

### 주요 옵션 유형

**단일 바이트 옵션:**
- **EOP — End of Option** (Number=`00000`): 옵션 목록 종료 마커
- **NOP — No Operation** (Number=`00001`): 정렬 패딩용

**멀티바이트 옵션:**

**1. Record Route Option** (Number=`00111`)
- 패킷이 통과하는 각 라우터의 IP 주소를 헤더 내 미리 할당된 공간에 순서대로 기록
- IP Options 필드 최대 40바이트 → 최대 9개 IP 주소만 저장 가능
- 평균 인터넷 라우터 홉 수 약 15에 비해 저장 한계가 작아 실용성 제한적
- 주의: `traceroute`는 이 옵션을 사용하지 않음 — 소스가 기록된 경로 정보를 목적지의 도움 없이 알 방법이 없기 때문

**2. Strict Source Route Option** (Number=`01001`)
- 소스가 지정한 게이트웨이 목록을 정확히·순서대로 모두 방문해야 함
- 목록에 없는 라우터 경유 불허

**3. Loose Source Route Option** (Number=`00011`)
- 목록에 지정된 라우터는 반드시 방문해야 하지만, 중간에 명시되지 않은 다른 라우터도 경유 가능

**4. Timestamp Option** (Number=`00100`)
- 라우터가 데이터그램 처리 시각(자정 UTC 기준 밀리초 단위)을 기록
- **Overflow 필드**: 공간 부족으로 타임스탬프를 추가하지 못한 라우터 수 기록
- **Flag 값에 따른 동작:**

| Flag | 동작 |
|------|------|
| 0 | 각 라우터가 타임스탬프만 제공된 필드에 추가 |
| 1 | 각 라우터가 자신의 outgoing IP 주소 + 타임스탬프를 함께 기록 |
| 3 | 소스가 IP 주소를 미리 지정; 라우터는 자신의 incoming 주소와 일치하면 outgoing 주소로 교체 후 타임스탬프 추가 |

### Source Route Option의 활용 목적

- 특정 ToS(최소 지연, 최대 처리량)를 가진 경로 선택
- 더 안전하거나 신뢰할 수 있는 경로 강제 지정
- 그러나 소스 라우팅 기반 보안 공격(소스 IP 스푸핑과 결합) 위험으로 현재 대부분 비활성화됨

### 옵션 처리 흐름

라우터는 IP Options 필드를 파싱하여 자신이 처리해야 하는 옵션을 수행한다. Copy 비트에 따라 단편화 시 옵션 복사 여부가 결정된다.

## Key Properties

- IP Options 필드는 최대 40바이트; 기본 헤더 20바이트 + 옵션 최대 40바이트 = IHL 최대 60바이트
- 현재 표준화된 옵션 대부분이 실제로는 거의 사용되지 않음
- 기업 네트워크 방화벽에서 옵션 포함 패킷은 일반적으로 차단 또는 Options 필드 제거 후 포워딩
- IANA에 옵션 목록 등록: https://www.iana.org/assignments/ip-parameters/ip-parameters.xhtml
- IPv6는 Options 필드 대신 Next Header 필드로 연결되는 확장 헤더(Extension Header) 체인 방식 사용

## Relationships

- [[ipv4-datagram]] — Options 필드가 포함된 IPv4 헤더; IHL 필드가 Options 포함 실제 헤더 크기를 지시
- [[ipv4-fragmentation]] — Copy 비트가 단편화 시 각 옵션의 전파 방식을 제어
- [[network-layer]] — 옵션이 처리되는 계층

## Open Questions

- Source Route Option이 현재도 소스 IP 스푸핑 공격과 결합될 경우 구체적으로 어떤 위협이 발생하는가?
- Record Route Option의 현대적 유용성 — Goodchild et al. (ACM IMC 2017, "The Record Route Option is an Option!")의 주장은 어떤 환경에서 타당한가?
- IPv6 확장 헤더 방식이 IPv4 Options 방식보다 라우터 처리 효율 면에서 실제로 더 우수한가?

## Sources

- raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf
