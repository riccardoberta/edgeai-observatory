# MicroFlow: An Efficient Rust-Based Inference Engine for TinyML

**Full citation:** Carnelos, M., Pasti, F., Bellotto, N. (2024). MicroFlow: An Efficient Rust-Based Inference Engine for TinyML. arXiv:2409.19432. https://arxiv.org/abs/2409.19432

**Linked concepts:** [[TensorFlow_Lite_Micro]]

## Abstract summary

The authors (University of Padua, Grepit AB) present MicroFlow, an open-source TinyML inference engine written in Rust, designed to exploit Rust's compile-time memory safety guarantees for deploying neural networks on highly resource-constrained, bare-metal microcontrollers, including 8-bit MCUs with as little as 2 KB of RAM.

## Research problem

Established TinyML inference runtimes such as TensorFlow Lite Micro are written in C/C++, a choice that trades memory-safety guarantees for low-level control; for critical or safety-relevant embedded applications, the absence of compile-time memory-safety checking is a genuine risk, and it is unclear whether a memory-safe language like Rust can match C/C++-based runtimes in resource efficiency on extremely constrained hardware.

## Key idea

Build a compiler-based TinyML inference engine in Rust that translates a trained model directly into safe, statically-checked Rust code ahead of deployment, combining Rust's ownership/borrow-checking memory-safety model with the static memory planning techniques already used by C/C++-based engines like TFLM.

## Technical contribution

The MicroFlow engine itself, an open-source Rust-based compiler/runtime for neural network inference on bare-metal targets; an empirical demonstration that memory safety does not require sacrificing the extreme resource efficiency needed for sub-2KB-RAM 8-bit microcontrollers.

## Experimental methodology

Evaluation of MicroFlow against TensorFlow Lite Micro and other TinyML runtimes on standard benchmark models, measuring memory footprint, inference latency, and energy consumption on real microcontroller hardware, including very constrained 8-bit targets.

## Results

MicroFlow matches or exceeds the resource efficiency (memory footprint, latency) of TensorFlow Lite Micro on the evaluated benchmarks while additionally providing Rust's compile-time memory-safety guarantees, successfully deploying on 8-bit MCUs with only 2 KB of RAM.

## Comparison with the state of the art

Positions itself as a safety-oriented alternative to the C/C++-based TFLM/CMSIS-NN stack that has dominated TinyML inference, demonstrating that a memory-safe systems language can be competitive on the field's most resource-constrained targets rather than only on more capable hardware.

## Strengths

Concrete, hardware-validated efficiency comparable to the incumbent C/C++ runtime; addresses a genuine and under-addressed safety concern (memory bugs in embedded ML deployment); fully open-source.

## Weaknesses

As a newer, smaller project, the operator/model coverage and tooling ecosystem are less mature than TFLM's, which benefits from broader industry adoption and tool support.

## Limitations

Evaluated on a benchmark set of standard models; broader coverage of model architectures (e.g. attention-based models) and of non-Arm targets is not yet as extensively validated as for TFLM.

## Open questions

Does the Rust memory-safety guarantee meaningfully reduce real-world deployment bugs in practice, and by how much, compared to disciplined C/C++ development practices? Can MicroFlow's approach extend to on-device training, not just inference?

## Possible extensions

Extending MicroFlow's compiler-based approach to support on-device learning (sparse updates, as in TinyTrain) within the same memory-safety guarantees; broadening operator coverage to match TFLM/CMSIS-NN.

## Relevance to our research

A relevant safety-oriented alternative within the [[TensorFlow_Lite_Micro]] ecosystem, worth tracking as memory-safety becomes a more prominent concern for critical embedded EdgeAI deployments.

## Possible thesis topics

A head-to-head benchmark of MicroFlow versus TFLM/CMSIS-NN on a realistic EdgeAI application (keyword spotting or HAR) deployed on the same Cortex-M hardware, measuring both efficiency and developer-facing safety properties.

## Possible collaborations

Groups working on memory-safe systems programming for embedded ML and on formal verification of embedded inference pipelines.

## Links to related papers

[[2021_David_TensorFlowLiteMicro]], [[2018_Lai_CMSIS-NN]]
