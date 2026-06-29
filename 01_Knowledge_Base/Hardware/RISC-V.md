# RISC-V

## Evolution of the concept

RISC-V entered the EdgeAI hardware landscape as an open, royalty-free instruction set alternative to proprietary cores (notably ARM's Cortex-M and Cortex-A families), promising freedom from vendor lock-in and an open software/tooling ecosystem. The GAP-8 SoC was an early, commercially-oriented demonstration that a fully programmable RISC-V multi-core cluster could be paired with a dedicated CNN accelerator and an extremely low-power always-on domain, making it viable for battery-constrained IoT end-nodes. Since then, the direction has broadened toward RISC-V vector extensions and toolchain efforts (such as migrating existing ARM NEON-optimized code to RISC-V Vector Extensions) aimed at closing the software-maturity gap with the more established ARM ecosystem.

## Key papers

[[2018_Flamand_GAP8]] — fabricated 8-core RISC-V SoC with integrated CNN accelerator and 30 µW sleep-power always-on domain, demonstrating open-ISA viability for battery-powered IoT edge nodes.

## Open problems

How mature is the current RISC-V compiler/toolchain ecosystem (TVM, MLIR-based tooling) for deploying non-CNN EdgeAI models (e.g. small transformers) compared to the equivalent ARM ecosystem? How do fixed-function RISC-V CNN accelerators (GAP-8-style) compare in energy-per-inference to more recent flexible RISC-V vector-extension accelerators?

## Research ideas

Energy-per-inference benchmark of GAP-8-class RISC-V hardware against Cortex-M+CMSIS-NN for the same EdgeAI task; evaluation of current RISC-V vector-extension tooling maturity for deploying non-CNN models.

## Possible thesis topics

Benchmarking RISC-V vector-extension accelerators versus fixed-function CNN accelerators (GAP-8-style) on the same modern EdgeAI workload; porting a [[microTVM_TVM]] or [[MLIR]]-based deployment pipeline to a RISC-V target and measuring tooling maturity against the equivalent ARM path.

## Links

[[Cortex-M]], [[microTVM_TVM]], [[Quantization]], [[NAS]]
