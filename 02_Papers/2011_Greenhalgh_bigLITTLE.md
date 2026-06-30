# big.LITTLE Processing with ARM Cortex-A15 & Cortex-A7

**Full citation:** Greenhalgh, P. (2011). big.LITTLE Processing with ARM Cortex-A15 & Cortex-A7. *ARM White Paper*. (Vendor source.) https://research.ijcaonline.org/volume119/number1/pxc3903106.pdf

**Linked concepts:** [[Cortex-A]]

## Abstract summary

The author (ARM) describes big.LITTLE, a heterogeneous multi-core processing technology that pairs a high-performance CPU cluster (Cortex-A15, "big") with a power-efficient CPU cluster (Cortex-A7, "LITTLE") of the same instruction-set architecture, and a task-migration mechanism that dynamically moves workloads between the two clusters depending on whether peak performance or energy efficiency matters at a given moment.

## Research problem

Mobile and embedded application processors face conflicting demands: some workloads require peak single-thread performance, while others (often the majority of runtime, e.g. background and idle-adjacent tasks) only need modest performance but should run as energy-efficiently as possible; a single CPU core design cannot be simultaneously optimal for both regimes.

## Key idea

Combine two CPU cluster types — architecturally compatible but micro-architecturally very different (one tuned for peak performance, one for energy efficiency) — on the same chip, and migrate software tasks transparently between the two clusters at the operating-system level depending on current performance/power requirements, so the system as a whole spends most of its time on the efficient cluster and only escalates to the high-performance cluster when needed.

## Technical contribution

The big.LITTLE heterogeneous-cluster architecture itself, including the instruction-set-architecture compatibility design that allows transparent task migration between clusters without application-level changes; the task-migration/scheduling mechanism (and its later evolution toward finer-grained global task scheduling) that decides, at the OS level, which cluster should run a given task.

## Experimental methodology

Presents the big.LITTLE architecture and its task-migration approach, supported by performance/power characterization of the Cortex-A15 ("big") and Cortex-A7 ("LITTLE") clusters individually and in combination, illustrating the energy savings achievable by running typical mobile workloads predominantly on the efficient cluster.

## Results

Demonstrates that combining the two cluster types and intelligently migrating tasks achieves substantially better energy efficiency for typical, performance-variable mobile workloads than either a big-only design (wasteful for light tasks) or a LITTLE-only design (insufficient for peak-performance tasks) could achieve alone.

## Comparison with the state of the art

Introduced heterogeneous-core task migration as a practical alternative to either single-cluster designs or to dynamic voltage/frequency scaling alone, establishing big.LITTLE as the architectural precedent that influenced essentially all later heterogeneous mobile/embedded SoC designs, including those now also routing workloads to dedicated NPUs.

## Strengths

A pragmatic, ISA-compatible heterogeneous design that requires no rewriting of application software to benefit from; clearly demonstrated energy savings for the highly variable workload mixes typical of mobile devices.

## Weaknesses

The original task-migration approach (as described in this 2011 white paper) operates at a coarse cluster-switching granularity and predates more sophisticated global task scheduling across all cores of both clusters simultaneously, which came in subsequent generations of the technology.

## Limitations

Focused on general-purpose CPU workload heterogeneity (performance versus power for typical mobile compute tasks); does not address how a similar heterogeneous-routing philosophy should extend to a third type of compute unit specialized for machine learning inference (i.e. a dedicated NPU), which became a separate, additional component on later Cortex-A SoCs.

## Open questions

How should task/workload routing logic generalize when a chip includes not just big/LITTLE CPU clusters but also a dedicated NPU, GPU, and DSP, each with different performance/power/latency trade-offs for different workload types, including ML inference specifically?

## Possible extensions

Extending heterogeneous task-routing logic to jointly consider CPU big/LITTLE clusters and dedicated ML accelerators (NPUs) on the same SoC, choosing the best compute unit per inference workload rather than only per general-purpose task.

## Relevance to our research

The architectural precedent for today's CPU/GPU/NPU workload routing on Cortex-A SoCs used for EdgeAI inference; essential background for understanding why and how modern Cortex-A-based edge devices route ML workloads across heterogeneous compute units.

## Possible thesis topics

Measuring how an EdgeAI inference workload (e.g. a vision model) is actually routed and scheduled across the big/LITTLE CPU clusters and any available NPU on a modern Cortex-A SoC, and whether the original big.LITTLE task-migration philosophy still describes the observed behavior accurately.

## Possible collaborations

Groups working on heterogeneous SoC scheduling and on operating-system-level support for ML-workload-aware task routing.

## Links to related papers

[[2014_Chen_DianNao]]
