# DSP (Digital Signal Processor)

A DSP is a processor core optimized for the repetitive multiply-accumulate math common in signal processing, and remains the traditional substrate for always-on, ultra-low-power signal-processing workloads at the edge — notably audio, where a device must listen continuously within a tight power budget, as in keyword spotting.

## Evolution of the concept

An early, concrete demonstration of replacing the back end of a classic analog/DSP signal chain with a learned classifier is Yang et al.'s "A 1μW Voice Activity Detector Using Analog Feature Extraction and Digital Deep Neural Network" (2018), which pairs analog front-end feature extraction with a small digital DNN classifier to detect speech at microwatt-level power — anticipating the network/accelerator co-design direction below. A closely related design, Giraldo et al.'s Vocell (2020), extends this pattern from single-task voice-activity detection to a complete always-on pipeline: a mixed-signal system-on-chip interfacing directly to an analog microphone, combining a dedicated neural accelerator for speaker-verification embeddings with a general-purpose RISC-V core for feature extraction and classification, at 10 μW for combined keyword spotting and speaker verification.

As neural networks took over many signal-processing tasks, research shifted from hand-designed DSP algorithms toward co-designing the neural network and the DSP-class accelerator together, since the joint design space — network architecture choices times accelerator configuration choices — is far larger than either dimension explored alone. The HANNAH framework (see [[NAS]]) is a representative example of this automated joint-search direction; DSP-class accelerators for audio sensing are otherwise a fragmented landscape of vendor-specific designs more often described in product literature than in a single foundational publication, so this entry should be read as representative rather than pointing to one canonical "DSP" paper.

Two studies update this picture with a system-level lens. Bartoli et al. (2025) show that the DSP-domain feature-extraction stage — computing MFCCs (Mel-Frequency Cepstral Coefficients, a standard compact audio representation) — is itself a non-negligible contributor to total keyword-spotting pipeline cost across three STM32 platform tiers, not just the neural-inference stage that prior efficiency studies usually isolate. Liang et al. (2025) demonstrate, via a working FPGA-based prototype, that a dedicated keyword-spotting accelerator co-designed with the algorithm can push latency, power, and cost further than running the same task on a general-purpose DSP/microcontroller. Bartoli et al.'s finding that feature extraction is an overlooked cost center is itself anticipated by Wu et al.'s 2023 keyword-spotting chip, which attacks the feature-extraction stage directly, replacing the standard MFCC front end with a lighter subband-energy feature-extraction scheme to reach 34.7 μW system power while retaining competitive accuracy — evidence that optimizing the feature-extraction stage is a distinct and increasingly recognized lever alongside classifier compression.

## Key papers

[[2018_Yang_VoiceActivityDetector]] — combines an analog feature-extraction front end with a small digital DNN classifier to achieve microwatt-level always-on voice-activity detection; an early concrete instance of the signal-processing/learned-classifier co-design later generalized by HANNAH-style frameworks.

[[2020_Giraldo_Vocell]] — silicon-validated 65 nm mixed-signal system-on-chip combining a dedicated neural accelerator for speaker verification with a RISC-V core for feature extraction/classification, achieving combined keyword spotting and speaker verification at 10 μW.

[[2022_Gerum_HANNAH]] — automated joint neural-network/hardware-accelerator co-design framework for ultra-low-power audio processing devices, a representative (not singularly canonical) DSP/audio-accelerator paper.

[[2025_Bartoli_EndToEndKeywordSpotting]] — system-level keyword-spotting benchmark across three STM32 tiers, showing the DSP-domain MFCC feature-extraction stage is a significant, often-overlooked contributor to total pipeline cost.

[[2025_Liang_IntelligentAudioSoC]] — dedicated keyword-spotting accelerator co-designed with the algorithm into an audio system-on-chip, validated via a working FPGA-based prototype.

[[2023_Wu_KeywordSpottingIC]] — always-on keyword-spotting chip replacing the standard MFCC front end with subband-energy feature extraction, reaching 34.7 μW system power.

## Open problems

How does joint network/accelerator co-search (HANNAH-style) compare, in solution quality and search cost, to a two-stage hardware-aware NAS approach over a fixed DSP accelerator? Can the same joint-search philosophy generalize beyond audio to other always-on sensing modalities, such as biosignals or vibration for predictive maintenance?

## Research ideas

A comparative study of joint network/accelerator co-search versus sequential hardware-aware NAS for a fixed always-on audio sensing task, measuring search cost against final solution quality.

## Possible thesis topics

Applying HANNAH-style joint co-design to a non-audio always-on sensing task, such as biosignals or predictive-maintenance vibration sensing. Benchmarking DSP-class accelerators against NPU and Cortex-M+CMSIS-NN deployments for the same keyword-spotting task.

## Links

[[Keyword_Spotting]], [[NAS]], [[Cortex-M]], [[NPU]], [[RISC-V]]
