# CMSIS-NN

CMSIS-NN is Arm's library of hand-optimized neural-network kernels (convolution, matrix multiplication, and similar) for Cortex-M microcontrollers, often used underneath [[TensorFlow_Lite_Micro]] to accelerate the actual math.

## Evolution of the concept

The kernel-design technique CMSIS-NN relies on — expressing convolution as a matrix-matrix product ("im2col"-style unrolling) so it can run on optimized linear-algebra/SIMD routines instead of naive nested loops — traces back to Chellapilla, Puri, and Simard's "High Performance Convolutional Neural Networks for Document Processing" (2006), which first showed unrolled-convolution-via-matrix-multiplication giving a 2.4–3.0x speedup over direct convolution.

CMSIS-NN (Lai et al., 2018, Arm) applies the same underlying principle, adapted to Cortex-M's 16-bit SIMD instructions and 8-bit quantized data following an affine scheme compatible with TensorFlow, to make neural inference practical on cores with no dedicated hardware for neural computation. It quickly became the de facto standard for Cortex-M, later integrated as the kernel backend of TensorFlow Lite Micro, and reports 4.6x throughput and 4.9x energy efficiency over an unoptimized baseline.

A 2025 survey (Abushahla et al.) situates CMSIS-NN within the broader, more fragmented landscape of microcontroller quantization platforms — alongside RISC-V-based and hybrid/NPU-enabled software stacks — noting that the kernel library itself has remained comparatively stable while most recent progress has come from the algorithmic (quantization-method) side rather than from further low-level kernel innovation.

Jung, Burrello, Scherer, Conti, and Benini (2025) extend hand-optimized kernels beyond convolution toward lightweight transformer attention — an extension CMSIS-NN itself does not cover — by building an MCU kernel library specifically for the attention block's data-movement patterns, reporting higher data reuse than CMSIS-NN's general-purpose kernels, plus a "Fused-Weight Self-Attention" scheduling technique that reduces the number of attention operations via offline weight fusion.

## Key papers

[[2006_Chellapilla_HighPerformanceCNNDocumentProcessing]] — first demonstration that unrolling convolution into a matrix-matrix product and running it through optimized linear-algebra routines beats direct/naive convolution; the general technique CMSIS-NN's kernels build on.

[[2018_Lai_CMSIS-NN]] — optimized kernels for Cortex-M, 4.6x throughput and 4.9x energy efficiency over an unoptimized baseline.

[[2025_Abushahla_QuantizationMicrocontrollersSurvey]] — survey connecting quantization methods to microcontroller hardware/software platforms (including CMSIS-NN-class kernel libraries), useful as a reference for how CMSIS-NN sits relative to RISC-V and NPU-enabled alternatives.

[[2026_Jain_TinyFed6G]] — uses CMSIS-NN-class kernels as the on-device inference layer for Cortex-M devices participating in federated learning.

[[2025_Jung_TinyTransformersLowPowerMCUs]] — MCU-targeted attention-block kernel library and Fused-Weight Self-Attention scheduling, directly extending hand-optimized kernel coverage from convolution to lightweight transformer attention, benchmarked against CMSIS-NN.

## Open problems

Generalizing the "hand-optimized kernel" approach toward automatic generation via a compiler (see [[microTVM_TVM]]) without losing performance. Extension to more recent Cortex-M cores with Helium (MVE) vector instructions, not covered by the original paper.

## Research ideas

Extending the kernels for Cortex-M55/M85 with Helium instructions. Automatic kernel generation via a compiler for new network architectures (for example lightweight attention) not covered by the current library.

## Possible thesis topics

A comparative benchmark between CMSIS-NN and compiler-generated kernels (microTVM) on Cortex-M55/M85 with Helium instructions.

## Links

[[TensorFlow_Lite_Micro]], [[Cortex-M]], [[Quantization]]
