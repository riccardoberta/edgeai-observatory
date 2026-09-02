# FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution

**Full citation:** Yang, S., Fan, X., Pan, M., Xi, H., Wang, Z., Sun, S., Keutzer, K., Han, S., Zaharia, M., Xu, C., Stoica, I. (2026). FreeToken: Efficient Edge-Native MoE Serving with Bandwidth-Adaptive Execution. arXiv:2608.16157 [cs.DC]. Submitted 17 Aug 2026. System released at flashml.ai. DOI: 10.48550/arXiv.2608.16157.

**Linked concepts:** [[Mixture-of-Experts (MoE) & Edge LLM Serving]] — the sharpest single data point for that concept's central "how edge is edge" open problem (2026-09-02 Knowledge Base Consolidation cycle). Also touches [[Compression]] (FreeToken serves already-quantized MXFP4/NVFP4 experts but performs no compression itself) and [[NPU]]/edge-inference generally.

## Abstract summary

Frontier open-weight MoE models are increasingly available, but serving them still largely assumes datacenter infrastructure. FreeToken is an edge-native MoE serving system that treats a personal machine as a unified, elastic inference platform rather than a small GPU. It co-designs model layout/loading, expert residency, CPU–GPU execution, agentic state reuse, and runtime memory management around two realities of local AI: agent workloads continuously change their execution pattern, and edge hardware exposes heterogeneous resources that differ machine to machine. Rather than a fixed offloading strategy, FreeToken continuously remaps computation and model state onto whatever resources are actually available. It supports 20+ MoE models and real coding/tool-using agents on hardware from an 8GB laptop GPU to a single workstation GPU, scaling from a 35B model on a laptop to a 284B model on a gaming desktop and the 753B GLM-5.2 on a single workstation GPU. Released at flashml.ai.

## Research problem

Serving frontier-scale open-weight MoE models has assumed datacenter infrastructure, but personal machines (laptops, gaming desktops, single workstations) have far less GPU memory and much lower CPU–GPU bandwidth. Existing local-LLM serving engines (llama.cpp, Ollama, KTransformers, MoE-Infinity) rely on offline-tuned, fixed offloading strategies — e.g., placement decided once at prefill time — that break down under real agentic workloads, where tool use and multi-turn interaction continuously shift which experts get routed to. The paper's own measurement shows this concretely: a placement frozen at prefill time captures only a small fraction of routed traffic under agentic use, leaving both GPU and PCIe idle while the CPU absorbs most of the (mismatched) load.

## Key idea

Treat a personal machine's heterogeneous resources — GPU VRAM, CPU DRAM, PCIe bandwidth — as a unified, elastic pool, and continuously remap computation and model state onto whatever is actually available at each step rather than committing to a fixed offloading plan. This is realized through three co-designed mechanisms: (1) prefill codesign — pipelined, double-buffered full-layer expert loading plus semantic-aware state caching, making prefill transfer-bound rather than compute-stalled; (2) decode codesign — a semantic-aware expert cache governed by a "q★" policy that partitions GPU cache capacity between hot (GPU-resident) and cold (CPU-computed) experts based on measured, not assumed, bandwidth; (3) elastic memory management that treats GPU cache capacity as a runtime-adjustable resource rather than a static allocation.

## Technical contribution

An end-to-end, open-released (flashml.ai) MoE serving system supporting 20+ MoE models and real agentic tool-using workloads — not just single-turn synthetic benchmarks; a bandwidth-adaptive execution policy (q★) that is measured per-machine rather than hand-tuned; a demonstrated scaling range from a 35B model on an 8GB laptop GPU to a 284B model (DeepSeek-V4-Flash, native MXFP4 experts) on a gaming desktop and a 753B model (GLM-5.2, NVFP4, 433GB checkpoint) on a single 96GB workstation GPU.

## Experimental methodology

Six discrete-GPU systems: RTX 5090, 4090, and 3090 rented dual-socket servers, each capped to 6 CPU threads and NUMA-pinned to emulate edge-class host bandwidth (56.7–77.3 GB/s, matching what the two real edge machines reach at full threads); a real RTX 5090 desktop (Ryzen 9 9950X3D, 53.8 GB/s); a real RTX 4060 8GB laptop (Core i9-13900H, 47.5 GB/s); and an RTX PRO 6000 96GB workstation (178 GB/s) for the frontier-scale demonstration. All bandwidths were measured on deployed tensor shapes rather than taken from spec sheets. Two primary models: DeepSeek-V4-Flash (284B params, 13B active, native MXFP4 routed experts) and Qwen3.6-35B-A3B (BF16; NVFP4 on the 8GB laptop for precision parity with its official release). GLM-5.2 (753B/40B active, NVFP4) was added for the workstation-tier demonstration. Four agentic workloads: W1 math reasoning (AIME, single-turn, decode-dominated, no tool use); W2 coding agent (SWE-bench issue via the OpenCode harness, real tool execution, 3 scripted turns); W3 coding agent via Claude Code's native protocol (concurrent subagents, 56–65k-token sessions); W4 email/calendar agent via OpenClaw (13 fixed turns, ~24.5k-token system-context floor, idle watchdog disabled to keep slow engines measurable). Baselines: llama.cpp, Ollama, KTransformers, and MoE-Infinity, with weight formats bit-exactly matched across engines. Metrics: per-request mean decode throughput (tok/s) and mean time-to-first-token (TTFT); cross-engine wall-clock agent-trajectory totals were explicitly not compared, since trajectories diverge across engines.

## Results

On the RTX 5090, FreeToken sustains 77–83 tok/s decode on Qwen3.6-35B-A3B and 22–25 tok/s on DeepSeek-V4-Flash — 1.8–2.3× and 1.5–1.9× the strongest baseline in each workload, respectively. Its decode rate stays within 12% of its own single-turn (W1) value across the three agentic workloads, whereas the most context-sensitive baseline, KTransformers on DSV4-Flash, has already lost 31% of its W1 rate by W2 — evidence that single-stream benchmarks overstate baseline agentic performance. MoE-Infinity serves only W1 (8.8 tok/s): its per-expert prefill staging cap aborts longer-prompt workloads, and it retains no KV cache across requests. On TTFT, FreeToken posts the lowest mean in 5 of 6 multi-turn cells (KTransformers' GPU-prefill arm wins Qwen3.6×W3; llama.cpp wins W1's short isolated prompts). The tail matters more than the mean: FreeToken's worst turn stays below 44s in every cell, while every baseline crosses 150s somewhere (llama.cpp 232s, Ollama 179s, KTransformers 946s) — past the timeouts real agent harnesses actually enforce (OpenClaw's 120s idle watchdog, Claude Code's ~10-minute default), making tail TTFT an availability boundary rather than just a latency statistic. Ablations: pipelined full-layer double-buffering raises prefill throughput to 6.7k tok/s at 16k-token prompts; disabling the second buffer serializes transfer against computation and costs 19% of throughput at 4k tokens.

## Comparison with the state of the art

Benchmarked directly and head-to-head, with weight formats bit-exactly matched, against the four dominant local-LLM serving engines (llama.cpp, Ollama, KTransformers, MoE-Infinity) rather than only against internal ablations — a stronger evidentiary bar than most local-LLM serving papers set for themselves. The related-work discussion (per the paper's structure) positions FreeToken against static or frequency-based expert-caching approaches and against WiSP, a system that partitions VRAM between expert weights and KV cache by marginal latency value; FreeToken's point of departure is treating the whole placement/caching problem as dynamically, continuously adaptive rather than statically tuned.

## Strengths

Real agentic workloads (SWE-bench issues via two different harnesses, a multi-turn email/calendar agent) rather than only synthetic single-turn decode benchmarks, with the paper's own data showing why that distinction matters (KTransformers' 31% W1→W2 rate drop); tail-latency reporting, not just means, surfaces an availability boundary that mean-only reporting would hide entirely; bandwidth measured on deployed tensor shapes rather than taken from platform specifications, improving the reproducibility of the hardware characterization; a genuinely heterogeneous hardware sweep that includes a real 8GB laptop, not only high-end GPUs; open release (flashml.ai) and an unusually strong systems/ML-systems author pedigree (Han, Stoica, Zaharia, Keutzer) that improves both credibility and likely third-party adoption/reproducibility.

## Weaknesses

All six test systems are discrete-GPU machines, down to an 8GB laptop GPU — there is no true MCU/NPU-class or even integrated-GPU-only edge target, so despite the "edge-native" framing the weight class remains well above the Cortex-M/RISC-V tier this Observatory's lab work typically targets. Three of the six systems ("rented servers") are explicitly capped/NUMA-pinned to *emulate* edge-class bandwidth rather than being organically edge machines; only the desktop and laptop are described as real edge hardware used to "validate the emulation," so five of six data points rely partly on an emulation methodology. Cross-engine wall-clock agent-trajectory totals are explicitly not compared — only decode tok/s and TTFT are — leaving open whether FreeToken's per-token gains translate proportionally into faster real task completion end-to-end.

## Limitations

FreeToken depends on the routed-expert weights already being available in a GPU-friendly compressed format (MXFP4/NVFP4) for its largest-scale demonstrations — it is a serving/scheduling system built on top of existing model-level quantization work, not a source of compression itself, so its largest-model results are contingent on upstream quantization quality it does not control. All four agentic workloads tested (AIME math, two coding-agent harnesses, an email/calendar agent) are text/tool-use tasks; there is no coverage of vision-language or multimodal MoE agents.

## Open questions

Does the bandwidth-adaptive q★ policy degrade gracefully as hardware scales further down toward genuinely embedded (NPU-stick, single-board-computer) targets, or does its core assumption — a capable discrete GPU plus CPU DRAM over PCIe — break down below some hardware floor? This is precisely the boundary question the 2026-08-23 weekly digest flags as a research hook ("where does edge-native LLM serving stop being edge?"). How does the tail-latency advantage change under concurrent multi-agent or multi-user serving on the same machine, rather than the single-session workloads tested here?

## Possible extensions

Port the pipelined-loading and semantic-aware caching principles to a lower-tier hardware target (e.g., a Jetson-class or NPU-equipped single-board computer) to test the "where does edge-native stop being edge" boundary directly; extend the four-workload agentic benchmark suite with a vision-language agentic task to test whether the bandwidth-adaptive execution model generalizes beyond text MoE; measure end-to-end agent-trajectory wall-clock time (not just per-token metrics) to confirm the per-token gains translate into faster real task completion.

## Relevance to our research

FreeToken is the sharpest evidence yet of a tension recurring across the Observatory's August 2026 digests: MICRO/ICCAD-caliber systems groups are applying genuinely novel bandwidth-adaptive scheduling ideas to hardware (laptop/workstation GPUs) that sits well above this lab's core MCU/NPU/[[RISC-V]] focus. It is the clearest single data point for the still-open "Edge LLM Serving / Local Inference Systems" taxonomy gap flagged in the 2026-08-13, 2026-08-20, and 2026-08-23 digests, alongside APEX, EdgeXpert, UnionSparse, PolyQ, and HeteroMosaic — see the taxonomy Evolution note added 2026-08-25, which recommends Ricky decide whether to formalize this taxonomy node now that six independent papers have converged on it.

## Possible thesis topics

"Where does edge-native MoE serving stop being edge?" — a Master's/PhD scoping study (per the 2026-08-23 digest's hook) porting FreeToken's bandwidth-adaptive execution model to genuinely embedded hardware and characterizing where its core assumptions break down. A study of FreeToken's q★ cache-partitioning policy under concurrent multi-tenant serving on shared edge hardware — directly relevant to any lab deployment scenario with more than one simultaneous user or agent (Master's).

## Possible collaborations

No obvious direct-collaboration fit given the scale of the author team (Berkeley/MIT/Anyscale-adjacent systems groups — Stoica, Zaharia, Han, Keutzer) relative to a single academic lab, but the released system (flashml.ai) is directly usable as an experimental platform for the thesis topics above without requiring formal collaboration.

## Links to related papers

Conceptually part of the same emerging "edge LLM/MoE serving" cluster as PolyQ (arXiv:2607.14618), HeteroMosaic (arXiv:2607.12839), APEX (arXiv:2608.11688), EdgeXpert (arXiv:2608.05303), and UnionSparse (arXiv:2608.09291) — all flagged across the 2026-07-19 through 2026-08-13 weekly digests as part of the same trend. None of these five has a `02_Papers/` deep-analysis record yet either (see the cross-cycle backlog noted in the taxonomy Evolution note added 2026-08-25).
