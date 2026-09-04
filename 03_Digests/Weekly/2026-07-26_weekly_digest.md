# Weekly Digest — 2026-07-26

Four papers, pivoting from inference-efficiency toward **on-device training, adaptation, and continual learning on resource-constrained hardware**: a RISC-V single-core float16 training framework, a heterogeneous on-device adaptation pipeline that repurposes an inference accelerator for frozen-backbone feature extraction, and an in-memory-computing (ECRAM) continual-learning system — plus one efficient-inference entry, a sparsity-aware FPGA CNN accelerator. Together they touch [[On-device_Learning]], [[Continual_Learning]], [[RISC-V]], [[Quantization]], [[FPGA]], [[Pruning]], and [[Compression]]. A recurring sub-motif — freeze most of the network and update only a lightweight, cheap-to-train part — links three of the four and connects back to established [[On-device_Learning]] work (TinyTL, TinyTrain).

---

## 1. Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core

**Source:** arXiv:2607.21130 (cs.AR; cross-listed cs.AI) — submitted 23 Jul 2026; accepted to IEEE PRIME 2026
**Authors:** Benjamin Hubinet, Pierre-Alain Moellic, Olivier Savry, Olivier Potin, Jean-Baptiste Rigaud
**Link:** https://arxiv.org/abs/2607.21130

**Why it matters:** Targets *complete on-device training* on a RISC-V single core — not an accelerator, not application-class silicon — using only standard RISC-V ISA extensions, on top of AIfES, an existing open-source embedded training framework. That combination (open source, standard ISA, true MCU-class target, transfer-learning support) makes it directly usable for [[RISC-V]] and [[On-device_Learning]] work.

**Technical summary:** The authors leverage the standard RISC-V `Zfh` (scalar float16) and `Zvfh` (vector float16) extensions to enable end-to-end on-device training on a resource-constrained RISC-V single core, contributing an open-source framework built on AIfES. Using float16 instead of float32 cuts the training memory footprint by ~50% with minimal model-quality degradation. Transfer-learning and fine-tuning scenarios are supported through layer-freezing capabilities (training only selected layers). They quantify the hardware cost of the ISA support: adding `Zfh` to an RV64GC super-scalar out-of-order FPGA softcore costs only +1.15% LUT6 and +0.05% FF at 175 MHz, and they outline a `Zvfh` vector implementation within the same core.

**Novelty assessment:** High. Low-precision training and layer freezing are individually known ([[Quantization]]; TinyTL/TinyTrain in [[On-device_Learning]]), but the specific contribution — a fully open-source float16 *training* (not just inference) path riding on standardized RISC-V float16 extensions, characterized end-to-end from ISA area overhead up to model accuracy on a single MCU-class core — is a genuinely useful and reproducible systems result. The area-overhead numbers make the "is it worth adding float16 to my core?" question answerable with data.

**Relevance score:** 5/5 — direct fit for [[RISC-V]] and [[On-device_Learning]]; open source, MCU-class, and immediately actionable.

---

## 2. Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator

**Source:** arXiv:2607.18101 (cs.LG; cross-listed cs.AR, cs.CV) — submitted 20 Jul 2026; accepted to the ITEM Workshop @ ECML-PKDD 2026
**Authors:** Mateusz Piechocki, Alessandro Capotondi, Marek Kraft
**Link:** https://arxiv.org/abs/2607.18101

**Why it matters:** The pragmatic, commercial-hardware counterpart to on-core training approaches: instead of building training support into the core, it repurposes an inference-only edge accelerator (Hailo-8L) to do the expensive part of on-device adaptation. It attacks the obstacle that makes lifelong personalization hard on the edge — end-to-end backpropagation is too costly — by keeping the backbone frozen and quantized on the accelerator and fine-tuning only a small head on the host CPU. High reproduction value (code released) for in-field personalization on Raspberry-Pi-class + NPU-stick hardware.

**Technical summary:** The authors propose a heterogeneous adaptation pipeline that partitions the computational graph so the pre-trained backbone is quantized to INT8 and executed on a Hailo-8L inference accelerator for frozen-backbone feature extraction, while only a lightweight FP32 classification head is fine-tuned on the host CPU. This enables frequent, energy-efficient in-field updates with most weights fixed. Across multiple architectures and datasets, the pipeline reaches up to 15.4x faster wall-clock training than a Raspberry Pi 5 CPU baseline, offers competitive throughput in favorable settings, and consistently lowers energy per sample. Post-training quantization restoration turns out to be crucial to preserve the quality of accelerator-generated features and limit accuracy loss in quantization-sensitive architectures.

**Novelty assessment:** Solid systems novelty. Frozen-backbone / head-only fine-tuning is established ([[On-device_Learning]]: TinyTL), but repurposing a strictly inference-oriented commercial accelerator as the feature-extraction engine of a training loop — and characterizing the INT8 quantization-restoration step needed to keep features usable — is a well-motivated, practical contribution, and a concrete, reproducible reference architecture for heterogeneous CPU+NPU on-device adaptation. Pairs naturally with the RISC-V training paper above: both freeze the backbone, one adds low-precision training to the core, the other offloads frozen inference to fixed-function silicon.

**Relevance score:** 4/5 — strong fit for [[On-device_Learning]] and [[Quantization]]; hardware (Hailo-8L + Raspberry Pi 5) sits a notch above the most constrained MCU targets.

---

## 3. Leveraging ECRAM for Edge Continual Learning (CLASP)

**Source:** arXiv:2607.19661 (cs.AR; cross-listed cs.ET, cs.LG) — submitted 22 Jul 2026 (extended abstract of an AICS 2025 poster)
**Authors:** Nabila Tasnim, Haoran Liu, Qing Cao, Saugata Ghose
**Link:** https://arxiv.org/abs/2607.19661

**Why it matters:** A look at where the device-technology frontier of on-device learning is heading, relevant to [[Continual_Learning]]. Continual learning is attractive for edge platforms (autonomous vehicles, smart sensors) that must adapt in the field without catastrophic forgetting, but the data movement it generates between CPU/GPU and memory is a poor fit for the edge. CLASP attacks that with in-memory computing on a fabricated emerging-memory device.

**Technical summary:** The authors present CLASP (Continual Learning Acceleration System Platform), described as the first end-to-end system with in-memory-computing (processing-using-memory) acceleration for continual learning. It confronts the two standard obstacles of in-memory computing — noisy compute operations that harm training accuracy, and poor or incomplete support for resource-efficient training — via hardware/software co-design exposing software-visible, assembly-level instructions that drop into a range of continual-learning algorithms. CLASP is built around a fabricated, back-end-of-line-compatible ECRAM (electrochemical RAM) device. Using learning-without-forgetting and experience-replay on MNIST, CLASP with ECRAM approaches in-GPU training accuracy while delivering 67x speedup and 132x energy savings.

**Novelty assessment:** Moderate, with caveats. An end-to-end in-memory-computing continual-learning stack built around a fabricated ECRAM device — with a software-visible instruction interface so it isn't locked to one algorithm — is a real, forward-looking contribution at the [[Continual_Learning]] x emerging-hardware corner. But this is an extended abstract of a 2025 poster, and the headline speedup/energy numbers are demonstrated only on MNIST, a weak proxy for real edge continual-learning workloads; the 67x/132x figures should be treated as promising but preliminary until a full paper with harder benchmarks appears.

**Relevance score:** 3/5 — conceptually important for [[Continual_Learning]] and on-device learning on emerging memory, but early-stage (MNIST-only, extended-abstract) and on a device technology outside the [[Cortex-M]]/[[RISC-V]] mainstream.

---

## 4. SparHiXcel-v2: A Flexible Sparsity-Aware FPGA Accelerator with Column-Wise Compression for Efficient CNN Inference

**Source:** arXiv:2607.19248 (cs.AR) — submitted 21 Jul 2026
**Authors:** Amirhossein Zarei, Shervin Vakili
**Link:** https://arxiv.org/abs/2607.19248

**Why it matters:** Fits [[FPGA]] and the perennial sparsity dilemma — unstructured sparsity gives better accuracy but maps badly to hardware, while structured sparsity is hardware-friendly but rigid. This paper tackles it with a configurable architecture plus a co-designed pruning scheme, reporting concrete throughput/efficiency numbers on a cost-effective FPGA part.

**Technical summary:** SparHiXcel-v2 is a configurable FPGA CNN accelerator built around a scalable 2-D MAC array with a column-wise kernel compression technique that handles irregular sparsity patterns at minimal hardware overhead, aiming for a better flexibility-vs-efficiency balance than pure structured or unstructured approaches. The design is paired with a hardware-algorithm co-design framework: an ordering-optimization scheme and a multi-phase structured pruning-and-revival algorithm tuned to the microarchitecture. On an AMD Kintex UltraScale+ FPGA in structured-sparsity mode it reaches over 2.5 TOPS and 210 GOP/s/W for VGG16, and over 1.1 TOPS and 72 GOP/s/W for ResNet18, with modest accuracy degradation.

**Novelty assessment:** Moderate. Sparsity-aware CNN accelerators are a crowded space, and this is explicitly a second-generation refinement, so the novelty is incremental — the column-wise compression plus microarchitecture-matched prune-and-revive schedule are sensible refinements rather than a new paradigm. Its value is as a well-characterized, cost-effective FPGA design point (concrete TOPS / GOP-per-watt on named models and a named part) usable as a baseline or reference in [[FPGA]]/[[Pruning]] studies.

**Relevance score:** 3/5 — relevant to [[FPGA]], [[Pruning]], and [[Compression]] with citable efficiency numbers, on application-class FPGA hardware.

---

## Suggested thesis / research hooks

- **Float16 vs. int8 on-device training on RISC-V:** compare the `Zfh`/`Zvfh` float16 training path against integer/quantized training (cf. Deutel 2024, on-device training on quantized Cortex-M) on the same RISC-V core — which wins on the memory/accuracy/energy Pareto front for true MCU-class targets? (Master's/PhD; [[RISC-V]], [[On-device_Learning]], [[Quantization]].)
- **Repurposing inference-only NPUs for training:** generalize the "frozen backbone on the accelerator, head on the CPU" pattern beyond Hailo-8L to other inference-only edge accelerators (Ethos-U, Coral) and quantify how far the frozen-feature-extraction trick scales before quantization-restoration can no longer recover accuracy. (Master's; [[On-device_Learning]] x [[Quantization]].)
- **Continual learning on commodity edge memory, not ECRAM:** take CLASP's software-visible in-memory-computing continual-learning instruction model and ask how much of its benefit survives on commodity SRAM/eDRAM-based near-memory compute, on harder-than-MNIST edge benchmarks. (PhD-scale; [[Continual_Learning]] x emerging hardware.)
- **Unifying the "freeze most of the net" principle:** three of these papers (and TinyTL/TinyTrain in [[On-device_Learning]]) all reduce on-device training cost by updating only a small part of the network. Is there a portable framework — across low-precision cores, offloaded frozen backbones, and in-memory computing — that predicts, for a given hardware budget, which subset to train? (PhD-scale; [[On-device_Learning]] x [[Quantization]] x [[Continual_Learning]].)
