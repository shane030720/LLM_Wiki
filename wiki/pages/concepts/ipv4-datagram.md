---
title: IPv4 Datagram
category: concept
tags: [ip, ipv4, header, datagram, network-layer, ttl, checksum, protocol]
sources: [raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

IPv4 Datagram은 인터넷 프로토콜 버전 4 [RFC 791]에서 정의된 네트워크 계층의 프로토콜 데이터 단위(PDU)로, 20~60바이트의 헤더와 가변 길이 페이로드로 구성된다. 비신뢰적(unreliable), 비연결형(connectionless) 방식으로 전달되며, 각 데이터그램은 독립적으로 처리된다. 최대 크기는 65,535바이트이고, 헤더는 32비트 경계를 기준으로 구조화된다.

## How It Works

### 헤더 필드 구성 (20바이트 기본 헤더)

| 필드 | 크기 | 설명 |
|------|------|------|
| Version | 4 bits | IP 버전 번호 (4 또는 6); IPv4와 IPv6는 상호운용 불가 |
| IHL (Internet Header Length) | 4 bits | 헤더 크기를 32비트 워드 단위로 표현; 최대 15×4=60바이트 |
| ToS / DSCP+ECN | 8 bits | 원래 Type of Service; 현재는 6비트 DSCP + 2비트 ECN으로 재정의 |
| Total Length | 16 bits | 헤더 포함 전체 데이터그램 크기; 최대 65,535바이트 |
| Identification | 16 bits | 데이터그램 식별자; 단편화·재조립에만 사용 [RFC6864] |
| Flags | 3 bits | Reserved·DF(Don't Fragment)·MF(More Fragments) |
| Fragment Offset | 13 bits | 원본 데이터그램 내 조각 위치; 8바이트 단위 |
| TTL (Time-to-Live) | 8 bits | 최대 라우터 홉 수; 매 라우터마다 1 감소, 0이면 폐기 |
| Protocol | 8 bits | 페이로드 프로토콜 유형 (TCP=6, UDP=17 등) |
| Header Checksum | 16 bits | 헤더 전용 오류 검사 |
| Source Address | 32 bits | 발신지 IPv4 주소 |
| Destination Address | 32 bits | 목적지 IPv4 주소 |
| Options | 가변 | 선택적 기능; 32비트 경계 맞춤 (NOP/EOP 패딩 사용) |

### 주요 필드 상세

**ToS / DSCP (RFC 2474, RFC 8436):**
- 3개 우측 비트가 모두 0이면: 좌측 3비트 = 기존 Precedence 비트 (하위 호환)
- 3개 우측 비트 중 하나라도 1이면: 6비트 전체로 56가지 차등 서비스 정의

**Total Length 관련 제약:**
- 페이로드 길이 = Total Length - (IHL × 4)
- 호스트는 576바이트 이상의 데이터그램을 수신할 의무 없음 [RFC791] (1980년대 16비트 CPU 메모리 구조에서 유래)
- 이 때문에 UDP 기반 IETF 프로토콜 다수가 페이로드를 512바이트로 제한

**TTL 동작:**
- [RFC1122]는 기본값 64 권장 (일부 구현은 128·255 사용)
- TTL=0 도달 시 데이터그램 폐기, ICMP 메시지로 송신자에 통보
- 목적: 라우팅 루프로 인한 패킷 무한 순환 방지

**Protocol 필드와 역다중화:**
- IP 데이터그램이 다른 프로토콜의 PDU를 페이로드로 전달할 때, Protocol 필드로 상위 계층 프로토콜을 식별
- IP가 단일 하위 프로토콜이 아닌 다수 상위 프로토콜을 동시에 지원하는 역다중화(demultiplexing) 기능 제공

**Header Checksum:**
- IPv4 헤더만을 대상으로 계산 (페이로드 미포함)
- IPv6에서는 이 필드가 제거됨 (유선망에서 비트 오류가 드물고, 상위 계층에서 더 강력한 검사 제공)

### IPv4 vs IPv6 비교

| 항목 | IPv4 | IPv6 |
|------|------|------|
| 주소 크기 | 32 bits | 128 bits (4배) |
| 헤더 크기 | 가변 20~60B | 고정 40B |
| 체크섬 | 있음 | 없음 |
| 단편화 주체 | 라우터·호스트 모두 | 종단 호스트만 (확장 헤더 활용) |
| 페이로드 길이 필드 | 없음 (Total Length에서 계산) | 있음 (Payload Length) |
| Options 처리 | 헤더 내 가변 길이 | Next Header 필드로 연결되는 확장 헤더 체인 |

### IPv6 주소 표기 규칙 [RFC4291]
- 128비트를 16진수 블록 8개로 표현, 콜론(:)으로 구분
- 선행 0 생략 가능: `0058` → `58`
- 연속된 0 블록은 `::` 로 한 번만 축약 가능: `::1` (루프백), `2001:db8::2`
- 포트 번호와 구분하기 위해 대괄호 사용: `http://[2001:db8::2]:443/`

## Key Properties

- IP는 각 데이터그램을 독립적으로 처리 (연결 상태 정보 없음)
- 전달 보장 없음; 필요한 신뢰성은 상위 계층이 제공
- Protocol 필드로 TCP·UDP·ICMP 등 다양한 상위 프로토콜을 동시에 지원
- IPv6는 고정 헤더 40B로 라우터 처리 단순화; 확장 헤더로 옵션 기능 제공
- Hop-by-hop Options 확장 헤더는 경로상 모든 장치가 처리해야 함

## Relationships

- [[network-layer]] — IPv4 데이터그램이 속하는 계층; best-effort 서비스 모델의 구현체
- [[ipv4-fragmentation]] — Identification·Flags·Fragment Offset 필드를 활용한 단편화·재조립 메커니즘
- [[ipv4-options]] — 헤더의 Options 필드에 담기는 선택적 기능들
- [[classful-addressing]] — IPv4 주소 공간의 역사적 분류 체계
- [[subnet-addressing]] — 서브넷 마스크를 활용한 IPv4 주소 계층 구조
- [[network-addressing]] — MAC·IP·Port 주소 체계 전반의 개요
- [[tcp]] — Protocol 필드값 6; TCP 세그먼트를 페이로드로 전달
- [[path-mtu-discovery]] — DF 비트와 ICMP를 활용하여 경로 MTU를 발견하는 메커니즘
- [[tcp-congestion-control]] — ECN 필드(ToS 하위 2비트)를 통해 네트워크 혼잡 신호를 전달

## Open Questions

- IPv6 헤더에서 체크섬 제거가 실제로 안전한가? 무선망·광학망에서의 비트 오류율 수준은?
- DSCP/ECN 기반 QoS가 엣지에서는 작동해도 인터넷 코어를 통과하며 신호가 유지되는가?
- 576바이트 수신 의무 한계가 현재도 구현 수준에서 어떤 영향을 미치는가?

## Sources

- raw/컴퓨터네트워크/Week 09 Internet Protocol (1).pdf
