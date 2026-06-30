# Spatz: Clustering Compact RISC-V-Based Vector Units to Maximize Computing Efficiency

**Full citation:** Perotti, M., Riedel, S., Cavalcante, M., Benini, L. (2023). Spatz: Clustering Compact RISC-V-Based Vector Units to Maximize Computing Efficiency. arXiv:2309.10137 (IEEE Transactions on Computer-Aided Design of Integrated Circuits and Systems). https://arxiv.org/abs/2309.10137

**Linked concepts:** [[RISC-V]]

## Abstract summary

The authors (ETH Zurich / University of Bologna) present Spatz, a compact, 64-bit floating-point-capable RISC-V Vector Extension (Zve64d) processing element, and an open-source dual-core clustered vector-processor architecture built around it that shares a single scratchpad memory between cores to maximize compute efficiency at small area/power cost.

## Research problem

General-purpose RISC-V cores lack the data-parallel throughput needed for compute-intensive EdgeAI/DSP kernels, while existing vector-processor designs are often too large or power-hungry for small, embedded computing clusters; a vector unit compact enough for embedded clusters without sacrificing efficiency was missing from the open RISC-V ecosystem.

## Key idea

Build a minimal but standards-compliant RISC-V Vector Extension core (Spatz) and cluster multiple compact instances around a shared scratchpad memory, rather than scaling up a single large vector unit, to get high aggregate efficiency from small, replicable building blocks.

## Technical contribution

The Spatz core itself, implementing RISC-V's Zve64d vector extension subset; a dual-core clustered architecture sharing a scratchpad memory; an open-source RTL implementation (released as part of the PULP ecosystem) enabling reproducible silicon-level evaluation.

## Experimental methodology

Architectural and post-layout evaluation of the Spatz core and dual-core cluster, including a notably small latch-based vector register file (2 KiB), measuring achievable peak energy efficiency and area against the configuration's resource footprint.

## Results

Spatz achieves peak energy efficiency using a vector register file as small as 2 KiB, demonstrating that compact, clustered vector units can deliver competitive efficiency without the area/power cost of larger conventional vector processors.

## Comparison with the state of the art

Targets the same open-ISA, embedded-cluster niche as GAP-8's fixed-function CNN accelerator but takes a general-purpose vector-extension route instead, trading some workload specificity for broader applicability across DSP/EdgeAI kernel types.

## Strengths

Fully open-source RTL (reproducible, extensible by other research groups); explicit, measured area/energy efficiency trade-off analysis rather than only a qualitative architecture description.

## Weaknesses

Evaluated primarily on architectural/kernel-level benchmarks rather than full EdgeAI model workloads, leaving an open question about how the efficiency gains translate to realistic end-to-end inference.

## Limitations

A single dual-core cluster configuration is the main demonstrated design point; scaling behavior to larger clusters is discussed but less thoroughly validated than the core building block itself.

## Open questions

How does Spatz-class vector compute compare, on the same realistic EdgeAI inference workload, to fixed-function RISC-V CNN accelerators like GAP-8 or to ARM's Helium MVE on Cortex-M? How mature is compiler/toolchain support (e.g. via [[microTVM_TVM]] or [[MLIR]]) for automatically targeting Spatz-style vector extensions?

## Possible extensions

End-to-end EdgeAI model benchmarking on a Spatz-based cluster; toolchain work to auto-generate Spatz-targeted kernels from a higher-level compiler stack.

## Relevance to our research

Strengthens the RISC-V hardware entry with a concrete, open-source, silicon-validated vector-extension design, directly relevant to the open question (already flagged in our [[RISC-V]] entry) of how vector-extension accelerators compare to fixed-function designs like GAP-8.

## Possible thesis topics

Benchmarking a Spatz-class RISC-V vector cluster against GAP-8-style fixed-function accelerators and against Cortex-M+Helium on a common quantized EdgeAI model; evaluating compiler-generated kernel performance on Spatz via TVM/MLIR-based tooling.

## Possible collaborations

The PULP platform group (ETH Zurich / University of Bologna) maintaining the open-source Spatz RTL and surrounding RISC-V tooling ecosystem.

## Links to related papers

[[2018_Flamand_GAP8]], [[2014_Asanovic_RISCVCaseForFree]]
