# Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels

**Full citation:** Taherin, A., Anvari, S.T., Amante, C., Chen, Y., Noroian, R., Feric, Z., Agostini, N.B., Zhao, P., Cano, J., Ren, B., Wang, Y., Kaeli, D. (2026). Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels. arXiv:2608.25053 [cs.AR]. Northeastern University; University of Glasgow; William & Mary. Submitted 25 Aug 2026. Accepted at IEEE International Symposium on Workload Characterization (IISWC 2026). DOI: 10.48550/arXiv.2608.25053.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2608.25053)

**Linked concepts:** [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]], [[Quantization]]

## Abstract summary

Edge LLM deployment cost is shaped by more than model size and precision — inference backend, hardware platform, memory traffic, and power management all interact. Hydra is a common-schema, phase-aware workload-characterization framework for LLM inference on edge SoCs, instrumenting HuggingFace Transformers and llama.cpp with a shared per-prompt timing schema fused with hardware telemetry, separating the prefill and decode phases. Evaluated across three consecutive NVIDIA Jetson AGX generations (Xavier, Orin, Thor), 13 instruction-tuned LLMs from seven families, five execution formats, and input/output-length sensitivity sweeps, producing an open, 107K-per-prompt-record corpus. Key finding: aggregate latency hides important effects — backend structure changes where latency is introduced, quantization reduces memory traffic and energy but does not predict power monotonically, and SoC generation changes how utilization/efficiency metrics should even be interpreted.

## Research problem

Edge LLM deployment decisions (which backend, which quantization level, which SoC generation) are typically evaluated using single aggregate latency or throughput numbers, which obscure where time and energy are actually spent. Prefill (processing the prompt) and decode (generating tokens) have fundamentally different compute/memory-bandwidth profiles, and existing benchmarking practice largely does not separate them or connect timing to system-resource telemetry in a reproducible, cross-backend, cross-generation way — making it hard to draw generalizable conclusions about what actually drives edge LLM inference cost.

## Key idea

Build a common measurement schema that instruments two different, widely-used inference backends (HuggingFace Transformers, llama.cpp) with the same per-prompt, phase-level (prefill/decode) timing structure, and fuse that with hardware telemetry (utilization, memory traffic, power) so that results are directly comparable across backends, hardware generations, and quantization levels rather than being backend- or platform-specific one-off measurements.

## Technical contribution

A backend-agnostic, phase-aware measurement schema and instrumentation for HuggingFace Transformers and llama.cpp; a large-scale, systematically swept evaluation spanning three edge SoC generations (Jetson AGX Xavier, Orin, Thor), 13 LLMs across seven model families, and five execution formats; an open-source 107,000-record trace corpus; and the phase-level analysis methodology itself, which the paper argues is necessary because aggregate latency conflates effects that only phase separation reveals.

## Experimental methodology

Empirical measurement study (not simulation) on real hardware: three consecutive generations of NVIDIA Jetson AGX edge SoCs (Xavier, Orin, Thor). 13 instruction-tuned LLMs from 7 model families, 5 execution formats (quantization/backend combinations), with input/output-length sensitivity sweeps. Per-prompt records combine phase-level (prefill/decode) timing with hardware telemetry (utilization, memory traffic, power). The full corpus (~107K records) and framework are released open-source.

## Results

Three headline findings: (1) backend structure — not just model or hardware choice — changes where latency is introduced within the prefill/decode pipeline; (2) quantization reduces memory traffic and energy but does not predict power draw monotonically, i.e. lower precision does not always mean proportionally lower power; (3) SoC generation changes how utilization and efficiency metrics should be interpreted, meaning cross-generation comparisons using the same metric definitions can be misleading without phase-aware context.

## Comparison with the state of the art

Distinguishes itself from prior edge-LLM benchmarking work by (a) separating prefill and decode phases rather than reporting aggregate latency, (b) spanning three hardware generations rather than a single platform snapshot, and (c) instrumenting two backends under one common schema rather than reporting backend-specific numbers that are hard to compare. This places Hydra alongside, but methodologically more rigorous than, typical single-platform Jetson benchmarking papers (e.g. the vision-inference profiling work recorded separately by this Observatory, [[2025_Chakraborty_ProfilingJetsonVisionInference]]) — though Hydra targets LLM inference specifically rather than vision.

## Strengths

Genuinely reproducible, open-source methodology and a large public trace corpus rather than a one-off internal benchmark; the phase-aware (prefill/decode) approach directly addresses a real methodological weakness in how edge LLM inference is typically reported; spans three hardware generations, giving a longitudinal view rather than a single snapshot; the non-monotonic power/quantization finding is a genuinely useful, non-obvious result for anyone designing quantization-aware edge LLM deployments.

## Weaknesses

Restricted to the Jetson AGX tier (workstation/embedded-GPU-class SoCs) — does not address the MCU- or mobile-NPU-class tier this Observatory's core taxonomy (Cortex-M, RISC-V-NPU) centers on; this is explicitly the gap the Observatory's own consolidation candidate queue flagged when this paper (and the related Apple Neural Engine study, [[2026_Bryngelson_AppleNeuralEngine]]) was first surfaced by the August monthly report — a standardized measurement methodology at the MCU/NPU tier remains absent.

## Limitations

Findings are specific to the AGX Xavier/Orin/Thor generational lineage and the two backends instrumented (HuggingFace Transformers, llama.cpp); whether the same phase-aware conclusions (backend-dependent latency location, non-monotonic power/quantization relationship) hold for MCU-class or mobile-NPU-class inference is untested by this paper.

## Open questions

Does a Hydra-style phase-aware, cross-backend, cross-generation measurement methodology transfer to MCU/Ethos-U/RISC-V-NPU-class hardware, where LLM inference is only beginning to appear (e.g. the [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]] concept's cluster of laptop/edge-GPU-class papers)? Why does quantization fail to predict power monotonically — what is the underlying mechanism (memory-controller behavior, dynamic voltage/frequency scaling interaction) driving this?

## Possible extensions

Applying the Hydra measurement schema to MCU/NPU-tier hardware to directly close the standardized-measurement-infrastructure gap this Observatory's consolidation queue has tracked since 2026-08-31; investigating the mechanism behind the non-monotonic quantization/power relationship through targeted micro-benchmarks.

## Relevance to our research

Directly relevant to the [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]] concept's edge-LLM-deployment focus, providing rigorous, phase-aware measurement methodology that the concept's serving/scheduling papers (HeteroMosaic, PolyQ, APEX) could adopt for evaluation. Also the primary evidence, alongside [[2026_Bryngelson_AppleNeuralEngine]], for the Observatory's still-open "standardized MCU/NPU-tier measurement infrastructure" consolidation candidate — this paper and the ANE study both build rigorous measurement infrastructure, but neither has an analogue at the microcontroller/NPU tier.

## Possible thesis topics

Building an MCU/NPU-tier analogue of Hydra's phase-aware, cross-backend measurement schema, directly targeting the standardized-measurement-infrastructure gap this Observatory has tracked since 2026-08-31 (PhD-scale; bridges Hardware and [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]]). Investigating the causal mechanism behind quantization's non-monotonic effect on power draw across SoC generations (Master's/PhD).

## Possible collaborations

The Northeastern University / Glasgow / William & Mary author team behind Hydra, and the open-source Hydra framework itself (github.com/amirtaherin/hydra) as reusable measurement infrastructure for any lab benchmarking edge LLM inference.

## Links to related papers

[[2026_Bryngelson_AppleNeuralEngine]] (the other half of the Observatory's MCU/NPU-tier measurement-infrastructure evidence, at the Apple-silicon tier); [[2025_Chakraborty_ProfilingJetsonVisionInference]] (a narrower, single-generation Jetson profiling study, for vision rather than LLM workloads).
