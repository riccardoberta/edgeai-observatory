# Weekly Digest — 2026-08-20

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Four papers selected this week, submitted 13–17 Aug 2026 (the window since the last digest, 2026-08-13). This cycle's arXiv coverage skewed toward cs.AR, which was swept in full for the window; eess.SP and cs.DC were covered via full listing pages that, given tooling constraints this run, reliably surfaced entries only through roughly mid-window (see Sourcing note) — a narrower sweep than usual, flagged as a coverage caveat below. No single dominant theme emerged this week (unlike last week's edge-MoE cluster); instead the four papers span four different corners of the taxonomy: on-device learning hardware for spiking networks, a security architecture for quantized edge LLM execution, hardware-generated quantization for a non-neural model class (boosted decision trees), and a wearable sensing front-end design study. Touches [[On-device Learning]], [[Quantization]], [[Compression]], and [[Human Activity Recognition]].

**Sourcing note (methodology, this cycle):** cs.AR was swept via both its "recent" listing (which paginated cleanly through Tue 18 Aug) and monthly listing, giving full coverage of the 13–18 Aug window for that category. eess.SP's "recent" listing was retrieved and covered through Mon 17 Aug. cs.DC could only be retrieved via its monthly listing page, which — due to a caching/pagination limitation in this run's web-fetch tooling — repeatedly returned only the first 50 entries (early August) regardless of the requested page offset; deeper-month cs.DC entries (which is where the 13–20 Aug window would fall) could not be reliably retrieved this cycle. This is a genuine coverage gap for cs.DC this week, noted here rather than silently skipped. cs.LG was not swept directly (its volume make exhaustive review impractical in this run); candidates were instead surfaced via keyword search and via cross-listings surfaced from the cs.AR/eess.SP sweeps. The optional IEEE Xplore check was run (search UI reachable, "edge inference tinyml" query, sorted newest): results loaded but, as in prior cycles, could not be reliably date-filtered to a 7-day window — treated as inconclusive, no new entries drawn from it. ACM Digital Library was reached but blocked by an automated bot-verification page and could not be searched this cycle. Two targeted Google Scholar searches were run (SNN/edge-microcontroller quantized training; TEE/PIM/quantized-edge-LLM security) as cross-checks: neither surfaced additional corroborating or contradicting results for this week's picks, nor any missed papers — both searches returned only older or tangential prior art.

---

## 1. Lonic: Algorithm-Hardware Co-Design for Energy-Efficient Fully Local Online SNN Training with INT4 Precision

**Source:** arXiv:2608.12500 (cs.AR) — submitted 14 Aug 2026; accepted at ICCAD 2026
**Authors:** Peilin Chen, Xiaoxuan Yang
**Link:** https://arxiv.org/abs/2608.12500

**Why it matters:** Spiking neural networks are attractive for ultra-low-power edge learning, but prior temporally- and fully-local online SNN training algorithms have mostly been evaluated algorithmically, without checking whether their theoretical efficiency actually survives contact with real hardware. Lonic closes that gap with a full algorithm-hardware co-design, directly relevant to our [[On-device Learning]] line.

**Technical summary:** On the algorithm side, Lonic implements INT4 low-precision training for fully local online SNN learning while preserving accuracy. On the hardware side, it introduces reconfigurable multiplier-free integer PE arrays, a dual-optimization zero-gating strategy, a temporal prefix-accelerated local-learning dataflow, and low-precision weight movement. Compared to Apple M4 and Nvidia V100 GPUs, Lonic reports average energy-efficiency improvements of 17.44x and 66.28x respectively, with speedups of 3.25x and 1.02x; it also reports 15.95x (14.64x) energy (area) efficiency over ASIC TPU-like and H2Learn accelerators. Code is released on GitHub.

**Novelty assessment:** High. Most on-device/online SNN training work stops at the algorithm level or simulated efficiency estimates; pairing an INT4 local-learning algorithm with a matched multiplier-free integer datapath, and reporting gains against both commodity hardware (M4, V100) and prior specialized accelerators (TPU-like, H2Learn), gives this a stronger real-device grounding than most papers in this space. Code availability adds reproducibility value.

**Relevance score:** 5/5 — directly actionable for [[On-device Learning]] and [[Quantization]] (INT4); strongest deep-analysis candidate this week given the breadth of its comparison baselines and released code.

---

## 2. YAVIN: A Unified Architecture for Secure Edge Processing in Memory

**Source:** arXiv:2608.13496 (cs.AR) — submitted 13 Aug 2026
**Authors:** Shouzhi Fang, William C. Tegge, Md Omar Faruque, Peipei Zhou, Endadul Hoque, Alex K. Jones
**Link:** https://arxiv.org/abs/2608.13496

**Why it matters:** Processing-in-memory (PIM) reduces the Von Neumann bottleneck for edge inference, but conventional trusted execution environments (TEEs) only protect the processor, leaving the memory bus — and any PIM computation — outside the trust boundary. YAVIN is the first design we've tracked that extends a TEE's trust boundary into PIM itself, with results reported specifically for quantized edge-class LLM execution, making it a genuine edge-security/[[Quantization]] crossover rather than a purely academic security paper.

**Technical summary:** YAVIN establishes a unified trusted computing base spanning both processor execution and a dedicated, PIM-capable memory region, treating the memory bus itself as untrusted. It contributes the first PIM implementations of the LightSaber KEM post-quantum cryptosystem and ASCON-128 authenticated encryption, co-designed for efficient DRAM execution, plus a bit-sliced ordering scheme that limits temporary plaintext exposure during tensor workloads. Compared to the latest PIM AES implementation, YAVIN achieves over 20x speedup while incurring only 34% and 9.3% overhead when executing INT8 and INT32 quantized edge-class LLMs respectively, relative to unencrypted plaintext execution.

**Novelty assessment:** Moderate-to-high. Extending TEE trust into PIM (rather than treating PIM as inherently untrusted or out of scope) is a genuine architectural contribution, and grounding the overhead numbers specifically in quantized edge-LLM execution — rather than only synthetic cryptographic benchmarks — connects it directly to practical on-device LLM deployment concerns (privacy of prompts/weights during PIM-accelerated inference).

**Relevance score:** 4/5 — relevant to [[Quantization]]-adjacent edge-LLM deployment and a taxonomy gap noted below (secure/private on-device execution isn't currently a first-class taxonomy branch); worth tracking as edge LLM privacy becomes a more prominent concern.

---

## 3. FQTree: Fine-grained Quantization and Hardware Generation of Boosted Decision Trees

**Source:** arXiv:2608.12140 (cs.AR; cross-listed cs.LG) — submitted 13 Aug 2026; accepted at ASAP 2026
**Authors:** Zhiqiang Que, Chang Sun, Haiyang Wang, Dinesh Pamunuwa, Roshan Weerasekera, Qijia Tang, Bakhtiar Zadeh, Wayne Luk, Maria Spiropulu
**Link:** https://arxiv.org/abs/2608.12140

**Why it matters:** Almost all of our [[Quantization]] coverage to date has focused on neural networks; FQTree is a reminder that boosted decision trees (BDTs) — still widely used in latency-critical settings — face their own hardware-quantization problem, and that manually-tuned fixed-point formats for BDTs carry real accuracy/cost trade-offs worth systematizing.

**Technical summary:** FQTree performs fine-grained quantization-aware training of BDTs, paired with the QXGB framework for automatic hardware generation. It introduces a hardware-oriented leaf-value quantization scheme using a global quantization step plus a tree-wise shift, enabling compact non-negative integer leaf representations, controlled clipping/pruning, and bias folding to reduce datapath cost; quantization is applied during boosting itself so later trees adapt to the already-quantized ensemble's errors, and the trained model is lowered to low-latency hardware via a compiler-based flow. Code is available on GitHub.

**Novelty assessment:** Moderate. The core idea (quantization-aware boosting + automatic hardware lowering) is a sensible, well-engineered systematization of a problem that's usually handled ad hoc; the main novelty is in making the quantization boosting-aware (so later trees compensate for earlier quantization error) rather than quantizing a fully-trained ensemble post hoc.

**Relevance score:** 3/5 — relevant to [[Quantization]] and [[Compression]] as a non-neural data point, useful for benchmarking/teaching purposes, though decision-tree hardware is a narrower niche than our core neural-network-centric taxonomy.

---

## 4. One Residual with Three Reuses: A Wristband Front End for Gesture Sensing

**Source:** arXiv:2608.16542 (cs.LG; cross-listed cs.AR, cs.HC) — submitted 17 Aug 2026
**Authors:** Sam Rifaki
**Link:** https://arxiv.org/abs/2608.16542

**Why it matters:** A genuinely MCU-class (not GPU- or ASIC-class) contribution to our [[Human Activity Recognition]] branch: a design study for an always-on wristband front end that fuses IMU and 60GHz FMCW radar for gesture sensing and motor-symptom monitoring, built to fit inside a coin-cell power budget on a real, named edge MCU.

**Technical summary:** The paper shares a single on-chip residual generator across three functions — classifier wake-up gating, mmWave-vs-IMU sensor routing, and innovation-based EKF measurement reweighting — occupying just 14.4KB of program memory and 278B of state, running at 110K MACs/frame on an Ambiq Apollo4 Blue Plus class edge MCU. Across four public corpora (IPN Hand, SHREC 2021, MiliPoint 60GHz FMCW radar, EAT-Radar), it reaches detection probability 0.72–0.80 at a 1% false-alarm rate, cuts classifier-invocation energy by 47% at 90% gesture-detection recall, and lowers pose-tracking RMSE by 4.6x under measurement-bias drift versus an adaptive-Kalman-with-R-inflation baseline. The authors are explicit that this is a design study: measured silicon power and on-body capture are deferred to follow-on hardware work.

**Novelty assessment:** Moderate. Sharing one residual generator across three otherwise-separate functions (wake-up gating, sensor routing, and Kalman-filter reweighting) is an elegant resource-reuse idea well-suited to coin-cell-class MCUs, but the explicit caveat that silicon power and on-body validation are not yet measured tempers the strength of the efficiency claims — this is promising groundwork, not yet a validated deployed system.

**Relevance score:** 3/5 — good, genuinely MCU-class fit for [[Human Activity Recognition]] and wearable sensing, but single-author, pre-silicon, and not yet corroborated by hardware measurements; worth a light-touch watch rather than deep-analysis priority until follow-on hardware results appear.

---

## Candidates for deep analysis (`02_Papers/`)

No deep-analysis records were created automatically this cycle. In priority order:

- **#1 Lonic (arXiv:2608.12500)** — the strongest candidate: full algorithm-hardware co-design, code released, and comparisons against both commodity hardware and specialized prior accelerators give it the most checkable, reproducible claims of the four.
- **#2 YAVIN (arXiv:2608.13496)** — worth a deep record for the TEE-into-PIM architecture alone, particularly given growing interest in on-device LLM privacy; the quantized-edge-LLM overhead numbers are directly relevant to deployment-cost trade-off discussions.

## Suggested thesis / research hooks this week

- **Does INT4 local-learning generalize beyond SNNs?** Lonic's INT4 fully-local online training result is specific to spiking networks; is there a comparable multiplier-free, prefix-accelerated dataflow that would make INT4 (or lower) local on-device training viable for standard ANNs under the same energy budget? (Master's/PhD; [[On-device Learning]] × [[Quantization]].)
- **Trusted PIM as a prerequisite for on-device LLM privacy:** YAVIN's TEE-into-PIM extension is evaluated on quantized edge-class LLMs but treats "edge-class LLM" fairly generically. What does the overhead curve look like across the quantization spectrum (INT8/INT4/mixed-precision) our own [[Quantization]] work already tracks, and does trusted PIM change the accuracy/latency/security Pareto front for on-device LLM inference specifically on MCU/NPU-class (not just DRAM-PIM) targets? (PhD-scale; [[Quantization]] × security, a prospective taxonomy extension — see note below.)
- **Boosting-aware quantization beyond decision trees:** FQTree's core trick — making quantization aware of the training process (later boosting rounds compensate for earlier quantization error) rather than quantizing post hoc — parallels quantization-aware training (QAT) for neural nets, but is applied to an ensemble method with very different error dynamics. Is there a useful hybrid (e.g., boosted shallow NN ensembles) where this idea transfers directly? (Master's; [[Quantization]] × [[Compression]].)
- **From design study to silicon for wearable sensor fusion:** the wristband paper's shared-residual-generator idea is validated only on public corpora with no on-body or silicon-power measurements yet. A natural, well-scoped Master's project: port the shared generator to a real Ambiq Apollo4-class MCU, measure actual power under on-body conditions, and check whether the reported 47% energy reduction and 4.6x RMSE improvement survive real sensor noise. (Master's; [[Human Activity Recognition]].)

---

## Taxonomy note

YAVIN highlights a gap: secure/private on-device execution (TEEs, encrypted PIM, confidential computing for edge inference) doesn't map cleanly onto any existing taxonomy branch — it currently only loosely touches [[Quantization]] via its edge-LLM evaluation. As on-device LLM privacy becomes a more visible concern (this is the first paper we've tracked explicitly combining TEE/PIM security with quantized edge-LLM benchmarks), a dedicated "Edge AI Security / Trusted Execution" node under a taxonomy branch may be worth considering in a future refinement pass, distinct from the algorithmic Algorithms/Frameworks/Hardware/Applications structure. Flagging for consideration rather than creating it unilaterally this cycle.

---

**Notes:** All four scored papers are within the 13–17 Aug 2026 window and were verified at the abstract level from their arXiv pages; none has yet been read in full-PDF depth, so efficiency/latency/energy figures (Lonic's 17–66x energy-efficiency claims, YAVIN's 20x/34%/9.3% figures, FQTree's hardware-cost claims, and the wristband paper's 47%/4.6x figures) should be re-verified before citation in a survey or thesis. This cycle had a genuine cs.DC coverage gap: the monthly listing page could only be retrieved for its first ~50 (early-August) entries regardless of pagination offset, due to a tooling limitation, so the 13–20 Aug cs.DC window was not swept — this should be revisited next cycle, ideally with a different retrieval method (e.g., arXiv's export API or "recent" listing pagination, if reachable) rather than the monthly-listing page. cs.LG was not swept directly given its volume; the one cs.LG-classified pick this week (the wristband paper) was surfaced via its cs.AR/cs.HC cross-listing rather than a direct cs.LG sweep — this remains a standing coverage caveat noted in prior digests too. IEEE Xplore was reached and searched but, as in prior cycles, could not be reliably date-filtered to confirm a 7-day window, so it contributed no new entries. ACM Digital Library was reached but blocked by an automated bot-verification challenge page this cycle and could not be searched at all (a regression from being merely "not checked" in some prior weeks). Two targeted Google Scholar searches were run as cross-checks and neither surfaced additional relevant results nor contradicted this week's picks. `sources.yaml` `last_checked` for arXiv should be advanced to 2026-08-20 (partial coverage caveat for cs.DC and cs.LG noted above).
