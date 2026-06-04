---
title: TCP Window Scale Option (WSCALE)
category: concept
tags: [tcp, window, flow-control, options, bandwidth-delay-product, performance]
sources: [raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition

TCP의 수신 윈도우(receive window) 광고 크기를 16비트 이상으로 확장하기 위한 TCP 옵션(RFC 1323). 대역폭-지연 곱(Bandwidth-Delay Product, BDP)이 큰 "long fat pipe" 네트워크에서 성능 병목을 해소한다.

## How It Works

**문제: 16비트 윈도우 필드의 한계**

TCP 헤더의 Window 필드는 16비트로 최대 65,535바이트만 표현 가능하다. 고대역폭 또는 고지연 네트워크(예: 위성 링크, 고속 WAN)에서는 이 크기가 회선 용량을 충분히 활용하지 못하는 병목이 된다.

**Window Scale 옵션의 동작**

헤더 필드 크기를 변경하는 대신, 1바이트 스케일 팩터(scaling factor) `s`를 정의하여 기존 16비트 값에 적용한다:

- 범위: 0 ≤ s ≤ 14
- 실제 윈도우 크기 = Window 필드 값 × 2^s
- 최대 윈도우 크기: 2^14 × (2^16 − 1) = **약 1 GiB**

**적용 규칙**

- WSCALE 옵션은 **SYN 세그먼트에서만** 교환 가능 (이후에는 변경 불가)
- 양방향 윈도우 확장을 위해 **양쪽 모두** SYN 세그먼트에 WSCALE 옵션을 포함해야 함
- 어느 한쪽이라도 옵션을 보내지 않으면 해당 방향의 윈도우는 확장되지 않음 (interoperability)

**BDP (Bandwidth-Delay Product)**

BDP = 링크 대역폭 × RTT

BDP가 65,535바이트를 초과하는 경우, 기본 TCP 윈도우 크기로는 파이프를 가득 채울 수 없어 성능이 저하된다. 예: 1 Gbps 링크에 100ms RTT → BDP ≈ 12.5 MB → 16비트 윈도우로는 0.5% 활용에 불과.

## Key Properties

- WSCALE은 헤더 구조를 변경하지 않고 스케일 팩터로 표현 범위를 확장
- 스케일 팩터는 연결별로 고정 (SYN 교환 이후 변경 불가)
- 스케일 팩터는 방향별로 독립 설정 (송신/수신 각각 다를 수 있음)
- "Long fat pipe" 환경에서 반드시 필요한 옵션
- RFC 1323에서 Timestamps 옵션과 함께 정의

## Relationships

- [[tcp-three-way-handshake]] (WSCALE이 SYN/SYN+ACK에서 교환되는 시점)
- [[tcp-timestamps]] (RFC 1323에서 함께 정의된 관련 옵션)
- [[tcp]] (흐름 제어(flow control) 메커니즘의 일부)
- [[tcp-header]] (Window 필드와 WSCALE 옵션의 관계)

## Open Questions

- s ≤ 14로 최대 1GiB로 제한된 이유는 무엇인가? 현대의 고속 네트워크에서 이 한계가 다시 병목이 될 수 있는가?
- WSCALE 협상 실패 시(한쪽이 지원하지 않을 때) 실제 성능 저하를 어떻게 진단하는가?

## Sources

- raw/컴퓨터네트워크/Week 05 TCP Connection Establishment.pdf (p. 33)
