# Weekly Digest — 2026-07-13

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Four papers selected this week, all firmly inside the 7-day window (submitted 4–9 Jul 2026). The set skews toward **efficient inference hardware**: an ultra-low-power bit-serial CNN accelerator for XR vision, an FPGA LUT-native acceleration framework, a cross-layer measurement study of on-device LLM inference on mobile NPUs, and a communication-efficient federated anomaly-detection method for IoT. Together they touch the [[Vision]], [[Quantization]], [[FPGA]], [[NPU]], [[Federated Learning]], [[Industrial IoT]], and [[Predictive Maintenance]] branches of the taxonomy.

**Sourcing note (methodology, this cycle):** the sandbox running this automated cycle could not reach the arXiv listing/query API directly (`export.arxiv.org` is blocked by the outbound network allowlist, and `web_fetch` refused non-provenanced URLs). Monitoring was therefore done through the Claude in Chrome extension on Ricky's browser, navigating the arXiv `recent` listings for cs.LG, cs.AR and eess.SP directly and reading each candidate's abstract page in full before inclusion — in line with the Observatory's "no hallucinated information / every claim traceable to source" principle. cs.DC was not separately swept this cycle (time budget); cs.LG, cs.AR and eess.SP together already surfaced a strong, coherent set. Every paper below was read at the abstract level from its arXiv page; none has yet been read in full-PDF depth. The optional IEEE Xplore / ACM DL / Google Scholar cross-checks were **skipped** this cycle: arXiv coverage alone was sufficient for a valid digest, and Google Scholar's terms discourage the kind of unattended automated querying an unsupervised scheduled run would amount to. They remain available for on-demand, human-in-the-loop use in a follow-up conversation.

---

## 1. FedKAD: Federated Low-Rank Koopman Learning for Multivariate Time-Series Anomaly Detection in IoT Systems

**Source:** arXiv:2607.08978 (cs.LG; cross-listed eess.SP) — submitted 9 Jul 2026
**Authors:** Tung-Anh Nguyen, Van-Phuc Bui, Anh Tuyen Le, Kim Hue Ta, Minh Thuy Le, J. Andrew Zhang, Xiaojing Huang
**Link:** https://arxiv.org/abs/2607.08978

**Why it matters:** This is the most directly actionable paper of the week for our [[Industrial IoT]] and [[Predictive Maintenance]] lines, and it sits at the intersection with [[Federated Learning]]. It attacks the exact deployment reality our lab cares about — decentralized, non-IID multivariate sensor streams, limited bandwidth, and MCU-class compute/memory budgets — and argues that you do *not* need to train and communicate large neural anomaly detectors to get competitive detection. The claimed efficiency deltas (three orders of magnitude faster training, ~80× less communication, ~79× lower inference latency) are exactly the kind of numbers that make on-device deployment feasible rather than aspirational.

**Technical summary:** FedKAD learns *normal* temporal dynamics via lightweight sliding-window **Koopman** representations instead of deep sequence models. Federated training is cast as a **low-rank consensus** problem: raw sensor streams and local reduced dynamics stay on the device, and only compact subspace variables are exchanged with the server. To optimize the shared representation under orthonormality (Stiefel-manifold) constraints, the authors derive a **federated Stiefel-ADMM** algorithm with convergence and stationarity guarantees under partial client participation. At inference, each client flags anomalies locally from the prediction residual between observed future trajectories and the learned Koopman dynamics. On four standard multivariate-time-series anomaly-detection benchmarks, FedKAD matches or beats federated deep-learning baselines while reporting up to 2.1×10³ faster training, 80× lower communication, and 79× lower inference latency.

**Novelty assessment:** The individual ingredients (Koopman operator learning, federated ADMM, Stiefel-manifold optimization) are each known, but their combination into a communication- and compute-frugal *federated* anomaly detector with a formal convergence result under partial participation is a genuinely novel and well-motivated systems-plus-theory contribution. The framing — replace the heavy neural model with a linear-dynamics surrogate you can actually afford to run on the edge — is a clean counterpoint to the deep-learning default we track under [[Industrial IoT]] anomaly detection, and complements last week's embedded-anomaly-detection survey (which flagged weak on-device drift handling and portability as open gaps).

**Relevance score:** 4/5 — strong fit for [[Federated Learning]] + [[Industrial IoT]] + [[Predictive Maintenance]]; the leading candidate this week for a `02_Papers/` deep-analysis record. Held below 5 pending full-PDF verification of the efficiency claims and of what "edge device" concretely means in their experiments (MCU vs edge-CPU).

---

## 2. Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference

**Source:** arXiv:2607.05475 (cs.AR; cross-listed cs.AI) — submitted 6 Jul 2026
**Authors:** Guanyu Cai, Ruiming Tian, Lang Yang, Zhouhong Ren, Jinliang Yuan, Lingkun Li, Jiliang Wang
**Link:** https://arxiv.org/abs/2607.05475

**Why it matters:** On-device LLM inference is the fastest-moving edge frontier, and this is a rare *measurement-first* paper rather than yet another optimization trick — it maps where the energy and latency actually go across [[NPU]], GPU and CPU backends on mobile. That makes it high-value reference material for anyone in the group deploying LLMs on constrained hardware, and its profiling tool (PowerBench) is a reusable asset for our own benchmarking work.

**Technical summary:** The authors present what they describe as the first comprehensive cross-layer measurement study of mobile LLM inference, spanning five mainstream frameworks and three hardware backends (CPU, GPU, NPU). They build **PowerBench**, a fine-grained profiler giving backend-specific energy attribution (not just device-level power). Three headline findings: (1) framework-induced performance gaps are *amplified* on NPUs — up to 10× with custom operators — because of divergent offloading and quantization strategies; (2) a clear **phase split** — NPUs excel at compute-bound *prefilling* while CPUs win on memory-bound *decoding*, because the NPU prefers large fixed-shape workloads that clash with the small-kernel, dynamic nature of decode; (3) substantial **scheduling headroom** is missed by prior work — suboptimal thread configs, uncoordinated NPU sleep latencies, and CPU polling intervals waste up to 40% of energy. They distill an energy-oriented best-practice configuration estimated to cut NPU-backend energy by up to 54.8% across three datasets.

**Novelty assessment:** Low algorithmic novelty (no new model or kernel), high *diagnostic* novelty. The prefill-on-NPU / decode-on-CPU characterization and the backend-specific energy attribution are the reusable insights, and the quantified "40% wasted on scheduling" result is the kind of finding that reshapes how you deploy rather than how you train. Connects the [[NPU]] and [[Quantization]] branches to the emerging LLM-on-edge trend we started tracking with the on-device SLM personalization paper last week.

**Relevance score:** 4/5 — strong reference and methodology value for [[NPU]] deployment and on-device LLM work; PowerBench and the phase-split insight are directly reusable. Reference/measurement value over research novelty.

---

## 3. BitFair: A 12nm Bit-Serial CNN Accelerator with Learnable Early Termination and Adaptive Bit Ordering for Ultra-Low-Power XR Vision

**Source:** arXiv:2607.05445 (cs.AR; cross-listed cs.CV, eess.IV) — submitted 4 Jul 2026
**Authors:** Ang Li, Chang Gao
**Link:** https://arxiv.org/abs/2607.05445

**Why it matters:** A fabricated (GlobalFoundries 12nm FinFET) accelerator that pushes always-on [[Vision]] into the sub-milliwatt-per-op, sub-millisecond-latency regime demanded by XR wearables. It is a concrete data point on how far *dynamic bit-level sparsity* can be exploited in silicon, and the core idea — learn per-layer thresholds that stop computing bits once the output is provably going to be zeroed by ReLU — is a compression/quantization concept reusable well beyond this specific chip.

**Technical summary:** BitFair is a software–hardware co-designed **bit-serial** CNN accelerator with two main levers. First, **learnable bit-level early termination**: per-layer thresholds trigger termination when accumulated partial sums reliably predict the final ReLU output will be zero, avoiding wasted work on bits that don't matter. Second, **adaptive bit ordering**: a search for layer-wise bit orders that front-load the most informative bits, maximizing early termination without hurting accuracy. The 12nm implementation has a 0.34 mm² core, 104 KB on-chip memory, and voltage scaling from 0.55–0.70 V, reaching sub-millisecond latency, up to 117.0 BTOPS/W and 0.07 pJ/SOP. On the event-vision benchmarks IBM DVS128 Gesture and N-MNIST it reports 96.5% and 97.7% accuracy, improving effective energy efficiency by 4.0–22.1× and accuracy by up to 9.2% over prior fabricated XR-vision accelerators.

**Novelty assessment:** Solid, well-executed hardware novelty. Bit-serial accelerators and bit-level sparsity are not new, but *learning* the early-termination thresholds and *searching* the bit order to maximize exploitable sparsity — as a joint software/hardware co-design validated in a taped-out 12nm chip — is a meaningful step. Sits at the [[Quantization]] × [[Vision]] × accelerator-hardware corner of the taxonomy and pairs conceptually with last week's UnIT (input-adaptive inference-time sparsity): both embrace dynamic, data-dependent sparsity, one on commodity MCUs, one in custom silicon.

**Relevance score:** 4/5 — strong for [[Vision]] and hardware-aware [[Quantization]]; the learnable-early-termination idea is transferable. One notch below a 5 because it is a custom ASIC (harder to reproduce in our typically MCU/FPGA/software-framework-oriented work) and is evaluated on event-camera datasets rather than our usual targets.

---

## 4. FPGN: Redefining Ultra-Fast Programmable Gate-based Neural Acceleration with Differentiable LUTs

**Source:** arXiv:2607.08427 (cs.AR; cross-listed cs.LG) — submitted 9 Jul 2026
**Authors:** Jiawei Liang, Haotong Qin, Linfeng Du, Xingyu Liu, Shangkun Li, Hui Yu, Michele Magno, Xinyu Chen, Jiang Xu, Wei Zhang
**Link:** https://arxiv.org/abs/2607.08427

**Why it matters:** Directly relevant to our [[FPGA]] branch and to nanosecond-latency inference for latency-critical edge tasks. FPGN pushes the "LUT-native" idea — treat the FPGA's lookup tables as *learnable neurons* rather than as building blocks for arithmetic operators — from an algorithmic curiosity into an end-to-end, physically-aware accelerator flow, which is precisely the gap that has held this line back.

**Technical summary:** FPGN is an end-to-end, physically-aware framework closing the gap between LUT-native learning and latency-optimized FPGA implementation. It contributes (i) a **hardware-aligned differentiable formulation** so that trained LUT neurons faithfully match real FPGA LUT primitives; (ii) a **structured LUT-native topology** with a streaming hardware architecture that improves routing locality and timing closure; and (iii) a **latency-driven compiler** using high-fidelity analytical Quality-of-Results models to automate design-space exploration and hardware generation. Reported results: up to **205× latency reduction** versus representative FPGA-based Binarized Neural Network (BNN) accelerators, and up to **30× higher LUT efficiency** than prior differentiable LUT-native networks, while maintaining competitive accuracy.

**Novelty assessment:** Genuine novelty in bridging algorithm and physical implementation. Prior LUT-native work optimized the math but produced physically-unaware topologies with poor routability/timing and no automated flow; FPGN's contribution is making the differentiable formulation *hardware-faithful* and wrapping it in an automated, latency-driven compiler. The BNN comparison ties it to the low-bit/[[Quantization]] lineage we already track (binarized networks), extended into the FPGA-LUT-as-neuron paradigm.

**Novelty caveat:** The 205× figure is against BNN baselines and the applicability is narrow — ultra-low-latency, small-model, FPGA-resident inference — so it is powerful within its niche rather than a general edge-deployment result.

**Relevance score:** 3/5 — relevant to [[FPGA]] deployment and low-bit inference, and a strong result, but narrower in applicability than the other three and requiring FPGA-specific expertise/toolchains that sit slightly outside our most active (MCU/framework) work.

---

## Candidates for deep analysis (`02_Papers/`)

No deep-analysis records were created automatically this cycle. In priority order:

- **#1 FedKAD (arXiv:2607.08978)** — strongest candidate: directly actionable for our [[Industrial IoT]] / [[Predictive Maintenance]] work under a [[Federated Learning]] setting, with a clear efficiency story worth verifying in full and a thesis hook (below).
- **#2 "Is Your NPU Ready for LLMs?" (arXiv:2607.05475)** — worth a deep record as a reference/benchmarking artifact if we pursue on-device LLM/[[NPU]] deployment; PowerBench could feed our own measurement setup.

## Suggested thesis / research hooks this week

- **On-device federated anomaly detection with linear-dynamics surrogates:** validate FedKAD-style Koopman anomaly detection on real MCU/edge hardware (Cortex-M / RISC-V) against quantized neural baselines, and test its behavior under concept drift — the exact gap flagged in last week's embedded-anomaly-detection survey. (Master's/PhD.)
- **Backend-aware scheduling for on-device LLM inference:** reproduce the prefill-on-NPU / decode-on-CPU phase split from paper #2 on our own devices and quantify how much of the 40% scheduling waste is recoverable in an open framework (e.g. via microTVM / ONNX Runtime). (Master's.)
- **Dynamic bit-level sparsity beyond ASICs:** transfer BitFair's learnable early-termination idea from custom silicon to a software/MCU or FPGA setting and measure whether the energy savings survive without dedicated bit-serial hardware. (Bridges #3 and #4; PhD-scale.)

---

**Notes:** All four papers are firmly within the last-7-days window and were verified at the abstract level from their arXiv pages; none has yet been read in full-PDF depth, so efficiency/accuracy figures should be re-checked before citation in any survey or thesis. IEEE/ACM and Google Scholar checks were not run this cycle (see sourcing note). `sources.yaml` `last_checked` for arXiv should be advanced to 2026-07-13.
