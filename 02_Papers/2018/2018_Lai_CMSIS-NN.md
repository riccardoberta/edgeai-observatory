# CMSIS-NN: Efficient Neural Network Kernels for Arm Cortex-M CPUs

**Full citation:** Lai, L., Suda, N., Chandra, V. (2018). CMSIS-NN: Efficient Neural Network Kernels for Arm Cortex-M CPUs. arXiv:1801.06601. https://arxiv.org/abs/1801.06601

**Linked concepts:** [[CMSIS-NN]], [[Cortex-M]]

## Abstract summary

The authors (Arm) present CMSIS-NN, a library of low-level kernels optimized to run neural networks on Cortex-M processors, obtained through 8-bit quantization and exploitation of the SIMD instructions available on these cores, reporting improvements of 4.6x in throughput and 4.9x in energy efficiency.

## Research problem

Cortex-M-based microcontrollers, a typical target for low-power IoT applications, have no dedicated hardware for neural computation and require highly optimized software kernels to make inference practical within the energy and latency constraints.

## Key idea

Implement neural network primitives (convolutions, pooling, activations, fully-connected layers) as kernels written to fully exploit the 16-bit SIMD instructions of Cortex-M (DSP instruction set), operating on 8-bit quantized data following the affine scheme compatible with TensorFlow.

## Technical contribution

A set of open-source kernels integrated into Arm's CMSIS framework; a quantization scheme and memory layout designed to minimize data transfers and maximize cache reuse, given the extremely limited memory of Cortex-M devices.

## Experimental methodology

Benchmarking the kernels on reference CNNs (e.g. a small CNN for CIFAR-10) running on real Cortex-M microcontrollers, comparing throughput and energy per inference against an unoptimized reference implementation.

## Results

4.6x improvement in runtime throughput and 4.9x improvement in energy efficiency relative to the baseline implementation, at equal accuracy of the quantized model.

## Comparison with the state of the art

At the time, no standard equivalent existed for Cortex-M; CMSIS-NN quickly became the de facto reference, later integrated as the kernel backend of TensorFlow Lite Micro.

## Strengths

Very deep specialization on the target hardware, widely adopted in industry, actively maintained by Arm, compatible with TensorFlow's quantization scheme.

## Weaknesses

Specific to the Cortex-M family: it brings no benefit to other architectures (RISC-V, DSP) that require their own optimized kernels; hand-tuned optimizations are hard to maintain as model architectures evolve.

## Limitations

Covers mainly classic CNNs; support for more recent architectures (attention, lightweight Transformers) requires extensions not covered by the original paper.

## Open questions

How to generalize the "hand-optimized kernel" approach toward automatic generation via compiler (e.g. TVM) without losing performance? How well do the gains transfer to more recent Cortex-M cores with vector extensions (Helium/MVE)?

## Possible extensions

Extending the kernels to support the Helium (MVE) instructions of Cortex-M55/M85; automatic kernel generation via compiler for new network architectures.

## Relevance to our research

A core infrastructural component for any efficient-inference experiment on Cortex-M; often the actual backend behind the benchmarks reported in TinyML papers.

## Possible thesis topics

Comparative benchmark between CMSIS-NN and compiler-generated kernels (microTVM) on Cortex-M55/M85 with Helium instructions; extension of the kernels to operators for compact sequence-to-sequence models.

## Possible collaborations

Arm (maintainer of the library), TinyML groups working on MLPerf Tiny benchmarks.

## Links to related papers

[[2021_David_TensorFlowLiteMicro]], [[2017_Jacob_QuantizationIntegerOnlyInference]]
