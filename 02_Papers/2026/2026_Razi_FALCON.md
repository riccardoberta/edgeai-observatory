# FALCON: Fault-Tolerant Magnetic Tunnel Junction-Based In-Memory Stochastic Architecture for Reliability-Critical Edge AI Applications

**Full citation:** Razi, F., Moghadam, M., Aygun, S., Najafi, M.H., Riedel, M. (2026). FALCON: Fault-Tolerant Magnetic Tunnel Junction-Based In-Memory Stochastic Architecture for Reliability-Critical Edge AI Applications. arXiv:2609.00701 [cs.AR]. University of Louisiana at Lafayette; University of Minnesota. Submitted 1 Sep 2026. DOI: 10.48550/arXiv.2609.00701.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2609.00701)

**Linked concepts:** [[NPU]], [[Quantization]] — no clean match in the Hardware branch (Cortex-M/A, RISC-V, DSP, FPGA, NPU); this is an in-memory-computing/emerging-NVM architecture, flagged as a taxonomy gap (see taxonomy Evolution notes).

## Abstract summary

Data movement between memory and compute is a dominant latency and energy cost in data-centric edge AI workloads (the "memory wall"). In-memory computing (IMC) using emerging non-volatile memory — here, Magnetic Tunnel Junctions (MTJs) — addresses this by computing inside the memory array itself, but conventional binary radix-based IMC designs are highly vulnerable to process-induced variation and thermal noise. FALCON combines MTJ-based in-memory arithmetic with stochastic computing (SC), encoding values as uniform bit-streams that are inherently tolerant of localized soft errors, and implements a suite of arithmetic operations using compact logic primitives directly within the memory array.

## Research problem

Reliability-critical edge AI applications need both energy-efficient in-memory computation and robustness to the process variation, thermal noise, and fault rates inherent to emerging non-volatile memory technologies at edge-relevant process nodes. Conventional binary radix-based in-memory computing designs are precise but fragile: a single bit-flip can corrupt an entire binary-encoded value, and MTJ devices are especially prone to such stochastic switching errors. This creates a tension between the efficiency benefits of in-memory computing and the reliability edge AI applications (particularly safety- or reliability-critical ones) require.

## Key idea

Encode numerical values as stochastic bit-streams (each bit independently representing a probability rather than a fixed positional weight) rather than binary radix, so that isolated bit errors perturb the represented value only slightly rather than catastrophically — a property inherent to stochastic computing that becomes especially valuable when the underlying memory technology (MTJ) is itself failure-prone. Implement the stochastic arithmetic primitives directly within the MTJ memory array using compact in-memory logic, rather than in separate compute logic, to retain the data-movement savings that motivate in-memory computing in the first place.

## Technical contribution

A fault-tolerant, MTJ-based in-memory arithmetic architecture integrating stochastic computing directly into the memory array; a suite of arithmetic operations (the specific set not confirmed at abstract level — verify from full PDF) implemented via compact logic primitives executable in-memory; an explicit reliability analysis connecting stochastic encoding's inherent error tolerance to MTJ's process-variation and thermal-noise failure modes, rather than treating reliability and efficiency as separate design axes.

## Experimental methodology

Not confirmed at abstract level (device-level simulation vs. fabricated silicon, specific benchmarks, and comparison baselines all require full-PDF verification). This record is built from the abstract and secondary summaries; flagged for a full-PDF verification pass before citing quantitative results in a survey.

## Results

Not confirmed at abstract level — quantitative reliability, area, latency, or energy results require full-PDF verification.

## Comparison with the state of the art

Builds directly on the same author group's own closely related prior work: "Maximizing Memory-Level Parallelism via Integrated Stochastic Logic-in-Memory Architectures" (Razi, Moghadam, Aygun, Najafi, Riedel; arXiv:2604.23146, Apr 2026), which addresses the bit-serial throughput bottleneck of conventional stochastic computing via a parallel "bit-bundle" MTJ logic-in-memory design, and "All-in-Memory Stochastic Computing using ReRAM" (de Lima, Moghadam, Aygun, Castrillon, Najafi, Khan; DAC 2025), which applies a related stochastic-computing-in-memory approach to a different emerging-memory substrate (ReRAM instead of MTJ) with a partially overlapping author subset. FALCON's distinguishing contribution within this lineage is explicitly targeting fault tolerance for reliability-critical applications, rather than throughput (the April 2026 paper) or random-number-generation cost (the DAC 2025 paper).

## Strengths

Addresses a genuine, underexplored tension (efficiency vs. reliability) in in-memory computing rather than only optimizing for throughput or energy; stochastic computing's inherent fault tolerance is a well-motivated match for MTJ's known failure modes, rather than an arbitrary pairing; part of a sustained, multi-paper research program (three related papers from overlapping authors across 18 months: DAC 2025 ReRAM paper, April 2026 MTJ-parallelism paper, this September 2026 fault-tolerance paper) indicating a maturing, active research direction rather than a one-off result.

## Weaknesses

This record is built from abstract-level material only — the paper's own quantitative claims (fault-tolerance improvement, area/energy overhead of the SC encoding versus binary radix, comparison against non-fault-tolerant IMC baselines) are not yet verified from the full text; needs a follow-up full-PDF pass before citing specific numbers.

## Limitations

As with the group's related papers, the approach is validated on MTJ-specific device characteristics; transferability to other emerging non-volatile memory technologies (ReRAM, PCM) is not established by this paper alone (though the group's own DAC 2025 ReRAM paper suggests the general stochastic-computing-in-memory approach does transfer across substrates). Not yet independently corroborated by a fully separate research group — see the Observatory taxonomy's note on this gap's current single-research-program provenance.

## Open questions

What is FALCON's concrete area, latency, and energy overhead relative to a non-fault-tolerant binary-radix MTJ in-memory baseline, at matched reliability targets? Does the fault-tolerance benefit transfer to the group's own ReRAM-based stochastic-in-memory design, unifying the substrate-specific and reliability-specific strands of this research line? Has any research group outside this author cluster (Louisiana at Lafayette / Minnesota / Dresden) begun independent work on stochastic-computing-based in-memory fault tolerance for edge AI?

## Possible extensions

Applying FALCON's fault-tolerant stochastic-encoding approach to the group's own parallel "bit-bundle" throughput optimization (arXiv:2604.23146), potentially unifying reliability and throughput gains in one MTJ in-memory design; porting the fault-tolerance approach to the ReRAM substrate used in the group's DAC 2025 paper to test cross-technology generality.

## Relevance to our research

The Observatory's first recorded paper in in-memory computing with emerging non-volatile memory — a Hardware taxonomy gap flagged since the 2026-09-02 weekly digest. Currently the strongest single anchor for this direction, but (per the taxonomy's own two-independent-anchor convention applied to other Hardware gaps, e.g. [[Event-Driven_Neuromorphic_Accelerators]] and the Security branch) not yet corroborated by a fully independent research group — the closest related papers found in this pass share authors with FALCON. Kept as a recorded, real paper and a "watching" taxonomy candidate rather than a formalized node until independent corroboration appears.

## Possible thesis topics

A comparative benchmark of MTJ-based versus ReRAM-based stochastic-computing-in-memory designs (bridging FALCON and the group's own DAC 2025 ReRAM paper) for edge AI reliability (Master's/PhD). A literature-monitoring project specifically tracking whether independent research groups begin publishing in stochastic-computing-based in-memory fault tolerance, to formally resolve this Observatory's open taxonomy question.

## Possible collaborations

The Razi/Moghadam/Aygun/Najafi (University of Louisiana at Lafayette) and Riedel (University of Minnesota) group directly — currently the most active research program in this space that the Observatory has identified.

## Links to related papers

None yet in `02_Papers/` on in-memory computing or emerging non-volatile memory — this is the Observatory's first deep-analysis record in this direction. The same author group's related papers (arXiv:2604.23146, MTJ logic-in-memory parallelism; DAC 2025, ReRAM stochastic computing) are discussed above but not yet independently recorded.
