# Generative EdgeAI (Gen EdgeAI)

This concept covers deploying *generative* and *multimodal* AI models — as opposed to the discriminative/classification workloads (keyword spotting, HAR, vision classification/detection) that the other Applications concepts cover — on resource-constrained edge hardware. It is a newer and less mature niche than the rest of this branch, but it has real, independently-converging momentum: a dedicated "Generative EDGE AI Working Group" has existed since 2024 within the industry-facing EDGE AI FOUNDATION, and a full 2026 edited book, "Enhancing Edge Devices With Generative Intelligence" (IGI Global), collects many independently-authored chapters on the topic.

It is deliberately kept distinct from [[MoE_Edge_LLM_Serving]] (Algorithms): that concept is about LLM *serving/scheduling infrastructure* (memory management, expert routing, heterogeneous CPU/GPU/NPU scheduling) mostly on laptop/workstation/mobile-SoC-class hardware, while this concept is about the *application-level* problem of building and evaluating generative/multimodal end-user systems — including, as one of the anchor papers below shows, genuinely small hardware such as a Raspberry Pi or Jetson Nano. A paper could plausibly belong to both if it addressed serving mechanics and an end-user generative application together; none currently does.

## Evolution of the concept

Giorgetti et al. use the term "Generative EdgeAI (Gen EdgeAI)" explicitly to name this niche in a practical tutorial and proof-of-concept system for multimodal Visual Question Answering (VQA — answering a natural-language question about an image) on the STM32MP2 low-power microprocessor. Their system chains a lightweight VQA model (adapting a multi-modal fusion architecture family, distilled from a much larger teacher model) with speech-to-text, a small language model, and text-to-speech into a full spoken-question, spoken-answer pipeline, with real on-device latency, power, and memory measurements for all four stages, and released code and trained models.

Abdulkadhim and Repas approach the same space from a different, evaluation-focused angle with LEAF (LLM Edge Assessment Framework): existing edge-AI benchmarking frameworks were built for discriminative tasks like object detection and don't capture what matters for generative workloads — token-level generation speed, semantic quality, and, distinctively, whether the hardware's own lifecycle (extending the life of existing devices versus buying new purpose-built silicon) is accounted for in what "sustainable Edge AI" means. LEAF folds this Circular Economy thinking directly into its metrics and, tested across five hardware classes running 4-bit-quantized language models, finds that a repurposed legacy consumer GPU (an NVIDIA GTX 1050 Ti) can outperform modern purpose-built edge system-on-chips on energy-per-task efficiency — challenging the assumption that newer silicon is always the more sustainable choice.

These two papers approach the space from different angles that already suggest useful substructure: one is architecture- and training-methodology-focused, building a specific multimodal system; the other is evaluation-methodology-focused, defining how to measure generative-AI edge deployments, with no new model architecture of its own.

## Key papers

[[2026_Giorgetti_VQAEdge]] — practical tutorial and proof-of-concept system for lightweight multimodal VQA on STM32MP2 (NPU-accelerated), chained into a full spoken-question/spoken-answer generative pipeline (speech-to-text, VQA, small language model, text-to-speech); real on-device latency/power/memory measurements for all four stages; released code and trained models. Co-authored within this Observatory's own research group (DITEN, University of Genoa).

[[2026_Abdulkadhim_LEAF]] — LLM Edge Assessment Framework: a five-pillar (Circular Economy Score, Joules/Token, Tokens/Second, semantic-accuracy score, end-to-end latency) benchmarking methodology for generative AI at the edge, validated across five hardware classes; finds that repurposed legacy consumer hardware can outperform modern purpose-built edge system-on-chips on energy-per-task efficiency.

## Open problems

Is "Generative EdgeAI" itself just the application-level face of [[MoE_Edge_LLM_Serving]]'s serving problem, or a genuinely separate research question? So far no paper has been claimed by both concepts, but the two share an obvious throughline — language models running on constrained hardware — worth re-examining as more Gen EdgeAI papers accumulate.

Does LEAF's "old hardware beats new system-on-chip" finding hold for multimodal (not just text) generative workloads? LEAF's methodology and hardware sweep are text-language-model-specific; the Giorgetti et al. pipeline is multimodal (vision, language, and speech) but was evaluated on a single hardware platform with only per-component, not LEAF-style cross-hardware, energy/lifecycle analysis. No paper yet applies a LEAF-style methodology to a multimodal Gen EdgeAI pipeline.

How much of a "Gen EdgeAI" pipeline can realistically run NPU-accelerated today? In Giorgetti et al., only the VQA component used the STM32MP2's NPU; speech-to-text, the language model, and text-to-speech all ran on the CPU because NPU acceleration was not yet available for those model types — an open, concrete, checkable question about how fast NPU toolchains catch up with generative/multimodal workload types, distinct from the CNN-era NPU support the [[NPU]] concept otherwise tracks.

## Research ideas

Apply LEAF's Circular-Economy-aware benchmarking methodology to a multimodal generative pipeline (for example, the Giorgetti et al. released code) to test whether the "repurposed hardware wins" finding generalizes beyond text-only language models. Extend NPU acceleration from the VQA-only case in Giorgetti et al. to the full speech-to-text/language-model/text-to-speech pipeline and re-measure the resulting power/latency profile. Build a small "Gen EdgeAI component zoo" — alternative small language models, speech-to-text, and text-to-speech models benchmarked under a shared harness — comparable to what already exists for discriminative TinyML.

## Possible thesis topics

Full-pipeline NPU acceleration and end-to-end quality evaluation of a spoken multimodal VQA system, directly extending the Giorgetti et al. released code (Master's, low-friction start given this Observatory's own co-authorship of the base paper).

Cross-hardware, cross-modality generative-AI benchmarking: extend LEAF's five-pillar methodology to multimodal workloads and microcontroller/NPU-tier hardware (Master's/PhD).

## Links

[[Distillation]], [[Vision]], [[NPU]], [[Quantization]], [[MoE_Edge_LLM_Serving]]
