# Quantization

Quantization represents a model's weights and activations with fewer bits — for example 8-bit integers instead of 32-bit floating-point numbers — to shrink a model's memory footprint and speed up inference, particularly on hardware without efficient floating-point units. *Post-training quantization* converts an already-trained model without further training; *quantization-aware training* (QAT) simulates the effect of reduced precision during training itself, usually yielding better accuracy at very low precisions.

## Evolution of the concept

The idea arises from the need to run inference on hardware without efficient floating-point units. Jacob et al. (2017) define the 8-bit affine quantization scheme (a linear mapping between the real-valued range a tensor takes and a fixed integer range) together with quantization-aware training; this became the standard later adopted by TensorFlow Lite and CMSIS-NN. Even earlier, Hubara et al. (NeurIPS 2016) had already shown that networks could be trained with weights and activations constrained to a single bit, proving that the extreme end of the precision spectrum was reachable at all. From here the line of research branched toward more aggressive precisions (4-bit, binary/ternary) and toward mixed precision, where different layers of the same network use different bit-widths.

With the rise of large language models, the 2023–2024 wave of quantization research shifted toward post-training, calibration-light methods for compressing LLMs to 4-bit or 3-bit precision for edge and on-device deployment. AWQ (Lin et al., MLSys 2024) protects a small set of activation-salient weight channels — the channels a model is most sensitive to — from quantization error, avoiding the expensive backpropagation-based calibration required by earlier methods, and ships with a paired inference engine (TinyChat) that realizes measured speedups on edge GPUs.

A 2025 review (Kang) takes stock of this now-fragmented landscape, situating post-training quantization alongside compiler optimizations and hardware-software co-design as three interlocking — not independent — levers for edge-inference acceleration, and names runtime adaptability and hardware-aware scheduling, rather than further static compression, as the field's next open challenge.

Two further surveys ground quantization in the hardware that actually executes it, rather than treating it as a purely algorithmic technique: Deng et al. (Proceedings of the IEEE, 2020) treat quantization jointly with hardware acceleration, directly bearing on the open problem below about hardware support for sub-8-bit precision; and Abushahla et al. (2025) explicitly connect quantization methods to the runtime libraries and hardware platforms that execute them. Husom et al. (2025) provide the largest empirical dataset of its kind — energy, latency, and accuracy measured jointly across 28 quantized LLMs on a real Raspberry Pi 4 — grounding recent quantization-tradeoff claims in one consistent real-hardware measurement, rather than comparisons pieced together across papers with different setups.

## Key papers

[[2017_Jacob_QuantizationIntegerOnlyInference]] — the 8-bit affine scheme and quantization-aware training, the basis of the entire subsequent mobile/embedded inference stack.

[[2016_Han_DeepCompression]] — trained quantization as the second stage of a compression pipeline, demonstrating complementarity with pruning and entropy coding.

[[2016_Hubara_BinarizedNeuralNetworks]] — trains both weights and activations constrained to +1/−1, establishing binary precision as the extreme end of the quantization spectrum and a direct precursor to the ternary/sub-8-bit schemes named as an open problem below.

[[2024_Lin_AWQ]] — activation-aware salient-channel protection for post-training LLM quantization, with a paired edge-GPU inference engine; representative of the 2023–2024 shift toward quantizing large language models for edge deployment rather than only CNNs.

[[2017_Umuroglu_FINN]] — pairs aggressive (binary) quantization with a per-layer FPGA dataflow architecture, showing quantization gains are realized only when matched with a hardware design that fully exploits the reduced precision.

[[2021_Banbury_MLPerfTiny]] — standardized TinyML benchmark suite and measurement methodology, used across the field (including quantization work) to compare optimization techniques on a level playing field.

[[2022_Zhang_DeepLearningHARWearableSensors]] — survey connecting quantization and other compression choices to deployment constraints for wearable Human Activity Recognition models.

[[2022_Lin_OnDeviceTraining256KB]] — quantization-aware scaling for numerically stable 8-bit on-device training without normalization layers, extending quantization from inference to the training loop itself.

[[2023_Zhan_FPGABinaryNN]] — systematic comparison of FPGA-based binary neural network accelerators, the hardware-side counterpart to algorithmic binary/ternary quantization research.

[[2024_Deutel_OnDeviceTrainingQuantizedCortexM]] — keeps the full training loop, not just inference, in a fully quantized integer representation on real Cortex-M hardware.

[[2025_Abushahla_QuantizationMicrocontrollersSurvey]] — survey explicitly connecting quantization methods to the runtime libraries and hardware platforms that execute them, rather than treating quantization as a purely algorithmic topic.

[[2026_Jain_TinyFed6G]] — assigns differently-quantized model variants to federated-learning devices according to each device's real-time resource profile.

[[2026_Sen_NVFP4QuantizationEdgeAI]] — characterizes NVFP4 (hierarchical FP4/FP8/FP32 block-and-tensor scaling) for edge deployment, with a closed-form bits-per-input model and a no-retrain vs. retrain comparison against conventional FP4.

[[2025_Kang_EdgeIntelligenceReview]] — 2025 review synthesizing the fragmented edge-inference-optimization literature (model compression including post-training quantization, compiler optimizations, hardware-software co-design) into one categorization by architectural target and adaptation mechanism.

[[2020_Deng_ModelCompressionHardwareAccelerationSurvey]] — treats quantization jointly with hardware acceleration rather than as a purely algorithmic topic.

[[2025_Husom_SustainableLLMInferenceEdgeAI]] — large-scale (28 models) empirical characterization of energy, latency, and accuracy jointly across quantization levels on a real Raspberry Pi 4.

## Open problems

Extension to sub-8-bit precision while keeping implementation simplicity and hardware support. Automating the choice of which layers to quantize aggressively. Data-free quantization, useful when the original training set of a model is not available.

## Research ideas

Automatic mixed precision guided by NAS. Quantization jointly with distillation for models to be deployed on Cortex-M. Evaluation of how well quantization gains transfer to RISC-V microcontrollers without dedicated SIMD (single-instruction-multiple-data) support.

## Possible thesis topics

A comparative study between quantization-aware training and more recent post-training quantization techniques on models for microcontrollers. Binary/ternary quantization for Cortex-M targeting CMSIS-NN.

## Links

[[Pruning]], [[Compression]], [[CMSIS-NN]], [[TensorFlow_Lite_Micro]]
