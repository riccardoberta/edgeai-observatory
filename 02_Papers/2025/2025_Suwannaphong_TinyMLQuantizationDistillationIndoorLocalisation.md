# Optimising TinyML with Quantization and Distillation of Transformer and Mamba Models for Indoor Localisation on Edge Devices

**Full citation:** Suwannaphong, T., Jovan, F., Craddock, I., McConville, R. (2025). Optimising TinyML with quantization and distillation of transformer and mamba models for indoor localisation on edge devices. Scientific Reports, 15, Article 10081. DOI: 10.1038/s41598-025-94205-9. Also on arXiv:2412.09289.

**PDF:** [Nature/Scientific Reports](https://www.nature.com/articles/s41598-025-94205-9)

**Verification note:** Bibliographic details confirmed via WebSearch (Nature.com, PMC, arXiv). Abstract-level verified.

**Linked concepts:** [[Distillation]], [[Quantization]]

## Abstract summary

Combines quantization and knowledge distillation to compress both Transformer and Mamba (state-space model) architectures for indoor-localisation on resource-constrained edge devices, comparing how well each architecture family tolerates the combined compression pipeline.

## Research problem

Transformer and the newer Mamba/state-space-model architectures both show strong accuracy on sequence tasks like indoor localisation, but neither has been systematically evaluated for how well it tolerates combined quantization-plus-distillation compression for genuine edge deployment.

## Key idea

Apply quantization and distillation jointly (not just one technique in isolation) to both architecture families, directly comparing which is more compression-tolerant for a real edge task.

## Technical contribution

A joint quantization-and-distillation compression pipeline applied comparatively across Transformer and Mamba architectures for the same downstream task, rather than validating each technique on only one architecture family.

## Experimental methodology

Compression and evaluation on an indoor-localisation task using edge-representative hardware constraints, comparing compressed Transformer versus compressed Mamba models for accuracy retention under the combined pipeline.

## Results

Demonstrates that combined quantization-plus-distillation can compress both architecture families into a compact, efficient package suitable for edge deployment, with the paper reporting specific accuracy/efficiency trade-offs between the two architecture families (details at abstract level in this record).

## Comparison with the state of the art

Extends the general quantization-plus-distillation combination pattern (implicit in surveys like this KB's [[2025_Kang_EdgeIntelligenceReview]]) to the newer Mamba/state-space-model family, not just CNN/Transformer, which most existing Distillation-concept anchors predate.

## Strengths

Recent (2025), high-visibility venue (Scientific Reports/Nature), and one of the first entries in this KB to touch Mamba/state-space models under a compression lens; directly combines two of this KB's Algorithms-branch concepts in one system.

## Weaknesses

Single downstream task (indoor localisation) — generalization of the Transformer-vs-Mamba compression-tolerance finding to other sequence tasks is untested.

## Limitations

Abstract-level record; specific quantitative accuracy/efficiency numbers per architecture not captured in full detail.

## Open questions

Does the relative compression-tolerance ranking between Transformer and Mamba hold for other sequence tasks (e.g. keyword spotting, biosignals) this KB already tracks?

## Possible extensions

Repeating the same joint quantization-plus-distillation comparison on a KB-relevant sequence task like keyword spotting or biosignal classification.

## Relevance to our research

One of this KB's first entries applying compression techniques to Mamba/state-space architectures, an emerging alternative to Transformers relevant to future Vision/Applications-branch coverage.

## Possible thesis topics

Extending this Transformer-vs-Mamba compression-tolerance comparison to a different EdgeAI sequence task already tracked in this KB (HAR, keyword spotting, biosignals).

## Possible collaborations

Groups working on state-space models (Mamba) for resource-constrained sequence modeling.

## Links to related papers

[[2025_Kang_EdgeIntelligenceReview]], [[2015_Hinton_DistillingKnowledge]]
