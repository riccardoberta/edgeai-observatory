# DSP

## Evolution of the concept

Digital signal processor (DSP) class hardware is the traditional substrate for always-on, ultra-low-power signal-processing workloads (notably audio) at the edge, and remains highly relevant for tasks like keyword spotting where a device must listen continuously within a tight power budget. As neural networks took over many of these signal-processing tasks, the research direction shifted from hand-designed DSP algorithms toward co-designing the neural network and the DSP-class accelerator together, since the joint design space (network architecture choices × accelerator configuration choices) is far larger than either dimension explored alone. The HANNAH framework is a representative example of this automated joint-search direction, rather than a single canonical "DSP" paper — DSP-class accelerators for audio sensing are a fragmented landscape of vendor-specific designs more often described in product literature than in a single foundational publication, so this entry should be read as representative rather than canonical.

## Key papers

[[2022_Gerum_HANNAH]] — automated joint neural-network/hardware-accelerator co-design framework for ultra-low-power audio processing devices, chosen as a representative (not singularly canonical) DSP/audio-accelerator paper.

## Open problems

How does joint network/accelerator co-search (HANNAH-style) compare, in solution quality and search cost, to a two-stage hardware-aware NAS approach over a fixed DSP accelerator? Can the same joint-search philosophy generalize beyond audio to other always-on sensing modalities (biosignals, vibration for predictive maintenance)?

## Research ideas

Comparative study of joint network/accelerator co-search versus sequential hardware-aware NAS for a fixed always-on audio sensing task, measuring search cost against final solution quality.

## Possible thesis topics

Applying HANNAH-style joint co-design to a non-audio always-on sensing task in our [[Applications]] taxonomy (e.g. biosignals or predictive maintenance vibration sensing); benchmarking DSP-class accelerators against NPU and Cortex-M+CMSIS-NN deployments for the same keyword-spotting task.

## Links

[[Keyword_Spotting]], [[NAS]], [[Cortex-M]], [[NPU]]
