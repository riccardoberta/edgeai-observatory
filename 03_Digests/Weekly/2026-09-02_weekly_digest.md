# Weekly Digest — 2026-09-02

Source scope: arXiv (cs.LG, cs.AR, cs.DC, eess.SP), per `00_Config/sources.yaml`, plus optional cross-checks via IEEE Xplore and Google Scholar (Claude in Chrome, unige.it institutional access reachable this cycle). Six items selected this cycle, submitted 25 Aug – 1 Sep 2026. The previous digest (2026-08-31) covered submissions through 26 Aug 2026, so this cycle's arXiv window is 27 Aug – 2 Sep 2026 (~7 days); one Scholar-sourced pick (#6, LLMscope) is dated 25 Aug and falls just before that window but in categories (cs.CR/cs.AI) neither digest's routine sweep covers, so it is included here as a genuine gap-filler rather than a duplicate. This week's picks span on-device LLM serving infrastructure (memory management, split fine-tuning), hardware-accelerator co-design for edge LLM inference, a reliability-focused in-memory computing architecture, an FPGA/Transformer survey, and — new for the Observatory — a physical-security angle on edge AI chips. Touches [[Quantization]], [[FPGA]], [[NPU]], [[Federated Learning]], and reinforces the recurring "edge LLM serving infrastructure" taxonomy gap flagged in prior digests (see Taxonomy note below), while also surfacing a new gap around hardware security of edge AI accelerators.

**Sourcing note (methodology, this cycle):** cs.AR was retrieved via its "recent" listing with full clean coverage of 27 Aug – 2 Sep 2026 (46 entries, no gaps). cs.DC "recent" listing covered 72 entries total; the first 50 (Wed 2 Sep through the first 8 of 14 entries on Fri 28 Aug) were reviewed, but the remaining ~6 entries from Fri 28 Aug and all of Thu 27 Aug (entries 51–72) were not reached this cycle — a coverage gap to close next cycle, ideally via pagination or the "all" view. eess.SP is high-volume (126 entries this week); only the first 50 were reviewed (all of Wed 2 Sep, plus the first 23 of 41 entries on Tue 1 Sep), so Mon 31 Aug back through Thu 27 Aug were not swept — a larger gap than usual for this source, noted for next cycle. cs.LG was not swept directly given its volume (a standing caveat across cycles); candidates were surfaced only via cross-listings from the cs.AR/cs.DC/eess.SP sweeps and via the FPGA survey pick, which is primary-listed in cs.LG. IEEE Xplore was reachable via Claude in Chrome this cycle, but its search-result listing does not expose reliable per-item indexing dates, so candidates surfaced there were not scored directly (risk of misdating a claim); a promising item ("A Comparative Benchmark and Decision Guide for Edge AI Deployment... on Resource-Constrained IMU Sensor Nodes", ICERA 2026) was seen but not verified as new-this-week and is flagged only for a possible future look. ACM Digital Library was blocked by a bot/security-verification interstitial this cycle and could not be searched. Google Scholar (`scisbd=1`, filtered to 2026) was reachable with working unige.it institutional full-text links ("Testo completo su UNIGE") and surfaced pick #6 (LLMscope) directly; a handful of targeted searches were run, consistent with the sparing-use guidance for this source.

---

## 1. mzCache: On-Device LLM Memory Management under Multitasking

**Source:** arXiv:2609.01338 (cs.OS; cross-listed cs.DC, cs.LG) — submitted 1 Sep 2026; accepted at MobiCom 2026
**Authors:** Hongseung Yu, Minsung Kim, Jongseok Park, Kyunghan Lee
**Link:** https://arxiv.org/abs/2609.01338

**Why it matters:** Directly addresses the "edge LLM serving infrastructure" gap this Observatory has flagged repeatedly in recent digests (see Taxonomy note). Mobile on-device LLM inference is typically evaluated in isolation, but real phones run multiple apps concurrently, and OS-level memory pressure evicting model weights/KV cache is a real, previously under-addressed deployment obstacle. Accepted at MobiCom 2026, a top systems venue, and implemented as a real Android app on llama.cpp rather than simulated.

**Technical summary:** mzCache partitions LLM memory (weights + KV cache) into fine-grained shared buffers, enabling partial eviction/restoration with concurrent CPU-GPU access over the unified memory of mobile SoCs. Hybrid swap and "backward-out" eviction policies allow low-latency restoration from any eviction state, avoiding both slow storage reads and full KV-cache recomputation when a suspended app resumes inference. Measured on real hardware (Android devices), it achieves a 2.1–5.5× reduction in Time-to-First-Token versus storage-backed partial offload in real multitasking scenarios.

**Novelty assessment:** High as systems infrastructure. The problem framing (multitasking-induced memory pressure on on-device LLM serving) is under-studied relative to single-app benchmarks, and the OS/GPU co-design (restoration-oriented memory management with concurrent cross-processor access) is a genuinely new mechanism, not an incremental tuning of an existing scheme.

**Relevance score:** 5/5 — strongest deep-analysis candidate this week: real Android deployment, top-tier venue (MobiCom), and a concrete, measured improvement (2.1–5.5×) on a deployment obstacle (multitasking memory pressure) not addressed by prior edge-LLM serving work in the Observatory's records.

---

## 2. Just Talk Once: Communication-Efficient Split Federated LLM Fine-Tuning on Edge Devices

**Source:** arXiv:2609.01457 (cs.DC) — submitted 1 Sep 2026; accepted at ACM MobiHoc 2026
**Authors:** Jiaxiang Geng, Xianhao Chen, Bing Luo
**Link:** https://arxiv.org/abs/2609.01457

**Why it matters:** Extends [[Federated Learning]] into the LLM fine-tuning regime under the memory/bandwidth constraints that define edge deployment. Split federated learning (splitting model layers between client and server) usually still requires continuous bidirectional client involvement during training, which is a poor fit for intermittently-connected edge devices; this paper removes that requirement.

**Technical summary:** L-shaped SFT exploits weight tying in modern LLMs so server-side hidden activations can be supervised directly with target embeddings, letting training loss be computed server-side without sending outputs back to the client. Building on this, one-shot SFT lets clients upload activations once and go offline while the server continues optimizing over cached representations — eliminating the step-by-step communication loop of conventional split fine-tuning. Evaluated on a real testbed mixing commercial smartphones and NVIDIA developer boards as heterogeneous edge clients, showing significant reductions in both communication cost and client online time versus existing split-fine-tuning baselines.

**Novelty assessment:** Moderate-to-high. The weight-tying insight enabling one-directional (server-only) loss computation is a clean, non-obvious mechanism specific to how modern LLMs share input/output embeddings, and the one-shot (upload-once, go-offline) client model is a meaningful departure from the continuous-participation assumption that pervades federated/split learning literature.

**Relevance score:** 4/5 — good deep-analysis candidate for the [[Federated Learning]] branch: real heterogeneous-hardware testbed (smartphones + Jetson-class boards), a mechanism (weight-tying exploitation) that could generalize to other split-learning schemes, and direct relevance to intermittent-connectivity edge scenarios.

---

## 3. Hardware Acceleration of Block-Diffusion LLM for Edge Devices

**Source:** arXiv:2609.01084 (cs.AR) — submitted 1 Sep 2026
**Authors:** Wei-Hsing Huang, Kiseok Lee, Ming-Yen Lee, Weiyu Sun, Cheng-Jhih Shih, Gayatri Tanksali, Arpit Khandelwal, Pin-Jun Chen, Yingyan Celine Lin, Shimeng Yu
**Link:** https://arxiv.org/abs/2609.01084

**Why it matters:** A concrete hardware/algorithm co-design for a still-uncommon LLM architecture family (block-diffusion LLMs) targeting single-stream, batch-one edge inference specifically — the regime where weight-traffic amortization tricks used in server-side batched serving do not apply. Involves Yingyan Celine Lin and Shimeng Yu, both established names in efficient-ML hardware research.

**Technical summary:** The paper co-designs three components: WIFiV-LPDDR (a wide-I/O LPDDR memory system for precision-tagged reads), BRQ-KV (a low-rank-plus-INT8-residual [[Quantization]] scheme for the KV-cache prefix with query-dependent per-entry precision), and DAT-FFN (drift-mapped canonical replacement / low-bit delta / cached-state carry for FFN weights, keeping live activations unquantized). All three map onto a single input-stationary mixed-precision systolic array. On modeled Jetson-class platforms with 1.5B/7B models, the full stack reports 3.79×/3.96× energy reduction and 2.88×/4.44× latency speedup, with less than one absolute percentage point of benchmark-score degradation from the uncompressed baseline.

**Novelty assessment:** Moderate-to-high. Block-diffusion LLMs are a newer architecture class with different caching/compute properties than autoregressive transformers, and the memory-hierarchy co-design (wide-I/O DRAM interface + mixed-precision systolic array + three distinct FFN-weight compression strategies chosen per drift pattern) is a substantive systems contribution rather than a straightforward application of existing quantization techniques.

**Relevance score:** 4/5 — strong candidate for the [[Quantization]] and Hardware branches; reports both accuracy-preservation numbers and hardware-level energy/latency figures on modeled real platforms (Jetson-class), though results are simulation/modeled rather than measured on physical silicon.

---

## 4. FALCON: Fault-Tolerant Magnetic Tunnel Junction-Based In-Memory Stochastic Architecture for Reliability-Critical Edge AI Applications

**Source:** arXiv:2609.00701 (cs.ET; cross-listed cs.AR, eess.IV) — submitted 1 Sep 2026
**Authors:** Farzad Razi, Mehran Moghadam, Sercan Aygun, M. Hassan Najafi, Marc Riedel
**Link:** https://arxiv.org/abs/2609.00701

**Why it matters:** Targets a hardware-reliability problem largely absent from the Observatory's current taxonomy: in-memory computing (IMC) with emerging non-volatile memory (Magnetic Tunnel Junctions) is attractive for edge AI's memory-wall and energy constraints, but conventional binary-radix IMC is fragile under process variation and thermal noise — exactly the conditions edge deployments face outside controlled data-center environments.

**Technical summary:** FALCON combines MTJ-based in-memory arithmetic with Stochastic Computing (encoding values as bit-streams, which naturally tolerates localized soft errors) plus a deterministic bit-mapping mechanism and reconfigurable logic-in-memory structures, avoiding both external-processor round-trips and area/power-hungry random number generators. Validated in 14nm FinFET technology, it maintains correct functionality under aggressive voltage scaling, severe process variation, and noise injection up to 30%, demonstrated on a noise-tolerant image-processing case study (morphological closing).

**Novelty assessment:** Moderate. Stochastic computing and MTJ-based IMC are each individually established research directions, but their combination with a reconfigurable logic-in-memory structure and demonstrated 30%-noise tolerance at 14nm is a solid, quantified reliability contribution — relevant less as a new algorithm and more as a hardware building block for edge deployments in harsh or uncontrolled environments (industrial, automotive).

**Relevance score:** 3/5 — a useful reliability/hardware data point that doesn't map cleanly onto the current Hardware taxonomy (Cortex-M/A, RISC-V, DSP, FPGA, NPU); worth flagging as a possible new taxonomy node ("in-memory computing / emerging non-volatile memory") rather than forcing it into an existing category.

---

## 5. Recent Developments in Transformer Inference Deployment on FPGA Platforms: A Survey

**Source:** arXiv:2609.01212 (cs.LG; cross-listed cs.AR) — submitted 1 Sep 2026; published in Journal of Systems Architecture, Vol. 177 (2026)
**Authors:** Arjan Blankestijn, Uraz Odyurt, Amirreza Yousefzadeh
**Link:** https://arxiv.org/abs/2609.01212

**Why it matters:** A systematic literature review specifically on Transformer inference on [[FPGA]] platforms — exactly the kind of citable, taxonomy-organizing reference the Observatory's design principles call for ("which papers should be cited when writing a survey"). Already peer-reviewed and published (not just a preprint), which strengthens its citability.

**Technical summary:** The authors perform a systematic review of recent techniques and design choices for deploying Transformer-based models on FPGA accelerators, covering both operational-performance concerns (throughput, latency) and efficiency concerns (energy), and propose a taxonomy of implementation/optimization techniques intended as a guide for both academic and industry researchers.

**Novelty assessment:** Low as a technical contribution (it is a survey, not a new method), but high as a reference-value contribution — a recent, peer-reviewed taxonomy of FPGA/Transformer deployment techniques is exactly the sort of source this Observatory should cite when writing surveys or scoping new FPGA-related thesis topics.

**Relevance score:** 3/5 — not a deep-analysis candidate for extraction of a single technical contribution, but recommended as a standing reference for the [[FPGA]] taxonomy branch and for any future survey-writing or literature-scoping work touching Transformer-on-FPGA deployment.

---

## 6. LLMscope: Extracting LLM Assets from Edge AI Chips via Optical Probing

**Source:** arXiv:2608.25321 (cs.CR; cross-listed cs.AI) — submitted 25 Aug 2026; found via Google Scholar (unige.it institutional access), not the routine arXiv category sweep
**Authors:** Dev Mehta, Lily Dukette, William Folan, Olivia Kochol, Noah Solomon, Shahin Tajik, Fatemeh Ganji
**Link:** https://arxiv.org/abs/2608.25321

**Why it matters:** A new dimension for the Observatory: as LLM inference moves onto edge AI accelerators (the hardware this Observatory tracks under [[NPU]], [[FPGA]], etc.), those chips introduce physical attack surfaces that model-level security research does not cover. This paper demonstrates that model weights and intermediate values can potentially be physically extracted from an edge accelerator via optical probing — a hardware-security concern directly relevant to any lab deploying proprietary or licensed models on edge silicon.

**Technical summary:** LLMscope exploits the fact that edge AI LLM accelerators reuse the same buffers and compute subcircuits across memory addresses, tiles, modules, and layers — meaning that probing a small number of physical memory locations during inference execution can recover asset values (weights, activations) across the whole model. The authors demonstrate full recovery of targeted values in their setup and establish a methodology for reconstructing asset values even when some individual weights or bits cannot be directly probed.

**Novelty assessment:** High. Physical/hardware-level extraction attacks against edge AI accelerators specifically (as opposed to cloud-side model-stealing via API queries) are a comparatively unexplored threat model, and the "shared buffers/subcircuits across tiles" observation is a specific, exploitable structural property of accelerator design rather than a generic side-channel claim.

**Relevance score:** 4/5 — flags a genuinely new research direction and a taxonomy gap (hardware/physical security of edge AI accelerators) not yet represented in the Observatory's Algorithms/Frameworks/Hardware/Applications structure; worth a deep-analysis record and consideration as a new taxonomy branch.

---

## Candidates for deep analysis (`02_Papers/`)

No deep-analysis records were created automatically this cycle. In priority order:

- **#1 mzCache (arXiv:2609.01338)** — the strongest candidate: MobiCom 2026, real Android deployment, and a measured 2.1–5.5× TTFT improvement on a previously under-addressed problem (multitasking memory pressure for on-device LLM serving).
- **#6 LLMscope (arXiv:2608.25321)** — worth a deep record to seed a possible new "hardware security of edge AI accelerators" taxonomy branch; a genuinely novel threat model with a demonstrated full-recovery attack.
- **#2 Just Talk Once (arXiv:2609.01457)** — worth a deep record for the [[Federated Learning]] branch: real heterogeneous testbed (smartphones + Jetson boards) and a mechanism (weight-tying exploitation for one-directional loss computation) that could generalize beyond this specific split-learning scheme.
- **#3 Hardware Acceleration of Block-Diffusion LLM (arXiv:2609.01084)** — worth a deep record for the [[Quantization]] branch given the three-way FFN-compression co-design and strong reported energy/latency numbers, with the caveat that results are on modeled rather than measured hardware.

## Suggested thesis / research hooks this week

- **Multitasking-aware serving as a general edge-LLM design constraint:** mzCache addresses OS-level memory pressure from concurrent apps for on-device LLM inference, but the same problem (shared-memory contention under multitasking) likely applies to any always-on edge ML workload sharing a mobile SoC (e.g., a keyword-spotting model running alongside a periodically-invoked LLM). A Master's-scale study could ask whether mzCache's restoration-oriented memory management generalizes to mixed classical-ML/LLM workloads on the same device.
- **Generalizing "weight-tying enables one-directional split learning" beyond fine-tuning:** L-shaped SFT's core trick (using tied input/output embeddings to supervise server-side activations without returning outputs to the client) is specific to fine-tuning with a fixed embedding table. Does an analogous trick exist for split *inference* (not just training) with other parameter-sharing architectures (e.g., encoder-decoder models with tied embeddings)? A well-scoped PhD-level systems question bridging [[Federated Learning]] and split-inference serving.
- **Threat-modeling edge AI accelerators beyond optical probing:** LLMscope demonstrates one physical extraction channel (optical probing exploiting buffer/subcircuit reuse). A systematic comparative study of which edge accelerator architectures (NPU designs, systolic arrays, IMC-based designs like FALCON's) are more or less structurally vulnerable to this class of attack — and what countermeasures (e.g., address randomization, buffer partitioning) cost in area/energy — would be a strong PhD-scale contribution bridging hardware architecture and security, and a natural first entry for a new Observatory taxonomy branch.
- **Reliability-by-construction for edge IMC beyond stochastic computing:** FALCON uses stochastic computing to tolerate MTJ noise/variation. Given the Observatory's existing interest in [[Quantization]] and low-precision inference, a Master's-scale comparative study could evaluate whether stochastic-computing-based reliability and aggressive fixed-point quantization compose well (or conflict) when applied to the same in-memory-computing substrate.

---

## Taxonomy note

Two candidate additions to the taxonomy emerged this cycle rather than being adopted unilaterally, per the Observatory's "continuously refine the taxonomy" principle: (1) **in-memory computing / emerging non-volatile memory** as a Hardware branch entry (motivated by FALCON's MTJ-based design this week, and relevant to prior digests' accelerator coverage that didn't fit cleanly into Cortex-M/A, RISC-V, DSP, FPGA, or NPU), and (2) **hardware/physical security of edge AI accelerators** as either a new Applications-adjacent branch or a cross-cutting concern (motivated by LLMscope this week — the first security-focused pick in recent digest history). Neither is created automatically; both are flagged for Ricky's consideration. Separately, the "edge LLM serving infrastructure" gap flagged in the 2026-08-20, 2026-08-23, and 2026-08-31 digests remains open and is reinforced again this week by mzCache and Just Talk Once, both of which concern *how* LLMs get served/fine-tuned on constrained devices rather than new model or compression algorithms.

---

**Notes:** All six picks were verified at the abstract level from their arXiv pages (via direct fetch or Claude in Chrome); none has yet been read in full-PDF depth, so the specific figures cited here (mzCache's 2.1–5.5× TTFT reduction; the block-diffusion accelerator's 3.79×/3.96× energy and 2.88×/4.44× latency figures on modeled Jetson-class platforms; FALCON's 30%-noise-tolerance claim at 14nm; LLMscope's "full recovery" claim) should be re-verified before citation in a survey or thesis. cs.AR had full clean coverage of 27 Aug – 2 Sep. cs.DC and eess.SP both had partial coverage this cycle (cs.DC: missing ~22 entries from Thu 27–Fri 28 Aug; eess.SP: missing all of Mon 31 Aug through Thu 27 Aug, a larger-than-usual gap given eess.SP's high volume this week, 126 entries) — both should be retried with a different retrieval strategy (e.g., the arXiv API's date-range query, if reachable, or the paginated "all" view) next cycle. cs.LG was not swept directly given its volume, a standing caveat. IEEE Xplore was reachable via Claude in Chrome but its search UI does not expose reliable per-item dates, so no IEEE-sourced picks were scored this cycle (one candidate noted for a possible future look). ACM Digital Library was blocked by a bot-check interstitial. Google Scholar was reachable with working unige.it full-text links and directly sourced pick #6. `sources.yaml` `last_checked` for arXiv should be advanced to 2026-09-02; IEEE Xplore's and Google Scholar's `last_checked` could reasonably be advanced too since both were reachable this cycle, though neither produced a fully verified new-this-week date for every candidate seen.
