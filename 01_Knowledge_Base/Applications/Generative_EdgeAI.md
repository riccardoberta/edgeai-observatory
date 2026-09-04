# Generative EdgeAI (Gen EdgeAI)

## Evolution of the concept

This concept groups research on deploying *generative* and *multimodal* AI models — as opposed to the discriminative/classification workloads (keyword spotting, HAR, vision classification/detection) that dominate this Observatory's other Applications concepts — on resource-constrained edge hardware. It was created 2026-09-04 in response to a targeted Google Scholar search for the literal term "EdgeAI", which surfaced [[2026_Giorgetti_VQAEdge]] — co-authored by this Observatory's own Riccardo Berta — using the term "Generative EdgeAI (Gen EdgeAI)" explicitly as "a particular niche of EdgeAI" focused on deploying generative models on edge devices. A follow-up search confirmed this is not one group's private framing: a dedicated "Generative EDGE AI Working Group" has existed since 2024 within the industry-facing EDGE AI FOUNDATION (evidenced by Morabito, Adorante, Mousannif & Pau's 2025 "Expanding The Horizons of Generative Edge AI" position paper), an entire edited book — "Enhancing Edge Devices With Generative Intelligence" (IGI Global, 2026) — has been published with many independently-authored chapters on the topic, and [[2026_Abdulkadhim_LEAF]] is a fully independent, peer-reviewed (MDPI) technical contribution (an LLM-edge benchmarking methodology) with no author overlap with the Giorgetti/Pau/Berta cluster. These two papers — a practical multimodal-VQA tutorial/system from one group and a systematic text-only LLM benchmarking framework from a wholly independent group — are recorded as this concept's founding anchors, clearing this Observatory's two-independent-anchor bar for formalizing a new taxonomy node (the same bar applied to [[MoE_Edge_LLM_Serving]], [[Hardware_Security_of_Edge_AI_Accelerators]], and the Event-Driven/Neuromorphic Accelerators node).

The two founding papers approach the space from different angles that already suggest useful substructure: [[2026_Giorgetti_VQAEdge]] is architecture- and training-methodology-focused (adapting a specific multimodal architecture family — MFB fusion with attention/co-attention — for a specific MPU's NPU, via knowledge distillation) and includes a full proof-of-concept end-to-end pipeline (STT→VQA→LM→TTS) demonstrating conversational, spoken interaction; [[2026_Abdulkadhim_LEAF]] is evaluation-methodology-focused (defining how to *measure* generative-AI edge deployments across speed, semantic accuracy, and — its distinguishing contribution — hardware-lifecycle/Circular-Economy sustainability) with no new model architecture of its own. Both explicitly distinguish themselves from prior discriminative-task-oriented edge AI work.

This concept is deliberately kept distinct from [[MoE_Edge_LLM_Serving]] (Algorithms): that cluster is about *serving/scheduling infrastructure* for LLM inference (memory management, expert routing, heterogeneous CPU/GPU/NPU scheduling) mostly on laptop/workstation/mobile-SoC-class hardware, while this concept is about the *application-level* problem of building and evaluating generative/multimodal end-user systems (VQA, conversational agents) — including, in LEAF's case, genuinely small hardware (Raspberry Pi, Jetson Nano). A paper can plausibly belong to both if it addresses serving mechanics *and* an end-user generative application; none currently does, but the boundary is worth watching as the space grows.

## Key papers

[[2026_Giorgetti_VQAEdge]] — practical tutorial and proof-of-concept system for lightweight multimodal VQA on STM32MP2 (NPU-accelerated), chained into a full spoken-question/spoken-answer generative pipeline (STT, VQA, small LM, TTS); real on-device latency/power/memory measurements for all four stages; released code and trained models.

[[2026_Abdulkadhim_LEAF]] — LLM Edge Assessment Framework: a five-pillar (Circular Economy Score, Joules/Token, Tokens/Second, BERTScore, end-to-end latency) benchmarking methodology for generative AI at the edge, validated across five hardware classes; headline finding that repurposed legacy consumer hardware can outperform modern purpose-built edge SoCs on energy-per-task efficiency.

## Open problems

**Is "Generative EdgeAI" itself just the application-level face of [[MoE_Edge_LLM_Serving]]'s serving problem, or a genuinely separate research question?** Both concepts are less than a month old in this KB's formal taxonomy and share an obvious throughline (LLMs running on constrained hardware), but so far no paper has been claimed by both — worth re-examining as more Gen EdgeAI papers accumulate whether the application/infrastructure split holds up or should be merged.

**Does LEAF's "old hardware beats new SoC" finding hold for multimodal (not just text) generative workloads?** LEAF's five-pillar methodology and hardware sweep are text-LLM-specific; [[2026_Giorgetti_VQAEdge]]'s pipeline is multimodal (vision + language + speech) but was evaluated on a single hardware platform (STM32MP2) with only per-component, not LEAF-style cross-hardware, energy/lifecycle analysis. No paper yet applies a LEAF-style methodology to a multimodal Gen EdgeAI pipeline.

**How much of the "Gen EdgeAI" pipeline can realistically run NPU-accelerated today?** In Giorgetti et al., only the VQA component used STM32MP2's NPU; STT, LM, and TTS all ran on CPU "due to lack of acceleration at the time of writing" — an open, concrete, checkable question about how fast NPU toolchains catch up with generative/multimodal workload types, distinct from the CNN-era NPU support this Observatory's [[NPU]] concept otherwise tracks.

## Research ideas

Apply LEAF's Circular-Economy-aware benchmarking methodology to a multimodal generative pipeline (e.g. Giorgetti et al.'s own released code) to test whether the "repurposed hardware wins" finding generalizes beyond text-only LLMs. Extend NPU acceleration from the VQA-only case in Giorgetti et al. to the full STT/LM/TTS pipeline and re-measure the resulting power/latency profile. Build a small "Gen EdgeAI component zoo" (alternative small LMs, STT, TTS models benchmarked under a shared harness) comparable to what already exists for discriminative TinyML.

## Possible thesis topics

Full-pipeline NPU acceleration and end-to-end quality evaluation of a spoken multimodal VQA system, directly extending [[2026_Giorgetti_VQAEdge]]'s released code (Master's, low-friction start given this Observatory's own co-authorship of the base paper).

Cross-hardware, cross-modality generative-AI benchmarking: extend LEAF's five-pillar methodology to multimodal workloads and MCU/NPU-tier hardware (bridging this concept, [[2026_Abdulkadhim_LEAF]], and the mcu-npu-measurement-infrastructure consolidation candidate) (Master's/PhD).

## Links

[[Distillation]], [[Vision]], [[NPU]], [[Quantization]], [[MoE_Edge_LLM_Serving]] (application-level Gen EdgeAI vs. that concept's serving/scheduling infrastructure focus — related but deliberately kept distinct, see Evolution of the concept above)
