# Weekly Digest — 2026-07-26

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`. Four papers selected this week, all inside the 7-day window (submitted 20–23 Jul 2026). The dominant theme this cycle is a clear pivot from last week's *inference*-efficiency focus toward **on-device training, adaptation, and continual learning on resource-constrained hardware**: a RISC-V single-core float16 training framework, a heterogeneous on-device adaptation pipeline that repurposes an inference accelerator for frozen-backbone feature extraction, and an in-memory-computing (ECRAM) continual-learning system — plus one strong **efficient-inference** entry, a sparsity-aware FPGA CNN accelerator. Together they touch the [[On-device Learning]], [[Continual Learning]], [[RISC-V]], [[Quantization]], [[FPGA]], [[Pruning]], and [[Compression]] branches of the taxonomy. The recurring sub-motif — freeze most of the network and update only a lightweight, cheap-to-train part — links three of the four and connects back to established records like [[On-device Learning]] (TinyTL, TinyTrain).

**Sourcing note (methodology, this cycle):** as in prior automated cycles, the sandbox could not reach arXiv's listing/query API directly (`export.arxiv.org` is outside the outbound network allowlist, and `web_fetch` refuses non-provenanced URLs). Monitoring was therefore done through the Claude in Chrome extension on Ricky's browser, navigating the arXiv `recent` listings for cs.AR and eess.SP directly and reading each selected paper's abstract page in full before inclusion — in line with the Observatory's "no hallucinated information / every claim traceable to source" principle. cs.AR covered the full Mon 20 Jul – Fri 24 Jul window and yielded the strongest, most coherent EdgeAI set (the edge-relevant cs.LG items surfaced as cs.AR cross-lists and are captured below); eess.SP was swept but, as last week, was almost entirely wireless-comms / ISAC / RIS work with little edge-deployment relevance. cs.DC was reached via cross-lists rather than swept separately. Every paper below was read at the abstract level from its arXiv page; none has yet been read in full-PDF depth. The optional IEEE Xplore / ACM DL / Google Scholar cross-checks were **skipped** this cycle: arXiv coverage alone was sufficient for a valid digest, and Google Scholar's terms discourage the kind of unattended automated querying an unsupervised scheduled run would amount to. They remain available for on-demand, human-in-the-loop use in a follow-up conversation.

---

## 1. Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core

**Source:** arXiv:2607.21130 (cs.AR; cross-listed cs.AI) — submitted 23 Jul 2026; accepted to IEEE PRIME 2026
**Authors:** Benjamin Hubinet, Pierre-Alain Moellic, Olivier Savry, Olivier Potin, Jean-Baptiste Rigaud
**Link:** https://arxiv.org/abs/2607.21130

**Why it matters:** This is the bullseye paper of the week for our group. It targets *complete on-device training* on a RISC-V **single core** — not an accelerator, not application-class silicon — using only standard RISC-V ISA extensions, and it does so on top of AIfES, an existing open-source embedded training framework. That combination (open source, standard ISA, true MCU-class target, transfer-learning support) makes it directly usable in our [[RISC-V]] and [[On-device Learning]] lines rather than merely citable.

**Technical summary:** The authors leverage the standard RISC-V `Zfh` (scalar float16) and `Zvfh` (vector float16) extensions to enable end-to-end on-device training on a resource-constrained RISC-V single core, contributing an open-source framework built on AIfES. Using float16 instead of float32 cuts the training memory footprint by ~50% with minimal model-quality degradation. Transfer-learning and fine-tuning scenarios are supported through **layer-freezing** capabilities (train only selected layers). They quantify the hardware cost of the ISA support: adding `Zfh` to an RV64GC super-scalar out-of-order FPGA softcore costs only +1.15% LUT6 and +0.05% FF at 175 MHz, and they outline a `Zvfh` vector implementation within the same core.

**Novelty assessment:** High for our purposes. Low-precision training and layer freezing are individually known ([[Quantization]]; TinyTL/TinyTrain in [[On-device Learning]]), but the specific contribution — a fully open-source float16 *training* (not just inference) path riding on standardized RISC-V float16 extensions, characterized end-to-end from ISA area overhead up to model accuracy on a single MCU-class core — is a genuinely useful and reproducible systems result. The area-overhead numbers make the "is it worth adding float16 to my core?" question answerable with data.

**Relevance score:** 5/5 — direct fit for [[RISC-V]] and [[On-device Learning]]; open-source, MCU-class, and immediately actionable for the group's embedded-training work. The strongest deep-analysis candidate this week.

---

## 2. Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator

**Source:** arXiv:2607.18101 (cs.LG; cross-listed cs.AR, cs.CV) — submitted 20 Jul 2026; accepted to the ITEM Workshop @ ECML-PKDD 2026
**Authors:** Mateusz Piechocki, Alessandro Capotondi, Marek Kraft
**Link:** https://arxiv.org/abs/2607.18101

**Why it matters:** This is the pragmatic, commercial-hardware counterpart to paper #1: instead of building training support into the core, it *repurposes an inference-only edge accelerator* (Hailo-8L) to do the expensive part of on-device adaptation. It attacks the exact obstacle that makes lifelong personalization hard on the edge — end-to-end backprop is too costly — by keeping the backbone frozen and quantized on the accelerator and fine-tuning only a small head on the host CPU. High reproduction value (code released) for anyone doing in-field personalization on Raspberry-Pi-class + NPU-stick hardware.

**Technical summary:** The authors propose a heterogeneous adaptation pipeline that partitions the computational graph so the pre-trained backbone is quantized to INT8 and executed on a Hailo-8L inference accelerator for **frozen-backbone feature extraction**, while only a lightweight FP32 classification head is fine-tuned on the host CPU. This enables frequent, energy-efficient in-field updates with most weights fixed. Across multiple architectures and datasets, the pipeline reaches up to 15.4× faster wall-clock training than a Raspberry Pi 5 CPU baseline, offers competitive throughput in favorable settings, and consistently lowers energy per sample. They find that **post-training quantization restoration** is crucial to preserve the quality of accelerator-generated features and limit accuracy loss in quantization-sensitive architectures.

**Novelty assessment:** Solid systems novelty. Frozen-backbone / head-only fine-tuning is established ([[On-device Learning]]: TinyTL), but repurposing a strictly inference-oriented commercial accelerator as the feature-extraction engine of a training loop — and characterizing the INT8 quantization-restoration step needed to keep features usable — is a well-motivated, practical contribution. Its value is as a concrete, reproducible reference architecture for heterogeneous CPU+NPU on-device adaptation. Pairs naturally with #1 (both freeze the backbone; one adds low-precision training to the core, the other offloads frozen inference to fixed-function silicon).

**Relevance score:** 4/5 — strong fit for [[On-device Learning]] and [[Quantization]]; directly reproducible and relevant to heterogeneous edge personalization. Below 5 only because the hardware (Hailo-8L + Pi 5) is a notch above the group's most constrained MCU targets.

---

## 3. Leveraging ECRAM for Edge Continual Learning (CLASP)

**Source:** arXiv:2607.19661 (cs.AR; cross-listed cs.ET, cs.LG) — submitted 22 Jul 2026 (extended abstract of an AICS 2025 poster)
**Authors:** Nabila Tasnim, Haoran Liu, Qing Cao, Saugata Ghose
**Link:** https://arxiv.org/abs/2607.19661

**Why it matters:** This is the week's best fit for the [[Continual Learning]] branch and a look at where the *device-technology* frontier of on-device learning is heading. Continual learning is attractive for edge platforms (autonomous vehicles, smart sensors) that must adapt in the field without catastrophic forgetting, but the data movement it generates between CPU/GPU and memory is a poor fit for the edge. CLASP attacks that with in-memory computing on a fabricated emerging-memory device — a direction worth tracking even if it is not near-term deployable in our toolchain.

**Technical summary:** The authors present CLASP (Continual Learning Acceleration System Platform), described as the first end-to-end system with in-memory-computing (IMC / processing-using-memory) acceleration for continual learning. It confronts the two standard IMC obstacles — noisy compute operations that harm training accuracy, and poor/incomplete support for resource-efficient training — via hardware/software co-design exposing software-visible, assembly-level instructions that drop into a range of continual-learning algorithms. CLASP is built around a fabricated, back-end-of-line (BEOL)-compatible **ECRAM** (electrochemical RAM) device. Using learning-without-forgetting and experience-replay on MNIST, CLASP with ECRAM approaches in-GPU training accuracy while delivering 67× speedup and 132× energy savings.

**Novelty assessment:** Moderate, with caveats. An end-to-end IMC continual-learning stack built around a fabricated ECRAM device — with a software-visible instruction interface so it isn't locked to one algorithm — is a real and forward-looking contribution at the [[Continual Learning]] × emerging-hardware corner. But this is an *extended abstract* of a 2025 poster, and the headline speedup/energy numbers are demonstrated only on MNIST, a weak proxy for real edge continual-learning workloads. Treat the 67×/132× figures as promising-but-preliminary until a full paper with harder benchmarks appears.

**Relevance score:** 3/5 — conceptually important for [[Continual Learning]] and on-device learning on emerging memory, and a good trend marker, but early-stage (MNIST-only, extended-abstract) and on a device technology (ECRAM/IMC) outside our current [[Cortex-M]]/[[RISC-V]] toolchain, so not immediately actionable.

---

## 4. SparHiXcel-v2: A Flexible Sparsity-Aware FPGA Accelerator with Column-Wise Compression for Efficient CNN Inference

**Source:** arXiv:2607.19248 (cs.AR) — submitted 21 Jul 2026
**Authors:** Amirhossein Zarei, Shervin Vakili
**Link:** https://arxiv.org/abs/2607.19248

**Why it matters:** The week's efficient-*inference* entry and best fit for the [[FPGA]] branch. It tackles the perennial sparsity dilemma — unstructured sparsity gives better accuracy but maps badly to hardware, while structured sparsity is hardware-friendly but rigid — with a configurable architecture plus a co-designed pruning scheme, and reports concrete throughput/efficiency numbers on a cost-effective FPGA part. Good reference/benchmarking value for the group's [[FPGA]] and [[Pruning]]/[[Compression]] work.

**Technical summary:** SparHiXcel-v2 is a configurable FPGA CNN accelerator built around a scalable 2-D MAC array with a **column-wise kernel compression** technique that handles irregular sparsity patterns at minimal hardware overhead, aiming for a better flexibility-vs-efficiency balance than pure structured or unstructured approaches. The design is paired with a hardware-algorithm co-design framework: an ordering-optimization scheme and a multi-phase **structured pruning-and-revival** algorithm tuned to the microarchitecture. On an AMD Kintex UltraScale+ FPGA in structured-sparsity mode it reaches over 2.5 TOPS and 210 GOP/s/W for VGG16, and over 1.1 TOPS and 72 GOP/s/W for ResNet18, with modest accuracy degradation.

**Novelty assessment:** Moderate. Sparsity-aware CNN accelerators are a crowded space, and this is explicitly a "-v2" refinement, so the novelty is incremental — the column-wise compression plus microarchitecture-matched prune-and-revive schedule are sensible refinements rather than a new paradigm. Its value is as a well-characterized, cost-effective FPGA design point (concrete TOPS / GOP-per-watt on named models and a named part) usable as a baseline or reference in [[FPGA]]/[[Pruning]] studies.

**Relevance score:** 3/5 — relevant to [[FPGA]], [[Pruning]], and [[Compression]] with citable efficiency numbers, but incremental and on application-class FPGA hardware rather than our most constrained targets.

---

## Honorable mention (just outside the 7-day window)

- **Mitigating Compiler Fusion-Induced Power Bursts in Mobile NPU Inference as the Battery Depletes** — arXiv:2607.16555 (cs.AR; submitted 17 Jul 2026, announced in the 21 Jul listing). A measurement study on a Snapdragon 8 Gen 3 showing that aggressive operator fusion in a mobile [[NPU]] compiler creates monolithic "superlayers" whose concentrated execution causes large peak-current bursts that trigger DVFS and hurt the low-voltage margin; a black-box pre-compilation graph rewrite inserting barriers at power hot-spots cuts peak current from 3.12 A to 1.94 A (MobileNetV4, 768×768, ImageNet-1k) for 3.76% latency overhead. Genuinely relevant to compiler-level [[NPU]] deployment and thematically continues the edge-LLM/NPU thread, but its submission date falls just before this cycle's window (and after last week's), so it is noted rather than scored. Worth a look if power-delivery-aware compilation is on the radar.

---

## Candidates for deep analysis (`02_Papers/`)

No deep-analysis records were created automatically this cycle. In priority order:

- **#1 Float16 On-Device Training on RISC-V (arXiv:2607.21130)** — clear top candidate: open-source, MCU-class RISC-V *training* on standard ISA extensions, with end-to-end characterization from ISA area overhead to model accuracy. Directly relevant to the group's embedded-training work and an obvious thesis springboard (below).
- **#2 On-Device Model Adaptation with an Edge AI Accelerator (arXiv:2607.18101)** — worth a deep record as a reproducible reference architecture for heterogeneous CPU+NPU on-device adaptation; code is released, and the INT8 quantization-restoration finding is a concrete, reusable detail.

## Suggested thesis / research hooks this week

- **Float16 vs int8 on-device training on RISC-V:** extend paper #1 by comparing its `Zfh`/`Zvfh` float16 training path against integer/quantized training (cf. Deutel 2024, on-device training on quantized Cortex-M) on the same RISC-V core — which wins on the memory/accuracy/energy Pareto front for true MCU-class targets? (Master's/PhD; bridges [[RISC-V]], [[On-device Learning]], [[Quantization]].)
- **Repurposing inference-only NPUs for training:** generalize paper #2's "frozen backbone on the accelerator, head on the CPU" pattern beyond Hailo-8L to other inference-only edge accelerators (Ethos-U, Coral) and quantify how far the frozen-feature-extraction trick scales before quantization-restoration can no longer recover accuracy. (Master's; [[On-device Learning]] × [[Quantization]].)
- **Continual learning on commodity edge memory, not ECRAM:** take CLASP's (#3) software-visible IMC continual-learning instruction model and ask how much of its benefit survives on *commodity* SRAM/eDRAM-based near-memory compute (no fabricated ECRAM), on harder-than-MNIST edge benchmarks. (PhD-scale; [[Continual Learning]] × emerging hardware.)
- **Unifying the "freeze most of the net" principle:** three of this week's papers (and TinyTL/TinyTrain in [[On-device Learning]]) all reduce on-device training cost by updating only a small part of the network. Is there a portable framework — across low-precision cores, offloaded frozen backbones, and IMC — that predicts, for a given hardware budget, *which* subset to train? (PhD-scale; [[On-device Learning]] × [[Quantization]] × [[Continual Learning]].)

---

**Notes:** All four scored papers are within the last-7-days window (submitted 20–23 Jul 2026) and were verified at the abstract level from their arXiv pages; none has yet been read in full-PDF depth, so efficiency/accuracy figures should be re-checked before citation in any survey or thesis. eess.SP was swept but yielded no strong EdgeAI entries this week (dominated by wireless / ISAC / RIS work); cs.DC and the edge-relevant cs.LG items were covered via cs.AR cross-lists. IEEE/ACM and Google Scholar checks were not run this cycle (see sourcing note). `sources.yaml` `last_checked` for arXiv advanced to 2026-07-26.
