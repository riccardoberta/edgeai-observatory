# Vision

## Evolution of the concept

The line of research starts well before edge constraints entered the picture: Krizhevsky, Sutskever, and Hinton's "ImageNet Classification with Deep Convolutional Neural Networks" (AlexNet, NeurIPS 2012) is the result that proved deep CNNs could dramatically outperform prior approaches on large-scale image classification, triggering the shift to CNN-based vision that MobileNet later had to make efficient enough for mobile and embedded hardware. The vision-on-edge line of research arises from the need to run CNNs for classification/detection on mobile and embedded devices. MobileNet (Howard et al., 2017) is the foundational architecture: depthwise-separable convolutions and two global multipliers to trade off accuracy and cost, which became the standard backbone for much subsequent research on quantization and hardware-aware NAS (e.g. Once-for-All).

## Key papers

[[2012_Krizhevsky_AlexNet]] — the AlexNet result that established deep CNNs as the dominant approach to image classification, the starting point of the line of work MobileNet later makes efficient for edge/mobile hardware.

[[2017_Howard_MobileNets]] — efficient-by-design architecture, reference backbone for vision on edge/mobile.

## Open problems

How efficient does the depthwise-separable factorization remain on hardware very different from mobile CPU/GPU (e.g. microcontrollers without efficient SIMD support for depthwise operations).

## Research ideas

Quantized/binary versions of MobileNet for Cortex-M; NAS for automatic search of the width/resolution multipliers specific to a target hardware.

## Possible thesis topics

Study of the real efficiency of depthwise-separable convolutions on Cortex-M with CMSIS-NN, compared to standard convolutions at equal accuracy.

## Links

[[NAS]], [[Quantization]], [[Cortex-M]]
