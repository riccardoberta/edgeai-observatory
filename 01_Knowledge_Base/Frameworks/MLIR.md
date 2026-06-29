# MLIR

## Evolution of the concept

Lattner et al. (2020) introduce MLIR (Multi-Level Intermediate Representation) to address the fragmentation of ML compiler stacks: instead of every framework/hardware-target combination building its own ad-hoc intermediate representation, MLIR provides a common, extensible infrastructure ("dialects") where abstraction levels — from high-level tensor graphs down to hardware-specific instructions — can coexist and be progressively lowered through shared tooling. It has since become a substrate underneath several ML deployment efforts relevant to EdgeAI, including parts of the TensorFlow compiler stack and the ONNX-MLIR project for compiling ONNX models.

## Key papers

[[2020_Lattner_MLIR]] — the original infrastructure paper defining MLIR's dialect mechanism and its motivation in the context of compiler fragmentation and the "end of Moore's Law."

## Open problems

How mature and performant are MLIR-based lowering paths specifically for ultra-constrained MCU and NPU targets, compared to more mature, narrower stacks like [[CMSIS-NN]] or [[microTVM_TVM]]'s own scheduling? Building a new dialect still requires significant compiler expertise, limiting how broadly the infrastructure-level benefits translate into easy wins for EdgeAI practitioners without compiler backgrounds.

## Research ideas

A grounded benchmark comparing an MLIR-based deployment path (e.g. ONNX-MLIR) against TVM/microTVM and CMSIS-NN for the same EdgeAI model and MCU/NPU target, measuring engineering effort alongside latency, memory, and energy.

## Possible thesis topics

Evaluating whether an MLIR-based custom dialect for a specific EdgeAI hardware target (e.g. a particular NPU or DSP) can match hand-optimized vendor SDK performance, and at what engineering cost.

## Links

[[microTVM_TVM]], [[ONNX_Runtime]], [[CMSIS-NN]]
