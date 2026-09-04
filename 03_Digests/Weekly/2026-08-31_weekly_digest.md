# Weekly Digest — 2026-08-31

Four papers spanning workload-characterization methodology for edge LLM serving, a streaming FPGA vision accelerator, an on-device NPU measurement study, and a wireless systems/communications co-design for distributed MoE inference. Touches [[Quantization]], [[Vision]], [[NPU]], and [[FPGA]] (see also [[MoE_Edge_LLM_Serving]]).

---

## 1. Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels

**Source:** arXiv:2608.25053 (cs.AR; cross-listed cs.AI, cs.DC, cs.PF) — submitted 25 Aug 2026; accepted at IEEE IISWC 2026
**Authors:** Amir Taherin, Sana Taghipour Anvari, Charles Amante, Yixiao Chen, Ruben Noroian, Zlatan Feric, Nicolas Bohm Agostini, Pu Zhao, José Cano, Bin Ren, Yanzhi Wang, David Kaeli
**Link:** https://arxiv.org/abs/2608.25053

**Why it matters:** Addresses a lack of standardized, reproducible methodology for characterizing edge LLM inference across hardware generations and backends. Hydra instruments HuggingFace Transformers and llama.cpp with a shared per-prompt timing schema fused with hardware telemetry, evaluated across three consecutive NVIDIA Jetson AGX generations (Xavier, Orin, Thor). The author list (Kaeli, Yanzhi Wang, Zlatan Feric) also produced the edge-RAG compression study in the prior digest, suggesting a sustained research thread on edge LLM deployment measurement.

**Technical summary:** Hydra characterizes 13 instruction-tuned LLMs from seven families across five execution formats (including multiple quantization levels), separating prefill and decode phases and connecting phase-level timing to system-resource utilization and efficiency metrics. The released artifact contains ~107K per-prompt records, publicly available with the framework's source code. Key finding: aggregate latency hides deployment-relevant effects — inference-backend structure changes *where* latency is introduced, [[Quantization]] reduces memory traffic and energy but does not predict power draw monotonically, and SoC generation changes how utilization/efficiency figures should even be interpreted.

**Novelty assessment:** High as a methodology and open-artifact contribution. It is not a new model or algorithm but a standardized, reproducible measurement framework, and the non-monotonic quantization/power finding is a genuinely useful empirical result that complicates simple "lower precision = lower power" assumptions.

**Relevance score:** 5/5 — open-source artifact and data (107K records), and a citable, non-obvious empirical finding about quantization's relationship to power.

---

## 2. SweepLSD: A One-Pass, O(width)-Memory Line Segment Detector with an Integer-Only Streaming Core and a Real-Time FPGA Realization

**Source:** arXiv:2608.22086 (eess.IV; cross-listed cs.AR, cs.CV) — submitted late Aug 2026
**Authors:** Yoshiyasu Shimizu
**Link:** https://arxiv.org/abs/2608.22086

**Why it matters:** A concrete [[Vision]] x [[Quantization]] x [[FPGA]] data point: a line-segment detector designed from the ground up for streaming, memory-constrained embedded deployment rather than adapted post hoc from a GPU-oriented design. The one-pass, O(width)-memory design directly targets the SRAM/BRAM constraints that make many vision algorithms impractical on FPGA-class edge hardware.

**Technical summary:** SweepLSD processes image data in a single streaming pass with memory scaling only with image width (not full-frame buffering), using an integer-only computational core suited to FPGA fixed-point logic, and demonstrates a real-time FPGA realization. Code, benchmarks, and evaluation harnesses are openly released (MIT license).

**Novelty assessment:** Moderate-to-high. Line segment detection is a well-studied problem, but the combination of strict O(width) memory bounds, an integer-only streaming core, and a real, real-time FPGA implementation (rather than a GPU baseline or simulation) is a solid, verifiable embedded-systems contribution with an open, reproducible release.

**Relevance score:** 4/5 — good fit for [[Vision]]: open code, real hardware realization, and a memory-efficiency angle relevant to resource-constrained edge deployment generally.

---

## 3. What Actually Runs: A Measurement Study of Language Model Placement and Decode Speed on the Apple Neural Engine

**Source:** arXiv:2608.22110 (cs.LG; cross-listed cs.AR, cs.PF) — submitted 22 Aug 2026
**Author:** Shahir M A
**Link:** https://arxiv.org/abs/2608.22110

**Why it matters:** A rigorous, independently-run measurement study of a widely-deployed consumer [[NPU]] (Apple's Neural Engine) that most researchers treat as a black box. It directly informs [[Quantization]] x Hardware questions: which operator formulations and weight encodings actually get accelerator placement, versus silently falling back to CPU.

**Technical summary:** Combines three independent measurement paths — a 64-shape sweep of LLM primitives recording per-operation device eligibility, matched models trained across size/precision with byte-identical quantized/fp16 structure, and direct reads of the ANE's memory-controller byte counters during inference — to establish what actually executes on-accelerator rather than what the compiler intends. Central finding: accelerator placement is a property of *how* a computation is expressed, not what it computes (a fused RMSNorm is ANE-eligible; its arithmetically identical decomposition is CPU-only), and weight encoding gates residency (an fp16 conv-heavy model runs entirely on CPU while its int8/2-bit versions reach ~83% ANE residency and run 1.8–2.2x faster). The smallest, fastest models measured are ternary (25M-parameter half-attention ternary model: 10.5 MB, 0.63 ms/token). Code, harnesses, and run ledgers are openly released.

**Novelty assessment:** High for rigor and actionability, despite being single-authored. The methodology (three independent, cross-validated measurement paths) is unusually careful for a hardware-measurement paper, and the "expression, not computation, gates placement" finding is a genuinely non-obvious, practically important result for anyone deploying quantized models on Apple silicon.

**Relevance score:** 4/5 — strong candidate for the [[NPU]] branch: open code and a clear, falsifiable design procedure ("choose the encoding first, then spend the byte budget on parameters").

---

## 4. AirMoE: Realizing Over-the-Air Distributed Mixture-of-Experts Inference at the Wireless Edge

**Source:** arXiv:2608.22932 (eess.SP) — submitted 24 Aug 2026, revised 26 Aug 2026
**Authors:** Huiling Yang, Zhanwei Wang, Kaibin Huang
**Link:** https://arxiv.org/abs/2608.22932

**Why it matters:** Extends distributed MoE-LLM inference at the wireless edge from a pure systems/scheduling problem into a joint communications-and-computing co-design, using over-the-air computing (AirComp) to aggregate expert outputs via simultaneous wireless waveform superposition instead of sequential uplink transmissions. This is a distinct angle from the edge-native MoE serving systems in [[MoE_Edge_LLM_Serving]] (e.g. FreeToken) — here the bottleneck and the fix are both at the physical/wireless layer, not the memory/compute layer.

**Technical summary:** Proposes an inference-aware AirMoE error metric quantifying how AirComp aggregation distortion propagates to end-to-end inference accuracy, via perturbation-based layer-sensitivity calibration. Decomposes the resulting joint optimization into a two-timescale framework: a fast-timescale, provably globally-optimal threshold-based power-control policy, and a slow-timescale activation- and channel-aware expert-placement strategy that assigns higher-importance experts to devices with lower channel-power cost. Reports accuracy gains over baselines, especially under strong device heterogeneity.

**Novelty assessment:** Moderate-to-high as a systems/communications co-design — AirComp itself is an established over-the-air aggregation technique (more familiar from federated-learning gradient aggregation), but its application to MoE expert-output aggregation with a bespoke inference-aware distortion metric and provably-optimal power control is a new combination.

**Relevance score:** 3/5 — a genuinely novel angle bridging serving concerns and the physical wireless layer, theoretical/simulation-based (no real radio hardware deployment reported) and somewhat adjacent to the Observatory's usual embedded/TinyML focus.

---

## Suggested thesis / research hooks

- **From Jetson-class to MCU-class workload characterization:** Hydra's methodology (shared timing schema + hardware telemetry fusion) is built for Jetson AGX-class SoCs (GPU + accelerator). Would the same phase-aware characterization approach transfer to genuinely MCU-class hardware ([[Cortex-M]], [[NPU]] micro-accelerators), where prefill/decode phases and even the models themselves look very different? A well-scoped Master's-level replication/extension study.
- **Does "expression gates placement" hold beyond Apple silicon?** The ANE paper's central finding — that operator formulation, not just precision, determines accelerator eligibility — is plausible for other NPUs (Arm Ethos, Cortex-M NPU extensions) but untested there. A comparative measurement study across two or three commodity NPUs would be a strong PhD-scale systems contribution extending this paper's methodology.
- **Generalizing O(width)-memory streaming beyond line detection:** SweepLSD's one-pass, width-bounded memory design is specific to line segment detection, but the underlying streaming-memory discipline could plausibly generalize to other structured vision primitives (edge/corner detection, simple pose primitives) relevant to always-on vision use cases adjacent to [[Keyword_Spotting]]. A Master's-scale generalization study.
- **AirComp for edge inference vs. edge training:** AirMoE applies over-the-air aggregation to MoE expert-output aggregation at inference time; the same physical-layer aggregation trick is already used for gradient aggregation in over-the-air [[Federated_Learning]]. Is there a unified framework connecting AirComp-for-training and AirComp-for-inference, and would AirMoE's layer-sensitivity calibration technique improve over-the-air federated-learning gradient aggregation too? A PhD-scale question bridging signal processing and [[Federated_Learning]].
