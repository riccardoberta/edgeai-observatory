# MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications

**Full citation:** Howard, A.G., Zhu, M., Chen, B., Kalenichenko, D., Wang, W., Weyand, T., Andreetto, M., Adam, H. (2017). MobileNets: Efficient Convolutional Neural Networks for Mobile Vision Applications. arXiv:1704.04861. https://arxiv.org/abs/1704.04861

**Linked concepts:** [[Vision]], [[NAS]] (reference architecture for later search-based work)

## Abstract summary

The authors (Google) present MobileNets, a family of CNN architectures based on depthwise-separable convolutions, which drastically reduce parameters and operations compared to standard CNNs, with two global hyperparameters (width multiplier and resolution multiplier) to trade off accuracy and computational cost.

## Research problem

State-of-the-art CNNs for vision (VGG, ResNet) are too expensive in terms of parameters and operations to run efficiently on mobile and embedded devices with latency and energy constraints.

## Key idea

Replace standard convolutions with depthwise-separable convolutions, which factorize a standard convolution into a depthwise convolution (per channel) followed by a pointwise (1x1) convolution, drastically reducing the number of operations at equal representational capacity.

## Technical contribution

The MobileNet architecture based on depthwise-separable blocks; introduction of the width multiplier and resolution multiplier as simple "knobs" to obtain models of different sizes without redesigning the architecture.

## Experimental methodology

Evaluation on ImageNet classification and downstream tasks (object detection, face attributes, fine-grained geolocalization), comparing accuracy, number of parameters, and operations (FLOPs) against standard CNNs such as VGG and GoogleNet.

## Results

MobileNet achieves competitive accuracy with VGG-16 using a tiny fraction of the parameters and operations; the family of models obtained by varying the two multipliers allows choosing the optimal point on the accuracy/cost curve for a given use case.

## Comparison with the state of the art

Compared to the CNNs of the time, designed only to maximize accuracy, MobileNet is among the first architectures explicitly designed for mobile efficiency, opening a research line (efficient-by-design architectures) that would culminate in MobileNetV2/V3 and in hardware-aware NAS.

## Strengths

Conceptual simplicity, wide adoption as a backbone for mobile/embedded applications, starting point for much subsequent research on quantization and NAS.

## Weaknesses

The two hyperparameters are chosen manually and relatively coarsely: it is not an automatic search for the best trade-off, unlike later NAS approaches.

## Limitations

Validated mainly on image classification; transfer to very different tasks still requires empirical re-validation.

## Open questions

How efficient does the depthwise-separable factorization remain on hardware very different from mobile CPU/GPU (e.g. microcontrollers without efficient SIMD support for depthwise operations)?

## Possible extensions

Quantized/binary versions of MobileNet for Cortex-M; automatic search (NAS) of the width/resolution multipliers for specific hardware, as later done by Once-for-All.

## Relevance to our research

A reference architecture used as baseline in many TinyML and quantization papers; useful as a standard backbone for embedded vision experiments.

## Possible thesis topics

Study of the real efficiency of depthwise-separable convolutions on Cortex-M with CMSIS-NN, compared to standard convolutions at equal accuracy.

## Possible collaborations

Groups working on edge vision benchmarks (e.g. Visual Wake Words) and on compilers optimized for depthwise operators.

## Links to related papers

[[2019_Cai_OnceForAll]], [[2017_Jacob_QuantizationIntegerOnlyInference]]
