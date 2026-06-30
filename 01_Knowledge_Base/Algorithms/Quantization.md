# Quantization

## Evolution of the concept

The idea arises from the need to run inference on hardware without efficient floating-point units. The foundational work by Jacob et al. (2017) defines the 8-bit affine quantization scheme and quantization-aware training, which later became the standard adopted by TensorFlow Lite and CMSIS-NN. Even before that, Hubara et al. (NeurIPS 2016) had already shown that networks could be trained with weights and activations constrained to a single bit, proving the extreme end of the precision spectrum was reachable. From here the line of research branched toward more aggressive precisions (4-bit, binary/ternary) and toward layer-by-layer mixed precision. With the rise of large language models, the 2023-2024 wave of quantization research shifted toward post-training, calibration-light methods for compressing LLMs to INT4/INT3 for edge/on-device deployment: AWQ (Lin et al., MLSys 2024 Best Paper) protects a small set of activation-salient weight channels from quantization error, avoiding the backpropagation-based calibration required by earlier methods, and ships with a paired inference engine (TinyChat) that realizes measured speedups on edge GPUs.

## Key papers

[[2017_Jacob_QuantizationIntegerOnlyInference]] — 8-bit affine scheme and QAT, the basis of the entire subsequent mobile/embedded inference stack.

[[2016_Han_DeepCompression]] — trained quantization as the second stage of a compression pipeline, demonstrating complementarity with pruning and entropy coding.

[[2016_Hubara_BinarizedNeuralNetworks]] — trains both weights and activations constrained to +1/-1, establishing binary precision as the extreme end of the quantization spectrum and a direct precursor to the ternary/sub-8-bit schemes named as an open problem below.

[[2024_Lin_AWQ]] — activation-aware salient-channel protection for post-training LLM quantization, with a paired edge-GPU inference engine; representative of the 2023-2024 shift toward quantizing large language models for edge deployment rather than only CNNs.

[[2017_Umuroglu_FINN]] — pairs aggressive (binary) quantization with a per-layer FPGA dataflow architecture, showing quantization gains realized only when matched with a hardware design that fully exploits the reduced precision.

[[2021_Banbury_MLPerfTiny]] — standardized TinyML benchmark suite and measurement methodology, used across the field (including quantization work) to compare optimization techniques on a level playing field.

[[2022_Zhang_DeepLearningHARWearableSensors]] — survey connecting quantization and other compression choices to deployment constraints for wearable HAR models.

[[2022_Lin_OnDeviceTraining256KB]] — quantization-aware scaling for numerically stable 8-bit on-device training without normalization layers, extending quantization from inference to the training loop itself.

[[2023_Zhan_FPGABinaryNN]] — systematic comparison of FPGA-based binary neural network accelerators, the hardware-side counterpart to algorithmic binary/ternary quantization research.

[[2024_Deutel_OnDeviceTrainingQuantizedCortexM]] — keeps the full training loop (not just inference) in a fully quantized integer representation on real Cortex-M hardware.

[[2025_Abushahla_QuantizationMicrocontrollersSurvey]] — survey explicitly connecting quantization methods to the runtime libraries and hardware platforms that execute them, rather than treating quantization as a purely algorithmic topic.

[[2026_Jain_TinyFed6G]] — assigns differently-quantized model variants to federated-learning devices according to each device's real-time resource profile.

## Open problems

Extension to sub-8-bit precision while keeping implementation simplicity and hardware support. Automating the choice of which layers to quantize aggressively. Data-free quantization, useful when the original training set of the model is not available.

## Research ideas

Automatic mixed precision guided by NAS; quantization jointly with distillation for models to be deployed on Cortex-M; evaluation of how well quantization gains transfer to RISC-V microcontrollers without dedicated SIMD support.

## Possible thesis topics

Comparative study between QAT and more recent post-training quantization techniques on models for microcontrollers; binary/ternary quantization for Cortex-M targeting CMSIS-NN.

## Links

[[Pruning]], [[Compression]], [[CMSIS-NN]], [[TensorFlow Lite Micro]]
