# EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding

**Full citation:** Ha, S., Seo, H., Jo, Y., Moon, Y., Yoo, H.-J. (2026). EdgeXpert: An Edge Device for Memory-Efficient LLM Inference with Mixture-of-Experts and Speculative Decoding. arXiv:2608.05303 [cs.AR, cs.CL, cs.LG]. Submitted 5 Aug 2026. Accepted at the 59th IEEE/ACM International Symposium on Microarchitecture (MICRO 2026). ACM classes C.1.3, B.7.1, I.2.7. DOI: 10.48550/arXiv.2608.05303.

**Linked concepts:** core member of [[Mixture-of-Experts (MoE) & Edge LLM Serving]].

## Abstract summary

On-device LLM deployment is bottlenecked by external memory access (EMA) in feed-forward network layers. Speculative decoding (multiple tokens per stage) and MoE (sparse expert activation) are both promising individually, but the paper identifies a fundamental incompatibility when combining them. EdgeXpert is a software-hardware co-designed LLM accelerator resolving this: in the prefill stage, prompt-wise expert reuse reformulates routing as prompt-level rather than per-token expert selection, using a lightweight encoder to identify important tokens and construct a shared expert set, routing less-important tokens with a reduced expert budget; in the decode stage, depth-aware expert coalescing exploits contextual similarity and mutual exclusivity of same-depth candidate tokens, loading only salient channels rather than the union of all required channels, with computational calibration recovering accuracy without extra memory access. Synthesized in Samsung 28nm at 800 MHz, it achieves up to 56.3% latency reduction and 44.1% energy reduction versus prior work, with near-baseline accuracy.

## Research problem

Speculative decoding reduces decoding stages by generating multiple candidate tokens per stage; MoE reduces per-stage cost by activating only a sparse subset of experts. Both individually target the same goal — reducing the external memory access that dominates LLM inference cost on-device — but the paper identifies that combining them naively doesn't work: speculative decoding's multiple simultaneously-generated candidate tokens each may want to route to different experts, and MoE's per-token routing decision doesn't compose cleanly with speculative decoding's parallel generation, undermining the memory-access savings either technique alone would provide.

## Key idea

Resolve the MoE/speculative-decoding incompatibility at each pipeline stage differently. In prefill: reformulate routing as prompt-level rather than strictly per-token, using a lightweight encoder to find important tokens, build one shared expert set from them, and route the less-important remaining tokens through a reduced expert budget — trading a small amount of per-token routing precision for a shared, coalesced expert-loading pattern. In decode: exploit the fact that same-depth speculative candidate tokens tend to be contextually similar and mutually exclusive (only one will actually be accepted), so rather than loading the union of channels all candidates might need, load only the salient channels and use a computational-calibration step to recover the resulting accuracy loss without any additional memory access.

## Technical contribution

Identification and formal resolution of the specific incompatibility between speculative decoding and MoE routing, rather than treating the two techniques independently as prior work does; prompt-wise expert reuse for the prefill stage; depth-aware expert coalescing for the decode stage, exploiting speculative-candidate contextual similarity/mutual exclusivity; a computational-calibration mechanism that recovers accuracy from the coalescing approximation without extra memory access; a full hardware-software co-designed accelerator synthesized in real silicon (Samsung 28nm, 800MHz) rather than only simulated.

## Experimental methodology

Synthesized in Samsung 28nm CMOS technology at 800MHz. Evaluated latency and energy versus prior work (unspecified baselines at the abstract level), with accuracy reported as "near-baseline" — implying comparison against an unquantized/uncoalesced reference.

## Results

Up to 56.3% latency reduction and 44.1% energy reduction versus prior work, with near-baseline accuracy — synthesized silicon numbers, not simulation, giving these figures real hardware grounding.

## Comparison with the state of the art

The paper's central comparison is conceptual and architectural: prior work treats speculative decoding and MoE as independent optimizations; EdgeXpert's contribution is specifically resolving their interaction. Quantitatively benchmarked against unspecified "prior work" on latency/energy — the 2026-08-13 digest notes this was independently corroborated via a targeted Google Scholar cross-check that cycle, adding some confidence beyond the abstract alone.

## Strengths

Identifying and solving a specific *interaction* problem between two established techniques (rather than proposing yet another standalone optimization) is a genuinely different kind of contribution — architectural insight, not just an incremental result; grounded in real Samsung 28nm synthesized silicon rather than simulation alone, giving the reported gains stronger reproducibility credibility; MICRO 2026 acceptance signals rigorous peer review at a top computer-architecture venue; the prefill/decode-stage-specific solutions (prompt-wise reuse vs. depth-aware coalescing) show the authors reasoned about where in the pipeline the incompatibility actually bites, rather than applying one generic fix everywhere.

## Weaknesses

"Prior work" is not named at the abstract level, making it hard to assess exactly how strong a comparison baseline the 56.3%/44.1% figures represent; the computational-calibration step that recovers accuracy from the decode-stage channel-coalescing approximation is described only functionally, not in enough detail (at the abstract level) to assess its own overhead or limits; like the rest of this cluster, the hardware class (custom Samsung 28nm ASIC) sits above the MCU/NPU tier this lab typically targets, and reproducing custom-silicon results without tape-out access is a real practical barrier.

## Limitations

The prompt-wise expert-reuse trick in prefill trades routing precision (shared expert set across "important" tokens, reduced budget for others) for memory-access savings — how much this costs in accuracy versus true per-token routing, independent of the reported "near-baseline" headline, is not detailed at the abstract level and would need full-PDF verification before citing in a survey.

## Open questions

Does the prompt-wise expert-reuse and depth-aware coalescing approach generalize to MoE models with very different routing sparsity patterns than whatever was tested, or is it tuned to a specific model family? Is there a combined design point stacking EdgeXpert's hardware-software co-design with APEX's prefetching and UnionSparse's low-bit sparse storage — the same unifying question the 2026-08-13 digest raised across all three MoE-memory papers?

## Possible extensions

Build the combined edge-MoE-memory design point the 2026-08-13 digest suggests: EdgeXpert-style coalesced loading fed by APEX-style prefetching, storing weights in UnionSparse's low-bit sparse format; characterize the accuracy cost of prompt-wise expert reuse specifically (isolated from the decode-stage coalescing) via full-PDF verification.

## Relevance to our research

A core member of the "Mixture-of-Experts (MoE) & Edge LLM Serving" taxonomy cluster formalized 2026-08-25, and one of the strongest deep-analysis candidates in the whole backlog given its MICRO-caliber architectural contribution and real silicon numbers.

## Possible thesis topics

Unifying edge-MoE memory management: build the combined design point stacking APEX (prefetching), EdgeXpert (hardware-software co-design), and UnionSparse (index-efficient sparsity) and identify where the mechanisms conflict (PhD-scale, per the 2026-08-13 digest's explicit hook).

## Possible collaborations

Hoi-Jun Yoo's group (per the author list), given EdgeXpert's MICRO-caliber, real-silicon LLM accelerator work — a natural fit for any lab work on custom edge-LLM accelerator design.

## Links to related papers

Part of the "edge MoE inference" cluster identified in the 2026-08-13 digest alongside APEX (arXiv:2608.11688, `02_Papers/2026/2026_Kanani_APEX.md`) and UnionSparse (arXiv:2608.09291, `02_Papers/2026/2026_Jiang_UnionSparse.md`) — the digest explicitly suggested a joint deep-analysis pass comparing the three, now possible with all three recorded.
