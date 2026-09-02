# Profiling Concurrent Vision Inference Workloads on NVIDIA Jetson -- Extended

**Full citation:** Chakraborty, A., Tavernier, W., Kourtis, A., Pickavet, M., Oikonomakis, A., Colle, D. (2025). Profiling Concurrent Vision Inference Workloads on NVIDIA Jetson -- Extended. arXiv:2508.08430 [cs.PF]. Ghent University; imec. Submitted 11 Aug 2025. DOI: 10.48550/arXiv.2508.08430.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2508.08430)

**Linked concepts:** [[Vision]] — no clean match in the Hardware branch (Cortex-M/A, RISC-V, DSP, FPGA, NPU); this targets edge-GPU-class hardware (NVIDIA Jetson), flagged as a taxonomy gap (see taxonomy Evolution notes).

## Abstract summary

Low-power GPU-based AI accelerators are increasingly deployed for real-time inference at the network edge, but remain underutilised even under computationally intensive workloads — a consequence of limited understanding of GPU resource sharing in edge scenarios. The paper profiles both high- and low-level metrics (GPU utilisation, memory usage, streaming-multiprocessor utilisation, tensor-core usage) on NVIDIA Jetson edge devices under concurrent vision-inference workloads, integrating traces from multiple profiling tools. Findings: GPU utilisation can reach 100% under specific optimisations, but critical low-level resources (SMs, tensor cores) often operate at only 15-30% utilisation, and CPU-side events (thread scheduling, context switching) frequently emerge as bottlenecks constraining overall GPU performance.

## Research problem

IoT growth and edge-network advances are pushing more real-time inference workloads onto low-power edge GPUs, but these devices remain poorly utilised in practice even when running computationally demanding workloads. The underlying cause was not well understood: is it a hardware limitation, a scheduling problem, or a software-stack inefficiency? Without a detailed, multi-level profiling methodology, edge-GPU deployment decisions and optimisations were being made without visibility into where the actual bottlenecks lie.

## Key idea

Combine high-level GPU metrics (overall utilisation, memory usage) with low-level microarchitectural metrics (streaming-multiprocessor utilisation, tensor-core usage) and CPU-side system metrics (thread scheduling, context switching), integrating traces from multiple independent profiling tools into one unified view, rather than relying on any single tool's or metric's necessarily partial picture of concurrent vision-inference performance on Jetson hardware.

## Technical contribution

A multi-tool, multi-level profiling methodology combining high-level and low-level GPU metrics with CPU-side system events for concurrent vision-inference workloads on NVIDIA Jetson; the empirical finding that high-level GPU utilisation figures (which can show 100%) are a misleading proxy for actual compute-resource usage, since low-level SM and tensor-core utilisation can remain at 15-30% simultaneously; identification of CPU-side thread scheduling and context switching as frequent, previously under-recognised bottlenecks constraining GPU performance in edge deployments.

## Experimental methodology

Empirical profiling study on real NVIDIA Jetson edge hardware (specific model(s) not confirmed at abstract level — verify from full PDF) under concurrent vision-inference workloads. Integrated traces from multiple profiling tools to jointly capture GPU utilisation, memory usage, SM utilisation, tensor-core usage, and CPU-side scheduling events.

## Results

GPU utilisation can reach 100% under specific optimisations, yet SM and tensor-core utilisation — the actual compute resources doing useful work — often remain at only 15-30% simultaneously, revealing that headline utilisation metrics substantially overstate genuine hardware efficiency. CPU-side events (thread scheduling, context switching) frequently emerge as bottlenecks that constrain overall GPU performance, implicating the software/OS scheduling stack rather than the GPU hardware itself as a limiting factor in several observed cases.

## Comparison with the state of the art

Distinguishes itself from single-metric or vendor-reported Jetson benchmarking work (e.g. NVIDIA's own published Jetson benchmarks, or narrower single-tool profiling studies) by combining multiple independent profiling tools and both GPU- and CPU-side metrics into one integrated analysis, surfacing the GPU-utilisation-vs-SM-utilisation discrepancy that single-metric studies would miss entirely.

## Strengths

Directly actionable finding (headline GPU utilisation is a misleading efficiency proxy) that changes how edge-GPU deployments should be profiled and optimised going forward; the multi-tool, multi-level methodology is itself reusable by other researchers profiling edge-GPU workloads; identifying CPU-side scheduling as a bottleneck points optimisation effort toward the OS/software stack, a genuinely underexplored lever versus the more commonly studied model- or kernel-level optimisations this Observatory's [[Quantization]] and [[Compression]] concepts already track heavily.

## Weaknesses

Restricted to vision-inference workloads and NVIDIA Jetson hardware specifically — generality to other workload types (e.g. LLM inference, per [[2026_Taherin_Hydra]]) or other edge-GPU vendors is untested; specific Jetson model(s), software stack versions, and the particular "optimisations" that reach 100% GPU utilisation are not confirmed at abstract level.

## Limitations

As an empirical profiling study on specific hardware and workloads, findings may be sensitive to the particular Jetson generation, JetPack/driver software-stack version, and vision-model architectures used; the CPU-side scheduling bottleneck finding may be partly an artifact of the specific OS/scheduler configuration tested rather than a universal property of edge-GPU deployments.

## Open questions

Does the GPU-utilisation-vs-SM-utilisation discrepancy and the CPU-scheduling-bottleneck finding generalise to other edge-GPU workload types (LLM inference, as characterized on Jetson by [[2026_Taherin_Hydra]]) and to other Jetson generations? What specific OS/scheduler-level interventions would resolve the identified CPU-side bottlenecks?

## Possible extensions

Extending the multi-tool, multi-level profiling methodology to LLM inference workloads on Jetson, directly complementing [[2026_Taherin_Hydra]]'s phase-aware LLM characterization with this paper's GPU-microarchitecture-level view; investigating concrete OS-scheduler interventions to resolve the identified CPU-side bottlenecks.

## Relevance to our research

The Observatory's first recorded paper characterizing edge-GPU-class hardware (NVIDIA Jetson) at the microarchitecture level — a Hardware taxonomy gap this coverage-assessment pass identified, since the current Hardware branch (Cortex-M, Cortex-A, RISC-V, DSP, FPGA, NPU) has no node for GPU-class edge accelerators despite NVIDIA being an actively monitored hardware vendor in `00_Config/sources.yaml`. Kept as a recorded paper and a new "watching" consolidation candidate rather than a formalized taxonomy node until a second, independent Jetson/edge-GPU characterization paper is recorded.

## Possible thesis topics

Extending this paper's multi-tool profiling methodology to LLM inference workloads on Jetson, producing a GPU-microarchitecture-level companion to [[2026_Taherin_Hydra]]'s phase-aware characterization (Master's/PhD). Investigating and evaluating concrete OS-scheduler-level fixes for the CPU-side bottlenecks this paper identifies (Master's).

## Possible collaborations

The Ghent University / imec author team (Chakraborty, Tavernier, Kourtis, Pickavet, Oikonomakis, Colle) for edge-GPU profiling methodology.

## Links to related papers

[[2026_Taherin_Hydra]] (LLM-inference characterization on the same Jetson AGX hardware family, a natural workload-type complement to this paper's vision-inference focus).
