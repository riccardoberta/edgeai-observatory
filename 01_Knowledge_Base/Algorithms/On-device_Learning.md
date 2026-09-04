# On-device Learning

On-device learning asks whether a deployed device can update its own model from locally collected data — for personalization, adaptation to drift, or privacy (no raw data leaves the device) — instead of the usual approach of training in the cloud and deploying a frozen model. The main obstacle is memory: standard backpropagation needs to store activations, gradients, and optimizer state, which together can be orders of magnitude larger than the SRAM available on a microcontroller.

## Evolution of the concept

Saha, Sandha, and Srivastava's review (IEEE Sensors Journal, 2022) covers the full microcontroller-class machine-learning pipeline end to end — algorithm, compression, runtime, hardware — and treats on-device training and adaptation as one explicit stage of that pipeline rather than an isolated topic, making it a useful general entry point.

Cai et al.'s TinyTL (2020) identifies *activations*, not weights, as the real memory bottleneck for on-device training, and freezes the network's backbone while training only a small, memory-efficient bias or "lite-residual" module, cutting training memory by up to 12.9x. Lin et al. (2022) build on this insight to make a first concrete, hardware-validated case that full training — not just inference — is possible within a 256 KB memory budget: an algorithm-system co-design combining Quantization-Aware Scaling (keeping training numerically stable in low precision without needing normalization layers), a Sparse Update scheme (updating only a selected subset of weights rather than the whole network), and a dedicated lightweight training engine, validated on real microcontroller hardware. Deutel et al. (2024) push further still, keeping the *entire* training loop — forward pass, backward pass, and weight update — in a fully quantized integer representation with dynamic partial-gradient updates, demonstrated across three Cortex-M variants (M0+, M4, M7).

TinyTrain (Kwon et al., ICML 2024) tackles a second constraint the memory-focused work above leaves open: data scarcity at the edge. It combines task- and memory-aware sparse-update selection with a meta-learning pre-training phase, so that on-device fine-tuning needs less labeled data, validated on real microcontroller and mobile hardware under few-shot conditions.

Freitag et al. (2022) provide an earlier, real-hardware data point specifically for combining on-device training with federated learning: implementing the full training loop directly on microcontrollers for a keyword-spotting task, and characterizing — through physical-device experiments rather than simulation — how federated-round frequency trades off against bandwidth usage and training time (see also [[Federated_Learning]]).

## Key papers

[[2022_Saha_MLMicrocontrollerClassHardwareReview]] — broad, full-pipeline review of microcontroller-class machine learning (algorithm, compression, runtime, hardware) treating on-device training and adaptation as one explicit pipeline stage.

[[2022_Lin_OnDeviceTraining256KB]] — algorithm-system co-design (Quantization-Aware Scaling, Sparse Update, and a dedicated Tiny Training Engine) enabling on-device transfer learning within 256 KB of memory, validated on real microcontroller hardware.

[[2020_Cai_TinyTL]] — identifies activations, not weights, as the real memory bottleneck for on-device training, and freezes the backbone while learning only a small memory-efficient bias/lite-residual module, cutting training memory up to 12.9x; an important precursor to the sparse-update approach above.

[[2024_Kwon_TinyTrain]] — task-adaptive sparse-update selection combined with meta-learning pre-training to jointly address compute/memory constraints and data scarcity, validated on real edge hardware under few-shot conditions.

[[2024_Deutel_OnDeviceTrainingQuantizedCortexM]] — keeps the entire training loop (forward pass, backward pass, weight update) in a fully quantized integer representation with dynamic partial-gradient updates, demonstrated across Cortex-M0+/M4/M7.

[[2021_David_TensorFlowLiteMicro]] — the inference runtime whose static-allocation, no-operating-system design underlies many on-device training implementations targeting the same microcontroller-class hardware.

[[2017_Kirkpatrick_OvercomingCatastrophicForgetting]] — Elastic Weight Consolidation, directly relevant to keeping on-device learning stable under non-stationary data (see Open problems below).

[[2025_Gao_TinyMLBearingFaultDiagnosis]] — transfer learning with limited target-domain labels, optimized and deployed directly on an ESP32-S3 microcontroller for industrial fault diagnosis.

[[2022_Freitag_OnDeviceTrainingMCUFederated]] — real-microcontroller implementation of on-device training combined with federated learning for keyword spotting, characterizing the round-frequency/bandwidth/training-time trade-off empirically rather than in simulation.

## Open problems

How to make on-device learning robust to non-stationary, continuously drifting data without unbounded memory growth — the intersection with [[Continual_Learning]]. How to extend memory-budgeted training beyond vision transfer learning to other modalities (audio, time series, biosignals). How to combine on-device training with federated aggregation ([[Federated_Learning]]) without compounding memory and communication costs.

## Research ideas

A sparse-update training scheme specialized for streaming sensor data (audio, inertial-measurement-unit, biosignals) rather than vision transfer learning. Combining importance-aware weight protection, as in EWC-style continual learning, with a fixed training memory budget, so devices can keep adapting over months without forgetting or running out of memory.

## Possible thesis topics

Implementing and benchmarking on-device training for a non-vision EdgeAI task — for example keyword-spotting personalization, or Human Activity Recognition model adaptation to a new user — on real Cortex-M hardware, measuring memory, energy, and accuracy trade-offs against a cloud-trained baseline.

## Links

[[Continual_Learning]], [[Federated_Learning]], [[Quantization]], [[Cortex-M]]
