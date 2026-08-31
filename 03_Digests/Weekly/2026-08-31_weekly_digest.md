# Weekly Digest — 2026-08-31

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Four papers selected this cycle, submitted 22–26 Aug 2026. Note on cadence: the previous digest (2026-08-23) covered submissions through 20 Aug, so this cycle's effective window is 21–31 Aug 2026 (11 days, bridging a one-week gap in the digest schedule) rather than the usual 7. Picks span workload-characterization methodology for edge LLM serving, a streaming FPGA vision accelerator, an on-device NPU measurement study, and a wireless systems/communications co-design for distributed MoE inference. Touches [[Quantization]], [[Vision]], [[NPU]], and [[FPGA]], and reinforces the still-open "edge LLM serving infrastructure" taxonomy gap flagged in prior digests (see Taxonomy note below).

**Sourcing note (methodology, this cycle):** cs.AR was retrieved via its "recent" listing, which this cycle covered Mon 31 – Tue 25 Aug 2026 (49 entries, full clean coverage of that span) — but arXiv's "recent" view only surfaces the most recent five posting days, so Fri 21 – Mon 24 Aug was not reached and is a coverage gap for cs.AR this cycle. eess.SP's "recent" listing gave full coverage of Wed 26 Aug (16 entries) and near-full coverage of Tue 25 Aug (34 of 37 entries), but a pagination/caching issue with the fetch tool prevented reaching Mon 24 Aug and earlier. cs.DC could not be swept directly this cycle: the fetch tool repeatedly returned page 1 of the monthly listing regardless of the requested pagination offset, so no direct cs.DC sweep was completed; candidates were instead surfaced via cs.AR/eess.SP cross-listings (Hydra, pick #1 below, is cross-listed to cs.DC). cs.LG was not swept directly given its volume, a standing caveat across cycles; candidates were surfaced only via cross-listings from the cs.AR/eess.SP sweeps. The optional IEEE Xplore, ACM Digital Library, and Google Scholar checks via Claude in Chrome could not run this cycle — browser navigation to all three sites was denied/blocked in this unattended run (no user present on unige.it institutional access or to grant per-site browser approval); this is a more complete block than in past cycles, where at least one of the three was reachable. No entries were drawn from those sources this cycle.

---

## 1. Hydra: Phase-Aware Workload Characterization of LLM Inference across Edge SoC Generations, Backends, and Quantization Levels

**Source:** arXiv:2608.25053 (cs.AR; cross-listed cs.AI, cs.DC, cs.PF) — submitted 25 Aug 2026; accepted at IEEE IISWC 2026
**Authors:** Amir Taherin, Sana Taghipour Anvari, Charles Amante, Yixiao Chen, Ruben Noroian, Zlatan Feric, Nicolas Bohm Agostini, Pu Zhao, José Cano, Bin Ren, Yanzhi Wang, David Kaeli
**Link:** https://arxiv.org/abs/2608.25053

**Why it matters:** Directly targets a gap this Observatory has flagged in recent digests — the lack of standardized, reproducible methodology for characterizing edge LLM inference across hardware generations and backends. Hydra instruments HuggingFace Transformers and llama.cpp with a shared per-prompt timing schema fused with hardware telemetry, evaluated across three consecutive NVIDIA Jetson AGX generations (Xavier, Orin, Thor). The author list (Kaeli, Yanzhi Wang, Zlatan Feric) overlaps with the group behind last week's edge-RAG compression paper, suggesting a sustained research thread on edge LLM deployment measurement.

**Technical summary:** Hydra characterizes 13 instruction-tuned LLMs from seven families across five execution formats (including multiple quantization levels), separating prefill and decode phases and connecting phase-level timing to system-resource utilization and efficiency metrics. The released artifact contains ~107K per-prompt records, publicly available with the framework's source code. Key finding: aggregate latency hides deployment-relevant effects — inference-backend structure changes *where* latency is introduced, [[Quantization]] reduces memory traffic and energy but does not predict power draw monotonically, and SoC generation changes how utilization/efficiency figures should even be interpreted.

**Novelty assessment:** High as a methodology and open-artifact contribution. It is not a new model or algorithm but a standardized, reproducible measurement framework — exactly the kind of infrastructure this Observatory's philosophy values (traceable, reusable knowledge) — and the non-monotonic quantization/power finding is a genuinely useful empirical result that complicates simple "lower precision = lower power" assumptions.

**Relevance score:** 5/5 — strongest deep-analysis candidate this week: open-source artifact and data (107K records), fills a previously flagged taxonomy/methodology gap, and produces a citable, non-obvious empirical finding about quantization's relationship to power.

---

## 2. SweepLSD: A One-Pass, O(width)-Memory Line Segment Detector with an Integer-Only Streaming Core and a Real-Time FPGA Realization

**Source:** arXiv:2608.22086 (eess.IV; cross-listed cs.AR, cs.CV) — submitted late Aug 2026
**Authors:** Yoshiyasu Shimizu
**Link:** https://arxiv.org/abs/2608.22086

**Why it matters:** A concrete [[Vision]] × [[Quantization]] × [[FPGA]] data point: a line-segment detector designed from the ground up for streaming, memory-constrained embedded deployment rather than adapted post-hoc from a GPU-oriented design. The one-pass, O(width)-memory design directly targets the SRAM/BRAM constraints that make many vision algorithms impractical on FPGA-class edge hardware.

**Technical summary:** SweepLSD processes image data in a single streaming pass with memory scaling only with image width (not full-frame buffering), using an integer-only computational core suited to FPGA fixed-point logic, and demonstrates a real-time FPGA realization. Code, benchmarks, and evaluation harnesses are openly released (MIT license).

**Novelty assessment:** Moderate-to-high. Line segment detection is a well-studied problem, but the combination of strict O(width) memory bounds, an integer-only streaming core, and a real, real-time FPGA implementation (rather than a GPU baseline or simulation) is a solid, verifiable embedded-systems contribution with an open, reproducible release.

**Relevance score:** 4/5 — good deep-analysis candidate for the [[Vision]] branch: open code, real hardware realization, and a memory-efficiency angle relevant to resource-constrained edge deployment generally, not just this one algorithm.

---

## 3. What Actually Runs: A Measurement Study of Language Model Placement and Decode Speed on the Apple Neural Engine

**Source:** arXiv:2608.22110 (cs.LG; cross-listed cs.AR, cs.PF) — submitted 22 Aug 2026
**Author:** Shahir M A
**Link:** https://arxiv.org/abs/2608.22110

**Why it matters:** A rigorous, independently-run measurement study of a widely-deployed consumer [[NPU]] (Apple's Neural Engine) that most researchers treat as a black box. It directly informs [[Quantization]] × Hardware questions our lab cares about: which operator formulations and weight encodings actually get accelerator placement, versus silently falling back to CPU.

**Technical summary:** Combines three independent measurement paths — a 64-shape sweep of LLM primitives recording per-operation device eligibility, matched models trained across size/precision with byte-identical quantized/fp16 structure, and direct reads of the ANE's memory-controller byte counters during inference — to establish what actually executes on-accelerator rather than what the compiler intends. Central finding: accelerator placement is a property of *how* a computation is expressed, not what it computes (a fused RMSNorm is ANE-eligible; its arithmetically identical decomposition is CPU-only), and weight encoding gates residency (an fp16 conv-heavy model runs entirely on CPU while its int8/2-bit versions reach ~83% ANE residency and run 1.8–2.2× faster). The smallest, fastest models measured are ternary (25M-parameter half-attention ternary model: 10.5 MB, 0.63 ms/token). Code, harnesses, and run ledgers are openly released.

**Novelty assessment:** High for rigor and actionability, despite being single-authored. The methodology (three independent, cross-validated measurement paths) is unusually careful for a hardware-measurement paper, and the "expression, not computation, gates placement" finding is a genuinely non-obvious, practically important result for anyone deploying quantized models on Apple silicon.

**Relevance score:** 4/5 — strong candidate for the [[NPU]] branch of the Hardware taxonomy; open code and a clear, falsifiable design procedure ("choose the encoding first, then spend the byte budget on parameters") make it directly actionable for future on-device deployment work.

---

## 4. AirMoE: Realizing Over-the-Air Distributed Mixture-of-Experts Inference at the Wireless Edge

**Source:** arXiv:2608.22932 (eess.SP) — submitted 24 Aug 2026, revised 26 Aug 2026
**Authors:** Huiling Yang, Zhanwei Wang, Kaibin Huang
**Link:** https://arxiv.org/abs/2608.22932

**Why it matters:** Extends distributed MoE-LLM inference at the wireless edge from a pure systems/scheduling problem into a joint communications-and-computing co-design, using over-the-air computing (AirComp) to aggregate expert outputs via simultaneous wireless waveform superposition instead of sequential uplink transmissions. This is a distinct angle from the edge-native MoE serving systems covered in recent digests (e.g., FreeToken) — here the bottleneck and the fix are both at the physical/wireless layer, not the memory/compute layer.

**Technical summary:** Proposes an inference-aware AirMoE error metric quantifying how AirComp aggregation distortion propagates to end-to-end inference accuracy, via perturbation-based layer-sensitivity calibration. Decomposes the resulting joint optimization into a two-timescale framework: a fast-timescale, provably globally-optimal threshold-based power-control policy, and a slow-timescale activation- and channel-aware expert-placement strategy that assigns higher-importance experts to devices with lower channel-power cost. Reports accuracy gains over baselines, especially under strong device heterogeneity.

**Novelty assessment:** Moderate-to-high as a systems/communications co-design — AirComp itself is an established over-the-air aggregation technique (more familiar from federated learning gradient aggregation), but its application to MoE expert-output aggregation with a bespoke inference-aware distortion metric and provably-optimal power control is a new combination.

**Relevance score:** 3/5 — a genuinely novel angle bridging Compression/serving concerns and the physical wireless layer, but the contribution is theoretical/simulation-based (no real radio hardware deployment reported) and is somewhat adjacent to the Observatory's usual embedded/TinyML focus.

---

## Candidates for deep analysis (`02_Papers/`)

No deep-analysis records were created automatically this cycle. In priority order:

- **#1 Hydra (arXiv:2608.25053)** — the strongest candidate: open-source measurement framework and 107K-record dataset directly addressing our flagged "edge LLM serving infrastructure" methodology gap, with a citable non-monotonic quantization/power finding.
- **#3 Apple ANE measurement study (arXiv:2608.22110)** — worth a deep record for the [[NPU]] branch: rigorous triple-measurement methodology, open code, and a directly actionable design procedure for quantized on-device deployment.
- **#2 SweepLSD (arXiv:2608.22086)** — worth a deep record for the [[Vision]] branch: real FPGA realization, open code, and a memory-efficiency framing (O(width)) that could generalize beyond line detection.

## Suggested thesis / research hooks this week

- **From Jetson-class to MCU-class workload characterization:** Hydra's methodology (shared timing schema + hardware telemetry fusion) is built for Jetson AGX-class SoCs (GPU + accelerator). Would the same phase-aware characterization approach transfer to genuinely MCU-class hardware ([[Cortex-M]], [[NPU]] micro-accelerators), where prefill/decode phases and even the models themselves look very different? A well-scoped Master's-level replication/extension study.
- **Does "expression gates placement" hold beyond Apple silicon?** The ANE paper's central finding — that operator *formulation*, not just precision, determines accelerator eligibility — is plausible for other NPUs (Arm Ethos, [[Cortex-M]] NPU extensions) but untested there. A comparative measurement study across 2–3 commodity NPUs would be a strong PhD-scale systems contribution and would directly extend this paper's methodology.
- **Generalizing O(width)-memory streaming beyond line detection:** SweepLSD's one-pass, width-bounded memory design is specific to line segment detection, but the underlying streaming-memory discipline could plausibly generalize to other structured vision primitives (edge/corner detection, simple pose primitives) relevant to [[Keyword_Spotting|Keyword Spotting]]-adjacent always-on vision use cases. A Master's-scale generalization study.
- **AirComp for edge inference vs. edge training:** AirMoE applies over-the-air aggregation to MoE expert-output aggregation at inference time; the same physical-layer aggregation trick is already used for gradient aggregation in over-the-air [[Federated Learning]]. Is there a unified framework connecting AirComp-for-training and AirComp-for-inference, and would AirMoE's layer-sensitivity calibration technique improve over-the-air FL gradient aggregation too? A PhD-scale question bridging Signal Processing and [[Federated Learning]].

---

## Taxonomy note

The cs.DC sweep failed entirely this cycle due to a tool-level pagination/caching issue (the fetch tool returned the first page of the monthly listing regardless of the requested offset) rather than a source-access problem — this should be retried with a different retrieval method (e.g., the arXiv API's date-range query, or the "recent" view instead of the monthly view) next cycle, since cs.DC is where a meaningful share of edge-serving/MoE papers has been surfacing recently (e.g., Hydra's cs.DC cross-listing, and last week's FreeToken). Separately, the "edge LLM serving infrastructure" taxonomy gap flagged in the 2026-08-20 and 2026-08-23 digests remains open and is reinforced by three of this week's four picks (Hydra, the Apple ANE study, and AirMoE all concern *how* models get deployed and executed rather than new model/compression algorithms) — still flagging for consideration rather than creating a new taxonomy node unilaterally.

---

**Notes:** All four scored papers fall in the 22–26 Aug 2026 range and were verified at the abstract level from their arXiv pages; none has yet been read in full-PDF depth, so the specific figures cited here (Hydra's ~107K records and three-SoC-generation scope; SweepLSD's O(width) memory claim and FPGA realization; the ANE paper's 1.8–2.2× speedup, ~83%/98.9% residency figures, and 10.5 MB/0.63 ms ternary-model numbers; AirMoE's claimed accuracy gains under device heterogeneity) should be re-verified before citation in a survey or thesis. cs.AR had full clean coverage of 25–31 Aug but a gap for 21–24 Aug (arXiv's "recent" view only shows five posting days). eess.SP had full/near-full coverage of 25–26 Aug but a gap for 24 Aug and earlier due to a fetch-tool pagination issue. cs.DC could not be swept directly this cycle (tool pagination bug, see Taxonomy note); cs.LG was not swept directly given its volume, a standing caveat. The optional IEEE Xplore, ACM Digital Library, and Google Scholar checks via Claude in Chrome could not run this cycle — all three site navigations were denied/blocked in this unattended run. `sources.yaml` `last_checked` for arXiv should be advanced to 2026-08-31, with the coverage gaps above noted for the next cycle.
