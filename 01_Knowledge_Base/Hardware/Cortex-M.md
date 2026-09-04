# Cortex-M

Arm Cortex-M cores are the most widely used hardware target for TinyML: low-power microcontrollers with no dedicated hardware for neural computation and only a few tens or hundreds of kilobytes of RAM.

## Evolution of the concept

The entire software ecosystem for this target developed in response to its constraints: [[CMSIS-NN]] for optimized kernels, [[TensorFlow_Lite_Micro]] as a runtime with static memory allocation. MCUNet (Lin, Chen, Lin, Gan, and Han, 2020) jointly co-designs a Neural Architecture Search method (TinyNAS, which first fits the search space to the resource budget before searching within it) with a code-generation inference engine (TinyEngine), together demonstrating ImageNet-scale classification directly on microcontroller-class hardware — a capability previously assumed out of reach, and the direct architectural ancestor of this concept's own on-device-training work below (from the same MIT research lineage).

Deutel et al. (2024) push the Cortex-M envelope beyond inference-only deployment, showing that fully quantized *training* — not just inference — is feasible directly on Cortex-M0+/M4/M7 hardware via a dynamic partial-gradient-update scheme, extending what these cores can do in place without offloading to a server (see also [[On-device_Learning]]).

## Key papers

[[2020_Lin_MCUNet]] — joint architecture-search-plus-inference-engine co-design (TinyNAS + TinyEngine) enabling ImageNet-scale classification on genuine microcontroller-class hardware; foundational to this concept's own on-device-training lineage.

[[2018_Lai_CMSIS-NN]] — kernels optimized for Cortex-M's SIMD (single-instruction-multiple-data) instructions.

[[2021_David_TensorFlowLiteMicro]] — an inference runtime designed for the memory constraints of these cores.

[[2021_Marsh_HeliumMVEReferenceBook]] — official technical reference for the Helium vector-instruction extension on Cortex-M55/M85, the hardware capability named as an open problem below since CMSIS-NN/TFLM coverage of it remains limited.

[[2024_Deutel_OnDeviceTrainingQuantizedCortexM]] — fully quantized on-device training with dynamic partial gradient updates, demonstrated across Cortex-M0+, M4, and M7.

[[2022_Lin_OnDeviceTraining256KB]] — quantization-aware scaling plus sparse gradient updates to make on-device training fit within 256 KB of memory, directly relevant to Cortex-M's tight SRAM budget.

[[2026_Jain_TinyFed6G]] — federated learning across a tier of Cortex-M/RISC-V TinyML devices, with per-device quantized model variants assigned according to each device's resource profile.

[[2026_Garavagno_HWNASUltraLowPower]] — hardware-aware NAS measured on real STM32 L0/L1/L4 hardware (20–40 KiB RAM class), reporting measured inference latency on each target.

[[2026_Sen_NVFP4QuantizationEdgeAI]] — quantization scheme whose ~7x activation-memory reduction is directly relevant to Cortex-M's tight SRAM budget, though evaluated algorithmically rather than on real Cortex-M hardware.

## Open problems

Exploiting the new Helium (MVE) vector instructions on Cortex-M55/M85, still poorly covered in the literature. Efficient support for architectures other than classic CNNs — for example lightweight attention.

## Research ideas

A study of the real efficiency of depthwise-separable convolutions (as in MobileNet) on Cortex-M with CMSIS-NN. An evaluation of how well quantization gains transfer to these cores compared to RISC-V without dedicated SIMD support.

## Possible thesis topics

Benchmarking new architectures (NAS-derived, distilled) on real Cortex-M hardware, comparing CMSIS-NN and microTVM as backends.

## Links

[[CMSIS-NN]], [[TensorFlow_Lite_Micro]], [[microTVM_TVM]]
