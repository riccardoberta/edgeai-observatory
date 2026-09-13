# Weekly Digest — 2026-09-06

Four items spanning integer-only test-time adaptation on microcontrollers, statistically certified inference on imperfect analog in-memory accelerators, a low-power memory architecture for spiking neural networks, and a biosignal application benchmarking full TinyML pipelines on STM32. Touches [[Quantization]], [[Continual_Learning]], [[Cortex-M]], [[NPU]], [[Event-Driven_Neuromorphic_Accelerators]], and [[Biosignals]].

---

## 1. FORGE: Forward-Only Test-Time Adaptation for Integer-Only Vision Models on Microcontrollers

**Source:** arXiv:2609.01683 (cs.CV; cross-listed cs.AR, cs.LG) — submitted 1 Sep 2026; published in Transactions on Machine Learning Research (2026)
**Authors:** Muhammad Rehan, Haider Ali, Muhammad Ali Munir, Moaz Amjad
**Link:** https://arxiv.org/abs/2609.01683

**Why it matters:** Vision models on microcontrollers are quantized to integer-only arithmetic and deployed in inference-only runtimes that fuse batch normalization into the preceding convolution — a step that destroys exactly the statistics that existing forward-only test-time adaptation (TTA) methods rely on to cope with field distribution shift (sensor noise, blur, lighting). Prior forward-only TTA work either targets server/edge-GPU-class models or assumes BN layers are still present, so this is the first method demonstrated on a real, deployed, BN-folded integer-only network. Directly relevant to [[Quantization]] and [[Continual_Learning]] on [[Cortex-M]]-class hardware.

**Technical summary:** FORGE restores adaptation on folded convolutions by re-normalizing each convolution's per-channel output to its clean training statistics, using only forward-pass estimates — no gradients, no BN layers required. It recovers most of gradient-based TENT's accuracy gain (+20.9 vs. +24.9 points) while being the only method that runs on a folded integer-only model, needs to adapt only 3 of 21 layers (selected without seeing test corruptions) to recover 93% of the benefit, and survives single-sample streaming with batch-size-scaled momentum. The authors validate bit-exact int8 convolution execution and deploy on a real ESP32-S3: measured with a Nordic PPK2 power profiler, the adaptation step costs only 8.3 mJ (6.8% of inference energy) and 21.9 ms.

**Novelty assessment:** High. The key insight — that BN-folding for integer inference destroys the very statistics normalization-based TTA needs — is a specific, non-obvious observation about the interaction between quantization deployment practice and continual/test-time adaptation research, and the fix is validated on real hardware rather than simulation.

**Relevance score:** 5/5 — published (TMLR), real ESP32-S3 deployment with measured energy/latency, open code, and a genuinely new mechanism bridging [[Quantization]] and on-device adaptation.

---

## 2. RACE-AIMC: Selective Inference for Heterogeneous Analog In-Memory Accelerators at the Edge

**Source:** arXiv:2609.03149 (cs.ET; cross-listed cs.AR, cs.LG) — submitted 2 Sep 2026
**Authors:** Osama Yousuf, Martin Lueker-Boden
**Link:** https://arxiv.org/abs/2609.03149

**Why it matters:** Analog in-memory computing (AIMC) accelerates inference by computing directly inside a memory array, but every physical chip is distorted differently by programming errors, noise, and limited-resolution converters, forcing a costly choice between running a redundant ensemble or trusting a single unreliable chip. This paper replaces that guesswork with a certified statistical guarantee, relevant to the Observatory's open "in-memory computing" [[NPU]]/Hardware gap and to a research group independent of the MTJ-focused FALCON line covered in the 2026-09-02 digest.

**Technical summary:** RACE-AIMC (Risk-Aware Certified Ensemble for AIMC) studies a pool of physical accelerators offline, selects the single best one for a given energy budget, and computes a mathematically exact upper bound on its error rate when it chooses to answer; online, only that one accelerator runs, with a lightweight check deciding whether to accept its answer or defer to a fallback. In simulations with noisy weight mapping across multiple independent test runs, every certified bound stayed under a 10% error target (mean bound 7.83% ± 0.89%, with 70.88% ± 0.98% of inputs answered directly), matching a clean digital baseline's accuracy while cutting modeled energy use by 69.02% versus always running the full ensemble.

**Novelty assessment:** Moderate-to-high. Selective/certified inference is established in ML generally, but applying an exact, per-chip statistical error bound to heterogeneous physical AIMC accelerators — turning "which chip do I trust" into a solved optimization rather than a design heuristic — is a genuinely new framing for edge accelerator deployment.

**Relevance score:** 4/5 — rigorous statistical guarantees, concrete modeled energy savings, and a second, independent research thread in analog in-memory computing reliability for edge deployment.

---

## 3. Non-uniform Memory Partitioning For Low-Power Spiking Neural Networks

**Source:** arXiv:2608.30444 (cs.AR) — submitted 31 Aug 2026; published at IEEE AICAS 2025
**Authors:** Simon Richter, Darío Fernández Khatiboun, Maryam Sadeghi, Milad Zamani, Farshad Moradi
**Link:** https://arxiv.org/abs/2608.30444

**Why it matters:** Spiking Neural Networks (SNNs) are the natural algorithm family for [[Event-Driven_Neuromorphic_Accelerators]], but their time-stepped processing makes synaptic-weight SRAM access the dominant source of power consumption — directly limiting how small and low-power a neuromorphic edge deployment can be.

**Technical summary:** The authors exploit the highly non-uniform average firing rate of neurons across an SNN to partition on-chip memory into multiple non-uniformly sized banks: weights of frequently-firing neurons go to shallow, low-access-cost memory, while rarely-accessed weights go to deeper, higher-density memory. An automatic exploration procedure finds optimal bank configurations given application requirements and hardware constraints. Synthesized in 28nm CMOS, the architecture achieves up to 61% reduction in synaptic weight memory access power versus a conventional design, with 2.1x lower area overhead than a uniformly-partitioned memory bank reaching comparable power savings.

**Novelty assessment:** Moderate. Firing-rate-aware memory hierarchy design is a targeted, well-quantified hardware optimization rather than a new algorithmic idea, but it is a concrete, synthesized (not just simulated) contribution to a specific and under-served hardware niche.

**Relevance score:** 3/5 — solid, quantified hardware contribution for [[Event-Driven_Neuromorphic_Accelerators]], narrower in scope than this week's other picks but a useful anchor for a still-thin part of the Hardware taxonomy.

---

## 4. Preprocessing and Feature Extraction Co-Optimization for Low-Power EEG-Based Neurodegenerative Disease Detection: A Benchmark on STM32 Embedded Platforms

**Source:** BMC Neurology (Springer), DOI 10.1186/s12883-026-05315-4 — published 1 Sep 2026 (open access, CC BY 4.0); found via Google Scholar topic search, not indexed on arXiv
**Authors:** Jakjoud Fatimazahra, Reha Abdelati, Jakjoud Widad
**Link:** https://doi.org/10.1186/s12883-026-05315-4

**Why it matters:** A concrete, fully-quantified [[Biosignals]] application that closes the loop from algorithm choice to real embedded deployment: twelve preprocessing techniques and six classifiers evaluated end-to-end on real STM32 hardware with [[Quantization]] via CMSIS-NN, rather than stopping at an offline accuracy number. Found through the Observatory's Google Scholar discovery pass (per the documented discovery-gap fix), not through arXiv or the IEEE/ACM/MDPI `site:` searches — a concrete instance of Scholar surfacing a paper the other channels missed this week.

**Technical summary:** The authors benchmark a lightweight TinyML framework for differential diagnosis of Alzheimer's disease versus Frontotemporal Dementia from EEG, using two public OpenNeuro datasets (88 participants total). All twelve preprocessing/six-classifier combinations were implemented and measured on real STM32 NUCLEO-64 and STM32WB55 boards ([[Cortex-M]]) with INT8 quantization via CMSIS-NN. The best pipeline — Sparse Decomposition preprocessing combined with XGBoost — reached 94.46% accuracy and 92.1% sensitivity while requiring only 45 KB of SRAM and low execution time.

**Novelty assessment:** Moderate. Neither EEG-based dementia classification nor STM32/CMSIS-NN deployment is new individually, but the systematic co-optimization across twelve preprocessing techniques and six classifiers, measured on real embedded hardware rather than simulated, is a useful reference point for what "wearable-feasible" actually costs in SRAM and accuracy for this application.

**Relevance score:** 3/5 — real embedded measurements and a strong accuracy/footprint result for a clinically-motivated [[Biosignals]] use case, though the paper is an applications benchmark rather than a new algorithmic or hardware contribution.

---

## Suggested thesis / research hooks

- **Extending BN-statistics-recovery TTA beyond vision:** FORGE's core trick (re-normalizing folded-convolution outputs to recover BN-adaptation statistics) is architecture-general wherever BN-folding is used for integer inference. Does the same recovery work for integer-only audio/keyword-spotting or biosignal models (e.g. the STM32 EEG pipeline in item 4), where distribution shift comes from sensor drift rather than visual corruption? A well-scoped Master's project bridging [[Quantization]] and [[Continual_Learning]].
- **Certified selective inference beyond AIMC:** RACE-AIMC's statistical certification framework assumes a pool of heterogeneous physical accelerators with per-chip noise profiles. Digital [[NPU]]s and microcontroller-class inference also show measurable per-chip performance/power variation (process variation, aging); would an analogous "risk-aware certified ensemble" approach generalize to picking among a fleet of nominally-identical digital edge devices, e.g. for a large IoT sensor deployment?
- **Firing-rate-aware memory hierarchies for other sparse workloads:** The non-uniform memory partitioning idea (allocate cheap memory to frequently-accessed weights) is specific to SNNs' firing-rate skew, but many pruned or dynamically-sparse networks show similarly skewed access patterns. A PhD-scale study could ask whether the same partitioning principle transfers to structured/dynamic pruning ([[Pruning]]) on conventional accelerators.
- **Standardizing "wearable-feasible" reporting for biosignal TinyML:** Item 4 reports SRAM footprint, accuracy, and execution time together for twelve preprocessing/classifier combinations on real hardware — a rare level of completeness for [[Biosignals]] papers, most of which report only offline accuracy. A short methodological piece proposing this as a standard reporting bar for wearable biosignal TinyML papers could itself be a useful, citable contribution.
