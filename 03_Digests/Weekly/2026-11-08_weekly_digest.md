# Weekly Digest — 2026-11-08

This digest covers roughly two weeks (the 1 November cycle did not produce a digest, so the window runs from the 25 October digest to 6 November 2026). The strongest item is a measured benchmark of ten sub-watt edge devices that argues MAC count is a misleading cost proxy for microcontroller-class accelerators, which lines up directly with the Observatory's open MCU/NPU toolchain thread. A hardware-aware NAS for optical flow on an Ethos-U55 microcontroller, an energy crossover study for federated keyword spotting on an ESP32-S3, and a sensor-side hardwired BNN complete the selection. Touches [[NPU]], [[Cortex-M]], [[NAS]], [[Federated_Learning]], [[Keyword_Spotting]], [[FPGA]] and [[Vision]].

Selection used arXiv abstract pages (three of four fetched; one was rate-limited), arXiv cs.AR and cs.LG recent listings, and Google Scholar snippets. No full text was read for any item.

---

## 1. TinyML Hits the Memory Wall: A Benchmark of Ten Sub-Watt Edge Devices

**Source:** arXiv:2611.03392 (cs.AR) — submitted 2 Nov 2026. Also surfaced in Scholar (date-sorted).
**Authors:** Pietro Bonazzi, Luigi Capogrosso, Ahmet Celik, Rosanna Manzo, Marco Giordano, Szymon Ruciński, Jonathan Hungerbuehler, Michele Magno
**Link:** https://arxiv.org/abs/2611.03392

**Why it matters:** Cross-device, measured-energy comparisons on commercial MCUs with and without NPUs are rare, and this one includes four devices new to such comparisons. Its central claim, that accelerator latency tracks memory traffic rather than MAC count, goes to the heart of how [[NPU]] and [[Cortex-M]] deployments should be reasoned about and evaluated.

**Technical summary:** Ten sub-watt devices (an in-sensor DSP, four MCUs with an NPU, five MCUs without one) run four CNNs (MobileNetV3, MCUNetV1, EfficientNet, SqueezeNet) and two tiny transformers (MobileViT-XXS, DeiT-tiny), with energy measured above idle for a common basis. Reported: the Sony IMX500 uses 1.3–3x less energy than the STM32N6 on every model; GAP9 is most efficient on MobileNetV3 and the Alif E7 on MCUNetV1 and SqueezeNet; the four accelerators use 6–34x less energy than the STM32V8; the Alif E7 and IMX500 form the Pareto front. The NPU advantage over a 1 GHz Cortex-M85 grows with workload intensity, from 1.4x (MCUNetV1) to 8.2x (SqueezeNet). The authors conclude MAC count is a misleading cost proxy for sub-watt accelerators.

**Novelty assessment:** Moderate-to-high as an empirical contribution: the methodology is standard but the device coverage and common-basis energy accounting are uncommon. The abstract page is truncated, no code or dataset link is listed, and the results are single-group measurements. Read at abstract level only.

**Relevance score:** 5/5 — measured, multi-device, on the Observatory's core tier; directly relevant to the measurement and toolchain questions already open.

---

## 2. MCUFlowNet: Hardware-Aware Neural Architecture Search for Optical Flow on Microcontrollers

**Source:** arXiv:2611.08147 (cs.CV; cross-listed cs.AR) — submitted 5 Nov 2026.
**Authors:** Enmin Lin, Jona Beysens
**Link:** https://arxiv.org/abs/2611.08147
**Code:** https://gitlab.kuleuven.be/emedia-research-lab/esat-stadius/mcuflownet/mcuflownet

**Why it matters:** Optical flow is rarely addressed on microcontrollers, and this work targets an Ethos-U55 board for drone obstacle avoidance. It also shows a [[NAS]] design in which peak SRAM is fixed by the macro stage and the search optimizes compiler-estimated latency, removing the need for an explicit memory constraint. Relevant to [[Vision]] and to robotics deployments on [[NPU]]-equipped MCUs.

**Technical summary:** PACE-NAS is a two-level search: a macro stage fixes the backbone and peak SRAM usage; a micro stage searches operators and depths to balance accuracy and compiler-estimated latency. Applied to EdgeFlowNet on a Grove Vision AI V2 board (Ethos-U55), profiling located peak SRAM at the full-resolution output head; replacing transposed convolutions with bilinear upsampling plus convolution cuts peak SRAM by 18%. MCUFlowNet-S runs 1.76x faster than a retrained EdgeFlowNet with 1.6% higher endpoint error. In simulated forest flights at 2 m/s it reaches the goal collision-free in 51.5% of trials versus 41.8% for the baseline. PACE-NAS also yields a PIDNet-S variant 1.17x faster at similar accuracy.

**Novelty assessment:** Moderate. Decoupling memory from latency in the search and the SRAM-peak diagnosis are useful; latency is compiler-estimated rather than measured end-to-end in the abstract, and closed-loop results are simulated. Code is open. Read at abstract level only.

**Relevance score:** 4/5 — open code, real MCU-NPU target, a concrete memory-aware NAS design; held back by simulated closed-loop evidence.

---

## 3. Energy Allocation Between Computation and Wi-Fi Transmission in TinyML Federated Learning on IoT Devices: A Measured Crossover

**Source:** Research Square preprint, 2026 (Siam, Azzedin) — Scholar result dated about four days before this run; snippet only.
**Link:** https://www.researchsquare.com (title search; direct URL not captured)

**Why it matters:** [[Federated_Learning]] on MCUs is usually argued on communication cost versus computation cost without device-level measurements. This work tests that assumption on a Wi-Fi microcontroller, which ties [[Keyword_Spotting]] training to a measured energy crossover.

**Technical summary:** From the snippet only: an ESP32-S3 trains the output head of a keyword-spotting CNN and the authors measure where on-device computation versus Wi-Fi transmission dominates energy. Models, datasets and numerical results were not visible.

**Novelty assessment:** Cannot be judged from the snippet; a measured-crossover framing is useful if the methodology is sound. Preprint, not peer reviewed.

**Relevance score:** 3/5 — on-topic and potentially a good measured-energy anchor; unverified beyond a snippet.

---

## 4. Hardwired Distributed Processing Units for Inference: Neural Decisions at the Sensor that Free the Host

**Source:** arXiv:2611.06436 (cs.AR; cs.DC, cs.LG) — submitted 4 Nov 2026.
**Author:** Raj Mali
**Link:** https://arxiv.org/abs/2611.06436

**Why it matters:** A processor-free, OS-free binarized CNN at the camera sensor on a low-cost Artix-7 [[FPGA]] is an extreme point in the design space for [[Vision]] at the edge, trading generality for a fixed-latency decision and a 16-byte-per-frame host interface.

**Technical summary:** An 80x60-pixel pipeline feeds a four-layer binarized CNN with 93,408 one-bit weights, detecting zebra crossings in 1,814 LUTs with fixed cycle count per frame and bit-exact match to its software model on 639 test images. When it gives an answer rather than "not sure" it is correct 95.7% of the time; a hardware contrast stage lifts dashcam-style accuracy from 47.7% to 78.2%. The host saves roughly 8 ms CPU time per frame.

**Novelty assessment:** Low-to-moderate: single-task, tiny dataset, one author, companion to two earlier papers; no code listed. Interesting as a bounded-scope architecture rather than a general method.

**Relevance score:** 3/5 — a concrete extreme-efficiency design point with limited generality.

---

## Also noted this week (not selected, kept for provenance)

- **Energy Measurement and Optimization of TinyML in Resource-Constrained Embedded Systems: A Systematic Mapping Study** — arXiv:2611.07264 (Almeida et al.). Listing-level only (abstract fetch rate-limited). [[Quantization]] / measurement. https://arxiv.org/abs/2611.07264
- **AutoCompress: Automated Hardware-Guided Model Compression** — arXiv:2611.08290. Listing-level only. [[Compression]]. https://arxiv.org/abs/2611.08290
- **SparseForge: Beyond Spike Sparsity toward Hardware-Exploitable Neuron Pruning for Efficient SNN Acceleration** — arXiv:2611.01611 (Wang et al.). Listing-level only. [[Pruning]] / [[Event-Driven_Neuromorphic_Accelerators]]. https://arxiv.org/abs/2611.01611
- **SMART-AIMC: Sensitivity-Aware Mixed ADC Resolution for Analog In-Memory Computing** — arXiv:2611.01707 (Chen et al.). Listing-level only. https://arxiv.org/abs/2611.01707
- **A Mixed-Precision CNN-LSTM Accelerator for Sleep Staging** — arXiv:2611.00660 (Chen et al.) and **FPGA Acceleration of CNN-BiLSTM for EEG-Based Sleep Staging** — arXiv:2611.00669 (Zhou et al.). Listing-level only. [[Biosignals]] / [[FPGA]].
- **SensorGuard-RV: Sensor-to-Register Data Protection for Resource-Constrained RISC-V Devices** — arXiv:2611.08380 (Noori, Shepherd). Listing-level only. [[RISC-V]].
- **Do sEMG Foundation Models Improve Cross-Subject Generalisation?** — arXiv:2611.08199. Listing-level only. [[Biosignals]].
- **Multi-objective NAS for TinyML keyword spotting: metaheuristic vs Bayesian optimization with hardware-in-the-loop** — Garai and Samui, Neural Computing and Applications (Springer), 2026. Scholar snippet only. [[NAS]] / [[Keyword_Spotting]].
- **Efficient Polish-Language Keyword Spotting on Microcontrollers** — Sobczyk and Fonał, Applied Sciences (MDPI), 2026. Scholar snippet only (dated about four months ago).
- **Federated Keyword Spotting on Constrained IoT Devices over Thread and CoAP** — Gutiérrez et al., IEEE, 2026. Scholar snippet only.
- **Search coverage this cycle:** arXiv via cs.AR recent listing (first 50 of 65 entries) and cs.LG recent listing (first 50 entries); cs.DC and eess.SP were not checked separately, and several abstract fetches were rate-limited. The `site:` WebSearch queries for IEEE Xplore, ACM DL, MDPI, ScienceDirect and SpringerLink (one query each) returned almost exclusively arXiv/preprint/blog pages and no new dated publisher items, so coverage of those libraries is thin and not evidence of absence. The Scholar pass ran 3 queries via Claude in Chrome (TinyML energy benchmark MCU NPU; NAS with Ethos-U/Cortex-M; keyword spotting/HAR TinyML), date-sorted. No institutional full-text check was performed.

---

## Signals for the knowledge base

The memory-wall benchmark adds independent, measured support to the existing `restricted-operator-set-codesign-mcu-npu` candidate (already `ready_for_review`): it extends "deployability is a toolchain/runtime property that MACs do not capture" with a cross-device energy and memory-traffic result. It also bears on the already-decided measurement-infrastructure thread (recorded in the consolidation history), which is not touched here. MCUFlowNet is recorded as a modest supporting observation for the robotics candidate (`robotics-edge-ai-applications-gap`, already `ready_for_review`). No new candidate is created and no status changes this week.

---

## Suggested thesis / research hooks

- **Memory traffic as the cost model for MCU NPUs:** reproduce part of the benchmark on a smaller device set and test whether a memory-traffic model predicts latency and energy better than MAC count, including on STM32N6 and Ethos-U55 boards.
- **Memory-aware NAS with fixed SRAM peak:** apply the PACE-NAS idea (macro stage fixes peak SRAM) to keyword spotting or HAR on an Ethos-U55 board and compare with explicit-constraint NAS.
- **Measured crossover for federated TinyML:** if the ESP32-S3 crossover study holds up on full-text reading, replicate it for HAR with several radios (Wi-Fi, BLE, Thread).
