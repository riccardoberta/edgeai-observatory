# TensorFlow Lite Micro

TensorFlow Lite Micro (TFLM) is Google's inference runtime for microcontrollers: no operating system, kilobytes of RAM, the most widely used runtime at the very low end of the hardware spectrum.

## Evolution of the concept

TFLM (David et al., 2021) arises from the observation that existing inference frameworks assume an operating system and dynamic memory allocation — assumptions not valid on microcontrollers with only a few tens or hundreds of kilobytes of RAM. The answer is a minimal interpreter with static memory allocation and swappable per-platform kernels, including CMSIS-NN for Cortex-M (see [[CMSIS-NN]]). It has become the reference runtime for the MLPerf Tiny benchmark (see [[MLPerf_Tiny]]), the standardized cross-vendor benchmark that gives the microcontroller-class inference field a common yardstick, and against which several TFLM-based submissions are measured.

Two more recent threads test the limits of the TFLM-centered ecosystem from different angles. MicroFlow (Carnelos et al., 2024) shows that a from-scratch Rust-based engine can match TFLM's resource efficiency while adding compile-time memory-safety guarantees, on microcontrollers with as little as 2 KB of RAM. EdgeMark (Hasanpour et al., 2025) builds a reproducible cross-tool automation and benchmarking framework that places TFLM head-to-head against other embedded-AI tools (Edge Impulse, Ekkono, Renesas eAI Translator), giving a more systematic basis for tool-selection decisions than informal comparisons.

An earlier paper (Manor and Greenberg, 2022) attacks the interpreter-versus-compiled-code performance gap from the hardware side rather than the compiler side: pairing a modified TFLM software stack with a custom microcontroller-NPU hardware accelerator, offloading TFLM's compute-heavy kernels to dedicated silicon while preserving TFLM's portable software interface, reaching up to 724x speedup over pure-software TFLM execution on the same microcontroller class.

## Key papers

[[2021_David_TensorFlowLiteMicro]] — runtime architecture, static memory planner, interoperability with the TensorFlow ecosystem.

[[2021_Banbury_MLPerfTiny]] — standardized benchmark suite for extremely low-power/microcontroller-class inference, with TFLM as one of its reference runtimes; defines the evaluation methodology much of the surrounding literature reports against.

[[2024_Carnelos_MicroFlow]] — Rust-based TinyML inference engine matching TFLM's resource efficiency while adding compile-time memory-safety guarantees, validated down to 2 KB-RAM 8-bit microcontrollers.

[[2025_Hasanpour_EdgeMark]] — automation and benchmarking system enabling reproducible cross-tool comparison of TFLM against other embedded-AI tools.

[[2026_Jain_TinyFed6G]] — uses TFLM-class deployment as the on-device execution layer for federated-learning devices running differently-quantized model variants.

[[2022_Manor_CustomHardwareTFLMAccelerator]] — modified TFLM software stack paired with a custom microcontroller-NPU hardware accelerator, reaching up to 724x speedup over pure-software TFLM execution on the same microcontroller class.

## Open problems

The performance gap between the generic interpreter (TFLM) and ad hoc compiled code (microTVM) as model complexity grows — the custom-hardware-offload work above closes part of this gap from the hardware side (724x via a custom microcontroller-NPU), but how that compares to microTVM's compiler-side answer, or to CMSIS-NN's software-kernel answer, on the same baseline hardware, remains untested. Native support for lightweight on-device fine-tuning, not currently central to the runtime's design.

## Research ideas

Tighter integration between TFLM and compilers like microTVM to generate model-specific kernels. Extending TFLM toward a lightweight on-device learning mechanism.

## Possible thesis topics

An experimental comparison between TFLM and microTVM on a common set of TinyML models, measuring the generic interpreter's overhead.

## Links

[[CMSIS-NN]], [[microTVM_TVM]], [[Cortex-M]], [[Keyword_Spotting]]
