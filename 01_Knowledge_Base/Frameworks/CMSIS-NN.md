# CMSIS-NN

## Evolution of the concept

The kernel-design technique CMSIS-NN relies on — expressing convolution as a matrix-matrix product (im2col-style unrolling) so it can run on optimized BLAS/SIMD routines instead of naive nested loops — traces back to Chellapilla, Puri, and Simard's "High Performance Convolutional Neural Networks for Document Processing" (IWFHR 2006), which first showed unrolled-convolution-via-BLAS giving a 2.4-3.0x speedup over direct convolution. CMSIS-NN (Lai et al., 2018, Arm) applies the same underlying principle, adapted to Cortex-M's 16-bit SIMD instructions and 8-bit quantized data following the affine scheme compatible with TensorFlow, to make neural inference practical on cores with no dedicated hardware for neural computation. It quickly became the de facto standard for Cortex-M, later integrated as the kernel backend of TensorFlow Lite Micro.

## Key papers

[[2006_Chellapilla_HighPerformanceCNNDocumentProcessing]] — first demonstration that unrolling convolution into a matrix-matrix product and running it through optimized BLAS routines beats direct/naive convolution; the general technique CMSIS-NN's GEMM-based kernels build on.

[[2018_Lai_CMSIS-NN]] — optimized kernels for Cortex-M, 4.6x throughput and 4.9x energy efficiency over an unoptimized baseline.

## Open problems

Generalizing the "hand-optimized kernel" approach toward automatic generation via compiler (TVM) without losing performance. Extension to more recent Cortex-M cores with Helium (MVE) vector instructions, not covered by the original paper.

## Research ideas

Extending the kernels for Cortex-M55/M85 with Helium; automatic kernel generation via compiler for new network architectures (e.g. lightweight attention) not covered by the current library.

## Possible thesis topics

Comparative benchmark between CMSIS-NN and compiler-generated kernels (microTVM) on Cortex-M55/M85 with Helium instructions.

## Links

[[TensorFlow Lite Micro]], [[Cortex-M]], [[Quantization]]
