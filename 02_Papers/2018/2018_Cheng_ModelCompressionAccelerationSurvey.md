# Model Compression and Acceleration for Deep Neural Networks: The Principles, Progress, and Challenges

**Full citation:** Cheng, Y., Wang, D., Zhou, P., Zhang, T. (2018). Model Compression and Acceleration for Deep Neural Networks: The Principles, Progress, and Challenges. IEEE Signal Processing Magazine, 35(1), 126-136. DOI: 10.1109/MSP.2017.2765695. Earlier preprint: arXiv:1710.09282.

**PDF:** [arXiv preprint](https://arxiv.org/abs/1710.09282)

**Verification note:** Bibliographic details confirmed via WebSearch (NASA/ADS, Semantic Scholar, IEEE Xplore listing). Abstract-level verified; this is the published IEEE Signal Processing Magazine version of the widely-cited (1800+ citations) 2017 arXiv preprint.

**Linked concepts:** [[Compression]], [[Pruning]], [[Quantization]], [[Distillation]]

## Abstract summary

An early, comprehensive survey organizing deep neural network compression and acceleration into four categories: parameter pruning/sharing, low-rank factorization, transferred/compact convolutional filters, and knowledge distillation, with a discussion of evaluation methodology for comparing techniques.

## Research problem

By 2017-2018 the compression literature had already fragmented into many disconnected techniques (pruning, quantization, low-rank factorization, distillation) with no shared taxonomy or evaluation methodology, making it hard for practitioners to compare approaches or combine them coherently.

## Key idea

Organize the fragmented compression/acceleration literature into four categories along a common axis (what is being reduced or approximated) and provide guidance on how techniques in different categories compose.

## Technical contribution

A structured taxonomy of compression/acceleration techniques, a discussion of accuracy-versus-speedup trade-offs across categories, and practical guidance on selecting or combining techniques for a given deployment scenario.

## Experimental methodology

Literature review and synthesis across the pruning, quantization, low-rank factorization, and distillation subfields as they stood through 2017, not a novel empirical study.

## Results

A widely adopted structured map of the compression/acceleration landscape that shaped how subsequent surveys (including this KB's own [[2025_Liu_ModelCompressionSurvey]]) organize the field.

## Comparison with the state of the art

Predates and frames the more specific, deeply-cited component techniques this KB already tracks individually ([[2016_Han_DeepCompression]] for pruning+quantization+coding, [[2015_Hinton_DistillingKnowledge]] for distillation) by placing them within one shared taxonomy.

## Strengths

Extremely widely cited (one of the most-cited surveys in the compression literature); clear four-way taxonomy still used as a reference structure by later work; balances breadth with concrete technique-level detail.

## Weaknesses

Published in 2017-2018, so it predates the entire 2020+ TinyML/microcontroller-deployment wave and the 2023+ LLM-compression wave; treats distillation relatively briefly compared to pruning/quantization.

## Limitations

No new empirical results; a survey's accuracy is bounded by how current its cited literature was at publication time (now seven-plus years old).

## Open questions

How would the four-category taxonomy need to be extended to accommodate techniques absent in 2017-2018 — sparse-update on-device training, NAS-guided compression, or LLM-scale post-training quantization?

## Possible extensions

A follow-up mapping showing how each of this KB's Algorithms-branch concepts (Quantization, Pruning, Distillation, NAS, Continual_Learning, On-device_Learning, Federated_Learning, MoE_Edge_LLM_Serving) relates to and extends this taxonomy's original four categories.

## Relevance to our research

The foundational, most-cited entry point for the compression/acceleration literature this KB's Compression concept organizes around — a surprising gap that this historical-audit pass closes.

## Possible thesis topics

A structured literature-mapping exercise placing every paper currently in this KB's Algorithms branch onto this survey's original four-category taxonomy, to assess which categories have grown most since 2018 and which remain thin.

## Possible collaborations

None specific — a foundational reference rather than an active research group to partner with.

## Links to related papers

[[2016_Han_DeepCompression]], [[2015_Hinton_DistillingKnowledge]], [[2025_Liu_ModelCompressionSurvey]]
