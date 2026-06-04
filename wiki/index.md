# Wiki Index

Master catalog of all wiki pages. Updated automatically at every Ingest and Lint operation.

> **LLM instruction:** Keep this table sorted by Category (concept → entity → synthesis), then alphabetically by Page within each category. Never delete rows — use ~~strikethrough~~ for deprecated pages.

---

## Content Catalog

| Page | Category | Tags | Updated | Summary |
|------|----------|------|---------|---------|
| [[abstract-data-type]] | concept | adt, abstraction, data-structure, interface | 2026-06-02 | Abstract Data Type(ADT, 추상 자료형)은 자료구조의 추상화(abstraction)다. ADT는 구체적인 구현... |
| [[access-network]] | concept | access-network, dsl, cable, hfc, cellular, networking, wan | 2026-06-03 | Access Network는 최종 사용자(end system)를 인터넷의 첫 번째 라우터(edge router)에 연결하는 네... |
| [[arp]] | concept | network, link-layer, protocol, addressing, arp | 2026-06-03 | ARP(Address Resolution Protocol, RFC 826)는 IP 주소(논리 주소)를 해당 링크 계층 하드웨어... |
| [[adjacency-matrix]] | concept | graph, adjacency-matrix, data-structure, implementation | 2026-06-02 | Adjacency Matrix(인접 행렬)는 를 2차원 행렬로 표현하는 구현 방식이다. 각 정점에 고유한 인덱스 번호를 부여하... |
| [[agent-pool]] | concept | agent-pattern, orchestrator, multi-agent, management | 2026-05-26 | 에이전트 설정(JSON)을 파일 시스템에 저장하고 Orchestrator가 필요에 따라 동적으로 선택·실행하는 에이전트 관리 ... |
| [[agent-session-control]] | concept | agent, session, cli, persistence, permission | 2026-06-03 | AI CLI 에이전트(Claude, Codex, Gemini)에서 대화 세션을 식별·재개·유지 또는 폐기하는 메커니즘의 총칭.... |
| [[agent-specification]] | concept | agent, specification, system-prompt, context, multi-agent | 2026-06-04 | Agent Specification은 LLM 기반 에이전트를 형식적으로 정의하는 구조다. 하나의 에이전트는 **System P... |
| [[agent-state-machine]] | concept | agent, state-machine, agentic-coding, lifecycle, dashboard | 2026-06-04 | Agent State Machine은 에이전틱 시스템에서 개별 에이전트가 가지는 런타임 상태(state)의 집합과 각 상태 간... |
| [[agentic-coding]] | concept | coding-paradigm, llm, sdlc, multi-agent | 2026-05-26 | 코딩 에이전트를 통해 SDLC가 보장되는 개발 프로세스를 수행하는 패러다임. 2025년 4분기부터 주류로 부상하며, 바이브 코... |
| [[agentic-coding-patterns]] | concept | agent-pattern, design-pattern, coding-paradigm, best-practice | 2026-05-26 | 에이전틱 코딩 환경에서 반복적으로 사용되는 구조화된 에이전트 협업 패턴의 집합. 기본 5가지 패턴과 코딩 특화 4가지 패턴으로... |
| [[agile-development-methodology]] | concept | agile, scrum, xp, methodology, sdlc, sprint | 2026-06-01 | Agile Development Methodology는 짧은 사이클(cycle)을 통해 완전한 소프트웨어 제품을 반복적으로 제... |
| [[ai-cli-invocation]] | concept | cli, subprocess, agent, python, invocation | 2026-06-03 | Python 코드에서 AI CLI 도구(Claude, Codex, Gemini)를 `subprocess.run()`으로 호출하... |
| [[all-pairs-shortest-paths]] | concept | graph, shortest-path, dynamic-programming, weighted-graph | 2026-06-01 | **All-pairs shortest paths(모든 쌍 최단 경로)** 문제는 가중치 방향 그래프(weighted direc... |
| [[amortized-analysis]] | concept | algorithm, analysis, complexity, data-structure | 2026-06-01 | Amortized Analysis(상각 분석)는 연속적인 연산의 최악 경우(worst case)에서 각 연산의 평균 비용을 분... |
| [[algorithm-analysis]] | concept | algorithm, analysis, running-time, complexity, worst-case | 2026-06-02 | Algorithm Analysis(알고리즘 분석)란 알고리즘의 실행 시간(running time)과 자원 사용량을 입력 크기 ... |
| [[array-doubling]] | concept | array, dynamic-array, amortized, data-structure | 2026-06-01 | Array Doubling(배열 배증)은 동적 배열(dynamic array)에서 공간이 부족할 때 현재 배열의 두 배 크기의... |
| [[array-based-vector]] | concept | vector, array, data-structure, adt | 2026-06-02 | Array-Based Vector는 고정 크기 배열을 내부 저장소로 사용하여 Vector ADT를 구현한 자료구조다. 요소는 ... |
| [[asymptotic-bounds]] | concept | algorithm, complexity, big-omega, big-theta, asymptotic, best-case, worst-case | 2026-06-02 | 점근적 경계(asymptotic bounds)는 알고리즘 복잡도를 상한·하한·tight bound 세 관점에서 표현하는 표기 ... |
| [[asymptotic-notation]] | concept | asymptotic, complexity, big-o, big-theta, big-omega, growth-rate | 2026-06-01 | 점근 표기법(Asymptotic Notation)은 함수의 점근적 성장률(asymptotic growth rate, asymp... |
| [[arq-protocols]] | concept | arq, error-control, reliability, network, sliding-window | 2026-06-03 | Automatic Repeat reQuest (ARQ)는 수신자가 패킷의 오류를 감지했을 때 송신자에게 재전송을 요청함으로써 ... |
| [[avl-tree]] | concept | avl-tree, balanced-tree, rotation, data-structure, map | 2026-06-02 | AVL Tree는 Adel'son-Vel'ski와 Landis가 고안한 자기 균형 이진 탐색 트리(self-balancing ... |
| [[big-oh-notation]] | concept | algorithm, complexity, big-oh, asymptotic, primitive-operation | 2026-06-02 | Big-Oh notation은 함수 f(n)의 점근적 상한(asymptotic upper bound)을 표현하는 수학적 표기법... |
| [[binary-search]] | concept | search, algorithm, sorted-array, data-structure | 2026-06-02 | Binary Search(이진 탐색)는 정렬된 배열에서 목표 키를 탐색할 때, 매 단계마다 탐색 범위를 절반으로 줄여 O(lo... |
| [[binary-search-tree]] | concept | bst, tree, data-structure, search, map | 2026-06-02 | Binary Search Tree(이진 탐색 트리, BST)는 각 내부 노드 v에 대해 왼쪽 서브트리의 모든 키가 v의 키보다... |
| [[binary-tree]] | concept | binary-tree, tree, data-structure, graph-theory | 2026-06-02 | Binary Tree(이진 트리)는 각 노드가 최대 두 개의 자식 노드를 갖는 트리 자료구조이다. 각 자식은 left chil... |
| [[binary-tree-implementation]] | concept | binary-tree, implementation, linked-list, array, data-structure | 2026-06-02 | 이진 트리는 크게 두 가지 방식으로 구현한다. 포인터 기반의 linked structure(연결 구조)는 노드 객체들이 포인터... |
| [[binary-tree-traversal]] | concept | binary-tree, traversal, algorithm, recursion, expression-tree | 2026-06-02 | Binary tree traversal(이진 트리 순회)은 이진 트리의 모든 노드를 정해진 규칙에 따라 빠짐없이 방문하는 알고... |
| [[bottom-up-heap-construction]] | concept | heap, algorithm, construction, optimization | 2026-06-02 | Bottom-up heap construction은 n개의 주어진 키로부터 을 O(n) 시간에 구성하는 알고리즘이다. n번의 ... |
| [[bcnf]] | concept | database, normalization, bcnf, functional-dependency | 2026-06-01 | BCNF(Boyce-Codd Normal Form)는 관계 스키마 R이 FD 집합 F에 대해 만족해야 하는 정규형으로, F+에... |
| [[breadth-first-search]] | concept | graph, traversal, bfs, algorithm, queue, shortest-path | 2026-06-02 | BFS(Breadth-First Search, 너비 우선 탐색)는 그래프의 모든 정점과 간선을 방문하는 순회 알고리즘이다. 시... |
| [[buffer-manager]] | concept | buffer, memory, io, replacement-policy, database | 2026-06-01 | Buffer Manager(버퍼 관리자)는 main memory 내의 buffer 공간을 관리하는 데이터베이스 서브시스템이다.... |
| [[business-process-management]] | concept | bpm, process, methodology, improvement, reengineering | 2026-06-01 | Business Process Management(BPM)은 조직이 엔드-투-엔드(end-to-end) 비즈니스 프로세스를 지... |
| [[class-np]] | concept | complexity, verification, nondeterministic, certificate | 2026-06-02 | Class NP는 **비결정론적 다항 시간(non-deterministic polynomial time)** 내에 풀 수 있는... |
| [[class-p]] | concept | complexity, polynomial, algorithm, decision-problem | 2026-06-02 | Class P는 **다항 시간(polynomial time)** 내에 해를 구할 수 있는 결정 문제(decision probl... |
| [[classful-addressing]] | concept | ip, ipv4, addressing, classful, netid, hostid, network-layer | 2026-06-03 | Classful Addressing(클래스풀 주소 지정)은 초기 인터넷에서 사용된 IPv4 주소 체계로, 32비트 주소를 고정... |
| [[cidr]] | concept | networking, IP, routing, addressing, scalability | 2026-06-03 | Classless Inter-Domain Routing (CIDR, RFC4632)은 1990년대 초 인터넷의  체계를 대체하... |
| [[collision-handling]] | concept | collision, separate-chaining, open-addressing, linear-probing, quadratic-probing, double-hashing, hash-table | 2026-06-02 | Collision Handling(충돌 처리)은 hash table에서 서로 다른 key가 동일한 hash value를 가져 ... |
| [[computer-network]] | concept | network, node, link, packet, bandwidth | 2026-06-02 | Computer Network는 통신 채널(communications channel)로 상호 연결된 범용 컴퓨터들의 집합으로,... |
| [[congestion-control-principles]] | concept | network, congestion, transport-layer, protocol | 2026-06-03 | Congestion control은 네트워크에서 너무 많은 소스(senders)가 너무 빠르게 너무 많은 데이터를 전송하여 네... |
| [[context-diagram]] | concept | process-modeling, dfd, systems-analysis, context | 2026-06-04 | Context Diagram은 모든 process model에서 최상위에 위치하는 DFD이다. 전체 시스템을 하나의 단일 프로... |
| [[context-explosion]] | concept | mcp, tool-calling, agent, context-window, tradeoff | 2026-06-04 | Context Explosion이란, AI 에이전트에 연결된 도구(tool)의 수가 증가할수록 각 도구의 스키마·설명이 컨텍스... |
| [[contract-driven-iteration]] | concept | agent-pattern, harness, workflow, quality-assurance | 2026-05-26 | 에이전트가 `TASK.md`의 Done-when 기준을 모두 충족할 때까지 반복 실행하는 루프 패턴. "계약(Contract)... |
| [[crud-matrix]] | concept | data-modeling, validation, process-model, systems-analysis, erd | 2026-06-04 | CRUD Matrix는 시스템의 프로세스(또는 유스케이스)와 데이터 엔티티를 교차 참조하여 각 프로세스가 각 엔티티에 대해 수... |
| [[data-flow-diagram]] | concept | dfd, process-modeling, systems-analysis, decomposition | 2026-06-01 | Data Flow Diagram(DFD)은 프로세스 모델을 작성하기 위한 대표적인 기법으로, 시스템 내에서 데이터가 어떻게 흐... |
| [[data-modeling]] | concept | data-model, systems-analysis, logical-model, physical-model, erd | 2026-06-01 | Data Model이란 비즈니스 시스템이 사용하고 생성하는 데이터를 공식적으로 표현하는 방법이다. 데이터가 포착되는 사람(pe... |
| [[database]] | concept | database, data-management, storage, persistence | 2026-06-01 | Database는 대규모의 구조화된 데이터(large collection of structured data)의 집합이다. 단순... |
| [[database-index]] | concept | index, database, search-key, data-structure, query-optimization | 2026-06-01 | 데이터베이스 인덱스는 원하는 레코드를 효율적으로 찾기 위해 설계된 보조 데이터 구조다. `(search-key, pointer... |
| [[database-normalization]] | concept | database, normalization, relational-database, design, lossless-join | 2026-06-01 | Database Normalization(데이터베이스 정규화)은 관계형 스키마를 "좋은 형태(good form)"로 만들기 위... |
| [[depth-first-search]] | concept | graph, traversal, dfs, algorithm, recursion | 2026-06-02 | DFS(Depth-First Search, 깊이 우선 탐색)는 그래프의 모든 정점과 간선을 방문하는 순회 알고리즘이다. 시작 ... |
| [[dfd-elements]] | concept | dfd, process, data-flow, data-store, external-entity | 2026-06-01 | DFD Elements는 Data Flow Diagram을 구성하는 네 가지 기본 요소로, Process, Data Flow,... |
| [[dfd-hierarchy]] | concept | process-modeling, dfd, systems-analysis, decomposition, balancing | 2026-06-04 | DFD Hierarchy는 복잡한 비즈니스 프로세스를 표현하기 위해 DFD를 의도적인 계층 구조로 조직화하는 방법이다. 최상위... |
| [[dictionary-adt]] | concept | dictionary, adt, hash, data-structure, search | 2026-06-02 | Dictionary ADT(추상 자료형)는 키-값(key-value) 쌍의 항목(entry)들을 저장하며, 탐색(search)... |
| [[directed-acyclic-graph]] | concept | graph, dag, directed-graph, topological-order, digraph | 2026-06-02 | DAG(Directed Acyclic Graph, 방향 비순환 그래프)는 모든 간선이 방향을 가지며(directed), 방향을... |
| [[divide-and-conquer]] | concept | algorithm, paradigm, recursion, divide-and-conquer | 2026-06-02 | Divide and Conquer(분할 정복)는 큰 문제를 동일한 유형의 더 작은 부분 문제들로 분할(Divide)하고, 각각... |
| [[deque]] | concept | deque, queue, data-structure, double-ended | 2026-06-02 | Deque(Double-Ended Queue)는 앞(front)과 뒤(rear) 양쪽에서 모두 삽입과 제거가 가능한 큐의 확장... |
| [[doubly-linked-list]] | concept | linked-list, data-structure, list, pointer, sentinel-node | 2026-06-02 | Doubly linked list(이중 연결 리스트)는 각 노드가 원소(element)와 함께 이전 노드를 가리키는 포인터(p... |
| [[dynamic-programming]] | concept | algorithm, optimization, dynamic-programming, subproblem | 2026-06-01 | Dynamic Programming(동적 계획법)은 하위 문제(subproblem)의 해를 재계산하지 않고 테이블이나 딕셔너리... |
| [[end-to-end-argument]] | concept | networking, architecture, design-principle, internet | 2026-06-03 | End-to-End Argument(종단간 논증)은 특정 네트워크 기능의 올바르고 완전한 구현은 통신 시스템의 끝점(endpo... |
| [[entity-relationship-diagram]] | concept | erd, entity, attribute, relationship, cardinality, modality, foreign-key, data-modeling | 2026-06-01 | Entity Relationship Diagram(ERD)은 데이터 모델을 시각적으로 표현하는 가장 대표적인 방법이다. 시스템... |
| [[entity-relationship-model]] | concept | database, er-model, schema-design, modeling | 2026-06-01 | Entity-Relationship(ER) 모델은 데이터베이스 스키마를 개념적으로 설계하기 위한 데이터 모델이다. 현실 세계를... |
| [[entry-adt]] | concept | adt, key-value, priority-queue, data-structure | 2026-06-02 | Entry는 key와 value의 쌍(pair)으로 구성된 추상 자료형(ADT)이다. Key는 해당 항목을 식별하거나 순위를 ... |
| [[epcc]] | concept | pattern, agentic-coding, coding-workflow, harness | 2026-06-04 | EPCC (Explore → Plan → Code → Commit)는 AI 에이전트가 코딩 작업을 수행할 때 따르는 4단계 순... |
| [[er-attributes]] | concept | database, er-model, attribute, composite, multivalued, derived | 2026-06-01 | ER 모델에서 attribute(속성)는 entity set의 모든 구성원이 공통으로 가지는 서술적 특성(descriptive... |
| [[er-to-relational-schema]] | concept | database, er-model, relational-schema, schema-design, reduction | 2026-06-01 | ER 다이어그램을 관계형 데이터베이스 스키마(relational schema)로 변환하는 체계적 절차이다. 모든 entity ... |
| [[event-response-list]] | concept | systems-analysis, use-case, requirement, event | 2026-06-04 | Event-Response List는 시스템이 반응해야 하는 모든 이벤트(event)를 식별하고 목록화한 아티팩트(artifa... |
| [[evpn]] | concept | vlan, overlay, tunneling, network, data-center, ethernet | 2026-06-03 | EVPN(Ethernet Virtual Private Network)은 Layer 2 Ethernet 프레임을 Layer 3 ... |
| [[external-merge-sort]] | concept | database, sorting, algorithm, external-memory, i-o-complexity | 2026-06-01 | External merge sort는 메모리에 전체를 올릴 수 없는 대용량 릴레이션을 디스크 상에서 정렬하기 위한 알고리즘이다... |
| [[external-memory-model]] | concept | algorithm, complexity, io, database | 2026-06-01 | External-Memory Model(외부 메모리 모델, EM 모델)은 데이터가 main memory에 모두 적재될 수 없어... |
| [[feasibility-analysis]] | concept | feasibility, analysis, project, economics, risk | 2026-06-01 | Feasibility Analysis(타당성 분석)는 제안된 정보시스템 프로젝트가 실제로 추진할 가치가 있는지를 기술적·경제적... |
| [[file-organization]] | concept | file, organization, heap, sequential, hashing | 2026-06-01 | File organization(파일 구성)은 데이터베이스의 레코드 집합을 파일(block의 시퀀스) 내에 배치하는 방식이다.... |
| [[functional-dependency]] | concept | database, relational-database, functional-dependency, normalization | 2026-06-01 | Functional Dependency(함수 종속)는 관계형 스키마 R에서 속성 집합 α와 β 사이의 제약으로, 어떤 두 튜플... |
| [[graph]] | concept | graph, data-structure, vertex, edge | 2026-06-02 | Graph는 객체 간의 쌍별(pairwise) 관계를 표현하는 자료구조로, 정점(vertex)의 집합 V와 간선(edge)의 ... |
| [[graph-representation]] | concept | graph, data-structure, adjacency-list, adjacency-matrix, edge-list | 2026-06-02 | 그래프를 컴퓨터 메모리에 저장하는 세 가지 주요 방식: Edge List, Adjacency List, Adjacency Ma... |
| [[graph-representations]] | concept | graph, data-structure, edge-list, adjacency-list, adjacency-matrix | 2026-06-02 | 그래프 G = (V, E)를 컴퓨터 메모리에 저장하는 세 가지 표준 방법이다: Edge List, Adjacency List,... |
| [[gratuitous-arp]] | concept | arp, link-layer, address-resolution, network | 2026-06-03 | Gratuitous ARP(GARP)는 호스트가 자신의 IP 주소를 대상으로 ARP request를 전송하는 특수 ARP 동작... |
| [[greedy-algorithm]] | concept | algorithm, optimization, greedy | 2026-06-02 | Greedy Algorithm(욕심쟁이 알고리즘)은 각 단계에서 주어진 제한적인 "단기적 기준(short-term criter... |
| [[handoff]] | concept | agent-communication, pipeline, multi-agent, workflow | 2026-05-26 | 멀티 에이전트 파이프라인에서 한 에이전트의 출력을 다음 에이전트의 입력으로 전달하는 마크다운 파일. 에이전트 간 공유 메모리 ... |
| [[harness-engineering]] | concept | agent-design, infrastructure, best-practice, context-engineering | 2026-05-26 | 프롬프트나 모델 자체를 넘어, 에이전트가 실행되는 외부 환경(도구, 데이터, 검증 파이프라인, 안전 장치)을 구조적으로 설계하... |
| [[hash-collision-handling]] | concept | hash, collision, open-addressing, separate-chaining, data-structure | 2026-06-02 | Hash collision은 서로 다른 두 개 이상의 키(key)가 동일한 해시 값(hash value)을 가져 동일한 버킷(... |
| [[hash-function]] | concept | hash-function, hash-code, compression-function, collision, hash-table | 2026-06-02 | Hash Function(해시 함수)은 임의의 key를 hash table의 bucket 인덱스 [0, N-1]로 변환하는 함... |
| [[hash-join]] | concept | database, join, algorithm, hashing, equi-join, partition | 2026-06-01 | Hash join은 equi-join과 natural join에 적용 가능한 join 알고리즘으로, hash function을... |
| [[hash-table]] | concept | hash-table, data-structure, map, bucket-array, load-factor, rehashing | 2026-06-02 | Hash Table(해시 테이블)은 key-value 쌍을 저장하는 자료구조로, hash function을 통해 key를 bu... |
| [[heap]] | concept | heap, tree, priority-queue, data-structure | 2026-06-02 | Heap은 각 노드에 키(key)를 저장하는 이진 트리(binary tree)로, 다음 두 가지 속성을 동시에 만족하는 자료구... |
| [[heap-sort]] | concept | heap, sort, algorithm, priority-queue | 2026-06-02 | Heap-sort는  기반 Priority Queue를 활용하는 비교 정렬 알고리즘으로, n개의 원소를 O(n log n) 시... |
| [[hook]] | concept | automation, agent-lifecycle, determinism, harness | 2026-05-26 | 에이전트 생명주기의 특정 이벤트에서 자동으로 실행되는 스크립트. 확률적으로 동작하는 AI 에이전트의 결정을 특정 시점에서 결정... |
| [[initial-sequence-number]] | concept | tcp, sequence-number, security, isn, randomness | 2026-06-03 | TCP 연결을 시작할 때 각 엔드포인트가 자신의 SYN 세그먼트에 포함시켜 전송하는 초기 시퀀스 번호(Initial Seque... |
| [[insertion-sort]] | concept | sorting, algorithm, insertion-sort, in-place | 2026-06-02 | Insertion Sort(삽입 정렬)는 우선순위 큐를 정렬 시퀀스(sorted sequence)로 구현한 의 변형이다. 새 ... |
| [[icmp]] | concept | network, protocol, icmp, error-reporting, diagnostics | 2026-06-03 | ICMP(Internet Control Message Protocol)는 호스트와 라우터가 네트워크 레벨의 정보를 주고받기 위... |
| [[internet-standards]] | concept | standard, ietf, rfc, w3c, ieee, sdo, de-facto, de-jure | 2026-06-02 | Standard(표준)은 "어떤 것을 수행하는 방식에 대해 널리 합의된 방법"이다. 인터넷 표준(Internet Standar... |
| [[intersection-entity]] | concept | erd, data-modeling, many-to-many, normalization, systems-analysis | 2026-06-04 | Intersection Entity(교차 엔티티, 연관 엔티티)는 두 엔티티 사이의 다대다(M:N) 관계를 해소하기 위해 새롭... |
| [[ip-forwarding]] | concept | networking, IP, forwarding, routing, hop-by-hop | 2026-06-03 | IP Forwarding(IP 포워딩)은 IP 데이터그램이 목적지에 도달할 수 있도록 호스트 또는 라우터가 포워딩 테이블(Fo... |
| [[ipv4-datagram]] | concept | ip, ipv4, header, datagram, network-layer, ttl, checksum, protocol | 2026-06-03 | IPv4 Datagram은 인터넷 프로토콜 버전 4 [RFC 791]에서 정의된 네트워크 계층의 프로토콜 데이터 단위(PDU)... |
| [[ipv4-fragmentation]] | concept | ip, ipv4, fragmentation, mtu, reassembly, flags | 2026-06-03 | IPv4 Fragmentation(IPv4 단편화)은 IP 데이터그램 크기가 링크의 MTU(Maximum Transfer Un... |
| [[ipv4-options]] | concept | ip, ipv4, options, record-route, source-route, timestamp, network-layer | 2026-06-03 | IPv4 Options는 IPv4 헤더의 선택적(optional) 필드로, 데이터그램 단위로 특수 처리를 지정할 수 있게 하는... |
| [[ipv4-special-purpose-addresses]] | concept | networking, IPv4, addressing, broadcast, loopback | 2026-06-03 | IPv4 Special-Purpose Addresses(IPv4 특수 목적 주소)는 일반 유니캐스트 주소 할당에 사용되지 않고... |
| [[ipv6-tunneling]] | concept | networking, IPv6, transition, tunneling, encapsulation | 2026-06-03 | IPv6 Tunneling(IPv6 터널링)은 IPv4 네트워크 인프라를 통해 IPv6 데이터그램을 전달하기 위해 IPv6 패... |
| [[iterator]] | concept | iterator, linked-list, ADT, abstraction, position | 2026-06-02 | Iterator(반복자)는 컨테이너(container)의 내부 구현(포인터, 인덱스 등)을 숨기면서(hiding) 원소에 순차... |
| [[list-adt]] | concept | list, doubly-linked-list, data-structure, adt, node | 2026-06-02 | List ADT는 요소를 Position으로 참조하는 추상 자료형이다. 이중 연결 리스트(Doubly Linked List)로... |
| [[longest-prefix-matching]] | concept | networking, routing, forwarding, algorithm, TCAM | 2026-06-03 | Longest Prefix Matching(최장 프리픽스 매칭, LPM)은 IP 포워딩 테이블에서 목적지 주소와 매칭되는 항목... |
| [[loop]] | concept | automation, scheduling, agent-lifecycle, recurring-task | 2026-05-26 | 에이전트가 정해진 주기 또는 조건에 따라 반복적으로 작업을 실행하는 자동화 메커니즘. 사람이 개입하지 않아도 에이전트가 정기적... |
| [[mac-address]] | concept | network, link-layer, addressing, ethernet, hardware | 2026-06-03 | MAC(Medium Access Control) 주소는 네트워크 인터페이스 카드(NIC)에 고유하게 부여된 48비트 하드웨어 ... |
| [[map-adt]] | concept | map, adt, data-structure, key-value | 2026-06-02 | Map(맵)은 key-value 쌍(entry)을 저장하는 추상 자료형(Abstract Data Type)이다. 각 key는 ... |
| [[mapping-cardinality]] | concept | database, er-model, cardinality, relationship, participation | 2026-06-01 | Mapping cardinality(매핑 카디널리티)는 하나의 entity가 특정 relationship set을 통해 연결될... |
| [[maximum-segment-size]] | concept | tcp, mss, mtu, options, fragmentation, ethernet | 2026-06-03 | TCP가 피어로부터 수신하겠다는 최대 세그먼트 크기. TCP 데이터 바이트만 계산하며 TCP 헤더나 IP 헤더의 크기는 포함하... |
| [[mcp]] | concept | protocol, integration, tool-use, standardization | 2026-05-26 | AI 에이전트가 외부 시스템과 균일한 방식으로 연결할 수 있도록 Anthropic이 만든 개방형 표준 프로토콜. OpenAI와... |
| [[memoization]] | concept | algorithm, dynamic-programming, recursion, caching, top-down | 2026-06-01 | Memoization(메모이제이션)은 재귀 알고리즘에서 하위 문제의 해를 딕셔너리(또는 테이블)에 저장해두고, 동일한 하위 문... |
| [[middlebox]] | concept | networking, middleware, NAT, firewall, SDN, NFV | 2026-06-03 | Middlebox(미들박스)는 출발지 호스트와 목적지 호스트 사이의 데이터 경로 상에서 표준 IP 라우터의 정상 기능 이외의 ... |
| [[minimum-spanning-tree]] | concept | graph, tree, optimization, spanning-tree | 2026-06-02 | Minimum Spanning Tree(최소 신장 트리, MST)는 연결된 무방향 가중 그래프 G=(V,E,W)에서 모든 정점... |
| [[modality]] | concept | erd, data-modeling, relationship, constraint, systems-analysis | 2026-06-04 | Modality는 ERD에서 관계(relationship)의 필수성(optionality)을 나타내는 개념으로, 한 엔티티의 ... |
| [[multi-cli-agent-setup]] | concept | agent, cli, pattern, agentic-coding, skill | 2026-06-04 | Multi-CLI Agent Setup은 Claude, Codex, Gemini 등 서로 다른 CLI 기반 AI 에이전트를 동... |
| [[multiplexing]] | concept | multiplexing, fdm, tdm, signal, networking | 2026-06-03 | Multiplexing(MUX)은 여러 입력 신호를 하나의 공유 채널(링크)로 합쳐 전송하는 비용 효율적인 자원 공유 기법이다... |
| [[mpls]] | concept | network, routing, mpls, traffic-engineering, label-switching | 2026-06-03 | MPLS(Multiprotocol Label Switching)는 MPLS 가능 라우터 네트워크에서 최장 프리픽스 매칭(lon... |
| [[network-address-translation]] | concept | networking, NAT, IPv4, addressing, security, middlebox | 2026-06-03 | Network Address Translation (NAT, 네트워크 주소 변환)은 로컬 네트워크의 사설(private) IP... |
| [[network-addressing]] | concept | networking, addressing, mac, ip, port, physical-address, logical-address, unicast | 2026-06-03 | Network Addressing은 네트워크 상의 장치 또는 프로세스를 고유하게 식별하기 위한 체계이다. TCP/IP 프로토콜... |
| [[network-connecting-devices]] | concept | switch, router, hub, bridge, repeater, stp, networking, layer2 | 2026-06-03 | Network Connecting Device는 호스트 또는 네트워크 세그먼트를 상호 연결하여 더 큰 네트워크나 인터넷을 구성... |
| [[network-layer]] | concept | network, routing, forwarding, data-plane, control-plane, sdn, best-effort | 2026-06-03 | Network Layer(네트워크 계층)는 인터넷 프로토콜 스택의 3계층으로, 송신 호스트에서 수신 호스트까지 데이터그램(da... |
| [[network-performance-metrics]] | concept | throughput, bandwidth, rtt, bdp, bottleneck, networking, performance | 2026-06-03 | 네트워크의 성능을 정량적으로 평가하는 주요 지표들의 집합이다. 핵심 지표로 Throughput(처리량), Bandwidth(대... |
| [[network-protocol]] | concept | protocol, syntax, semantics, timing, communication | 2026-06-02 | Network Protocol은 분산된 개체(distributed entities)들 간에 데이터 통신 또는 상태 동기화를 수... |
| [[normalization]] | concept | normalization, 1nf, 2nf, 3nf, data-modeling, logical-model, validation | 2026-06-01 | Normalization은 논리적 데이터 모델(logical data model)을 검증(validate)하고 그 조직을 개선... |
| [[np-completeness]] | concept | np-complete, np-hard, reduction, complexity, circuit-sat | 2026-06-02 | NP-Complete(NP-완전)는 에 속하면서 동시에 NP-Hard인 문제들의 클래스다. 어떤 문제 Q가 **NP-Hard*... |
| [[orchestrator]] | concept | agent, orchestrator, agentic-coding, subprocess, pool | 2026-06-04 | Orchestrator는 에이전틱 시스템에서 에이전트 풀(Agent Pool)의 정의 파일을 읽고, 현재 목표에 적합한 에이전... |
| [[ordered-index]] | concept | index, ordered-index, dense-index, sparse-index, primary-index, secondary-index, multilevel-index | 2026-06-01 | Ordered Index는 인덱스 엔트리들이 검색 키 값의 정렬 순서로 저장되는 인덱스다. 파일의 물리적 저장 순서와의 관계에... |
| [[osi-reference-model]] | concept | networking, osi, layering, standard, iso, 7-layer, pdu | 2026-06-03 | OSI(Open Systems Interconnection) 참조 모델은 ISO(국제표준화기구)가 개발한 7계층 네트워크 아키... |
| [[packet-delay]] | concept | delay, latency, queueing, transmission, propagation, networking | 2026-06-03 | 패킷이 소스에서 목적지로 전달되는 과정에서 각 노드(라우터)에서 발생하는 총 지연을 Nodal Delay라 한다. 총 지연은 ... |
| [[packet-scheduling]] | concept | networking, QoS, router, scheduling, queue, fairness | 2026-06-03 | Packet Scheduling(패킷 스케줄링)은 라우터의 출력 포트에서 큐에 대기 중인 패킷들 중 다음에 링크로 전송할 패킷... |
| [[packet-switching]] | concept | packet-switching, networking, routing, queueing, store-and-forward | 2026-06-03 | Packet Switching은 데이터를 패킷(packet) 단위로 분할하여 네트워크를 통해 전달하는 방식이다. 각 패킷은 헤... |
| [[parallel-agent]] | concept | agent-pattern, multi-agent, performance, workflow | 2026-05-26 | 여러 에이전트가 동일한 입력을 동시에 처리하거나 독립적인 작업을 병렬로 수행하는 구조. 총 실행 시간이 가장 오래 걸리는 단계... |
| [[path-mtu-discovery]] | concept | tcp, mtu, pmtud, icmp, fragmentation, smss | 2026-06-03 | 두 호스트 간의 경로(path) 상에서 가장 작은 MTU(Path MTU)를 발견하여 IP 단편화(fragmentation)를... |
| [[plan-mode]] | concept | agent-mode, workflow, review, implementation | 2026-05-26 | 에이전트가 파일 읽기와 검색만 수행하고 파일 수정을 차단하는 읽기 전용 실행 모드. 구현 전에 계획을 수립하고 사용자 승인을 ... |
| [[planner-reviewer-pipeline]] | concept | agent, pipeline, planner, reviewer, multi-agent, ping-pong, quality-gate | 2026-06-04 | Planner-Reviewer Pipeline은 Planner(AGENT1)와 Reviewer(AGENT2) 두 개의 전문화된... |
| [[pq-sort]] | concept | sorting, algorithm, priority-queue | 2026-06-02 | PQ-Sort는 우선순위 큐를 중간 자료구조로 활용하는 범용 비교 기반 정렬 알고리즘이다. 시퀀스 S의 n개 원소를 오름차순으... |
| [[priority-queue]] | concept | data-structure, abstract-data-type, queue, sorting | 2026-06-02 | Priority Queue(우선순위 큐)는 각 원소에 우선순위(key)를 부여하여 저장하는 추상 자료형(ADT)이다. 스택·큐... |
| [[process-description]] | concept | process-modeling, dfd, systems-analysis, documentation, structured-english | 2026-06-04 | Process Description은 DFD의 개별 프로세스에 부여하는 텍스트 기반 보충 문서이다. DFD 다이어그램만으로는 ... |
| [[process-model]] | concept | process-modeling, systems-analysis, design | 2026-06-01 | Process Model은 비즈니스 프로세스가 어떻게 운영되는지를 공식적으로 표현하는 방법이다. 수행되는 활동(activity... |
| [[product-requirements-document]] | concept | requirement, documentation, sdlc, vibe-coding, agentic-coding | 2026-06-03 | Product Requirements Document(PRD)는 소프트웨어 제품이 무엇을 해야 하는지를 Why → What →... |
| [[project-estimation-and-planning]] | concept | project-management, estimation, work-breakdown-structure, scope, timeboxing | 2026-06-01 | Project estimation and planning은 프로젝트의 시간과 노력에 대한 예측값을 도출하고, 이를 바탕으로 w... |
| [[project-portfolio-management]] | concept | project-management, portfolio, planning, sdlc | 2026-06-04 | Project Portfolio Management(PPM)은 조직 내 모든 프로젝트(진행 중인 것과 승인 대기 중인 것)를 ... |
| [[project-selection]] | concept | project-management, portfolio, sdlc, selection, feasibility | 2026-06-01 | Project selection은 조직이 수행할 IT 프로젝트를 식별하고 우선순위를 결정하는 과정이다. 승인 위원회(appro... |
| [[protocol-layering]] | concept | networking, layering, protocol, encapsulation, abstraction, service, interface | 2026-06-03 | Protocol Layering은 네트워크 기능을 순서가 있는 계층적 추상화 집합으로 조직화하는 소프트웨어 공학적 기법이다. ... |
| [[proxy-arp]] | concept | arp, network, router, link-layer, security | 2026-06-03 | Proxy ARP [RFC 1027]는 라우터(또는 특별히 구성된 시스템)가 다른 호스트를 대신하여 ARP request에 응... |
| [[pseudocode]] | concept | algorithm, pseudocode, notation, analysis | 2026-06-02 | Pseudocode(의사코드)란 알고리즘을 기술하기 위한 고수준(high-level) 표기법으로, 영어 산문보다는 구조적이고 ... |
| [[query-processing]] | concept | database, query, optimization, relational-algebra, selection, index | 2026-06-01 | Query processing은 SQL로 작성된 질의를 실제 데이터로 변환하는 일련의 과정이다. Parsing과 transla... |
| [[queue]] | concept | queue, data-structure, fifo, adt | 2026-06-02 | Queue는 First-In-First-Out(FIFO) 원칙을 따르는 선형 추상 자료형(ADT)이다. 먼저 삽입된 요소가 먼... |
| [[rapid-application-development]] | concept | rad, prototyping, iterative, methodology, sdlc, case-tool | 2026-06-01 | Rapid Application Development(RAD)은 특수 기법과 도구(CASE tools, visual progr... |
| [[record-structure]] | concept | record, block, storage, file, slotted-page | 2026-06-01 | Record structure(레코드 구조)는 데이터베이스 파일 내에서 개별 레코드(field의 시퀀스)를 block에 저장하... |
| [[relational-algebra]] | concept | database, query-language, algebra, operator, sql | 2026-06-01 | Relational Algebra는 relation을 입력으로 받아 새로운 relation을 출력하는 연산들의 집합으로 구성된... |
| [[relational-model]] | concept | database, relation, tuple, schema, key | 2026-06-01 | Relational Model은 데이터를 테이블(table) 형태로 조직화하는 데이터 모델이다. 각 테이블은 relation이... |
| [[requirement-engineering]] | concept | requirement, sdlc, system-analysis, software-engineering | 2026-06-03 | Requirement Engineering은 소프트웨어 시스템이 "무엇을" 해야 하는지를 체계적으로 수집, 분석, 명세, 검증... |
| [[route-aggregation]] | concept | networking, routing, IP, scalability, hierarchy | 2026-06-03 | Route Aggregation(경로 집약, Supernetting이라고도 함)은 인접한 여러 IP prefix를 하나의 짧은... |
| [[router-architecture]] | concept | networking, router, hardware, switching, forwarding, queuing | 2026-06-03 | Router Architecture(라우터 아키텍처)는 네트워크 라우터의 내부 구조로, 입력 포트(input ports), 스... |
| [[scope-creep]] | concept | project-management, scope, risk, sdlc | 2026-06-04 | Scope Creep(범위 잠식)은 프로젝트 진행 중 초기에 정의되지 않은 요구사항이나 기능이 공식적인 변경 검토 없이 점진적... |
| [[sdlc]] | concept | software-engineering, process, requirements | 2026-05-26 | 소프트웨어 개발의 전 과정을 단계별로 구조화한 프레임워크. Planning → Analysis → Design → Implem... |
| [[sdlc-methodology-selection]] | concept | sdlc, methodology, project-management, waterfall, agile, rad | 2026-06-01 | SDLC(Systems Development Life Cycle) methodology selection은 프로젝트에 가장 적... |
| [[selection-sort]] | concept | sorting, algorithm, selection-sort, in-place | 2026-06-02 | Selection Sort(선택 정렬)는 우선순위 큐를 비정렬 시퀀스(unsorted sequence)로 구현한 의 변형이다.... |
| [[selective-acknowledgment]] | concept | tcp, sack, acknowledgment, retransmission, options | 2026-06-03 | TCP 수신자가 연속적이지 않게(out-of-sequence) 수신된 데이터 블록의 범위를 송신자에게 알려, 송신자가 실제로 ... |
| [[sequence-adt]] | concept | sequence, adt, data-structure, index, position | 2026-06-02 | Sequence ADT는 Vector ADT(인덱스 기반 접근)와 List ADT(position 기반 접근)를 통합한 추상 ... |
| [[sequential-agent]] | concept | agent-pattern, pipeline, multi-agent, workflow | 2026-05-26 | 이전 에이전트의 완료를 기다린 후 다음 에이전트가 실행되는 직렬 파이프라인 구조. 각 에이전트의 출력이 다음 에이전트의 입력이... |
| [[silly-window-syndrome]] | concept | tcp, flow-control, performance, sws, nagle, clark, delayed-ack | 2026-06-03 | Silly Window Syndrome (SWS)는 TCP 슬라이딩 윈도우의 잘못된 구현으로 인해 매우 작은 데이터를 운반하는... |
| [[singly-linked-list]] | concept | linked-list, data-structure, pointer, node, dynamic | 2026-06-02 | Singly Linked List는 노드(node)의 시퀀스로 구성된 구체적(concrete) 자료구조다. 각 노드는 데이터 ... |
| [[skill]] | concept | harness, agent-design, reusability, procedure | 2026-05-26 | 에이전트가 특정 반복 가능한 작업을 수행하는 방법을 정의한 마크다운 파일. SKILL.md와 보조 파일들로 하나의 폴더를 구성... |
| [[software-engineering-evolution]] | concept | software-engineering, history, AI, paradigm-shift, intelligent-systems | 2026-06-03 | Software Engineering Evolution(소프트웨어 엔지니어링의 진화)은 소프트웨어 개발 패러다임이 역사적으로 ... |
| [[spec-driven-development]] | concept | coding-paradigm, requirements, vibe-coding, best-practice | 2026-05-26 | "Spec First, Code Later" 원칙에 따라 코드 작성 이전에 요구사항 명세를 먼저 완성하는 개발 방법론. 바이브... |
| [[sql]] | concept | sql, query-language, ddl, dml, database | 2026-06-01 | SQL(Structured Query Language)은 관계형 데이터베이스를 기술하고 조작하기 위한 비절차적(non-proc... |
| [[sql-aggregate-functions]] | concept | sql, aggregate, group-by, having, avg, sum, count | 2026-06-01 | SQL 집계 함수(Aggregate Functions)는 관계의 특정 컬럼에 있는 값들의 집합(또는 멀티셋)에 대해 단일 스칼... |
| [[sql-data-types-and-schemas]] | concept | sql, data-type, schema, index, large-object, vector, database | 2026-06-01 | SQL은 기본 스칼라 타입(varchar, numeric 등) 외에도 기본값(DEFAULT), 인덱스(INDEX), 대용량 객... |
| [[sql-ddl]] | concept | sql, ddl, schema, table, constraint, data-type | 2026-06-01 | SQL DDL(Data Definition Language)은 관계형 데이터베이스의 스키마를 정의·변경·삭제하는 SQL 명령어... |
| [[sql-dml]] | concept | sql, dml, insert, update, delete, case, modification | 2026-06-01 | SQL 데이터 수정 언어는 기존 관계의 내용을 변경하는 명령어 집합이다. `DELETE`(튜플 삭제), `INSERT`(튜플 ... |
| [[sql-integrity-constraints]] | concept | sql, integrity, constraint, referential-integrity, foreign-key, database | 2026-06-01 | Integrity Constraint(무결성 제약)는 권한이 있는 사용자의 데이터베이스 변경이 데이터 일관성을 훼손하지 않도록... |
| [[sql-join-expressions]] | concept | sql, join, relational-algebra, database | 2026-06-01 | SQL Join 연산은 두 릴레이션의 튜플을 조인 조건(join predicate)에 따라 결합하는 연산이다. 기본적으로 Ca... |
| [[sql-null-values]] | concept | sql, null, three-valued-logic, unknown, is-null | 2026-06-01 | SQL에서 NULL은 값이 알 수 없거나(unknown) 존재하지 않음을 나타내는 특수 마커다. NULL을 포함하는 비교 연산... |
| [[sql-select-query]] | concept | sql, select, query, join, natural-join, set-operation, order-by | 2026-06-01 | SQL SELECT 질의는 하나 이상의 관계에서 조건을 만족하는 튜플들의 특정 속성 값을 추출하는 연산이다. 관계 대수의 pr... |
| [[sql-subqueries]] | concept | sql, subquery, exists, in, with, derived-relation, correlated-subquery | 2026-06-01 | SQL 서브쿼리(subquery)는 다른 쿼리 내부에 중첩된 `SELECT-FROM-WHERE` 표현식이다. 집합 멤버십 검사... |
| [[sql-transactions]] | concept | sql, transaction, atomicity, isolation, database | 2026-06-01 | Transaction(트랜잭션)은 데이터베이스에서 하나의 논리적 작업 단위(unit of work)이다. 원자성(atomici... |
| [[sql-views]] | concept | sql, view, virtual-relation, database | 2026-06-01 | View(뷰)는 실제 데이터베이스에 물리적으로 저장된 릴레이션이 아닌 가상 릴레이션(virtual relation)이다. `C... |
| [[stack]] | concept | stack, data-structure, lifo, abstract-data-type, array, linked-list | 2026-06-02 | Stack은 Last-In-First-Out (LIFO) 원칙에 따라 원소를 삽입하고 제거하는 추상 자료구조(ADT)다. 가장... |
| [[storage-hierarchy]] | concept | storage, hardware, memory, database | 2026-06-01 | Storage hierarchy(저장 계층 구조)는 컴퓨터 시스템에서 데이터를 저장하는 물리적 매체를 접근 속도, 비용, 용량... |
| [[string-matching]] | concept | string, pattern-matching, algorithm, text-processing | 2026-06-01 | String Matching(스트링 매칭)은 텍스트 T(크기 n)에서 패턴 P(크기 m)와 동일한 부분 문자열을 찾는 문제다.... |
| [[strongly-connected-component]] | concept | graph, algorithm, directed-graph, connectivity, scc | 2026-06-01 | Strongly Connected Component(SCC, 강연결 요소)는 방향 그래프(digraph)의 극대 강연결 부분 ... |
| [[structured-systems-development]] | concept | sdlc, waterfall, v-model, parallel, methodology, structured | 2026-06-01 | Structured Systems Development은 SDLC 기반의 전통적 개발 방법론 범주로, 한 단계(phase)가 ... |
| [[subnet-addressing]] | concept | ip, ipv4, subnet, subnetting, subnet-mask, prefix-length, network-layer, cidr | 2026-06-03 | Subnet Addressing(서브넷 주소 지정, RFC 950)은 1980년대 초 LAN의 급증에 대응하여 도입된 메커니즘... |
| [[subprocess]] | concept | python, agent-communication, cli, implementation | 2026-05-26 | Python `subprocess` 모듈을 사용하여 하나의 에이전트가 다른 CLI 에이전트를 프로세스로 호출하는 메커니즘. 에... |
| [[system]] | concept | system, architecture, components, boundary, constraint | 2026-06-03 | System(시스템)이란 공통된 목적이나 목표를 달성하기 위해 함께 동작하는, 상호작용하고 상호 연관되거나 상호 의존적인 구성... |
| [[system-analysis]] | concept | system-analysis, requirements, specification, modeling, constraint | 2026-06-03 | System Analysis(시스템 분석)란 사용자·운영·비즈니스가 원하는 목표를 도출하고, 시스템의 범위와 제약을 명확화하며... |
| [[system-prompt]] | concept | agent-design, prompt-engineering, context, llm | 2026-05-26 | 에이전트의 역할, 입출력 형식, 제약 조건을 정의하는 지시문. 대화 시작 전 LLM에게 주입되며 에이전트의 전체 행동 방식을 ... |
| [[system-request]] | concept | sdlc, requirements, project-management, systems-analysis, project-initiation | 2026-06-04 | System Request는 SDLC(Systems Development Life Cycle)의 Planning Phase 중... |
| [[systems-development-life-cycle]] | concept | sdlc, process, information-systems, methodology, lifecycle | 2026-06-01 | Systems Development Life Cycle(SDLC)는 정보시스템을 계획·분석·설계·구현하는 일련의 단계로 구성된... |
| [[tcp-congestion-control]] | concept | tcp, congestion, aimd, slow-start, network | 2026-06-03 | TCP Congestion Control은 TCP 송신자가 congestion window(cwnd)를 동적으로 조정하여 네트... |
| [[tcp-error-control]] | concept | tcp, error-control, ack, duplicate-ack, fast-retransmit, retransmission | 2026-06-03 | TCP Error Control은 체크섬(Checksum), 확인 응답(Acknowledgment), 타임아웃(Timeout)... |
| [[tcp-flow-control]] | concept | tcp, flow-control, rwnd, buffer, producer-consumer | 2026-06-03 | TCP Flow Control은 수신 측 응용 프로그램이 데이터를 처리하는 속도에 맞추어 송신자의 전송 속도를 조절하는 end... |
| [[tcp-header]] | concept | tcp, header, protocol, networking, segment | 2026-06-03 | TCP Header는 TCP segment의 앞부분에 위치하는 제어 정보 블록으로, 기본 크기는 20바이트이며 옵션 포함 시 ... |
| [[tcp-reset-segment]] | concept | tcp, reset, rst, connection, abort | 2026-06-03 | TCP에서 참조 연결(reference connection)에 올바르지 않은 세그먼트가 도착했을 때 전송되는 특수 제어 세그먼... |
| [[tcp-retransmission-timeout]] | concept | tcp, rto, rtt, ewma, retransmission, karn, exponential-backoff | 2026-06-03 | TCP Retransmission Timeout (RTO)는 TCP 송신자가 전송한 세그먼트에 대한 ACK를 기다리는 최대 시... |
| [[tcp-server-operation]] | concept | tcp, server, connection-queue, port, backlog, socket | 2026-06-03 | TCP 서버가 들어오는 연결을 처리하는 방식의 총체. 포트 번호 관리, 4-tuple 기반의 동시 연결 식별, 연결 큐(inc... |
| [[tcp-sliding-window]] | concept | tcp, sliding-window, sequence-number, buffer, snd-una, snd-nxt, rcv-nxt | 2026-06-03 | TCP Sliding Window는 TCP가 신뢰성 있는 데이터 전송을 구현하기 위해 사용하는 바이트 지향(byte-orien... |
| [[tcp-state-machine]] | concept | tcp, state-machine, finite-state-machine, connection, transition | 2026-06-03 | TCP의 연결 수립, 데이터 전송, 연결 종료 단계에서 발생하는 모든 이벤트를 추적하기 위해 TCP를 유한 상태 기계(Fini... |
| [[tcp-three-way-handshake]] | concept | tcp, connection, handshake, network, socket | 2026-06-03 | TCP 연결을 수립하기 위해 클라이언트와 서버가 세 개의 세그먼트(SYN → SYN+ACK → ACK)를 교환하는 절차. 연결... |
| [[tcp-timers]] | concept | tcp, timer, network, flow-control | 2026-06-03 | TCP는 연결 관리와 신뢰성 있는 데이터 전송을 위해 네 가지 타이머를 사용한다: Retransmission Timer, Pe... |
| [[tcp-timestamps]] | concept | tcp, timestamps, rtt, paws, options, sequence-number | 2026-06-03 | 각 TCP 세그먼트에 타임스탬프 값을 포함시키는 옵션(RFC 1323). 두 가지 목적으로 사용된다: (1) RTT의 정밀한 ... |
| [[tcp-window-scale]] | concept | tcp, window, flow-control, options, bandwidth-delay-product, performance | 2026-06-03 | TCP의 수신 윈도우(receive window) 광고 크기를 16비트 이상으로 확장하기 위한 TCP 옵션(RFC 1323).... |
| [[tcp-ip-architecture]] | concept | networking, tcp-ip, internet, layering, hourglass, end-to-end, rfc | 2026-06-03 | TCP/IP 아키텍처는 인터넷의 기반이 되는 프로토콜 스택 아키텍처로, RFC 1122에서 정의한 인터넷 아키텍처를 구현한다.... |
| [[third-normal-form]] | concept | database, normalization, 3nf, functional-dependency | 2026-06-01 | 3NF(Third Normal Form)는 관계 스키마 R이 FD 집합 F에 대해 만족해야 하는 정규형으로, F+에 속하는 모... |
| [[time-complexity-classes]] | concept | algorithm, complexity, time-complexity, hierarchy | 2026-06-02 | 시간 복잡도 클래스(time complexity class)는 알고리즘의 실행 시간이 입력 크기 n에 대해 어떤 함수적 관계를... |
| [[time-wait-state]] | concept | tcp, connection, state, timewait, 2msl, socket | 2026-06-03 | TCP active close를 수행한 엔드포인트가 최종 ACK를 전송한 후 2×MSL(Maximum Segment Lifet... |
| [[timeboxing]] | concept | project-management, scheduling, agile, scope | 2026-06-04 | Timeboxing은 프로젝트에 고정된 마감 기한(timebox)을 설정하고, 그 기한 내에 완수 가능한 핵심·필수 기능에만 ... |
| [[topological-sorting]] | concept | graph, dag, algorithm, topological-order, dfs | 2026-06-02 | 위상 정렬(Topological Sorting)은 DAG(Directed Acyclic Graph)의 정점들을 topologi... |
| [[transaction-management]] | concept | transaction, atomicity, consistency, concurrency, database | 2026-06-01 | Transaction Management는 데이터베이스에서 일련의 연산이 원자적(atomic)으로 수행되도록 보장하는 메커니즘... |
| [[transitive-closure]] | concept | graph, digraph, reachability, dynamic-programming | 2026-06-01 | 방향 그래프(digraph) G가 주어졌을 때, G의 **transitive closure** G\*는 G와 동일한 정점 집합... |
| [[transport-layer-demultiplexing]] | concept | transport-layer, demultiplexing, multiplexing, tcp, udp, networking, socket | 2026-06-03 | Transport Layer Demultiplexing(역다중화)은 수신 호스트가 도착한 transport-layer segm... |
| [[tree-data-structure]] | concept | tree, data-structure, hierarchical, linked-structure | 2026-06-02 | Tree는 노드(node)들이 부모-자식(parent-child) 관계로 연결된 계층적(hierarchical) 추상 자료구조... |
| [[tree-traversal]] | concept | traversal, tree, binary-tree, algorithm, recursion, preorder, postorder, inorder | 2026-06-02 | Tree Traversal(트리 순회)은 트리의 모든 노드를 정해진 순서에 따라 빠짐없이 방문하는 알고리즘이다. 방문 순서에 ... |
| [[trinode-restructuring]] | concept | tree, avl-tree, rotation, balancing, algorithm | 2026-06-02 | Trinode Restructuring은 AVL 트리에서 불균형이 발생했을 때 세 노드 (x, y, z)를 재배치하여 높이 균... |
| [[use-case]] | concept | use-case, requirements, systems-analysis, actor, event-driven | 2026-06-01 | Use Case는 시스템이 외부 환경과 상호작용하는 방식을 표현하는 요구사항 분석 도구다. 외부 사용자(actor)가 특정 이... |
| [[use-case-formats]] | concept | use-case, casual-format, fully-dressed, requirements, systems-analysis | 2026-06-01 | Use Case Format은 use case를 문서화하는 상세 수준(level of detail)과 구조를 결정하는 작성 방... |
| [[vlsm]] | concept | networking, IP, subnet, addressing | 2026-06-03 | Variable-Length Subnet Mask (VLSM, RFC1878)은  의 확장으로, 동일한 상위 네트워크 블록 내... |
| [[vector-array-list]] | concept | vector, array-list, sequence, data-structure, dynamic-array | 2026-06-02 | Vector(Array List)는 n개의 요소를 선형 순서로 저장하고, 인덱스(index)를 통해 임의 접근(random a... |
| [[vector-adt]] | concept | vector, array-list, adt, data-structure, index | 2026-06-02 | Vector(또는 Array List) ADT는 배열의 개념을 확장하여 객체의 시퀀스를 저장하는 추상 자료형이다. 각 요소는 ... |
| [[vibe-coding]] | concept | coding-paradigm, llm, prompt-engineering | 2026-05-26 | 자연어로 목표와 제약을 전달하면 LLM이 코드를 생성하는 개발 패러다임. 개발자는 코드 구문을 직접 작성하는 대신 청사진 설계... |
| [[vlan]] | concept | network, link-layer, vlan, switching, isolation, 802.1q | 2026-06-03 | VLAN(Virtual Local Area Network)은 단일 물리적 스위치 인프라 위에 여러 가상 LAN을 구성하는 기술... |
| [[weak-entity-set]] | concept | database, er-model, weak-entity, primary-key, discriminator | 2026-06-01 | Weak entity set은 자체적인 primary key를 가지지 않는 entity set이다. 그 존재가 identify... |
| [[array-based-stack]] | entity | stack, array, data-structure, implementation, cpp | 2026-06-02 | Array-based Stack은  ADT를 고정 크기 배열(array)로 구현한 방식이다. 배열 S와 top 인덱스 t(초기... |
| [[b-plus-tree]] | entity | b-plus-tree, index, tree, data-structure, database | 2026-06-01 | B+-Tree는 데이터베이스 인덱싱을 위한 자기 균형 트리(self-balancing tree) 자료구조로, 1970년 Rud... |
| [[b-tree]] | entity | b-tree, index, tree, data-structure, database | 2026-06-01 | B-Tree는 1970년 Rudolf Bayer와 E. McCreight가 발표한 "Organization and Mainte... |
| [[boyer-moore-algorithm]] | entity | algorithm, string, pattern-matching, boyer-moore, heuristic | 2026-06-01 | Boyer-Moore 알고리즘은 Robert Boyer와 J Strother Moore가 고안한 문자열 매칭 알고리즘이다. 두... |
| [[brute-force-string-matching]] | entity | algorithm, string, pattern-matching, brute-force | 2026-06-01 | Brute-Force Pattern Matching(완전 탐색 패턴 매칭)은 패턴 P를 텍스트 T의 모든 가능한 이동(shif... |
| [[claude-code]] | entity | cli-tool, ai-agent, anthropic, coding-assistant | 2026-05-26 |  |
| [[codex-cli]] | entity | cli-tool, ai-agent, openai, coding-assistant | 2026-05-26 |  |
| [[database-management-system]] | entity | dbms, database, storage-manager, query-processor, transaction | 2026-06-01 | DBMS(Database Management System)는 데이터베이스를 저장·관리하고 접근을 용이하게 하는 소프트웨어다. ... |
| [[dijkstras-algorithm]] | entity | algorithm, graph, shortest-path, greedy | 2026-06-02 | Dijkstra's Algorithm은 비음수 가중치(nonnegative weights)를 갖는 가중 그래프에서 단일 출발점... |
| [[ethernet]] | entity | ethernet, lan, csma-cd, ieee-802-3, networking, wired | 2026-06-03 | Ethernet은 현재 가장 지배적인 유선 LAN 기술이다. 1970년대 Bob Metcalfe 등이 Xerox PARC에서 ... |
| [[fastmcp]] | entity | mcp, framework, python, tool-server, agent | 2026-06-04 | FastMCP는 (Model Context Protocol) 서버를 Python으로 빠르게 구축할 수 있도록 설계된 프레임워크... |
| [[floyd-warshall-algorithm]] | entity | algorithm, dynamic-programming, graph, shortest-path, transitive-closure | 2026-06-01 | Floyd-Warshall 알고리즘은 방향 그래프(digraph)에서 동적 프로그래밍(dynamic programming)을 ... |
| [[gemini-cli]] | entity | cli-tool, ai-agent, google, coding-assistant | 2026-05-26 |  |
| [[heapsort]] | entity | sort, algorithm, comparison-sort, heap, tree, divide-and-conquer | 2026-06-02 | Heapsort(힙 정렬)는 Heap 자료구조를 이용한 비교 기반 in-place 정렬 알고리즘이다. 모든 원소를 최대 힙(m... |
| [[ieee-802-11]] | entity | wifi, wireless, lan, ieee-802-11, csma-ca, networking, bss, ess | 2026-06-03 | IEEE 802.11은 무선 LAN(WLAN)의 표준 집합이며, Wi-Fi Alliance가 장치 간 상호 운용성을 인증한다.... |
| [[internet]] | entity | internet, isp, tier1, ixp, history, infrastructure, cloud | 2026-06-02 | Internet(대문자 'I')은 전 세계적으로 상호 연결된 ISP(Internet Service Provider)들의 집합으... |
| [[knuth-morris-pratt-algorithm]] | entity | algorithm, string, pattern-matching, kmp, failure-function | 2026-06-01 | Knuth-Morris-Pratt(KMP) 알고리즘은 Donald Knuth, Vaughan Pratt, James Morri... |
| [[kruskals-algorithm]] | entity | algorithm, graph, mst, greedy, disjoint-set | 2026-06-02 | Kruskal's Algorithm은 연결된 무방향 가중 그래프에서 를 구하는 그리디 알고리즘이다. 전체 간선을 가중치 오름차... |
| [[linked-list-based-stack]] | entity | stack, linked-list, data-structure, implementation, cpp | 2026-06-02 | Linked List-based Stack은  ADT를 단일 연결 리스트(singly linked list)로 구현한 방식이다... |
| [[matrix-chain-multiplication]] | entity | algorithm, dynamic-programming, optimization, matrix, combinatorics | 2026-06-01 | Matrix-Chain Multiplication(행렬 체인 곱셈) 알고리즘은 n개의 행렬 A1, A2, ..., An의 곱을... |
| [[mergesort]] | entity | sort, algorithm, comparison-sort, divide-and-conquer | 2026-06-02 | Mergesort(병합 정렬)는  패러다임을 사용하는 비교 기반 정렬 알고리즘이다. 배열을 중간 인덱스를 기준으로 절반씩 재귀... |
| [[postgresql]] | entity | postgresql, rdbms, open-source, database, sql | 2026-06-01 | PostgreSQL은 "세계에서 가장 발전된 오픈소스 데이터베이스"를 표방하는 관계형 DBMS이다. UC Berkeley의 I... |
| [[postgresql-storage]] | entity | postgresql, storage, page, heap, tuple | 2026-06-01 | PostgreSQL은 테이블 데이터를 파일 시스템 상의 파일로 저장하며, 각 파일은 8KB 단위의 page(block)로 분할... |
| [[prims-algorithm]] | entity | algorithm, graph, mst, greedy | 2026-06-02 | Prim's Algorithm은 연결된 무방향 가중 그래프에서 를 구하는 그리디 알고리즘이다. 임의의 시작 정점(root)에서... |
| [[quick-sort]] | entity | sort, algorithm, comparison-sort, divide-and-conquer, randomized | 2026-06-02 | Quick-Sort(퀵 정렬)는  패러다임에 기반한 랜덤화 비교 정렬 알고리즘이다. 임의로 선택한 pivot 원소를 기준으로 ... |
| [[radix-sort]] | entity | sort, algorithm, non-comparison-sort, linear-time, bucket | 2026-06-02 | Radix Sort(기수 정렬)는 키를 직접 비교하지 않고, 키의 각 자릿수(field)를 기준으로 버킷(bucket)에 분배... |
| [[red-black-tree]] | entity | tree, data-structure, balanced-tree, search, algorithm | 2026-06-01 | Red-Black Tree(레드-블랙 트리)는 각 노드에 Red 또는 Black 색상을 부여하는 4가지 속성으로 균형을 자동 ... |
| [[sequential-search]] | entity | algorithm, search, linear-search, array, optimality | 2026-06-01 | Sequential Search(순차 탐색, 선형 탐색)는 배열의 원소를 처음부터 순서대로 목표값 K와 비교하여 탐색하는 알고... |
| [[systems-analyst]] | entity | systems-analysis, role, information-systems, project | 2026-06-01 | Systems Analyst는 정보시스템 개발 프로젝트에서 핵심 역할을 수행하는 직무다. Dennis, Wixom, Roth의... |
| [[tcp]] | entity | tcp, transport-layer, protocol, reliability, networking | 2026-06-03 | TCP(Transmission Control Protocol)는 인터넷 전송 계층(transport layer)의 핵심 프로토... |
| [[traceroute]] | entity | icmp, network, diagnostic, ttl, tool | 2026-06-03 | Traceroute는 패킷이 출발지에서 목적지까지 거치는 경로(hop sequence)와 각 구간의 RTT(Round-Trip... |
| [[tree-cpp-implementation]] | entity | tree, cpp, stl, implementation, linked-structure, iterator | 2026-06-02 | C++ STL `std::list`를 활용하여 일반 트리(general tree)를 구현한 자료구조 구현체이다. `Node` ... |
| [[union-find]] | entity | union-find, disjoint-set, data-structure, algorithm | 2026-06-02 | Union-Find ADT(분리 집합 ADT)는 서로 소(disjoint)인 집합들의 모음을 관리하는 자료 구조다. Union... |
| [[database-evolution]] | synthesis | database, history, big-data, ai, nosql, relational-model | 2026-06-01 | 데이터베이스 기술은 데이터 규모와 활용 패턴의 변화에 따라 순차적으로 진화해왔으며, 관계형 모델이 핵심 기반으로 유지되면서도 ... |
| [[hook-based-determinism]] | synthesis | hook, agent, determinism, automation, reliability | 2026-06-04 | AI 에이전트는 본질적으로 확률적(probabilistic)으로 동작하므로 매 결정마다 틀릴 가능성이 존재한다.  (에이전트 ... |
| [[join-algorithm-comparison]] | synthesis | database, join, algorithm, performance, optimization, cost-model | 2026-06-01 | 데이터베이스의 5가지 주요 join 알고리즘(nested-loop join, block nested-loop join, ind... |
| [[map-implementation-comparison]] | synthesis | map, bst, avl-tree, hash-table, performance, comparison | 2026-06-02 | Map ADT를 구현하는 세 가지 주요 자료구조 — BST, AVL Tree, Hash Table — 는 평균·최악 시간 복잡... |
| [[np-complete-problems]] | synthesis | np-complete, sat, tsp, vertex-cover, reduction, knapsack, hamiltonian | 2026-06-02 | NP-Complete 문제들은 다항 시간 환원(polynomial reduction)의 연쇄를 통해 서로 연결된 구조적 패밀리... |
| [[stack-implementation-comparison]] | synthesis | stack, array, linked-list, comparison, tradeoff, data-structure | 2026-06-02 |  ADT를 구현하는 두 가지 주요 방식—과 —은 모든 연산에서 동일한 O(1) 시간복잡도를 제공하지만, 메모리 관리 방식과 예... |
| [[string-matching-algorithm-comparison]] | synthesis | algorithm, string, pattern-matching, comparison, complexity | 2026-06-01 | 세 가지 주요 문자열 매칭 알고리즘(Brute-Force, KMP, Boyer-Moore)은 이론적 시간복잡도와 실용적 성능 ... |
| [[vector-vs-list]] | synthesis | vector, list, data-structure, comparison, ADT, sequence, time-complexity | 2026-06-02 | Array 기반 Vector와 Doubly linked list 기반 List는 동일한 Sequence ADT를 구현하지만, ... |
| [[vibe-vs-agentic-coding]] | synthesis | coding-paradigm, comparison, decision-framework | 2026-05-26 | Vibe Coding과 Agentic Coding은 연속선 위의 두 점이 아니라 근본적으로 다른 패러다임이다. 작업 규모와 품... |
| [[pipeline-design-patterns]] | synthesis | agent-pattern, pipeline, design, comparison | 2026-05-26 | 멀티 에이전트 파이프라인 설계에서 Sequential, Parallel, Orchestrator-Workers, Ping-Po... |
| [[sorting-algorithm-comparison]] | synthesis | sort, algorithm, comparison, analysis, complexity | 2026-06-02 | 비교 기반 정렬 알고리즘들은 Ω(n log n)의 공통 하한을 가지지만, worst-case 보장 여부, 공간 효율, 구현 복... |

---

## Statistics

- **Total pages:** 263
- **Concepts:** 219
- **Entities:** 33
- **Syntheses:** 11
- **Open contradictions:** 0
- **Last updated:** 2026-06-04
