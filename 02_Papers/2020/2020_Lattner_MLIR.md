# MLIR: A Compiler Infrastructure for the End of Moore's Law

**Full citation:** Lattner, C., Amini, M., Bondhugula, U., Cohen, A., Davis, A., Pienaar, J., Riddle, R., Shpeisman, T., Vasilache, N., Zinenko, O. (2020). MLIR: A Compiler Infrastructure for the End of Moore's Law. arXiv:2002.11054. https://arxiv.org/abs/2002.11054

**Linked concepts:** [[MLIR]], [[microTVM_TVM]]

## Abstract summary

The authors (Google) present MLIR (Multi-Level Intermediate Representation), a reusable and extensible compiler infrastructure designed to reduce the cost of building domain-specific compilers, improve code generation for heterogeneous hardware, and let different compilers and abstraction levels interoperate, motivated by the slowdown of general-purpose performance scaling (the "end of Moore's Law") that pushes more workloads toward specialized accelerators.

## Research problem

Modern ML and hardware ecosystems are fragmented: every new accelerator, domain-specific language, or framework tends to grow its own ad-hoc intermediate representation and compiler stack, duplicating engineering effort and making it hard to share optimizations across levels of abstraction (from high-level tensor graphs down to hardware-specific instructions).

## Key idea

Define a common, extensible IR infrastructure ("dialects") where each abstraction level — from framework-level tensor operations to low-level hardware instructions — can be represented and progressively lowered through well-defined transformations, allowing optimization passes and infrastructure to be reused across very different compilers and targets instead of rebuilt from scratch each time.

## Technical contribution

The MLIR dialect mechanism itself: a system for defining custom operations, types, and transformations that coexist within one infrastructure, plus a standard set of reusable dialects and passes; demonstrated use as the foundation for multiple production compiler efforts (e.g. TensorFlow's compiler stack, accelerator-specific backends).

## Experimental methodology

Primarily a systems/infrastructure paper rather than a benchmark-driven one: it argues its case through design rationale, case studies of dialects built on top of MLIR (e.g. for TensorFlow graphs, for polyhedral loop optimization, for hardware-specific lowering), and qualitative evidence of adoption across Google's compiler efforts at the time of writing.

## Results

Demonstrated that a single infrastructure can host multiple dialects spanning very different abstraction levels (from high-level ML graphs to low-level hardware IR) and that this enables sharing of common optimizations and infrastructure that would otherwise be duplicated per compiler.

## Comparison with the state of the art

Prior compiler infrastructures (e.g. LLVM IR alone) were not designed with ML workloads' multi-level abstraction needs in mind, forcing ML compiler projects (XLA, TVM, Glow, etc.) to build mostly separate stacks; MLIR explicitly targets this gap by being usable as a shared substrate beneath or alongside such projects, including later integration with [[microTVM_TVM]]'s ecosystem and with ONNX tooling (e.g. the ONNX-MLIR project).

## Strengths

Strong adoption and ecosystem impact since publication (used inside TensorFlow, several hardware vendor toolchains, and as a common substrate referenced by other ML-compiler projects); the dialect mechanism is genuinely reusable rather than ML-specific, giving it longevity beyond a single hardware generation.

## Weaknesses

As an infrastructure paper, it offers limited quantitative evidence (no standard benchmark comparison against alternative compiler stacks); the benefits (reduced duplication, easier cross-team sharing) are inherently more visible in long-term ecosystem effects than in a single paper's experiments.

## Limitations

Building a new dialect and lowering pipeline still requires significant compiler expertise; MLIR by itself does not guarantee good performance on a given target — that still depends on the quality of dialects and lowering passes built for it, which for many EdgeAI-relevant targets (specific MCU/NPU backends) were still maturing at publication time.

## Open questions

How mature and performant are MLIR-based lowering paths specifically for ultra-constrained MCU and NPU targets relevant to EdgeAI, compared to more mature, narrower stacks like CMSIS-NN or TVM's own scheduling? How does MLIR-based tooling (e.g. ONNX-MLIR) compare in practice to TVM/microTVM for deploying the same model on the same constrained hardware?

## Possible extensions

A concrete benchmark comparing an MLIR-based deployment path (e.g. via ONNX-MLIR) against [[microTVM_TVM]] and [[CMSIS-NN]] for the same EdgeAI model and target MCU, to ground the qualitative infrastructure claims in measured latency/memory/energy numbers relevant to this Observatory's taxonomy.

## Relevance to our research

Background/infrastructure reference for the [[MLIR]] concept: relevant whenever evaluating or building a deployment toolchain for EdgeAI models, since several frameworks in our Frameworks taxonomy branch (TVM, ONNX Runtime via ONNX-MLIR) are built on or interoperate with MLIR.

## Possible thesis topics

A comparative benchmark of MLIR-based vs. TVM-based vs. vendor-SDK (CMSIS-NN) deployment paths for a fixed EdgeAI model on a fixed MCU target, measuring engineering effort, latency, memory footprint, and energy.

## Possible collaborations

Compiler-infrastructure groups working on ML deployment toolchains (e.g. teams contributing to TVM, ONNX-MLIR, or vendor NPU compiler backends).

## Links to related papers

[[2018_Chen_TVM]] (alternative/complementary ML compiler stack), [[2018_Lai_CMSIS-NN]] (hand-optimized alternative to compiler-based lowering for Cortex-M)
