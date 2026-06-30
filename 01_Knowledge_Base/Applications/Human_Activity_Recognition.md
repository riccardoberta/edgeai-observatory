# Human Activity Recognition

## Evolution of the concept

Human Activity Recognition (HAR) from mobile and wearable sensor data (accelerometer, gyroscope) moved from hand-engineered features and classical ML toward deep learning architectures (CNNs, RNNs/LSTMs, hybrids), substantially improving recognition accuracy. Ordóñez and Roggen's "Deep Convolutional and LSTM Recurrent Neural Networks for Multimodal Wearable Activity Recognition" (Sensors, MDPI, 2016) is one of the foundational papers in this shift: it introduces DeepConvLSTM, a generic CNN+LSTM architecture that performs sensor fusion naturally across modalities and explicitly models the temporal dynamics of activity, without requiring hand-engineered features — establishing the architecture family later HAR work (and the systematic review below) builds on. The central open challenge for EdgeAI is that this accuracy gain must be delivered within the tight compute, memory, and power budgets of mobile and wearable hardware. More recently, the field has begun exploring cross-modal foundation-model approaches (e.g. tokenizing activity sensory signals alongside EEG/ECG) and self-supervised pretraining on very large unlabeled wearable datasets, which raises a new open question of how to compress such foundation models down to something deployable on-device. A 2024 study (Lattanzi et al.) directly tests one assumption behind this transformer-adoption trend on the tiniest deployment tier: under a realistic tiny-wearable RAM budget, the most capable deployable transformer variant achieves up to 14% lower accuracy than CNN/LSTM baselines, showing that transformers' theoretical time-series advantages do not automatically transfer once genuinely constrained to tiny-device memory.

## Key papers

[[2016_Ordonez_DeepConvLSTM]] — DeepConvLSTM, a generic CNN+LSTM architecture for multimodal wearable HAR with natural sensor fusion and explicit temporal modeling, foundational for the architecture family later surveyed below.

[[2022_Zhang_DeepLearningHARWearableSensors]] — systematic review categorizing deep learning architectures for wearables-based HAR and their resource-constraint trade-offs.

[[2024_Lattanzi_TransformersTinyHAR]] — hardware-budget-constrained empirical comparison showing transformers lose up to 14% accuracy versus CNN/LSTM baselines once genuinely constrained to tiny-wearable RAM budgets.

## Open problems

How do the most accurate wearable HAR architectures perform when actually deployed on Cortex-M-class hardware under realistic power budgets, rather than evaluated only for offline accuracy? How much does self-supervised pretraining on large-scale unlabeled wearable data change the accuracy-versus-resource trade-off, and can the resulting models be compressed enough for on-device deployment?

## Research ideas

Benchmarking the architecture families surveyed in the review on real Cortex-M/Cortex-A hardware for energy-per-inference and latency, to ground qualitative comparisons in deployment-realistic numbers; compressing a cross-modal biosignal/activity foundation model (e.g. BIOT-style) for wearable-class hardware.

## Possible thesis topics

On-device benchmark of CNN versus RNN/LSTM versus hybrid HAR architectures for energy-per-inference on wearable-class hardware; compressing a self-supervised wearable HAR foundation model for microcontroller deployment.

## Links

[[Biosignals]], [[On-device_Learning]], [[Quantization]], [[Compression]], [[Cortex-M]]
