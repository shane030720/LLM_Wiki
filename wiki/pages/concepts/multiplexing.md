---
title: Multiplexing and Demultiplexing
category: concept
tags: [multiplexing, fdm, tdm, signal, networking]
sources: [raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf]
created: 2026-06-03
updated: 2026-06-03
---

## Definition
Multiplexing(MUX)은 여러 입력 신호를 하나의 공유 채널(링크)로 합쳐 전송하는 비용 효율적인 자원 공유 기법이다. Demultiplexing(DEMUX)은 그 역방향 동작으로, 하나의 입력 신호를 여러 출력 선 중 하나로 분배한다. 전자공학에서 MUX는 여러 입력 중 하나를 선택하는 특수 스위치로 구현되며, 네트워크의 모든 계층에서 이 개념이 적용된다.

## How It Works
두 가지 주요 방식이 존재한다.

**Frequency-Division Multiplexing (FDM):**
- 각 신호에 서로 다른 주파수 대역을 할당
- 모든 신호가 동시에 같은 매체를 통해 전송
- 완전 활용(full-utilized) 상태에서는 모든 주파수 대역이 사용됨
- 부분 활용(under-utilized) 상태에서는 할당된 대역이 비어 낭비됨

**Synchronous Time-Division Multiplexing (STDM/TDM):**
- 시간을 고정 슬롯으로 나누어 각 신호에 특정 슬롯을 할당
- 각 신호는 자신의 슬롯에만 전송권을 가짐
- Under-utilized 상태에서 빈 슬롯이 낭비됨

**계층별 Multiplexing:**
- 물리 계층: FDM/TDM으로 링크 자원 공유
- 전송(transport) 계층: 다수의 응용 프로세스 데이터를 하나의 네트워크 경로로 합침
- 응용(application) 계층: 다수의 세션·스트림을 하나의 연결로 합침

## Key Properties
- Bandwidth는 이상적으로 단위 시간당 전송 비트 수에 비례
- MUX/DEMUX는 네트워크 모든 계층에서 발생 (계층 간 직교적으로 작동)
- FDM은 주파수 도메인 분리, TDM은 시간 도메인 분리
- Statistical TDM은 고정 슬롯 대신 수요에 따라 슬롯을 동적 할당하여 under-utilization 감소

## Relationships
- [[packet-switching]] — 라우터의 링크 자원 공유에 multiplexing 개념 적용
- [[network-performance-metrics]] — 대역폭(bandwidth)은 multiplexing 효율과 직결
- [[access-network]] — HFC 케이블 망에서 FDM으로 비디오·데이터 채널 분리
- [[ethernet]] — Ethernet 프레임의 Type 필드로 상위 계층 프로토콜 demultiplexing 수행

## Open Questions
- Statistical TDM에서 burst 트래픽이 발생할 때 공정성(fairness)을 어떻게 보장하는가?
- 계층별 multiplexing이 중첩될 때 성능에 어떤 부작용이 발생할 수 있는가?

## Sources
- raw/컴퓨터네트워크/Week 03 Networking Technologies.pdf
