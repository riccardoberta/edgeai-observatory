# ONNX Runtime

## Evolution of the concept

ONNX Runtime grew out of the need to deploy models trained in any framework (PyTorch, TensorFlow, scikit-learn, etc.) onto heterogeneous hardware without re-implementing them per target. It separates the model graph (in the standardized ONNX format) from the execution backend (pluggable "execution providers" per hardware target), making it a "write once, run anywhere" inference layer. Unlike [[TensorFlow_Lite_Micro]] or [[CMSIS-NN]], it targets primarily mobile/edge-server-class hardware (Cortex-A, edge GPUs/NPUs) rather than ultra-constrained microcontrollers, and — notably for this Observatory — has no single canonical academic paper describing it; both the ONNX exchange format itself (released by Microsoft and Facebook/Meta in 2017) and the runtime are industry-driven open-source projects documented via their own specifications and repositories rather than a peer-reviewed paper, with related academic work covering specific lowering paths (e.g. ONNX-MLIR) or third-party performance characterizations. One such third-party study (Ahn et al., 2023) applies the standardized MLPerf Edge Inference methodology to compare ONNX Runtime against TensorFlow Lite, OpenVINO, and PyTorch under FP16/INT8 quantization on x86 and ARM hardware, finding that quantization speedups vary meaningfully by framework/hardware combination — a useful neutral reference point given the absence of a canonical ONNX Runtime paper.

## Key papers

[[2019_Microsoft_ONNXRuntime]] — overview of the runtime's execution-provider architecture and its role as a framework-agnostic deployment layer; cites the related "Compiling ONNX Neural Network Models Using MLIR" work as one concrete academic reference point.

[[2023_Ahn_QuantizationDNNInferenceEdgeDevices]] — standardized, MLPerf-based cross-framework performance characterization placing ONNX Runtime against TFLite/OpenVINO/PyTorch under quantization on x86/ARM hardware.

## Open problems

How does ONNX Runtime's mobile/edge execution-provider performance compare empirically, on the same model and hardware, to TVM/microTVM and to native vendor SDKs? How complete and stable is ONNX operator coverage for newer model architectures relevant to EdgeAI (e.g. small attention-based models)?

## Research ideas

A controlled benchmark of the same EdgeAI model deployed via ONNX Runtime, TensorFlow Lite Micro, and microTVM on equivalent Cortex-A/Cortex-M hardware, to ground qualitative framework comparisons in measured numbers.

## Possible thesis topics

Comparative benchmark of ONNX Runtime vs. TVM/microTVM vs. native vendor SDKs across a range of EdgeAI hardware tiers (MCU to edge-GPU); evaluation of ONNX export fidelity for newer architectures.

## Links

[[MLIR]], [[microTVM_TVM]], [[TensorFlow_Lite_Micro]], [[Cortex-A]]
