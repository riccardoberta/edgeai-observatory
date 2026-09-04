# Introducing LEAF: LLM Edge Assessment Framework for Generative AI on the Edge

**Full citation:** Abdulkadhim, M., Repas, S. R. (2026). Introducing LEAF: LLM Edge Assessment Framework for Generative AI on the Edge. Machine Learning and Knowledge Extraction, 8(2), 48. DOI: 10.3390/make8020048. Published 2026-02-18. Open access, CC BY 3.0.

**PDF/HTML:** [MDPI](https://www.mdpi.com/2504-4990/8/2/48)

**Linked concepts:** [[Generative_EdgeAI]] — founding anchor (alongside [[2026_Giorgetti_VQAEdge]]), created 2026-09-04. Also touches [[Quantization]] (all benchmarked models are 4-bit quantized via Ollama).

**Verification note:** this record is built from the abstract and bibliographic metadata (MDPI's structured `dc.description`/`og:description` fields), not a full-text read of the paper — flagged per this Observatory's honesty-over-forced-completeness practice. The abstract is detailed enough to establish the paper's problem, method, and headline finding with confidence; a full-text pass would be needed before citing specific per-device numbers beyond what's summarized below.

## Abstract summary

Existing edge-AI benchmarking frameworks are built for discriminative tasks (e.g. object detection) and don't capture the multidimensional trade-offs generative AI introduces at the edge — token generation speed, semantic accuracy, and hardware sustainability. The authors introduce LEAF (LLM Edge Assessment Framework), an evaluation methodology integrating Circular Economy principles directly into performance metrics across five pillars: Circular Economy Score, Energy Efficiency (Joules/Token), Performance Speed (Tokens/Second), semantic accuracy (BERTScore), and End-to-End Latency. LEAF is validated across five hardware classes — embedded IoT devices (Raspberry Pi 4 and 5, NVIDIA Jetson Nano) through professional edge servers (NVIDIA T400) to repurposed legacy workstations (NVIDIA GTX 1050 Ti) — running 4-bit quantized LLMs via Ollama. The headline finding is counterintuitive: the legacy GTX 1050 Ti achieved a 20x speedup over the Raspberry Pi 4 and better energy-per-task efficiency than low-power ARM boards, challenging the assumption that newer purpose-built edge silicon is necessary for good Edge AI outcomes.

## Research problem

Generative AI (LLM) deployment at the edge is evaluated, when it is evaluated at all, using benchmarking methodology inherited from discriminative deep learning (accuracy/latency/throughput on fixed classification or detection tasks). This misses what actually matters for edge-deployed generative workloads: token-level generation speed and semantic quality together with energy cost per unit of useful output, and — the paper's distinguishing angle — whether the hardware lifecycle itself (new purpose-built silicon vs. extending the life of existing devices) is being accounted for in what "sustainable Edge AI" means.

## Key idea

Define a benchmarking methodology purpose-built for generative (token-producing) edge workloads rather than adapting discriminative-task benchmarks, and fold Circular Economy thinking directly into the metric set (not just as a discussion point) via a dedicated Circular Economy Score alongside four more conventional performance/efficiency pillars. Then use that methodology empirically to test a specific, provocative hypothesis: that repurposed older consumer hardware (a legacy discrete GPU) can outperform modern low-power edge SoCs for LLM inference, which — if true — reframes "sustainable Edge AI" as partly about hardware lifecycle extension rather than only newer, more efficient silicon.

## Technical contribution

A five-pillar evaluation methodology (Circular Economy Score, Joules/Token, Tokens/Second, BERTScore semantic accuracy, end-to-end latency) specifically designed for generative/LLM edge workloads, distinct from discriminative-task edge benchmarks. An empirical cross-hardware study spanning five genuinely different device classes (Raspberry Pi 4, Raspberry Pi 5, NVIDIA Jetson Nano, NVIDIA T400, NVIDIA GTX 1050 Ti) under a common runtime (Ollama, 4-bit quantized models) — a breadth of hardware comparison distinct from most single-platform edge-LLM deployment papers.

## Experimental methodology

Five hardware classes benchmarked under a shared harness: Ollama runtime, 4-bit-quantized LLMs, measuring the five LEAF pillars per device. (Full model list, task set for semantic-accuracy/BERTScore evaluation, and per-device absolute numbers beyond the headline comparison are in the full text, not yet verified in this pass.)

## Results

Headline result: the repurposed legacy NVIDIA GTX 1050 Ti workstation GPU achieved a 20x speedup over the Raspberry Pi 4 and better energy-per-task efficiency than low-power ARM architectures, by minimizing active runtime (i.e., finishing the task faster more than compensates for the older GPU's higher instantaneous power draw). This directly contradicts the assumption that newer, purpose-built edge SoCs are necessary for good sustainable-AI outcomes.

## Comparison with the state of the art

Positioned explicitly against "existing edge benchmarking frameworks" as being tailored to discriminative tasks (object detection is the paper's own example) and therefore not fit for purpose for generative AI evaluation — LEAF's contribution is filling that methodological gap rather than improving on a prior generative-specific benchmark. (Not yet verified against the full text's own related-work section.)

## Strengths

A genuinely novel axis (Circular Economy / hardware-lifecycle sustainability) folded directly into a quantitative metric rather than treated as a qualitative afterword. Broad, realistic hardware span (five classes from Raspberry Pi to discrete GPU) under one common runtime, making the cross-device comparison methodologically consistent. The headline finding is a real, checkable, counterintuitive empirical claim (not just a benchmark release) with direct implications for how EdgeAI hardware procurement and e-waste decisions might be made. Already shows independent uptake: at least one later 2026 MDPI paper (Giedra et al., a related LLM-inference benchmarking study) cites LEAF, suggesting the framework or its finding is being picked up outside the originating group.

## Weaknesses

Not yet verified from full text in this pass: the specific LLM models and their parameter counts, the semantic-accuracy task set BERTScore was computed against, and whether the "20x speedup" and "better energy-per-task efficiency" claims are consistent across all five hardware classes or specific to the GTX 1050 Ti vs. Raspberry Pi 4 comparison. Comparing a discrete desktop-class GPU (even an older one) against ARM SBCs conflates two different axes — raw compute capability and hardware lifecycle/circularity — and it's not yet clear from the abstract alone how LEAF's Circular Economy Score disentangles "old but powerful" from "genuinely resource-efficient."

## Limitations

This record has not verified the full paper text; treat the specific numeric claims here as abstract-level until independently checked. The five-hardware-class study, however broad relative to typical single-platform edge-LLM papers, still does not include genuinely MCU-class hardware (Cortex-M/RISC-V-NPU tier) that is the floor of this Observatory's core taxonomy — all five devices (even the Raspberry Pis) are full Linux-capable SBC/GPU-class systems.

## Open questions

Does the "repurposed legacy hardware beats purpose-built edge SoC" finding hold across a wider range of LLM sizes and quantization levels, or is it specific to the models tested? How does LEAF's Circular Economy Score weight embodied carbon / manufacturing footprint of new silicon against the operational energy savings newer SoCs might offer at scale — i.e., is the 20x speedup finding robust to a full lifecycle-carbon accounting, or only to operational energy-per-task?

## Possible extensions

Full-text verification pass to confirm model list, task set, and per-device numbers, and to extract the paper's own defined formula for the Circular Economy Score (not available from the abstract). Apply the LEAF methodology to genuinely MCU/NPU-class hardware (the gap this Observatory's own [[MoE_Edge_LLM_Serving]] cluster and the mcu-npu-measurement-infrastructure consolidation candidate have both flagged) to see whether the "repurposed hardware wins" finding extends that far down the hardware stack or breaks down.

## Relevance to our research

Founding anchor, alongside [[2026_Giorgetti_VQAEdge]], of the new [[Generative_EdgeAI]] concept under Applications. Genuinely independent of the Giorgetti/Pau/Berta cluster (different institutions, different modality focus — pure-text LLM benchmarking here vs. multimodal VQA tutorial there, different methodology — systematic benchmarking framework vs. practical system tutorial) — this independence is what clears this Observatory's two-independent-anchor bar for formalizing a new taxonomy node, rather than treating Generative EdgeAI as a single research group's framing. Also a natural complement to [[MoE_Edge_LLM_Serving]]'s hardware-tier open question ("where does edge-native stop being edge") — LEAF's own hardware span (Pi 4/5, Jetson Nano, T400, GTX 1050 Ti) sits in a similar workstation/SBC/edge-GPU tier to that cluster's FreeToken/PolyQ/HeteroMosaic papers, and its sustainability framing (hardware lifecycle extension) adds a dimension — environmental/circularity — not yet present in that cluster's open problems.

## Possible thesis topics

Extending LEAF's methodology to MCU/NPU-class hardware to test whether its "repurposed hardware wins" finding holds at the true TinyML tier, bridging this concept, [[MoE_Edge_LLM_Serving]], and the mcu-npu-measurement-infrastructure consolidation candidate (Master's/PhD, contingent on full-text verification of the methodology first).

## Possible collaborations

Not yet identified — authors' institutional affiliations not verified in this pass (full text needed).

## Links to related papers

Founding anchor of [[Generative_EdgeAI]] together with [[2026_Giorgetti_VQAEdge]]. Already cited by at least one later 2026 MDPI paper on LLM inference benchmarking (Giedra et al.) — worth checking whether that paper belongs in this Observatory's KB too if the [[Generative_EdgeAI]] concept grows.
