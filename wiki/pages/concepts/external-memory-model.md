---
title: External-Memory Model
category: concept
tags: [algorithm, complexity, io, database]
sources: [raw/데이터베이스/Storage and File Structure (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
External-Memory Model(외부 메모리 모델, EM 모델)은 데이터가 main memory에 모두 적재될 수 없어 external memory(disk)에 저장되는 환경에서 알고리즘의 비용을 분석하는 계산 모델이다. RAM 모델의 시간 복잡도(기본 연산 횟수) 대신 I/O 복잡도(disk 읽기·쓰기 횟수)를 핵심 성능 지표로 사용한다.

## How It Works
- **RAM model**: 메모리 접근 등 기본 연산의 횟수를 기준으로 시간 복잡도 측정
- **EM model**: external memory에서 main memory로의 read/write 횟수(I/O 수)를 기준으로 I/O 복잡도 측정

주요 notation:
- **N**: 데이터 파일의 레코드 총 수
- **M**: main memory에 한 번에 적재할 수 있는 레코드 수
- **B**: 하나의 block에 담을 수 있는 레코드 수

알고리즘 설계 목표는 I/O 횟수를 최소화하는 것이며, block 단위로 데이터를 전송하므로 B를 최대한 활용하는 것이 중요하다.

## Key Properties
- disk 접근 시간이 memory 접근 시간보다 수십만 배 느리므로 I/O 횟수가 실제 성능을 결정
- Block 단위 전송: 한 번의 I/O는 레코드 하나가 아니라 block(B개 레코드) 전체를 전송
- RAM 모델에서 효율적인 알고리즘이 EM 모델에서는 비효율적일 수 있음
- 데이터베이스의 index 구조, 정렬, 조인 알고리즘 설계 시 이 모델을 기준으로 분석

## Relationships
- [[storage-hierarchy]] (EM 모델이 전제하는 물리적 저장 계층 구조)
- [[buffer-manager]] (main memory의 M 크기를 관리하는 컴포넌트로, EM 모델의 M에 대응)

## Open Questions
- SSD 등 flash storage는 random I/O와 sequential I/O의 속도 차이가 작아 기존 EM 모델 가정이 달라지는데, 이를 어떻게 반영하는가?
- M과 B의 비율에 따라 최적 알고리즘이 어떻게 달라지는가?

## Sources
- raw/데이터베이스/Storage and File Structure (1).pdf
