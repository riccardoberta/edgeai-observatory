# ExecuTorch -- A Unified PyTorch Solution to Run AI Models On-Device

**Full citation:** Nachin, M., Desai, D., Jia, S.S., Lai, C., Liu, M., Szwejbka, J., Alvarez, R., et al. (2026). ExecuTorch -- A Unified PyTorch Solution to Run AI Models On-Device. arXiv:2605.08195 [cs.LG]. Meta AI. Submitted 5 May 2026. DOI: 10.48550/arXiv.2605.08195.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2605.08195)

**Linked concepts:** [[ExecuTorch]], [[Quantization]]

## Abstract summary

Deploying PyTorch-trained models on edge hardware traditionally requires model conversion or complete reimplementation outside the PyTorch ecosystem. ExecuTorch is a unified, PyTorch-native deployment framework for edge AI that preserves PyTorch semantics while scaling from embedded microcontrollers to complex SoCs with dedicated accelerators, supporting quantization and pluggable execution backends. It powers billions of daily inferences across Meta's family of apps and Reality Labs devices, and the paper benchmarks it against llama.cpp, ONNX Runtime, LiteRT, and Core ML on modern consumer devices.

## Research problem

TinyML/edge-AI deployment has historically been fragmented: a model trained in PyTorch typically has to be converted to a separate format (ONNX, TFLite, a vendor-specific IR) or reimplemented in a different framework entirely to run on edge hardware, breaking the research-to-production pipeline and making it hard to validate deployment behavior directly from the training framework. This fragmentation is worse across heterogeneous target hardware, since microcontrollers, mobile SoCs with NPUs, and larger embedded compute clusters each traditionally need separate toolchains.

## Key idea

Keep the entire model-authoring-to-deployment pipeline inside PyTorch itself: represent the exported model in a PyTorch-native intermediate form, apply optimizations (including quantization) using PyTorch-native tooling, and dispatch execution to any of several pluggable hardware "backends" — from microcontroller-class targets up to SoCs with dedicated accelerators — without leaving the PyTorch ecosystem or requiring model conversion into a separate framework's format.

## Technical contribution

A PyTorch-native edge deployment framework spanning the full hardware range from embedded microcontrollers to SoC-class accelerators within one unified pipeline; a pluggable execution-backend architecture supporting 12 hardware backends; native support for quantization and other PyTorch-native optimizations applied before deployment rather than after conversion; a large-scale cross-framework benchmark against llama.cpp, ONNX Runtime, LiteRT (TensorFlow Lite's successor), and Core ML on modern consumer devices (Samsung Galaxy S25 Ultra, Google Pixel 9 Pro XL, Apple iPhone 15 Pro); and production validation at Meta's scale — billions of daily inferences across Meta's apps and Reality Labs devices.

## Experimental methodology

Benchmarked against llama.cpp, ONNX Runtime, LiteRT, and Core ML on three modern flagship consumer devices (Samsung Galaxy S25 Ultra, Google Pixel 9 Pro XL, Apple iPhone 15 Pro). Specific models, metrics, and benchmark protocol details not confirmed at abstract level — verify from full PDF. Production deployment scale (billions of daily inferences) is reported as an operational fact rather than a controlled experiment.

## Results

Not confirmed at abstract level beyond the qualitative claim of competitive or favorable performance against llama.cpp, ONNX Runtime, LiteRT, and Core ML on the tested devices; specific latency/throughput/accuracy numbers require full-PDF verification before citing in a survey.

## Comparison with the state of the art

Directly positioned against the Observatory's other tracked cross-hardware deployment frameworks — [[ONNX_Runtime]] (also framework-agnostic but not PyTorch-native, requiring export to the ONNX format) and [[TensorFlow_Lite_Micro]] (MCU-focused, TensorFlow-native) — with ExecuTorch's distinguishing claim being that it requires no model conversion at all when the model was authored in PyTorch, spanning a wider hardware range (MCU to SoC/cluster) than TFLite Micro's MCU focus within a single framework.

## Strengths

Backed by a large, named engineering team at Meta and validated at genuine production scale (billions of daily inferences), giving it credibility beyond a research prototype; addresses a real, widely-felt pain point (framework fragmentation between training and edge deployment) rather than a narrow technical niche; the cross-framework benchmark against four major competing deployment stacks on real flagship hardware gives a concrete, checkable point of comparison, unlike [[ONNX_Runtime]]'s own record, which notes the absence of any canonical benchmark paper for ONNX Runtime itself.

## Weaknesses

As an industry systems paper (not a peer-reviewed academic venue submission per the abstract-level material), the benchmark comparisons may reflect Meta's own tuning effort on ExecuTorch relative to less-optimized configurations of competing frameworks — an inherent risk in vendor-authored cross-framework benchmarks generally; quantitative results not yet verified from the full text in this pass.

## Limitations

As with any single-vendor framework paper, evaluation is necessarily from the authoring organization's own perspective; true microcontroller-tier (Cortex-M-class) performance, as opposed to the smartphone-tier devices benchmarked in the paper, is not directly demonstrated in the abstract-level material despite the framework's claimed MCU-to-SoC scaling range.

## Open questions

How does ExecuTorch's actual measured performance compare to [[CMSIS-NN]] or [[TensorFlow_Lite_Micro]] specifically at the Cortex-M microcontroller tier, rather than the smartphone-class devices benchmarked in the paper? How mature and complete is ExecuTorch's operator coverage for newer model architectures (small transformers, MoE) relative to [[ONNX_Runtime]] and [[microTVM_TVM]]?

## Possible extensions

A controlled benchmark of the same model deployed via ExecuTorch, TensorFlow Lite Micro, and CMSIS-NN specifically at the Cortex-M tier, extending the paper's own smartphone-tier comparison down to genuinely constrained microcontroller hardware — directly analogous to the controlled-benchmark research idea already proposed in this Observatory's [[ONNX_Runtime]] concept.

## Relevance to our research

Adds a major, production-validated PyTorch-native framework to the Observatory's Frameworks taxonomy branch, alongside [[TensorFlow_Lite_Micro]], [[CMSIS-NN]], [[microTVM_TVM]], [[MLIR]], and [[ONNX_Runtime]] — closing a real coverage gap identified in this pass, since ExecuTorch (and PyTorch on-device deployment generally) had no representation despite PyTorch being the dominant model-training framework in current ML research.

## Possible thesis topics

A controlled, Cortex-M-tier benchmark comparing ExecuTorch against [[TensorFlow_Lite_Micro]] and [[CMSIS-NN]] on the same model and hardware (Master's; extends the comparative-benchmark thesis idea already proposed for [[ONNX_Runtime]] to a third framework). Evaluating ExecuTorch's operator coverage and export fidelity for transformer/MoE architectures relevant to this Observatory's [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]] concept.

## Possible collaborations

Meta AI's ExecuTorch engineering team, and the open-source ExecuTorch project (github.com/pytorch/executorch) directly, given its scale and active development.

## Links to related papers

[[2019_Microsoft_ONNXRuntime]] (the Observatory's other framework-agnostic cross-hardware deployment runtime, a natural comparison point); [[2021_David_TensorFlowLiteMicro]] (the Observatory's existing MCU-tier deployment framework, against which ExecuTorch's MCU-scaling claim should eventually be benchmarked).
