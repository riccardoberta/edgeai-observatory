# Cortex-A

## Evolution of the concept

ARM Cortex-A is the application-processor core family that powers smartphones, tablets, and higher-end edge devices — distinct from the microcontroller-class [[Cortex-M]] family covered elsewhere in this taxonomy. Cortex-A SoCs typically pair general-purpose CPU cores with a GPU and, increasingly, a dedicated NPU/DSP block, making "EdgeAI on Cortex-A" fundamentally a heterogeneous-compute deployment problem rather than a single-core optimization problem. The field's understanding has evolved from early CPU-only mobile inference toward routing workloads across CPU, GPU, and NPU through frameworks like Android's NNAPI, with cross-vendor benchmarking (AI Benchmark) revealing both rapid year-over-year gains in mobile NPU throughput and persistent fragmentation in how well that hardware capability is actually exposed to applications.

## Key papers

[[2019_Ignatov_AIBenchmarkSmartphones]] — standardized, cross-vendor benchmark of deep learning inference across nearly all major Cortex-A mobile SoCs, documenting the heterogeneous CPU/GPU/NPU compute landscape and the Android ML deployment pipeline.

## Open problems

How much of the available Cortex-A-class heterogeneous compute (NPU/DSP/GPU) do general-purpose cross-platform runtimes ([[ONNX_Runtime]], TensorFlow Lite for mobile) actually exploit compared to vendor-specific delegates? How does energy efficiency on Cortex-A-class hardware compare, for the same model, to dedicated NPU/FPGA/RISC-V accelerator paths covered elsewhere in this taxonomy?

## Research ideas

A current-generation replication of the AI Benchmark methodology extended to non-vision EdgeAI tasks (keyword spotting, HAR, biosignals) relevant to our [[Applications]] taxonomy, to test whether Cortex-A heterogeneous compute gains generalize beyond the vision workloads it was originally measured on.

## Possible thesis topics

Comparative benchmark of ONNX Runtime versus native vendor delegates on the same Cortex-A SoC for a fixed EdgeAI task; energy-per-inference comparison between a Cortex-A mobile SoC and a Cortex-M+CMSIS-NN or NPU-based deployment for an equivalent model.

## Links

[[Cortex-M]], [[NPU]], [[ONNX_Runtime]], [[Vision]]
