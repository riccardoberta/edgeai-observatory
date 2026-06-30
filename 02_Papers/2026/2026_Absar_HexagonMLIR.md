# Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs)

**Full citation:** Absar, M.J., Baskaran, M., Sharma, A., Bhandari, A., Aggarwal, A., Rangasamy, A., Das, D., Hosseini, F., Slama, F., Brumar, I., Verma, J., Bindumadhavan, K., Kothari, M., Gupta, M., Kolachana, R., Lethin, R., Narang, S., Ladwa, S.M., Jain, S., Dalvi, S.S., Rahman, T., Komatireddy, V.R.R., Pandya, V.V., Shi, X., Zipper, Z. (2026). Hexagon-MLIR: An AI Compilation Stack For Qualcomm's Neural Processing Units (NPUs). arXiv:2602.19762. https://arxiv.org/abs/2602.19762

**Linked concepts:** [[MLIR]], [[NPU]]

## Abstract summary

The authors (Qualcomm) present Hexagon-MLIR, an open-source AI compilation stack built on the MLIR framework that provides unified support for lowering Triton kernels and PyTorch models to Qualcomm's Hexagon Neural Processing Units, with compiler passes designed to exploit NPU-specific architectural features.

## Research problem

Deploying models written in modern ML programming abstractions (Triton kernels, PyTorch graphs) onto vendor-specific NPU hardware like Qualcomm's Hexagon requires a compilation path that can both interface with these increasingly standard front-end abstractions and exploit the NPU's specific architectural features, a gap that vendor-specific, non-MLIR-based toolchains historically had to address with custom, less reusable infrastructure.

## Key idea

Build the NPU-targeting compilation stack directly on MLIR's extensible infrastructure, defining custom dialects and lowering passes that translate from standard front-end representations (Triton, PyTorch) down to Hexagon NPU-specific code, reusing MLIR's general compiler infrastructure rather than building a fully bespoke toolchain.

## Technical contribution

The Hexagon-MLIR compilation stack itself, including its MLIR dialects and lowering passes for Triton-kernel and PyTorch-model ingestion; documented compiler passes that exploit Hexagon NPU-specific architectural features for performance.

## Experimental methodology

Description and evaluation of the compilation stack's ability to lower representative Triton kernels and PyTorch models to functioning, NPU-executing code, with discussion of the architecture-specific optimization passes and their role in the overall toolchain (evaluation methodology and benchmark results to be assessed against the published paper as the field's reception develops, given the very recent publication date).

## Results

The paper demonstrates a working, open-source MLIR-based compilation path from standard ML front-ends (Triton, PyTorch) to Qualcomm Hexagon NPU hardware, establishing MLIR as a viable, reusable infrastructure choice for vendor-specific NPU compilation rather than requiring fully bespoke toolchains.

## Comparison with the state of the art

Distinguishes itself from earlier, more bespoke vendor-specific NPU toolchains by building on MLIR's general, reusable compiler infrastructure, aligning Qualcomm's NPU compilation path with the broader industry trend (also seen in TVM/microTVM and other MLIR-based projects) toward shared compiler infrastructure across hardware vendors.

## Strengths

Open-source; built on widely-adopted standard front-end abstractions (Triton, PyTorch) rather than a proprietary input format; backed by a large, dedicated engineering team at a major NPU vendor.

## Weaknesses

As a very recently published industry paper (February 2026), independent third-party evaluation and community adoption track record are not yet available at the time of this record's writing.

## Limitations

Specific to Qualcomm's Hexagon NPU architecture; generalization of the specific lowering passes to other NPU vendors' hardware is not addressed, though the underlying MLIR-based methodology is in principle portable.

## Open questions

How does Hexagon-MLIR's performance compare to Qualcomm's prior, non-MLIR-based NPU toolchains on the same models? Will other NPU vendors converge on similar MLIR-based compilation stacks, and if so, does this create a more unified cross-vendor NPU deployment path for EdgeAI?

## Possible extensions

A cross-vendor comparison of MLIR-based NPU compilation stacks (Hexagon-MLIR and any analogous efforts from other NPU vendors) for the same model and task, assessing how much cross-vendor portability the shared MLIR foundation actually delivers in practice.

## Relevance to our research

Directly relevant to both [[MLIR]] (as a concrete, large-scale industrial application of the MLIR compiler infrastructure) and [[NPU]] (as a current, vendor-specific NPU compilation case study), worth revisiting as community evaluation accumulates.

## Possible thesis topics

A practical evaluation of deploying a representative EdgeAI model (vision or audio) through the Hexagon-MLIR stack onto real Qualcomm NPU hardware, measuring latency/energy against a CPU or Cortex-M baseline.

## Possible collaborations

Groups working on MLIR-based compiler infrastructure and on NPU-vendor-specific deployment toolchains.

## Links to related papers

[[2023_Das_MLDrivenHardwareCostModelMLIR]], [[2014_Chen_DianNao]]
