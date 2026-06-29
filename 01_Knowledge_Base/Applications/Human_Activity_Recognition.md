# Human Activity Recognition

## Evolution of the concept

Human Activity Recognition (HAR) from mobile and wearable sensor data (accelerometer, gyroscope) moved from hand-engineered features and classical ML toward deep learning architectures (CNNs, RNNs/LSTMs, hybrids), substantially improving recognition accuracy. The central open challenge for EdgeAI is that this accuracy gain must be delivered within the tight compute, memory, and power budgets of mobile and wearable hardware. More recently, the field has begun exploring cross-modal foundation-model approaches (e.g. tokenizing activity sensory signals alongside EEG/ECG) and self-supervised pretraining on very large unlabeled wearable datasets, which raises a new open question of how to compress such foundation models down to something deployable on-device.

## Key papers

[[2022_Zhang_DeepLearningHARWearableSensors]] — systematic review categorizing deep learning architectures for wearables-based HAR and their resource-constraint trade-offs.

## Open problems

How do the most accurate wearable HAR architectures perform when actually deployed on Cortex-M-class hardware under realistic power budgets, rather than evaluated only for offline accuracy? How much does self-supervised pretraining on large-scale unlabeled wearable data change the accuracy-versus-resource trade-off, and can the resulting models be compressed enough for on-device deployment?

## Research ideas

Benchmarking the architecture families surveyed in the review on real Cortex-M/Cortex-A hardware for energy-per-inference and latency, to ground qualitative comparisons in deployment-realistic numbers; compressing a cross-modal biosignal/activity foundation model (e.g. BIOT-style) for wearable-class hardware.

## Possible thesis topics

On-device benchmark of CNN versus RNN/LSTM versus hybrid HAR architectures for energy-per-inference on wearable-class hardware; compressing a self-supervised wearable HAR foundation model for microcontroller deployment.

## Links

[[Biosignals]], [[On-device_Learning]], [[Quantization]], [[Compression]], [[Cortex-M]]
