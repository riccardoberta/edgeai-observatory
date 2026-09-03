# Optimizing the Deployment of Tiny Transformers on Low-Power MCUs

**Full citation:** Jung, V.J.B., Burrello, A., Scherer, M., Conti, F., Benini, L. (2025). Optimizing the Deployment of Tiny Transformers on Low-Power MCUs. IEEE Transactions on Computers, 74(2). Earlier preprint: arXiv:2404.02945 (2024)

**PDF:** [arXiv](https://arxiv.org/abs/2404.02945)

**Linked concepts:** [[CMSIS-NN]]

## Abstract summary

A complete framework for deploying encoder Tiny Transformers on single- and multi-core commercial MCUs, including an optimized attention-block kernel library and a novel Fused-Weight Self-Attention inference schedule that fuses linear-projection weights offline, reducing operations and parameters.

## Research problem

Transformer attention blocks involve data-movement and operator patterns (softmax, multi-head reshaping) that hand-optimized kernel libraries like CMSIS-NN — designed around convolution/GEMM patterns — do not handle efficiently on MCU-class hardware.

## Key idea

Build an MCU-targeted kernel library specifically optimized for the attention block's data-reuse and marshaling patterns, and reduce the attention computation itself via offline weight fusion (Fused-Weight Self-Attention).

## Technical contribution

An end-to-end Tiny-Transformer deployment framework for MCUs, including attention-specific kernels reported to feature higher data reuse than CMSIS-NN's general-purpose kernels, plus the Fused-Weight Self-Attention scheduling technique.

## Experimental methodology

Deployment and benchmarking on single- and multi-core MCUs (including GAP9), comparing against CMSIS-NN-based baseline kernels for transformer attention operations.

## Results

Higher data reuse and reduced operation/parameter count versus CMSIS-NN-based attention kernels, enabling practical Tiny Transformer deployment on MCU-class hardware.

## Comparison with the state of the art

Directly addresses this concept's own open problem about generalizing beyond hand-optimized convolution kernels toward newer architectures (lightweight attention) "not covered by the current library" — this paper is exactly that extension, evaluated head-to-head against CMSIS-NN.

## Strengths

Directly benchmarked against CMSIS-NN on real MCU hardware; addresses a genuine architectural gap (attention, not just convolution) in the existing kernel library ecosystem; well-cited (45+) for a specialized systems paper.

## Weaknesses

Attention-specific; does not replace CMSIS-NN's broader convolution/GEMM kernel coverage, so practical deployment likely needs both libraries together.

## Limitations

Validated primarily on PULP/GAP9-class multi-core MCUs rather than the single-core Cortex-M devices CMSIS-NN itself primarily targets.

## Open questions

Does the Fused-Weight Self-Attention technique's benefit transfer to genuinely single-core Cortex-M devices with Helium/MVE, or is it specific to the multi-core PULP architecture evaluated?

## Possible extensions

Porting and re-benchmarking the Fused-Weight Self-Attention kernels on Cortex-M55/M85 with Helium (MVE) vector instructions, directly extending this concept's own Helium-extension research idea to transformer workloads.

## Relevance to our research

Directly closes this concept's own explicitly-named open problem: extending hand-optimized MCU kernels beyond convolution toward lightweight attention architectures.

## Possible thesis topics

Porting this paper's Fused-Weight Self-Attention kernels to Cortex-M55/M85 Helium and benchmarking against both the original PULP results and standard CMSIS-NN convolution kernels.

## Possible collaborations

ETH Zürich / University of Bologna (Benini group), working on PULP-platform and transformer deployment for constrained hardware.

## Links to related papers

[[2018_Lai_CMSIS-NN]], [[2025_Zeng_TinyNeXt]]
