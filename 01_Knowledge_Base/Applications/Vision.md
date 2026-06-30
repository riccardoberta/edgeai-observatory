# Vision

## Evolution of the concept

The line of research starts well before edge constraints entered the picture: Krizhevsky, Sutskever, and Hinton's "ImageNet Classification with Deep Convolutional Neural Networks" (AlexNet, NeurIPS 2012) is the result that proved deep CNNs could dramatically outperform prior approaches on large-scale image classification, triggering the shift to CNN-based vision that MobileNet later had to make efficient enough for mobile and embedded hardware. The vision-on-edge line of research arises from the need to run CNNs for classification/detection on mobile and embedded devices. MobileNet (Howard et al., 2017) is the foundational architecture: depthwise-separable convolutions and two global multipliers to trade off accuracy and cost, which became the standard backbone for much subsequent research on quantization and hardware-aware NAS (e.g. Once-for-All). The 2023-2025 wave has shifted the efficient-architecture question from CNNs to hybrid CNN/transformer designs: TinyNeXt (Zeng et al., ICCV 2025) targets the memory-bound nature of standard self-attention specifically, introducing a Lean Single-Head Self-Attention mechanism and a stage-aware macro design to bring transformer-style representations within reach of TinyML-class memory budgets, extending the "efficient-by-design" philosophy MobileNet pioneered to a new architecture family.

## Key papers

[[2012_Krizhevsky_AlexNet]] — the AlexNet result that established deep CNNs as the dominant approach to image classification, the starting point of the line of work MobileNet later makes efficient for edge/mobile hardware.

[[2017_Howard_MobileNets]] — efficient-by-design architecture, reference backbone for vision on edge/mobile.

[[2025_Zeng_TinyNeXt]] — hybrid CNN/transformer architecture with a memory-efficient self-attention mechanism, extending efficient-by-design principles from CNNs to transformers for TinyML.

[[2018_Flamand_GAP8]] — RISC-V multi-core platform with a dedicated convolution engine, a hardware target for low-power always-on vision (CNN inference) at the edge.

[[2019_Ignatov_AIBenchmarkSmartphones]] — cross-vendor benchmark of deep learning vision models across major mobile Cortex-A SoCs, the empirical counterpart to architecture-level efficient-vision research.

[[2021_Yazdanbakhsh_EdgeTPUEvaluation]] — large-scale empirical sweep of CNN architectures on Edge TPU hardware, producing performance/energy estimators directly useful for efficient-vision-model design.

## Open problems

How efficient does the depthwise-separable factorization remain on hardware very different from mobile CPU/GPU (e.g. microcontrollers without efficient SIMD support for depthwise operations).

## Research ideas

Quantized/binary versions of MobileNet for Cortex-M; NAS for automatic search of the width/resolution multipliers specific to a target hardware.

## Possible thesis topics

Study of the real efficiency of depthwise-separable convolutions on Cortex-M with CMSIS-NN, compared to standard convolutions at equal accuracy.

## Links

[[NAS]], [[Quantization]], [[Cortex-M]]
