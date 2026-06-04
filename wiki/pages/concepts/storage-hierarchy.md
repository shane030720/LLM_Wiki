---
title: Storage Hierarchy
category: concept
tags: [storage, hardware, memory, database]
sources: [raw/데이터베이스/Storage and File Structure (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Storage hierarchy(저장 계층 구조)는 컴퓨터 시스템에서 데이터를 저장하는 물리적 매체를 접근 속도, 비용, 용량, 휘발성 기준으로 계층화한 구조다. Cache부터 Magnetic disk까지 속도와 비용이 반비례하는 계층을 형성하며, 데이터베이스는 주로 external memory(외부 메모리, 비휘발성)에 영구 저장된다.

## How It Works
각 계층은 접근 속도와 휘발성이 다르다.

- **Cache**: 가장 빠르고 비싼 저장소. 접근 시간 수 nanoseconds(10⁻⁹초). volatile(휘발성). 하드웨어가 직접 관리.
- **Main Memory (RAM)**: 접근 시간 수백 nanoseconds(10⁻⁷초). volatile. 전원 차단 또는 시스템 크래시 시 데이터 소실.
- **Flash Memory**: non-volatile(비휘발성). 접근 시간 수십~수백 microseconds(10⁻⁴~10⁻⁵초). RAM보다 느리지만 Magnetic disk보다 빠름.
- **Magnetic Disk**: non-volatile. 접근 시간 수 milliseconds(10⁻³초). RAM보다 훨씬 느리며, 접근을 위해 반드시 데이터를 main memory로 block 단위로 이동시켜야 한다.

데이터베이스는 Magnetic disk 등의 external memory에 영구 저장되고, 처리를 위해 main memory의 buffer로 block 단위로 로드된다.

## Key Properties
- Cache와 RAM은 volatile: 전원 차단 시 데이터 소실
- Flash memory와 Magnetic disk는 non-volatile: 영구 저장 가능
- 계층이 낮을수록 (cache → disk) 접근 속도 감소, 용량 증가, 단위 용량당 비용 감소
- 데이터베이스 시스템은 disk와 memory 간 block 전송 횟수를 최소화하려 한다

## Relationships
- [[external-memory-model]] (이 계층 구조에서 disk I/O를 핵심 비용으로 분석하는 복잡도 모델)
- [[buffer-manager]] (main memory 내 buffer 공간을 관리하여 disk 접근 횟수를 줄이는 컴포넌트)

## Open Questions
- Flash memory(SSD)가 보편화되면서 전통적인 storage hierarchy 모델의 I/O 비용 가정이 어떻게 바뀌는가?
- Non-volatile RAM(NVRAM, Optane 등) 같은 새로운 매체는 기존 계층 구조의 어디에 위치하는가?

## Sources
- raw/데이터베이스/Storage and File Structure (1).pdf
