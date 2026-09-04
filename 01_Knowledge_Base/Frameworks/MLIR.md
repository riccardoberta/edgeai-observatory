# MLIR (Multi-Level Intermediate Representation)

MLIR is a compiler infrastructure — originating at Google, now part of the LLVM project — for building custom compiler passes and representations. Instead of every framework/hardware-target combination inventing its own ad hoc intermediate representation, MLIR provides a common, extensible infrastructure ("dialects") where abstraction levels, from high-level tensor graphs down to hardware-specific instructions, can coexist and be progressively "lowered" (translated to a more concrete representation) through shared tooling.

## Evolution of the concept

MLIR's lineage traces directly back to Lattner and Adve's "LLVM: A Compilation Framework for Lifelong Program Analysis & Transformation" (2004), which established the single-static-assignment intermediate representation (a form where every variable is assigned exactly once, simplifying analysis and optimization) and the modular, pass-based infrastructure that made LLVM the dominant general-purpose compiler backend. Chris Lattner, LLVM's original author, later co-created MLIR to solve the analogous fragmentation problem one level up, specifically for machine-learning compiler stacks. Lattner et al. (2020) introduce MLIR to address exactly this fragmentation of ML compiler stacks.

MLIR has since become a substrate underneath several ML deployment efforts relevant to EdgeAI, including parts of the TensorFlow compiler stack and the ONNX-MLIR project for compiling ONNX models (see [[ONNX_Runtime]]). Das and Mannarswamy (2023) show that hardware-cost modeling for MLIR-level compiler optimizations can itself be learned, treating MLIR code as a natural-language-style sequence-modeling problem rather than relying on hand-engineered heuristics. Qualcomm's Hexagon-MLIR (Absar et al., 2026) is a large, industrial-scale demonstration that an NPU vendor can build its AI compilation stack directly on MLIR's dialects and lowering infrastructure, rather than a fully bespoke toolchain, lowering standard front-ends (Triton, PyTorch) to its Hexagon NPU.

A 2025 paper (Lücke et al.) extends MLIR's core infrastructure itself with the Transform Dialect: rather than defining a new dialect for a new abstraction level, as Hexagon-MLIR or ONNX-MLIR do, it makes the transformations and optimization strategies applied to *existing* dialects into first-class, composable, schedulable representation — giving users direct programmatic control over how and when optimizations are applied, instead of relying on a fixed, opaque sequence of compiler passes.

## Key papers

[[2020_Lattner_MLIR]] — the original infrastructure paper defining MLIR's dialect mechanism and its motivation in the context of compiler fragmentation.

[[2004_Lattner_LLVM]] — the foundational general-purpose compiler infrastructure (single-static-assignment IR, modular optimization passes) whose design philosophy MLIR extends to ML-specific, multi-level intermediate representations.

[[2023_Das_MLDrivenHardwareCostModelMLIR]] — learned, natural-language-style hardware-cost model operating directly on MLIR text representations, replacing hand-engineered cost heuristics for compiler optimization passes.

[[2026_Absar_HexagonMLIR]] — open-source, MLIR-based AI compilation stack for Qualcomm's Hexagon NPUs, lowering Triton and PyTorch to NPU-specific code; a large industrial validation of MLIR as shared NPU-compilation infrastructure.

[[2019_Microsoft_ONNXRuntime]] — separates the ONNX graph representation from hardware-specific execution providers, an architectural pattern that parallels MLIR's own separation of high-level graphs from progressively-lowered, hardware-specific dialects.

[[2025_Lucke_MLIRTransformDialect]] — the Transform Dialect: expresses compiler transformations themselves as composable, schedulable MLIR representation, giving fine-grained programmatic control over optimization-strategy construction.

## Open problems

How mature and performant are MLIR-based lowering paths specifically for ultra-constrained microcontroller and NPU targets, compared to more mature, narrower stacks like [[CMSIS-NN]] or [[microTVM_TVM]]'s own scheduling? Building a new dialect still requires significant compiler expertise, which limits how broadly the infrastructure-level benefits translate into easy wins for EdgeAI practitioners without a compiler background.

## Research ideas

A grounded benchmark comparing an MLIR-based deployment path (for example ONNX-MLIR) against TVM/microTVM and CMSIS-NN for the same EdgeAI model and microcontroller/NPU target, measuring engineering effort alongside latency, memory, and energy.

## Possible thesis topics

Evaluating whether an MLIR-based custom dialect for a specific EdgeAI hardware target (for example a particular NPU or DSP) can match hand-optimized vendor SDK performance, and at what engineering cost.

## Links

[[microTVM_TVM]], [[ONNX_Runtime]], [[CMSIS-NN]]
