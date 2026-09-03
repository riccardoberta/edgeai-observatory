# Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency

**Full citation:** Husom, E.J., Goknil, A., Astekin, M., Shar, L.K. et al. (2025). Sustainable LLM Inference for Edge AI: Evaluating Quantized LLMs for Energy Efficiency, Output Accuracy, and Inference Latency. ACM Transactions on Internet of Things, 6(4). DOI: 10.1145/3767742.

**PDF:** [arXiv](https://arxiv.org/abs/2504.03360)

**Verification note:** Bibliographic details confirmed via WebSearch (ACM DL, arXiv). Abstract-level verified.

**Linked concepts:** [[Quantization]]

## Abstract summary

An empirical evaluation of 28 quantized LLMs from the Ollama library deployed on a Raspberry Pi 4 (4GB RAM), jointly measuring energy efficiency, inference latency, and output accuracy (via CommonsenseQA, BIG-Bench Hard, TruthfulQA, GSM8K, and HumanEval) across multiple quantization levels.

## Research problem

LLM quantization research typically reports accuracy retention or inference speed in isolation; genuine edge deployment requires understanding the joint trade-off between energy, latency, and accuracy across quantization levels on real constrained hardware, which had not been systematically characterized at this scale.

## Key idea

Evaluate a large number (28) of quantized LLM variants on identical real edge hardware across a standardized, multi-task accuracy benchmark suite, jointly reporting energy, latency, and accuracy rather than any single metric.

## Technical contribution

The largest reported systematic empirical characterization of quantized-LLM energy/latency/accuracy trade-offs on genuine edge hardware (Raspberry Pi 4), across a standardized multi-task benchmark suite.

## Experimental methodology

28 quantized LLMs deployed on a Raspberry Pi 4 with 4GB RAM, evaluated across five standardized benchmarks (CommonsenseQA, BIG-Bench Hard, TruthfulQA, GSM8K, HumanEval) with energy, latency, and accuracy measured for each configuration.

## Results

Characterizes how energy efficiency, latency, and accuracy trade off across quantization levels on real edge hardware, providing a large empirical dataset rather than a single point estimate — directly useful for practitioners choosing a quantization level for a specific deployment constraint.

## Comparison with the state of the art

A large-scale empirical complement to this KB's algorithm-focused quantization anchors (AWQ, NVFP4 characterization) and its broader survey anchor [[2025_Kang_EdgeIntelligenceReview]], grounding the field's quantization-tradeoff claims in one consistent, real-hardware dataset rather than comparing across papers with different setups.

## Strengths

Large-scale (28 models), standardized multi-task benchmark suite, genuine constrained hardware (Raspberry Pi 4, not a server GPU); jointly reports energy — a dimension many quantization papers omit.

## Weaknesses

Single hardware platform (Raspberry Pi 4); Ollama-library models specifically, which may not represent the full diversity of quantization methods this KB tracks (AWQ, NVFP4, etc.).

## Limitations

Raspberry Pi 4 is more capable than genuinely microcontroller-class hardware, so findings may not transfer directly to Cortex-M-tier deployment.

## Open questions

How would this paper's joint energy/latency/accuracy characterization change on a lower tier of hardware (Cortex-M-class) or for the specific quantization methods (AWQ, NVFP4) already anchored elsewhere in this KB's Quantization concept?

## Possible extensions

Repeating this paper's evaluation methodology (28-model sweep, standardized multi-task benchmarks, joint energy/latency/accuracy reporting) on a lower-tier or NPU-equipped edge platform.

## Relevance to our research

A large, standardized empirical dataset directly answering practical "which quantization level should I use" questions this KB's more algorithm-focused Quantization anchors do not address empirically at this scale.

## Possible thesis topics

Extending this paper's 28-model, multi-task, joint-metric evaluation methodology to a different hardware tier or to non-Ollama-library quantization methods already tracked in this KB.

## Possible collaborations

Groups working on empirical, standardized edge-AI benchmarking (SINTEF, Kristiania).

## Links to related papers

[[2025_Kang_EdgeIntelligenceReview]], [[2024_Lin_AWQ]], [[2026_Sen_NVFP4QuantizationEdgeAI]]
