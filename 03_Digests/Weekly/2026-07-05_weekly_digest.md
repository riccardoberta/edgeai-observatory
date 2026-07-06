# Weekly Digest — 2026-07-05

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Three papers selected this week, spanning on-device continual learning of small language models, inference-time pruning on microcontrollers, and embedded anomaly detection — touching the [[Continual Learning]], [[On-device Learning]], [[Pruning]], and [[Industrial IoT]] branches of the taxonomy.

**Sourcing note (methodology, this cycle):** the sandbox running this automated cycle could not reach the arXiv listing/query API directly (the outbound proxy blocked `export.arxiv.org`). Monitoring was therefore done via web search over `arxiv.org` followed by full-text retrieval of each candidate; every paper written up below was read in full before inclusion, in line with the Observatory's "no hallucinated information / every claim traceable to source" principle. One paper (#1) falls squarely inside the last-7-days window (submitted 26 Jun 2026); the other two are recent, highly relevant, fully-verified works retained to keep coverage meaningful. Several additional late-June 2026 candidates were surfaced but could **not** be full-text-verified this cycle (their PDFs returned no machine-readable text) and are listed at the end as *unverified leads* to re-check next week rather than summarized here.

---

## 1. Continual Learning for Sequential Personalization of Small Language Models: A Stability Monitoring Analysis

**Source:** arXiv:2606.27634 (cs.LG) — submitted 26 Jun 2026
**Authors:** Thomas S. Paula, Lucas S. Kupssinskü, Rodrigo C. Barros (MALTA Lab, PUCRS, Brazil; Kunumi Institute)
**Link:** https://arxiv.org/abs/2606.27634

**Why it matters:** This is the only paper this week firmly inside the monitoring window, and it sits right on an emerging edge-AI frontier: personalizing Small Language Models (SLMs, ≤1B params) *on the device itself* as user data arrives over time. That turns deployment into a [[Continual Learning]] problem with catastrophic forgetting as the central risk. Its practical contribution — a cheap, checkpoint-level *stability monitor* — is directly reusable in our [[On-device Learning]] notes and connects the LLM-on-edge trend to the classic forgetting literature we already track (Kirkpatrick EWC, iCaRL).

**Technical summary:** The authors run sequential LoRA fine-tuning of three sub-1B SLMs (Qwen 3.5 0.8B, Llama 3.2 1B, Gemma 3 1B) across three TRACE tasks (FOMC, ScienceQA, NumGLUE) with no replay. After each adaptation stage they save a checkpoint and evaluate it on current, past, and future tasks plus a fixed reference set, building a checkpoint-by-task accuracy matrix and standard CL metrics (OP/BWT/FWT). The headline finding: a *reference-set KL divergence* from the base model tracks performance collapse well (Pearson r ≈ −0.5, p < 0.001), is **order-invariant** (same trajectory when task order is reversed), and appears to have a "failure zone" around KL ≈ 0.8. Gemma showed high instability (KL to base peaking ~1.62, sharp backward-transfer degradation) while Qwen stayed anchored (KL ~0.30, even positive BWT). So a lightweight distributional diagnostic can act as an early-warning signal *before* task accuracy visibly collapses.

**Novelty assessment:** Not a new CL algorithm and not embedded-hardware work — experiments run on a Titan X GPU, and quantized/on-MCU evaluation is explicitly left as future work. The novelty is methodological: framing on-device SLM personalization as a *stability-monitoring* problem and showing that a cheap, model-agnostic KL signal predicts forgetting order-invariantly. The "intrinsic stability fingerprint" per model family is a genuinely interesting observation worth watching.

**Relevance score:** 4/5 — strong conceptual fit for [[Continual Learning]] and [[On-device Learning]]; the KL early-warning idea is a candidate thesis hook (see below). Loses a point because it is not yet validated under quantization or on constrained hardware, which is exactly where our lab operates.

---

## 2. UnIT: Scalable Unstructured Inference-Time Pruning for MAC-efficient Neural Inference on MCUs

**Source:** arXiv:2507.07885 (cs.LG) — recent MCU-pruning work (submission date not captured this cycle)
**Authors:** Ashe Neth, Sawinder Kaur, Mohammad Nur Hossain Khan, Subrata Biswas, Asif Salekin, Bashima Islam (Worcester Polytechnic Institute; Syracuse University; Arizona State University)
**Link:** https://arxiv.org/abs/2507.07885

**Why it matters:** This is the most directly relevant paper of the week for our core [[Pruning]] line and for deployment on [[Cortex-M]]-class and even sub-Cortex-M microcontrollers. Almost all pruning we track is applied at training or compile time and relies on *structured* sparsity because irregular sparsity wastes cycles on hardware without SIMD/parallel compute. UnIT flips this: it prunes *at inference time*, per input, exploiting fine-grained irregular sparsity on exactly the tiny cores where structured pruning leaves efficiency on the table.

**Technical summary:** UnIT dynamically identifies and skips unnecessary multiply-accumulate (MAC) operations during inference, guided by input-specific activation patterns. It converts pruning decisions into cheap threshold checks — replacing multiplications with comparisons and approximated divisions — and reuses threshold computations across connections, with layer- and group-specific pruning sensitivity. It contributes three hardware-friendly division approximations tailored to common embedded platforms, and requires **no retraining and no hardware specialization**. Demonstrated on an MSP430 microcontroller, it reports 11.02%–82.03% MAC reduction, 27.30%–84.19% faster inference, and 27.33%–84.38% lower energy versus training-time-pruned models, while maintaining accuracy.

**Novelty assessment:** Genuinely novel angle. Unstructured, input-adaptive, inference-time pruning that deliberately *embraces* irregular sparsity is the opposite of the field's structured-pruning default, and the demonstration on an MSP430 (well below Cortex-M in capability) is a strong systems result. The multiplication→threshold-check reformulation and the embedded-friendly division approximations are the reusable ideas. Complements our existing training-time pruning entries (Optimal Brain Damage, Deep Compression, Learning Weights & Connections) rather than overlapping them.

**Relevance score:** 5/5 — directly extends [[Pruning]] and [[Cortex-M]] / MCU deployment; the strongest candidate this week for a `02_Papers/` deep-analysis record.

---

## 3. Real-Time Machine Learning for Embedded Anomaly Detection

**Source:** arXiv:2512.19383 (cs.LG) — submitted 22 Dec 2025 (survey; presented at the 2nd National Conference on AI and IT, Chadli Bendjedid El-Tarf University, Algeria)
**Authors:** Abdelmadjid Benmachiche, Khadija Rais, Hamda Slimi
**Link:** https://arxiv.org/abs/2512.19383

**Why it matters:** A compact, hardware-aware survey mapping the design space of on-device anomaly detection under hard memory/latency/power limits — useful reference material for our [[Industrial IoT]] and [[Predictive Maintenance]] branches, and a good framing document for thesis scoping because it foregrounds the constraints (concept drift, <10–160 KB budgets, safety-criticality) that papers usually gloss over.

**Technical summary:** The paper organizes embedded anomaly detection into four families and compares them by accuracy, memory, latency, and hardware fit: (1) tree-based — Isolation Forest, incl. a federated variant reaching >96% accuracy in <160 KB, the default for ultra-constrained MCUs but blind to temporal structure; (2) one-class learning — OCSVM / Deep SVDD / autoencoders, expressive but memory-heavy and mostly edge-CPU-class; (3) lightweight neural nets — quantized LSTM-autoencoders and 1D-CNNs via TFLite Micro / MicroPython, best for time-series but heavier on RAM; (4) statistical / threshold methods — control charts, moving stats, lightweight PCA running in <10 KB with deterministic latency for safety-critical use. It argues the strongest real systems are *cascaded* (cheap IF screen → heavier model only when triggered) and flags open gaps: no standardized hardware-aware benchmarks, weak on-device concept-drift handling, near-absent adversarial-robustness evaluation, and poor cross-platform portability (Cortex-M ↔ ESP32 ↔ RISC-V).

**Novelty assessment:** Low as a research contribution — it is a survey with no new algorithm or result — but valuable as a structured, constraint-first map of the anomaly-detection design space. Its "research gaps" section (drift, benchmarking, adversarial robustness, portability) reads almost like a thesis-topic menu. Cite in teaching/onboarding material rather than as a `02_Papers/` deep-analysis record.

**Relevance score:** 3/5 — supports [[Industrial IoT]] / [[Predictive Maintenance]] scoping and teaching; reference value over research novelty.

---

## Unverified leads for next cycle

The following late-June 2026 candidates were surfaced but could not be full-text-verified this cycle (PDF text not machine-readable via the retrieval path available in this run). They look on-topic and should be re-checked next week, ideally with the Claude in Chrome extension on unige.it access:

- **TinyML for On-Device and Edge Analytics in Wireless Networks: A Survey of Deployments, Opportunities, and Concept-Drift Mitigation** — arXiv:2606.30843 (relevant to [[Federated Learning]], [[Industrial IoT]]).
- **Efficient Network Inference via Hardware-Aware Architecture Search, Model Pruning & Quantization** — arXiv:2606.23210 (relevant to [[NAS]], [[Pruning]], [[Quantization]] on MCUs).
- **Latent Replay Detection: Memory-Efficient Continual Object Detection on Microcontrollers via Task-Adaptive Compression** — arXiv:2603.00138 (relevant to [[Continual Learning]], [[Vision]]).
- **Fast Transformer Inference on ARM-Based HMPSoCs** — arXiv:2606.02836 (relevant to [[Cortex-A]]).

Also noted (relevant but not in the last-7-days window): *Equivariant-Aware Structured Pruning for Efficient Edge Deployment* (arXiv:2511.17242) — G-CNN structured pruning + knowledge distillation + INT8 on EuroSAT/CIFAR-10, ~87% parameter reduction with accuracy recovered by adaptive fine-tuning; a useful cross-reference for [[Pruning]] + [[Distillation]] + [[Vision]] if we revisit symmetry-aware compression.

---

**Notes:** No deep-analysis records (`02_Papers/`) were created automatically. **#2 (UnIT)** is the strongest candidate for that next step given its direct relevance to active [[Pruning]] work on microcontrollers; **#1 (SLM stability monitoring)** is a good second, especially if we pursue the on-device SLM personalization direction. Suggested thesis hooks this week: (a) validate UnIT-style inference-time pruning on Cortex-M with CMSIS-NN and quantized models; (b) test whether the KL-divergence stability signal from #1 survives quantization and works as an on-device early-warning trigger for continual on-device learning.
