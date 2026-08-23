# Weekly Digest — 2026-08-23

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Five papers selected this week, submitted 17–20 Aug 2026 (the window since the last digest, 2026-08-20, whose covered window ran through 17 Aug). cs.AR was swept in full for the entire window this cycle with no gaps. This week's picks span five different corners of the taxonomy rather than clustering on one theme: a custom ASIC for event-driven graph-neural-network vision, a full-stack edge-native MoE LLM serving system, a resource-efficient EEG-decoding ASIC, an empirical study of adaptive context compression for edge-device RAG, and an FPGA visual-inspection accelerator using FFT-domain quantization. Touches [[Vision]], [[Quantization]], [[Compression]], [[Biosignals]], and [[Industrial IoT]], plus flags a recurring taxonomy gap around edge/on-device LLM serving infrastructure (see note below).

**Sourcing note (methodology, this cycle):** cs.AR was retrieved via its "recent" listing, which covers Mon 17 – Fri 21 Aug 2026 (43 entries) with full coverage and no gaps — a clean sweep this cycle. eess.SP's "recent" listing was retrieved and gave full coverage of Fri 21 Aug (22 entries) and Thu 20 Aug (14 entries), plus a partial first page of Wed 19 Aug (14 of 21 entries); Tue 18 and Mon 17 Aug were not retrieved this cycle due to the single-page fetch limit, a partial-coverage caveat similar to prior weeks. cs.DC's "recent" listing was retrieved and gave full coverage of Fri 21 Aug (11), Thu 20 Aug (12), and Wed 19 Aug (11), plus a partial first page of Tue 18 Aug (16 of 41 entries); Mon 17 Aug and the remainder of Tue 18 were not retrieved — still an improvement over last week's total cs.DC gap. cs.LG was not swept directly given its volume (a standing caveat across cycles); candidates were surfaced only via cross-listings from the cs.AR/eess.SP/cs.DC sweeps. The optional IEEE Xplore check was run via Claude in Chrome: the search UI was reachable but not signed in with unige.it institutional access this cycle (this is an unattended scheduled run, so Ricky was not on the campus network/VPN to authenticate), and results still cannot be reliably date-filtered to a 7-day window (only publication year is shown) — treated as inconclusive, no entries drawn from it. ACM Digital Library was reached but blocked by a Cloudflare bot-verification challenge page again this cycle and could not be searched (consistent with recent weeks). Two targeted Google Scholar searches were run as cross-checks: a search for "event-driven graph neural network processor edge vision 2026" surfaced one relevant piece of prior art — an FPGA-based event-driven GNN accelerator for edge vision (T. Liu et al., ~April 2026, IEEE, 1 citation) — which sharpens the novelty framing for pick #1 below; a search for "edge-native mixture-of-experts MoE serving personal machine" returned no results, most likely because pick #2 is too recent to be indexed yet. Neither search surfaced anything contradicting this week's picks.

---

## 1. ETHEREAL: A 25.6-μs/inf. Low-latency Event-driven Graph-neural-network Processor for High-resolution Vision at the Edge

**Source:** arXiv:2608.17787 (cs.AR; cross-listed cs.CV) — submitted 18 Aug 2026; submitted to IEEE JSSC
**Authors:** Adrian Kneip, Martin Lefebvre, Daniel Gehrig, Victoria Catalán Pastor, Davide Scaramuzza, Marian Verhelst, Charlotte Frenkel
**Link:** https://arxiv.org/abs/2608.17787

**Why it matters:** Dynamic vision sensors (event cameras) offer μs-level temporal resolution well suited to sub-ms edge-vision latency targets, and event-driven graph neural networks (EV-GNNs) are an accurate, efficient algorithmic match for their sparse, irregular event streams — but until now no dedicated hardware existed to handle EV-GNNs' mixed dense-regular/sparse-irregular access pattern. ETHEREAL is the first EV-GNN processor chip, closing that algorithm-hardware gap directly in our [[Vision]] branch. The author list combines leading edge-AI hardware groups (Verhelst, Frenkel) with event-vision/robotics expertise (Scaramuzza, Gehrig).

**Technical summary:** ETHEREAL introduces a neighbor-parallel spline-convolution engine combined with a split 2D/3D memory hierarchy featuring a novel spatiotemporal event-caching mechanism, purpose-built for EV-GNN inference. Measured (silicon, not simulated) results on the state-of-the-art DAGr-GNN workload and the VGA-resolution (640×480) DSEC event-vision dataset show 25.6μs latency and 1.6μJ energy per end-to-end event-wise inference.

**Novelty assessment:** High. A Google Scholar cross-check surfaced one piece of related prior art — an FPGA-based event-driven GNN accelerator for edge vision (T. Liu et al., ~April 2026) — so ETHEREAL is not the first system to target this problem space, but it appears to be the first full custom-ASIC implementation with real silicon measurements (rather than FPGA emulation), which is a meaningfully stronger efficiency and reproducibility claim.

**Relevance score:** 5/5 — strongest deep-analysis candidate this week: real silicon, a genuinely novel hardware class (EV-GNN processor), high-caliber authorship, and a direct fit for [[Vision]] × Hardware.

---

## 2. FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution

**Source:** arXiv:2608.16157 (cs.DC) — submitted 17 Aug 2026; system released at flashml.ai
**Authors:** Shuo Yang, Xiaoze Fan, Melissa Pan, Haocheng Xi, Zhe Wang, Shanlin Sun, Kurt Keutzer, Song Han, Matei Zaharia, Chenfeng Xu, Ion Stoica
**Link:** https://arxiv.org/abs/2608.16157

**Why it matters:** This paper was submitted 17 Aug 2026 — technically inside last week's nominal 13–17 Aug window, but missed at the time because of that cycle's total cs.DC coverage gap. It is being picked up and flagged explicitly this week rather than silently skipped. FreeToken tackles the systems/serving side of on-device LLM deployment: treating a personal machine (laptop or workstation GPU) as an elastic inference platform for frontier-scale open-weight MoE models, rather than a scaled-down datacenter GPU. The author list (Song Han, Ion Stoica, Matei Zaharia, Kurt Keutzer) gives it unusually strong systems and efficient-ML pedigree.

**Technical summary:** FreeToken co-designs model layout/loading, expert residency, CPU–GPU execution split, agentic state reuse, and runtime memory management, continuously remapping computation and model state onto whatever heterogeneous resources are actually available rather than committing to a fixed offloading strategy. It supports 20+ MoE models and real coding/tool-using agent workloads on hardware ranging from an 8GB laptop GPU to a single workstation GPU, scaling from a 35B model on a laptop to a 284B model on a gaming desktop and a 753B model (GLM-5.2) on a single workstation GPU. The system is openly released.

**Novelty assessment:** High as a systems contribution — bandwidth-adaptive, workload-aware dynamic offloading (versus the static, offline-tuned offloading typical of prior local-LLM serving work), demonstrated at unusually large model scales for consumer/prosumer hardware, with an open release.

**Relevance score:** 4/5 — sits at the boundary of the Observatory's usual embedded/TinyML focus (laptop/workstation GPUs, not MCU/NPU-class devices), but directly relevant to the fast-growing on-device/local-LLM deployment trend and to the "edge LLM serving" taxonomy gap flagged in recent digests.

---

## 3. A Resource-Efficient CNN-Based EEG Auditory Attention Decoding ASIC

**Source:** arXiv:2608.20198 (cs.AR; cross-listed eess.SP) — submitted 20 Aug 2026; accepted at BioCAS 2026
**Authors:** Qier Ma, Richard George, Stefan Scholze, Jehn Constantin, Tobias Reichenbach, Christian Mayr
**Link:** https://arxiv.org/abs/2608.20198

**Why it matters:** Addresses the "cocktail party problem" for cochlear-implant users — following a target speaker in a noisy environment — via real-time EEG-based auditory attention decoding, a clinically motivated [[Biosignals]] task. A resource-efficient, fully-implemented ASIC (not a simulation or FPGA prototype) makes this a concrete Hardware × [[Quantization]] × [[Biosignals]] data point.

**Technical summary:** Integrates a quantized CNN inference engine with a Pearson-correlation classifier, using streaming execution, on-chip buffering, and a memory-efficient dataflow to minimize hardware cost while sustaining real-time performance. Fully implemented in GF22FDX 22nm CMOS: 2.09mm² total silicon area (the CNN inference engine and streaming classifier together need only 0.076mm²), 0.55V core voltage, 0.4941mW power, and 7.34ms inference latency.

**Novelty assessment:** Moderate-to-high. The contribution is less a new algorithm than a tightly engineered, fully-taped-out silicon implementation of quantized CNN + correlation-based AAD; the achieved area/power envelope is small enough for realistic integration into hearing-assistance or cochlear-implant hardware, which is the paper's main practical value.

**Relevance score:** 4/5 — strong deep-analysis candidate for the [[Biosignals]] branch given real silicon numbers and a clear clinical use case.

---

## 4. From Retrieved Context to Runtime Control: Adaptive Compression for Edge-based RAG

**Source:** arXiv:2608.19535 (cs.AI; cross-listed cs.DC, cs.CL, cs.IR, cs.PF) — submitted 20 Aug 2026; accepted at the ACM AI Leadership Summit 2026
**Authors:** Zlatan Feric, Amir Taherin, Yanzhi Wang, David Kaeli
**Link:** https://arxiv.org/abs/2608.19535

**Why it matters:** The first paper we've tracked to empirically characterize the RAG-on-edge-SoC latency/energy tradeoff and argue for telemetry-driven adaptive context compression rather than a fixed, offline-tuned compression rate. It extends [[Compression]] to a workload class the Observatory hasn't covered before — compressing *retrieved context* for edge LLM inference, rather than compressing model weights or activations.

**Technical summary:** Characterizes the compression tradeoff on an NVIDIA Jetson AGX Thor edge SoC using Llama and Qwen generators, the Natural Questions and HotpotQA datasets, and LLMLingua-2 compression. Generation dominates the RAG latency/energy budget for larger (7B–8B) generators (~90% of per-query latency, ~91% of GPU energy). The compression rate has an "adaptive operating region": mild compression leaves energy savings on the table, while overly aggressive compression degrades answer quality; an intermediate compression rate cuts GPU energy by up to 53.2% and whole-SoC energy by up to 48.2% with negligible quality loss. The paper argues for — but does not yet implement — runtime policies that adapt compression dynamically using workload features and edge telemetry.

**Novelty assessment:** Moderate. The empirical characterization on real edge-SoC hardware is solid and directly actionable, but the adaptive/telemetry-driven controller itself is presented as a vision for future work rather than an implemented and evaluated system.

**Relevance score:** 4/5 — a genuinely new angle for [[Compression]] (retrieved-context compression for edge RAG) with real hardware measurements; the open telemetry-controller design is a natural next-step research gap.

---

## 5. Energy-Efficient Visual Inspection with FFT-Based CNNs and Adaptive Floating-Point Quantization

**Source:** arXiv:2608.19837 (cs.AR) — submitted 20 Aug 2026; accepted at ISOCC 2026
**Authors:** Lukas Krupp, Marco Groß, Michael Graichen, Kim Ulrich, Norbert Wehn
**Link:** https://arxiv.org/abs/2608.19837

**Why it matters:** A concrete [[Quantization]] × [[Industrial IoT]] × [[Vision]] data point: an FFT-domain CNN accelerator for industrial visual inspection, evaluated on a real industrial fault-detection dataset rather than a generic vision benchmark.

**Technical summary:** Combines FFT-based convolution (via serial radix-2² SDF FFT modules) with adaptive post-training FP8 quantization on an industrial CPU-FPGA platform, comparing two FPGA-oriented bias-optimization strategies: progressive bias adjustment (PBA) within the FFT itself, versus layer-wise exponent-bias selection across the CNN. Layer-wise bias optimization raises accuracy from 80.33% to 84.13% without widening the datapath. Implemented as a LeNet-5 accelerator; the FPGA achieves roughly 2.5× higher energy efficiency than CPU-only inference.

**Novelty assessment:** Moderate. The core contribution is a careful empirical comparison of two FP8 bias-optimization strategies for FFT-domain CNN inference rather than a fundamentally new quantization scheme, but it is a useful, well-executed industrial data point.

**Relevance score:** 3/5 — solid engineering relevant to [[Quantization]] and [[Industrial IoT]], narrower novelty than this week's top picks.

---

## Candidates for deep analysis (`02_Papers/`)

No deep-analysis records were created automatically this cycle. In priority order:

- **#1 ETHEREAL (arXiv:2608.17787)** — the strongest candidate: first EV-GNN ASIC, real silicon measurements, high-caliber authorship, and a genuinely new hardware class for the [[Vision]] branch.
- **#3 EEG AAD ASIC (arXiv:2608.20198)** — worth a deep record for the [[Biosignals]] branch: fully-taped-out silicon with a clear clinical use case (cochlear implants) and strong area/power efficiency numbers.
- **#2 FreeToken (arXiv:2608.16157)** — worth a deep record given its unusually strong authorship, open release, and relevance to the on-device/local-LLM serving trend, though note it sits at the edge of our usual MCU/NPU-class scope (laptop/workstation GPUs here, not embedded devices).

## Suggested thesis / research hooks this week

- **Event-driven GNN accelerators beyond vision:** ETHEREAL's neighbor-parallel spline-convolution engine and spatiotemporal event-caching are built for DVS event-vision streams — would the same architecture transfer to other genuinely sparse, irregular event streams (biosignal spike trains, sparse radar point clouds)? A PhD-scale hardware-architecture question spanning [[Vision]] and [[Biosignals]].
- **Where does "edge-native LLM serving" stop being edge?** FreeToken's smallest target is an 8GB laptop GPU, well above MCU/NPU-class embedded hardware. Is there a principled boundary between "edge-native" MoE serving (laptop/workstation-scale) and genuine TinyML on-device inference, and does FreeToken's bandwidth-adaptive execution idea degrade gracefully as it scales down toward embedded targets? Master's/PhD scoping study.
- **Closing the loop on adaptive edge-RAG compression:** the edge-RAG paper characterizes the compression/energy/quality tradeoff in detail but explicitly leaves the telemetry-driven runtime controller as future work. A well-scoped Master's project: implement and evaluate a closed-loop controller that adapts LLMLingua-2 compression rate to live edge-SoC telemetry, using the paper's own operating-region data as a starting point. [[Compression]].
- **A common quantization-robustness principle for small streaming CNN classifiers?** The EEG AAD ASIC and the FFT-CNN visual-inspection accelerator both quantize small, real-time, streaming CNN classifiers on real hardware, but in very different application domains (biosignals vs. industrial vision) and different arithmetic formats (fixed-point classifier vs. FP8 FFT-domain). Is there a shared quantization-sensitivity pattern across these two "small streaming CNN" use cases worth documenting on the [[Quantization]] concept page, or are the domains different enough that they should stay separate? Master's-scale comparative study.

---

## Taxonomy note

Two papers this week (FreeToken and the edge-RAG compression study) are systems/serving papers about deploying large models — MoE LLMs and RAG pipelines — on personal or edge hardware, rather than papers proposing a new compression/quantization *algorithm*. This reinforces a gap flagged in a prior digest (2026-08-20, re: TEE/PIM security): on-device/edge LLM *serving infrastructure* doesn't map cleanly onto the current Algorithms/Frameworks/Hardware/Applications taxonomy. It is adjacent to [[Compression]] (FreeToken performs no explicit compression; the RAG paper compresses retrieved context, not weights) but distinct from it. As on-device LLM deployment continues to show up in the weekly sweep, a dedicated "Edge LLM Serving / Local Inference Systems" taxonomy node may be worth considering in a future refinement pass — flagging for consideration rather than creating it unilaterally this cycle, consistent with the still-open Edge AI Security gap noted last week.

---

**Notes:** All five scored papers are within the 17–20 Aug 2026 window (FreeToken's 17 Aug submission was recovered from a gap in last cycle's cs.DC coverage, as noted above) and were verified at the abstract level from their arXiv pages; none has yet been read in full-PDF depth, so the efficiency/latency/energy figures cited here (ETHEREAL's 25.6μs/1.6μJ, FreeToken's model-scale claims, the EEG ASIC's 0.4941mW/7.34ms, the edge-RAG paper's 53.2%/48.2% energy reductions, and the FFT-CNN accelerator's 2.5× efficiency and 80.33%→84.13% accuracy figures) should be re-verified before citation in a survey or thesis. cs.AR had full clean coverage of the window this cycle; eess.SP and cs.DC each had a partial-coverage caveat (see Sourcing note above) that should be revisited next cycle if a different retrieval method becomes available. cs.LG was not swept directly given its volume, a standing caveat across cycles. IEEE Xplore was reached via Claude in Chrome but not authenticated with unige.it institutional access this cycle (unattended run), and its results still cannot be reliably date-filtered — treated as inconclusive. ACM Digital Library was blocked by a Cloudflare bot-verification challenge again and could not be searched. Two targeted Google Scholar searches were run as cross-checks; one surfaced useful novelty context for pick #1 (noted above), the other returned no results. `sources.yaml` `last_checked` for arXiv should be advanced to 2026-08-23 (partial-coverage caveats for eess.SP and cs.DC noted above).
