# End-to-End Efficiency in Keyword Spotting: A System-Level Approach for Embedded Microcontrollers

**Full citation:** Bartoli, P., Bondini, T., Veronesi, C., Giudici, A., Antonello, N., Zappa, F. (2025). End-to-End Efficiency in Keyword Spotting: A System-Level Approach for Embedded Microcontrollers. arXiv:2509.07051. https://arxiv.org/abs/2509.07051

**Linked concepts:** [[DSP]], [[Keyword_Spotting]]

## Abstract summary

The authors analyze the entire keyword-spotting processing pipeline — from MFCC (Mel-Frequency Cepstral Coefficient) feature extraction, a classic DSP-domain operation, through to neural inference — and propose TKWS, a compact residual-block architecture, benchmarking the full pipeline's efficiency across three STM32 microcontroller platforms (N6, H7, U5).

## Research problem

Keyword-spotting efficiency studies often evaluate only the neural network inference stage in isolation, while the DSP-domain feature-extraction front end (MFCC computation) can be a comparably significant contributor to total latency and energy on real microcontroller hardware — a system-level, pipeline-wide view is needed to identify where the actual bottlenecks lie.

## Key idea

Treat keyword spotting as a single end-to-end system (DSP feature extraction plus neural inference) and benchmark it as a whole across multiple real MCU platforms with different DSP/compute capability profiles, rather than benchmarking the neural network component alone.

## Technical contribution

TKWS, a compact residual-block neural architecture for keyword spotting; a system-level benchmarking methodology that attributes latency/energy across the MFCC feature-extraction and neural-inference stages separately, across three STM32 platform tiers.

## Experimental methodology

End-to-end benchmarking of the full MFCC-plus-TKWS pipeline on STM32 N6, H7, and U5 platforms, measuring F1-score, parameter count, and per-stage latency/energy breakdown.

## Results

The TKWS architecture (three residual blocks, only 14.4k parameters) achieves up to 92.4% F1-score, while the system-level breakdown reveals that the DSP-domain feature-extraction stage is a non-negligible contributor to total pipeline cost across all three MCU tiers.

## Comparison with the state of the art

Extends classic keyword-spotting MCU benchmarks (originally framed around neural-network-only comparisons) to explicitly include the DSP feature-extraction stage, providing a more complete system-level efficiency picture than network-only studies.

## Strengths

Multi-platform benchmarking (three distinct STM32 tiers) rather than a single MCU; explicit per-stage cost attribution that exposes the often-overlooked DSP feature-extraction overhead.

## Weaknesses

Limited to MFCC-based feature extraction and the STM32 platform family; generality to other always-on sensing front ends (analog feature extraction, other MCU vendors) is not directly tested.

## Limitations

Evaluated specifically on keyword spotting; whether the same DSP-stage-bottleneck finding generalizes to other always-on audio/sensing tasks is an open question.

## Open questions

How much of the DSP feature-extraction cost could be eliminated by learned, end-to-end front ends that bypass MFCC entirely? Does the same system-level (DSP-plus-inference) cost balance hold on dedicated DSP/NPU-equipped platforms rather than general-purpose Cortex-M MCUs?

## Possible extensions

Replacing the fixed MFCC front end with a learned feature extractor and re-measuring the system-level cost balance; extending the benchmarking methodology to Cortex-M+NPU or DSP-accelerated platforms.

## Relevance to our research

Brings the DSP hardware entry into the 2023-2026 window with a concrete, system-level efficiency study, directly connecting [[DSP]] to the [[Keyword_Spotting]] application area with a full-pipeline (not network-only) measurement.

## Possible thesis topics

Comparing fixed (MFCC) versus learned feature-extraction front ends for the same TKWS-class network on STM32 hardware; extending the system-level benchmarking methodology to a DSP- or NPU-accelerated MCU platform.

## Possible collaborations

Groups maintaining always-on audio sensing benchmarks and STM32-based EdgeAI toolchains.

## Links to related papers

[[2018_Yang_VoiceActivityDetector]], [[2022_Gerum_HANNAH]]
