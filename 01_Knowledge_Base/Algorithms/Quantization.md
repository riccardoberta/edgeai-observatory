# Quantization

## Evolution of the concept

The idea arises from the need to run inference on hardware without efficient floating-point units. The foundational work by Jacob et al. (2017) defines the 8-bit affine quantization scheme and quantization-aware training, which later became the standard adopted by TensorFlow Lite and CMSIS-NN. Even before that, Hubara et al. (NeurIPS 2016) had already shown that networks could be trained with weights and activations constrained to a single bit, proving the extreme end of the precision spectrum was reachable. From here the line of research branched toward more aggressive precisions (4-bit, binary/ternary) and toward layer-by-layer mixed precision.

## Key papers

[[2017_Jacob_QuantizationIntegerOnlyInference]] — 8-bit affine scheme and QAT, the basis of the entire subsequent mobile/embedded inference stack.

[[2016_Han_DeepCompression]] — trained quantization as the second stage of a compression pipeline, demonstrating complementarity with pruning and entropy coding.

[[2016_Hubara_BinarizedNeuralNetworks]] — trains both weights and activations constrained to +1/-1, establishing binary precision as the extreme end of the quantization spectrum and a direct precursor to the ternary/sub-8-bit schemes named as an open problem below.

## Open problems

Extension to sub-8-bit precision while keeping implementation simplicity and hardware support. Automating the choice of which layers to quantize aggressively. Data-free quantization, useful when the original training set of the model is not available.

## Research ideas

Automatic mixed precision guided by NAS; quantization jointly with distillation for models to be deployed on Cortex-M; evaluation of how well quantization gains transfer to RISC-V microcontrollers without dedicated SIMD support.

## Possible thesis topics

Comparative study between QAT and more recent post-training quantization techniques on models for microcontrollers; binary/ternary quantization for Cortex-M targeting CMSIS-NN.

## Links

[[Pruning]], [[Compression]], [[CMSIS-NN]], [[TensorFlow Lite Micro]]
