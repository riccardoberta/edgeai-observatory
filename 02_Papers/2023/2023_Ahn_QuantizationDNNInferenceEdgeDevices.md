# Performance Characterization of using Quantization for DNN Inference on Edge Devices

**Full citation:** Ahn, H., Chen, T., Alnaasan, N., Shafi, A., Abduljabbar, M., Subramoni, H., Panda, D.K. (2023). Performance Characterization of using Quantization for DNN Inference on Edge Devices: Extended Version. arXiv:2303.05016. https://arxiv.org/abs/2303.05016

**Linked concepts:** [[ONNX_Runtime]]

## Abstract summary

The authors (Ohio State University) characterize the performance impact of quantization (FP16/INT8, static and dynamic) for DNN inference on edge devices using the MLPerf Edge Inference benchmarking methodology, comparing multiple inference frameworks — including ONNX Runtime, TensorFlow Lite, OpenVINO, and PyTorch — across Intel x86 processors and a Raspberry Pi ARM device.

## Research problem

Quantization is widely used to reduce model size and improve inference performance on edge hardware, but how its benefits vary across different inference frameworks (ONNX Runtime, TFLite, OpenVINO, PyTorch) and different edge hardware (x86 vs. ARM) was not systematically characterized using a standardized benchmarking methodology, making framework/hardware selection decisions for quantized deployment largely anecdotal.

## Key idea

Apply the standardized MLPerf Edge Inference benchmarking methodology consistently across multiple inference frameworks and edge hardware platforms, holding the quantization scheme (FP16/INT8, static/dynamic) and the model set (MobileNetV2, VGG-19, DenseNet-121) fixed, to produce a fair, reproducible comparison of how much each framework/hardware combination benefits from quantization.

## Technical contribution

A systematic, MLPerf-standardized performance characterization spanning ONNX Runtime, TensorFlow Lite, OpenVINO, and PyTorch on both Intel x86 and ARM (Raspberry Pi) hardware, quantifying the speedup each framework/hardware pairing obtains from INT8/FP16 quantization.

## Experimental methodology

Benchmarking of MobileNetV2, VGG-19, and DenseNet-121 under FP32 baseline and FP16/INT8 quantized variants (static and dynamic schemes), run through ONNX Runtime, TensorFlow Lite, OpenVINO (Intel CPU only), and PyTorch, on Intel x86 and Raspberry Pi ARM hardware, following the MLPerf offline inference scenario.

## Results

INT8 quantization delivers substantial speedups across frameworks and hardware (reported as 3.3x with OpenVINO on Intel CPU and 4x with TFLite on Raspberry Pi for the MLPerf offline scenario), but the magnitude of the benefit varies meaningfully by framework and hardware combination, indicating that quantization gains are not uniform across the deployment stack.

## Comparison with the state of the art

Unlike framework-specific quantization papers or vendor benchmarks, this study applies one standardized methodology (MLPerf) consistently across multiple competing frameworks including ONNX Runtime, providing a more neutral, cross-framework comparison point than typically available in the literature.

## Strengths

Standardized, reproducible MLPerf-based methodology; directly compares ONNX Runtime against its main competitors (TFLite, OpenVINO, PyTorch) under identical conditions; covers both x86 and ARM edge hardware.

## Weaknesses

Limited to vision classification models (MobileNetV2, VGG-19, DenseNet-121); does not cover microcontroller-class hardware (Cortex-M) or other EdgeAI application domains (audio, sensor time-series).

## Limitations

OpenVINO comparison is restricted to Intel CPU only, limiting the cross-hardware comparison for that specific framework; evaluation does not include microcontroller-class targets relevant to the more extreme end of our Hardware taxonomy.

## Open questions

How would the relative framework rankings change for non-vision EdgeAI workloads (keyword spotting, HAR, biosignals)? Does ONNX Runtime's relative quantization benefit hold up on microcontroller-class hardware, or only on the Cortex-A/x86-class devices tested here?

## Possible extensions

Extending this MLPerf-standardized methodology to microcontroller-class hardware and non-vision EdgeAI tasks, to determine whether ONNX Runtime's measured quantization benefits on Cortex-A/x86 hardware generalize to the more constrained end of our Hardware taxonomy.

## Relevance to our research

A standardized, neutral reference point for evaluating [[ONNX_Runtime]]'s quantized-inference performance against its main competitors, useful when justifying framework choice for Cortex-A-class or x86-class edge deployment.

## Possible thesis topics

Extending the MLPerf-based cross-framework quantization benchmark to a non-vision EdgeAI task (HAR or keyword spotting) and to microcontroller-class hardware, to test whether the reported framework rankings generalize.

## Possible collaborations

Groups maintaining MLPerf Edge benchmarking infrastructure and cross-framework inference performance studies.

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]], [[2025_Hasanpour_EdgeMark]]
