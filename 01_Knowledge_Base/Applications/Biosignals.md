# Biosignals

## Evolution of the concept

Biosignal analysis (EEG, ECG, PPG, EMG, and related physiological signals) has historically relied on deep learning models trained and specialized for one specific dataset and clinical setting, which limited cross-study and cross-device generalization. The field is now shifting toward foundation-model approaches that tokenize heterogeneous biosignals into a unified representation, enabling a single model to be pretrained across multiple structurally different datasets (different channel counts, sample lengths, missing-value patterns) and fine-tuned for varied downstream clinical tasks. For EdgeAI specifically, the central tension is that these foundation models are far larger than what embedded biosignal-sensing hardware can run directly, making compression (quantization, pruning, distillation) a critical open direction to bring foundation-model-level performance to wearable health-monitoring devices.

## Key papers

[[2023_Yang_BIOT]] — Biosignal Transformer (BIOT) foundation model demonstrating cross-data pretraining and fine-tuning across EEG, ECG, and human activity sensory signals via a unified tokenization scheme.

## Open problems

How much can biosignal foundation models be compressed (quantization, pruning, distillation) while retaining cross-dataset transfer benefits, to make them viable for on-device biosignal monitoring? Does cross-modal pretraining generalize to other biosignals relevant to edge health monitoring beyond EEG/ECG/activity, such as PPG or EMG?

## Research ideas

Applying quantization and distillation to a BIOT-style biosignal foundation model to evaluate how much cross-dataset benefit survives compression to a footprint suitable for embedded health-monitoring hardware.

## Possible thesis topics

Compressing a cross-modal biosignal foundation model for deployment on Cortex-M/Cortex-A-class wearable hardware; extending unified biosignal tokenization to additional modalities (PPG, EMG) relevant to wearable health monitoring.

## Links

[[Human_Activity_Recognition]], [[Quantization]], [[Distillation]], [[Compression]], [[On-device_Learning]]
