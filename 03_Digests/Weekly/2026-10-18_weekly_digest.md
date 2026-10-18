# Weekly Digest — 2026-10-18

A modest week with one clear standout. LocalTrain gives the integer-only on-device training thread its first fabricated-FPGA energy measurement against an embedded GPU, which is the kind of number the candidate queue has been missing. Three further items are selected at lower scores: a Wi-Fi CSI human-activity-recognition feasibility study on a memory-constrained microcontroller, a noise-aware training method for transformers on analog compute-in-memory hardware, and a distillation recipe for power-grid edge inference. Touches [[On-device_Learning]], [[Quantization]], [[FPGA]], [[Human_Activity_Recognition]], [[Distillation]] and [[Industrial_IoT]].

Covers arXiv listings of 8 to 16 October 2026 plus Google Scholar results sorted by date. Selection was made from arXiv abstract pages and Scholar snippets only; no full text was read for any item, and this is noted per item.

---

## 1. LocalTrain: Integer-Only Local Learning for Energy-Efficient CNN Training on Edge FPGAs

**Source:** arXiv:2610.17099 (cs.AR; cross-listed cs.LG) — submitted 12 Oct 2026. Found in the cs.AR recent listing.
**Authors:** Shiqi Ding, Xuanyu Liang, Xinyang Liu, Boyang Li, Zhiqiang Que, Guosheng Hu, Jiayang Li
**Link:** https://arxiv.org/abs/2610.17099

**Why it matters:** Recent weeks have accumulated papers treating the memory and energy cost of training as the design variable on constrained devices, mostly at the microcontroller tier and mostly without a hardware energy comparison. This one trains a CNN end to end with integer arithmetic on a small FPGA board and compares measured training energy against an embedded GPU running the same integer method. It extends the [[On-device_Learning]] thread to [[FPGA]], and its integer-only constraint is the same one that has pushed [[Quantization]]-aware training toward runtimes with no floating point.

**Technical summary:** Local learning removes cross-layer backpropagation dependencies by attaching regional auxiliary classifiers. The authors argue that memory, gradient accumulation and quantization-scale handling remain hard even then, and address them with a shared integer matrix engine, on-chip expansion of compact errors, tile-by-tile gradient accumulation, and reuse of historical scales for direct output conversion. On a KV260 board at 200 MHz the prototype reaches 76.57% accuracy on CIFAR-10 and 91.85% on SVHN at about 4.20 W mean module power, with effective throughput of roughly 31.6 GMAC/s. Versus the same integer method on a Jetson Orin Nano it uses 40.4% and 42.1% less measured training energy but runs 1.86x and 1.82x longer.

**Novelty assessment:** Moderate. Local learning and integer training are known individually; the contribution is the integrated, measured hardware realization and the energy-versus-latency trade-off against an embedded GPU. The accuracies are low in absolute terms for CIFAR-10, the networks are small, the paper is seven pages, and the abstract page lists no code. Hardware-versus-software agreement is supported by selected state checks and matching prediction counts rather than a full equivalence study. Read at abstract level only.

**Relevance score:** 4/5 — measured energy on real hardware for integer-only training, directly on an active candidate; held below 5 because the target is a mid-size FPGA rather than a microcontroller and no code is listed.

---

## 2. Feasibility and Deployment Analysis of Wi-Fi-Based Human Activity Recognition on a Memory-Constrained Microcontroller

**Source:** IEEE Access, 2026 (Malik, Ahmad, Kim) — Scholar result dated about five days before this run; IEEE DOI not captured (snippet only).
**Link:** https://ieeexplore.ieee.org (title search; open-access PDF listed on Scholar)

**Why it matters:** Wi-Fi channel-state-information sensing is a device-free route to [[Human_Activity_Recognition]], and the usual objection is that the models do not fit where the radio sits. A paper framed as a feasibility and deployment analysis, with a stated note that accuracy elsewhere is floating-point and INT8 is reported separately, suggests attention to the gap between conversion success and retained accuracy that the [[Quantization]] page flags.

**Technical summary:** From the snippet only: the paper analyses deploying a Wi-Fi-based HAR model on a memory-constrained microcontroller and distinguishes floating-point accuracies from INT8 results, stating that successful conversion alone does not establish deployability. Target device, model, datasets, memory and latency figures were not visible.

**Novelty assessment:** Cannot be judged from the snippet. The framing (feasibility analysis, explicit INT8 versus float separation) is a methodological virtue; novelty over earlier Wi-Fi CSI HAR on embedded devices, including a UABC embedded-device system found in the same search, is unknown.

**Relevance score:** 3/5 — on-topic application at the microcontroller tier, but unverified beyond a snippet; an unige.it full-text read would settle whether it earns a higher score.

---

## 3. ABNAT: Attention-Based Noise-Aware Training for Robust Transformers on Analog Compute-in-Memory Systems

**Source:** arXiv:2610.22065 (cs.LG) — listed 16 Oct 2026; abstract page was rate-limited (HTTP 429) so only title, authors and subject tags were read.
**Authors:** Wenshuai Yao, Wenyong Zhou, Hanyong Shao, Zhiyuan Ning, Yizhe Chen, Yuannuo Feng, Kechao Tang, Ru Huang
**Link:** https://arxiv.org/abs/2610.22065

**Why it matters:** Analog in-memory computing is now the densest hardware thread in the queue, and the open problem there is making models tolerate the non-idealities of the devices. This is a training-side answer for transformers, a model family the earlier chip papers have not addressed.

**Technical summary:** Title-level only: noise-aware training that uses attention structure to make transformers robust on analog compute-in-memory systems. Noise model, device assumptions, accuracy numbers and hardware validation could not be read.

**Novelty assessment:** Unassessable without the abstract; the only fact available is that it targets transformers rather than CNNs on analog CiM. It should not be read as validated on silicon.

**Relevance score:** 3/5 — plausible and on an active thread, but title-level only. Re-read next cycle.

---

## 4. Physics-Aware Distillation of a Grid Foundation Model for Real-Time Edge Inference

**Source:** arXiv:2610.21833 (cs.LG) — submitted 15 Oct 2026.
**Authors:** Vlad Alexandru Sănduleac, Shahariya Rasheed Rayamarakkarveettil Puthanpurayil, Noman Khan, Remus Teodorescu
**Link:** https://arxiv.org/abs/2610.21833

**Why it matters:** A compact case of [[Distillation]] for an [[Industrial_IoT]]-style setting with a domain constraint, plus an honest negative result: the physics-residual term the authors introduce hurts performance when averaged over layers, and most of the gain comes from plain output matching.

**Technical summary:** A 20.1M-parameter, 12-layer graph transformer pretrained on a masked power-flow objective is distilled into a 0.62M-parameter, 6-layer student (32.5x fewer parameters) using output, physics-residual, latent-state and attention-transfer losses. On a renewable-heavy IEEE 118-bus variant with 97,529 AC-OPF-feasible scenarios, distillation lowers student error on all four predicted quantities, by up to 48% on active-power dispatch, and every distilled student beats the teacher on reactive-power dispatch. All eight loss combinations are ablated, and accuracy against ground truth is reported separately from fidelity to the teacher.

**Novelty assessment:** Low-to-moderate. The separation of accuracy from fidelity and the reported negative ablation are good practice; the architecture and losses are standard. No edge-hardware measurement is reported (the small model is only proposed for future benchmarking), the title's real-time edge claim is therefore untested, and no code is listed.

**Relevance score:** 3/5 — clean, honest distillation study on a power-systems use case, but no deployment evidence.

---

## Also noted this week (not selected, kept for provenance)

- **Joint entropy-aware quantization for energy-efficient TinyML human activity recognition on IoT edge devices** — Lamaakal, Yahyati, El Makkaoui, Ouahbi, *Scientific Reports*, 2026. Scholar snippet only; reports deployment on microcontroller-class devices. [[Quantization]] / [[Human_Activity_Recognition]]. Candidate for a closer read.
- **Hardware-constrained deployment of an INT8 MobileNetV1 for single-image human activity recognition on an STM32F407 microcontroller** — Tarhouni, Ben Aicha, El Khediri, Moulahi, *Computing* (Springer), 2026. Scholar snippet only. [[Cortex-M]].
- **Reliable Federated TinyML Deployment for IoT Security** — Park, Bae, Prabhu, Saha, Li, arXiv preprint, 2026. Scholar snippet; the authors state microcontroller deployment as future work. [[Federated_Learning]].
- **BitSparse: Compact Activation Storage for ReLU Feed-Forward Networks** — arXiv:2610.22256, Zhu, Sun, Lio, Yu. Listing-level only; potentially relevant to activation memory. https://arxiv.org/abs/2610.22256
- **GPU Goldmines: Tunable WebGPU Kernels for Edge LLM Inference** — arXiv:2610.17321 (cs.DC). Listing-level only. https://arxiv.org/abs/2610.17321
- **Seamless Deployment of Machine Learning Inference at the Far Edge: An Empirical AWS IoT Greengrass Architecture for Industrial Predictive Maintenance** — arXiv:2610.14815 (cs.DC). Listing-level only. [[Predictive_Maintenance]]. https://arxiv.org/abs/2610.14815
- **FPGA Based Design And Implementation of Neural Network Compensators for Nanocrystalline MEMS Pressure Sensor** — arXiv:2610.18136 (cs.AR). Listing-level only. https://arxiv.org/abs/2610.18136
- **HeteroVDiff: Pipelining Video Diffusion across Mobile NPU and GPU with Shared Weights** — arXiv:2610.16244 (cs.DC). Listing-level only. [[NPU]]. https://arxiv.org/abs/2610.16244
- **DEX: Digit-Level Early Exit for Energy-Efficient MSDF Neural Network Inference** — arXiv:2610.11748 (cs.AR). Listing-level only. https://arxiv.org/abs/2610.11748
- **ReSAFT: An Efficient Stuck-at Fault-Tolerant Scheme for ReRAM-based Process-in-Memory Accelerators** — arXiv:2610.09999 (cs.AR). Listing-level only; same device-fault theme as the in-memory-computing candidate.
- **Scholar background noise:** many Scholar hits were book chapters and review articles on TinyML (for example a *TinyML Systematic Review* in IEEE Access and an XAI/TinyML survey); none was selected. Also seen: QScheduler (already tracked), TrainDeeploy (DATE 2026, Conti group), and an integer-only tanh/sigmoid kernel for RISC-V (ICCS 2026), none new this week.
- **Search coverage this cycle:** arXiv coverage came from the cs.AR, cs.LG, eess.SP and cs.DC "recent" listings (cs.LG showed only its first 50 of 306 entries for 16 Oct; eess.SP only partly covered), not from the advanced search. The `site:`-filtered WebSearch queries for IEEE Xplore, ACM DL, MDPI, ScienceDirect and SpringerLink returned almost entirely non-publisher pages (arXiv, preprints, vendor blogs) and surfaced no new dated item; coverage of those five libraries is therefore thin and should not be read as absence of relevant work. Further arXiv abstract fetches were rate-limited (HTTP 429) after the first few, so ABNAT and some items stayed at title level. The Scholar pass ran 3 queries via Chrome (pruning/NAS/TinyML; keyword spotting/biosignal/HAR on microcontrollers; integer-only/on-device training on NPU/RISC-V).

---

## Signals for the knowledge base

LocalTrain adds a measured-energy anchor to the integer-only on-device training candidate, which is already at `ready_for_review`; evidence was appended without changing its status. It also shows a pattern worth the Consolidation cycle noticing: in this sub-regime the trade-off is energy versus latency (40% less training energy at about 1.8x the time against an embedded GPU), not a straight win. ABNAT is recorded as supporting context for the in-memory-computing candidate (a training-side answer to device non-ideality), at title level only. Nothing else this week clears the bar for a new candidate.

---

## Suggested thesis / research hooks

- **Integer-only training energy on a microcontroller-class platform:** LocalTrain's FPGA-versus-Jetson comparison has no counterpart at the Cortex-M or NPU-equipped microcontroller tier. A Master's project could reproduce an integer-only local-learning step on an STM32N6-class device and report energy per step against the FPGA figures.
- **Float-versus-INT8 gap in Wi-Fi CSI HAR:** if the full text confirms the paper reports the gap, a thesis could replicate it across several CSI datasets and microcontrollers, with a reproducible quantization pipeline through [[TensorFlow_Lite_Micro]].
- **When does physics-informed distillation help?** The grid paper's negative physics-residual result invites a systematic study of which domain-constraint terms survive distillation into sub-million-parameter students and on which edge hardware they run.
- **Transformer noise-aware training validated on a real analog chip:** if ABNAT's abstract confirms simulation-only evaluation, a collaboration with a group holding a CiM prototype could close that gap.
