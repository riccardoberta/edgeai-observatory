# Edge Intelligence: A Review of Deep Neural Network Inference in Resource-Limited Environments

**Full citation:** Kang, B. (2025). Edge Intelligence: A Review of Deep Neural Network Inference in Resource-Limited Environments. Electronics, 14(12), 2495. DOI: 10.3390/electronics14122495

**PDF:** [MDPI (open access)](https://www.mdpi.com/2079-9292/14/12/2495)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[Quantization]], [[Compression]]

## Abstract summary

A comprehensive 2025 review of recent advances in accelerating DNN inference on edge platforms (smartwatches, IoT nodes, intelligent sensors), covering model compression, compiler optimizations, and hardware-software co-design, with post-training quantization (PTQ) — calibration-based quantization without retraining — discussed as a central technique. Categorizes existing frameworks by architectural target and adaptation mechanism and analyzes latency/energy/accuracy trade-offs across techniques, discussing open challenges in runtime adaptability and hardware-aware scheduling.

## Research problem

The DNN edge-inference optimization literature has grown rapidly and fragmented across model-compression, compiler, and hardware-co-design approaches, each evaluated under different assumptions and hardware targets, making it difficult to compare techniques or identify practical deployment strategies for a given resource-limited environment.

## Key idea

Synthesize the fragmented edge-inference-optimization literature into a unified categorization by architectural target and adaptation mechanism, with explicit attention to post-training quantization as a retraining-free path to deployment and to the latency/energy/accuracy trade-offs each technique family makes, rather than treating compression, compiler optimization, and hardware co-design as separate literatures.

## Technical contribution

A structured review and categorization of DNN edge-inference-acceleration techniques (model compression including quantization, compiler optimizations, hardware-software co-design), explicitly analyzing trade-offs across latency, energy, and accuracy and identifying runtime adaptability and hardware-aware scheduling as open challenges.

## Experimental methodology

Literature review and synthesis (not a novel empirical study); categorizes existing frameworks and techniques and analyzes their reported latency/energy/accuracy trade-offs across resource-limited deployment scenarios (smartwatches, IoT nodes, intelligent sensors).

## Results

Provides a structured, up-to-date (2025) map of the DNN edge-inference-optimization landscape, with post-training quantization highlighted as a practical, calibration-based, retraining-free deployment path, and identifies runtime adaptability and hardware-aware scheduling as the field's key remaining open challenges.

## Comparison with the state of the art

Complements this Observatory's existing quantization-focused key papers (e.g. [[2017_Jacob_QuantizationIntegerOnlyInference]], [[2024_Lin_AWQ]]) and the CMSIS-NN/MCU-focused survey [[2025_Abushahla_QuantizationMicrocontrollersSurvey]] with a broader 2025 synthesis spanning quantization, compiler optimization, and hardware co-design together rather than any one technique family in isolation.

## Strengths

Recent (2025), fully open-access, broad synthesis useful as an up-to-date entry point into the fragmented edge-inference-optimization literature; explicitly connects PTQ to compiler and hardware-co-design considerations rather than treating quantization in isolation.

## Weaknesses

As a review rather than a novel empirical study, it does not itself validate specific latency/energy/accuracy numbers on new hardware; breadth across compression/compiler/hardware topics necessarily trades off against depth on any single technique.

## Limitations

Review-based synthesis is only as current as its cited literature and may not capture the very latest (post-mid-2025) developments; does not report new benchmark results of its own.

## Open questions

The review explicitly names runtime adaptability and hardware-aware scheduling as open challenges — how would a runtime-adaptive quantization/scheduling scheme need to be designed to work within Cortex-M-class memory budgets specifically, rather than the smartwatch/IoT-node-class hardware more broadly discussed?

## Possible extensions

Following up the review's runtime-adaptability and hardware-aware-scheduling open challenges with a concrete implementation and evaluation on Cortex-M-class hardware, connecting to this Observatory's existing quantization/CMSIS-NN literature.

## Relevance to our research

A recent, broad, fully open-access synthesis for [[Quantization]] and [[Compression]] connecting quantization to compiler and hardware-co-design considerations — useful as an up-to-date survey anchor alongside this Observatory's more technique-specific quantization key papers.

## Possible thesis topics

Implementing a runtime-adaptive, hardware-aware quantization/scheduling scheme for Cortex-M-class hardware, directly following up the open challenge this review identifies but does not itself address.

## Possible collaborations

Groups working on edge-inference-optimization surveys and hardware-aware scheduling research.

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]], [[2025_Abushahla_QuantizationMicrocontrollersSurvey]]
