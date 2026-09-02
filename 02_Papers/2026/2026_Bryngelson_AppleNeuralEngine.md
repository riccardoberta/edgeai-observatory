# Apple Neural Engine: Architecture, Programming, and Performance

**Full citation:** Bryngelson, S.H. (2026). Apple Neural Engine: Architecture, Programming, and Performance. arXiv:2606.22283 [cs.AR]. Georgia Institute of Technology. Submitted Jun 2026. DOI: 10.48550/arXiv.2606.22283.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2606.22283)

**Linked concepts:** [[NPU]]

## Abstract summary

A reverse-engineered account of Apple's Neural Engine (ANE), based on direct measurement on Apple silicon and static analysis of the private runtime, compiler, kernel driver, and firmware, since Apple does not publish an architectural specification. The account covers the A11 through A18 and M1 through M5 chip families, with per-chip target tables and an operation-by-device support matrix, with direct measurements taken on M1 and M5. On the M1, the engine holds about 12 fp16 TFLOP/s against a DRAM-bandwidth ceiling, with a roofline ridge point near 141 FLOP/byte, a 2MB working-set threshold, a 0.23ms floor under any single dispatch, and efficiency near 0.37pJ/FLOP at the compute optimum; on a 256-channel 3x3 convolution it runs about 3.8x faster than the same chip's GPU and 9x more energy-efficient.

## Research problem

The Apple Neural Engine is deployed at enormous scale (every recent iPhone, iPad, and Mac) and is central to on-device ML on Apple platforms, yet Apple has never published its architecture, ISA, or a performance model — access is only through the closed-source Core ML compiler and runtime. This opacity makes principled on-device deployment decisions (what maps well to the ANE, what its actual roofline looks like, when it beats the GPU) effectively guesswork for developers and researchers, and leaves a major commercial NPU family absent from the kind of open architectural literature this Observatory already tracks for other NPUs (e.g. [[2021_Yazdanbakhsh_EdgeTPUEvaluation]] for Edge TPU).

## Key idea

Reverse-engineer the ANE's architecture and performance model through a combination of direct hardware measurement (microbenchmarks on real M1 and M5 silicon) and static analysis of Apple's private compiler, kernel driver, and firmware components, rather than waiting for or assuming official documentation, producing the first open, chip-family-spanning (A11-A18, M1-M5) reference account.

## Technical contribution

A reverse-engineered architectural account of the ANE spanning eight iPhone/iPad chip generations (A11-A18) and five Mac chip generations (M1-M5); per-chip target tables and an operation-by-device support matrix documenting what each generation actually supports; a measured roofline model (compute ceiling, DRAM-bandwidth ceiling, ridge point, working-set threshold) derived from direct M1 and M5 measurement; a measured dispatch-latency floor and energy-efficiency figure at the compute optimum; a head-to-head measured comparison against the same chip's GPU on a representative convolution workload.

## Experimental methodology

Direct hardware measurement (microbenchmarking) on Apple M1 and M5 silicon, combined with static analysis of Apple's private ANE compiler, kernel driver, and firmware to reconstruct architectural details not observable through black-box measurement alone. The operation-by-device support matrix and per-chip target tables were compiled across the full A11-A18/M1-M5 family range, though direct performance measurement was limited to M1 and M5.

## Results

On M1: approximately 12 fp16 TFLOP/s compute ceiling, DRAM-bandwidth-bound roofline ridge point at ~141 FLOP/byte, a 2MB working-set threshold before bandwidth-boundedness sets in, a 0.23ms latency floor for any single dispatch regardless of workload size, and ~0.37pJ/FLOP energy efficiency at the compute-bound optimum. On a 256-channel 3x3 convolution, the ANE is about 3.8x faster than the same chip's GPU and about 9x more energy-efficient.

## Comparison with the state of the art

Fills a gap analogous to what large-scale empirical NPU characterization studies (e.g. [[2021_Yazdanbakhsh_EdgeTPUEvaluation]]'s ~423,000-CNN-variant sweep of Edge TPU) have done for other commercial NPU families, but via reverse engineering rather than vendor cooperation, since Apple provides no equivalent official documentation. A related contemporaneous work, Orion (arXiv:2603.06728, 2026), builds an end-to-end system bypassing Core ML entirely to run direct ANE training/inference — evidence of a broader 2026 wave of independent reverse-engineering efforts targeting the ANE, not a single isolated paper.

## Strengths

Fills a genuine, long-standing documentation gap for one of the most widely deployed commercial NPUs in existence; combines measurement with static analysis rather than relying on either alone, strengthening confidence in the reconstructed architectural picture; spans eight-plus chip generations rather than a single snapshot, giving a longitudinal view of how the ANE has evolved; the measured roofline, latency-floor, and energy-efficiency figures give developers and researchers a principled basis for on-device deployment decisions that previously required empirical trial-and-error.

## Weaknesses

Direct performance measurement is limited to two chip generations (M1, M5) out of the thirteen covered by the broader architectural survey — performance figures for the intervening generations (A12-A18, M2-M4) rely on the static-analysis/reverse-engineering methodology rather than direct measurement, and may be less precisely characterized; being reverse-engineered rather than vendor-confirmed, some architectural details carry inherent uncertainty that only Apple could fully resolve.

## Limitations

As a reverse-engineering effort, the account is necessarily incomplete or provisional wherever Apple's private runtime/compiler/firmware resists static analysis; findings are specific to the ANE and Apple's software stack (Core ML) and do not directly generalize to other mobile/edge NPU families without separate characterization work.

## Open questions

How does the ANE's measured roofline and energy-efficiency profile compare directly against other mobile NPU families (Qualcomm Hexagon, per [[2026_Absar_HexagonMLIR]]; Samsung's multi-precision NPU, per [[2023_Park_MultiModeNPU]]) under a common benchmark methodology? Does the 0.23ms per-dispatch latency floor meaningfully constrain small-model or low-latency on-device use cases, and how does it compare to the dispatch overhead of other commercial NPUs?

## Possible extensions

A cross-vendor mobile-NPU roofline comparison combining this paper's ANE measurements with equivalent data for Hexagon, Samsung's NPU, and Edge TPU under one common methodology; extending direct measurement coverage to the remaining chip generations (A12-A18, M2-M4) currently characterized only via static analysis.

## Relevance to our research

Extends the Observatory's [[NPU]] concept with a rigorously reverse-engineered account of a major commercial NPU family previously entirely absent from the tracked literature, and is one of two anchor papers (alongside [[2026_Taherin_Hydra]]) for the still-open "standardized MCU/NPU-tier measurement infrastructure" consolidation candidate — both papers build rigorous, open, longitudinal measurement infrastructure, but at the Apple-silicon/Jetson tier rather than the MCU/microcontroller-NPU tier this Observatory's core taxonomy centers on.

## Possible thesis topics

A common-methodology roofline comparison across ANE, Hexagon, Samsung's mobile NPU, and Edge TPU, using this paper's measurement approach as a template (Master's/PhD; bridges [[NPU]] with cross-vendor benchmarking). Extending reverse-engineering-based NPU characterization to a currently undocumented MCU-class NPU (e.g. Arm Ethos-U), directly addressing this Observatory's MCU/NPU-tier measurement-infrastructure gap.

## Possible collaborations

Spencer H. Bryngelson's group (Georgia Institute of Technology) on ANE architecture; potential connection to the Orion project (arXiv:2603.06728) for anyone pursuing direct, Core-ML-bypassing ANE programming.

## Links to related papers

[[2026_Taherin_Hydra]] (the other anchor for the Observatory's open MCU/NPU-tier measurement-infrastructure question, at the Jetson-generation tier); [[2021_Yazdanbakhsh_EdgeTPUEvaluation]] (the Observatory's precedent for large-scale empirical NPU characterization, for a different commercial NPU family); [[2026_Absar_HexagonMLIR]] and [[2023_Park_MultiModeNPU]] (other commercial mobile-NPU designs this paper's findings could be compared against).
