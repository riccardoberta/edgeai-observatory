# Energy-Efficient Dual-Core RISC-V Architecture for Edge AI Acceleration with Dynamic MAC Unit Reuse

**Full citation:** Tanase, C.A. (2026). Energy-Efficient Dual-Core RISC-V Architecture for Edge AI Acceleration with Dynamic MAC Unit Reuse. *Computers*, 15(4), 219. DOI: 10.3390/computers15040219

**PDF:** [MDPI (open access)](https://www.mdpi.com/2073-431X/15/4/219)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page plus WebSearch cross-reference. Author affiliation: Faculty of Electrical Engineering and Computer Science, Ștefan cel Mare University of Suceava, Romania.

**Linked concepts:** [[NPU]], [[RISC-V]]

## Abstract summary

Proposes a dual-core RISC-V architecture for edge AI acceleration in which the two cores compete for a single shared Multiply-Accumulate (MAC) unit and a shared external memory subsystem, governed by a channel-based arbitration mechanism with CPU-priority semantics; each core keeps private instruction/data caches. A tightly coupled Neural Processing Unit (NPU) executes CONV, GEMM, and POOL operations opportunistically whenever the shared MAC unit is free, and three-level dynamic frequency scaling (100/200/400 MHz) is applied to the MAC unit to accelerate CNN workloads when idle cycles are available.

## Research problem

Dedicated per-core NPU or DSP units in multi-core edge microcontrollers duplicate expensive MAC hardware even though the cores rarely saturate it simultaneously, wasting area and static power in area/power-constrained edge devices; a design is needed that lets multiple RISC-V cores share one MAC resource for both general-purpose and CNN-acceleration duties without one core starving the other.

## Key idea

Time-multiplex a single MAC unit between two RISC-V cores via a FIFO-based, priority-aware arbitration channel, and let the tightly coupled NPU "opportunistically" claim otherwise-idle MAC cycles for CNN inference (CONV/GEMM/POOL), combined with three-level dynamic frequency scaling on the shared MAC unit to trade energy against throughput as workload demand changes.

## Technical contribution

A channel-based, CPU-priority MAC-sharing arbitration scheme for dual-core RISC-V edge SoCs; a tightly coupled NPU design that reuses the shared MAC datapath rather than instantiating a separate accelerator array; three-level DFS (100/200/400 MHz) applied specifically to the shared MAC unit as an energy/throughput control knob.

## Experimental methodology

Architectural implementation and evaluation of the dual-core RISC-V design with the shared MAC/NPU subsystem, characterizing arbitration behavior, MAC-unit utilization/idle-cycle recovery by the NPU, and energy consumption across the three DFS levels under representative CNN inference workloads (per the MDPI abstract).

## Results

The shared-MAC, opportunistic-NPU design and DFS scheme reduce silicon area and static power relative to per-core dedicated accelerators while sustaining CNN inference throughput by exploiting idle MAC cycles; DFS provides a tunable energy/performance operating range across the three frequency levels (per the published abstract — full quantitative figures not independently re-derived here).

## Comparison with the state of the art

Contrasts with the more common per-core dedicated-NPU pattern seen in most multi-core edge SoCs (and with the standalone-array approach exemplified by [[2017_Chen_Eyeriss]]); instead of maximizing local reuse within one accelerator array, this design maximizes utilization of one shared MAC resource across cores and duties (general-purpose compute and CNN inference).

## Strengths

Directly addresses area/power duplication in multi-core edge AI SoCs, a practical concern often glossed over in single-core accelerator papers; combines architectural sharing with a classic power-management technique (DFS) rather than proposing either in isolation; open, RISC-V-based design consistent with the Observatory's interest in open ISAs for edge AI.

## Weaknesses

As an MDPI 2026 publication read at abstract/article-page level (not independently benchmarked against a broader accelerator suite in this record), quantitative comparisons against dedicated per-core NPU baselines and against other MAC-sharing schemes in the literature are not detailed here; single-benchmark-class evaluation (CNN inference) leaves open how well the arbitration scheme generalizes to mixed workloads with different core-priority patterns.

## Limitations

Two-core scope only; unclear how the channel-based arbitration scheme scales to more than two cores contending for one shared MAC, which would be relevant for larger edge SoCs.

## Open questions

Does the CPU-priority arbitration policy introduce worst-case latency bounds acceptable for real-time inference, or only average-case throughput gains? How does the design compare quantitatively, on the same workload and process node, against a per-core dedicated-NPU baseline and against [[2017_Chen_Eyeriss]]-style Row-Stationary dataflow accelerators?

## Possible extensions

Scaling the shared-MAC arbitration scheme to more than two cores; combining the opportunistic-NPU idea with quantization/sparsity-aware MAC scheduling; a head-to-head silicon or cycle-accurate comparison against dedicated per-core NPU designs on identical CNN benchmarks.

## Relevance to our research

A recent (2026), fully open-access example of RISC-V/NPU co-design for edge AI, directly relevant to the Observatory's [[NPU]] and [[RISC-V]] concept nodes and to the open-ISA thread running through the Hardware taxonomy branch; useful as a current anchor when assessing how open-ISA cores are integrating tightly coupled AI acceleration.

## Possible thesis topics

Quantitative benchmarking of MAC-sharing arbitration policies (priority-based vs. round-robin vs. deadline-aware) for multi-core RISC-V edge AI SoCs, measuring the throughput/fairness/energy trade-off as core count scales beyond two.

## Possible collaborations

RISC-V edge-SoC design groups and open-hardware NPU projects (e.g. groups behind X-HEEP, Marsellus, and similar open RISC-V AI-IoT end-node SoCs referenced in adjacent literature).

## Links to related papers

[[2017_Chen_Eyeriss]]
