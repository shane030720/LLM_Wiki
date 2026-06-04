---
title: Buffer Manager
category: concept
tags: [buffer, memory, io, replacement-policy, database]
sources: [raw/데이터베이스/Storage and File Structure (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Buffer Manager(버퍼 관리자)는 main memory 내의 buffer 공간을 관리하는 데이터베이스 서브시스템이다. Buffer는 disk block의 복사본을 보관하는 main memory의 일부이며, Buffer Manager는 disk와 memory 사이의 block 전송 횟수를 최소화하여 I/O 비용을 줄이는 역할을 담당한다.

## How It Works
프로그램이 disk의 특정 block을 요청하면 Buffer Manager는 다음 두 경로로 처리한다.

1. **Buffer hit**: 해당 block이 이미 buffer에 있으면 buffer 내 주소를 즉시 반환 (disk I/O 없음)
2. **Buffer miss**: buffer에 없으면
   - buffer에 새 block을 위한 공간 확보 (필요 시 기존 block 교체)
   - 교체 대상 block이 마지막 disk 저장 이후 수정된(dirty) 경우에만 disk에 write-back
   - disk에서 해당 block을 buffer로 읽어 주소 반환

**Buffer Replacement Policies (교체 정책)**

- **LRU (Least Recently Used)**: 가장 오래 전에 사용된 block을 교체. 과거 참조 패턴을 미래 참조의 예측에 활용. OS가 일반적으로 사용하는 정책.
  - 단점: 반복 스캔 패턴(예: nested loop join)에서 비효율적. 같은 데이터를 반복 접근할 때 방금 쫓아낸 block을 다시 읽어야 하는 상황 발생.
- **MRU (Most Recently Used)**: 가장 최근에 사용된 block을 교체. 처리 중인 block은 pin 상태 유지, 마지막 tuple 처리 완료 후 unpin되면 MRU 교체 대상이 됨.
- **혼합 전략**: query optimizer가 제공하는 접근 패턴 힌트를 활용하여 상황에 맞는 정책을 선택적으로 적용.

**Pinned Block**: 현재 사용 중이어서 disk에 write-back하지 못하도록 고정된 buffer block.

## Key Properties
- Buffer hit 시 disk I/O 없이 메모리 주소만 반환하므로 접근 비용이 극히 낮음
- 수정된(dirty) block만 disk에 write-back하여 불필요한 I/O 절감
- LRU는 일반적이나 데이터베이스 특유의 반복 스캔 패턴에서 성능이 저하될 수 있음
- 통계 정보 활용: data dictionary처럼 자주 접근되는 block은 휴리스틱으로 상시 유지
- Query optimizer가 buffer replacement에 힌트를 제공하는 것이 최적에 가까운 전략

## Relationships
- [[storage-hierarchy]] (buffer는 main memory 계층에 존재하며 disk와 상호작용)
- [[external-memory-model]] (buffer 관리는 I/O 복잡도를 줄이는 핵심 수단이며, M이 buffer 크기에 대응)
- [[file-organization]] (파일의 접근 패턴에 따라 교체 정책 결정)
- [[postgresql-storage]] (PostgreSQL의 shared buffer pool이 Buffer Manager를 구현)

## Open Questions
- Nested loop join처럼 LRU가 비효율적인 접근 패턴에 대한 일반적인 최적 교체 정책은?
- Buffer 크기 M이 커질수록 I/O 복잡도가 어떤 비율로 감소하는가?

## Sources
- raw/데이터베이스/Storage and File Structure (1).pdf
