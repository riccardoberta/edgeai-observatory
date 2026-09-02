# ExecuTorch

## Evolution of the concept

Created 2026-09-02 to close a Frameworks coverage gap: PyTorch is the dominant model-authoring framework in current ML research, yet the Observatory's Frameworks branch previously had no representation for PyTorch-native edge deployment, only TensorFlow-native ([[TensorFlow_Lite_Micro]]) and framework-agnostic ([[ONNX_Runtime]], [[microTVM_TVM]]) paths. ExecuTorch, introduced by Meta in [[2026_Nachin_ExecuTorch]], fills this directly: a unified, PyTorch-native deployment pipeline scaling from embedded microcontrollers to SoC-class accelerators without requiring model conversion out of PyTorch. It is validated at genuine production scale (billions of daily inferences across Meta's apps and Reality Labs devices), distinguishing it from a research prototype.

## Key papers

[[2026_Nachin_ExecuTorch]] — introduces ExecuTorch's PyTorch-native pipeline and pluggable 12-backend architecture, spanning microcontroller to SoC-class hardware; benchmarks against llama.cpp, ONNX Runtime, LiteRT, and Core ML on flagship consumer devices.

## Open problems

How does ExecuTorch's measured performance compare to [[CMSIS-NN]] or [[TensorFlow_Lite_Micro]] specifically at the Cortex-M microcontroller tier, rather than the smartphone-class devices its own benchmark covers? How mature is its operator coverage for newer architectures (small transformers, MoE) relevant to [[Mixture-of-Experts (MoE) & Edge LLM Serving]]?

## Research ideas

A controlled, Cortex-M-tier benchmark of the same model deployed via ExecuTorch, [[TensorFlow_Lite_Micro]], and [[CMSIS-NN]] on equivalent hardware — extending ExecuTorch's own smartphone-tier comparison down to genuinely constrained microcontroller deployment.

## Possible thesis topics

Cortex-M-tier comparative benchmark of ExecuTorch against [[TensorFlow_Lite_Micro]] and [[CMSIS-NN]] (Master's); evaluation of ExecuTorch's export fidelity and operator coverage for transformer/MoE architectures.

## Links

[[TensorFlow_Lite_Micro]], [[ONNX_Runtime]], [[Cortex-M]], [[Quantization]]
