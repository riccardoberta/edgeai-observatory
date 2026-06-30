# AI Benchmark: All About Deep Learning on Smartphones in 2019

**Full citation:** Ignatov, A., Timofte, R., Kulik, A., Yang, S., Wang, K., Baum, F., Wu, M., Xu, L., Van Gool, L. (2019). AI Benchmark: All About Deep Learning on Smartphones in 2019. arXiv:1910.06663. https://arxiv.org/abs/1910.06663

**Linked concepts:** [[Cortex-A]], [[Vision]], [[NPU]]

## Abstract summary

The authors (ETH Zürich with Google, Samsung, Huawei, Qualcomm, MediaTek and Unisoc collaborators) present a large-scale benchmark and survey of the AI-acceleration capabilities of essentially all major mobile chipsets (Cortex-A application-processor SoCs paired with their integrated mobile NPUs/DSPs) as of 2019, evaluating real deep learning inference workloads and tracking the rapid generational improvement of mobile AI accelerators, alongside an overview of the Android ML deployment pipeline.

## Research problem

Mobile application processors (Cortex-A class SoCs) increasingly ship with heterogeneous AI acceleration (NPU/DSP/GPU blocks alongside the Cortex-A cores), but there was no standardized, vendor-neutral, continuously updated way to measure and compare real deep-learning inference performance across this fragmented landscape of chipsets, frameworks, and deployment APIs.

## Key idea

Build a single, regularly updated benchmark suite (AI Benchmark) covering a broad range of representative deep learning model types and run it consistently across all major commercial mobile SoCs, so that practitioners and researchers have an apples-to-apples view of mobile AI-acceleration performance rather than relying on vendor-reported peak numbers.

## Technical contribution

A standardized, cross-vendor mobile AI inference benchmark and survey methodology, together with an analysis of the heterogeneous compute landscape inside Cortex-A class mobile SoCs (CPU, GPU, NPU/DSP) and of how the Android ML pipeline (NNAPI and vendor delegates) routes inference workloads to these different compute units.

## Experimental methodology

Systematic benchmarking of deep learning inference latency and accuracy across chipsets from Qualcomm, HiSilicon (Huawei), Samsung, MediaTek, and Unisoc, using representative vision-oriented model architectures, run through the standard Android deployment pipeline (NNAPI plus vendor-specific delegates) to reflect realistic application-level performance rather than idealized hardware peak figures.

## Results

The study documents that mobile NPU performance was, at the time, roughly doubling with each SoC generation and approaching the inference throughput of contemporaneous CUDA-class discrete GPUs for some model classes, while also revealing substantial vendor-to-vendor variation in how well the Android ML pipeline actually exposes that raw hardware capability to applications.

## Comparison with the state of the art

Unlike single-vendor or single-device case studies, this is one of the few cross-vendor, standardized comparisons of Cortex-A-class mobile SoCs for AI inference, and it directly complements accelerator-specific studies such as the Edge TPU characterization in our [[NPU]] entry by covering the full breadth of the commercial mobile-SoC market rather than one accelerator family.

## Strengths

Broad, standardized, continuously-maintained benchmark covering nearly the entire commercial mobile-chipset market; grounded in realistic application-level deployment (the actual Android ML pipeline) rather than synthetic peak-performance figures; valuable historical record of how quickly mobile AI acceleration capability evolved.

## Weaknesses

As a benchmark/survey paper rather than a novel architecture or algorithm contribution, it does not propose new techniques; results are tied to a specific point in time (2019) and to the Android ecosystem specifically, so they require updating to remain representative of current hardware generations.

## Limitations

Cortex-A SoCs and their AI accelerators are commercial, often partially closed products, so the benchmark cannot fully attribute observed performance differences to specific microarchitectural causes (unlike the more controlled internal characterization possible for a single accelerator family, as in our [[NPU]] entry); focuses on vision-oriented workloads typical of smartphone use cases, so coverage of other modalities (audio, biosignals) relevant to our Applications taxonomy is limited.

## Open questions

How has the gap between mobile NPU and discrete GPU inference performance evolved since 2019, and how does it compare with the more controlled characterization approach used for Edge TPU in our [[NPU]] entry? How well do current cross-platform inference runtimes (e.g. ONNX Runtime, TFLite) exploit Cortex-A-class heterogeneous compute compared to the vendor-specific delegates surveyed here?

## Possible extensions

A modern re-run of this benchmark methodology on current-generation Cortex-A mobile/edge SoCs, including non-vision workloads (keyword spotting, HAR, biosignals) relevant to the rest of our taxonomy, to assess whether the same generational-improvement trend continues.

## Relevance to our research

Foundational reference for the [[Cortex-A]] branch of our Hardware taxonomy, providing the application-processor-class counterpart to the microcontroller-class [[Cortex-M]] entry, and a bridge to the broader question of how cross-platform frameworks ([[ONNX_Runtime]], [[microTVM_TVM]]) perform on real heterogeneous mobile hardware.

## Possible thesis topics

A current-generation replication of this benchmark scoped to non-vision EdgeAI tasks in our taxonomy (keyword spotting, HAR, biosignals) on modern Cortex-A mobile SoCs; comparative study of ONNX Runtime versus native vendor delegates on the same Cortex-A hardware.

## Possible collaborations

Mobile SoC vendors monitored as hardware vendors in `00_Config/sources.yaml` (Qualcomm, MediaTek); ETH Zürich computer vision lab (original authors).

## Links to related papers

[[2021_Yazdanbakhsh_EdgeTPUEvaluation]] (analogous large-scale accelerator characterization, narrower in hardware scope but deeper in microarchitectural detail), [[2021_David_TensorFlowLiteMicro]], [[2019_Microsoft_ONNXRuntime]] (cross-platform deployment frameworks relevant to the same Cortex-A hardware tier)
