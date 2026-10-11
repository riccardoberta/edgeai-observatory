# Weekly Digest — 2026-10-11

A thin week for new arXiv submissions that clear the bar, and a useful one for the on-device training thread. Three items are selected, all at or near the microcontroller tier, and all three report numbers measured on real or realistic embedded targets. MemFLoRA reframes parameter-efficient adaptation of CNNs around the one quantity that actually limits training on a constrained device — saved activation state — and gives the "activations, not weights" argument a concrete, HAR-validated recipe. TinyUDE removes the numerical-solver tape from training physics-informed models, making on-device training feasible in about 61 kB on an ESP32. A Bologna-line hearable beamformer shows a mixed-precision (float32/int8/float16) transformer pipeline fitting an MCU power and latency budget. Touches [[On-device_Learning]], [[Human_Activity_Recognition]], [[Quantization]], [[Compression]], [[Cortex-M]], [[Keyword_Spotting]] and [[Industrial_IoT]].

Covers arXiv papers submitted 22 September to 6 October 2026. Two of the three were first surfaced this cycle by the Google Scholar keyword pass rather than the arXiv listings and carry earlier submission dates; this is stated per item.

---

## 1. MemFLoRA: Memory-Floor LoRA for CNN Adaptation at the Edge

**Source:** arXiv:2610.08669 (cs.LG; cross-listed cs.AI) — submitted 6 Oct 2026; accepted at ASP-DAC 2027 (Tokyo, 25–28 Jan 2027). Found via Google Scholar (query: "on-device training" / "on-device learning" microcontroller OR edge, sorted by date).
**Authors:** Mehmet Emre Akbulut, Johannes Geier, Ulf Schlichtmann
**Link:** https://arxiv.org/abs/2610.08669

**Why it matters:** The [[On-device_Learning]] page already holds the claim, from TinyTL onward, that activations rather than trainable parameters are the memory bottleneck of on-device training. Most LoRA-style adapters nonetheless target transformers and are judged by parameter count. This paper turns the claim into a design criterion for CNNs and shows the saving is large on a [[Human_Activity_Recognition]] workload — the application where post-deployment shift (new user, new body location, new sensor placement) is the standard motivation for adapting on the device.

**Technical summary:** The authors define an "activation-memory-floor" criterion: trainable backward computations must not depend on full-width layer inputs. The adapter that follows freezes the low-rank down-projection, trains a scale-matched up-projection, runs backbone normalization in eval mode, and uses activation-minimal backward rules, so the state saved for the backward pass shrinks to the low-rank branch. Evaluated on three HAR datasets and two CNN backbones under subject, body-location and sensor-placement shifts, it reduces saved-activation memory by 98.5–98.7% and peak training-state memory by 94.9–97.3% relative to full fine-tuning, while matching or exceeding CNN parameter-efficient fine-tuning baselines on accuracy.

**Novelty assessment:** Moderate-to-high. The memory-first framing is the contribution; low-rank adapters and frozen backbones are known. The reported memory figures are for saved training state, apparently measured at the framework level; the abstract does not say the adapter was run on a microcontroller, how it compares against sparse-update methods such as TinyTrain or the Tiny Training Engine, or what its energy cost is. The abstract notes released code (the URL was not captured in the text read); check before any 02_Papers/ record.

**Relevance score:** 4/5 — a direct, quantified answer to the central open problem of [[On-device_Learning]] on a core application, from a credible systems group (TUM), with code and a design-automation venue; held below 5 because hardware deployment is not stated in the abstract.

---

## 2. Transformer-based Neural Beamforming for Real-Time Speech Enhancement on Smart Low-Power Hearable Devices

**Source:** arXiv:2609.33755 (cs.SD; cross-listed cs.AI, eess.AS) — submitted 27 Sep 2026. Found via Google Scholar (query: "microcontroller" "neural network" inference memory OR latency, sorted by date); outside the 7-day window by a few days.
**Authors:** Luca Bompani, Marco Fariselli, Giovanni Oltrecolli, Francesco Conti
**Link:** https://arxiv.org/abs/2609.33755

**Why it matters:** Audio on hearables is one of the tightest real-time, always-on edge targets: milliwatts, a battery of about 100 mAh, and a latency ceiling set by perception. Neural spatial filtering has so far been shown mostly on larger processors. This is, per the authors, the first real-time multi-channel transformer-based beamformer on an MCU-class device, and it is a clean example of mixed precision chosen per stage rather than per model — relevant to [[Quantization]] and to the audio side of [[Keyword_Spotting]]-type always-on pipelines.

**Technical summary:** Six microphones feed a three-stage pipeline: a float32 minimum-variance distortionless response (MVDR) beamformer, an int8 CNN that estimates the MVDR weights, and a float16 lightweight transformer that applies a per-frame correction. Weight estimation is time-sliced against beamforming so that the per-frame latency is 15 ms while a complete set of CNN-derived weights is refreshed every 564 ms. The deployed pipeline reaches STOI 97.65%, SI-SNR 20.26 dB and wideband PESQ 3.676 at 45.9 mW average power. A speech-activity-detection module (98.5% accuracy, 0.62 mJ per inference) bypasses the pipeline during silence; the system is reported to exceed a 16 h all-day target on a 100 mAh battery, with an estimated lifetime of up to about 20 h.

**Novelty assessment:** Moderate-to-high as a systems result. The individual components (MVDR, CNN weight estimation, int8/float16 mixed precision) are known; the contribution is a measured end-to-end deployment with explicit latency, power and battery-life accounting. The abstract does not name the MCU or state whether code is released, and the battery-life figure is an estimate under assumed deployment conditions rather than a measurement. Author group overlaps with the PULP line also behind the 2026-10-05 MEGATRON entry, so this is not independent of the earlier Bologna-region evidence on hardware.

**Relevance score:** 4/5 — complete, measured pipeline on MCU-class hardware with power and latency budgets and a clear mixed-precision rationale; the unnamed target and unconfirmed code release keep it from 5.

---

## 3. TinyUDE: Solver-Free Universal Differential Equations on Microcontrollers via Lie-Taylor Jet Matching

**Source:** arXiv:2609.26972 (cs.LG; cross-listed cs.ET) — submitted 22 Sep 2026. Found via Google Scholar (query: "on-device training" / "on-device learning"); outside the 7-day window.
**Authors:** Pranavanath Balamurali, Hrishi Kamireddy
**Link:** https://arxiv.org/abs/2609.26972

**Why it matters:** Hybrid physics-plus-neural models (universal differential equations) are what many industrial and control applications actually want on the device, but training them by backpropagating through an ODE solver needs megabytes of solver tape. This paper removes the solver from training altogether, which is a different route to the same goal as the sparse-update and zeroth-order methods already tracked: on-device training whose memory cost is accounted for and small. Relevant to [[On-device_Learning]] and, as a pattern, to [[Industrial_IoT]] models that embed physical structure.

**Technical summary:** "Lie-Taylor jet matching" fits a hybrid vector field directly to the first and second time-derivatives of the observed states, estimated online with Savitzky–Golay filtering, so gradients are analytic and no automatic-differentiation software is needed. Naive derivative matching degrades under sensor noise; the authors add noise-adaptive mechanisms (full-rate phase-shifted sampling, a reservoir buffer, cosine-annealed optimization with weight averaging, on-device noise estimation and polynomial-misfit quality gating). On a damped pendulum and a chaotic double pendulum the method matches or exceeds an RK4/multiple-shooting/discrete-adjoint/Adam baseline at matched data windows, reaching a geometric-mean relative field error of 0.65× the baseline within 108 kB of static memory across 0–5% noise. On an ESP32 the on-device run recovers the damping coefficient (0.400, true 0.400) within 61.3 kB of static memory and 7.24 ms per update (18.1% duty cycle at 25 Hz).

**Novelty assessment:** Moderate. Derivative-matching ("gradient matching") for dynamical systems predates this; the new pieces are the noise-adaptive stack that closes the accuracy gap and the measured MCU deployment with a stated memory and time budget. Validation is on two low-dimensional benchmark systems, so scaling to realistic plants and to larger networks is untested, and the abstract does not mention released code.

**Relevance score:** 3/5 — a real MCU measurement with an explicit memory budget on a genuine on-device-training problem, but the systems are toy-scale and the topic sits at the edge of the Observatory's core taxonomy.

---

## Also noted this week (not selected, kept for provenance)

- **NanoSentry: An Edge-Deployable Unified Neural Architecture for Multi-Domain Industrial Prognostics and Health Management** — Chowdhury, Nasek, Prottoy et al., *Artificial Intelligence* (Wiley Online Library), 2026. Scholar snippet only (not read beyond it): reports on-device evidence on an STM32H7 (Cortex-M7, 480 MHz) with a DWT-cycle-counter latency measurement over 1,000 runs and an estimated energy per inference. [[Industrial_IoT]] / [[Predictive_Maintenance]] on a [[Cortex-M]]; a candidate for a closer read if the full text is reachable through unige.it.
- **Do I Need the Cloud? Uncertainty-Aware Step-Level Handoff for Small Language Model Agents** — arXiv:2610.07816 (cs.AI), Abolfazl Younesi. STEPGATE scores each action a local small model proposes and escalates only difficult steps; a Qwen2.5-1.5B/7B pair reaches 82.7% task success at 30.8% escalation on a 52-task BFCL-derived set versus 67.3% local-only. Small test sets, one model family; relevant to [[MoE_Edge_LLM_Serving]] only at the policy level. https://arxiv.org/abs/2610.07816
- **DySCo: Dynamic Sharding for Collaborative Edge-Cloud LLM Inference with Depth-Synchronized Batching** — arXiv:2610.08268 (cs.DC). Listing-level only (title and subject tags). https://arxiv.org/abs/2610.08268
- **Tram-FL: Reducing Communication and Computation Costs through Sequential Model Circulation in Decentralized Federated Learning** — arXiv:2610.07859 (cs.DC). Listing-level only. [[Federated_Learning]]. https://arxiv.org/abs/2610.07859
- **Q-MINO: A Minimal-Norm Method for Quantization-Aware Training** — arXiv:2610.00738 (cs.AR listing), Don Li. Listing-level only. [[Quantization]]. https://arxiv.org/abs/2610.00738
- **JASPER: Special Session on Joint Reliability And Security Assessment of SPlit Computing for Edge Robustness** — arXiv:2610.04396 (cs.AR listing), Enrico Magliano et al. Listing-level only. https://arxiv.org/abs/2610.04396
- **SmartBike: A Low-Power Edge IoT System for Cycling Safety and Real-Time Awareness** — arXiv:2610.11824 (eess.SP listing). Listing-level only; the page did not say whether a neural network is involved. https://arxiv.org/abs/2610.11824
- **Not re-selected (already in the 2026-10-05 digest):** AdaptViT (2610.02288), ShatterQuant (2610.00207), EdgeDAE (2610.00311), ZTA-Q (2610.01867).
- **Search coverage this cycle:** The arXiv advanced and keyword search pages returned HTTP 500 and "Rate exceeded" from Chrome, so arXiv coverage relied on the cs.AR, cs.LG, eess.SP and cs.DC "recent" listings, whose pages show only the first 50 entries (cs.LG: 50 of 324 for 9 Oct), plus Scholar. The `site:`-filtered searches for IEEE Xplore, ACM DL, MDPI, ScienceDirect and SpringerLink (one query each) returned mostly non-publisher pages and surfaced no new dated item worth selecting; coverage of those libraries this week is therefore thin and should not be read as absence of relevant work. The Scholar pass ran 3 queries via Chrome.

---

## Signals for the knowledge base

The on-device training thread gained two more independent observations. MemFLoRA states the memory constraint as a criterion — no trainable backward computation may depend on full-width layer inputs — which is the CNN-adapter counterpart of the feasible-suffix selection and the SRAM budgeting already in the candidate queue; TinyUDE shows a different elimination, dropping the solver tape rather than activations. Together with the HO-FL and edge-SNN items of last week and the five-paper Scholar cluster of the September monthly synthesis, the pattern "training feasibility is decided by an accounted memory budget, not by parameter count" now rests on observations from at least ten unrelated groups across four separate cycles. The candidate has been moved to `ready_for_review`; whether it deserves a concept of its own or should be merged into the existing [[On-device_Learning]] page is a decision for the Knowledge Base Consolidation cycle. The hearable beamformer is a single clean data point for stage-wise mixed precision (float32 / int8 / float16 in one pipeline); it does not yet constitute a signal.

---

## Suggested thesis / research hooks

- **Put MemFLoRA on a microcontroller-class budget:** The paper reports saved-activation and peak training-state memory, not a deployment. A Master's project could port the adapter to a Cortex-M or a RISC-V MCU through [[TensorFlow_Lite_Micro]]-style static allocation, measure peak SRAM, time and energy per adaptation step on the HAR datasets, and compare against TinyTrain and the Tiny Training Engine's sparse update under identical memory caps.
- **Memory-floor criterion as a search constraint:** The activation-memory-floor rule is checkable from a layer graph. A thesis could embed it as a hard constraint in [[NAS]] or in a LoRA-rank/placement search, so that adapters are generated that satisfy a user-specified peak-SRAM budget by construction.
- **Stage-wise precision audit for hearable pipelines:** The beamformer mixes float32, int8 and float16 across stages. A reproducible study could sweep each stage's precision on Cortex-M with and without an FPU or Helium, recording accuracy (STOI, SI-SNR), power and latency, to show which stage actually dictates the energy budget.
- **Solver-free training beyond toy systems:** TinyUDE's 61 kB figure is for a pendulum. A PhD-level direction is to test whether derivative matching with noise-gated updates scales to a real condition-monitoring plant (for instance a motor or bearing model) on an MCU, which would link the result to the [[Predictive_Maintenance]] concept.
