# Vision

## Evolution of the concept

The vision-on-edge line of research arises from the need to run CNNs for classification/detection on mobile and embedded devices. MobileNet (Howard et al., 2017) is the foundational architecture: depthwise-separable convolutions and two global multipliers to trade off accuracy and cost, which became the standard backbone for much subsequent research on quantization and hardware-aware NAS (e.g. Once-for-All).

## Key papers

[[2017_Howard_MobileNets]] — efficient-by-design architecture, reference backbone for vision on edge/mobile.

## Open problems

How efficient does the depthwise-separable factorization remain on hardware very different from mobile CPU/GPU (e.g. microcontrollers without efficient SIMD support for depthwise operations).

## Research ideas

Quantized/binary versions of MobileNet for Cortex-M; NAS for automatic search of the width/resolution multipliers specific to a target hardware.

## Possible thesis topics

Study of the real efficiency of depthwise-separable convolutions on Cortex-M with CMSIS-NN, compared to standard convolutions at equal accuracy.

## Links

[[NAS]], [[Quantization]], [[Cortex-M]]
