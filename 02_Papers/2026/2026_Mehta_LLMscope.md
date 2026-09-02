# LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing

**Full citation:** Mehta, D., Dukette, L., Folan, W., Kochol, O., Solomon, N., Tajik, S., Ganji, F. (2026). LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing. arXiv:2608.25321 [cs.CR, cs.AI]. Submitted 26 Aug 2026. License CC BY-NC-ND 4.0. DOI: 10.48550/arXiv.2608.25321.

**Linked concepts:** anchor paper (alongside [[2026_Fang_YAVIN]]) for the new [[Hardware Security of Edge AI Accelerators]] concept, created in the 2026-09-02 Knowledge Base Consolidation cycle. Touches [[FPGA]] as the accelerator class attacked in the validation experiment.

## Abstract summary

The move of LLM inference to edge AI accelerators introduces new physical vulnerabilities: during execution, model parameters and intermediate inference states are repeatedly loaded into and processed on the chip, making them susceptible to physical side-channel attacks. Using laser voltage imaging, the authors show that LLM assets — embeddings, attention, quantized MLP weights, activations, and other inference states — can be extracted from localized memories and compute subcircuits. They validate the attack on an FPGA-based LLM accelerator: because such accelerators reuse the same buffers and compute subcircuits across addresses, tiles, modules, and layers, reading asset values reduces to probing a limited set of physical memory locations during inference. The paper demonstrates full recovery of targeted values, establishes a methodology to recover asset values even when some weights or bits are not directly probed, and derives lower bounds relating imaging effort to asset dimensions, showing that even direct recovery scales linearly with the size of the targeted asset.

## Research problem

As LLM inference moves from datacenter GPUs onto edge AI accelerators, the physical chip itself becomes part of the attack surface in a way that model-level security research (e.g., API-based model-stealing, adversarial examples) does not address. Model parameters and intermediate activations are physically present — loaded into on-chip memories and processed by on-chip subcircuits — during every inference pass, which raises the question of whether an attacker with physical access to the chip can extract proprietary or licensed model assets without ever compromising the software/cryptographic stack.

## Key idea

Exploit a structural property common to edge AI accelerator design for area/power efficiency: buffers and compute subcircuits are reused across memory addresses, tiles, modules, and layers, rather than each logical location having dedicated physical hardware. This means an attacker does not need to image the entire chip surface exhaustively — probing a comparatively small number of physical locations during inference, using laser voltage imaging, is enough to recover asset values (weights, activations, embeddings, attention states) across the whole model, because the same physical circuits process many different logical values over the course of execution.

## Technical contribution

Demonstration that laser voltage imaging — an established physical side-channel technique — can extract LLM-specific assets (embeddings, attention, quantized MLP weights and activations, other inference states) from an edge AI accelerator; identification and exploitation of buffer/subcircuit reuse across addresses, tiles, modules, and layers as the structural property that makes this tractable; a reconstruction methodology that recovers asset values even when some individual weights or bits cannot be directly probed; a derived lower bound relating imaging effort to asset dimensions, showing recovery cost scales linearly with the size of the targeted asset rather than combinatorially.

## Experimental methodology

Attack validated on an FPGA-based LLM accelerator using laser voltage imaging. The authors probe physical memory locations during live inference execution and demonstrate recovery of targeted asset values (weights, activations, and other inference states), then generalize the methodology to partial-probing scenarios (recovering values even when some weights/bits are not directly read) and derive scaling lower bounds analytically.

## Results

Full recovery of targeted asset values on the FPGA-based LLM accelerator test platform. A reconstruction methodology that tolerates incomplete direct probing. Imaging effort for direct recovery shown to scale linearly with the size of the targeted asset — meaning the attack does not become disproportionately harder as models grow, which is a materially worse scaling property (for defenders) than a combinatorial or exponential cost would be.

## Comparison with the state of the art

Positioned as a new threat model rather than an incremental improvement on prior physical-extraction work: prior side-channel and physical-extraction literature has largely targeted cryptographic keys or smaller ML models rather than LLM-specific assets (embeddings, attention states, quantized MLP weights) on accelerators built for LLM inference specifically. The paper's contribution is showing this class of attack transfers to the LLM-on-edge-accelerator setting and characterizing its cost scaling.

## Strengths

A genuinely new attack surface for this Observatory's tracked literature — the first physical/hardware-level extraction attack recorded here, as opposed to purely algorithmic or cloud-API-based model-stealing concerns; validated on real hardware (an FPGA-based accelerator), not simulated; the "reuse of buffers/subcircuits across tiles" observation is a specific, falsifiable structural claim about accelerator design, not a generic side-channel assertion; the linear-scaling lower bound gives a concrete, quantitative handle on attack cost that a defender can reason about.

## Weaknesses

Validated on a single FPGA-based accelerator platform; the abstract does not establish how the attack's cost or the exploited buffer-reuse structure transfers to custom ASIC or NPU designs, which may reuse buffers differently (or less) than the FPGA prototype tested. Laser voltage imaging requires specialized equipment and, typically, decapsulation or physical access to the die — the practical threat model (who has this capability, and under what deployment scenario) is not detailed at the abstract level.

## Limitations

As with any physical/hardware-level attack, real-world applicability depends on an adversary having sustained physical access to the target chip during inference — a materially different (and for many deployment scenarios, more restrictive) threat model than remote/API-based attacks. The paper does not report on countermeasures (e.g., address randomization, buffer partitioning, physical shielding) or their cost, leaving the defensive side of this threat model open.

## Open questions

Does a cryptographic trust-boundary defense such as [[2026_Fang_YAVIN]]'s TEE-into-PIM architecture provide any protection against this class of physical probing attack, given that laser voltage imaging reads state directly off the physical substrate rather than off the memory bus YAVIN treats as the untrusted channel? How does the attack's cost and the underlying buffer-reuse structure vary across accelerator classes (FPGA, custom ASIC, NPU, systolic array)? What countermeasures (address randomization, buffer partitioning, shielding) are effective, and at what area/power cost — particularly given that buffer/subcircuit reuse is itself usually a deliberate area/power optimization, creating a potential tension between efficiency and physical security.

## Possible extensions

A systematic comparative study of which edge accelerator architectures are more or less structurally vulnerable to this class of attack, and what countermeasures cost in area/energy (the explicit 2026-09-02 digest hook); an evaluation of whether YAVIN-style trust-boundary architectures offer any defense-in-depth against physical probing, or whether the two threat models require entirely independent countermeasures.

## Relevance to our research

The second independent anchor (after [[2026_Fang_YAVIN]]) for what is now the [[Hardware Security of Edge AI Accelerators]] concept, created in this cycle. Establishes that edge AI accelerator hardware security spans at least two distinct threat models — architectural trust-boundary gaps (YAVIN) and physical/side-channel extraction (LLMscope) — that the Observatory should track as a single emerging concern with two variants rather than two unrelated one-off results.

## Possible thesis topics

Threat-modeling edge AI accelerators beyond optical probing: a systematic comparative study of which accelerator architectures (NPU designs, systolic arrays, in-memory-computing designs) are more or less structurally vulnerable to physical/side-channel extraction, and what countermeasures cost in area/energy (PhD-scale, bridging hardware architecture and security; the explicit 2026-09-02 digest hook).

## Possible collaborations

Shahin Tajik's and Fatemeh Ganji's groups (WPI), given their established physical/hardware-security track record evident in this paper's methodology — a natural fit if the lab develops interest in physical security of edge accelerators as a research direction.

## Links to related papers

The second data point (after [[2026_Fang_YAVIN]]) in the Observatory's emerging hardware-security thread; together they ground the new [[Hardware Security of Edge AI Accelerators]] concept. No other `02_Papers/` records address physical/side-channel attacks on edge AI accelerator hardware to date.
