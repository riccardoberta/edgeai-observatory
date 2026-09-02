# TensorFlow Lite Micro

## Evolution of the concept

TFLM (David et al., 2021) arises from the observation that existing inference frameworks assume an operating system and dynamic memory allocation — assumptions not valid on microcontrollers with only a few tens/hundreds of KB of RAM. The answer is a minimal interpreter with static memory allocation and swappable per-platform kernels (including CMSIS-NN for Cortex-M). It has become the reference runtime for the MLPerf Tiny benchmark (Banbury et al., NeurIPS 2021 Datasets & Benchmarks Track), the standardized cross-vendor benchmark that gives the MCU-class inference field a common yardstick and that several TFLM-based submissions are measured against. Two more recent threads test the limits of the TFLM-centered ecosystem from different angles: MicroFlow (Carnelos et al., 2024) shows that a from-scratch Rust-based engine can match TFLM's resource efficiency while adding compile-time memory-safety guarantees, on MCUs with as little as 2 KB of RAM; and EdgeMark (Hasanpour et al., 2025) builds a reproducible cross-tool automation/benchmarking framework that places TFLM head-to-head against other eAI tools (Edge Impulse, Ekkono, Renesas eAI Translator), giving a more systematic basis for tool-selection decisions than informal comparisons. An earlier IEEE Access paper (Manor and Greenberg, 2022) attacks the interpreter-versus-compiled-code performance gap from the hardware side rather than the compiler side: pairing a modified TFLM software stack with a custom MCU-NPU hardware accelerator, offloading TFLM's compute-heavy kernels to dedicated silicon while preserving TFLM's portable software interface, reaching up to 724x speedup over pure-software TFLM execution on the same microcontroller class.

## Key papers

[[2021_David_TensorFlowLiteMicro]] — runtime architecture, static memory planner, interoperability with the TensorFlow ecosystem.

[[2021_Banbury_MLPerfTiny]] — standardized benchmark suite for extremely low-power/MCU-class inference, with TFLM as one of its reference runtimes; defines the evaluation methodology much of the surrounding literature reports against.

[[2024_Carnelos_MicroFlow]] — Rust-based TinyML inference engine matching TFLM's resource efficiency while adding compile-time memory-safety guarantees, validated down to 2 KB-RAM 8-bit MCUs.

[[2025_Hasanpour_EdgeMark]] — automation and benchmarking system enabling reproducible cross-tool comparison of TFLM against other embedded AI tools.

[[2026_Jain_TinyFed6G]] — uses TFLM-class deployment as the on-device execution layer for federated-learning devices running differently-quantized model variants.

[[2022_Manor_CustomHardwareTFLMAccelerator]] — modified TFLM software stack paired with a custom MCU-NPU hardware accelerator, reaching up to 724x speedup over pure-software TFLM execution on the same microcontroller class; IEEE Access.

## Open problems

Performance gap between the generic interpreter (TFLM) and ad-hoc compiled code (microTVM) as model complexity grows — [[2022_Manor_CustomHardwareTFLMAccelerator]] closes part of this gap from the hardware-offload side (724x via a custom MCU-NPU), but how that compares to microTVM's compiler-side answer or to CMSIS-NN's software-kernel answer, on the same baseline hardware, remains untested. Native support for lightweight on-device fine-tuning, not currently central to the runtime's design.

## Research ideas

Tighter integration between TFLM and compilers like microTVM to generate model-specific kernels; extending TFLM toward a lightweight on-device learning mechanism.

## Possible thesis topics

Experimental comparison between TFLM and microTVM on a common set of TinyML models, measuring the generic interpreter's overhead.

## Links

[[CMSIS-NN]], [[microTVM_TVM|microTVM]], [[Cortex-M]], [[Keyword Spotting]]
