# MLPerf Tiny

MLPerf Tiny is the MLCommons/MLPerf consortium's standardized benchmark suite for ultra-low-power, extremely resource-constrained inference — the microcontroller-class regime this Observatory's core taxonomy centers on. It covers keyword spotting, visual wake words, image classification, and anomaly detection under one common latency/energy/accuracy measurement methodology, letting hardware vendors and researchers compare TinyML performance claims on a level playing field rather than each reporting numbers measured a different way.

## Evolution of the concept

Banbury, Reddi, et al. (NeurIPS 2021 Datasets and Benchmarks Track) introduce MLPerf Tiny to fill a specific gap: the general-purpose MLPerf Inference benchmark (Reddi et al., 2020), which established the field's governance model and scenario taxonomy (single-stream, multi-stream, server, offline), explicitly excludes microcontroller-class devices. MLPerf Tiny adapts that same governance template to the ultra-low-power regime, standardizing on the four tasks named above.

## Key papers

[[2021_Banbury_MLPerfTiny]] — standardized benchmark suite and measurement methodology for TinyML inference on ultra-low-power hardware, filling a prior gap where TinyML hardware/software performance claims were largely incomparable across papers and vendors.

[[2020_Reddi_MLPerfInferenceBenchmark]] — the general-purpose MLPerf Inference methodology and governance model MLPerf Tiny directly inherits and adapts for the microcontroller regime; explicitly excludes MCU-class devices, motivating MLPerf Tiny's creation.

## Open problems

MLPerf Tiny's device classes are a plausible anchor for quantitatively defining where "edge-native" LLM/MoE serving research (see [[MoE_Edge_LLM_Serving]]) stops being genuine TinyML, but no tracked paper has attempted this yet. How well do MLPerf Tiny's four representative tasks (keyword spotting, visual wake words, image classification, anomaly detection) continue to represent the field's actual workload mix as edge LLM/MoE inference grows in importance?

## Research ideas

Using MLPerf Tiny's device-class definitions as the quantitative anchor for the "how edge is edge" boundary question raised in [[MoE_Edge_LLM_Serving]] — a direct, testable link between this concept and that open problem.

## Possible thesis topics

Proposing and validating a quantitative "edge-native" boundary definition anchored to MLPerf Tiny's and MLPerf Inference's device-class definitions (Master's-scale position/measurement study; the same thesis idea also listed under [[MoE_Edge_LLM_Serving]]).

## Links

[[TensorFlow_Lite_Micro]], [[Quantization]], [[Compression]], [[Keyword_Spotting]], [[Vision]]
