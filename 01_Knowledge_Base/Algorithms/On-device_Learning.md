# On-device Learning

## Evolution of the concept

Early TinyML work focused almost entirely on inference: train in the cloud, deploy a frozen model. On-device learning challenges that split by asking whether a deployed device can update its own model from locally collected data — for personalization, adaptation to drift, or privacy reasons (no raw data leaves the device). The main obstacle is memory: standard back-propagation needs to store activations, gradients, and optimizer state, which can be orders of magnitude larger than the SRAM available on a microcontroller. Lin et al. (2022) make a first concrete, hardware-validated case that training (not just inference) is possible within a 256 KB memory budget, via a combination of quantization-aware training tricks and selecting only a sparse subset of weights to update. TinyTrain (Kwon et al., ICML 2024) extends this line by tackling a second constraint that TinyTL/the 256 KB work left open — data scarcity at the edge — combining a task- and memory-aware sparse-update selection with a meta-learning pre-training phase so that on-device fine-tuning needs less labeled data, validated on real microcontroller and mobile hardware.

## Key papers

[[2022_Lin_OnDeviceTraining256KB]] — algorithm-system co-design (Quantization-Aware Scaling + Sparse Update + a dedicated Tiny Training Engine) enabling on-device transfer learning within 256 KB of memory, validated on real microcontroller hardware.

[[2020_Cai_TinyTL]] — identifies activations, not weights, as the real memory bottleneck for on-device training, and freezes the backbone while learning only a small memory-efficient bias/lite-residual module, cutting training memory up to 12.9x; an important precursor to the sparse-update line of work in [[2022_Lin_OnDeviceTraining256KB]].

[[2024_Kwon_TinyTrain]] — task-adaptive sparse-update selection combined with meta-learning pre-training to jointly address compute/memory and data-scarcity constraints, validated on real edge hardware under few-shot conditions.

## Open problems

How to make on-device learning robust to non-stationary, continuously drifting data without unbounded memory growth (the intersection with [[Continual_Learning]]). How to extend memory-budgeted training beyond vision transfer learning to other modalities (audio, time series, biosignals). How to combine on-device training with federated aggregation ([[Federated_Learning]]) without compounding the memory and communication costs.

## Research ideas

A sparse-update training scheme specialized for streaming sensor data (audio, IMU, biosignals) rather than vision transfer learning; combining importance-aware weight protection (as in EWC-style continual learning) with a fixed training memory budget, so devices can keep adapting over months without forgetting or running out of memory.

## Possible thesis topics

Implementing and benchmarking on-device training for a non-vision EdgeAI task (e.g. keyword spotting personalization, or HAR model adaptation to a new user) on real Cortex-M hardware, measuring memory, energy, and accuracy trade-offs against the cloud-trained baseline.

## Links

[[Continual_Learning]], [[Federated_Learning]], [[Quantization]], [[Cortex-M]]
