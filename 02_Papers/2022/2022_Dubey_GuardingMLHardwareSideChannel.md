# Guarding Machine Learning Hardware Against Physical Side-channel Attacks

**Full citation:** Dubey, A., Cammarota, R., Suresh, V., Aysu, A. (2022). Guarding Machine Learning Hardware Against Physical Side-channel Attacks. ACM Journal on Emerging Technologies in Computing Systems (JETC), 18(3), Article 56. DOI: 10.1145/3465377

**PDF:** [ACM Digital Library](https://dl.acm.org/doi/10.1145/3465377) · [arXiv preprint](https://arxiv.org/abs/2109.00187)

**Verification note:** ACM-published journal article; bibliographic details confirmed via WebSearch cross-referencing dblp-style listings and the ACM DL record.

**Linked concepts:** [[Hardware_Security_of_Edge_AI_Accelerators]], [[NPU]]

## Abstract summary

A survey and analysis of countermeasures for protecting machine learning hardware against physical (power/EM) side-channel attacks, which can leak model weights, activations, and other sensitive inference state by observing physical signals during computation — the same class of confidentiality concern this Observatory's Security branch tracks, though addressed here via power/EM side channels rather than the laser-voltage-imaging or PIM-trust-boundary approaches of its two existing anchor papers.

## Research problem

Machine learning accelerators, including those deployed at the edge, are physically accessible to an adversary in many real deployment scenarios, and their power consumption and electromagnetic emissions during computation can leak model parameters and other confidential inference state through physical side channels, independent of any purely logical or cryptographic security measures.

## Key idea

Systematically catalog and analyze the physical side-channel attack surface of ML hardware (power and EM channels specifically) and the countermeasure design space available to guard against them, providing a structured reference for the trade-offs between physical security and area/power/performance cost.

## Technical contribution

A structured survey and analysis of physical side-channel attacks and countermeasures specifically for ML hardware, covering the attack surface (power/EM side channels leaking weights, activations, inference state) and the countermeasure landscape (masking and related techniques), framed for the ML-accelerator context rather than general cryptographic hardware.

## Experimental methodology

Literature survey and analysis of physical side-channel attack and countermeasure techniques as applied to machine learning hardware (not a single novel empirical attack or defense); synthesizes prior side-channel security research and evaluates its applicability to ML-specific accelerator designs.

## Results

Provides a structured mapping of the physical-side-channel threat landscape for ML hardware and the available countermeasure design space, serving as a reference point for area/power/performance costs of physical-security hardening in ML accelerator design.

## Comparison with the state of the art

Complements this Observatory's two existing Hardware_Security_of_Edge_AI_Accelerators anchors — [[2026_Fang_YAVIN]] (an architectural TEE/PIM trust-boundary defense against bus-level eavesdropping) and [[2026_Mehta_LLMscope]] (a specific laser-voltage-imaging physical extraction attack) — with a broader survey of the power/EM side-channel attack surface and countermeasure landscape, a third and distinct physical-security threat model (power/EM side channels rather than bus eavesdropping or optical probing) for the same underlying concern: confidentiality of model state on edge accelerator hardware.

## Strengths

Peer-reviewed, ACM-published survey giving structured coverage of a threat model (power/EM side channels) not covered by this Observatory's two existing Security-branch anchor papers; directly extends the concept's own stated interest in "which edge accelerator architectures are structurally more or less vulnerable" and "what countermeasures cost in area/energy."

## Weaknesses

As a survey rather than a novel empirical attack/defense demonstration, it does not itself provide new quantitative results on a specific edge accelerator; predates the 2026 YAVIN/LLMscope anchor papers, so it does not address the confidential-computing/PIM or optical-probing threat models those introduce.

## Limitations

Focused specifically on power/EM side channels; does not cover the bus-eavesdropping threat model YAVIN defends against or the optical/laser-based physical extraction LLMscope demonstrates, so this Observatory's Security-branch open question about whether these threat models are "orthogonal" still requires bridging work this paper alone does not provide.

## Open questions

Does a YAVIN-style architectural trust-boundary defense (bus encryption) offer any protection against power/EM side-channel leakage, or are these two threat models (bus eavesdropping vs. power/EM side channels) as orthogonal to each other as this Observatory's Security concept already suspects bus-eavesdropping and optical-probing to be? Do the masking countermeasures this survey catalogs remain effective, and at what area/power cost, on modern quantized edge-class LLM accelerators — the specific regime YAVIN's overhead is measured against?

## Possible extensions

Extending this Observatory's Hardware_Security_of_Edge_AI_Accelerators concept's existing "variants" structure (architectural trust-boundary extension vs. physical/optical extraction) with a third variant — power/EM side-channel attacks and masking countermeasures — using this paper as its anchor, and testing whether any of the three threat models compose or interact.

## Relevance to our research

Fills a genuine gap in this Observatory's [[Hardware_Security_of_Edge_AI_Accelerators]] concept: its two existing anchors cover bus-eavesdropping defense (YAVIN) and optical physical extraction (LLMscope), but not the longer-established power/EM side-channel attack literature this survey catalogs — directly relevant to the concept's own open question about which accelerator architectures are structurally vulnerable to which physical attack classes.

## Possible thesis topics

A systematic evaluation of whether power/EM side-channel countermeasures (as cataloged in this survey) provide any incidental protection against the optical/laser-based extraction technique demonstrated by [[2026_Mehta_LLMscope]], or whether the two threat models require entirely independent countermeasure investment (PhD-scale; directly extends this Observatory's existing Hardware_Security open problem).

## Possible collaborations

Hardware security research groups working on side-channel analysis and countermeasures for ML accelerators (NC State University and Intel-affiliated authors, per the paper's institutional affiliations).

## Links to related papers

[[2026_Fang_YAVIN]], [[2026_Mehta_LLMscope]]
