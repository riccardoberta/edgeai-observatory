# ONNX Runtime

ONNX (Open Neural Network Exchange) is a standardized model-exchange format; ONNX Runtime is a cross-framework inference engine that runs models exported in that format. It grew out of the need to deploy models trained in any framework (PyTorch, TensorFlow, scikit-learn, and others) onto heterogeneous hardware without re-implementing them per target: it separates the model graph (in the standardized ONNX format) from the execution backend (pluggable "execution providers" per hardware target), making it a "write once, run anywhere" inference layer. Unlike [[TensorFlow_Lite_Micro]] or [[CMSIS-NN]], it targets primarily mobile and edge-server-class hardware (Cortex-A, edge GPUs/NPUs) rather than ultra-constrained microcontrollers.

## Evolution of the concept

Notably for this Observatory, ONNX Runtime has no single canonical academic paper describing it: both the ONNX exchange format itself (released by Microsoft and Facebook/Meta in 2017) and the runtime are industry-driven open-source projects, documented via their own specifications and repositories rather than a peer-reviewed paper. Related academic work instead covers specific lowering paths (for example ONNX-MLIR, see [[MLIR]]) or third-party performance characterizations.

One such third-party study (Ahn et al., 2023) applies the standardized MLPerf Edge Inference methodology (see [[MLPerf_Tiny]]) to compare ONNX Runtime against TensorFlow Lite, OpenVINO, and PyTorch under 16-bit and 8-bit quantization on x86 and ARM hardware, finding that quantization speedups vary meaningfully by framework/hardware combination — a useful neutral reference point given the absence of a canonical ONNX Runtime paper. A second example (Zhao, 2025) uses ONNX Runtime as the deployment substrate for a unified, resource-aware inference-acceleration framework for generative models — combining mixed-precision quantization, sparse attention, and dynamic expert routing, adapted at runtime — demonstrated on Jetson Orin-class edge hardware, showing that ONNX Runtime's execution-provider architecture can support dynamic, input-dependent computation-path switching, not just static graph execution.

## Key papers

[[2019_Microsoft_ONNXRuntime]] — overview of the runtime's execution-provider architecture and its role as a framework-agnostic deployment layer; cites the related "Compiling ONNX Neural Network Models Using MLIR" work as one concrete academic reference point.

[[2023_Ahn_QuantizationDNNInferenceEdgeDevices]] — standardized, MLPerf-based cross-framework performance characterization placing ONNX Runtime against TensorFlow Lite, OpenVINO, and PyTorch under quantization on x86/ARM hardware.

[[2025_Zhao_UnifiedResourceAwareEdgeInference]] — unified mixed-precision-quantization, sparse-attention, and dynamic-expert-routing framework for generative-model inference, implemented and deployed via ONNX Runtime on Jetson Orin-class edge hardware.

## Open problems

How does ONNX Runtime's mobile/edge execution-provider performance compare empirically, on the same model and hardware, to TVM/microTVM and to native vendor SDKs? How complete and stable is ONNX operator coverage for newer model architectures relevant to EdgeAI, such as small attention-based models?

## Research ideas

A controlled benchmark of the same EdgeAI model deployed via ONNX Runtime, TensorFlow Lite Micro, and microTVM on equivalent Cortex-A/Cortex-M hardware, to ground qualitative framework comparisons in measured numbers.

## Possible thesis topics

A comparative benchmark of ONNX Runtime versus TVM/microTVM versus native vendor SDKs across a range of EdgeAI hardware tiers (microcontroller to edge-GPU). An evaluation of ONNX export fidelity for newer architectures.

## Links

[[MLIR]], [[microTVM_TVM]], [[TensorFlow_Lite_Micro]], [[Cortex-A]]
