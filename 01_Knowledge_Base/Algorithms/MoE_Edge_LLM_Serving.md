# Mixture-of-Experts (MoE) & Edge LLM Serving

This concept covers *serving* — not training or compressing — large language models (dense or Mixture-of-Experts) under the memory, bandwidth, and power constraints of edge and near-edge hardware. A Mixture-of-Experts (MoE) model is a network built from many "expert" sub-networks, of which only a small number are activated for any given input via a learned gating/routing mechanism — keeping the compute cost low despite a very large total parameter count. Serving such a model at the edge raises problems distinct from training or compressing it: which experts to keep in fast memory, how to schedule work across a device's CPU, GPU, and NPU, and how to hide the latency of loading experts that were not predicted in advance.

## Evolution of the concept

The architectural idea underlying essentially every production MoE model traces back to Shazeer et al.'s "Outrageously Large Neural Networks" (ICLR 2017), which introduced the gating-network-plus-top-k-sparse-routing design still in use today. EdgeMoE (Yi et al., IEEE Transactions on Mobile Computing 2025, originally 2023) is one of the first systems explicitly designed for on-device MoE serving — combining expert-specific bitwidth adaptation with predictive expert preloading to make MoE-based LLM inference viable on mobile devices — rather than adapted from infrastructure built for dense models.

A comprehensive cross-layer measurement study of mobile LLM inference (Cai et al.) found that NPUs excel at compute-bound "prefilling" (processing the input prompt) while CPUs win at memory-bound "decoding" (generating output tokens one at a time), because NPUs prefer large, fixed-shape workloads that clash with decoding's small, dynamic computation. This finding motivates much of the work that followed: a heterogeneous CPU/integrated-GPU/NPU scheduler gated by a roofline model (a way of predicting whether a computation is limited by raw compute speed or by memory bandwidth) responds directly to it (Jun et al., "HeteroMosaic"), while a separate line of work (Oh et al., "PolyQ") tackles the same deployment regime from the compiler side, making fine-grained per-channel mixed-precision quantization efficiently executable on CPUs specifically — the most universal on-device inference substrate — by pushing layout regularization to compile time.

A cluster of work targets the specific problem of paging MoE experts in and out of scarce memory fast enough: learned, confidence-driven expert prefetching before the attention block (Kanani et al., "APEX"); a hardware-software co-designed accelerator, synthesized in Samsung 28nm silicon, that resolves a previously unrecognized incompatibility between speculative decoding and MoE routing (Ha et al., "EdgeXpert"); and work naming the "Payload-to-Metadata Ratio" as a first-order design concern once quantization shrinks a sparse model's actual payload faster than its sparse-format metadata (Jiang et al., "UnionSparse"). All three target the same underlying problem — how to page expert weights in and out of scarce memory fast enough — from different angles (prediction, hardware co-design, storage format), and each proposes that combining all three would work better than any one alone, though none has actually built and benchmarked that combination yet.

A genuinely edge-native MoE serving system (Yang et al., "FreeToken", authored by a Berkeley/MIT/Anyscale-adjacent group including Song Han, Ion Stoica, Matei Zaharia, and Kurt Keutzer) continuously remaps computation across a personal machine's heterogeneous GPU/CPU/PCIe resources, rather than using a fixed offloading plan. Its demonstrated hardware range — an 8GB laptop GPU up to a 96GB workstation GPU — sits well above the Cortex-M/RISC-V/NPU tier this Observatory's core taxonomy centers on, sharpening a tension named in Field Notes above: none of this cluster's papers has yet proposed a quantitative criterion for where "edge-native" LLM serving stops and genuine TinyML begins.

Further recent additions reinforce that this cluster's center of gravity is *serving infrastructure* — memory management, scheduling, communication-efficient fine-tuning — rather than new model architectures or compression algorithms: OS-level memory management for on-device LLM serving under real multitasking, measured on real Android hardware ("mzCache"); split federated LLM fine-tuning that exploits weight tying so clients can upload activations once and then go offline, extending [[Federated_Learning]] into the LLM fine-tuning regime under intermittent connectivity ("Just Talk Once"); and a hardware-accelerator co-design for block-diffusion LLMs modeled on Jetson-class platforms.

## Key papers

[[2017_Shazeer_SparselyGatedMoE]] — the gating-network-plus-top-k-sparse-routing MoE layer design underlying essentially every production MoE model this cluster's serving systems deploy; the foundational architectural anchor.

[[2025_Yi_EdgeMoE]] — bitwidth-adaptive expert storage plus predictive expert preloading for on-device MoE-LLM inference on mobile devices; one of the first systems explicitly designed for this problem.

[[2026_Cai_NPUReadyForLLMs]] — first comprehensive cross-layer measurement study of mobile LLM inference; the diagnostic foundation the rest of this cluster responds to.

[[2026_Jun_HeteroMosaic]] — heterogeneous CPU/integrated-GPU/NPU scheduling gated by a roofline model, with trace-guided co-optimization modeling real hardware effects (dynamic voltage/frequency scaling, resource contention, NPU wake latency).

[[2026_Oh_PolyQ]] — compile-time channel permutation/clustering making fine-grained mixed-precision quantization efficiently executable on CPUs specifically.

[[2026_Kanani_APEX]] — learned, confidence-driven expert prefetching operating before the attention block, with a correctness-preserving mode and a stall-free execution mode.

[[2026_Ha_EdgeXpert]] — hardware-software co-designed accelerator resolving the MoE/speculative-decoding incompatibility via prompt-wise expert reuse (prefill) and depth-aware expert coalescing (decode); synthesized in Samsung 28nm silicon.

[[2026_Jiang_UnionSparse]] — names the Payload-to-Metadata Ratio as a first-order design concern for combined sparse-plus-quantized inference; an index-efficient bitmap encoding and a small-batch-optimized sparse-matrix-multiply kernel; open code.

[[2026_Yang_FreeToken]] — edge-native MoE serving system continuously remapping computation across a personal machine's heterogeneous GPU/CPU/PCIe resources; the sharpest evidence yet for the "how edge is edge" open problem below; open release.

[[2026_Taherin_Hydra]] — phase-aware (prefill/decode) LLM inference characterization across three Jetson AGX hardware generations, 13 models, and 5 execution formats; finds that quantization does not predict power draw monotonically, and that backend structure changes where latency is actually introduced — measurement infrastructure this cluster's scheduling and co-design work could adopt for evaluation.

## Open problems

**Where does "edge-native" stop being edge?** HeteroMosaic and PolyQ target workstation/laptop/mobile CPUs and AMD Ryzen AI SoCs; the APEX/EdgeXpert/UnionSparse memory-management trio targets similarly capable hardware; FreeToken spans an 8GB laptop GPU to a 96GB workstation GPU. All apply genuinely novel systems ideas to hardware well above the MCU/RISC-V/NPU tier that defines "TinyML" elsewhere in this taxonomy. No paper in the cluster has yet proposed a *quantitative* criterion — a memory budget, power envelope, or cost tier — for where "edge-native" MoE/LLM serving stops and genuine TinyML begins. Anchoring such a definition to MLPerf Tiny's device classes versus MLPerf Inference's edge category is one plausible starting point, but no tracked paper has attempted it. This question is recorded here rather than as its own concept, since every paper that raises it is itself a member of this cluster; it should become its own concept only if a paper actually proposes and validates a quantitative boundary, rather than continuing to just name the tension.

**Do the memory-management mechanisms compose?** APEX (prefetching), EdgeXpert (hardware-software co-designed coalesced loading), and UnionSparse (index-efficient low-bit sparse storage) each address the MoE expert-loading bottleneck independently; none has been benchmarked against or combined with the other two, despite all three papers naming this as the natural next step.

**Does this cluster's serving infrastructure reach true microcontroller-class hardware at all?** Every paper in the cluster that reports a hardware floor — FreeToken's 8GB laptop GPU, PolyQ's mobile CPU, APEX/UnionSparse's unspecified "edge GPU" — stops well above Cortex-M/RISC-V. Whether MoE inference, which fundamentally requires holding or fast-paging a large total parameter count even though only a small subset activates per token, is feasible at all under true microcontroller memory budgets is an open, largely unaddressed question — a matter of hard feasibility, distinct from the terminology question above.

**How does this relate to the separate standardized-measurement-infrastructure gap?** [[2026_Taherin_Hydra]] (an open, phase-aware Jetson AGX measurement framework) and a reverse-engineered Apple Neural Engine architecture/performance study extend the same "diagnose before you build" progression [[2026_Cai_NPUReadyForLLMs]] began, but target measurement/characterization infrastructure rather than serving systems, and neither has a microcontroller/NPU-tier analogue yet (see Known Gaps in taxonomy.md). This is tracked as a separate, related gap rather than folded into this concept, since it is about benchmarking methodology rather than serving mechanisms — worth linking more explicitly if a future paper bridges the two.

## Research ideas

Building the combined memory-management design point APEX, EdgeXpert, and UnionSparse each independently propose but none has built: prefetching feeding a coalesced-loading accelerator, storing weights in an index-efficient sparse format. Quantifying the "edge-native" boundary with a validated criterion (memory budget, power envelope, or cost tier) anchored to MLPerf Tiny vs. MLPerf Inference device classes, rather than continuing to only name the tension qualitatively. Testing whether any of this cluster's mechanisms (bandwidth-adaptive execution, roofline-gated co-scheduling, prefetching) degrade gracefully — or break down entirely — when ported to genuinely embedded (Jetson-class, NPU-stick, or Cortex-M/RISC-V-class) hardware, rather than the laptop/workstation/mobile-SoC tier every cluster paper has tested so far.

## Possible thesis topics

Unifying edge-MoE memory management: implement and benchmark the combined design point stacking APEX-style prefetching, EdgeXpert-style hardware-software co-designed coalesced loading, and UnionSparse's low-bit sparse storage format, and characterize where the three mechanisms' assumptions conflict (PhD-scale; bridges [[Compression]], [[Quantization]], and this concept).

Quantifying the edge-native boundary: propose and empirically validate a quantitative criterion separating "edge-native" MoE/LLM serving from genuine TinyML deployment, using MLPerf Tiny's and MLPerf Inference's own device-class definitions as a starting anchor (Master's-scale position/measurement study).

Porting edge-native MoE serving toward true microcontroller-class hardware: take FreeToken's bandwidth-adaptive execution model, or a comparable mechanism from this cluster, and characterize where its core assumptions break down as hardware scales down toward genuinely embedded targets (Master's/PhD; bridges [[Cortex-M]], [[RISC-V]], and [[NPU]]).

Backend-aware scheduling for on-device LLM inference in open frameworks: reproduce the prefill-on-NPU/decode-on-CPU phase split [[2026_Cai_NPUReadyForLLMs]] identified, and quantify how much of HeteroMosaic's or PolyQ's reported efficiency gains are recoverable in an open runtime such as microTVM or ONNX Runtime, rather than the papers' own proprietary implementations (Master's).

## Links

[[Quantization]], [[Compression]], [[Federated_Learning]], [[NPU]], [[RISC-V]], [[Cortex-M]], [[Hardware_Security_of_Edge_AI_Accelerators]] (YAVIN, a member of that concept, evaluates its security overhead on the same quantized edge-class LLM execution regime this cluster serves), [[Generative_EdgeAI]] (the application-level counterpart — this concept is about serving/scheduling infrastructure, that one about end-user generative/multimodal systems built on top of it)
