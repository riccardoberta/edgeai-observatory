# RISC-V

RISC-V is an open, royalty-free instruction-set architecture (ISA) — as opposed to Arm's proprietary one — increasingly used as the basis for custom edge AI silicon because vendors can extend it freely with their own instructions.

## Evolution of the concept

RISC-V's case for existing at all predates any EdgeAI-specific use case: Asanović and Patterson's "Instruction Sets Should Be Free: The Case For RISC-V" (2014) lays out the foundational argument that proprietary, royalty-bearing instruction sets impose unnecessary licensing and fragmentation costs on hardware innovation, and that a free, modular, open ISA removes that barrier — the argument that, once accepted by chip designers, made an open alternative to Arm's Cortex-M/Cortex-A licensing model possible in the first place.

The GAP-8 SoC was an early, commercially-oriented demonstration that a fully programmable RISC-V multi-core cluster could be paired with a dedicated CNN accelerator and an extremely low-power always-on domain, making it viable for battery-constrained IoT end-nodes. Since then, the direction has broadened toward RISC-V vector extensions and toolchain efforts — such as migrating existing Arm NEON-optimized code to RISC-V Vector Extensions — aimed at closing the software-maturity gap with the more established Arm ecosystem.

Two more recent threads push this broadening further. Spatz (Perotti et al., 2023) shows that a compact, open-source RISC-V Vector Extension core can be clustered around a shared scratchpad memory to reach peak energy efficiency with a vector register file as small as 2 KiB — a general-purpose alternative to GAP-8's fixed-function CNN accelerator. MARVEL (Kumar M et al., 2025) automates the traditionally manual hardware/compiler co-design step itself, generating model-class-aware custom RISC-V ISA extensions directly from a high-level neural-network profile.

XpulpNN (Garofalo, Tagliavini, Conti, Benini, and Rossi, 2021), from the same Bologna research group behind GAP-8 and Spatz, extends the RISC-V ISA itself with 4-bit and 2-bit SIMD (single-instruction-multiple-data) instructions plus a fused dot-product/load execution paradigm, reporting near-linear (not sub-linear) speedup with reduced precision — directly answering the question of whether the ISA itself, not just the surrounding software stack, can support quantized-model deployment efficiently.

## Key papers

[[2014_Asanovic_RISCVCaseForFree]] — the founding argument for an open, royalty-free ISA, the precondition that makes RISC-V-based EdgeAI hardware (like GAP-8 below) viable as a vendor-lock-in-free alternative to Arm.

[[2018_Flamand_GAP8]] — fabricated 8-core RISC-V SoC with an integrated CNN accelerator and 30 μW sleep-power always-on domain, demonstrating open-ISA viability for battery-powered IoT edge nodes.

[[2023_Perotti_Spatz]] — compact, open-source RISC-V Vector Extension core clustered around a shared scratchpad, reaching peak energy efficiency with a 2 KiB vector register file.

[[2025_KumarM_MARVEL]] — automated end-to-end framework generating model-class-aware custom RISC-V ISA extensions and compiler support directly from a neural-network model profile.

[[2021_Garofalo_XpulpNN]] — RISC-V ISA extended with 4-bit/2-bit SIMD instructions and a fused dot-product/load execution paradigm, achieving near-linear speedup for quantized neural-network inference.

## Open problems

How mature is the current RISC-V compiler/toolchain ecosystem (TVM, MLIR-based tooling) for deploying non-CNN EdgeAI models, such as small transformers, compared to the equivalent Arm ecosystem? How do fixed-function RISC-V CNN accelerators (GAP-8-style) compare in energy-per-inference to more recent flexible RISC-V vector-extension accelerators?

## Research ideas

An energy-per-inference benchmark of GAP-8-class RISC-V hardware against Cortex-M+CMSIS-NN for the same EdgeAI task. An evaluation of current RISC-V vector-extension tooling maturity for deploying non-CNN models.

## Possible thesis topics

Benchmarking RISC-V vector-extension accelerators versus fixed-function CNN accelerators (GAP-8-style) on the same modern EdgeAI workload. Porting a [[microTVM_TVM]] or [[MLIR]]-based deployment pipeline to a RISC-V target and measuring tooling maturity against the equivalent Arm path.

## Links

[[Cortex-M]], [[microTVM_TVM]], [[Quantization]], [[NAS]]
