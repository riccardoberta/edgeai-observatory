# Human Activity Recognition (HAR)

HAR classifies a person's physical activity — walking, running, sitting, falling, and similar — from wearable sensor data, typically an accelerometer and/or gyroscope stream. The central open challenge for EdgeAI is delivering good accuracy within the tight compute, memory, and power budgets of mobile and wearable hardware.

## Evolution of the concept

HAR moved from hand-engineered features and classical machine learning toward deep-learning architectures (CNNs, RNNs/LSTMs, and hybrids), substantially improving recognition accuracy. Ronao and Cho ("Human Activity Recognition with Smartphone Sensors Using Deep Learning Neural Networks", 2016) is one of the field's most-cited early results, establishing CNNs as automatic feature extractors for smartphone-sensor HAR in place of hand-engineered features. Ordóñez and Roggen ("Deep Convolutional and LSTM Recurrent Neural Networks for Multimodal Wearable Activity Recognition", 2016) push the architecture further with DeepConvLSTM, a generic CNN+LSTM design that performs sensor fusion naturally across modalities and explicitly models the temporal dynamics of activity, without requiring hand-engineered features — establishing the architecture family later HAR work builds on.

More recently, the field has begun exploring cross-modal foundation-model approaches (tokenizing activity sensor signals alongside EEG/ECG, see [[Biosignals]]) and self-supervised pretraining on very large unlabeled wearable datasets, raising the question of how to compress such foundation models down to something deployable on-device.

On the compression side, Contoli and Lattanzi ("A Study on the Application of TensorFlow Compression Techniques to Human Activity Recognition", 2023) systematically compare quantization strategies (dynamic-range, full-integer, cascading) across CNN, LSTM, and CNN-LSTM HAR architectures. A follow-up study by the same lead author (Lattanzi et al., 2024) directly tests one assumption behind the broader transformer-adoption trend on the tiniest deployment tier: under a realistic tiny-wearable RAM budget, the most capable deployable transformer variant achieves up to 14% lower accuracy than CNN/LSTM baselines, showing that transformers' theoretical time-series advantages do not automatically transfer once genuinely constrained to tiny-device memory.

A complementary study (Moreira, 2024) supplies exactly the deployment-realistic validation this concept's open problems below ask for: a HAR model deployed and validated in real time on a genuine commercial low-power microcontroller kit (B-L475E-IOT01A), reaching 90% overall accuracy for dynamic activities but with honestly reported, lower recall for static-activity discrimination (sitting vs. standing) — a concrete failure mode that offline-accuracy-only benchmarks tend not to surface.

## Key papers

[[2016_Ordonez_DeepConvLSTM]] — DeepConvLSTM, a generic CNN+LSTM architecture for multimodal wearable HAR with natural sensor fusion and explicit temporal modeling, foundational for the architecture family later surveyed below.

[[2022_Zhang_DeepLearningHARWearableSensors]] — systematic review categorizing deep learning architectures for wearables-based HAR and their resource-constraint trade-offs.

[[2024_Lattanzi_TransformersTinyHAR]] — hardware-budget-constrained empirical comparison showing transformers lose up to 14% accuracy versus CNN/LSTM baselines once genuinely constrained to tiny-wearable RAM budgets.

[[2024_Moreira_HighPerformanceHAR]] — real-time HAR deployed and validated on a genuine commercial low-power microcontroller kit, reaching 90% overall accuracy, with honestly reported lower recall for static-activity discrimination.

[[2026_Darvishi_EmbeddedMLPipelines]] — a tutorial/systems synthesis (not an empirical study) using a 2-second, 3-axis accelerometer window reduced to root-mean-square and spectral features as its running example; useful as a teaching reference for the feature-extraction and validation pitfalls specific to wearable HAR pipelines, not as a benchmark source.

[[2016_Ronao_HARSmartphoneSensorsDeepLearning]] — one of the field's most-cited early deep-learning HAR papers, establishing CNNs as automatic feature extractors for smartphone-sensor activity recognition.

[[2023_Contoli_TensorFlowCompressionHAR]] — systematic comparison of TensorFlow Lite compression techniques across CNN/LSTM/CNN-LSTM HAR architectures; direct precursor to the tiny-transformer comparison above.

## Open problems

How do the most accurate wearable HAR architectures perform when actually deployed on Cortex-M-class hardware under realistic power budgets, rather than evaluated only for offline accuracy? How much does self-supervised pretraining on large-scale unlabeled wearable data change the accuracy-versus-resource trade-off, and can the resulting models be compressed enough for on-device deployment?

## Research ideas

Benchmarking the architecture families above on real Cortex-M/Cortex-A hardware for energy-per-inference and latency, to ground qualitative comparisons in deployment-realistic numbers. Compressing a cross-modal biosignal/activity foundation model (BIOT-style, see [[Biosignals]]) for wearable-class hardware.

## Possible thesis topics

An on-device benchmark of CNN versus RNN/LSTM versus hybrid HAR architectures for energy-per-inference on wearable-class hardware. Compressing a self-supervised wearable HAR foundation model for microcontroller deployment.

## Links

[[Biosignals]], [[On-device_Learning]], [[Quantization]], [[Compression]], [[Cortex-M]]
