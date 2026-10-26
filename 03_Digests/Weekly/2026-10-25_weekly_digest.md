# Weekly Digest — 2026-10-25

A quiet week with two solid hardware-side items. SpikeDuet measures, on a real commodity microcontroller, when the on-chip matrix accelerator beats optimized CPU execution for spiking networks, and finds that the smallest network stays CPU-optimal. TernScope pairs ternary-weight quantization-aware training with a hardware area comparison for edge medical segmentation. Two lower-scored items follow: a mixed-precision mapping tool for multi-precision accelerators and a firmware-validation framework for TinyML. Touches [[Quantization]], [[Cortex-M]], [[NPU]], [[Event-Driven_Neuromorphic_Accelerators]], [[Vision]] and [[Compression]].

Covers arXiv listings of roughly 16 to 23 October 2026 (cs.AR and cs.LG recent listings, abstract pages for the shortlisted items) plus Google Scholar results sorted by date. Selection used abstract pages (arXiv) and Scholar snippets only; no full text was read for any item.

---

## 1. SpikeDuet: CPU-Accelerator Co-Execution of Sparse SNNs on Commodity MCUs

**Source:** arXiv:2610.24677 (cs.AR) — submitted 17 Oct 2026. Found in the cs.AR recent listing.
**Authors:** Muhammad Fahd Ibrahim Bhatti, Muhammad Ali Siddiqi
**Link:** https://arxiv.org/abs/2610.24677

**Why it matters:** Microcontrollers with a small built-in matrix accelerator are becoming common, and the usual assumption is that offloading to the accelerator is always better. This paper tests that assumption on physical hardware for spiking networks and reports a case where it is not. It connects [[Event-Driven_Neuromorphic_Accelerators]] with the Cortex-M tier ([[Cortex-M]]) and the question of how the accelerator and the CPU should share work.

**Technical summary:** The authors ask whether the Matrix Vector Processor on the EFR32MG24 (Cortex-M33 core) can speed up SNN inference beyond optimized event-driven CPU execution. They build an snnTorch-to-C flow with hardware-calibrated engine selection, a function-preserving neuron reordering that groups co-active neurons for the accelerator, and asynchronous CPU/MVP scheduling. Across five network configurations on the device they report 1.27 to 1.87x speedup and 11 to 34% lower energy per inference than optimized sparse Cortex-M33 execution; the smallest Braille network stays CPU-optimal.

**Novelty assessment:** Moderate. Heterogeneous scheduling and neuron reordering are not new in general, but measured results on an off-the-shelf MCU accelerator, including a case where the accelerator does not win, are uncommon. Small networks (Braille-384 is the largest named), a single device family, and the abstract page lists no code. Read at abstract level only.

**Relevance score:** 4/5 — measured energy and latency on a commodity microcontroller accelerator; held below 5 for the single device, small scale and absent code.

---

## 2. TernScope: Model-Hardware Co-Design for Efficient Ternary Endoscopic Segmentation

**Source:** arXiv:2610.29617 (eess.IV; cross-listed cs.AR, cs.CV) — submitted 21 Oct 2026.
**Authors:** Zhuoyu Wu, Wenhui Ou, Qiawei Zheng, Xuhong Qiu, Wenqi Fang, Raphaël C.-W. Phan
**Link:** https://arxiv.org/abs/2610.29617
**Code:** https://github.com/ReaganWu/TernScope

**Why it matters:** A concrete, open-code example of pushing [[Quantization]] to ternary weights with 8-bit activations in a segmentation network (a task less often covered than classification), with the hardware consequence quantified: multiplier-free compute. Relevant to [[Vision]] at the edge and to the broader question of how far low-bit models change accelerator design.

**Technical summary:** A compact segmentation network built from split-channel large-kernel blocks and branch fusion, trained with Ternary Progressive Quantization-aware Training that quantizes from deep layers toward the input and output. All 25 convolutions use ternary weights and 8-bit activations. The model has 0.2483M parameters and 0.0949 GMACs and stays competitive in accuracy on in-domain and external datasets. Under the same 45 nm technology the compute array is 88.46% smaller than the original Gemmini systolic array with 8x8-bit multipliers.

**Novelty assessment:** Moderate. Progressive ternary QAT and the co-design framing are incremental, but the open code and the explicit area comparison are useful. The hardware result is an area estimate under a technology model, not a measured chip or microcontroller deployment, so the edge claim is untested on real devices. Read at abstract level only.

**Relevance score:** 4/5 — open code, a clear low-bit method and a hardware-cost number; the hardware evidence is a synthesis-level area figure only.

---

## 3. qGAMMA: A Framework for Optimal DNN Mapping on Multi-Precision Accelerators

**Source:** arXiv:2610.23222 (cs.AR; cs.AI) — submitted 16 Oct 2026.
**Authors:** Leandro Fiorin, Luigi Altamura, Cristina Silvano
**Link:** https://arxiv.org/abs/2610.23222

**Why it matters:** Mixed-precision networks only pay off if the accelerator mapping exploits them. This is a design-space-exploration tool for exactly that mapping step, linking [[Quantization]] (mixed precision) with accelerator design.

**Technical summary:** A genetic-algorithm search guided by an analytical performance model derived from synthesis results finds the mapping and accelerator configuration that best meets chosen metrics (performance, energy efficiency, utilization) across fixed- and floating-point formats on spatial accelerators.

**Novelty assessment:** Low-to-moderate from the abstract: a mapper in the lineage of earlier genetic-algorithm mappers, extended to multiple precisions. Validation is on an analytical model rather than measured silicon, no code is listed, and the abstract does not give quantitative results.

**Relevance score:** 3/5 — relevant tooling, but model-based and unquantified at abstract level.

---

## 4. LiteML-Edge: A Contract-Centered Framework and Methodology for Replay-Driven 1:1 Python–Firmware Validation in TinyML

**Source:** IEEE Latin America Transactions, 2026 (dos Santos, Torné, Figueiredo et al.) — Scholar result dated about four days before this run; snippet only, DOI not captured.
**Link:** https://latamt.ieeer9.org (open-access PDF listed on Scholar; title search)

**Why it matters:** The gap between a Python model and the firmware that runs it is a recurring source of silent deployment error. A methodology that validates the two one-to-one by replaying the same inputs addresses a reproducibility concern directly, in the same spirit as the Observatory's interest in whether conversion success implies retained accuracy.

**Technical summary:** From the snippet only: a contract-centered framework for replay-driven validation of equivalence between Python and firmware implementations in TinyML. Target hardware, models and results were not visible.

**Novelty assessment:** Cannot be judged from the snippet.

**Relevance score:** 3/5 — on-topic and potentially useful as a reproducibility instrument, unverified beyond a snippet. An unige.it full-text read would settle it.

---

## Also noted this week (not selected, kept for provenance)

- **SQuAT: Spherical Lattice Vector Quantization-Aware Training** — arXiv:2610.31412 (Loeschcke et al.). Listing-level only. [[Quantization]]. https://arxiv.org/abs/2610.31412
- **QuaNAS: Uncertainty-Aware Reuse of Earlier Searches for Query-Efficient NAS** — arXiv:2610.31251 (Satria et al.). Listing-level only. [[NAS]]. https://arxiv.org/abs/2610.31251
- **Towards Field-Deployable Wearable IMU Systems for Occupational Activity Recognition** — arXiv:2610.31160 (Haq et al.). Listing-level only; abstract fetch was rate-limited. [[Human_Activity_Recognition]]. https://arxiv.org/abs/2610.31160
- **MAC units for a 2x2 int8 systolic array on Tiny Tapeout** — arXiv:2610.24326 (Gorodecky). Listing-level only. https://arxiv.org/abs/2610.24326
- **Heart Signal (ECG) as Vibration Signature for Human Authentication Using TinyML** — arXiv:2610.24761 (Thota et al.). Listing-level only. [[Biosignals]]. https://arxiv.org/abs/2610.24761
- **FIGFLEX: Mixed-Precision FP-INT GEMM Accelerator Co-Designed with Low-Bit LLM Quantization** — arXiv:2610.30480 (Tahmasebi et al.). Listing-level only; LLM-oriented accelerator. https://arxiv.org/abs/2610.30480
- **A 105 MS/s 4.18 nJ/inference Mixed-Signal Streaming ML Engine for Wireless Baseband in 12LP+ FinFET** — arXiv:2610.26552 (Castañeda et al.). Listing-level only. https://arxiv.org/abs/2610.26552
- **A Generic On-Board AI Processing Chain for Earth Observation** — arXiv:2610.26340 (Foulon et al.). Listing-level only. https://arxiv.org/abs/2610.26340
- **An Energy-Efficient Edge-AI Framework for Continuous EEG-Based Cognitive Screening** — IEEE Open Journal, 2026 (Sinha et al.). Scholar snippet only; fully quantized TinyML model on embedded hardware. [[Biosignals]].
- **Co-Designing TinyML-powered Digital Health Applications for FPGA-based Wearable Devices** — Sesli et al., IEEE conference, 2026. Scholar snippet only; reports about 23% lower energy per inference with RISC-V-coupled accelerators. [[FPGA]] / [[RISC-V]].
- **Scholar background noise:** many hits were book chapters and Wiley/Springer-style TinyML overview chapters; none selected.
- **Search coverage this cycle:** arXiv coverage came from the cs.AR "recent" listing (about 56 entries; the last six of the 19 Oct entries not shown) and the cs.LG recent listing for 23 Oct (first 50 of 205 entries only); cs.DC and eess.SP were not checked. Several arXiv abstract fetches were rate-limited (HTTP 429). The `site:` WebSearch queries for IEEE Xplore, ACM DL and MDPI returned almost no publisher pages (mostly arXiv, preprints and blogs) and surfaced no new dated item; ScienceDirect and SpringerLink were not queried separately this cycle. Coverage of those libraries is therefore thin and should not be read as absence of relevant work. The Scholar pass ran 2 queries via Chrome (TinyML/microcontroller/quantization; RISC-V/NPU/on-device/accelerator/energy).

---

## Signals for the knowledge base

SpikeDuet is recorded as modest supporting evidence for the microcontroller-accelerator candidate (restricted-operator-set-codesign-mcu-npu), which is already at `ready_for_review`: it shows, on a different vendor's MCU accelerator, that deployability depends on how the workload maps to the accelerator, not on the accelerator's mere presence. It is a looser fit than the operator-coverage evidence already in that entry, and the entry's status is unchanged. TernScope and qGAMMA are single observations on low-bit co-design and mixed-precision mapping; they do not yet form a pattern and no new candidate is created this week.

---

## Suggested thesis / research hooks

- **When does the MCU matrix accelerator pay off?** SpikeDuet's smallest-network result invites a systematic crossover study (network size, sparsity, activity locality) on several MCU accelerators, including Arm Ethos-U and STM32N6-class parts, with measured energy.
- **Ternary or sub-8-bit models on a real microcontroller:** TernScope reports an area estimate only; a Master's project could port its ternary segmentation model to a Cortex-M or RISC-V target using packed storage and report measured latency and energy.
- **Python-to-firmware equivalence checking:** if the LiteML-Edge full text confirms a replay-based contract methodology, a thesis could apply it across [[TensorFlow_Lite_Micro]] and CMSIS-NN deployments to quantify silent divergence.
