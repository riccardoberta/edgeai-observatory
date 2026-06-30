# AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration

**Full citation:** Lin, J., Tang, J., Tang, H., Yang, S., Chen, W.-M., Wang, W.-C., Xiao, G., Dang, X., Gan, C., Han, S. (2024). AWQ: Activation-aware Weight Quantization for LLM Compression and Acceleration. Proceedings of MLSys 2024 (Best Paper Award). https://arxiv.org/abs/2306.00978

**Linked concepts:** [[Quantization]]

## Abstract summary

The authors (MIT, with collaborators) propose AWQ, a post-training weight-only quantization method for large language models that protects a small fraction of "salient" weight channels — identified by looking at activation magnitudes rather than weight magnitudes — from quantization error, instead of relying on mixed-precision storage or backpropagation-based calibration.

## Research problem

Quantizing LLMs to low bit-widths (e.g. INT4/INT3) for on-device deployment causes significant accuracy degradation, and existing approaches either require expensive backpropagation/regression-based calibration (GPTQ-style) or mixed-precision hardware support that is hard to deploy efficiently.

## Key idea

A small percentage of weight channels are disproportionately important to model accuracy, and which channels matter can be identified by observing activation magnitudes (not weight magnitudes); scaling these salient channels before quantization protects them from quantization error without needing mixed-precision storage.

## Technical contribution

The activation-aware salient-channel-detection method; a per-channel scaling search that reduces quantization error for these channels while keeping the entire model in a uniform low-bit format; the TinyChat inference engine, which fuses the dequantization and matrix multiplication on edge GPUs/CPUs to realize the theoretical speedup in practice.

## Experimental methodology

Evaluation on multiple LLM families (LLaMA, OPT, and instruction-tuned/multi-modal variants) at INT4/INT3 weight-only quantization, measuring perplexity and downstream task accuracy against full-precision and other post-training quantization baselines (GPTQ, RTN), plus on-device latency/throughput measurements on edge GPUs (Jetson Orin) and laptop/desktop hardware via the TinyChat engine.

## Results

AWQ matches or exceeds GPTQ-level accuracy without requiring any backpropagation or regression, generalizes better to instruction-tuned and multi-modal models, and the TinyChat engine delivers measured end-to-end speedups (reported as over 3x versus FP16 implementations) on edge GPU hardware.

## Comparison with the state of the art

Unlike GPTQ, which calibrates quantization via a layer-wise regression procedure, AWQ requires no backpropagation or reconstruction, making it cheaper to apply and more robust to overfitting on a small calibration set; it positions itself as the more practical and more generalizable choice for deploying quantized LLMs at the edge.

## Strengths

Simple, calibration-set-light method; strong empirical generalization across model families and tasks; comes with a paired, hardware-realized inference engine (TinyChat) rather than only a theoretical compression ratio.

## Weaknesses

Focused on weight-only quantization; activation quantization (which would further reduce compute, not just memory) is not addressed by this method.

## Limitations

Evaluated primarily on GPU-class edge hardware (Jetson Orin, laptops); applicability to microcontroller-class targets (Cortex-M) without a GPU is not directly demonstrated.

## Open questions

How well does activation-aware salient-channel protection transfer to extreme low-bit regimes (INT2/binary) relevant to microcontroller deployment? Can the salient-channel-detection idea be combined with structured pruning for further compression?

## Possible extensions

Combining AWQ-style activation-aware scaling with structured pruning ([[Pruning]]) or with hardware-aware NAS to jointly optimize bit-width and architecture for a target edge accelerator.

## Relevance to our research

A practical, widely-adopted reference method for deploying quantized LLMs on edge GPU-class hardware; relevant to the broader 2023-2024 shift in [[Quantization]] research toward edge deployment of large language models rather than only CNNs.

## Possible thesis topics

Benchmarking AWQ-quantized small language models on edge GPU/NPU hardware against CNN-era quantization baselines for latency and energy per token.

## Possible collaborations

Groups working on edge LLM inference engines and on hardware-aware co-design of quantization and accelerator architecture.

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]], [[2016_Hubara_BinarizedNeuralNetworks]]
