# Industrial IoT

Industrial IoT applications of EdgeAI center on monitoring industrial assets — machinery, production lines, plant infrastructure — in environments where continuous cloud connectivity is unreliable or unavailable (extreme heat, vibration, restricted physical access) and where labeled failure data is typically scarce.

## Evolution of the concept

A key enabler for acoustic-based anomaly detection specifically was the release of the MIMII dataset (Purohit et al., 2019): normal and anomalous operating sounds recorded from real industrial machines (valves, pumps, fans, slide rails), which gave the field a shared, realistic benchmark for unsupervised sound-based anomaly detection instead of ad hoc, non-comparable private recordings.

The field has moved toward unsupervised anomaly-detection methods that can be trained directly on resource-constrained edge hardware without requiring curated failure examples — Antonini et al. (2023) demonstrate that not just inference but the training phase itself can be pushed to extremely low-cost microcontrollers, using an unsupervised isolation-forest algorithm on an ESP32. This is a direct, concrete instance of the broader [[On-device_Learning]] research direction applied to a real industrial use case.

Two further studies broaden the picture in different directions. Luján-Mora et al. (2025) add a scalability dimension: an RNN/autoencoder edge fault-detection architecture validated across heterogeneous real hardware (from Raspberry Pi to NVIDIA Jetson), reaching 92.0% detection accuracy at sub-150ms response time and scaling to 500 IoT devices while holding accuracy above 88% — a rare case of accuracy, latency, energy, and multi-device scalability all evaluated together rather than any one metric in isolation. Liu et al. ("Deep Anomaly Detection for Time-Series Data in Industrial IoT", 2021) instead train an attention-CNN-LSTM anomaly detector via communication-efficient on-device federated learning across distributed nodes — a distinct, not-yet-compared strategy from Antonini et al.'s on-device unsupervised training route for distributed anomaly detection (see also [[Federated_Learning]]).

Alharthi et al. (2026) provide the first dedicated systematic review of exactly this concept's intersection — TinyML applied to Industrial IoT — synthesizing 35 studies and identifying predictive maintenance, equipment monitoring, and anomaly detection as the dominant application clusters, with vibration sensing as the most common sensor modality.

## Key papers

[[2019_Purohit_MIMIIDataset]] — public dataset of normal/anomalous sounds from real industrial machines (valves, pumps, fans, slide rails), establishing a shared benchmark for unsupervised industrial acoustic anomaly detection.

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] — end-to-end system performing unsupervised on-device training (isolation forest) on an ESP32 microcontroller for extreme industrial environments.

[[2024_delaFuente_ESN-PdM]] — dynamically routes predictive-maintenance inference between on-device, on-gateway, and cloud execution depending on accuracy/latency/battery needs, using TinyML optimization to make the edge tiers viable.

[[2025_LujanMora_EdgeAIFaultDetectionIoT]] — RNN/autoencoder edge fault-detection architecture validated across heterogeneous hardware (Raspberry Pi to Jetson), 92.0% accuracy at under 150ms, scaling to 500 devices with accuracy holding above 88%.

[[2021_Liu_DeepAnomalyDetectionFederatedIIoT]] — attention-CNN-LSTM anomaly detector trained via communication-efficient on-device federated learning across industrial nodes, one of the most-cited papers bridging federated learning and industrial anomaly detection.

[[2026_Alharthi_TinyMLIndustrialIoTSystematicReview]] — first dedicated systematic review of TinyML for Industrial IoT, synthesizing 35 studies across applications, system components, and methodologies.

## Open problems

How does fully on-device unsupervised training compare, in detection accuracy, to deep-learning-based anomaly detection methods deployed via inference-only edge pipelines? Can on-device training methodologies developed for general deep learning (sparse update, quantization-aware scaling) extend classical machine-learning on-device training (isolation forest) to lightweight deep anomaly-detection models on the same hardware class?

## Research ideas

Combining on-device unsupervised anomaly detection with sparse-update or quantization-aware on-device training techniques, to move from classical machine learning (isolation forest) to lightweight deep anomaly-detection models trainable within the same microcontroller resource envelope.

## Possible thesis topics

Extending on-device unsupervised training from isolation forest to a lightweight deep anomaly-detection model on ESP32-class hardware. A comparative study of on-device-trained versus cloud-trained anomaly detection for the same industrial asset class.

## Links

[[Predictive_Maintenance]], [[On-device_Learning]], [[Compression]], [[Cortex-M]]
