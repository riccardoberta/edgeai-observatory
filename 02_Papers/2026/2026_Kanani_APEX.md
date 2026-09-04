# APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference

**Full citation:** Kanani, A., Badawi, L., Ogras, U. Y. (2026). APEX: Adaptive Expert Prefetching for Memory-Efficient Edge MoE Inference. arXiv:2608.11688 [cs.AR, cs.AI, cs.LG]. Submitted 12 Aug 2026. Accepted at IEEE/ACM ESWEEK (CODES) 2026; official version to appear in IEEE TCAD. License CC BY-NC-ND 4.0. DOI: 10.48550/arXiv.2608.11688.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2608.11688)

**Linked concepts:** core member of [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]]; adjacent to [[Compression]].

## Abstract summary

MoE models are attractive for edge deployment because they activate only a small parameter subset per token, but MoE inference at the edge is fundamentally memory-limited: expert parameters are large and often reside in off-chip memory, putting expert loading on the critical path. APEX is a predictive resource-management framework that overlaps expert loading with useful computation via a lightweight prefetch router with a learned confidence model, predicting candidate experts before the attention block runs and dynamically fetching additional experts. It achieves over 99% overlap accuracy, substantially outperforming fixed top-k prefetching. Two execution modes: a correctness-preserving mode with exact routing semantics, and a stall-free mode eliminating residual stalls with negligible accuracy impact. The correctness-preserving mode reduces per-token latency by up to 26% and improves energy-delay product by up to 41% over state-of-the-art baselines.

## Research problem

MoE models' sparse per-token activation is supposed to be their edge-deployment advantage (small active parameter subset per token), but that advantage is undermined by memory: the specific experts a token needs still have to be loaded from off-chip memory before compute can proceed, and that load is on the critical path. Fixed top-k prefetching (always speculatively loading the top-k most likely experts) is the field's existing approach, but it's not adaptive to how confident the router actually is about its predictions.

## Key idea

Predict which experts will be needed *before* the attention block that determines actual routing even runs, using a lightweight, learned confidence model — and let that confidence drive how many candidate experts to prefetch, rather than a fixed top-k. This lets loading overlap with useful computation (attention, and other in-flight work) instead of stalling the pipeline once routing is known and it's too late to prefetch. Two modes trade off differently: correctness-preserving guarantees exact routing semantics (prefetch is purely a latency optimization, never changes what runs); stall-free instead operates on whatever experts are already available when needed, accepting negligible accuracy loss to eliminate stalls entirely.

## Technical contribution

A learned, confidence-driven prefetch router operating before the attention block (rather than after routing is known, when it's too late) — over 99% overlap accuracy versus fixed top-k baselines; two clearly delineated execution modes (correctness-preserving vs. stall-free) exposing an explicit accuracy/latency/energy trade-off to the deploying system rather than hiding it; up to 26% per-token latency reduction and 41% energy-delay-product improvement in the correctness-preserving mode specifically, meaning these gains come with zero routing-semantics compromise.

## Experimental methodology

Evaluated across multiple MoE models, comparing APEX's two execution modes against state-of-the-art expert-loading baselines (including fixed top-k prefetching) on per-token latency, energy-delay product, and overlap accuracy (the fraction of prefetched experts that turn out to be correctly needed).

## Results

Over 99% overlap accuracy versus fixed top-k prefetching baselines. Correctness-preserving mode: up to 26% per-token latency reduction and up to 41% energy-delay-product improvement over state-of-the-art baselines. Stall-free mode: additional efficiency gains beyond the correctness-preserving mode, with negligible impact on application accuracy (implying it is used when the small residual staleness is deemed acceptable for the deployment).

## Comparison with the state of the art

Directly benchmarked against fixed top-k prefetching techniques (the field's existing approach) and against unspecified "state-of-the-art baselines" on latency and energy-delay product. Expert prefetching as a general idea is not new; APEX's specific contribution — a learned, confidence-driven predictor operating before the attention block, with a formally correctness-preserving mode alongside a stall-free relaxation — is, per the 2026-08-13 digest, "a well-engineered systems contribution with a clean accuracy/latency/energy trade-off exposed to the user."

## Strengths

The >99% overlap-accuracy figure is a strong, directly checkable claim (not a vague qualitative improvement); the two-mode design (correctness-preserving vs. stall-free) is unusually transparent about the trade-off it's making, rather than presenting a single blended result; predicting before the attention block, rather than reactively after routing, is a genuinely different mechanism from fixed top-k, not just a tuned version of it; ESWEEK/CODES acceptance with an IEEE TCAD follow-on signals solid peer review.

## Weaknesses

The abstract does not specify what hardware class ("edge MoE inference") the evaluation targets — edge-GPU-class or MCU/NPU-class hardware make very different demands on a prefetch router's compute budget, and this ambiguity is a recurring issue across the whole MoE-serving cluster this paper belongs to; no comparison is given against the other members of the same cluster (EdgeXpert, UnionSparse), so it's unclear whether APEX's prefetching gains are additive with or redundant against those papers' hardware-co-design or index-efficiency approaches.

## Limitations

As a purely prefetching-based approach, APEX's ceiling is bounded by how predictable expert routing actually is for a given model/workload — for models or inputs where routing is genuinely hard to predict ahead of the attention block, the learned confidence model's >99% overlap accuracy may not hold, and the paper does not characterize this failure mode at the abstract level.

## Open questions

Is there a combined design point that stacks APEX's prefetching with EdgeXpert's hardware-software co-designed loading and UnionSparse's low-bit sparse storage format — do the three mechanisms compose, or do they conflict (e.g., over prefetch buffer allocation)? Is edge MoE inference (with APEX-style prefetching or otherwise) feasible on true MCU-class targets given their far tighter memory budgets, or does per-expert loading make MoE fundamentally unsuited below some memory floor?

## Possible extensions

Build the combined design point suggested by the 2026-08-13 digest: APEX-style prefetching feeding an EdgeXpert-style coalesced-loading accelerator, storing weights in UnionSparse's low-bit sparse format — and identify where the three mechanisms' assumptions conflict; characterize the failure mode where routing is genuinely hard to predict ahead of the attention block, and how gracefully the confidence model degrades in that regime.

## Relevance to our research

A core member of the "Mixture-of-Experts (MoE) & Edge LLM Serving" taxonomy cluster formalized 2026-08-25 — the top-ranked candidate from the 2026-08-13 digest for its clear mechanism and strong, checkable reported gains. Adjacent to [[Compression]] in spirit (managing what to load and when) without being a compression technique itself.

## Possible thesis topics

Unifying edge-MoE memory management: build the combined design point stacking APEX's prefetching, EdgeXpert's hardware-software co-designed coalesced loading, and UnionSparse's low-bit sparse storage, and map where the mechanisms conflict (PhD-scale, per the 2026-08-13 digest's explicit hook; bridges [[Compression]], [[Quantization]], and the new MoE/Edge-LLM-Serving taxonomy node). MCU-class MoE feasibility study: is edge MoE inference feasible on true MCU-class targets ([[Cortex-M]], [[RISC-V]]) given their tighter memory budgets, using APEX's prefetching as the test mechanism (Master's/PhD, per the same digest).

## Possible collaborations

Umit Y. Ogras's group, given APEX's IEEE/ACM ESWEEK (CODES) acceptance and TCAD follow-on — a natural fit for edge-systems memory-management collaboration.

## Links to related papers

Part of the "edge MoE inference" cluster identified in the 2026-08-13 digest alongside EdgeXpert (arXiv:2608.05303, `02_Papers/2026/2026_Ha_EdgeXpert.md`) and UnionSparse (arXiv:2608.09291, `02_Papers/2026/2026_Jiang_UnionSparse.md`) — the digest explicitly suggested a joint deep-analysis pass comparing the three approaches, which this trio of records now enables.
