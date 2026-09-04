# Cortex-A

Arm Cortex-A is the application-processor CPU core family that powers smartphones, tablets, and higher-end edge devices — distinct from the microcontroller-class [[Cortex-M]] family, and capable of running a full operating system. Cortex-A SoCs (systems-on-chip) typically pair general-purpose CPU cores with a GPU and, increasingly, a dedicated NPU/DSP block, making "EdgeAI on Cortex-A" fundamentally a heterogeneous-compute deployment problem — deciding which part of the chip should run which part of a workload — rather than a single-core optimization problem.

## Evolution of the concept

The heterogeneous-compute pattern that defines modern Cortex-A SoCs has its own precursor at the CPU level: Arm's big.LITTLE design (Greenhalgh, 2011) pairs a high-performance core cluster (Cortex-A15) with a power-efficient one (Cortex-A7), migrating workloads between them depending on demand. This is the architectural precedent for the CPU/GPU/NPU heterogeneous task-routing problem EdgeAI on Cortex-A now faces.

The field's understanding of that routing problem has evolved from early CPU-only mobile inference toward routing workloads across CPU, GPU, and NPU through frameworks like Android's NNAPI. Ignatov et al.'s AI Benchmark provides cross-vendor benchmarking of deep learning inference across nearly all major Cortex-A mobile SoCs, revealing both rapid year-over-year gains in mobile NPU throughput and persistent fragmentation in how well that hardware capability is actually exposed to applications.

The large-language-model era has sharpened this heterogeneous-compute question considerably. Chen et al. (2025) characterize how GPU and NPU compute, and shared SoC memory bandwidth, behave under real LLM inference, and design HeteroInfer, an engine that splits work across both accelerators by inference phase (compute-bound "prefill" versus bandwidth-bound "decode"), reporting 1.34x–6.02x speedups over single-accelerator engines — a concrete, current update to the AI-Benchmark-era picture of how much heterogeneous Cortex-A compute actually gets exploited. Park et al. (2023) provide a silicon-validated example of the hardware side of this trend: a 4-nanometer mobile NPU, deployed in flagship SoCs alongside Cortex-A cores, using a unified multi-precision datapath to handle the workload diversity of real mobile AI applications.

## Key papers

[[2011_Greenhalgh_bigLITTLE]] — introduces heterogeneous-core task migration between high-performance and power-efficient CPU clusters, the architectural precedent for today's CPU/GPU/NPU workload routing on Cortex-A SoCs.

[[2019_Ignatov_AIBenchmarkSmartphones]] — standardized, cross-vendor benchmark of deep learning inference across nearly all major Cortex-A mobile SoCs, documenting the heterogeneous CPU/GPU/NPU compute landscape and the Android machine-learning deployment pipeline.

[[2025_Chen_HeteroInfer]] — phase-aware GPU/NPU heterogeneous-parallelism engine for mobile LLM inference, with a hardware characterization of compute/bandwidth bottlenecks underlying the design.

[[2023_Park_MultiModeNPU]] — silicon-validated 4-nanometer mobile NPU paired with Cortex-A cores in flagship SoCs, using a unified multi-precision datapath to handle the workload diversity of real mobile AI applications.

## Open problems

How much of the available Cortex-A-class heterogeneous compute (NPU/DSP/GPU) do general-purpose cross-platform runtimes ([[ONNX_Runtime]], TensorFlow Lite for mobile) actually exploit, compared to vendor-specific software paths? How does energy efficiency on Cortex-A-class hardware compare, for the same model, to dedicated NPU/FPGA/RISC-V accelerator paths covered elsewhere in this taxonomy?

## Research ideas

A current-generation replication of the AI Benchmark methodology extended to non-vision EdgeAI tasks (keyword spotting, HAR, biosignals), to test whether Cortex-A heterogeneous-compute gains generalize beyond the vision workloads it was originally measured on.

## Possible thesis topics

A comparative benchmark of ONNX Runtime versus native vendor delegates on the same Cortex-A SoC for a fixed EdgeAI task. An energy-per-inference comparison between a Cortex-A mobile SoC and a Cortex-M+CMSIS-NN or NPU-based deployment for an equivalent model.

## Links

[[Cortex-M]], [[NPU]], [[ONNX_Runtime]], [[Vision]]
