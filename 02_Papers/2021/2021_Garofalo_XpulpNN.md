# XpulpNN: Enabling Energy Efficient and Flexible Inference of Quantized Neural Networks on RISC-V Based IoT End Nodes

**Full citation:** Garofalo, A., Tagliavini, G., Conti, F., Benini, L., Rossi, D. (2021). XpulpNN: Enabling Energy Efficient and Flexible Inference of Quantized Neural Networks on RISC-V Based IoT End Nodes. IEEE Transactions on Emerging Topics in Computing, 9(3), 1489-1505.

**PDF:** [ResearchGate](https://www.researchgate.net/publication/350935283_XpulpNN_Enabling_Energy_Efficient_and_Flexible_Inference_of_Quantized_Neural_Networks_on_RISC-V_based_IoT_End_Nodes)

**Linked concepts:** [[RISC-V]]

## Abstract summary

Extends the RISC-V ISA with nibble (4-bit) and crumb (2-bit) SIMD instructions plus a custom fused dot-product/load execution paradigm, integrated at the microarchitectural level, to accelerate heavily quantized neural network inference on RISC-V microcontroller-class cores.

## Research problem

Heavily quantized (sub-8-bit) neural network inference needs ISA-level support to realize its theoretical speedup; without it, sub-byte precision gains are lost to inefficient bit-manipulation overhead on generic RISC-V cores.

## Key idea

Extend the RISC-V ISA itself with SIMD instructions specifically for 4-bit and 2-bit precision, plus fuse the dot-product and load operation into one instruction to reduce memory-access overhead for QNN sum-of-products computation.

## Technical contribution

A multi-precision arithmetic unit integrated at both the microarchitectural and ISA level; near-linear speedup for sub-byte precision versus higher-precision integer computation on key QNN kernels; up to 1.64x peak MAC/cycle improvement from the fused dot-product/load execution paradigm.

## Experimental methodology

Implemented and evaluated on a RISC-V microcontroller-class core, measuring speedup and energy efficiency for QNN inference kernels at 2-bit and 4-bit precision versus standard integer execution.

## Results

Near-linear speedup with reduced precision (not the sub-linear returns typical of software-only sub-byte quantization); up to 1.64x peak MAC/cycle improvement from the fused execution paradigm.

## Comparison with the state of the art

Directly answers this concept's own open question about RISC-V toolchain/ISA maturity for deploying quantized models, extending the GAP-8/Spatz lineage already tracked (same Bologna research group) from fixed-function/vector-extension accelerators to ISA-level sub-byte quantization support specifically.

## Strengths

Well-cited (80+) for a specialized ISA-extension paper; near-linear (not sub-linear) speedup scaling is a genuinely strong result; directly from the same research lineage as this concept's GAP-8/Spatz anchors, showing a coherent Bologna-group research program.

## Weaknesses

ISA extension requires custom silicon (not available on off-the-shelf RISC-V cores), limiting immediate practical deployment versus software-only quantization approaches.

## Limitations

Evaluated on the group's own PULP-family silicon; generalization to other RISC-V implementations not demonstrated.

## Open questions

How does XpulpNN's ISA-level sub-byte SIMD support compare directly to Cortex-M's Helium (MVE) vector extension for the same quantized workload, addressing this concept's and [[Cortex-M]]'s shared open question about cross-ISA quantization efficiency?

## Possible extensions

A head-to-head energy-per-inference comparison of XpulpNN's ISA extension against Cortex-M55/M85's Helium MVE for the same sub-8-bit quantized model.

## Relevance to our research

Directly closes this concept's own named open problem about RISC-V toolchain/ISA maturity for quantized-model deployment, extending the same research lineage (GAP-8, Spatz) already anchoring this concept.

## Possible thesis topics

Cross-ISA energy-per-inference benchmark: XpulpNN's RISC-V sub-byte SIMD extension versus Cortex-M55/M85 Helium MVE for the same quantized model.

## Possible collaborations

University of Bologna / ETH Zürich (Benini, Rossi, Conti group) — the same lineage behind GAP-8 and Spatz.

## Links to related papers

[[2018_Flamand_GAP8]], [[2023_Perotti_Spatz]], [[2018_Lai_CMSIS-NN]]
