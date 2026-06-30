# TensorFlow Lite Micro

## Evolution of the concept

TFLM (David et al., 2021) arises from the observation that existing inference frameworks assume an operating system and dynamic memory allocation — assumptions not valid on microcontrollers with only a few tens/hundreds of KB of RAM. The answer is a minimal interpreter with static memory allocation and swappable per-platform kernels (including CMSIS-NN for Cortex-M). It has become the reference runtime for the MLPerf Tiny benchmark (Banbury et al., NeurIPS 2021 Datasets & Benchmarks Track), the standardized cross-vendor benchmark that gives the MCU-class inference field a common yardstick and that several TFLM-based submissions are measured against.

## Key papers

[[2021_David_TensorFlowLiteMicro]] — runtime architecture, static memory planner, interoperability with the TensorFlow ecosystem.

[[2021_Banbury_MLPerfTiny]] — standardized benchmark suite for extremely low-power/MCU-class inference, with TFLM as one of its reference runtimes; defines the evaluation methodology much of the surrounding literature reports against.

## Open problems

Performance gap between the generic interpreter (TFLM) and ad-hoc compiled code (microTVM) as model complexity grows. Native support for lightweight on-device fine-tuning, not currently central to the runtime's design.

## Research ideas

Tighter integration between TFLM and compilers like microTVM to generate model-specific kernels; extending TFLM toward a lightweight on-device learning mechanism.

## Possible thesis topics

Experimental comparison between TFLM and microTVM on a common set of TinyML models, measuring the generic interpreter's overhead.

## Links

[[CMSIS-NN]], [[microTVM]], [[Cortex-M]], [[Keyword Spotting]]
