# Instruction Sets Should Be Free: The Case For RISC-V

**Full citation:** Asanović, K., Patterson, D.A. (2014). Instruction Sets Should Be Free: The Case For RISC-V. *UC Berkeley Technical Report UCB/EECS-2014-146*. https://www2.eecs.berkeley.edu/Pubs/TechRpts/2014/EECS-2014-146.pdf

**Linked concepts:** [[RISC-V]]

## Abstract summary

The authors argue that instruction set architectures (ISAs) should be open and royalty-free, much like open standards in networking and software, and present RISC-V as a clean, modern, modular, and extensible open ISA designed to support this model — contrasting it with the proprietary, licensed ISAs (e.g. ARM, x86) that dominated the industry at the time.

## Research problem

Proprietary, licensed instruction set architectures impose licensing costs and legal/IP barriers on hardware innovation, research, and education, and tend to accumulate legacy complexity over decades of backward-compatible extensions; this limits who can design custom processors and slows architectural experimentation, particularly for academic research and specialized/niche hardware.

## Key idea

An ISA, like a network protocol or a file format standard, benefits the entire ecosystem more by being open and free to implement than by being a licensed, proprietary product; a deliberately clean, modular, and extensible base ISA (with optional standard extensions) can serve both as a practical, real-world-competitive architecture and as a long-lived open foundation for research, education, and custom silicon.

## Technical contribution

The argument and economic/technical case for open ISAs in general; the RISC-V ISA design itself — a small, clean base integer instruction set with a modular system of optional standard extensions (e.g. for floating point, atomics, vector operations), explicitly designed to avoid the legacy-complexity accumulation of older proprietary ISAs.

## Experimental methodology

Presents comparative analysis of RISC-V's design simplicity and extensibility against established proprietary ISAs, along with the broader economic and licensing case for openness, supported by early RISC-V implementations and the growing academic/research ecosystem already adopting it at the time of writing.

## Results

Establishes RISC-V as a credible, technically sound open alternative to proprietary ISAs, with a design that supports everything from tiny embedded cores to high-performance application processors via its modular extension system, without requiring per-implementation licensing fees.

## Comparison with the state of the art

Directly contrasts with the dominant licensed ISA model of the time (ARM, x86 and others), arguing that openness is both technically and economically advantageous for an ISA in a way that licensed alternatives structurally cannot match, given their business models.

## Strengths

A compelling, well-argued case that proved prescient: RISC-V has since grown into a major, widely adopted open ISA across academia, embedded systems, and increasingly commercial silicon, including specialized EdgeAI accelerators.

## Weaknesses

At the time of writing, RISC-V was a young architecture without the mature software/compiler ecosystem, commercial silicon track record, or vendor support that established proprietary ISAs already had — a gap that has narrowed substantially since but was a real limitation in 2014.

## Limitations

The paper makes a forward-looking architectural and economic argument rather than presenting extensive real-world deployment data, since RISC-V silicon and tooling were still nascent at publication time.

## Open questions

How does an open ISA's extension ecosystem avoid fragmenting into incompatible variants as many independent vendors and research groups add custom extensions, particularly for specialized domains like machine learning acceleration?

## Possible extensions

Custom RISC-V extensions specifically for efficient neural network inference (vector/matrix instructions for ML workloads), which several RISC-V-based EdgeAI chips (e.g. GAP-8) have since pursued, building directly on the openness and modularity argued for here.

## Relevance to our research

The founding argument for an open, royalty-free ISA; the precondition that makes RISC-V-based EdgeAI hardware viable as a vendor-lock-in-free alternative to ARM Cortex-M/A-based designs, directly relevant whenever the Observatory evaluates RISC-V-based edge accelerators.

## Possible thesis topics

A comparative evaluation of a RISC-V-based EdgeAI accelerator (e.g. GAP-8) against an equivalent ARM Cortex-M-based solution, assessing whether the openness argued for here translates into measurable practical advantages (cost, customizability, ecosystem maturity) for a specific TinyML application today.

## Possible collaborations

Open hardware and RISC-V research groups, and silicon vendors developing RISC-V-based EdgeAI accelerators.

## Links to related papers

[[2014_Chen_DianNao]]
