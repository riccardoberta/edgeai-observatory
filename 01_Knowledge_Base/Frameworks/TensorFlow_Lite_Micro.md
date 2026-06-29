# TensorFlow Lite Micro

## Evolution of the concept

TFLM (David et al., 2021) arises from the observation that existing inference frameworks assume an operating system and dynamic memory allocation — assumptions not valid on microcontrollers with only a few tens/hundreds of KB of RAM. The answer is a minimal interpreter with static memory allocation and swappable per-platform kernels (including CMSIS-NN for Cortex-M). It has become the reference runtime for the MLPerf Tiny benchmark.

## Key papers

[[2021_David_TensorFlowLiteMicro]] — runtime architecture, static memory planner, interoperability with the TensorFlow ecosystem.

## Open problems

Performance gap between the generic interpreter (TFLM) and ad-hoc compiled code (microTVM) as model complexity grows. Native support for lightweight on-device fine-tuning, not currently central to the runtime's design.

## Research ideas

Tighter integration between TFLM and compilers like microTVM to generate model-specific kernels; extending TFLM toward a lightweight on-device learning mechanism.

## Possible thesis topics

Experimental comparison between TFLM and microTVM on a common set of TinyML models, measuring the generic interpreter's overhead.

## Links

[[CMSIS-NN]], [[microTVM]], [[Cortex-M]], [[Keyword Spotting]]
