# Weekly Digest — 2026-09-20

Five items spanning a controlled cross-platform measurement study showing that INT8 quantization is not portable across edge accelerators, an open-source TinyML vision stack running on commercial smart glasses, a noise-robust 16k-parameter keyword-spotting model deployed on an ESP32, an edge-native compact sensor foundation model for human activity recognition, and an offline predictor of quantization-induced task degradation for robot world-action models validated on a real manipulator. Touches [[Quantization]], [[NPU]], [[Cortex-A]], [[Cortex-M]], [[ONNX_Runtime]], [[TensorFlow_Lite_Micro]], [[CMSIS-NN]], [[MLPerf_Tiny]], [[Vision]], [[Keyword_Spotting]], [[Human_Activity_Recognition]], and [[Pruning]].

Covers papers first listed between 14 and 20 September 2026.

---

## 1. Is INT8 Portable? A Cross-Platform Measurement Study of Quantized Inference on Embedded and Automotive Accelerators

**Source:** arXiv:2609.16085 (cs.AR; cross-listed cs.LG, cs.PF) — submitted 14 Sep 2026
**Authors:** Yuyeong Shin (KATECH, per artifact repository)
**Link:** https://arxiv.org/abs/2609.16085 — open artifact (scripts + 32 measurement reports): https://github.com/yyshin-katech/embedded-ai-quantization-guide/tree/paper1-v1

**Why it matters:** "Quantize once, deploy anywhere" is the default working assumption behind most [[Quantization]] pipelines and behind cross-framework runtimes like [[ONNX_Runtime]]. This paper tests that assumption with a controlled experiment across seven hardware classes and finds it fails on three independent axes. It is also the first paper found that offers a *reusable, open cross-chip measurement methodology* at the edge-accelerator tier — earlier measurement work was either a Jetson-/Apple-silicon-tier framework ([[2026_Taherin_Hydra]], [[2026_Bryngelson_AppleNeuralEngine]]) or a single fabricated chip's self-reported numbers (EPIC) — which bears directly on the measurement-infrastructure gap listed in the taxonomy's known gaps.

**Technical summary:** The study holds the ONNX artifact and the quantization scales fixed so that the integer kernel or ISA is the only free variable, then measures the same INT8 model on ARM and x86 CPUs, a discrete GPU, an NVIDIA Jetson AGX Orin iGPU and its NVDLA cores, and two vendor NPUs (Qualcomm Hexagon HTP, DEEPX DX-M1). Three findings: (1) the *sign* of the INT8 speedup is set by whether the CPU has a dot-product ISA (ARM SDOT / x86 VNNI) — cores with it speed up by up to 2.1×, cores without it slow down by 1.7× for the identical model and runtime; (2) INT8 outputs are not portable, and the rule is an invariance rather than a gradient: FP32 predictions are bit-identical across every pair of targets (1000/1000), INT8 predictions agree 1000/1000 only when two targets share an integer kernel and 958–965/1000 whenever they do not, regardless of whether the boundary is CPU↔CPU or CPU↔accelerator — and this is invisible to top-1 accuracy, which is preserved; (3) vendor NPUs "own" quantization: a bring-your-own QDQ graph fails silently on one NPU (external scales ignored, accuracy 0.75 → 0.005 while it compiles, profiles and runs without error) and loudly on the other (compiler refuses the graph), so only the vendor-native path yields a correct engine. A fixed-compute sweep further shows edge-NPU latency regimes are set by output/device-to-host transfer size rather than compute.

**Novelty assessment:** Moderate-to-high. Individual observations (ISA-dependent INT8 speedups, vendor-specific quantizers) are known folklore among practitioners, but a controlled, artifact-fixed, seven-platform measurement that turns them into quantified, reproducible rules — and in particular the "per-input determinism is lost across kernel boundaries even when accuracy is unchanged" invariance — is new and directly actionable for safety-critical (automotive) deployments where redundancy across heterogeneous units is assumed to be consistent.

**Relevance score:** 5/5 — open scripts and reports, a reusable cross-platform methodology, findings that cut across the Algorithms ([[Quantization]]), Frameworks ([[ONNX_Runtime]]) and Hardware ([[NPU]], [[Cortex-A]]) branches, and the strongest independent evidence to date that INT8 portability needs a measurement methodology of its own. Caveat: single author, preprint, not yet peer-reviewed; the MCU-class tier (Cortex-M, Ethos-U) is *not* covered.

---

## 2. Deploying TinyML on Commercial Smart Glasses

**Source:** EWSN 2026, EMERGE workshop (found via Google Scholar; open PDF on ewsn.org) — indexed ~17 Sep 2026
**Authors:** Patrick Krumpl, Francesco Corti, Dong Wang, Olga Saukh (Graz University of Technology; Complexity Science Hub Vienna)
**Link:** https://ewsn.org/file-repository/ewsn2026/emerge26-final1.pdf — open firmware: https://github.com/pkrumpl/frame-codebase

**Why it matters:** Most "AI smart glasses" offload inference to a phone or the cloud. This paper asks whether useful [[Vision]] inference can run *on* a commercially available, nRF52840-based ([[Cortex-M]]4) wearable, and answers with a full open-source firmware integration of [[TensorFlow_Lite_Micro]] accelerated by [[CMSIS-NN]] inside a production wearable stack (Bluetooth, camera, display, FPGA runtime, Lua). Its most reusable finding is methodological: once realistic firmware overhead is accounted for, the effective TinyML budget shrinks to ~270 kB flash / ~200 kB SRAM, and the bottlenecks differ from those bare-metal MCU benchmarks like [[MLPerf_Tiny]] measure.

**Technical summary:** Two workloads are deployed on Brilliant Labs Frame glasses: a MobileNetV1-based Visual Wake Words classifier and a FOMO-style centroid object detector (Edge Impulse lineage). The MLPerf Tiny VWW INT8 reference (325.5 kB) does not fit; a custom α=0.18 RGB INT8 variant (186 kB, ~43% less flash) reaches 81.6% top-1 on MS COCO minival, above the 80% MLPerf Tiny quality target. FOMO is SRAM-bound instead (238 kB arena at 96×96 INT8), and only a retrained 64×64 variant (114.7 kB arena) fits. CMSIS-NN reduces inference latency 13.8× for VWW (6763 → 491 ms) and 9.5× for FOMO (2552 → 268 ms) versus TFLM reference kernels, measured with the Cortex-M4 DWT cycle counter. End-to-end, though, one VWW pipeline iteration takes ~1.3 s (0.75 Hz), with image acquisition (41%) and JPEG-over-SPI preprocessing (22%) dominating — inference is only 37%. TFLM + CMSIS-NN add ~102 kB constant flash overhead; INT8 does not achieve the theoretical 4× size reduction because FlatBuffer topology/metadata are unchanged by quantization.

**Novelty assessment:** Moderate. The models and runtime are standard; the contribution is the systems-integration study on a real sealed consumer device and the quantified observation that sensor/preprocessing pipelines and firmware co-residency, not the neural network, set the practical limits — a point the authors explicitly raise as a benchmarking gap for TinyML.

**Relevance score:** 4/5 — real hardware, open code, standard benchmark (MLPerf Tiny VWW), and a Frameworks-branch result ([[TensorFlow_Lite_Micro]] + [[CMSIS-NN]]) with an unusual level of measurement detail for a wearable deployment. Workshop paper, single platform, no energy measurement.

---

## 3. SAMSTeG: A Noise-Robust Architecture for Low Parameter Edge Keyword Spotting

**Source:** IEEE Embedded Systems Letters (Early Access) — published 14 Sep 2026 (found via Google Scholar)
**Authors:** Shreyas Ramasubramanian, Aman Jayesh, Alan Nelson, Akshat Puneet, Mukund Hebbar, Srikar Somanchi, Abhishek Srivastava (IIIT Hyderabad)
**DOI:** [10.1109/LES.2026.3732944](https://doi.org/10.1109/LES.2026.3732944) — [IEEE Xplore](https://ieeexplore.ieee.org/document/11690602)

**Why it matters:** Small [[Keyword_Spotting]] models are routinely benchmarked on clean Speech Commands audio; the authors report that state-of-the-art small models lose more than 25 percentage points on average at 0 dB SNR, which is the regime always-on devices actually operate in. SAMSTeG targets that gap with a 15,886-parameter architecture and validates it on an ESP32 rather than only in simulation.

**Technical summary:** The architecture combines Hybrid Dropout with Split Activation (to prevent feature collapse in shallow networks) with a Multi-Scale Temporal Gating block for dynamic noise suppression that costs only 964 parameters. It reaches 96.32% clean accuracy with 800K MACs, degrades by an average 12.87 points at 0 dB SNR (vs. >25 for the compared baselines), and maintains 81.59–89.81% accuracy at 0 dB across four noise types. On the ESP32 it runs at 97 ms latency in 34.2 KB RAM at 27.6 mJ per inference (development board).

**Novelty assessment:** Moderate. Temporal gating and multi-scale features are established; the specific combination and the explicit noise-robustness evaluation protocol across noise types and SNRs at a ~16k-parameter budget is a useful, well-measured contribution rather than a new idea. The ESP32 energy figure is board-level, not chip-level.

**Relevance score:** 4/5 — peer-reviewed, real MCU deployment with latency/RAM/energy numbers, and a robustness framing that complements the accuracy-per-parameter framing the [[Keyword_Spotting]] concept page currently emphasizes. Note that a second tiny-KWS paper appeared the same week (CircleMatch, see "Also noted"), pushing the parameter budget an order of magnitude lower.

---

## 4. EdgeHAR: An Edge-Native Compact Sensor Foundation Model for Human Activity Recognition

**Source:** arXiv:2609.14498 (cs.LG; cross-listed cs.AI) — submitted 13 Sep 2026; ACM DOI 10.1145/3798063.3837321 registered (not yet live on dl.acm.org at time of writing)
**Authors:** He Zhang, Siyu Yuan, Siyu Liu, Sizhen Bian, Bin Guo
**Link:** https://arxiv.org/abs/2609.14498 (CC BY 4.0)

**Why it matters:** Sensor foundation models for [[Human_Activity_Recognition]] have so far been built for cloud-scale deployment and are brittle under the real sensing shifts wearables face — unseen users, devices, sampling rates and placements. EdgeHAR is an attempt to get foundation-model-level transferability while respecting edge compute, memory, latency and privacy constraints, a step beyond the domain-generalization-only work that has dominated [[Human_Activity_Recognition]] recently.

**Technical summary:** EdgeHAR factorizes IMU signals into three latent codes — an Activity-Semantic Code (reusable activity knowledge), a Motion-Dynamics Code (temporal patterns) and an Acquisition-Context Code (sensor-specific variation) — so that activity knowledge is disentangled from acquisition variability. Lightweight adaptation modules then let the compact model adapt to new users, devices, placements and activity classes with limited target-domain data. Across heterogeneous HAR datasets it is reported to maintain competitive recognition under distribution shift at substantially reduced deployment cost. The abstract does not state parameter counts, target hardware, or measured latency/memory; those need to be checked in the full text before any deep-analysis record.

**Novelty assessment:** Moderate-to-high in framing (an explicitly *edge-first* sensor foundation model with a disentangled representation), but the concrete edge-deployment evidence is not visible from the abstract. Two other HAR papers this week (a coverage-aware virtual-IMU augmentation framework, arXiv:2609.16768, and a systematic domain-generalization analysis for smartphone HAR, arXiv:2609.14863) confirm that data scarcity and acquisition shift remain the branch's central problems.

**Relevance score:** 4/5 — squarely on an Applications-branch concept, open-access, with an ACM venue behind it; provisional until the full text confirms actual edge footprint numbers.

---

## 5. Predict Before You Deploy: Offline Prediction of Quantization-Induced Task Degradation for World Action Models

**Source:** arXiv:2609.19441 (cs.RO; cross-listed cs.AI) — submitted 16 Sep 2026
**Authors:** Jiuyi Xu, Jinjia Guo, Meida Chen, Jing Du, Yangming Shi
**Link:** https://arxiv.org/abs/2609.19441 — code: https://github.com/jiuyixu25/PreDE

**Why it matters:** Post-training [[Quantization]] of video-generation-backbone world action models (WAMs) for on-robot deployment has a large configuration space (bit width, grouping, quantizer), and the only reliable way to know whether a configuration preserves task success has been expensive closed-loop robot evaluation. PreDE turns this into a calibrated offline decision. Together with a second, independent paper on recovering aggressively pruned VLA models for on-robot execution (see "Also noted") and the mixed-precision RBD-accelerator work of APEX-RBD, it gives robotics EdgeAI the two-independent-anchor footing that formalizing a Robotics / autonomous-systems applications concept would require.

**Technical summary:** Using closed-loop outcomes from a small development set, PreDE calibrates two thresholds on offline action deviations and then accepts, rejects or defers new quantization configurations from a fixed observation log. Across five WAMs and four benchmark settings the authors find quantization losses that cannot be explained by bit width alone or by a shared deviation threshold. On 28 held-out configurations from two policies, PreDE issued 21 decisions before any closed-loop test (75% coverage), all matching the observed labels; deferred candidates included both acceptable outcomes and a 33-point loss. In 450 real Franka Research 3 trials across two independently fine-tuned policies, every configuration assigned to a high-deviation group before testing showed significant degradation, while low-deviation comparisons showed none; W4A4 gave a 1.37× action-query speedup and ~44% lower peak memory on the robot.

**Novelty assessment:** Moderate. The idea of predicting task degradation from offline proxies is not new in general, but a policy-specific behavioral calibration with an explicit accept/reject/defer rule, validated on a real robot with statistical reporting, is a useful contribution to the "how do I safely compress a large model for on-robot use" question. The hardware tier (GPU-class onboard compute) is above the microcontroller tier that most of this Knowledge Base centers on.

**Relevance score:** 3/5 — solid quantified result and code, but its main value is as an independent anchor for a possible Robotics applications concept and as an instance of a broader pattern (cheap offline proxies replacing expensive closed-loop evaluation of compressed models).

---

## Also noted this week (not selected, kept for provenance)

- **CircleMatch: Prototype Matching with Circular Temporal Statistics for Tiny Keyword Spotting** — arXiv:2609.20070 (cs.SD), Jiajun Sun, Zhe Gao, 17 Sep 2026. Four [[Keyword_Spotting]] variants of ~1k to ~7k parameters (12-class) using learned class prototypes and parameter-free circular temporal aggregation; competitive accuracy on Speech Commands v1/v2 and the Multilingual Spoken Words Corpus micro subsets; code and weights released. No MCU deployment numbers. https://arxiv.org/abs/2609.20070
- **Recovering Aggressively Pruned Vision-Language-Action Models with Offline Hidden-State Distillation** — arXiv:2609.19579 (cs.RO), Chiyoung Kim, Sanghyuk Roy Choi, Minhyeok Lee, 16 Sep 2026. Width [[Pruning]] of a VLA language backbone by 63% drops LIBERO-Long success from 93.2% to 0.8%; offline hidden-state [[Distillation]] against a cached teacher pass recovers to within 3.5 points in ~8 GPU-hours; on a 6-DoF manipulator the 72%-reduced student runs 2.23× faster on-board with 62% less memory. Second independent robotics-EdgeAI paper this week. https://arxiv.org/abs/2609.19579
- **Lightweight Security-by-Design for TinyML Models in Constrained Embedded Environments** — MDPI Sensors 26(18):5727, Khaznah R. Alshammari, 9 Sep 2026, DOI 10.3390/s26185727. Three-layer pipeline (robustness-aware compressed-model selection, ASCON-signed weights at boot/OTA, runtime drift monitor) validated on real MCU hardware inside 62 KB RAM and <10 ms inference on Edge-IIoTset; reports attack success rate reduced from 60–84% to 38.9%. Model-level (adversarial/extraction) security rather than the physical/hardware angle covered by the existing [[Hardware_Security_of_Edge_AI_Accelerators]] concept; single-author, single paper — noted as a possible future Security-branch signal, no candidate opened. https://www.mdpi.com/1424-8220/26/18/5727
- **Beyond Noise: Understanding and Overcoming Temperature Effects in Analog DNN Inference** — arXiv:2609.15527 (cs.LG), Summ, Wang, Borras, Klein, Fröning (ECML-PKDD 2026 IoT/Edge/Mobile workshop), 14 Sep 2026. Experimental study on a representative analog accelerator finding temperature-induced degradation is driven mainly by systematic non-idealities rather than stochastic noise; hardware-in-the-loop training and temperature-aware calibration retain accuracy best. Adjacent to the "certified / risk-aware selective inference for imperfect edge accelerators" candidate but addresses mitigation via training/calibration, not per-unit certification — not added as evidence. https://arxiv.org/abs/2609.15527
- **Xronos: Heterogeneity-Aware Tensor Parallelism for Collaborative LLM Fine-Tuning on Edge CPUs** — arXiv:2609.19909 (cs.DC), Choi et al., 17 Sep 2026. Shows pipeline parallelism is ineffective on CPU-only edge devices (5.75× higher compute-stall ratio than GPU devices) and proposes heterogeneity-aware tensor partitioning; 18–56% fine-tuning time reduction. Relevant to [[On-device_Learning]] at the gateway/hub tier. https://arxiv.org/abs/2609.19909

---

## Suggested thesis / research hooks

- **Extend the INT8-portability protocol down to the MCU tier:** the KATECH study fixes the ONNX artifact and scales and measures kernel-boundary agreement across CPUs, GPUs and vendor NPUs, but stops above Cortex-M / Ethos-U / RISC-V-NPU hardware. A Master's project could port the same protocol to [[TensorFlow_Lite_Micro]] + [[CMSIS-NN]], microTVM and an Ethos-U vendor path, and ask whether the "1000/1000 agreement only when the integer kernel is shared" invariance holds at that tier. This would directly address the measurement-infrastructure gap listed in the taxonomy's known gaps.
- **Benchmark realism for wearables:** the smart-glasses paper shows firmware co-residency and the camera/JPEG pipeline, not the model, dominate end-to-end latency and shrink the usable budget by more than half. Is there a principled way to extend [[MLPerf_Tiny]]-style reporting with a "system budget" dimension (effective flash/SRAM after firmware, sensor-to-tensor latency) so that results transfer to real consumer devices?
- **Noise-robust KWS at the 1k–10k parameter scale:** SAMSTeG evaluates robustness across four noise types and SNRs at ~16k parameters; CircleMatch reaches ~1k–7k parameters but is evaluated on clean data. A well-scoped thesis could cross these two axes — prototype-matching architectures under the SAMSTeG noise protocol — and deploy both on the same MCU for a fair latency/energy comparison.
- **Edge-first sensor foundation models — verify the "edge" claim:** EdgeHAR's abstract promises edge constraints are met but gives no footprint numbers. Reproducing it on a Cortex-M or Cortex-A target and reporting memory/latency for the adaptation modules would be a useful, citable contribution to the [[Human_Activity_Recognition]] concept and a check on a trend likely to grow.
- **Offline proxies for compressed-model safety beyond robotics:** PreDE's accept/reject/defer rule calibrated on a small closed-loop set is a general pattern. Does the same idea transfer to, e.g., quantized biosignal classifiers or industrial anomaly detectors where "closed-loop" evaluation is a field trial rather than a robot run?
