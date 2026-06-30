# High Performance Convolutional Neural Networks for Document Processing

**Full citation:** Chellapilla, K., Puri, S., Simard, P. (2006). High Performance Convolutional Neural Networks for Document Processing. *Tenth International Workshop on Frontiers in Handwriting Recognition (IWFHR 2006)*. https://hal.science/inria-00112631

**Linked concepts:** [[CMSIS-NN]]

## Abstract summary

The authors show that convolution operations in a CNN can be reformulated as a single large matrix-matrix multiplication (by unrolling overlapping input patches into matrix rows, the "im2col" technique) and executed through highly optimized general matrix multiplication (GEMM) routines, achieving substantially faster CNN inference and training than direct/naive convolution implementations on the hardware of the time.

## Research problem

Direct, naive implementations of convolution (nested loops over input positions, channels, and kernel offsets) were a major performance bottleneck for CNN-based document and character recognition systems, and did not take advantage of decades of optimization work already invested in dense linear algebra (BLAS/GEMM) libraries.

## Key idea

Convolution is mathematically equivalent to a matrix multiplication if the input is first transformed by extracting and stacking ("unrolling") each receptive-field patch as a row (or column) of a matrix; once in this form, the convolution can be computed with a single call to a highly optimized GEMM routine instead of a custom, typically much less efficient convolution loop.

## Technical contribution

A practical demonstration and implementation of the im2col-plus-GEMM reformulation for CNN convolution and its application to a real handwriting/document-processing pipeline; quantification of the speedup obtained over direct convolution on the CPU hardware available at the time.

## Experimental methodology

Implements both direct convolution and the GEMM-based (im2col) approach for the convolutional layers of CNNs used in character/document recognition, and benchmarks training and inference time on the hardware of the era, comparing throughput between the two implementation strategies.

## Results

The GEMM-based convolution implementation achieves significantly faster execution than direct convolution loops, by leveraging the much higher arithmetic efficiency of optimized dense matrix-multiplication libraries, making CNN training and inference practical at larger scale than was feasible with naive convolution code.

## Comparison with the state of the art

At the time, this was one of the first demonstrations that reformulating convolution as GEMM — rather than writing custom, hardware-specific convolution loops — could deliver large, "free" performance gains by piggybacking on existing optimized linear algebra infrastructure; the technique became, over the following decade, the default approach used by virtually all major deep learning frameworks for CPU/GPU convolution.

## Strengths

A simple, general, and highly portable optimization technique, since it leverages whatever optimized GEMM routine is already available on a given platform rather than requiring new low-level code for each new hardware target.

## Weaknesses

The im2col data-rearrangement step itself uses extra memory (the unrolled patch matrix is typically larger than the original input) and additional memory-bandwidth, a cost that becomes especially significant on memory-constrained microcontroller-class hardware.

## Limitations

Developed and evaluated on the CPU hardware and document/character-recognition workloads of 2006; does not address the memory-overhead concerns of im2col on today's memory-constrained microcontroller targets, where this overhead must be carefully managed or avoided.

## Open questions

How can the im2col memory overhead be minimized or avoided on extremely memory-constrained microcontroller hardware, where SRAM is scarce, while still benefiting from GEMM-style optimized inner loops?

## Possible extensions

Memory-efficient or "implicit" GEMM convolution variants that avoid materializing the full unrolled patch matrix, directly relevant to how libraries such as CMSIS-NN implement convolution within tight SRAM budgets on Cortex-M devices.

## Relevance to our research

The general technique that CMSIS-NN's GEMM-based convolution kernels for Cortex-M build on; essential background for understanding why CMSIS-NN's kernel design looks the way it does and where its memory-overhead trade-offs come from.

## Possible thesis topics

Quantifying the memory-versus-speed trade-off of im2col-based GEMM convolution against direct/implicit convolution on a Cortex-M target using CMSIS-NN, across a range of layer shapes typical of TinyML models.

## Possible collaborations

Groups working on memory-efficient convolution kernel design for microcontrollers and on GEMM library optimization for embedded CPUs.

## Links to related papers

[[2017_Howard_MobileNets]]
