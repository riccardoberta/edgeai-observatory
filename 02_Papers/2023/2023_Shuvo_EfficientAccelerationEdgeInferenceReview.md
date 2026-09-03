# Efficient Acceleration of Deep Learning Inference on Resource-Constrained Edge Devices: A Review

**Full citation:** Shuvo, M.M.H., Islam, S.K., Cheng, J., Morshed, B.I. (2023). Efficient Acceleration of Deep Learning Inference on Resource-Constrained Edge Devices: A Review. Proceedings of the IEEE, 111(1), 42-91. DOI not confirmed via search — cite via journal/volume/pages.

**PDF:** [ResearchGate](https://www.researchgate.net/publication/366296203_Efficient_Acceleration_of_Deep_Learning_Inference_on_Resource-Constrained_Edge_Devices_A_Review)

**Verification note:** Bibliographic details (authors, venue, volume/issue/pages) confirmed via WebSearch (DBLP, NASA/ADS, Semantic Scholar); DOI not located through search and left unconfirmed rather than guessed. Abstract-level verified.

**Linked concepts:** [[Compression]], [[Quantization]], [[Pruning]]

## Abstract summary

A comprehensive review of tools and techniques specifically for accelerating deep learning inference on resource-constrained edge devices, covering the full pipeline from model compression through compiler-level and hardware-level optimization.

## Research problem

Edge-inference acceleration research spans multiple layers (algorithmic compression, compiler optimization, hardware acceleration) that are usually surveyed separately; practitioners need a single, current reference spanning the whole stack specifically for resource-constrained (not just "edge-server") devices.

## Key idea

Review the full edge-inference-acceleration stack — from compression techniques through to hardware execution — as one connected pipeline rather than a set of independent topics.

## Technical contribution

A structured, top-tier-venue (Proceedings of the IEEE) review connecting model compression, compiler-level optimization, and hardware acceleration specifically for resource-constrained edge deployment.

## Experimental methodology

Literature review and synthesis, not a novel empirical study.

## Results

A widely-cited (580+ citations) current reference for the full edge-inference-acceleration pipeline, published in one of the field's most prestigious general-purpose venues.

## Comparison with the state of the art

Complements this KB's other compression/acceleration surveys ([[2018_Cheng_ModelCompressionAccelerationSurvey]], [[2020_Deng_ModelCompressionHardwareAccelerationSurvey]]) with a more recent (2023), explicitly resource-constrained-edge-focused synthesis.

## Strengths

Recent, top-tier venue, very high citation count for its age; explicitly scoped to resource-constrained (not just generic edge/mobile) hardware, matching this KB's own focus.

## Weaknesses

As a broad review it necessarily covers ground already tracked elsewhere in this KB; specific novel technical contributions beyond synthesis are limited.

## Limitations

No new empirical results of its own.

## Open questions

Which parts of the reviewed acceleration pipeline remain bottlenecked specifically at the microcontroller (Cortex-M) tier versus the mobile/edge-GPU tier this review may weight more heavily?

## Possible extensions

A follow-up specifically isolating microcontroller-tier findings from this review's broader resource-constrained-edge scope.

## Relevance to our research

A recent, high-credibility, full-stack anchor for this KB's Compression concept, complementing the more algorithm-focused surveys already present.

## Possible thesis topics

A reproducibility study benchmarking a subset of the techniques this review surveys on a common Cortex-M target, to see which conclusions transfer to the most constrained tier.

## Possible collaborations

Groups working on full-stack edge-inference-acceleration benchmarking.

## Links to related papers

[[2018_Cheng_ModelCompressionAccelerationSurvey]], [[2020_Deng_ModelCompressionHardwareAccelerationSurvey]]
