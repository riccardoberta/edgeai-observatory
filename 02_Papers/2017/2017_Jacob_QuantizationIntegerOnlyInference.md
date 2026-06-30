# Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference

**Full citation:** Jacob, B., Kligys, S., Chen, B., Zhu, M., Tang, M., Howard, A., Adam, H., Kalenichenko, D. (2018). Quantization and Training of Neural Networks for Efficient Integer-Arithmetic-Only Inference. *Proceedings of the IEEE Conference on Computer Vision and Pattern Recognition (CVPR)*, pp. 2704–2713. arXiv:1712.05877. https://arxiv.org/abs/1712.05877

**Linked concepts:** [[Quantization]]

## Abstract summary

The authors (Google team) propose a quantization scheme that allows inference to run using integer-only arithmetic for both weights and activations, keeping accuracy close to the float32 model. They also introduce a training method that simulates quantization (quantization-aware training) to recover the accuracy lost in smaller models.

## Research problem

Floating-point inference is expensive on mobile and embedded hardware that lacks efficient floating-point units. A way is needed to reduce numerical precision without degrading accuracy too much, and to do so in a manner that is efficiently implementable on integer-only hardware.

## Key idea

Quantize weights and activations to 8-bit integers using an affine scheme (scale + zero-point), and implement all network operations (convolutions, sums, multiplications) using integer-only arithmetic, avoiding floating-point conversions during inference.

## Technical contribution

An affine quantization scheme with efficient computation on integer hardware; a training framework that inserts quantization-simulation nodes into the training graph (quantization-aware training, QAT) so the network learns to be robust to the precision loss; benchmarks on architectures such as MobileNet.

## Experimental methodology

Comparison between float32 models, post-training quantized models, and models with quantization-aware training, on ImageNet classification with MobileNet and other CNN architectures, measuring accuracy and latency on real mobile (ARM) hardware.

## Results

QAT recovers nearly all the accuracy lost by naive post-training quantization, especially on already-compact architectures like MobileNet, where the post-training loss is more pronounced. Significant latency gains on mobile CPUs thanks to integer arithmetic.

## Comparison with the state of the art

Compared to the "naive" post-training quantization common at the time, QAT substantially narrows the accuracy gap, especially for already-small models where every bit of precision matters more.

## Strengths

Simple scheme to implement, compatible with cheap integer-only hardware, conceptual basis that directly influenced TensorFlow Lite and most of the subsequent mobile inference stacks.

## Weaknesses

Focuses on 8 bits; does not explore more aggressive precisions (4-bit, binary) that require different techniques. QAT requires access to the full training pipeline, not always available for third-party models.

## Limitations

Latency gains depend heavily on hardware support for integer arithmetic; on hardware with an efficient FPU the advantage shrinks.

## Open questions

How to extend the scheme to sub-8-bit precision while keeping the same implementation simplicity? How to automate the choice of which layers to quantize aggressively vs. conservatively?

## Possible extensions

Mixed precision (layer-by-layer); data-free quantization for scenarios without access to the original training set.

## Relevance to our research

Foundational paper for any work on efficient inference on microcontrollers: the affine quantization scheme described here underlies both CMSIS-NN and TensorFlow Lite Micro.

## Possible thesis topics

Comparative study between QAT and more recent post-training quantization techniques on models for microcontrollers; extension of QAT to binary/ternary networks for Cortex-M.

## Possible collaborations

Groups working on compilers/runtimes for edge (TVM, TFLite Micro) and on ARM/RISC-V hardware with integer SIMD support.

## Links to related papers

[[2018_Lai_CMSIS-NN]], [[2021_David_TensorFlowLiteMicro]], [[2017_Howard_MobileNets]]
