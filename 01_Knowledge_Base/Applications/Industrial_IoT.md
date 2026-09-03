# Industrial IoT

## Evolution of the concept

Industrial IoT applications of EdgeAI center on monitoring industrial assets in environments where continuous cloud connectivity is unreliable or unavailable (extreme heat, vibration, restricted physical access), and where labeled failure data is typically scarce. A key enabler for acoustic-based anomaly detection specifically was the release of the MIMII dataset (Purohit et al., DCASE 2019 Workshop) — normal and anomalous operating sounds recorded from real industrial machines (valves, pumps, fans, slide rails) — which gave the field a shared, realistic benchmark for unsupervised sound-based anomaly detection instead of ad-hoc, non-comparable private recordings. The field has moved toward unsupervised anomaly detection methods that can be trained directly on resource-constrained edge hardware without requiring curated failure examples, demonstrating that not just inference but the training phase itself can be pushed to extremely low-cost microcontrollers via Tiny-MLOps methodologies. This is a direct, concrete instance of the broader [[On-device_Learning]] research direction applied to a real industrial use case. A 2025 Springer open-access study (Luján-Mora) adds a scalability dimension the on-device-training and hierarchical-routing literature above does not directly address: an RNN/autoencoder edge fault-detection architecture validated across heterogeneous real hardware (Raspberry Pi through NVIDIA Jetson), reaching 92.0% detection accuracy at sub-150ms response time and scaling to 500 IoT devices while holding accuracy above 88% — a rare case of accuracy, latency, energy, and multi-device scalability all evaluated together rather than any one metric in isolation. A 2026-09-03 exhaustive Scholar audit added two further anchors. Liu et al.'s "Deep Anomaly Detection for Time-Series Data in Industrial IoT" (IEEE IoT Journal, 2021, 750+ citations) is one of the most-cited papers at the intersection of federated learning and industrial anomaly detection, training an attention-CNN-LSTM detector via communication-efficient on-device federated learning rather than the on-device unsupervised training route this concept's Antonini et al. anchor takes — the two papers represent distinct, not-yet-compared strategies for distributed IIoT anomaly detection. A 2026 MDPI Sensors systematic review (Alharthi et al.) is the first dedicated survey for exactly this concept's intersection (TinyML + Industrial IoT), synthesizing 35 studies and identifying predictive maintenance, equipment monitoring, and anomaly detection as the dominant application clusters with vibration sensing as the most common sensor modality.

## Key papers

[[2019_Purohit_MIMIIDataset]] — public dataset of normal/anomalous sounds from real industrial machines (valves, pumps, fans, slide rails), establishing a shared benchmark for unsupervised industrial acoustic anomaly detection.

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] — end-to-end Tiny-MLOps anomaly detection system performing unsupervised on-device training (isolation forest) on an ESP32 microcontroller for extreme industrial environments.

[[2024_delaFuente_ESN-PdM]] — dynamically routes predictive-maintenance inference between on-device, on-gateway, and cloud execution depending on accuracy/latency/battery needs, using TinyML optimization to make the edge tiers viable.

[[2025_LujanMora_EdgeAIFaultDetectionIoT]] — RNN/autoencoder edge fault-detection architecture validated across heterogeneous hardware (Raspberry Pi to Jetson), 92.0% accuracy at <150ms, scaling to 500 devices with accuracy holding above 88%.

[[2021_Liu_DeepAnomalyDetectionFederatedIIoT]] — attention-CNN-LSTM anomaly detector trained via communication-efficient on-device federated learning across IIoT nodes, one of the most-cited papers bridging Federated_Learning and industrial anomaly detection.

[[2026_Alharthi_TinyMLIndustrialIoTSystematicReview]] — first dedicated systematic review of TinyML-for-Industrial-IoT, synthesizing 35 studies across applications, system components, and methodologies.

## Open problems

How does fully on-device unsupervised training compare, in detection accuracy, to deep-learning-based anomaly detection methods deployed via inference-only edge pipelines? Can on-device training methodologies developed for general deep learning (sparse update, quantization-aware scaling) extend classical-ML on-device training (isolation forest) to lightweight deep anomaly-detection models on the same hardware class?

## Research ideas

Combining on-device unsupervised anomaly detection with sparse-update or quantization-aware on-device training techniques to move from classical ML (isolation forest) to lightweight deep anomaly-detection models trainable within the same microcontroller resource envelope.

## Possible thesis topics

Extending on-device unsupervised training from isolation forest to a lightweight deep anomaly-detection model on ESP32-class hardware; comparative study of on-device-trained versus cloud-trained anomaly detection for the same industrial asset class.

## Links

[[Predictive_Maintenance]], [[On-device_Learning]], [[Compression]], [[Cortex-M]]
