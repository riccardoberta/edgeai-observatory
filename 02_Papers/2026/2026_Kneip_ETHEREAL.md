# ETHEREAL: A 25.6-μs/inf. Low-latency Event-driven Graph-neural-network Processor for High-resolution Vision at the Edge

**Full citation:** Kneip, A., Lefebvre, M., Gehrig, D., Catalán Pastor, V., Scaramuzza, D., Verhelst, M., Frenkel, C. (2026). ETHEREAL: A 25.6-μs/inf. Low-latency Event-driven Graph-neural-network Processor for High-resolution Vision at the Edge. arXiv:2608.17787 [cs.AR, cs.CV]. Delft University of Technology; KU Leuven; University of Zurich (Robotics and Perception Group); University of Pennsylvania. Submitted 18 Aug 2026 (v1). Submitted to IEEE Journal of Solid-State Circuits (JSSC). DOI: 10.48550/arXiv.2608.17787.

**Linked concepts:** [[Vision]], [[Quantization]] (runtime-reconfigurable 4b/8b precision) — no clean match in the Hardware branch (Cortex-M/A, RISC-V, DSP, FPGA, NPU); this is a custom digital ASIC, flagged as a taxonomy gap below.

## Abstract summary

Dynamic vision sensors (DVS) offer μs-level temporal resolution suited to sub-ms edge-vision latency targets, but exploiting them requires hardware that can jointly handle dense-regular compute and sparse-irregular memory access. The paper introduces ETHEREAL, the first event-driven graph-neural-network (EV-GNN) processor chip, combining a neighbor-parallel spline-convolution engine with a split 2D/3D memory hierarchy and a novel spatiotemporal event-caching mechanism. Measured on fabricated silicon, it reaches 25.6μs latency and 1.6μJ energy per end-to-end event-wise inference on the DAGr-GNN workload and the VGA-resolution (640×480) DSEC automotive dataset.

## Research problem

DVS event cameras generate events with ~1μs temporal resolution, well matched to the sub-ms latency needs of safety-critical edge vision (autonomous driving, drone navigation, XR). Event-driven graph neural networks (EV-GNNs) are the algorithmic approach that best exploits this — training on 3D-aggregated graph data for accuracy, then processing the event stream asynchronously via local message passing at inference time. But no dedicated hardware existed that could support EV-GNNs' mixed requirements: dense-regular compute for message-passing MACs, and sparse-irregular memory access for the event graph. Existing FPGA-based EV-GNN accelerators are limited to toy resolutions (≤128×128 pixels) and cannot scale to real-world, high-resolution workloads (≥640×480).

## Key idea

Two co-designed innovations close the gap. First, a spline-iterative reformulation of graph convolution: by swapping the order of the two MAC operations in the standard spline-convolution formulation, each large 2D weight tensor is fetched from memory only once per valid spline index and consumed in parallel by all neighbors that need it ("neighbor-level parallelism"), reducing the number of high-precision MACs by a factor of IC/(D+1)² (input channels over squared spline-basis size) versus a naive per-neighbor formulation. Second, a split 2D/3D spatiotemporal memory hierarchy with a dedicated event-caching mechanism that stores recent graph-node state efficiently across both purely spatial (2D) and spatiotemporal (3D) network layers.

## Technical contribution

(1) The first EV-GNN processor chip (measured silicon, not FPGA emulation or simulation); (2) a neighbor-parallel spline-convolution dataflow with eight reconfigurable dual-mode message-passing cores, giving up to 3.8× speedup over a neighbor-serial baseline at fixed memory bandwidth; (3) a "spline-skipping" mechanism that preserves performance at low neighbor counts by identifying and skipping unused spline indices via configuration LUTs; (4) reconfigurable processing elements supporting both 4b and 8b input/weight precision, switchable per layer at runtime, adding under 30% area overhead versus a fixed-precision baseline MAC array; (5) a split 2D/3D spatiotemporal cache memory architecture purpose-built for EV-GNN graph-data access patterns.

## Experimental methodology

Measured on fabricated silicon (process node not confirmed in the abstract-level and partial full-text material read in this pass; to verify from the full PDF's implementation section). Evaluated on the state-of-the-art DAGr-GNN network and the VGA-resolution (640×480 pixel) DSEC automotive event-vision dataset. Internal dataflow comparisons (neighbor-parallel vs. neighbor-serial; area overhead of dual-precision support) were run at the architecture/RTL level against the chip's own fixed-precision/serial baselines.

## Results

25.6μs latency and 1.6μJ energy per end-to-end event-wise inference on DAGr-GNN/DSEC — a first-in-class demonstration at this resolution. The neighbor-parallel dataflow improves total graph-convolution execution time by up to 3.8× on average versus a neighbor-serial approach at fixed weight-memory (WMEM, 512kB) bandwidth. The dual-mode reconfigurable MAC array (4×64 processing elements per core, 8 cores) adds under 30% area overhead versus a fixed-precision baseline while enabling per-layer 4b/8b precision switching.

## Comparison with the state of the art

Prior EV-GNN accelerators are FPGA-based and limited to toy, low-resolution (≤128×128 pixel) setups; ETHEREAL is presented as the first design to scale to high-resolution (≥640×480) EV-GNN workloads, and the first ASIC implementation with measured (rather than emulated) results. A Google Scholar cross-check run for the 2026-08-23 weekly digest independently surfaced a contemporaneous FPGA-based event-driven GNN accelerator for edge vision (T. Liu et al., ~April 2026, 1 citation at the time) as related prior art — meaning ETHEREAL is not the first attempt at EV-GNN hardware altogether, but its combination of high resolution and real silicon measurement appears to be a genuinely stronger reproducibility and efficiency claim than that prior work. A direct, matched-condition comparison against T. Liu et al. was not found in the abstract-level/partial full-text material gathered here.

## Strengths

First measured-silicon (not simulated or FPGA-emulated) EV-GNN processor; scales to real-world VGA resolution versus prior toy-scale (≤128×128) demonstrations; genuine algorithm-hardware co-design (the spline-iterative MAC reformulation is purpose-built for, and only pays off because of, the matched dual-mode core architecture) rather than a generic accelerator retrofitted to the workload; the reconfigurable 4b/8b precision exploits EV-GNNs' documented low sensitivity to 4-bit quantization, turning an algorithmic property into a real efficiency gain; the author team spans digital-circuits/hardware expertise (Verhelst, Frenkel) and event-vision/robotics expertise (Scaramuzza, Gehrig), strengthening both the hardware rigor and the algorithmic grounding; targeting IEEE JSSC, a top solid-state-circuits venue, signals a mature, thoroughly reviewed silicon result.

## Weaknesses

Evaluated on a single workload/dataset pairing (DAGr-GNN on DSEC) — no reported results on other EV-GNN architectures or other event-vision tasks/datasets (e.g., gesture recognition, other automotive benchmarks), so generality across the EV-GNN algorithm family is unverified; no quantitative comparison against non-GNN event-vision baselines (SNN accelerators, frame-based CNN accelerators) is evident from the material read, only against the chip's own internal ablations; process node, full die photo/area breakdown, and power-supply details beyond core voltage were not confirmed in this pass — full-PDF verification needed before citing in a survey.

## Limitations

The architecture uses 8 fixed message-passing cores, so the maximum exploitable neighbor-level parallelism is architecturally capped; workloads whose typical neighborhoods are much larger than what DSEC/DAGr-GNN exercise may see diminishing returns from the neighbor-parallel scheme. The MAC-reduction factor IC/(D+1)² depends on the spline degree D and kernel size chosen by the EV-GNN architecture, so the chip's efficiency gains are somewhat co-designed with — and possibly specific to — spline-convolution-style EV-GNNs like DAGr-GNN, rather than generic graph message-passing schemes.

## Open questions

Does the neighbor-parallel spline-convolution engine and spatiotemporal event-caching mechanism transfer to other genuinely sparse, irregular, asynchronous event streams beyond DVS vision — e.g., biosignal spike trains or sparse radar point clouds (explicitly flagged as a thesis hook in the 2026-08-23 weekly digest)? How does efficiency scale with denser event streams or different neighborhood-density regimes than DSEC exercises? What is the accuracy-vs-precision trade-off of the 4b mode across a wider variety of EV-GNN backbones and tasks, beyond the single DAGr-GNN/DSEC pairing reported?

## Possible extensions

Apply the split 2D/3D spatiotemporal event-caching mechanism to other sparse asynchronous sensing modalities ([[Biosignals]] spike trains, sparse radar point clouds); run a direct, matched-condition efficiency comparison against the T. Liu et al. FPGA-based EV-GNN accelerator to quantify the ASIC-vs-FPGA gap; extend the dual-mode 4b/8b MAC array with sub-4-bit (ternary/binary) modes given EV-GNNs' demonstrated quantization tolerance.

## Relevance to our research

Directly extends the Observatory's [[Vision]] branch with a new, silicon-validated hardware class (EV-GNN processors) at the intersection of neuromorphic sensing and graph neural computation — a corner not previously represented in `02_Papers/`. Also touches [[Quantization]] via its runtime-reconfigurable 4b/8b precision. Notably, ETHEREAL does not map cleanly onto any existing Hardware-branch node (Cortex-M, Cortex-A, RISC-V, DSP, FPGA, NPU) — it is a custom digital ASIC for a specific sensing/algorithm pairing, which is worth considering alongside the MoE and Edge-AI-Security taxonomy gaps already flagged in recent digests (see the taxonomy Evolution note added 2026-08-25).

## Possible thesis topics

Hardware-in-the-loop transfer of ETHEREAL's neighbor-parallel spline-convolution and spatiotemporal caching architecture to a non-vision sparse event stream — e.g., neuromorphic biosignal spike-train classification (PhD-scale; bridges [[Vision]] and [[Biosignals]]). A matched-condition comparative efficiency study against FPGA-based EV-GNN accelerators (T. Liu et al.) to quantify the ASIC-vs-FPGA trade-off for this workload class (Master's/PhD). Extending the reconfigurable-precision scheme toward sub-4-bit EV-GNN inference and characterizing the resulting accuracy cliff (Master's; [[Quantization]]).

## Possible collaborations

The ETHEREAL author team directly: TU Delft / KU Leuven digital-circuits groups (Verhelst, Frenkel), the UZH Robotics and Perception Group (Scaramuzza), and event-vision expertise (Gehrig) — a natural fit for any lab work involving event cameras or GNN accelerators. Groups pursuing FPGA-based EV-GNN work (e.g., T. Liu et al.) for a head-to-head ASIC-vs-FPGA comparison study.

## Links to related papers

None yet in `02_Papers/` on graph neural networks or event-based vision — this is the Observatory's first deep-analysis record touching event-driven sensing hardware. A future record on the T. Liu et al. FPGA-based EV-GNN accelerator (~April 2026), surfaced via the 2026-08-23 digest's Google Scholar cross-check, would make a natural companion/comparison entry.
