# Weekly Digest — 2026-09-02

Six items spanning on-device LLM serving infrastructure (memory management, split fine-tuning), hardware-accelerator co-design for edge LLM inference, a reliability-focused in-memory computing architecture, an FPGA/Transformer survey, and a physical-security angle on edge AI chips. Touches [[Quantization]], [[FPGA]], [[NPU]], [[Federated_Learning]], and [[Hardware_Security_of_Edge_AI_Accelerators]] (see also [[MoE_Edge_LLM_Serving]]).

---

## 1. mzCache: On-Device LLM Memory Management under Multitasking

**Source:** arXiv:2609.01338 (cs.OS; cross-listed cs.DC, cs.LG) — submitted 1 Sep 2026; accepted at MobiCom 2026
**Authors:** Hongseung Yu, Minsung Kim, Jongseok Park, Kyunghan Lee
**Link:** https://arxiv.org/abs/2609.01338

**Why it matters:** Addresses on-device LLM serving infrastructure (see [[MoE_Edge_LLM_Serving]]). Mobile on-device LLM inference is typically evaluated in isolation, but real phones run multiple apps concurrently, and OS-level memory pressure evicting model weights/KV cache is a real, previously under-addressed deployment obstacle. Accepted at MobiCom 2026, a top systems venue, and implemented as a real Android app on llama.cpp rather than simulated.

**Technical summary:** mzCache partitions LLM memory (weights + KV cache) into fine-grained shared buffers, enabling partial eviction/restoration with concurrent CPU-GPU access over the unified memory of mobile SoCs. Hybrid swap and "backward-out" eviction policies allow low-latency restoration from any eviction state, avoiding both slow storage reads and full KV-cache recomputation when a suspended app resumes inference. Measured on real hardware (Android devices), it achieves a 2.1–5.5x reduction in time-to-first-token versus storage-backed partial offload in real multitasking scenarios.

**Novelty assessment:** High as systems infrastructure. The problem framing (multitasking-induced memory pressure on on-device LLM serving) is under-studied relative to single-app benchmarks, and the OS/GPU co-design (restoration-oriented memory management with concurrent cross-processor access) is a genuinely new mechanism, not an incremental tuning of an existing scheme.

**Relevance score:** 5/5 — real Android deployment, top-tier venue (MobiCom), and a concrete, measured improvement (2.1–5.5x) on a deployment obstacle (multitasking memory pressure) not previously addressed in edge-LLM serving work.

---

## 2. Just Talk Once: Communication-Efficient Split Federated LLM Fine-Tuning on Edge Devices

**Source:** arXiv:2609.01457 (cs.DC) — submitted 1 Sep 2026; accepted at ACM MobiHoc 2026
**Authors:** Jiaxiang Geng, Xianhao Chen, Bing Luo
**Link:** https://arxiv.org/abs/2609.01457

**Why it matters:** Extends [[Federated_Learning]] into the LLM fine-tuning regime under the memory/bandwidth constraints that define edge deployment. Split federated learning (splitting model layers between client and server) usually still requires continuous bidirectional client involvement during training, a poor fit for intermittently-connected edge devices; this paper removes that requirement.

**Technical summary:** L-shaped split fine-tuning exploits weight tying in modern LLMs so server-side hidden activations can be supervised directly with target embeddings, letting training loss be computed server-side without sending outputs back to the client. Building on this, one-shot split fine-tuning lets clients upload activations once and go offline while the server continues optimizing over cached representations — eliminating the step-by-step communication loop of conventional split fine-tuning. Evaluated on a real testbed mixing commercial smartphones and NVIDIA developer boards as heterogeneous edge clients, showing significant reductions in both communication cost and client online time versus existing split-fine-tuning baselines.

**Novelty assessment:** Moderate-to-high. The weight-tying insight enabling one-directional (server-only) loss computation is a clean, non-obvious mechanism specific to how modern LLMs share input/output embeddings, and the one-shot (upload-once, go-offline) client model is a meaningful departure from the continuous-participation assumption that pervades federated/split-learning literature.

**Relevance score:** 4/5 — good fit for [[Federated_Learning]]: real heterogeneous-hardware testbed (smartphones + Jetson-class boards), a mechanism that could generalize to other split-learning schemes, and direct relevance to intermittent-connectivity edge scenarios.

---

## 3. Hardware Acceleration of Block-Diffusion LLM for Edge Devices

**Source:** arXiv:2609.01084 (cs.AR) — submitted 1 Sep 2026
**Authors:** Wei-Hsing Huang, Kiseok Lee, Ming-Yen Lee, Weiyu Sun, Cheng-Jhih Shih, Gayatri Tanksali, Arpit Khandelwal, Pin-Jun Chen, Yingyan Celine Lin, Shimeng Yu
**Link:** https://arxiv.org/abs/2609.01084

**Why it matters:** A concrete hardware/algorithm co-design for a still-uncommon LLM architecture family (block-diffusion LLMs) targeting single-stream, batch-one edge inference specifically — the regime where weight-traffic amortization tricks used in server-side batched serving do not apply. Involves Yingyan Celine Lin and Shimeng Yu, both established names in efficient-ML hardware research.

**Technical summary:** The paper co-designs three components: a wide-I/O LPDDR memory system for precision-tagged reads (WIFiV-LPDDR), a low-rank-plus-INT8-residual [[Quantization]] scheme for the KV-cache prefix with query-dependent per-entry precision (BRQ-KV), and drift-mapped canonical replacement / low-bit delta / cached-state carry for FFN weights, keeping live activations unquantized (DAT-FFN). All three map onto a single input-stationary mixed-precision systolic array. On modeled Jetson-class platforms with 1.5B/7B models, the full stack reports 3.79x/3.96x energy reduction and 2.88x/4.44x latency speedup, with less than one absolute percentage point of benchmark-score degradation from the uncompressed baseline.

**Novelty assessment:** Moderate-to-high. Block-diffusion LLMs are a newer architecture class with different caching/compute properties than autoregressive transformers, and the memory-hierarchy co-design (wide-I/O DRAM interface + mixed-precision systolic array + three distinct FFN-weight compression strategies chosen per drift pattern) is a substantive systems contribution rather than a straightforward application of existing quantization techniques.

**Relevance score:** 4/5 — strong candidate for [[Quantization]] and Hardware; reports both accuracy-preservation numbers and hardware-level energy/latency figures on modeled real platforms (Jetson-class), though results are simulation/modeled rather than measured on physical silicon.

---

## 4. FALCON: Fault-Tolerant Magnetic Tunnel Junction-Based In-Memory Stochastic Architecture for Reliability-Critical Edge AI Applications

**Source:** arXiv:2609.00701 (cs.ET; cross-listed cs.AR, eess.IV) — submitted 1 Sep 2026
**Authors:** Farzad Razi, Mehran Moghadam, Sercan Aygun, M. Hassan Najafi, Marc Riedel
**Link:** https://arxiv.org/abs/2609.00701

**Why it matters:** Targets a hardware-reliability problem: in-memory computing (IMC) with emerging non-volatile memory (Magnetic Tunnel Junctions) is attractive for edge AI's memory-wall and energy constraints, but conventional binary-radix IMC is fragile under process variation and thermal noise — exactly the conditions edge deployments face outside controlled data-center environments.

**Technical summary:** FALCON combines MTJ-based in-memory arithmetic with stochastic computing (encoding values as bit-streams, which naturally tolerates localized soft errors) plus a deterministic bit-mapping mechanism and reconfigurable logic-in-memory structures, avoiding both external-processor round-trips and area/power-hungry random-number generators. Validated in 14nm FinFET technology, it maintains correct functionality under aggressive voltage scaling, severe process variation, and noise injection up to 30%, demonstrated on a noise-tolerant image-processing case study (morphological closing).

**Novelty assessment:** Moderate. Stochastic computing and MTJ-based IMC are each individually established research directions, but their combination with a reconfigurable logic-in-memory structure and demonstrated 30%-noise tolerance at 14nm is a solid, quantified reliability contribution — relevant less as a new algorithm and more as a hardware building block for edge deployments in harsh or uncontrolled environments (industrial, automotive).

**Relevance score:** 3/5 — a useful reliability/hardware data point that does not map cleanly onto the taxonomy's existing Hardware nodes ([[Cortex-M]]/[[Cortex-A]], [[RISC-V]], [[DSP]], [[FPGA]], [[NPU]]) — in-memory computing with emerging non-volatile memory as a distinct hardware category.

---

## 5. Recent Developments in Transformer Inference Deployment on FPGA Platforms: A Survey

**Source:** arXiv:2609.01212 (cs.LG; cross-listed cs.AR) — submitted 1 Sep 2026; published in Journal of Systems Architecture, Vol. 177 (2026)
**Authors:** Arjan Blankestijn, Uraz Odyurt, Amirreza Yousefzadeh
**Link:** https://arxiv.org/abs/2609.01212

**Why it matters:** A systematic literature review specifically on Transformer inference on [[FPGA]] platforms — exactly the kind of citable, taxonomy-organizing reference worth keeping on hand when writing a survey. Already peer-reviewed and published (not just a preprint), which strengthens its citability.

**Technical summary:** The authors perform a systematic review of recent techniques and design choices for deploying Transformer-based models on FPGA accelerators, covering both operational-performance concerns (throughput, latency) and efficiency concerns (energy), and propose a taxonomy of implementation/optimization techniques intended as a guide for both academic and industry researchers.

**Novelty assessment:** Low as a technical contribution (it is a survey, not a new method), but high as a reference-value contribution — a recent, peer-reviewed taxonomy of FPGA/Transformer deployment techniques.

**Relevance score:** 3/5 — a standing reference for the [[FPGA]] branch and for any future survey-writing or literature-scoping work touching Transformer-on-FPGA deployment, rather than a deep-analysis candidate in its own right.

---

## 6. LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing

**Source:** arXiv:2608.25321 (cs.CR; cross-listed cs.AI) — submitted 25 Aug 2026
**Authors:** Dev Mehta, Lily Dukette, William Folan, Olivia Kochol, Noah Solomon, Shahin Tajik, Fatemeh Ganji
**Link:** https://arxiv.org/abs/2608.25321

**Why it matters:** As LLM inference moves onto edge AI accelerators (the hardware tracked under [[NPU]], [[FPGA]], etc.), those chips introduce physical attack surfaces that model-level security research does not cover. This paper demonstrates that model weights and intermediate values can potentially be physically extracted from an edge accelerator via optical probing — see [[Hardware_Security_of_Edge_AI_Accelerators]].

**Technical summary:** LLMscope exploits the fact that edge AI LLM accelerators reuse the same buffers and compute subcircuits across memory addresses, tiles, modules, and layers — meaning that probing a small number of physical memory locations during inference execution can recover asset values (weights, activations) across the whole model. The authors demonstrate full recovery of targeted values in their setup and establish a methodology for reconstructing asset values even when some individual weights or bits cannot be directly probed.

**Novelty assessment:** High. Physical/hardware-level extraction attacks against edge AI accelerators specifically (as opposed to cloud-side model-stealing via API queries) are a comparatively unexplored threat model, and the "shared buffers/subcircuits across tiles" observation is a specific, exploitable structural property of accelerator design rather than a generic side-channel claim.

**Relevance score:** 4/5 — a genuinely new research direction in hardware/physical security of edge AI accelerators.

---

## Suggested thesis / research hooks

- **Multitasking-aware serving as a general edge-LLM design constraint:** mzCache addresses OS-level memory pressure from concurrent apps for on-device LLM inference, but the same problem (shared-memory contention under multitasking) likely applies to any always-on edge ML workload sharing a mobile SoC (e.g. a keyword-spotting model running alongside a periodically-invoked LLM). A Master's-scale study could ask whether mzCache's restoration-oriented memory management generalizes to mixed classical-ML/LLM workloads on the same device.
- **Generalizing "weight-tying enables one-directional split learning" beyond fine-tuning:** L-shaped split fine-tuning's core trick (using tied input/output embeddings to supervise server-side activations without returning outputs to the client) is specific to fine-tuning with a fixed embedding table. Does an analogous trick exist for split *inference* (not just training) with other parameter-sharing architectures (e.g. encoder-decoder models with tied embeddings)? A well-scoped PhD-level systems question bridging [[Federated_Learning]] and split-inference serving.
- **Threat-modeling edge AI accelerators beyond optical probing:** LLMscope demonstrates one physical extraction channel (optical probing exploiting buffer/subcircuit reuse). A systematic comparative study of which edge accelerator architectures ([[NPU]] designs, systolic arrays, in-memory-computing designs like FALCON's) are more or less structurally vulnerable to this class of attack — and what countermeasures (e.g. address randomization, buffer partitioning) cost in area/energy — would be a strong PhD-scale contribution bridging hardware architecture and security ([[Hardware_Security_of_Edge_AI_Accelerators]]).
- **Reliability-by-construction for edge in-memory computing beyond stochastic computing:** FALCON uses stochastic computing to tolerate MTJ noise/variation. A Master's-scale comparative study could evaluate whether stochastic-computing-based reliability and aggressive fixed-point [[Quantization]] compose well (or conflict) when applied to the same in-memory-computing substrate.
