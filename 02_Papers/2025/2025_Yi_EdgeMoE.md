# EdgeMoE: Empowering Sparse Large Language Models on Mobile Devices

**Full citation:** Yi, R., Guo, L., Wei, S., Zhou, A., Wang, S., Xu, M. (2025). EdgeMoE: Empowering Sparse Large Language Models on Mobile Devices. IEEE Transactions on Mobile Computing, 24(8), 7059-7073. DOI: 10.1109/TMC.2025.3546466. Originally arXiv:2308.14352 (2023).

**PDF:** [arXiv](https://arxiv.org/abs/2308.14352)

**Verification note:** Bibliographic details confirmed via WebSearch (ADS, arXiv, OpenReview). Abstract-level verified; filed under 2025 as the officially published IEEE TMC version (original arXiv preprint 2023).

**Linked concepts:** [[MoE_Edge_LLM_Serving]]

## Abstract summary

EdgeMoE, described as the first on-device inference engine specifically for mixture-of-experts (MoE) large language models, combining expert-specific bitwidth adaptation (reducing expert size with acceptable accuracy loss) with expert preloading (anticipating which experts will be activated and prefetching them via a compute-I/O pipeline) to make MoE-based LLM inference viable on mobile devices.

## Research problem

MoE-based LLMs scale parameter count almost independently of per-token compute cost, making them attractive for capability, but their full parameter set (all experts) typically exceeds mobile-device memory, and naively loading experts on demand introduces prohibitive I/O latency.

## Key idea

Reduce each expert's storage footprint via expert-specific (not uniform) bitwidth adaptation, and hide the remaining I/O latency by predicting and preloading likely-to-be-activated experts ahead of when they are needed.

## Technical contribution

A combined bitwidth-adaptation-plus-preloading on-device MoE inference engine, the first system explicitly designed for this problem rather than adapting dense-model inference engines to MoE architectures.

## Experimental methodology

Deployed and evaluated on real mobile devices, measuring inference latency, memory footprint, and accuracy retention against both dense-model baselines and naive (non-preloading, uniform-bitwidth) MoE deployment.

## Results

Achieves substantially lower memory footprint and latency than naive on-device MoE deployment while retaining acceptable accuracy, demonstrating that MoE-based LLMs can be made mobile-viable through system-level (not just algorithmic) optimization.

## Comparison with the state of the art

Builds directly on the sparsely-gated MoE architecture of [[2017_Shazeer_SparselyGatedMoE]], adding the edge-specific system-level techniques (bitwidth-adaptive expert storage, predictive preloading) that the original architecture paper does not address; a natural companion to this KB's [[2025_Zhao_UnifiedResourceAwareEdgeInference]] which also combines quantization with dynamic expert routing for edge deployment.

## Strengths

One of the first systems explicitly designed for on-device MoE serving (not adapted from dense-model infrastructure); real mobile-device validation; well-cited (85+) for a recent systems paper.

## Weaknesses

Prediction-based preloading can mispredict, incurring a latency penalty when the wrong experts are prefetched — a limitation the paper's evaluation does not fully characterize under adversarial input distributions.

## Limitations

Validated on mobile-class hardware, not genuinely microcontroller-class devices; the bitwidth-adaptation and preloading techniques both assume enough on-device storage to hold a working set of experts, which may not hold at the most constrained tier.

## Open questions

How well does the expert-preloading prediction strategy generalize across different downstream tasks with different expert-activation patterns, and does it degrade gracefully or fail sharply under misprediction?

## Possible extensions

Extending expert-specific bitwidth adaptation and preloading to a genuinely storage-constrained tier below mobile-class devices, or combining it with the dynamic routing approach of [[2025_Zhao_UnifiedResourceAwareEdgeInference]].

## Relevance to our research

One of the concept-defining systems papers for MoE_Edge_LLM_Serving, directly relevant to understanding how MoE-based LLMs move from the architectural idea ([[2017_Shazeer_SparselyGatedMoE]]) to genuine edge deployment.

## Possible thesis topics

Benchmarking EdgeMoE-style bitwidth-adaptive preloading against the routing-based approach of [[2025_Zhao_UnifiedResourceAwareEdgeInference]] on a common MoE-LLM and mobile/edge hardware target.

## Possible collaborations

Groups working on on-device LLM serving systems (Beijing University of Posts and Telecommunications, Zhongguancun Laboratory).

## Links to related papers

[[2017_Shazeer_SparselyGatedMoE]], [[2025_Zhao_UnifiedResourceAwareEdgeInference]]
