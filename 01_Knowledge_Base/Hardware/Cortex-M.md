# Cortex-M

## Evolution of the concept

Cortex-M cores (Arm) are the most widely used hardware target for TinyML: low-power microcontrollers, with no dedicated hardware for neural computation, with only a few tens/hundreds of KB of RAM. The entire software ecosystem for this target developed in response to these constraints: CMSIS-NN for optimized kernels, TensorFlow Lite Micro as a runtime with static memory allocation.

## Key papers

[[2018_Lai_CMSIS-NN]] — kernels optimized for Cortex-M's SIMD instructions.

[[2021_David_TensorFlowLiteMicro]] — an inference runtime designed for the memory constraints of these cores.

## Open problems

Exploiting the new Helium (MVE) vector instructions on Cortex-M55/M85, still poorly covered in the literature. Efficient support for architectures other than classic CNNs (e.g. lightweight attention).

## Research ideas

Study of the real efficiency of depthwise-separable convolutions (MobileNet) on Cortex-M with CMSIS-NN; evaluation of how well quantization gains transfer to these cores compared to RISC-V without dedicated SIMD support.

## Possible thesis topics

Benchmarking new architectures (NAS-derived, distilled) on real Cortex-M hardware, comparing CMSIS-NN and microTVM as backends.

## Links

[[CMSIS-NN]], [[TensorFlow Lite Micro]], [[microTVM_TVM]]
