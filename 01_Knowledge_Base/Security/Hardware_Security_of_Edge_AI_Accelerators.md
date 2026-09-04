# Hardware / Physical Security of Edge AI Accelerators

This concept covers attacks and defenses at the hardware level for edge AI accelerators: extracting a model's architecture or weights by observing power consumption, electromagnetic emissions, or other physical side channels; and defenses such as extending a Trusted Execution Environment's (TEE's) protection boundary beyond the CPU into memory or accelerator-adjacent hardware. Model-level and cloud-side security research is well established elsewhere, but as LLM inference moves onto edge AI accelerator silicon, the accelerator itself becomes part of the attack surface in a way that efficiency-focused hardware research does not address.

Two anchor papers address different threat models that share a common underlying concern: protecting the confidentiality of model weights, activations, and other inference state on edge AI accelerator hardware. [[2026_Fang_YAVIN]] is a *defensive*, architectural contribution: it extends a TEE beyond the processor into a dedicated processing-in-memory (PIM) region, treating the memory bus itself — the channel between processor and PIM — as untrusted. Its overhead is measured specifically on quantized edge-class LLM execution (34% for 8-bit integer precision, 9.3% for 32-bit, relative to unencrypted execution), directly connecting the security architecture to on-device LLM deployment costs. [[2026_Mehta_LLMscope]] is an *offensive* contribution demonstrating the opposite direction: using laser voltage imaging, it physically extracts LLM weights, activations, and other inference state from an FPGA-based edge LLM accelerator, exploiting the fact that such accelerators reuse the same buffers and compute subcircuits across addresses, tiles, modules, and layers — a design choice typically made for area/power efficiency, not anticipating this as an attack surface. The attack achieves full recovery of targeted values, and its cost scales only linearly with asset size.

These two papers are grouped under one concept, with named variants below, rather than split into separate concepts, because the underlying concern is the same — confidentiality of model state on edge accelerator hardware — and because the natural next research question directly connects them (see Open problems). This is worth revisiting if either direction grows enough in the literature that the two variants stop informing each other directly.

## Evolution of the concept

Dubey et al.'s 2022 survey of physical (power/electromagnetic) side-channel attacks and countermeasures for ML hardware is a genuinely distinct, longer-established threat model — not bus-level eavesdropping like YAVIN, and not optical/laser probing like LLMscope — and its existence underscores that this concept's other two anchors are instances of a broader physical-security problem for ML accelerators that research has been tracking since at least the early 2020s.

Batina, Bhasin, Jap, and Picek's "CSI NN" (2019) is the original demonstration that a neural network's full architecture can be reverse-engineered purely from electromagnetic side-channel measurements during inference — the direct methodological ancestor of LLMscope's weight/activation extraction. Kurian, Dubey, Yaman, and Aysu's TPUXtract (2025) is the first successful model-extraction attack on a real, commercially deployed accelerator — the Google Edge TPU — using an online template-building electromagnetic-extraction methodology to reach 99.91% accuracy, including on previously unseen architectures, closing the gap between CSI NN's foundational threat model and its applicability to real, deployed edge accelerator silicon.

## Variants

**Architectural trust-boundary extension (trusted execution / confidential computing).** Extends a TEE's cryptographic trust boundary to cover previously untrusted components (for example PIM-capable memory) so that computation can happen on encrypted-then-decrypted data without ever leaving the trust boundary. Anchor: [[2026_Fang_YAVIN]].

**Physical / side-channel extraction.** Exploits physical properties of accelerator silicon (for example buffer and subcircuit reuse across logical addresses) to read out model assets directly from the physical substrate during execution, bypassing any purely logical/cryptographic trust boundary. Anchor: [[2026_Mehta_LLMscope]].

**Power/electromagnetic side-channel leakage.** Exploits power consumption or electromagnetic emissions during computation to infer model weights, activations, or inference state, a longer-established threat model distinct from both bus-eavesdropping and optical/laser probing — addressed via masking-style countermeasures rather than trust-boundary extension or physical shielding alone. Anchor: [[2022_Dubey_GuardingMLHardwareSideChannel]].

**Architecture / hyperparameter extraction via electromagnetic side channel.** Reconstructs a model's architecture (layer types, counts, sizes, activation functions) — not its weights or activations — purely from electromagnetic emanations during inference, without any logical access to the device. The founding paradigm behind the physical-extraction variant above; extended to a real commercial edge accelerator (Google Edge TPU) by TPUXtract. Anchors: [[2019_Batina_CSINN]] (founding paper), [[2025_Kurian_TPUXtract]] (real-hardware, unseen-architecture generalization).

## Key papers

[[2026_Fang_YAVIN]] — unified trusted computing base extending TEE trust into processing-in-memory; first PIM implementations of LightSaber KEM (post-quantum) and ASCON-128; overhead measured on quantized edge-class LLM execution.

[[2026_Mehta_LLMscope]] — laser voltage imaging attack recovering LLM weights, activations, and inference state from an FPGA-based edge accelerator by exploiting buffer/subcircuit reuse; full recovery demonstrated; recovery cost scales linearly with asset size.

[[2022_Dubey_GuardingMLHardwareSideChannel]] — survey of physical (power/electromagnetic) side-channel attacks and countermeasures for ML hardware, a third, earlier-established threat model distinct from bus-eavesdropping and optical probing.

[[2019_Batina_CSINN]] — the founding electromagnetic-side-channel architecture-reverse-engineering paper, the direct methodological ancestor of this concept's physical-extraction variant.

[[2025_Kurian_TPUXtract]] — first successful model-extraction attack on the real, commercial Google Edge TPU, 99.91% accuracy including on previously unseen architectures.

## Open problems

Does an architectural trust-boundary defense such as YAVIN's provide any protection against a physical probing attack such as LLMscope's? YAVIN treats the memory bus as the untrusted channel and encrypts data crossing it; LLMscope reads state directly off the physical substrate (via laser voltage imaging) rather than off the bus, which suggests the two threat models may be largely orthogonal — a TEE/PIM architecture could be cryptographically sound against bus-level eavesdropping while remaining fully exposed to physical probing of the memory or compute subcircuits themselves. This has not been tested by either paper and is, at present, the single most important open question tying this concept's two variants together.

What do effective countermeasures against physical probing (address randomization, buffer partitioning, physical shielding) cost in area and power — and are they compatible with the buffer/subcircuit reuse that LLMscope exploits, given that reuse is itself usually a deliberate area/power optimization? This creates a potential tension between the efficiency goals that dominate the rest of this taxonomy and physical security.

Does either threat model's severity vary systematically across accelerator classes (FPGA, custom ASIC, NPU, systolic array, in-memory-computing designs)? LLMscope's validation is FPGA-specific; whether custom-ASIC or NPU designs reuse buffers/subcircuits in comparable ways — and are therefore comparably vulnerable — is untested.

## Research ideas

A systematic comparative study of which edge accelerator architectures (NPU designs, systolic arrays, in-memory-computing designs) are structurally more or less vulnerable to physical/side-channel extraction, and what countermeasures cost in area/energy. An evaluation of whether a YAVIN-style architectural trust boundary offers any defense-in-depth against LLMscope-style physical probing, or whether the two threat models require entirely independent countermeasure strategies. Measuring YAVIN's security overhead across the fuller quantization spectrum this Observatory already tracks (4-bit, mixed-precision), not just the 8-bit/32-bit points reported so far.

## Possible thesis topics

Threat-modeling edge AI accelerators beyond optical probing: a systematic comparative study of structural vulnerability to physical/side-channel extraction across accelerator architectures, with a countermeasure area/energy cost analysis (PhD-scale; bridges hardware architecture and security).

A second data point for trusted PIM: measure YAVIN's TEE-into-PIM overhead across the full 8-bit/4-bit/mixed-precision quantization spectrum, and determine whether trusted PIM changes the accuracy/latency/security balance for on-device LLM inference (Master's/PhD; bridges [[Quantization]] and this concept).

## Links

[[Quantization]] (YAVIN's overhead is measured specifically on quantized edge-class LLM execution), [[FPGA]] (LLMscope's validated attack platform), [[NPU]], [[MoE_Edge_LLM_Serving]] (YAVIN evaluates on the same quantized edge-LLM execution regime that concept's serving systems target)
