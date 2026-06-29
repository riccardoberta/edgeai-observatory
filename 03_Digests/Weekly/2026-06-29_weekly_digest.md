# Weekly Digest — 2026-06-29

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Three papers selected this week, all from the last two weeks of submissions, spanning quantization, NAS, and embedded ML systems engineering — three of the Observatory's core taxonomy branches.

---

## 1. Characterizing the Impact of NVFP4 Quantization for Low-Power Edge AI Deployment

**Source:** arXiv:2606.06527 (cs.AR, cs.LG) — submitted 3 Jun 2026, revised through v3 10 Jun 2026
**Authors:** Ovishake Sen, Venkata Nithin Kamineni, Daniel Lobo, Swarup Bhunia, Rickard Ewetz, Baibhab Chatterjee
**Link:** https://arxiv.org/abs/2606.06527

**Why it matters:** This is the most directly relevant paper of the week for our [[Quantization]] line of work. It pushes precision down to 4-bit floating point (NVFP4: FP4 activations with FP8 block scale and FP32 tensor scale) and runs a careful ablation isolating what actually drives accuracy — block size, weight precision, and retraining — rather than just reporting a final number. That kind of disentangled analysis is exactly the gap most quantization papers leave open.

**Technical summary:** The paper studies NVFP4 quantization across six edge-efficient models. A block-size ablation finds B=16 gives the best accuracy/storage trade-off (4.5078 bits per input at N=4096). A weight-precision ablation shows FP8/FP16 weights barely improve over FP4 weights once the NVFP4 activation path is fixed — meaning activation quantization and scaling dominate accuracy behavior, not weight precision. Comparing plain unscaled FP4 against NVFP4, plain FP4 collapses accuracy for most compact models, while NVFP4 (with its block/tensor scaling) recovers most of it even without retraining, and reaches the best accuracy of all configurations when retraining is added.

**Novelty assessment:** Not a new quantization format — NVFP4 has been used in other (GPU-centric) contexts — but a rigorous, edge-focused ablation that isolates the real driver of NVFP4's effectiveness (scaling, not bit width alone). The "design guidance for hardware-software co-design" framing extends relevance beyond GPUs to accelerators, FPGAs, and near-memory computing.

**Relevance score:** 5/5 — directly extends [[Quantization]] and connects to [[Compression]]; a strong candidate for deep analysis in `02_Papers/`.

---

## 2. An affordable hardware-aware neural architecture search for deploying convolutional neural networks on ultra-low-power computing platforms

**Source:** arXiv:2606.16290 — submitted 15 Jun 2026
**Authors:** Andrea Mattia Garavagno, Edoardo Ragusa, Antonio Frisoli, Paolo Gastaldo
**Link:** https://arxiv.org/abs/2606.16290

**Why it matters:** Most HW-NAS work targets relatively capable microcontrollers; this paper explicitly targets ultra-low-power sensing nodes, and — notably — makes the search itself lightweight enough to run on embedded devices rather than only on a server/GPU. That's a meaningful practical constraint for our [[NAS]] notes and for deployment-side work in [[Cortex-M]].

**Technical summary:** The authors propose a HW-NAS that generates tiny CNNs fitting ultra-low-power MCU constraints, with a search procedure cheap enough to execute on the embedded device itself. Tested on three standard tiny computer-vision benchmarks, it matches state-of-the-art classification accuracy while producing much smaller architectures.

**Novelty assessment:** Incremental relative to the broader HW-NAS literature, but the "search runs on-device" angle is a genuinely useful systems contribution — most HW-NAS papers assume search happens off-device. Useful complement to existing [[NAS]] entries built around heavier search procedures (e.g. Once-for-All).

**Relevance score:** 4/5 — relevant to [[NAS]] and [[Vision]]; worth a closer look if we pursue on-device search as a thesis direction.

---

## 3. Embedded Machine Learning for Microcontroller-Class Edge Devices: Data, Feature, Evaluation, and Deployment Pipelines

**Source:** arXiv:2606.18122 — submitted 16 Jun 2026
**Author:** Mostafa Darvishi
**Link:** https://arxiv.org/abs/2606.18122

**Why it matters:** A systems-level synthesis rather than a single new technique — useful as a reference/teaching resource for the lab and for framing thesis topics around the parts of the embedded-ML pipeline that papers rarely cover explicitly: sampling/buffering, feature extraction as dimensionality reduction, validation under class imbalance, and streaming deployment.

**Technical summary:** The paper walks through the full embedded ML workflow for microcontroller-class devices, using inertial motion recognition (accelerometer-based) as a running example: a two-second three-axis window is reduced to RMS and spectral features before classification. It emphasizes engineering decisions usually glossed over in generic ML treatments — buffering strategy, feature engineering as a deliberate dimensionality-reduction step, evaluating under class imbalance, and co-designing model and runtime for streaming inference.

**Novelty assessment:** Low novelty as a research contribution (no new algorithm or benchmark result), but high value as a structured reference for onboarding students into the practical side of [[Human Activity Recognition]] / [[Biosignals]]-adjacent EdgeAI pipelines. Good candidate to cite in teaching material rather than in `02_Papers/` deep-analysis form.

**Relevance score:** 3/5 — supports teaching/onboarding more than it advances open research questions.

---

**Notes:** Full deep-analysis records (`02_Papers/`) have not yet been created for these three papers; #1 (NVFP4) is the strongest candidate for that next step given its direct relevance to active [[Quantization]] work.
