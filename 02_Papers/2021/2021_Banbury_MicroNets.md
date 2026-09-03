# MicroNets: Neural Network Architectures for Deploying TinyML Applications on Commodity Microcontrollers

**Full citation:** Banbury, C., Zhou, C., Fedorov, I., Matas Navarro, R., Thakker, U., Gope, D., Janapa Reddi, V., Mattina, M., Whatmough, P. (2021). MicroNets: Neural Network Architectures for Deploying TinyML Applications on Commodity Microcontrollers. Proceedings of Machine Learning and Systems (MLSys 2021), 3.

**PDF:** [MLSys Proceedings](https://proceedings.mlsys.org/paper_files/paper/2021/file/c4d41d9619462c534b7b61d1f772385e-Paper.pdf)

**Linked concepts:** [[microTVM_TVM]]

## Abstract summary

Uses differentiable neural architecture search (DNAS) to discover CNN architectures (MicroNets) that satisfy MCU SRAM, Flash, and latency constraints directly during search, then deploys them via MicroTVM's automatic low-level code generation for commodity microcontrollers.

## Research problem

Deep neural network inference demands compute and memory budgets far beyond typical MCU resources; manually designing architectures that fit tight SRAM/Flash/latency envelopes is slow and does not scale across hardware targets.

## Key idea

Incorporate MCU resource constraints (SRAM, Flash, latency) directly into a differentiable neural architecture search objective, so the search itself only proposes deployable architectures, rather than searching for accuracy first and checking deployability afterward.

## Technical contribution

The MicroNets architecture family plus a DNAS methodology that jointly optimizes for accuracy and MCU deployability constraints; deployment validated end-to-end via MicroTVM's automatic code generation.

## Experimental methodology

DNAS search under SRAM/Flash/latency constraints on standard TinyML benchmark tasks (including the visual wake words and keyword spotting tasks later standardized in MLPerf Tiny/TinyMLPerf), deployed via MicroTVM and evaluated on commodity microcontrollers.

## Results

MicroNets architectures meet tight MCU resource constraints while achieving competitive accuracy, demonstrating that constraint-aware NAS can outperform manually-designed or post-hoc-compressed architectures for this regime; very widely cited (500+).

## Comparison with the state of the art

Bridges this Observatory's [[NAS]] concept (hardware-aware NAS) with this concept's microTVM deployment pipeline, demonstrating MicroTVM's automatic code generation as a practical deployment path for NAS-discovered architectures rather than requiring hand-tuned kernels per architecture.

## Strengths

Extremely widely cited; demonstrates a full search-to-deployment pipeline rather than architecture search alone; directly informed the TinyML benchmark task selection later standardized in MLPerf Tiny.

## Weaknesses

DNAS search cost itself not deeply characterized relative to simpler NAS methods; CNN-only architecture family, predating transformer-based TinyML architectures.

## Limitations

Search-time compute cost for DNAS not the focus of the paper's own evaluation; single hardware target class (commodity Cortex-M MCUs).

## Open questions

How would MicroNets' constraint-aware DNAS methodology extend to incorporate energy (not just SRAM/Flash/latency) directly in the search objective, and how would it interact with microTVM's newer UMA-based accelerator-offloading pipeline?

## Possible extensions

Re-running MicroNets-style constrained DNAS with an energy term added to the objective, and deploying the result via microTVM's UMA accelerator interface rather than pure software kernels.

## Relevance to our research

A highly-cited, concrete example of this concept's own research idea (microTVM as compiler-based deployment for automatically-discovered, not hand-written, architectures) already realized in practice — a natural bridge between [[NAS]] and this concept.

## Possible thesis topics

Extending MicroNets-style constrained DNAS to incorporate energy directly in the search objective, deploying results via microTVM's UMA accelerator interface.

## Possible collaborations

Arm ML Research, Harvard (Reddi group) — groups working on hardware-aware NAS and TinyML benchmark design.

## Links to related papers

[[2018_Chen_TVM]], [[2019_Elsken_NASSurvey]], [[2021_Banbury_MLPerfTiny]]
