# Vision

Vision covers image classification, object detection, and related visual tasks running on constrained hardware, typically built on efficient CNN or hybrid CNN/transformer architectures.

## Evolution of the concept

The line of research starts well before edge constraints entered the picture: Krizhevsky, Sutskever, and Hinton's AlexNet ("ImageNet Classification with Deep Convolutional Neural Networks", 2012) proved deep CNNs could dramatically outperform prior approaches on large-scale image classification, triggering the shift to CNN-based vision that later work had to make efficient enough for mobile and embedded hardware. Zhang et al.'s ShuffleNet (2018) is one of the most-cited efficient-CNN-architecture papers in the field, a direct architectural sibling introducing pointwise group convolution and channel shuffle as further efficiency primitives.

MobileNet (Howard et al., 2017) is the foundational efficient-vision architecture: depthwise-separable convolutions (a cheaper alternative to standard convolution) plus two global multipliers to trade accuracy for cost, which became the standard backbone for much subsequent research on quantization and hardware-aware NAS (see [[NAS]]).

The 2023–2025 wave has shifted the efficient-architecture question from pure CNNs to hybrid CNN/transformer designs. TinyNeXt (Zeng et al., 2025) targets the memory-bound nature of standard self-attention specifically, introducing a lean single-head self-attention mechanism and a stage-aware macro design to bring transformer-style representations within reach of TinyML-class memory budgets, extending MobileNet's "efficient by design" philosophy to a new architecture family. A 2026 paper (Zhang) attacks a different bottleneck in the same problem: rather than the attention mechanism's memory footprint, it targets the hardware cost of the nonlinear operations surrounding attention (Layer Normalization, Softmax, GELU), replacing them with hardware-friendly approximations within a CNN-transformer hybrid pyramid architecture — evidence that "efficient vision transformer for the edge" is now a multi-front problem (attention memory, surrounding nonlinearities, and parameter count) rather than a single bottleneck to solve.

This concept had also been classification-only for some time despite object detection being an equally central edge-vision task. Moosmann et al.'s TinyissimoYOLO (2023) closes that gap: a quantized, sub-0.5 MB YOLO-family detector deployed on the MAX78000 microcontroller at up to 180 frames per second and 196 microjoules per inference.

## Key papers

[[2012_Krizhevsky_AlexNet]] — the AlexNet result that established deep CNNs as the dominant approach to image classification, the starting point of the line of work MobileNet later makes efficient for edge/mobile hardware.

[[2017_Howard_MobileNets]] — efficient-by-design architecture, the reference backbone for vision on edge/mobile hardware.

[[2025_Zeng_TinyNeXt]] — hybrid CNN/transformer architecture with a memory-efficient self-attention mechanism, extending efficient-by-design principles from CNNs to transformers for TinyML.

[[2018_Flamand_GAP8]] — RISC-V multi-core platform with a dedicated convolution engine, a hardware target for low-power always-on vision (CNN inference) at the edge.

[[2019_Ignatov_AIBenchmarkSmartphones]] — cross-vendor benchmark of deep learning vision models across major mobile Cortex-A SoCs, the empirical counterpart to architecture-level efficient-vision research.

[[2021_Yazdanbakhsh_EdgeTPUEvaluation]] — large-scale empirical sweep of CNN architectures on Edge TPU hardware, producing performance/energy estimators directly useful for efficient-vision-model design.

[[2026_Zhang_HardwareFriendlyViT]] — hardware-friendly CNN-transformer hybrid pyramid architecture replacing GELU/LayerNorm/Softmax with hardware-cheap approximations (ReLU, BatchNorm, a simplified "Softmax2") for low-power embedded vision.

[[2018_Zhang_ShuffleNet]] — pointwise group convolution and channel shuffle as further CNN efficiency primitives beyond depthwise-separable convolution, one of the most-cited efficient-CNN-architecture papers and a direct sibling to MobileNet.

[[2023_Moosmann_TinyissimoYOLO]] — quantized, sub-0.5 MB YOLO-family object detector deployed on the MAX78000 microcontroller (180 fps, 196 µJ/inference), extending this concept's coverage from classification into detection.

## Open problems

How efficient does the depthwise-separable factorization remain on hardware very different from mobile CPU/GPU — for example microcontrollers without efficient SIMD (single-instruction-multiple-data) support for depthwise operations.

## Research ideas

Quantized/binary versions of MobileNet for Cortex-M. NAS for automatic search of the width/resolution multipliers specific to a target hardware.

## Possible thesis topics

A study of the real efficiency of depthwise-separable convolutions on Cortex-M with CMSIS-NN, compared to standard convolutions at equal accuracy.

## Links

[[NAS]], [[Quantization]], [[Cortex-M]]
