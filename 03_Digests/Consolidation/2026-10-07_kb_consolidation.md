# Knowledge Base Consolidation — 2026-10-07

## Scope Reviewed

Second consolidation cycle, covering evidence accumulated since 2026-09-02: the weekly digests of 2026-09-06 through 2026-10-05, the September monthly report, the eight candidates in the active queue (four `ready_for_review`, four `watching`), the closed-candidate history, the taxonomy, and the concept pages touched by the queue (NPU, MLPerf Tiny, On-device Learning, Quantization, MoE Edge LLM Serving) plus the existing paper records for Hydra, the Apple Neural Engine study and FALCON.

Primary-source verification was the binding constraint of this cycle. Of the arXiv and DOI sources needed for the candidates, only arXiv:2609.16085 (the INT8-portability study) returned readable text. The PDFs of MEGATRON, PreDE, FoldQuantVLA, EdgeDAE, NPLSD, LiSenNet, the 16-bit MCU paper and the RiP-convolution paper returned no machine-readable text, one request was rate-limited (HTTP 429, instructing not to refetch), and the DOI page of the memristor SoC (Song et al.) was rate-limited too. Following the rule that persistent knowledge may not be written from digest summaries alone, the cycle therefore resolved only what could be verified.

## Main Signals

Across the queue, one idea recurs from several directions: on this class of hardware, deployability and cost are properties of the runtime, compiler and vendor toolchain rather than of bit width, MAC count or bare-metal benchmark scores. The verified INT8-portability study gives that idea its cleanest quantified form (speedup sign set by the CPU's dot-product ISA, output divergence across integer kernels, a vendor NPU that silently ignores external quantization scales). The restricted-operator-set, pre-deployment-prediction and on-device-training candidates are further faces of the same signal, but their anchors could not be verified this cycle.

## Existing Concepts Updated

[[MLPerf_Tiny]] — added a "Benchmark realism and measurement methodology" passage to its Evolution of the concept section, a Key papers entry, an open problem (what an open MCU-tier harness must capture), and research and thesis ideas. What changed: the page previously described MLPerf Tiny only as a standard; it now records that standard-workload scores do not predict behaviour across targets and that no open measurement harness exists at the Cortex-M / Ethos-U / RISC-V-NPU tier. Evidence: [[2026_Shin_INT8Portability]] (verified from the arXiv PDF), with [[2026_Taherin_Hydra]] and [[2026_Bryngelson_AppleNeuralEngine]] already recorded. The page states explicitly that claims from other preprints (bare-metal numbers not transferring to a real wearable, runtime effects invisible to bit-width proxies on MCUs) were not verified and are kept in the queue instead of being stated as fact.

[[MoE_Edge_LLM_Serving]] — one sentence repointed from the removed "known gap" to the MLPerf Tiny discussion; no technical content changed.

## New Concepts Added

None. The two candidates that most clearly met the two-independent-anchor convention (in-memory computing with emerging non-volatile memory; robotics applications of EdgeAI) rest on sources that could not be read this run, so creating them would have meant writing hardware and application claims from digest summaries.

## Paper Analyses Added or Updated

Added [[2026_Shin_INT8Portability]] (arXiv:2609.16085): the anchor for the MLPerf Tiny extension, verified against the arXiv PDF, with its limitation (no Cortex-M, Ethos-U or RISC-V-NPU target) recorded. No other paper warranted a persistent record this cycle. Hydra, the Apple Neural Engine study and FALCON were left unchanged; FALCON's record is still abstract-level and flags itself for a full-PDF pass.

## Candidates Kept Under Observation

Kept at `ready_for_review` (reviewed, not promoted; reason: primary sources could not be verified, not lack of merit):

- In-memory computing with emerging non-volatile memory. Three unrelated anchors are claimed (FALCON/MTJ, a 65 nm memristor SoC, MEGATRON/PCM). Re-verify MEGATRON and the Song et al. DOI before creating a Hardware concept; the narrow "emerging NVM" scope remains the safer first step, and the certified-selective-inference candidate may then fold into its open problems.
- Robotics / autonomous-systems applications. Five unrelated groups over four weeks; the open scope question (custom accelerator versus FPGA-GPU versus Jetson-class onboard compute) still has to be decided, with Jetson-class as the likely centre of gravity.
- Restricted operator sets on MCU-class NPUs. The strongest-evidenced candidate in the queue (five or more unrelated groups, three accelerator families, inference and training); the preferred outcome remains an operator-set and static-graph section in [[NPU]], decided together with the already-merged measurement material.

Kept at `watching`: edge-GPU / Jetson-class hardware (one characterization paper; deployment density is high but the characterization bar is unmet), certified selective inference for imperfect accelerators (one paper), pre-deployment prediction of quantization degradation (likely a Quantization subsection; needs an MCU/NPU-validated predictor or a second peer-reviewed positive result), and resource-accounted on-device training on MCUs (most anchors are snippet-level; likely an On-device Learning extension).

These are observed trends, not persistent knowledge: none of them was written into a concept page.

## Candidates Rejected

None.

## Knowledge Graph Changes

[[MLPerf_Tiny]] now links to [[NPU]] and [[ONNX_Runtime]] and cites [[2026_Shin_INT8Portability]], which links to [[Quantization]], [[NPU]], [[ONNX_Runtime]], [[Cortex-A]], [[2026_Taherin_Hydra]] and [[2026_Bryngelson_AppleNeuralEngine]]. This connects the Benchmarks & Datasets branch to the Hardware and Frameworks branches for the first time through a measurement-methodology relationship (benchmark → evaluated systems and toolchains). The taxonomy's Known gaps list was reduced from eight to seven entries to mirror the queue; the measurement gap survives as an open problem on the MLPerf Tiny page.

Consistency review: the NPU page's FALCON entry still says FALCON anchors "the in-memory-computing entry in the taxonomy's known gaps", which remains accurate. No duplicate concepts, contradictory descriptions or broken wikilinks were found in the pages touched; a full-repository link check was left to tools/check_consistency.py.

## Emerging Research Questions

Does the output divergence the INT8-portability study measures on CPUs and vendor NPUs also appear between CMSIS-NN kernels and Arm Ethos-U on the same quantized model, and does it matter for task metrics beyond top-1 agreement? Is a silent failure mode (a compiler that accepts a graph and ignores its quantization scales) specific to one vendor, or common on MCU-class NPU toolchains?

## Potential Thesis and Research Opportunities

An MCU-tier replication of the fixed-artifact INT8-portability protocol on MLPerf Tiny workloads across Cortex-M (CMSIS-NN), Ethos-U and a RISC-V NPU, released as an open harness (Master's; closes the gap named on [[MLPerf_Tiny]]).

A measurement study of output agreement across integer kernels on microcontroller targets, testing whether top-1 preservation hides divergence relevant to safety-critical use (Master's/PhD; bridges [[Quantization]] and [[MLPerf_Tiny]]).

Primary-source verification of the three review-ready candidates, ahead of the next cycle (MEGATRON and the memristor SoC for in-memory computing; PreDE, FoldQuantVLA and EdgeDAE for robotics; NPLSD and LiSenNet for operator sets), as a precondition for promoting each.
