# YAVIN: A Unified Architecture for Secure Edge Processing in Memory

**Full citation:** Fang, S., Tegge, W. C., Faruque, M. O., Zhou, P., Hoque, E., Jones, A. K. (2026). YAVIN: A Unified Architecture for Secure Edge Processing in Memory. arXiv:2608.13496 [cs.AR]. Submitted 13 Aug 2026. License CC BY 4.0. DOI: 10.48550/arXiv.2608.13496.

**Linked concepts:** [[Hardware Security of Edge AI Accelerators]] — anchor paper (architectural trust-boundary-extension variant), created 2026-09-02 by the Knowledge Base Consolidation cycle, resolving what was previously the "Edge AI Security / Trusted Execution" taxonomy gap flagged in the 2026-08-20 weekly digest (distinct from the "Mixture-of-Experts (MoE) & Edge LLM Serving" node; YAVIN evaluates on quantized edge LLMs but its contribution is security architecture, not serving/scheduling). Loosely touches [[Quantization]] via its evaluation on INT8/INT32 quantized edge-class LLMs.

## Abstract summary

Secure, private multi-tenant execution spanning processors, memory, and accelerators is a major challenge in edge computing; processing-in-memory (PIM) reduces the Von Neumann bottleneck but existing trusted execution environments (TEEs) only protect the processor, leaving the memory bus untrusted — so trusted computation cannot be performed directly within memory. YAVIN is a unified trusted computing base extending the TEE beyond the processor to a dedicated memory region supporting trusted PIM execution, treating the memory bus itself as untrusted. It presents the first PIM implementations of the LightSaber KEM post-quantum cryptosystem and ASCON-128 authenticated encryption, co-designed for efficient DRAM execution, plus a cryptography-PIM co-design for tensor workloads with bit-sliced ordering limiting temporary plaintext exposure. Versus the latest PIM AES implementation, YAVIN achieves over 20× speedup while incurring only 34% and 9.3% overhead executing INT8 and INT32 quantized edge-class LLMs, respectively, relative to plaintext execution.

## Research problem

Processing-in-memory (PIM) moves computation closer to data to reduce the Von Neumann bottleneck, which matters for edge inference where memory bandwidth is often the binding constraint. But conventional trusted execution environments (TEEs) only establish trust within the processor — the memory bus and any PIM computation sit entirely outside that trust boundary, meaning data must be decrypted before it reaches memory-side compute, defeating the purpose of a TEE for any workload that wants to use PIM. There was, per the paper's framing, no existing way to do trusted computation directly within memory.

## Key idea

Extend the TEE's trust boundary beyond the processor into a dedicated, PIM-capable memory region, while explicitly treating the memory bus itself as untrusted (rather than assuming it can be trusted just because it's inside the same package). Data can then be decrypted, processed, and re-encrypted by either processor or PIM execution while never leaving the TEE's trust boundary. Realizing this requires PIM-native implementations of the cryptographic primitives themselves — the paper builds the first PIM implementations of a post-quantum KEM (LightSaber) and an authenticated encryption scheme (ASCON-128), co-designed for efficient DRAM execution rather than ported from a CPU-oriented implementation.

## Technical contribution

A unified trusted computing base spanning processor and a dedicated PIM-capable memory region, with the memory bus treated as untrusted; the first PIM implementations of LightSaber KEM (post-quantum) and ASCON-128 authenticated encryption, co-designed for DRAM execution; a cryptography-PIM co-design for tensor-based workloads that reorganizes computation to satisfy authenticated encryption's ordering constraints with minimal overhead; a bit-sliced ordering scheme limiting temporary plaintext exposure during tensor workload execution — a concrete security property (not just a performance number).

## Experimental methodology

Compared against the latest PIM AES implementation on speedup. Overhead specifically measured for INT8 and INT32 quantized edge-class LLM execution, relative to unencrypted plaintext execution of the same workloads — grounding the security overhead in a concrete, practically relevant workload class rather than only synthetic cryptographic benchmarks.

## Results

Over 20× speedup versus the latest PIM AES implementation. Only 34% overhead for INT8 quantized edge-class LLM execution and 9.3% overhead for INT32 quantized edge-class LLM execution, both relative to unencrypted plaintext execution — notably, the *lower*-precision (INT8) format incurs *higher* relative overhead than the higher-precision (INT32) format, an inversion worth understanding (plausibly because INT8's smaller payload makes the fixed cryptographic/bit-slicing overhead a larger fraction of total work).

## Comparison with the state of the art

Directly benchmarked against the latest PIM AES implementation for raw cryptographic speedup, and self-benchmarked (encrypted vs. plaintext execution) for the LLM-specific overhead figures. Extending TEE trust into PIM, rather than treating PIM as inherently untrusted or out of scope, is presented as YAVIN's central architectural departure from prior TEE designs, per the 2026-08-20 digest.

## Strengths

A genuine architectural contribution (extending trust into PIM) rather than an incremental cryptographic optimization; grounding overhead numbers specifically in quantized edge-LLM execution connects the security contribution directly to a practical, currently-relevant deployment concern (prompt/weight privacy during PIM-accelerated on-device LLM inference) rather than only abstract cryptographic benchmarks; includes post-quantum cryptography (LightSaber KEM) rather than only classical schemes, which is forward-looking given the broader push toward post-quantum readiness; the bit-sliced ordering scheme is a specific, checkable security property (limiting temporary plaintext exposure), not just a performance claim.

## Weaknesses

The INT8-overhead-higher-than-INT32-overhead inversion is not explained at the abstract level and deserves scrutiny — if it reflects a real fixed-cost-dominates-at-low-precision effect, it has direct implications for how well YAVIN scales to even lower precision (INT4) formats increasingly common in edge LLM deployment; the paper does not specify what edge-class LLM(s) or task(s) were used for the overhead measurement, making it hard to assess how representative the 34%/9.3% figures are.

## Limitations

As with quantized-LLM security work generally, the overhead figures are specific to the precision formats tested (INT8, INT32) — the increasingly common INT4/mixed-precision formats this Observatory's [[Quantization]] work tracks are not evaluated, and given the apparent inverse relationship between precision and overhead, INT4 overhead could plausibly be higher still, though this is speculative without further data.

## Open questions

What does the overhead curve look like across the full quantization spectrum (INT8/INT4/mixed-precision) this Observatory already tracks, rather than just the two points (INT8, INT32) tested — does trusted PIM change the accuracy/latency/security Pareto front for on-device LLM inference specifically? Does the TEE-into-PIM architecture extend to MCU/NPU-class (not just DRAM-PIM) targets, or is it fundamentally tied to DRAM-based PIM implementations?

## Possible extensions

Measure the overhead curve across the full quantization spectrum (INT8/INT4/mixed-precision) this Observatory already tracks in its [[Quantization]] work, and determine whether trusted PIM changes the accuracy/latency/security Pareto front specifically on MCU/NPU-class (not just DRAM-PIM) targets — the explicit 2026-08-20 digest hook; investigate the cause of the INT8-higher-overhead-than-INT32 inversion.

## Relevance to our research

One of the two founding anchors (with [[2026_Mehta_LLMscope]]) of the [[Hardware Security of Edge AI Accelerators]] concept, created 2026-09-02 — secure/private on-device execution doesn't map onto any existing Algorithms/Frameworks/Hardware/Applications branch, which is why it now has its own Security branch. Distinct from, but occasionally confused with, the "Mixture-of-Experts (MoE) & Edge LLM Serving" node (YAVIN evaluates on quantized edge LLMs but its contribution is security, not serving).

## Possible thesis topics

Trusted PIM as a prerequisite for on-device LLM privacy: measure the overhead curve across the full quantization spectrum (INT8/INT4/mixed-precision) and determine whether trusted PIM changes the accuracy/latency/security Pareto front on MCU/NPU-class targets specifically (PhD-scale, per the 2026-08-20 digest's explicit hook; bridges [[Quantization]] and the still-open Edge AI Security taxonomy gap).

## Possible collaborations

Alex K. Jones's group, given YAVIN's architectural security contribution — a natural fit if the lab develops interest in trusted/confidential edge inference as a research direction, distinct from the lab's current core efficiency focus.

## Links to related papers

The Observatory's first `02_Papers/` record on trusted execution / confidential computing for edge AI. Paired with [[2026_Mehta_LLMscope]] (physical/optical extraction attack, recorded 2026-09-02) as the two founding anchors of the [[Hardware Security of Edge AI Accelerators]] concept — YAVIN is the defensive/architectural variant, LLMscope the offensive/physical variant.
