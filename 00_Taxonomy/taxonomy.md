# Taxonomy

This is a living document. Papers may belong to multiple categories, and new subcategories are introduced as new research directions emerge

## Algorithms

- Quantization (post-training, quantization-aware training, mixed precision, binary/ternary networks)
- Pruning (structured, unstructured, dynamic)
- Distillation (knowledge distillation, self-distillation)
- NAS (hardware-aware NAS, once-for-all networks)
- Compression (low-rank factorization, weight sharing)
- Continual Learning
- On-device Learning
- Federated Learning
- Mixture-of-Experts (MoE) & Edge LLM Serving (expert routing/caching/prefetching, heterogeneous CPU/GPU/NPU scheduling, quantization compilers for on-device LLM inference)

## Frameworks

- TensorFlow Lite Micro
- CMSIS-NN
- microTVM / TVM
- MLIR
- ONNX Runtime
- ExecuTorch (PyTorch-native, microcontroller-to-SoC deployment)
- Edge Impulse (MLOps platform layer above the runtimes above)

## Hardware

- Cortex-M
- Cortex-A
- RISC-V
- DSP
- FPGA
- NPU
- Event-Driven / Neuromorphic Accelerators (event-graph-neural-network hardware for sparse, asynchronous sensor streams — vision and audio)

## Applications

- Keyword Spotting
- Vision
- Human Activity Recognition
- Biosignals
- Industrial IoT
- Predictive Maintenance

## Benchmarks & Datasets

- MLPerf Tiny
- TinyML Reference Datasets (Speech Commands, Visual Wake Words)

## Security

- Hardware / Physical Security of Edge AI Accelerators (trusted execution environment extension into processing-in-memory, physical & side-channel extraction attacks)

## Evolution notes

Here we will note over time when a sub-category splits, merges with another, or becomes saturated

**2026-06-30 — Quantization/Compression: shift from CNN-era to LLM-era methods.** Since 2023-2024, new work in both [[Quantization]] and [[Compression]] has shifted from compressing CNNs (the AlexNet/VGG/MobileNet era) toward post-training, calibration-light compression of large language models for edge/on-device deployment — see [[2024_Lin_AWQ]], [[2024_Ashkboos_SliceGPT]], [[2024_Gu_MiniLLM]], synthesized in [[2025_Liu_ModelCompressionSurvey]]. Worth watching whether this becomes a distinct sub-category ("LLM edge compression") rather than a variant of the existing CNN-era techniques, since calibration cost and structured-vs-unstructured trade-offs differ from the AlexNet/VGG-era literature.

**2026-06-30 — Vision: hybrid CNN/transformer architectures emerging alongside pure CNNs.** [[2025_Zeng_TinyNeXt]] targets the memory-bound nature of standard self-attention directly (Lean Single-Head Self-Attention) and pairs it with a stage-aware CNN/transformer macro design, extending MobileNet-style efficient-by-design thinking to a new architecture family. Still a single data point; not yet enough to call this a sub-category split, but worth tracking as more TinyML-scale transformer work appears.

**2026-06-30 — Frameworks/Hardware: NPU vendors building compilation stacks directly on MLIR.** [[2026_Absar_HexagonMLIR]] (Qualcomm Hexagon) is a large industrial-scale case of an NPU vendor lowering standard front-ends (Triton, PyTorch) through MLIR's dialect infrastructure rather than a bespoke toolchain. Combined with [[2023_Das_MLDrivenHardwareCostModelMLIR]] (learned MLIR-level cost models), this suggests [[MLIR]] is consolidating as shared compiler infrastructure across NPU vendors, not just an academic substrate — worth re-checking in a year whether more vendors follow.

**2026-06-30 — Toolchain bifurcation: general compilers retreating from MCU-class targets vs. in-sensor AI.** Per the 2026-06 monthly report, Apache TVM's v0.25.0 release candidate trims "leftover microTVM/CRT crumbs" and the TVM forum has an open thread questioning microTVM's future, while hardware vendors (e.g. STMicroelectronics' ISPU 2.0) push AI processing further down into the sensor itself. Not proof microTVM is being discontinued, but a real signal that MCU-native libraries ([[CMSIS-NN]], [[TensorFlow_Lite_Micro]]) may be consolidating their position as the practical default for ultra-low-power deployment while [[microTVM_TVM]]'s center of gravity drifts toward GPU/accelerator-class hardware. Re-check in subsequent monthly reports.

**2026-08-25 — Cross-cycle synthesis: deep-analysis backlog, a recurring "how edge is edge" tension, and accumulating taxonomy gaps.** A deeper read across all eight weekly digests (2026-06-29 through 2026-08-23) and both monthly reports (June, July), done in response to a request to deep-analyze the three papers flagged by the 2026-08-23 digest (now recorded: [[2026_Kneip_ETHEREAL]], [[2026_Ma_EEGAuditoryAttentionASIC]], [[2026_Yang_FreeToken]]), surfaced three patterns no single weekly digest could show on its own.

*(1) A real deep-analysis backlog.* Only the three papers from the 2026-06-29 cycle (NVFP4, HW-NAS, Embedded ML pipelines) had `02_Papers/` records before this pass. Of the next seven weekly cycles, the 2026-08-23 cycle's three candidates (ETHEREAL, the EEG AAD ASIC, FreeToken) were just recorded earlier this session — but the other six each flagged 1–3 deep-analysis candidates that were still unrecorded: UnIT and the SLM-stability paper (07-05); FedKAD and "Is Your NPU Ready for LLMs?" (07-13); PolyQ and HeteroMosaic (07-19); the RISC-V float16 training paper and the Hailo-8L on-device adaptation paper (07-26); APEX, EdgeXpert, and UnionSparse (08-13); Lonic and YAVIN (08-20). That is 13 still-unrecorded candidates — worth a dedicated backlog-clearing pass rather than letting each week's candidates quietly accumulate.

*(2) A recurring "how edge is edge" tension.* PolyQ and HeteroMosaic (07-19), the APEX/EdgeXpert/UnionSparse MoE-memory cluster (08-13), and now FreeToken (08-23) all apply genuinely novel systems ideas to laptop/workstation/edge-GPU-class hardware rather than the lab's core MCU/[[RISC-V]]/[[NPU]] tier. Each digest has noted this in passing for its own week's paper; read together, it is a standing boundary question — at what point does "edge-native" stop meaning genuinely constrained hardware? — that the 2026-08-23 digest's suggested thesis hooks and the new FreeToken record both point back to.

*(3) Taxonomy gaps are accumulating faster than they're being resolved.* Three gaps have now been independently flagged and each time deferred "for a future refinement pass": a `Mixture-of-Experts` / edge-LLM-serving node (08-13, sharpened 08-23 after FreeToken), an "Edge AI Security / Trusted Execution" node (08-20, after YAVIN), and — newly noticed while writing the ETHEREAL record — that custom event-driven/neuromorphic accelerator ASICs (ETHEREAL) don't map onto the existing Hardware branch (Cortex-M, Cortex-A, RISC-V, DSP, FPGA, NPU) at all. With six independent papers now triangulating the edge-LLM-serving gap alone (PolyQ, HeteroMosaic, APEX, EdgeXpert, UnionSparse, FreeToken), this is worth Ricky's explicit decision on whether to formalize a node rather than deferring again.

*Also worth carrying forward, not yet acted on:* the "spend compute only where it matters" research program the July monthly report identified (UnIT, BitFair, AMC, HeteroMosaic) has independent production-scale corroboration in MLPerf Tiny v1.4 (Syntiant NDP120's 3.3% duty cycle) — worth checking in the next monthly report whether this is still generating new papers or has matured into assumed background practice. Prominent general ML-systems groups (Song Han, Ion Stoica, Matei Zaharia, Kurt Keutzer on FreeToken; Mohsen Imani on PolyQ; Deming Chen on HeteroMosaic) are increasingly publishing edge-adjacent work alongside the embedded-systems specialists this Observatory has traditionally tracked — a possible signal that mainstream ML-systems attention is shifting toward edge deployment, worth watching for in September. Finally, IEEE Xplore and ACM Digital Library access has been blocked, unauthenticated, or unreliably date-filtered in literally every cycle since June — this is a standing institutional-access gap, not a search-technique problem, and is worth solving directly (e.g. a monitoring run while Ricky is on the unige.it campus network) rather than re-noting weekly.

**2026-08-25 — Formalized: Mixture-of-Experts (MoE) & Edge LLM Serving, under Algorithms.** Following the cross-cycle synthesis above, Ricky asked to both clear the deep-analysis backlog and formalize this node given six independent papers had converged on it. The node now groups seven `02_Papers/` records: [[2026_Yang_FreeToken]] (bandwidth-adaptive MoE serving on laptop/workstation GPUs), [[2026_Kanani_APEX]] (learned expert prefetching), [[2026_Ha_EdgeXpert]] (hardware-software co-designed MoE + speculative decoding, Samsung 28nm silicon), [[2026_Jiang_UnionSparse]] (index-efficient low-bit sparse LLM inference — grouped here for its shared edge-LLM-memory-bottleneck framing though it is not itself MoE-specific), [[2026_Oh_PolyQ]] (CPU-oriented fractional-bit quantization compiler for edge LLMs), [[2026_Jun_HeteroMosaic]] (heterogeneous iGPU+NPU scheduling for edge LLM inference), and [[2026_Cai_NPUReadyForLLMs]] (the diagnostic measurement study the cluster's scheduling/co-design papers build on). The node's description folds in routing/caching/prefetching, heterogeneous scheduling, and LLM-specific quantization compilation, since the seven papers span all three without cleanly separating into distinct sub-nodes yet — revisit if the cluster keeps growing and a split becomes warranted (e.g., separating pure MoE-routing papers from general edge-LLM-serving-infrastructure papers like HeteroMosaic and PolyQ, which are not MoE-specific).

Deliberately *not* formalized in this pass: the "Edge AI Security / Trusted Execution" gap (08-20, anchored by [[2026_Fang_YAVIN]]) and the event-driven/neuromorphic-ASIC gap in the Hardware branch (08-23, anchored by [[2026_Kneip_ETHEREAL]]) remain open — each currently has only one anchor paper, versus the seven that justified acting on the MoE/serving node here. Revisit both if a second independent paper appears in either area.

The backlog itself is now cleared: all 13 papers flagged as deep-analysis candidates across the 2026-07-05 through 2026-08-20 weekly digests have `02_Papers/` records as of this pass — [[2025_Neth_UnIT]], [[2026_Paula_SLMStabilityMonitoring]], [[2026_Nguyen_FedKAD]], [[2026_Cai_NPUReadyForLLMs]], [[2026_Oh_PolyQ]], [[2026_Jun_HeteroMosaic]], [[2026_Hubinet_RISCVFloat16Training]], [[2026_Piechocki_Hailo8LAdaptation]], [[2026_Kanani_APEX]], [[2026_Ha_EdgeXpert]], [[2026_Jiang_UnionSparse]], [[2026_Chen_Lonic]], [[2026_Fang_YAVIN]] — alongside the three from the 2026-08-23 cycle recorded earlier the same day. One caveat: the RISC-V float16 training record could not be independently re-verified from source in this pass (a persistent web-fetch rate limit on that specific URL survived five retries across the session) and is built from the weekly digest's own full-text-verified summary rather than this session's direct read — flagged in that record itself, worth a follow-up re-fetch.

**2026-09-02 — First Knowledge Base Consolidation cycle: Security branch formalized, MoE/Edge-LLM-Serving concept page created.** The on-demand Knowledge Base Consolidation task ran for the first time this cycle, reviewing the two `ready_for_review` candidates in `00_Config/consolidation_candidates.yaml`. Both were promoted/merged into new persistent Knowledge Base concepts, verified against primary arXiv sources: (1) a new top-level **Security** taxonomy branch was created, with **Hardware / Physical Security of Edge AI Accelerators** as its first entry — grounded by two independent anchor papers three weeks apart, [[2026_Fang_YAVIN]] (architectural TEE/PIM trust-boundary extension) and [[2026_Mehta_LLMscope]] (physical/optical extraction attack), now recorded together as one concept with two named variants at `01_Knowledge_Base/Security/Hardware_Security_of_Edge_AI_Accelerators.md`. (2) The **Mixture-of-Experts (MoE) & Edge LLM Serving** taxonomy entry, added here on 2026-08-25 but never given a corresponding `01_Knowledge_Base/` concept page, now has one at `01_Knowledge_Base/Algorithms/MoE_Edge_LLM_Serving.md` — this closes a taxonomy/Knowledge-Base inconsistency this session found while reviewing the candidate queue. The recurring "how edge is edge" boundary question (previously only named in digests and this taxonomy file) is now documented as that concept's central open problem rather than left implicit. Full decisions, evidence, and rationale are recorded in `00_Config/consolidation_history.yaml` and `03_Digests/Consolidation/2026-09-02_kb_consolidation.md`. The three remaining `watching` candidates (MCU/NPU measurement infrastructure; event-driven/neuromorphic ASIC hardware gap; in-memory-computing/emerging-NVM hardware gap) were reviewed but left open — each still has only one anchor paper, short of the two-independent-papers bar this taxonomy has applied consistently since 2026-08-25.

**2026-09-02 — Deliberate coverage-gap-closing pass (same day, following the consolidation cycle above): three new taxonomy nodes, two new branches, eight new paper records.** In response to Ricky asking whether the KB's coverage of EdgeAI was sufficient and then directing gaps to be closed, this Observatory ran a targeted research pass (not tied to the weekly/monthly cycle) rather than mechanically promoting every open item. Real, verified papers were located via arXiv/web search for each candidate gap; nothing was formalized without genuine primary-source evidence, and honesty about remaining uncertainty was preferred over forced closure.

*Formalized as new taxonomy nodes:* **Event-Driven / Neuromorphic Accelerators** (Hardware) — cleared this taxonomy's two-independent-anchor bar: [[2024_Yang_EvGNN]] and [[2026_Kneip_ETHEREAL]] (same TU Delft-centered cluster, FPGA-to-ASIC lineage) plus [[2026_Jeziorek_EventAudioGNNKWS]] (a fully independent AGH Kraków/CEA-List/Keio group, applying the same event-graph-neural-network hardware paradigm to audio rather than vision) — the second, unrelated group's convergence on the same paradigm is the deciding evidence. This also corrected a standing error: the ETHEREAL record's prior-art discussion had provisionally attributed FPGA-generation prior work to "T. Liu et al."; direct verification identified the real paper as [[2024_Yang_EvGNN]], by an overlapping author subset (Kneip, Frenkel) — ETHEREAL is that cluster's own later ASIC-generation successor, not a response to unrelated work. **ExecuTorch** and **Edge Impulse** (Frameworks) — both real, well-documented, actively-used projects with primary-source papers ([[2026_Nachin_ExecuTorch]], Meta; [[2022_Hymel_EdgeImpulse]]) that were missing despite PyTorch-native deployment and MLOps-platform tooling being clearly real parts of the field; Edge Impulse in particular had been an actively-monitored `00_Config/sources.yaml` software project since the Observatory's founding with no corresponding Knowledge Base page. A new top-level **Benchmarks & Datasets** branch, with [[MLPerf_Tiny]] and [[TinyML_Reference_Datasets]] concepts organizing existing records ([[2021_Banbury_MLPerfTiny]], [[2018_Warden_SpeechCommands]]) that previously had no taxonomy home of their own, despite "Benchmarks" and "Datasets" being two of the four monitoring categories in this Observatory's founding instructions.

*Deliberately left open rather than force-closed:* the **in-memory computing / emerging NVM** hardware gap gained its first real recorded paper ([[2026_Razi_FALCON]]), but the two other candidate second-anchor papers found in this pass (an April 2026 MTJ logic-in-memory paper and a DAC 2025 ReRAM paper) share authors with FALCON — a real, active single research program (three papers in 18 months) rather than independent corroboration. Kept as a recorded paper and a `watching` consolidation candidate, not promoted to a formal node, pending a genuinely independent group. The **MCU/NPU-tier standardized measurement infrastructure** gap gained two solid, real paper records ([[2026_Taherin_Hydra]], [[2026_Bryngelson_AppleNeuralEngine]]) — both are rigorous, longitudinal, open measurement infrastructure — but both remain at the Jetson-AGX/Apple-silicon tier; no MCU/Ethos-U/RISC-V-NPU-tier analogue was found, so the specific gap named by the August 2026 monthly report remains genuinely unresolved. A new **Edge GPU / Jetson-class hardware** candidate was opened (anchor: [[2025_Chakraborty_ProfilingJetsonVisionInference]]) rather than formalized, since only one paper was verified in this pass; a second Jetson-tier characterization paper would clear the bar. **Robotics/autonomous-systems edge AI** was identified as a plausible Applications gap during the initial coverage review but no credible anchor paper was located in this pass — left unactioned rather than filled with a weak placeholder.

Full evidence trail in `00_Config/consolidation_history.yaml` (promoted: neuromorphic/event-driven) and `00_Config/consolidation_candidates.yaml` (still watching: in-memory computing/NVM, MCU/NPU measurement infrastructure, Edge GPU/Jetson tier).
