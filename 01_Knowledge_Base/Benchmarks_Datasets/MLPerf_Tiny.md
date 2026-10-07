# MLPerf Tiny

MLPerf Tiny is the MLCommons/MLPerf consortium's standardized benchmark suite for ultra-low-power, extremely resource-constrained inference — the microcontroller-class regime this Observatory's core taxonomy centers on. It covers keyword spotting, visual wake words, image classification, and anomaly detection under one common latency/energy/accuracy measurement methodology, letting hardware vendors and researchers compare TinyML performance claims on a level playing field rather than each reporting numbers measured a different way.

## Evolution of the concept

[[2021_Banbury_MLPerfTiny|Banbury]], [[2020_Reddi_MLPerfInferenceBenchmark|Reddi]], et al. (NeurIPS 2021 Datasets and Benchmarks Track) introduce MLPerf Tiny to fill a specific gap: the general-purpose MLPerf Inference benchmark (Reddi et al., 2020), which established the field's governance model and scenario taxonomy (single-stream, multi-stream, server, offline), explicitly excludes microcontroller-class devices. MLPerf Tiny adapts that same governance template to the ultra-low-power regime, standardizing on the four tasks named above.

**Benchmark realism and measurement methodology.** MLPerf Tiny standardizes what is measured on microcontroller-class hardware, but the measurement literature the Observatory tracks suggests that a standard workload score does not by itself predict how a model behaves on a given target. The clearest verified evidence is [[2026_Shin_INT8Portability|Shin]]'s controlled cross-platform study (2026): with the ONNX artifact and quantization scales held fixed, the sign of the INT8 speedup depends on whether the CPU has a dot-product instruction (roughly 1.8-2.1x faster with ARM SDOT or x86 VNNI, roughly 1.6-1.7x slower without), INT8 predictions disagree on 35-42 of 1000 inputs across different integer kernels while FP32 predictions are bit-identical, and one vendor NPU silently ignores externally supplied quantization scales (accuracy 0.75 to 0.005 with no error). Open, family-specific characterization frameworks exist for Jetson-class hardware ([[2026_Taherin_Hydra]]) and Apple silicon ([[2026_Bryngelson_AppleNeuralEngine]]). None of these three covers the Cortex-M / Arm Ethos-U / RISC-V-NPU tier, which is exactly MLPerf Tiny's regime, so a reusable open measurement harness at that tier is still missing. Related claims about bare-metal numbers failing to transfer to a real wearable, and about runtime effects invisible to bit-width proxies on MCUs, appear in recent preprints and workshop papers but had not been verified against the primary texts when this section was written; they are tracked in the Observatory's candidate queue rather than stated here.

## Key papers

[[2021_Banbury_MLPerfTiny]] — standardized benchmark suite and measurement methodology for TinyML inference on ultra-low-power hardware, filling a prior gap where TinyML hardware/software performance claims were largely incomparable across papers and vendors.

[[2020_Reddi_MLPerfInferenceBenchmark]] — the general-purpose MLPerf Inference methodology and governance model MLPerf Tiny directly inherits and adapts for the microcontroller regime; explicitly excludes MCU-class devices, motivating MLPerf Tiny's creation.

[[2026_Shin_INT8Portability]] — controlled, artifact-fixed INT8 measurement across seven hardware classes with released scripts and reports; shows speedup sign, output agreement and deployability depend on the target kernel/vendor toolchain, and stops above the microcontroller tier.

## Open problems

MLPerf Tiny's device classes are a plausible anchor for quantitatively defining where "edge-native" LLM/MoE serving research (see [[MoE_Edge_LLM_Serving]]) stops being genuine TinyML, but no tracked paper has attempted this yet. How well do MLPerf Tiny's four representative tasks (keyword spotting, visual wake words, image classification, anomaly detection) continue to represent the field's actual workload mix as edge LLM/MoE inference grows in importance?

What would an open, reusable MLPerf-Tiny-grounded measurement harness at the Cortex-M / Ethos-U / RISC-V-NPU tier need to capture beyond latency and energy: operator fallback to the CPU, firmware co-residency and sensor pipeline cost, and output agreement across integer kernels? No tracked paper provides one.

## Research ideas

Using MLPerf Tiny's device-class definitions as the quantitative anchor for the "how edge is edge" boundary question raised in [[MoE_Edge_LLM_Serving]] — a direct, testable link between this concept and that open problem.

Porting the fixed-artifact INT8-portability protocol of [[2026_Shin_INT8Portability]] to MLPerf Tiny workloads on Cortex-M, Ethos-U and RISC-V-NPU targets, with a released harness.

## Possible thesis topics

Proposing and validating a quantitative "edge-native" boundary definition anchored to MLPerf Tiny's and MLPerf Inference's device-class definitions (Master's-scale position/measurement study; the same thesis idea also listed under [[MoE_Edge_LLM_Serving]]).

An MCU-tier replication of the INT8-portability measurement study on MLPerf Tiny workloads (Master's).

## Links

[[TensorFlow_Lite_Micro]], [[Quantization]], [[Compression]], [[Keyword_Spotting]], [[Vision]], [[NPU]], [[ONNX_Runtime]]
