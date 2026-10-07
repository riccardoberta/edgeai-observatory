# Is INT8 Portable? A Cross-Platform Measurement Study of Quantized Inference on Embedded and Automotive Accelerators

**Full citation:** Shin, Y. (2026). Is INT8 Portable? A Cross-Platform Measurement Study of Quantized Inference on Embedded and Automotive Accelerators. arXiv:2609.16085 [cs.AR; cross-listed cs.LG, cs.PF]. KATECH (Korea Automotive Technology Institute), per the artifact repository. Submitted 14 Sep 2026. Open artifact: scripts and 32 measurement reports (github.com/yyshin-katech/embedded-ai-quantization-guide, tag paper1-v1). Preprint, not peer-reviewed at the time of recording.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2609.16085)

**Linked concepts:** [[MLPerf_Tiny]], [[Quantization]], [[NPU]], [[ONNX_Runtime]], [[Cortex-A]]

## Abstract summary

The paper tests the common assumption that an INT8-quantized model is portable across hardware ("quantize once, deploy anywhere"). Holding the model artifact and the quantization scales fixed and varying only the target's integer kernel or instruction set, it measures the same model on ARM CPUs with and without dot-product instructions (Raspberry Pi 5, Jetson AGX Orin CPU, i.MX8M-Nano), an x86 CPU without VNNI, a discrete GPU, the Jetson AGX Orin iGPU and NVDLA cores, and two vendor NPUs (Qualcomm Hexagon HTP and DEEPX DX-M1). It reports that INT8 portability fails on three axes: speed, numerical output, and deployability.

## Research problem

Quantization pipelines and cross-framework runtimes implicitly assume that a quantized graph behaves the same everywhere. For safety-relevant deployments (the paper's framing is automotive) that assume heterogeneous units give consistent outputs, the assumption had not been tested under a controlled design where only the hardware's integer kernel varies.

## Key idea

A controlled-comparison principle: fix the ONNX artifact and the quantization scales, so that the target's integer kernel/ISA is the only free variable, then publish scripts and per-run reports with a claim-to-artifact map so that each numbered claim can be re-checked.

## Technical contribution

Four reported findings, as read from the paper: (C1) the sign of the INT8 speedup is set by the CPU's dot-product ISA: cores with ARM SDOT or x86 VNNI gain roughly 1.8-2.1x, cores without lose roughly 1.6-1.7x for the identical model; (C2) FP32 predictions are bit-identical across all platforms (1000/1000), while INT8 predictions agree 958-965/1000 across targets that use different integer kernels, independent of whether the boundary is CPU-to-CPU or CPU-to-accelerator, and top-1 accuracy hides this; (C3) vendor NPUs own quantization: one NPU silently ignores externally supplied scales (accuracy 0.75 to 0.005 while compiling and running without error) and the other rejects the graph at compile time, so only vendor-native paths work; (C4) edge-NPU latency regimes depend on output/device-to-host transfer size rather than compute. The released scripts and 32 reports are the reusable part.

## Experimental methodology

Seven hardware classes (listed above), one fixed ONNX model artifact with fixed scales, agreement measured over 1000 inputs, a fixed-compute sweep for the NPU latency regimes. Not independently re-run by the Observatory. Details beyond what is summarized here (model choice, exact latency tables) were not read in this pass.

## Results

See the findings under Technical contribution. All quantitative values quoted there come from the paper's own reported claims as read on 2026-10-07.

## Comparison with the state of the art

Earlier measurement infrastructure tracked by the Observatory targets a single hardware family: [[2026_Taherin_Hydra]] (Jetson AGX generations, LLM workloads) and [[2026_Bryngelson_AppleNeuralEngine]] (Apple silicon). This paper is the first tracked one that applies a single fixed-artifact protocol across CPUs, edge GPU/NVDLA and vendor NPUs.

## Strengths

Controlled design with a single free variable; open scripts and reports with a claim-to-artifact map; findings that are quantified and falsifiable; the output-agreement result separates numerical determinism from accuracy, which an accuracy-only evaluation cannot see.

## Weaknesses

Single author, preprint. The model set and workload breadth were not checked in this pass. Individual observations (ISA-dependent INT8 speedups, vendor-specific quantizers) are known in practitioner circles; the contribution is quantifying and packaging them.

## Limitations

The platform list contains no Cortex-M, Arm Ethos-U or RISC-V NPU target, so the study says nothing directly about the microcontroller tier that is the Observatory's core.

## Open questions

Do the same invariances (kernel-boundary output divergence, silent-versus-loud vendor rejection) hold on Cortex-M with CMSIS-NN, on Ethos-U via Vela, and on MCU-class NPUs? Does output divergence across kernels matter for task metrics beyond top-1 agreement?

## Possible extensions

Port the fixed-artifact protocol to MCU-tier targets and to MLPerf Tiny workloads; add energy measurement.

## Relevance for our research

Primary anchor for the "validate on the target" and benchmark-realism material added to [[MLPerf_Tiny]] in the 2026-10-07 consolidation cycle.

## Possible thesis topics

An MCU-tier replication of the INT8-portability protocol across Cortex-M, Ethos-U and RISC-V NPU targets with a released harness (Master's).

## Possible collaborations

The author at KATECH; the artifact repository is public.

## Links to related papers

[[2026_Taherin_Hydra]], [[2026_Bryngelson_AppleNeuralEngine]]
