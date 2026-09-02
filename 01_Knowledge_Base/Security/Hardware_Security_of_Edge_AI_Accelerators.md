# Hardware Security of Edge AI Accelerators

## Evolution of the concept

Created in the 2026-09-02 Knowledge Base Consolidation cycle, promoting a consolidation candidate (`edge-ai-hardware-physical-security`) that had accumulated two independent anchor papers three weeks apart. This is the Observatory's first Knowledge Base concept addressing security rather than efficiency, and the first entry under a new top-level taxonomy branch, Security — model-level and cloud-side security research is well established elsewhere, but as LLM inference moves onto edge AI accelerator silicon, the accelerator itself becomes part of the attack surface in ways the Observatory's existing Algorithms/Frameworks/Hardware/Applications structure does not capture.

The two anchor papers address different threat models that share a common concern — protecting the confidentiality of model weights, activations, and other inference state on edge AI accelerator hardware:

[[2026_Fang_YAVIN]] (13 Aug 2026) is a *defensive*, architectural contribution: it extends a trusted execution environment (TEE) beyond the processor into a dedicated processing-in-memory (PIM) region, treating the memory bus itself — the channel between processor and PIM — as untrusted. Its overhead is measured specifically on quantized edge-class LLM execution (34% for INT8, 9.3% for INT32, relative to unencrypted execution), directly connecting the security architecture to on-device LLM deployment costs.

[[2026_Mehta_LLMscope]] (26 Aug 2026) is an *offensive* contribution demonstrating the opposite direction: using laser voltage imaging, it physically extracts LLM weights, activations, and other inference state from an FPGA-based edge LLM accelerator, exploiting the fact that such accelerators reuse the same buffers and compute subcircuits across addresses, tiles, modules, and layers — a design choice typically made for area/power efficiency, not anticipating this as an attack surface. The attack achieves full recovery of targeted values and its cost scales only linearly with asset size.

These two papers are grouped under one concept, with two named variants, rather than split into separate concepts, because the underlying concern is the same (confidentiality of model state on edge accelerator hardware) and because the natural next research question directly connects them (see Open problems below) — splitting now would separate two halves of what is really one question. Revisit this decision and consider forking into two concepts (e.g., "Trusted Execution / Confidential Computing for Edge AI" vs. "Physical & Side-Channel Attacks on Edge AI Accelerators") if the literature in either direction grows enough that they stop informing each other directly.

A 2026 historical-backfill pass added a third, earlier reference point that predates and structurally frames both 2026 anchors: Dubey et al.'s 2022 ACM JETC survey of physical (power/EM) side-channel attacks and countermeasures for ML hardware. This is a genuinely distinct threat model from both existing variants — not bus-level eavesdropping (YAVIN) and not optical/laser probing (LLMscope) — and its existence as a longer-established, peer-reviewed literature underscores that this concept's two 2026 anchors are instances of a broader physical-security problem for ML accelerators that research has been tracking since at least the early 2020s.

## Variants

**Architectural trust-boundary extension (trusted execution / confidential computing).** Extends a TEE's cryptographic trust boundary to cover previously-untrusted components (e.g., PIM-capable memory) so that computation can happen on encrypted-then-decrypted data without ever leaving the trust boundary. Anchor: [[2026_Fang_YAVIN]].

**Physical / side-channel extraction.** Exploits physical properties of accelerator silicon (e.g., buffer and subcircuit reuse across logical addresses) to read out model assets directly from the physical substrate during execution, bypassing any purely logical/cryptographic trust boundary. Anchor: [[2026_Mehta_LLMscope]].

**Power/EM side-channel leakage.** Exploits power consumption or electromagnetic emissions during computation to infer model weights, activations, or inference state, a longer-established threat model distinct from both bus-eavesdropping and optical/laser probing — addressed via masking-style countermeasures rather than trust-boundary extension or physical shielding alone. Anchor: [[2022_Dubey_GuardingMLHardwareSideChannel]].

## Open problems

Does an architectural trust-boundary defense such as YAVIN's provide any protection against a physical probing attack such as LLMscope's? YAVIN treats the memory bus as the untrusted channel and encrypts data crossing it; LLMscope reads state directly off the physical substrate (via laser voltage imaging) rather than off the bus, which suggests the two threat models may be largely orthogonal — a TEE/PIM architecture could be cryptographically sound against bus-level eavesdropping while remaining fully exposed to physical probing of the memory or compute subcircuits themselves. This has not been tested by either paper and is, at present, the single most important open question tying this concept's two variants together.

What do effective countermeasures against physical probing (address randomization, buffer partitioning, physical shielding) cost in area and power — and are they compatible with the buffer/subcircuit reuse that LLMscope exploits, given that reuse is itself usually a deliberate area/power optimization? This creates a potential tension between the efficiency goals that dominate the rest of this Observatory's taxonomy and physical security.

Does either threat model's severity vary systematically across accelerator classes (FPGA, custom ASIC, NPU, systolic array, in-memory-computing designs)? LLMscope's validation is FPGA-specific; whether custom-ASIC or NPU designs reuse buffers/subcircuits in comparable ways — and are therefore comparably vulnerable — is untested.

## Key papers

[[2026_Fang_YAVIN]] — unified trusted computing base extending TEE trust into processing-in-memory; first PIM implementations of LightSaber KEM (post-quantum) and ASCON-128; overhead measured on quantized edge-class LLM execution.

[[2026_Mehta_LLMscope]] — laser voltage imaging attack recovering LLM weights, activations, and inference state from an FPGA-based edge accelerator by exploiting buffer/subcircuit reuse; full recovery demonstrated; recovery cost scales linearly with asset size.

[[2022_Dubey_GuardingMLHardwareSideChannel]] — survey of physical (power/EM) side-channel attacks and countermeasures for ML hardware, a third, earlier-established threat model distinct from bus-eavesdropping and optical-probing; ACM JETC.

## Research ideas

A systematic comparative study of which edge accelerator architectures (NPU designs, systolic arrays, in-memory-computing designs) are structurally more or less vulnerable to physical/side-channel extraction, and what countermeasures cost in area/energy. An evaluation of whether a YAVIN-style architectural trust boundary offers any defense-in-depth against LLMscope-style physical probing, or whether the two threat models require entirely independent countermeasure strategies. Measuring YAVIN's security overhead across the fuller quantization spectrum this Observatory already tracks (INT4, mixed-precision), not just the INT8/INT32 points reported so far.

## Possible thesis topics

Threat-modeling edge AI accelerators beyond optical probing: a systematic comparative study of structural vulnerability to physical/side-channel extraction across accelerator architectures, with a countermeasure area/energy cost analysis (PhD-scale; bridges hardware architecture and security).

A second data point for trusted PIM: measure YAVIN's TEE-into-PIM overhead across the full INT8/INT4/mixed-precision quantization spectrum, and determine whether trusted PIM changes the accuracy/latency/security Pareto front for on-device LLM inference (Master's/PhD; bridges [[Quantization]] and this concept).

## Links

[[Quantization]] (YAVIN's overhead is measured specifically on quantized edge-class LLM execution), [[FPGA]] (LLMscope's validated attack platform), [[NPU]], [[Mixture-of-Experts (MoE) & Edge LLM Serving]] (YAVIN evaluates on the same quantized edge-LLM execution regime that concept's serving systems target — a security/serving crossover worth tracking if it recurs)
