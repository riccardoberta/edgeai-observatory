# Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference

**Full citation:** Chen, L., Feng, D., Feng, E., Wang, Y., Zhao, R., Xia, Y., Xu, P., Chen, H. (2025). Characterizing Mobile SoC for Accelerating Heterogeneous LLM Inference. Proceedings of the ACM SIGOPS 31st Symposium on Operating Systems Principles (SOSP '25). arXiv:2501.14794. https://arxiv.org/abs/2501.14794

**Linked concepts:** [[Cortex-A]], [[NPU]]

## Abstract summary

The authors characterize the heterogeneous compute and memory-bandwidth properties of modern mobile SoCs (Cortex-A CPU clusters paired with GPU and NPU blocks) for on-device LLM inference, and introduce HeteroInfer, an inference engine that jointly exploits GPU and NPU compute and bandwidth, reporting 1.34x-6.02x end-to-end speedups over GPU-only or NPU-only engines.

## Research problem

On-device LLM inference on mobile SoCs is typically restricted to a single accelerator (GPU or NPU) at a time, leaving the other heterogeneous compute resource and a meaningful share of total memory bandwidth unused, despite both mattering for the distinct prefill and decode phases of LLM inference.

## Key idea

Profile how GPU and NPU compute throughput and shared SoC memory bandwidth behave under realistic LLM inference workloads, then design heterogeneous parallel execution mechanisms that split work across both accelerators according to each phase's bottleneck (compute-bound prefill vs. bandwidth-bound decode).

## Technical contribution

A systematic characterization of mobile SoC heterogeneous-compute and bandwidth behavior specific to LLM inference; HeteroInfer, an inference engine implementing phase-aware GPU/NPU work-splitting mechanisms derived from that characterization.

## Experimental methodology

Benchmarking on real mobile SoCs across representative LLM workloads, comparing HeteroInfer's end-to-end latency and throughput against state-of-the-art GPU-only and NPU-only mobile LLM inference engines.

## Results

HeteroInfer delivers 1.34x to 6.02x end-to-end speedup over the best single-accelerator baselines, demonstrating that jointly exploiting GPU and NPU resources captures substantial performance otherwise left on the table by single-accelerator deployment.

## Comparison with the state of the art

Extends the AI Benchmark-era understanding of Cortex-A SoC heterogeneity (CPU/GPU/NPU) to the LLM inference setting, where the prefill/decode phase split creates a more structured opportunity for heterogeneous parallelism than earlier CNN-era mobile inference work exploited.

## Strengths

Grounds the heterogeneous-parallelism design in a concrete hardware characterization rather than a generic scheduling heuristic; reports substantial, hardware-measured speedups rather than only simulated estimates.

## Weaknesses

Benchmarked on specific mobile SoC generations; the magnitude of gains may not transfer directly to NPUs with very different memory-sharing architectures (e.g. NPUs with fully private SRAM vs. shared DRAM bandwidth).

## Limitations

Focused specifically on LLM inference (prefill/decode structure); the phase-aware splitting strategy may need rework for other EdgeAI workloads (vision, audio) with different compute/bandwidth balance.

## Open questions

How much of HeteroInfer's heterogeneous-parallelism benefit is recoverable through general-purpose cross-platform runtimes like [[ONNX_Runtime]] rather than a workload-specific engine? Does the same phase-aware splitting approach generalize to non-LLM EdgeAI models with comparably distinct compute phases?

## Possible extensions

Applying the same compute/bandwidth characterization methodology to non-LLM EdgeAI workloads (vision, keyword spotting) on the same class of mobile SoC; extending the approach to three-way CPU/GPU/NPU splitting rather than GPU/NPU only.

## Relevance to our research

Provides an up-to-date, empirically grounded successor to the AI Benchmark-era view of Cortex-A heterogeneous compute, directly relevant to the open question (already flagged in our [[Cortex-A]] entry) of how much heterogeneous compute general-purpose runtimes actually exploit.

## Possible thesis topics

Adapting HeteroInfer-style GPU/NPU work-splitting to a non-LLM EdgeAI task; measuring how close ONNX Runtime / TensorFlow Lite mobile delegates come to HeteroInfer's hand-tuned heterogeneous splitting on the same hardware.

## Possible collaborations

Groups working on mobile SoC vendor delegates and cross-platform inference runtimes ([[ONNX_Runtime]]) that could adopt phase-aware heterogeneous scheduling as a general feature.

## Links to related papers

[[2019_Ignatov_AIBenchmarkSmartphones]], [[2011_Greenhalgh_bigLITTLE]]
