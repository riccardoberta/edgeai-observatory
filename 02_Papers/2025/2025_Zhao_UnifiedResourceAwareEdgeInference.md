# A Unified and Resource-Aware Framework for Adaptive Inference Acceleration on Edge and Embedded Platforms

**Full citation:** Zhao, J. (2025). A Unified and Resource-Aware Framework for Adaptive Inference Acceleration on Edge and Embedded Platforms. Electronics, 14(11), 2188. DOI: 10.3390/electronics14112188

**PDF:** [MDPI (open access)](https://www.mdpi.com/2079-9292/14/11/2188)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page. Implemented using PyTorch and ONNX Runtime — included here as an ONNX-Runtime-based deployment example rather than a paper about ONNX Runtime's own architecture.

**Linked concepts:** [[Quantization]]

## Abstract summary

Proposes a unified inference-optimization framework for large-scale generative models (language and image generation) on edge/embedded platforms, integrating three complementary techniques: sensitivity-aware mixed-precision quantization, heterogeneous sparse attention to reduce attention complexity, and capacity-aware dynamic expert routing for input-adaptive computation. Implemented with PyTorch 1.13 and ONNX Runtime, the framework dynamically adjusts computation paths based on token complexity and hardware conditions, demonstrated on platforms including Jetson Orin.

## Research problem

Deploying large-scale generative models on diverse edge/embedded hardware requires simultaneously managing precision (quantization), attention computational cost, and expert/capacity allocation, but existing approaches typically optimize these dimensions independently rather than jointly and adaptively as a function of both input complexity and real-time hardware conditions.

## Key idea

Integrate mixed-precision quantization, sparse attention, and dynamic expert routing into one unified framework whose computation paths adapt at runtime based on token complexity and hardware state, rather than applying each optimization statically and independently, using ONNX Runtime as the deployment substrate that executes the resulting adaptive computation graph.

## Technical contribution

A unified framework combining sensitivity-aware mixed-precision quantization, heterogeneous sparse attention, and capacity-aware dynamic expert routing for input- and hardware-adaptive inference of generative models on edge platforms, implemented and deployed via ONNX Runtime.

## Experimental methodology

Implementation using PyTorch 1.13 and ONNX Runtime, evaluated on language and image generation tasks across edge/embedded platforms including Jetson Orin, measuring inference latency, memory usage, and throughput against existing baselines under constrained GPU environments, plus robustness tests under resource fluctuation and input noise.

## Results

Significant reductions in inference latency and memory usage alongside substantial throughput improvements for language and image generation tasks, outperforming existing baselines even under constrained GPU environments; qualitative analyses show fine-grained adaptivity, and robustness tests confirm stable behavior under resource fluctuation and input noise.

## Comparison with the state of the art

Distinguishes itself from single-technique edge-inference optimization (quantization alone, or sparse attention alone) by jointly and adaptively combining three complementary mechanisms, and is directly relevant to this Observatory's [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]] cluster's central theme of scheduling/routing generative-model computation across heterogeneous edge resources — though this paper is implemented via ONNX Runtime rather than the custom runtimes most MoE-serving-cluster papers use.

## Strengths

Jointly optimizes three complementary dimensions (precision, attention cost, expert routing) rather than one in isolation; validated on genuine edge-class hardware (Jetson Orin); fully open-access; concretely demonstrates ONNX Runtime as a viable deployment substrate for adaptive generative-model inference, relevant to this Observatory's [[ONNX_Runtime]] concept's open question about ONNX Runtime's mobile/edge execution-provider performance relative to alternatives.

## Weaknesses

Targets large-scale generative models (language/image generation) rather than the smaller CNN/RNN workloads more typical of this Observatory's core TinyML taxonomy; Jetson Orin is a comparatively capable edge-GPU platform, not representative of the Cortex-M/RISC-V tier.

## Limitations

Does not address microcontroller-class deployment; the three-technique integration adds system complexity that may not be justified for smaller, non-generative EdgeAI workloads where a single optimization technique may suffice.

## Open questions

Does this framework's adaptive, input-complexity-aware routing generalize to non-generative EdgeAI workloads (classification, detection) where the notion of "token complexity" does not directly apply? How does ONNX Runtime's execution-provider architecture handle the framework's dynamic, input-dependent computation-path switching compared to a custom runtime built specifically for this purpose?

## Possible extensions

Adapting the sensitivity-aware mixed-precision-quantization and hardware-adaptive routing ideas from this generative-model framework to non-generative EdgeAI classification/detection tasks on lower-capability hardware tiers.

## Relevance to our research

Provides this Observatory's [[ONNX_Runtime]] concept with a concrete, recent (2025) example of ONNX Runtime used as the deployment substrate for adaptive, resource-aware inference of generative models on edge-GPU-class hardware, and connects to the [[MoE_Edge_LLM_Serving|Mixture-of-Experts (MoE) & Edge LLM Serving]] cluster's dynamic-expert-routing theme via an open-runtime (rather than proprietary) implementation path.

## Possible thesis topics

Backend-aware evaluation of this framework's dynamic routing/quantization strategy when re-implemented on ONNX Runtime versus a custom C++ runtime, quantifying how much of its reported efficiency gain survives the switch to a general-purpose, open deployment stack.

## Possible collaborations

Groups working on adaptive inference optimization for generative models on edge hardware and ONNX Runtime execution-provider development.

## Links to related papers

[[2023_Ahn_QuantizationDNNInferenceEdgeDevices]]
