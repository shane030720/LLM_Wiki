---
title: Record Structure
category: concept
tags: [record, block, storage, file, slotted-page]
sources: [raw/데이터베이스/Storage and File Structure (1).pdf]
created: 2026-06-01
updated: 2026-06-01
---

## Definition
Record structure(레코드 구조)는 데이터베이스 파일 내에서 개별 레코드(field의 시퀀스)를 block에 저장하는 방식을 정의한다. 각 field의 크기 고정 여부에 따라 Fixed-length record와 Variable-length record로 구분되며, 여러 Variable-length record를 하나의 block에 저장하기 위해 Slotted page structure가 사용된다.

## How It Works

**Fixed-Length Records (고정 길이 레코드)**

레코드 i는 바이트 `n × (i − 1)`부터 시작(n = 레코드 크기). 접근이 단순하지만 레코드가 block 경계를 넘지 않도록 하는 것이 일반적인 가정이다.

삭제 방법 세 가지:
- Naive: 삭제 위치 이후 레코드를 모두 앞으로 이동 (비효율적)
- Improved: 마지막 레코드를 삭제된 위치로 이동
- Free list: 파일 header에 첫 번째 삭제 레코드의 주소를 저장하고, 삭제된 레코드의 공간에 다음 삭제 레코드의 주소를 체인으로 연결. 삭제된 레코드의 저장 공간을 포인터 저장에 재활용하여 공간 효율적

**Variable-Length Records (가변 길이 레코드)**

발생 원인: varchar 등 가변 길이 필드, 파일 내 다수 레코드 타입 혼재, 반복 필드(배열, multiset).

구조:
- 앞부분: 고정 길이 attribute 직접 저장
- 가변 길이 attribute는 (offset, length) 쌍으로 표현, 실제 데이터는 고정 길이 attribute 전부 뒤에 위치
- Null value는 null-value bitmap으로 표현

**Slotted Page Structure**

하나의 block에 여러 Variable-length record를 저장하기 위한 구조.

Page header에 포함:
- 레코드 항목 수
- block 내 free space의 끝 위치
- 각 레코드의 위치(offset)와 크기

레코드는 page 내에서 이동 가능(빈 공간 없이 연속 배치). 이 경우 header의 entry만 업데이트하면 된다. 포인터는 레코드를 직접 가리키지 않고 header의 entry를 가리켜서, 레코드가 이동해도 외부 포인터가 유효하게 유지된다.

## Key Properties
- Fixed-length record: 접근이 단순하고 삽입 위치 계산이 O(1)
- Free list: 삭제된 레코드 공간을 포인터로 재사용, 별도 포인터 오버헤드 없음
- Variable-length record: 유연하지만 (offset, length) 메타데이터 필요
- Slotted page: page 내부 레코드 이동을 외부에 투명하게 처리
- Block 경계를 넘는 레코드는 일반적으로 허용하지 않음

## Relationships
- [[file-organization]] (레코드를 파일 전체 차원에서 배치하는 방식)
- [[buffer-manager]] (block 단위로 memory에 적재하여 레코드에 접근)
- [[postgresql-storage]] (PostgreSQL의 heap page가 slotted page 구조를 구체적으로 구현)

## Open Questions
- Fixed-length record에서 free list 방식과 레코드 이동 방식 중 어떤 상황에서 각각이 유리한가?
- Variable-length record의 (offset, length) 표현에서 한 레코드의 최대 크기 제한은 어떻게 결정되는가?

## Sources
- raw/데이터베이스/Storage and File Structure (1).pdf
