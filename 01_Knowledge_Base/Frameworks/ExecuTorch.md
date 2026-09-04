# ExecuTorch

ExecuTorch is Meta's PyTorch-native deployment runtime: since PyTorch is the dominant model-authoring framework in current ML research, but the Observatory's other Frameworks concepts are either TensorFlow-native ([[TensorFlow_Lite_Micro]]) or framework-agnostic ([[ONNX_Runtime]], [[microTVM_TVM]]), ExecuTorch fills a real gap by letting a model stay in PyTorch all the way from authoring to deployment, on hardware ranging from embedded microcontrollers up to system-on-chip-class accelerators, without converting to a different framework first.

## Evolution of the concept

ExecuTorch was introduced by Meta ([[2026_Nachin_ExecuTorch]]) as a unified, PyTorch-native deployment pipeline with a pluggable 12-backend architecture, spanning microcontroller to system-on-chip-class hardware. It is validated at genuine production scale — billions of daily inferences across Meta's own apps and Reality Labs devices — distinguishing it from a research prototype, and is benchmarked against llama.cpp, ONNX Runtime, LiteRT, and Core ML on flagship consumer devices.

## Key papers

[[2026_Nachin_ExecuTorch]] — introduces ExecuTorch's PyTorch-native pipeline and pluggable 12-backend architecture, spanning microcontroller to system-on-chip-class hardware; benchmarks against llama.cpp, ONNX Runtime, LiteRT, and Core ML on flagship consumer devices.

## Open problems

How does ExecuTorch's measured performance compare to [[CMSIS-NN]] or [[TensorFlow_Lite_Micro]] specifically at the Cortex-M microcontroller tier, rather than the smartphone-class devices its own benchmark covers? How mature is its operator coverage for newer architectures (small transformers, Mixture-of-Experts) relevant to [[MoE_Edge_LLM_Serving]]?

## Research ideas

A controlled, Cortex-M-tier benchmark of the same model deployed via ExecuTorch, [[TensorFlow_Lite_Micro]], and [[CMSIS-NN]] on equivalent hardware — extending ExecuTorch's own smartphone-tier comparison down to genuinely constrained microcontroller deployment.

## Possible thesis topics

A Cortex-M-tier comparative benchmark of ExecuTorch against [[TensorFlow_Lite_Micro]] and [[CMSIS-NN]] (Master's). An evaluation of ExecuTorch's export fidelity and operator coverage for transformer/Mixture-of-Experts architectures.

## Links

[[TensorFlow_Lite_Micro]], [[ONNX_Runtime]], [[Cortex-M]], [[Quantization]]
