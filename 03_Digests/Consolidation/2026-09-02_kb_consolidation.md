# Knowledge Base Consolidation — 2026-09-02

A cross-cutting synthesis pass over the accumulated Knowledge Base, connecting concepts and papers that individual weekly and monthly entries treated separately. Two new concepts were formalized from this review: [[MoE_Edge_LLM_Serving]] (Algorithms) and [[Hardware_Security_of_Edge_AI_Accelerators]] (Security) — both are documented in full on their own Knowledge Base pages; this note preserves the cross-concept questions the review surfaced.

## Emerging research questions

Does an architectural trust-boundary defense (YAVIN's TEE-into-PIM) provide any protection against a physical probing attack (LLMscope's laser voltage imaging), given that the two operate on entirely different channels — the memory bus versus the physical substrate? Neither paper tests this, and it is the clearest next step for anyone extending either line of work; see [[Hardware_Security_of_Edge_AI_Accelerators]].

Within [[MoE_Edge_LLM_Serving]], the "how edge is edge" question remains genuinely unresolved: the field keeps articulating the tension between edge-native serving (laptop/workstation-scale MoE deployment) and genuine TinyML on-device inference without proposing a testable quantitative boundary — itself worth noting as a gap in the literature.

## Potential thesis and research opportunities

Threat-modeling edge AI accelerators beyond optical probing — a systematic comparative study of which accelerator architectures (NPU, systolic array, in-memory-computing designs) are structurally more or less vulnerable to physical/side-channel extraction, with a countermeasure area/energy cost analysis (PhD-scale, bridging hardware architecture and [[Hardware_Security_of_Edge_AI_Accelerators]]).

A second data point for trusted processing-in-memory — measuring YAVIN's TEE-into-PIM overhead across the fuller INT8/INT4/mixed-precision quantization spectrum, rather than only the INT8/INT32 points reported so far (Master's/PhD, bridging [[Quantization]] and [[Hardware_Security_of_Edge_AI_Accelerators]]).

Quantifying the edge-native boundary — proposing and empirically validating a criterion (memory budget, power envelope, or cost tier) separating "edge-native" MoE/LLM serving from genuine TinyML deployment, anchored to MLPerf Tiny's and MLPerf Inference's own device-class definitions (Master's-scale position/measurement study; [[MoE_Edge_LLM_Serving]]).

Unifying edge-MoE memory management — implementing and benchmarking the combined design point APEX, EdgeXpert, and UnionSparse each independently propose but none has built (prefetching feeding coalesced loading feeding index-efficient sparse storage), characterizing where the three mechanisms' assumptions conflict (PhD-scale; [[MoE_Edge_LLM_Serving]]).

Porting edge-native MoE serving toward true MCU-class hardware — taking FreeToken's bandwidth-adaptive execution model (or a comparable cluster mechanism) and characterizing where its assumptions break down as hardware scales down toward [[Cortex-M]]/[[RISC-V]]-class targets (Master's/PhD).
