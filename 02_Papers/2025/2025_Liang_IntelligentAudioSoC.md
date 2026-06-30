# Prototype: A Keyword Spotting-Based Intelligent Audio SoC for IoT

**Full citation:** Liang, H., Jia, D., Wang, Y., Huang, L., Zhong, S., Xiang, L., Huang, L., Yuan, T. (2025). Prototype: A Keyword Spotting-Based Intelligent Audio SoC for IoT. arXiv:2509.06964. https://arxiv.org/abs/2509.06964

**Linked concepts:** [[DSP]], [[Keyword_Spotting]]

## Abstract summary

The authors present a compact intelligent audio system-on-chip that integrates a dedicated keyword-spotting accelerator for ultra-low-latency, low-power, low-cost voice interaction in IoT devices, using algorithm-hardware co-design and demonstrating the design through a live FPGA-based prototype.

## Research problem

General-purpose MCU/DSP platforms running keyword spotting in software still incur latency, power, and cost overheads that limit always-on voice-interaction deployment in cost-sensitive IoT devices; a tighter, purpose-built hardware/algorithm co-design is needed to push further on all three axes simultaneously.

## Key idea

Co-design the keyword-spotting algorithm and a dedicated accelerator block together as a single SoC component, rather than running an off-the-shelf keyword-spotting model on a general-purpose DSP/MCU, to jointly minimize latency, power, and silicon cost.

## Technical contribution

A dedicated keyword-spotting accelerator architecture integrated into an audio-focused SoC design; an algorithm-hardware co-design methodology demonstrated end-to-end via a working FPGA-based prototype rather than only simulation.

## Experimental methodology

Implementation and live demonstration of the SoC's keyword-spotting accelerator on an FPGA prototype platform, characterizing latency, power, and cost-relevant design metrics for the integrated design.

## Results

The FPGA-based prototype demonstrates a functioning, low-latency, low-power keyword-spotting accelerator integrated as part of a complete audio SoC pipeline, validating the co-design approach in working hardware rather than only on paper.

## Comparison with the state of the art

Complements general-purpose DSP/MCU keyword-spotting deployments (e.g. CMSIS-NN/TFLM on Cortex-M, or system-level MFCC-plus-inference studies) with a fully dedicated accelerator path, trading flexibility for tighter latency/power/cost optimization.

## Strengths

End-to-end hardware demonstration (FPGA prototype) rather than purely architectural proposal; explicit joint optimization of latency, power, and cost rather than any single metric alone.

## Weaknesses

FPGA prototyping does not directly establish ASIC-level power/cost figures, which would require silicon fabrication to fully validate the IoT cost-sensitivity claims.

## Limitations

Demonstrated specifically for keyword spotting; generalizing the same dedicated-accelerator co-design approach to other always-on audio tasks (e.g. voice activity detection, sound event detection) is not directly shown.

## Open questions

How does this dedicated accelerator's energy-per-decision compare quantitatively to Helium-accelerated Cortex-M or to NPU-based keyword-spotting deployments on the same task and model? What is the silicon-level (ASIC) cost and power profile once moved beyond the FPGA prototype?

## Possible extensions

ASIC implementation and silicon-level characterization of the prototyped accelerator; extending the co-design methodology to other always-on audio tasks beyond keyword spotting.

## Relevance to our research

Adds a dedicated-accelerator, hardware-validated data point to the DSP entry's always-on audio-sensing focus, complementing the system-level software-pipeline perspective of the companion TKWS study added in the same update.

## Possible thesis topics

Benchmarking this dedicated accelerator design against Helium-accelerated Cortex-M and NPU-based keyword-spotting deployments on a common task; ASIC cost/power projection study for the prototyped architecture.

## Possible collaborations

Groups working on FPGA-based accelerator prototyping and on always-on audio SoC design relevant to the [[Keyword_Spotting]] application area.

## Links to related papers

[[2018_Yang_VoiceActivityDetector]], [[2025_Bartoli_EndToEndKeywordSpotting]]
