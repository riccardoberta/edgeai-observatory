# Model Compression and Hardware Acceleration for Neural Networks: A Comprehensive Survey

**Full citation:** Deng, L., Li, G., Han, S., Shi, L., Xie, Y. (2020). Model Compression and Hardware Acceleration for Neural Networks: A Comprehensive Survey. Proceedings of the IEEE, 108(4), 485-532. DOI: 10.1109/JPROC.2020.2976475.

**PDF:** [DOI](https://doi.org/10.1109/JPROC.2020.2976475)

**Verification note:** Bibliographic details confirmed via WebSearch (NASA/ADS, DBLP, ResearchGate). Abstract-level verified; Proceedings of the IEEE is a top-tier venue (this KB's other Proceedings of the IEEE entries include foundational survey-class work).

**Linked concepts:** [[Quantization]], [[Compression]], [[Pruning]]

## Abstract summary

A comprehensive, jointly-scoped survey covering both algorithmic model compression (pruning, quantization, tensor decomposition, knowledge distillation) and the hardware architectures designed to exploit compressed models, treating the two as a single co-design problem rather than separate topics.

## Research problem

Compression surveys typically treat the algorithmic side (what to remove/approximate) separately from the hardware side (what silicon can actually exploit); this leaves a gap in understanding which compression techniques translate into real hardware speedups versus only theoretical parameter reduction.

## Key idea

Present compression and hardware acceleration jointly, showing how each compression technique interacts with specific hardware capabilities (SIMD width, memory hierarchy, sparse-matrix support) rather than treating compression ratio as hardware-agnostic.

## Technical contribution

A unified survey structure spanning both algorithmic compression techniques and the accelerator architectures (including quantization-friendly and sparsity-friendly designs) that realize their benefits, plus a discussion of the resulting co-design space.

## Experimental methodology

Literature survey and synthesis across the compression and hardware-accelerator literature through 2019-2020, not a novel empirical study.

## Results

A structured joint view of the algorithm/hardware co-design space that remains a widely-cited entry point (1400+ citations) for understanding why compression ratio alone does not predict real-world speedup.

## Comparison with the state of the art

Complements this KB's other compression surveys ([[2018_Cheng_ModelCompressionAccelerationSurvey]], [[2025_Liu_ModelCompressionSurvey]]) by explicitly centering the hardware side, directly relevant to the "real hardware speedup vs. theoretical reduction" question this KB's own Pruning concept flags as an open problem.

## Strengths

Top-tier venue and very high citation count; explicitly bridges algorithms and hardware rather than treating them separately; broad enough to serve as a shared reference across this KB's Algorithms and Hardware branches.

## Weaknesses

Published in 2020, so it predates the LLM-compression wave and most microcontroller-specific NPU/accelerator work in this KB's Hardware branch.

## Limitations

No new empirical results of its own; a survey's currency is bounded by its publication date.

## Open questions

How has the algorithm/hardware co-design picture changed with the emergence of dedicated edge NPUs and LLM-specific accelerators (e.g. this KB's [[2026_Fang_YAVIN]], [[2026_Mehta_LLMscope]]) since 2020?

## Possible extensions

An updated joint algorithm/hardware survey extending this paper's framing to 2020-2026 developments: NVFP4-class quantization, structured Pruning-at-Initialization, and MoE-serving-specific hardware.

## Relevance to our research

Directly addresses this KB's own recurring question of whether a compression technique yields real hardware speedup, bridging the Algorithms and Hardware taxonomy branches explicitly.

## Possible thesis topics

Reproducing this survey's algorithm/hardware co-design framework for a specific modern target (e.g. RISC-V with vector extensions, or a commercial edge NPU), measuring where 2020-era conclusions still hold.

## Possible collaborations

Groups working on hardware/algorithm co-design for efficient inference — a natural bridge between this KB's Algorithms and Hardware branches.

## Links to related papers

[[2018_Cheng_ModelCompressionAccelerationSurvey]], [[2025_Liu_ModelCompressionSurvey]], [[2016_Han_DeepCompression]]
