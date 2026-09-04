# Weekly Digest — 2026-07-19

Four papers dominated by **on-device LLM / transformer inference efficiency**: a CPU-oriented fractional-bit quantization compiler, a heterogeneity-first scheduler that co-schedules integrated GPU and NPU on edge SoCs, and a saliency-driven adaptive-precision compression scheme for ultra-low-power transformers — plus one strong **biosignals / wearable** entry on approximate-computing arrhythmia detection. Together they touch [[Quantization]], [[Compression]], [[NPU]], [[Biosignals]], and [[Cortex-M]].

---

## 1. PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference

**Source:** arXiv:2607.14618 (cs.LG; cross-listed cs.AR, cs.OS) — submitted 16 Jul 2026; accepted to ICCAD 2026
**Authors:** Hyunwoo Oh, Suyeon Jang, Hanning Chen, KyungIn Nam, Sanggeon Yun, Ryozo Masukawa, Mohsen Imani
**Link:** https://arxiv.org/abs/2607.14618

**Why it matters:** Directly relevant to [[Quantization]]. CPUs remain the most universal on-device inference target (every phone, laptop and many MCUs), yet fine-grained mixed-precision quantization has been hard to run efficiently on them — one either accepts coarse operating points (uniform 4-bit) or pays a runtime layout-regularization tax. PolyQ makes fractional-bit, per-channel quantization actually deployable on CPU-only targets by pushing the hard work to compile time.

**Technical summary:** PolyQ is a CPU-oriented compiler/quantization co-design for activation-aware channel-wise bit allocation under a user-specified average-bit budget. It assigns per-channel bit-widths from {2, 3, 4, 8, 16}, then a compile-time model compiler permutes and clusters channels into bit-homogeneous blocks, generates SIMD- and lookup-table-compatible kernels, and merges compatible permutations across operators so that layout regularization stays off the runtime path. Across Falcon-H1-3B, Llama2-13B and Qwen3-32B on WikiText-2, PolyQ gives stable quality scaling from 3–6 bits and improves perplexity by 2.4–32.1% over prior methods at a 3-bit target. End-to-end measurements on three representative CPUs (workstation, laptop, mobile) show compiler layout regularization cuts activation-reorder traffic by up to 70.8%, prefill latency and decode throughput scale nearly proportionally with the configured bit budget, and energy-per-token overhead stays below 2% relative to an optimized lookup-table back-end.

**Novelty assessment:** Moderate-to-high. Activation-aware and mixed-precision quantization are established (cf. AWQ, integer-only inference in [[Quantization]]), but the specific contribution — turning fine-grained per-channel budgets into bit-homogeneous blocks at compile time so a CPU can execute them with regular, SIMD/lookup-table-friendly layouts and near-linear latency/throughput scaling with the bit budget — is a genuinely useful systems contribution. The "predictable scaling with configured average bits" property makes deployment planning tractable rather than trial-and-error.

**Relevance score:** 4/5 — strong fit for [[Quantization]] and on-device LLM deployment; the compile-time block-homogenization idea is transferable to MCU/edge-CPU targets.

---

## 2. HeteroMosaic: Exposing and Exploiting Heterogeneous Execution Opportunities for Energy-Efficient Edge LLM Inference

**Source:** arXiv:2607.12839 (cs.DC; cross-listed cs.AR) — submitted 14 Jul 2026 (v3, 16 Jul); accepted to MICRO 2026
**Authors:** Gregory Hyegang Jun, Wesley Pang, Eddie Richter, Mehdi Saeedi, Aporva Amarnath, Pallavi Ferrao, Deming Chen
**Link:** https://arxiv.org/abs/2607.12839

**Why it matters:** Modern edge SoCs bundle CPU, integrated GPU, and [[NPU]] on unified memory, but real LLM runtimes typically make coarse device-level placement decisions and leave most of the heterogeneous silicon idle. HeteroMosaic proposes a scheduler that recovers this waste by co-executing iGPU and NPU — a constructive counterpart to purely diagnostic measurement studies of the same bottleneck (see "Is Your NPU Ready for LLMs?"). High reference and reproduction value for deploying LLMs on Ryzen-AI / Jetson-class heterogeneous edge hardware.

**Technical summary:** HeteroMosaic is a heterogeneity-first scheduling framework. It first uses a heterogeneous roofline model to decide when combining iGPU and NPU execution is actually beneficial, then decomposes inference into dependency-preserving micro-batches that expose cross-accelerator overlap, and applies trace-guided co-optimization of scheduling and device allocation under practical effects (memory contention, dynamic voltage/frequency scaling, device variation, NPU runtime overheads). Implemented in PyTorch C++ and evaluated on three AMD Ryzen AI platforms (NPU-heavy, balanced, iGPU-heavy). On the balanced platform it reports up to 1.73x speedup over an iGPU baseline, 1.78x over an NPU baseline, and 2.05x over frameworks such as llama.cpp, while reducing energy by up to 45.3%, and up to 2.35x over prior heterogeneous edge-AI solutions.

**Novelty assessment:** Solid systems novelty. Heterogeneous scheduling is not new, but the combination of a heterogeneous roofline to gate when co-execution pays off, dependency-preserving micro-batching to expose overlap, and trace-guided allocation that models real DVFS/contention/NPU-wakeup effects is a well-motivated advance over device-level or operator-isolated placement. The 45% energy reduction on a unified-memory SoC is the headline for edge deployment, extending [[NPU]] and the on-device-LLM trend (see [[MoE_Edge_LLM_Serving]]).

**Relevance score:** 4/5 — strong reference/methodology value for [[NPU]] and heterogeneous edge inference; application-class rather than MCU-class hardware.

---

## 3. Toward Energy-Efficient and Low-Power Arrhythmia Detection for Wearable Devices

**Source:** arXiv:2607.14747 (cs.AR; cross-listed cs.LG, cs.NE, cs.PF) — submitted 16 Jul 2026
**Authors:** Floriaan Bulten, Yawar Rasheed, Arlene John, Vincenzo Stoico, Ghayoor Gillani
**Link:** https://arxiv.org/abs/2607.14747

**Why it matters:** A clean example of *approximate computing* applied to always-on health monitoring, fitting [[Biosignals]]. Wearable ECG arrhythmia detection is a canonical ultra-low-power edge task, and the paper attacks the deployment constraint that determines wearable battery life — microwatt-scale power budgets — with hardware-level approximations rather than yet another accuracy-chasing model.

**Technical summary:** The authors reduce the power/energy of a state-of-the-art deep-learning arrhythmia-detection model through two approximation techniques: data-precision reduction and approximate multiplication, applied jointly to the model and its synthesized hardware architecture. Trained/validated on the MIT-BIH Arrhythmia Database, various approximate-multiplier implementations are synthesized and evaluated. Versus an 8.75 µW / 2.08 µJ reference architecture, the proposed design consumes 3.07 µW / 2.17 µJ at 12 kHz — a 64.9% power reduction — while retaining 93.7% classification accuracy and 92.1% sensitivity. At 100 MHz it consumes 9.45 mW / 0.8 µJ, a 61.5% energy reduction versus the state of the art.

**Novelty assessment:** Moderate. Approximate multipliers and precision reduction are individually well-known (sitting at the [[Quantization]] x approximate-computing corner), but the systematic co-application to a fabricated-quality ECG arrhythmia pipeline with a concrete µW-level power/accuracy trade-off is a useful, concrete data point for wearable [[Biosignals]] deployment — a well-characterized reference operating point rather than a new algorithmic idea.

**Relevance score:** 4/5 — strong fit for [[Biosignals]] and ultra-low-power edge hardware; the novelty is in careful engineering and characterization rather than a new method.

---

## 4. Adaptive Model Compression (AMC): Saliency-Driven Resource Allocation for Ultra-Low-Power Transformer Inference

**Source:** arXiv:2607.10109 (cs.IR; cross-listed cs.AI, cs.AR, cs.LG) — submitted 11 Jul 2026
**Authors:** Jiayin Hu, Kai Yuan, Vanessa Hu, Xuetao Yin, Jianhua Li, Sean Suchter
**Link:** https://arxiv.org/abs/2607.10109

**Why it matters:** Relevant to [[Compression]] and to the broader question of dynamic, data-dependent precision on the edge. Static inference wastes energy by processing easy and hard tokens with identical intensity; AMC allocates hardware resources by token importance — conceptually the transformer-token analogue of BitFair's dynamic bit-level early termination and UnIT's input-adaptive sparsity.

**Technical summary:** AMC is a saliency-driven, multi-tier framework that dynamically allocates compute based on token importance: high-saliency tokens get full-precision processing, while less significant data has its rank and bit-width aggressively reduced. On 45 nm CMOS hardware the authors report a 59.2% reduction in system energy and a 2.24x throughput increase, with a marginal 3.6% accuracy trade-off.

**Novelty assessment:** Moderate, with caveats. The saliency-driven, per-token mixed-rank/mixed-precision idea is a reasonable and timely direction, and the joint rank+bit-width reduction is a slightly richer knob than bit-width alone. The abstract is light on which model/dataset produces the accuracy number and what the baseline is, and the primary listing is cs.IR, so the claims need full-text scrutiny before citation. The conceptual link to dynamic-sparsity accelerators is the main reason to keep it on the radar; energy/throughput figures are reported on a 45 nm CMOS design point with limited baseline detail and should be treated as indicative until verified.

**Relevance score:** 3/5 — relevant to [[Compression]] and dynamic-precision inference, the weakest-specified of this set and not evaluated on MCU-class hardware.

---

## Suggested thesis / research hooks

- **Fractional-bit quantization on true MCUs:** port PolyQ-style compile-time bit-homogeneous blocking from application-class CPUs down to [[Cortex-M]] / [[RISC-V]] (with [[CMSIS-NN]] / [[microTVM_TVM|microTVM]] back-ends) and measure whether the near-linear latency-vs-bit-budget scaling survives without wide SIMD/lookup-table units. (Master's/PhD.)
- **Roofline-gated accelerator co-scheduling on open edge SoCs:** reproduce HeteroMosaic's iGPU+NPU co-execution on non-Ryzen edge hardware (e.g. Jetson, or a RISC-V + NPU platform) and quantify how much of the 45% energy saving is recoverable in an open runtime ([[ONNX_Runtime|ONNX Runtime]] / [[microTVM_TVM|microTVM]]). (Master's.)
- **Approximate-multiplier design space for wearable biosignals:** extend the arrhythmia-detection study to other [[Biosignals]] tasks (EEG seizure detection, PPG) and map the µW power/accuracy Pareto front across approximate-multiplier families. (Master's.)
- **Unifying dynamic, data-dependent precision:** compare AMC's token-saliency precision allocation against BitFair's bit-level early termination and UnIT's input-adaptive sparsity under one framework — is there a portable "spend compute where it matters" principle that works on commodity MCUs, not just custom silicon? (PhD-scale; [[Compression]] x [[Quantization]].)
