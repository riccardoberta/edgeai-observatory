# HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference

**Full citation:** Jun, G. H., Pang, W., Richter, E., Saeedi, M., Amarnath, A., Ferrao, P., Chen, D. (2026). HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference. arXiv:2607.12839 [cs.DC, cs.AR]. Submitted 14 Jul 2026; revised through v3, 16 Jul 2026. Accepted at the 59th IEEE/ACM International Symposium on Microarchitecture (MICRO 2026). License CC BY 4.0. DOI: 10.48550/arXiv.2607.12839.

**Linked concepts:** [[NPU]]; also the core exemplar of [[Mixture-of-Experts (MoE) & Edge LLM Serving]] — HeteroMosaic is a scheduling/serving system, not an MoE-specific technique, but its heterogeneous-scheduling problem is shared with the cluster's MoE-memory papers.

## Abstract summary

Modern edge SoCs combine CPUs, integrated GPUs (iGPUs), and NPUs, but existing LLM runtimes make coarse device-level decisions or optimize operators in isolation, underutilizing heterogeneous resources — particularly on unified-memory platforms where performance depends on both device placement and task-graph coordination. HeteroMosaic is a heterogeneity-first scheduling framework: it uses a heterogeneous roofline model to identify when combining iGPU and NPU execution is beneficial, decomposes inference into dependency-preserving micro-batches exposing cross-accelerator overlap, and applies trace-guided co-optimization of scheduling and device allocation under practical effects (memory contention, DVFS, device variation, NPU runtime overheads). Implemented in PyTorch C++ and evaluated on three AMD Ryzen AI platforms (NPU-heavy, balanced, iGPU-heavy), it achieves up to 1.73× speedup over an iGPU baseline, 1.78× over an NPU baseline, and 2.05× over frameworks such as llama.cpp on the balanced platform, reducing energy by up to 45.3%, and up to 2.35× over prior heterogeneous edge-AI solutions.

## Research problem

Edge SoCs increasingly bundle CPU + iGPU + NPU on unified memory, but LLM serving runtimes treat this heterogeneity poorly: they make coarse, device-level placement decisions (run everything on the NPU, or everything on the iGPU) or optimize individual operators in isolation, rather than reasoning about the whole task graph's cross-accelerator opportunities. On unified-memory platforms specifically, performance depends jointly on device placement *and* task-graph coordination — a problem existing runtimes are not built to solve. The 2026-07-13 digest's "Is Your NPU Ready for LLMs?" measurement study had already shown concretely where the resulting waste comes from (a prefill/decode phase mismatch with NPU/CPU hardware preferences); HeteroMosaic is the constructive response.

## Key idea

Gate heterogeneous co-execution decisions with a heterogeneous roofline model — combining iGPU and NPU execution only when the model predicts it will actually help, rather than always splitting work — then expose the cross-accelerator overlap opportunity by decomposing inference into dependency-preserving micro-batches, and finally apply trace-guided co-optimization of scheduling and device allocation that accounts for real-world effects (memory contention, DVFS, device-to-device variation, NPU runtime wake-up overheads) that a purely analytical model would miss.

## Technical contribution

A heterogeneous roofline model specifically for gating iGPU+NPU co-execution decisions (not just characterizing peak performance); a dependency-preserving micro-batching decomposition that exposes cross-accelerator overlap without breaking the task graph's correctness constraints; trace-guided co-optimization of scheduling and device allocation that explicitly models memory contention, DVFS, device variation, and NPU runtime overheads; a full implementation in PyTorch C++ evaluated on real, diverse hardware (three AMD Ryzen AI platform configurations) rather than only simulation.

## Experimental methodology

Implemented in PyTorch C++, evaluated on three AMD Ryzen AI platforms spanning NPU-heavy, balanced, and iGPU-heavy hardware designs — testing whether the scheduling framework generalizes across different heterogeneous resource balances rather than only one fixed configuration. Compared against an iGPU-only baseline, an NPU-only baseline, llama.cpp, and prior heterogeneous edge-AI scheduling solutions.

## Results

On the balanced platform: up to 1.73× speedup over the iGPU baseline, 1.78× over the NPU baseline, and 2.05× over frameworks such as llama.cpp, with up to 45.3% energy reduction. Up to 2.35× improvement over prior heterogeneous edge-AI solutions specifically — meaning HeteroMosaic's advantage holds not just against single-device baselines but against other systems that already attempt heterogeneous scheduling.

## Comparison with the state of the art

Directly benchmarked against both single-device baselines (iGPU-only, NPU-only, llama.cpp) and prior heterogeneous edge-AI scheduling solutions (2.35× improvement over these specifically) — a genuinely comprehensive comparison set rather than only a self-ablation. Heterogeneous scheduling itself is not new; the contribution is the specific combination of a roofline-gated co-execution decision, dependency-preserving micro-batching, and trace-guided allocation modeling real hardware effects (DVFS, contention, NPU wake latency) that prior heterogeneous solutions did not jointly address.

## Strengths

Evaluated on three different hardware balance points (NPU-heavy, balanced, iGPU-heavy), directly testing generalization rather than reporting a single favorable configuration; models real-world scheduling effects (memory contention, DVFS, device variation, NPU wake-up overhead) rather than only an idealized analytical roofline, which is exactly the kind of gap that makes theoretically sound scheduling frameworks fail in practice; MICRO 2026 acceptance signals rigorous peer review at a top computer-architecture venue; the pairing with the prior week's NPU-measurement paper ("diagnose → schedule") gives HeteroMosaic's design choices a directly traceable empirical motivation rather than an assumed one.

## Weaknesses

Evaluated exclusively on AMD Ryzen AI platforms — application-class edge SoC hardware, not MCU/NPU-class embedded targets, so despite "edge LLM inference" framing this sits well above this Observatory's typical hardware focus; the roofline-gating decision and trace-guided co-optimization likely require offline profiling/trace collection specific to each hardware platform, and the abstract does not specify how much per-platform tuning is needed to reach the reported gains on a new device.

## Limitations

As with FreeToken and PolyQ, HeteroMosaic's demonstrated hardware class (Ryzen AI SoCs with iGPU+NPU) sits above the Cortex-M/RISC-V tier this lab's work typically targets — the roofline-gating and micro-batching ideas are conceptually portable, but the specific implementation is built around PyTorch C++ on application-class silicon.

## Open questions

How much of HeteroMosaic's 45% energy saving is recoverable in an open runtime (microTVM, ONNX Runtime) rather than the paper's PyTorch C++ implementation, per the 2026-07-19 digest's explicit hook? Does the roofline-gating approach generalize to non-Ryzen heterogeneous edge hardware (e.g., Jetson-class or a RISC-V+NPU platform), and if so, how much re-profiling is required per new device?

## Possible extensions

Reproduce HeteroMosaic's iGPU+NPU co-execution on non-Ryzen edge hardware (Jetson, or a RISC-V + NPU platform) and quantify how much of the 45% energy saving is recoverable in an open runtime such as ONNX Runtime or microTVM (the explicit 2026-07-19 digest hook); characterize the per-platform profiling/tuning cost needed to reach the reported gains on a genuinely new hardware target, as a practical adoption-cost study.

## Relevance to our research

Strong reference/methodology value for [[NPU]] and heterogeneous edge inference, and the constructive counterpart to "Is Your NPU Ready for LLMs?" in what the 2026-07-19 digest called a "diagnose → schedule" pair worth tracking together. Also the core exemplar of the "Mixture-of-Experts (MoE) & Edge LLM Serving" taxonomy cluster formalized 2026-08-25 — though HeteroMosaic is not MoE-specific, it shares the cluster's central tension (application-class edge hardware, not MCU-class) with APEX, EdgeXpert, UnionSparse, and FreeToken.

## Possible thesis topics

Roofline-gated accelerator co-scheduling on open edge SoCs: reproduce HeteroMosaic's iGPU+NPU co-execution on non-Ryzen edge hardware and quantify how much of the 45% energy saving is recoverable in an open runtime (Master's, per the 2026-07-19 digest's explicit hook).

## Possible collaborations

Deming Chen's group (UIUC), whose MICRO-2026-accepted HeteroMosaic authorship the July 2026 monthly report flagged as worth tracking across future submissions given their edge-LLM-efficiency track record.

## Links to related papers

The direct constructive follow-on to "Is Your NPU Ready for LLMs?" (arXiv:2607.05475, `02_Papers/2026/2026_Cai_NPUReadyForLLMs.md`) — the 2026-07-19 digest's "diagnose → schedule" pairing. Part of the same emerging "edge LLM/MoE serving" cluster as PolyQ, APEX, EdgeXpert, UnionSparse, and FreeToken (`02_Papers/2026/2026_Yang_FreeToken.md`).
