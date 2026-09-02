# MLPerf Tiny

## Evolution of the concept

Created 2026-09-02, formalizing a new top-level Benchmarks & Datasets taxonomy branch. Before this pass, MLPerf Tiny existed in the Observatory only as a paper record ([[2021_Banbury_MLPerfTiny]]) cross-linked from several Algorithms and Applications concepts, with no organizational home of its own — despite "Benchmarks" being one of the four categories the project's founding instructions explicitly name for continuous monitoring, alongside digital libraries, conferences, and hardware vendors. MLPerf Tiny (Banbury, Reddi, et al.; NeurIPS 2021 Datasets and Benchmarks Track) is the MLCommons/MLPerf consortium's standardized benchmark suite for ultra-low-power, extremely resource-constrained inference — the microcontroller-class regime this Observatory's core taxonomy centers on — covering keyword spotting, visual wake words, image classification, and anomaly detection under one common latency/energy/accuracy measurement methodology.

## Key papers

[[2021_Banbury_MLPerfTiny]] — standardized benchmark suite and measurement methodology for TinyML inference on ultra-low-power hardware, filling a prior gap where TinyML hardware/software performance claims were largely incomparable across papers and vendors.

## Open problems

MLPerf Tiny's device classes have been informally proposed (August 2026 monthly report, see [[Mixture-of-Experts (MoE) & Edge LLM Serving]]'s open problems) as a possible anchor for quantitatively defining where "edge-native" LLM/MoE serving research stops being genuine TinyML — this has not yet been attempted by any tracked paper. How well do MLPerf Tiny's four representative tasks (keyword spotting, visual wake words, image classification, anomaly detection) continue to represent the field's actual workload mix as edge LLM/MoE inference (per [[Mixture-of-Experts (MoE) & Edge LLM Serving]]) grows in importance?

## Research ideas

Using MLPerf Tiny's device-class definitions as the quantitative anchor for the "how edge is edge" boundary question already raised in [[Mixture-of-Experts (MoE) & Edge LLM Serving]] — a direct, testable link between this concept and that open problem.

## Possible thesis topics

Proposing and validating a quantitative "edge-native" boundary definition anchored to MLPerf Tiny's and MLPerf Inference's device-class definitions (Master's-scale position/measurement study; directly extends the same thesis idea already listed under [[Mixture-of-Experts (MoE) & Edge LLM Serving]]).

## Links

[[TensorFlow_Lite_Micro]], [[Quantization]], [[Compression]], [[Keyword_Spotting]], [[Vision]]
