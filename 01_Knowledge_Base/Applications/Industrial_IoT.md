# Industrial IoT

## Evolution of the concept

Industrial IoT applications of EdgeAI center on monitoring industrial assets in environments where continuous cloud connectivity is unreliable or unavailable (extreme heat, vibration, restricted physical access), and where labeled failure data is typically scarce. The field has moved toward unsupervised anomaly detection methods that can be trained directly on resource-constrained edge hardware without requiring curated failure examples, demonstrating that not just inference but the training phase itself can be pushed to extremely low-cost microcontrollers via Tiny-MLOps methodologies. This is a direct, concrete instance of the broader [[On-device_Learning]] research direction applied to a real industrial use case.

## Key papers

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] — end-to-end Tiny-MLOps anomaly detection system performing unsupervised on-device training (isolation forest) on an ESP32 microcontroller for extreme industrial environments.

## Open problems

How does fully on-device unsupervised training compare, in detection accuracy, to deep-learning-based anomaly detection methods deployed via inference-only edge pipelines? Can on-device training methodologies developed for general deep learning (sparse update, quantization-aware scaling) extend classical-ML on-device training (isolation forest) to lightweight deep anomaly-detection models on the same hardware class?

## Research ideas

Combining on-device unsupervised anomaly detection with sparse-update or quantization-aware on-device training techniques to move from classical ML (isolation forest) to lightweight deep anomaly-detection models trainable within the same microcontroller resource envelope.

## Possible thesis topics

Extending on-device unsupervised training from isolation forest to a lightweight deep anomaly-detection model on ESP32-class hardware; comparative study of on-device-trained versus cloud-trained anomaly detection for the same industrial asset class.

## Links

[[Predictive_Maintenance]], [[On-device_Learning]], [[Compression]], [[Cortex-M]]
