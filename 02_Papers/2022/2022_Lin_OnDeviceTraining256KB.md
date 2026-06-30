# On-Device Training Under 256KB Memory

**Full citation:** Lin, J., Zhu, L., Chen, W.-M., Wang, W.-C., Gan, C., Han, S. (2022). On-Device Training Under 256KB Memory. *Advances in Neural Information Processing Systems (NeurIPS) 35*. arXiv:2206.15472. https://arxiv.org/abs/2206.15472

**Linked concepts:** [[On-device_Learning]], [[Quantization]], [[Cortex-M]]

## Abstract summary

The authors present an algorithm-system co-design framework that makes on-device training of neural networks possible within 256 KB of memory — about three orders of magnitude less than typical cloud training setups — enabling pre-trained models to be fine-tuned directly on microcontrollers using locally collected sensor data, without sending data to the cloud.

## Research problem

On-device training (fine-tuning a deployed model with new local data) would let edge devices personalize and adapt without compromising privacy or needing connectivity, but the memory required for full back-propagation (storing activations, gradients, and an optimizer state) vastly exceeds the SRAM available on microcontroller-class hardware (often under 256 KB), and quantized inference graphs are hard to train because of low bit-precision and missing normalization layers.

## Key idea

Combine two techniques: Quantization-Aware Scaling, which calibrates gradient scales so that 8-bit quantized training remains numerically stable without the normalization layers usually relied on; and Sparse Update, which automatically selects which layers and sub-tensors actually need a gradient computed, skipping backward computation (and the associated memory) for the rest under a given memory budget.

## Technical contribution

A "Tiny Training Engine" that translates the sparse, quantization-aware training graph into an efficient, compile-time-optimized execution graph for MCU-class hardware, fusing operators and pruning the autodiff graph ahead of time so that the runtime memory footprint matches the theoretical savings of the sparse-update scheme.

## Experimental methodology

Evaluated on visual recognition transfer-learning tasks with backbones used in TinyML (e.g. MCUNet, MobileNetV2, ProxylessNAS), measuring peak training memory, training accuracy versus full back-propagation, and end-to-end measured memory/latency on real microcontroller hardware (e.g. STM32 boards), comparing against existing training frameworks (e.g. PyTorch, TensorFlow Lite) ported to MCUs.

## Results

The framework reduces training memory by over 1000x compared to standard full back-propagation (dense PyTorch-style training) while keeping accuracy close to full fine-tuning, and is the first system demonstrated to perform on-device training within a 256 KB memory budget on real microcontroller hardware rather than only in simulation.

## Comparison with the state of the art

Prior on-device "training" work was largely limited to fine-tuning only the last layer (similar to other TinyML personalization approaches), which has limited adaptation capacity; this paper enables sparse but deeper updates across the network within the same memory budget, with measured results on physical MCUs rather than purely simulated figures.

## Strengths

Genuine algorithm-system co-design (not just an algorithmic trick), with a real compiler/runtime contribution; demonstrated on physical hardware, not simulation; from a well-resourced and well-cited lab (Song Han's group at MIT), with public code.

## Weaknesses

Evaluated mainly on vision transfer-learning benchmarks; unclear how well Sparse Update generalizes to other modalities (audio, time series, biosignals) where layer importance patterns may differ. The Quantization-Aware Scaling and Sparse Update hyperparameters likely require per-model/per-task tuning.

## Limitations

Targets fine-tuning a pre-trained model on new data, not training from scratch; still assumes a capable pre-trained backbone exists and fits in flash; does not address streaming/continual personalization where data arrives incrementally over a long device lifetime (the focus of [[Continual_Learning]] and [[On-device_Learning]] more broadly).

## Open questions

How does Sparse Update interact with continual/incremental learning settings where the “important” layers may shift over time? Can the same co-design approach be extended to federated settings (combining with frameworks like TinyFed6G) where on-device training feeds into aggregation rather than only local personalization?

## Possible extensions

Combining Sparse Update with [[Federated_Learning]] frameworks for MCU clients (reducing both communication and local training memory simultaneously); extending the approach to non-vision modalities such as audio (keyword spotting) or biosignals.

## Relevance to our research

Foundational reference for the [[On-device_Learning]] concept: it is the clearest existing demonstration that training (not just inference) is feasible within MCU-class memory budgets, directly relevant to thesis work on personalized or adaptive EdgeAI systems.

## Possible thesis topics

Extending sparse on-device training to streaming/continual settings (catastrophic-forgetting-aware sparse updates); applying the Tiny Training Engine's co-design philosophy to a non-vision EdgeAI task (HAR, biosignals, keyword spotting) and measuring memory/accuracy trade-offs on real hardware.

## Possible collaborations

MIT-HAN-LAB (Song Han's group); groups working on compiler/runtime co-design for embedded ML (e.g. TVM/microTVM community, given overlap in graph-compilation philosophy).

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]] (quantization fundamentals underlying Quantization-Aware Scaling), [[2021_David_TensorFlowLiteMicro]] (comparable embedded runtime, inference-only), [[2018_Chen_TVM]] (compiler co-design philosophy)
