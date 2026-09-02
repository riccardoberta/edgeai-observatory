# Knowledge Base Consolidation — 2026-09-02

## Scope Reviewed

This is the Observatory's first Knowledge Base Consolidation cycle, run on explicit request. No prior consolidation report exists, so the review covered the full accumulated evidence base: `00_Config/sources.yaml`, `00_Config/consolidation_candidates.yaml` (five bootstrapped candidates), `00_Config/consolidation_history.yaml` (empty), `00_Taxonomy/taxonomy.md` (including its full "Evolution notes" history back to 2026-06-30), all 23 `01_Knowledge_Base/` concept pages, the `02_Papers/2026/` records most relevant to the candidate queue, all ten Weekly Digests (2026-06-29 through 2026-09-02), and all three Monthly Reports (June, July, August 2026).

## Main Signals

Two candidates in the queue were marked `ready_for_review`; three were `watching`. Both `ready_for_review` candidates were mature: each had two or more independent evidence points spanning weeks, explicit cross-references in the taxonomy's own evolution notes, and (for the boundary-definition candidate) an explicit proposal in the August monthly report for how it might be formalized. While reviewing the candidate queue against the taxonomy file directly, this cycle also found a structural gap the queue itself did not flag: the "Mixture-of-Experts (MoE) & Edge LLM Serving" taxonomy entry, added to `taxonomy.md` on 2026-08-25 and grounded by seven already-verified `02_Papers/` records, had never been given a corresponding `01_Knowledge_Base/` concept page — only the taxonomy bullet existed. This is exactly the kind of inconsistency this task's scan-beyond-the-queue mandate is meant to catch.

## Existing Concepts Updated

None of the 21 pre-existing `01_Knowledge_Base/` concept pages required substantive updates this cycle — the evidence reviewed did not extend, refine, or challenge any of them beyond the two actions below. `[[2026_Fang_YAVIN]]`'s "Linked concepts", "Relevance to our research", and "Links to related papers" sections were updated to point at the newly created Security concept instead of describing an open taxonomy gap, and six other `02_Papers/` records (FreeToken, APEX, EdgeXpert, UnionSparse, PolyQ, HeteroMosaic, "Is Your NPU Ready for LLMs?") had their "Linked concepts" lines updated from prose references to the "MoE & Edge LLM Serving taxonomy cluster formalized 2026-08-25" into proper `[[Mixture-of-Experts (MoE) & Edge LLM Serving]]` wikilinks pointing at the new concept page, so the knowledge graph is now actually navigable rather than only textually described.

## New Concepts Added

**Mixture-of-Experts (MoE) & Edge LLM Serving** (`01_Knowledge_Base/Algorithms/MoE_Edge_LLM_Serving.md`). Not itself a queue candidate, but a gap discovered by cross-referencing the queue against the taxonomy file (see Main Signals). Built from seven already-verified `02_Papers/` records spanning July–August 2026 (the diagnostic study "Is Your NPU Ready for LLMs?", HeteroMosaic, PolyQ, APEX, EdgeXpert, UnionSparse, FreeToken), tracing the cluster's evolution from diagnosis (NPU/CPU prefill-decode phase mismatch) through scheduling and compiler responses to MoE-specific memory-management co-design, and culminating in FreeToken's edge-native serving system. Its central, still-open problem — where "edge-native" stops being edge — absorbs the `edge-native-boundary-definition` candidate (see Candidates Rejected/Merged below). Three further papers from the 2026-09-02 weekly digest (mzCache, Just Talk Once, a block-diffusion-LLM hardware accelerator) are noted as accumulating evidence but are explicitly flagged as not yet independently re-verified from primary sources by this cycle — evidence so far comes from the weekly digest's own abstract-level review.

**Hardware Security of Edge AI Accelerators** (`01_Knowledge_Base/Security/Hardware_Security_of_Edge_AI_Accelerators.md`), under a newly created top-level **Security** taxonomy branch. Promotes the `edge-ai-hardware-physical-security` candidate, anchored by two independent papers verified directly against their arXiv abstract pages this cycle: YAVIN (arXiv:2608.13496, architectural TEE-into-PIM trust-boundary extension) and LLMscope (arXiv:2608.25321, laser-voltage-imaging physical extraction attack, newly given a `02_Papers/` record this cycle — `2026_Mehta_LLMscope.md`). Kept as one concept with two named variants rather than split into two, since the natural next research question (does an architectural trust boundary defend against physical probing?) directly connects them.

## Paper Analyses Added or Updated

One new paper analysis: `02_Papers/2026/2026_Mehta_LLMscope.md`, created because LLMscope is a primary anchor for the new Security concept (per the Observatory's conservative bar for `02_Papers/` records). Verified against its arXiv abstract page (arXiv:2608.25321, submitted 26 Aug 2026, cs.CR/cs.AI) before writing. One existing analysis updated: `02_Papers/2026/2026_Fang_YAVIN.md` (re-verified against its arXiv abstract page, arXiv:2608.13496, confirming the 20×/34%/9.3% figures already recorded), with its concept links repointed to the new Security concept. No other new paper analyses were created this cycle — the three additional MoE-cluster papers surfaced in the 2026-09-02 digest (mzCache, Just Talk Once, the block-diffusion accelerator) were judged not yet to meet the bar for a persistent `02_Papers/` record on their own (each is one data point, not yet a primary anchor for a distinct concept), consistent with the Observatory's "quality over quantity" principle; they are noted as pipeline evidence in the new MoE concept page instead.

## Candidates Kept Under Observation

All three `watching` candidates were reviewed and deliberately left as `watching`, unchanged, because none has gained the second independent anchor paper the taxonomy's own methodology (set 2026-08-25) requires before formalization:

- **Standardized Measurement Infrastructure for MCU/NPU-Class Edge Inference** (`mcu-npu-measurement-infrastructure`) — still anchored only by the August monthly report's synthesis of Hydra and the Apple Neural Engine study, neither of which targets the MCU/NPU tier itself.
- **Event-Driven / Neuromorphic ASIC Accelerators** (`neuromorphic-event-driven-asic-hardware-gap`) — still anchored only by ETHEREAL.
- **In-Memory Computing with Emerging Non-Volatile Memory** (`in-memory-computing-emerging-nvm-hardware-gap`) — still anchored only by FALCON, first seen this same cycle's weekly digest (2026-09-02), so a second anchor could not plausibly have appeared yet.

These remain observations, not promotions — no Knowledge Base content was created or implied for any of them.

## Candidates Rejected

None. Both `ready_for_review` candidates had sufficient independent evidence and were resolved (one promoted, one merged); none of the reviewed material was judged too incremental, unsupported, or unlikely to improve the Observatory's conceptual representation.

## Knowledge Graph Changes

Two new nodes added to the graph (Mixture-of-Experts (MoE) & Edge LLM Serving; Hardware Security of Edge AI Accelerators), with a new cross-concept edge between them (YAVIN's quantized-edge-LLM security evaluation touches the same execution regime the MoE/serving concept's systems target). Eight `02_Papers/` records (YAVIN, LLMscope, FreeToken, APEX, EdgeXpert, UnionSparse, PolyQ, HeteroMosaic, "Is Your NPU Ready for LLMs?" — nine total) now carry proper wiki-style-resolvable "Linked concepts" pointing at these two concept pages, replacing prose descriptions of an unformalized taxonomy cluster. A new top-level Security branch was added to `00_Taxonomy/taxonomy.md`, alongside a new evolution note (dated 2026-09-02) documenting both decisions and explicitly recording the taxonomy/Knowledge-Base inconsistency this cycle found and fixed, so future cycles do not need to re-discover it.

## Emerging Research Questions

The single most important open question surfaced by this cycle is not from either promoted concept individually but from their intersection: does an architectural trust-boundary defense (YAVIN's TEE-into-PIM) provide any protection against a physical probing attack (LLMscope's laser voltage imaging), given that the two operate on entirely different channels (the memory bus vs. the physical substrate)? Neither paper tests this, and it is the clearest next step for anyone extending either line of work. Within the MoE & Edge LLM Serving concept, the "how edge is edge" question remains genuinely unresolved after four digests and one monthly report naming it — the field keeps articulating the tension without proposing a testable quantitative boundary, which is itself worth noting as a gap in the literature rather than just in the Observatory's taxonomy.

## Potential Thesis and Research Opportunities

Grounded in the material actually reviewed this cycle (not generic brainstorming):

Threat-modeling edge AI accelerators beyond optical probing — a systematic comparative study of which accelerator architectures (NPU, systolic array, in-memory-computing designs) are structurally more or less vulnerable to physical/side-channel extraction, with a countermeasure area/energy cost analysis (PhD-scale, bridging hardware architecture and the new Security concept).

A second data point for trusted PIM — measuring YAVIN's TEE-into-PIM overhead across the fuller INT8/INT4/mixed-precision quantization spectrum this Observatory already tracks, rather than only the INT8/INT32 points reported so far (Master's/PhD, bridging [[Quantization]] and the Security concept).

Quantifying the edge-native boundary — proposing and empirically validating a criterion (memory budget, power envelope, or cost tier) separating "edge-native" MoE/LLM serving from genuine TinyML deployment, anchored to MLPerf Tiny's and MLPerf Inference's own device-class definitions (Master's-scale position/measurement study).

Unifying edge-MoE memory management — implementing and benchmarking the combined design point APEX, EdgeXpert, and UnionSparse each independently propose but none has built (prefetching feeding coalesced loading feeding index-efficient sparse storage), characterizing where the three mechanisms' assumptions conflict (PhD-scale).

Porting edge-native MoE serving toward true MCU-class hardware — taking FreeToken's bandwidth-adaptive execution model (or a comparable cluster mechanism) and characterizing where its assumptions break down as hardware scales down toward Cortex-M/RISC-V-class targets (Master's/PhD).

## Knowledge Base consistency review (addendum)

A review of the affected areas (the Algorithms branch and the new Security branch, plus all `02_Papers/` records touched this cycle) found no duplicate concepts, no inconsistent terminology, no contradictory descriptions, and no broken wiki-style links introduced by this cycle's changes. The one inconsistency found — the MoE & Edge LLM Serving taxonomy entry without a matching Knowledge Base page — was fixed as described above. Reciprocal links were checked and added in both directions between the two new concepts and their anchor papers, and between the two new concepts themselves. No taxonomy expansion beyond the one new top-level branch (Security) judged necessary was made; the three `watching` candidates were deliberately left unformalized rather than expanding the taxonomy further without a second independent anchor.
