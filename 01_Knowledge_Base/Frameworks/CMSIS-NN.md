# CMSIS-NN

## Evolution of the concept

CMSIS-NN (Lai et al., 2018, Arm) was created to make neural inference practical on Cortex-M, which has no dedicated hardware for neural computation: hand-written kernels that fully exploit the 16-bit SIMD instructions available on these cores, operating on 8-bit quantized data following the affine scheme compatible with TensorFlow. It quickly became the de facto standard for Cortex-M, later integrated as the kernel backend of TensorFlow Lite Micro.

## Key papers

[[2018_Lai_CMSIS-NN]] — optimized kernels for Cortex-M, 4.6x throughput and 4.9x energy efficiency over an unoptimized baseline.

## Open problems

Generalizing the "hand-optimized kernel" approach toward automatic generation via compiler (TVM) without losing performance. Extension to more recent Cortex-M cores with Helium (MVE) vector instructions, not covered by the original paper.

## Research ideas

Extending the kernels for Cortex-M55/M85 with Helium; automatic kernel generation via compiler for new network architectures (e.g. lightweight attention) not covered by the current library.

## Possible thesis topics

Comparative benchmark between CMSIS-NN and compiler-generated kernels (microTVM) on Cortex-M55/M85 with Helium instructions.

## Links

[[TensorFlow Lite Micro]], [[Cortex-M]], [[Quantization]]
