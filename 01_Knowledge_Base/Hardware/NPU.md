# NPU (Neural Processing Unit)

An NPU is a chip or chip block purpose-built to accelerate neural-network inference — matrix multiplication at high throughput and low power — increasingly included alongside the CPU in modern edge SoCs, from mobile Cortex-A chips (see [[Cortex-A]]) to dedicated edge devices such as Google's Coral/Edge TPU products.

## Evolution of the concept

NPUs emerged as fixed-function, ASIC-class (application-specific integrated circuit) accelerators specifically designed for neural-network inference. The line starts with Chen et al.'s DianNao (2014), the first widely-cited small-footprint ASIC accelerator design specifically for machine-learning workloads, which established the basic architectural recipe — dedicated on-chip buffers and a fixed-function arithmetic datapath, to avoid the memory-bandwidth and energy cost of general-purpose CPU/GPU execution — that essentially all later NPU designs build on.

The following year, Chen et al.'s Eyeriss (2017) reframed the design problem around *data-movement energy* rather than raw compute, introducing the Row-Stationary dataflow and a general dataflow taxonomy (weight-stationary, output-stationary, no-local-reuse, row-stationary — different strategies for which values stay fixed in a compute unit's local memory while others stream past). This taxonomy became the standard vocabulary for reasoning about accelerator energy efficiency across the memory hierarchy, a framing later NPU papers, including hardware/software co-design work, implicitly build on. Sze, Chen, Yang, and Emer's tutorial and survey (2017) — by the same MIT lead authors behind Eyeriss, and the single most-cited reference in the entire field — presents this same dataflow taxonomy and the full efficient-DNN-processing design space at teaching depth.

Early evaluation of NPU hardware relied largely on vendor-reported peak-performance figures. The field's understanding deepened substantially with large-scale empirical characterization studies: Yazdanbakhsh et al. swept roughly 423,000 CNN variants across real Edge TPU hardware, surfacing interpretable microarchitectural bottlenecks and enabling learned performance/energy estimators that can substitute for exhaustive on-device measurement — a capability directly useful for hardware-aware neural architecture search (see [[NAS]]).

Recent industrial designs show the field converging on hardware/software co-design as the key lever beyond raw peak-throughput scaling. Samsung's 4-nanometer flagship-mobile NPU (Park et al., 2023) tackles workload-precision diversity with a unified multi-precision datapath plus hardware-utilization-aware scheduling. NXP's eIQ Neutron (Bamberg et al., 2025) attacks the same general utilization problem from the compiler side, using constrained-programming-based scheduling co-designed with a flexible NPU datapath, reaching an average 1.8x (peak 4x) speedup over a comparable embedded NPU/compiler stack at equal peak throughput and memory.

A 2026 open-hardware example, Tanase's dual-core RISC-V edge-AI architecture, applies the same era's utilization-maximizing philosophy at a smaller scale: rather than a dedicated per-core NPU, two RISC-V cores share a single multiply-accumulate unit through priority-based arbitration, with a tightly coupled NPU opportunistically claiming idle cycles for CNN inference — evidence that the shared/opportunistic-resource idea from mobile-class NPU scheduling is now reaching lightweight, open-instruction-set edge cores.

## Key papers

[[2014_Chen_DianNao]] — the foundational fixed-function neural-network accelerator ASIC architecture, establishing the dedicated-buffer/fixed-datapath design pattern that essentially all subsequent NPUs (including mobile and edge NPUs) descend from.

[[2017_Chen_Eyeriss]] — silicon-validated 65 nm CNN accelerator introducing the Row-Stationary dataflow and a general dataflow taxonomy, establishing data-movement energy (not raw compute) as the central NPU design metric.

[[2017_Sze_EfficientProcessingDNNTutorialSurvey]] — the field's single most-cited reference, a comprehensive tutorial covering DNN hardware fundamentals through the full dataflow taxonomy, by the same MIT authors behind Eyeriss.

[[2021_Yazdanbakhsh_EdgeTPUEvaluation]] — large-scale empirical characterization of Edge TPU accelerators across roughly 423,000 CNN variants, producing microarchitectural insights and learned latency/energy estimators.

[[2023_Park_MultiModeNPU]] — silicon-validated 4-nanometer mobile NPU with a unified multi-precision datapath and hardware-utilization-aware scheduling for an 8K multiply-accumulate array.

[[2025_Bamberg_eIQNeutron]] — NPU/compiler co-design using constrained-programming-based scheduling, reaching 1.8x average (4x peak) speedup over a comparable embedded NPU/compiler stack.

[[2019_Ignatov_AIBenchmarkSmartphones]] — vendor-neutral benchmark suite covering mobile NPUs/AI accelerators across major commercial Cortex-A SoCs, giving an apples-to-apples view that complements single-vendor characterization studies.

[[2025_Chen_HeteroInfer]] — heterogeneous GPU+NPU parallel execution for on-device LLM inference, splitting compute-bound "prefill" and bandwidth-bound "decode" phases across both accelerators on shared SoC memory.

[[2026_Absar_HexagonMLIR]] — MLIR-based compilation stack targeting Hexagon NPUs, reusing MLIR's dialect/lowering infrastructure instead of a bespoke NPU toolchain.

[[2026_Bryngelson_AppleNeuralEngine]] — reverse-engineered architecture, programming model, and measured roofline (compute ceiling, bandwidth ceiling, dispatch-latency floor, energy efficiency) of Apple's Neural Engine across the A11–A18/M1–M5 chip families, since Apple publishes no official specification.

[[2026_Tanase_DualCoreRISCVEdgeAI]] — open, silicon-agnostic dual-core RISC-V edge-AI architecture sharing a single multiply-accumulate unit across cores via priority-based arbitration, with a tightly coupled NPU opportunistically claiming idle cycles for CNN inference.

## Open problems

How well do learned latency/energy estimators generalize to non-CNN architectures (small transformers, RNNs) now common in TinyML research? How do Edge TPU's microarchitectural bottlenecks compare to other NPU families (Arm Ethos, CEVA NeuPro) on the same model set — is there a generalizable theory of NPU bottlenecks, or is it largely vendor-specific?

## Research ideas

Building an analogous large-scale performance-characterization study for a different NPU family (for example Arm Ethos-U, used alongside Cortex-M) to test the generality of the learned-estimator approach.

## Possible thesis topics

Extending Edge-TPU-style empirical characterization to non-CNN model families. Using learned NPU performance proxies as a fast hardware-aware fitness function inside a [[NAS]] search loop.

## Links

[[NAS]], [[Cortex-A]], [[FPGA]], [[RISC-V]]
