# Taxonomy

Living document. Any paper can belong to multiple categories. Sub-entries are added as new directions emerge, not by redesigning the structure every time.

## Algorithms

- Quantization (post-training, quantization-aware training, mixed precision, binary/ternary networks)
- Pruning (structured, unstructured, dynamic)
- Distillation (knowledge distillation, self-distillation)
- NAS (hardware-aware NAS, once-for-all networks)
- Compression (low-rank factorization, weight sharing)
- Continual Learning
- On-device Learning
- Federated Learning

## Frameworks

- TensorFlow Lite Micro
- CMSIS-NN
- microTVM / TVM
- MLIR
- ONNX Runtime

## Hardware

- Cortex-M
- Cortex-A
- RISC-V
- DSP
- FPGA
- NPU

## Applications

- Keyword Spotting
- Vision
- Human Activity Recognition
- Biosignals
- Industrial IoT
- Predictive Maintenance

## Evolution notes

(here we will note over time when a sub-category splits, merges with another, or becomes saturated)

**2026-06-30 — Quantization/Compression: shift from CNN-era to LLM-era methods.** Since 2023-2024, new work in both [[Quantization]] and [[Compression]] has shifted from compressing CNNs (the AlexNet/VGG/MobileNet era) toward post-training, calibration-light compression of large language models for edge/on-device deployment — see [[2024_Lin_AWQ]], [[2024_Ashkboos_SliceGPT]], [[2024_Gu_MiniLLM]], synthesized in [[2025_Liu_ModelCompressionSurvey]]. Worth watching whether this becomes a distinct sub-category ("LLM edge compression") rather than a variant of the existing CNN-era techniques, since calibration cost and structured-vs-unstructured trade-offs differ from the AlexNet/VGG-era literature.

**2026-06-30 — Vision: hybrid CNN/transformer architectures emerging alongside pure CNNs.** [[2025_Zeng_TinyNeXt]] targets the memory-bound nature of standard self-attention directly (Lean Single-Head Self-Attention) and pairs it with a stage-aware CNN/transformer macro design, extending MobileNet-style efficient-by-design thinking to a new architecture family. Still a single data point; not yet enough to call this a sub-category split, but worth tracking as more TinyML-scale transformer work appears.

**2026-06-30 — Frameworks/Hardware: NPU vendors building compilation stacks directly on MLIR.** [[2026_Absar_HexagonMLIR]] (Qualcomm Hexagon) is a large industrial-scale case of an NPU vendor lowering standard front-ends (Triton, PyTorch) through MLIR's dialect infrastructure rather than a bespoke toolchain. Combined with [[2023_Das_MLDrivenHardwareCostModelMLIR]] (learned MLIR-level cost models), this suggests [[MLIR]] is consolidating as shared compiler infrastructure across NPU vendors, not just an academic substrate — worth re-checking in a year whether more vendors follow.

**2026-06-30 — Toolchain bifurcation: general compilers retreating from MCU-class targets vs. in-sensor AI.** Per the 2026-06 monthly report, Apache TVM's v0.25.0 release candidate trims "leftover microTVM/CRT crumbs" and the TVM forum has an open thread questioning microTVM's future, while hardware vendors (e.g. STMicroelectronics' ISPU 2.0) push AI processing further down into the sensor itself. Not proof microTVM is being discontinued, but a real signal that MCU-native libraries ([[CMSIS-NN]], [[TensorFlow_Lite_Micro]]) may be consolidating their position as the practical default for ultra-low-power deployment while [[microTVM_TVM]]'s center of gravity drifts toward GPU/accelerator-class hardware. Re-check in subsequent monthly reports.
