# Deep Learning in Human Activity Recognition with Wearable Sensors: A Review on Advances

**Full citation:** Zhang, S., Li, Y., Zhang, S., Shahabi, F., Xia, S., Deng, Y., Alshurafa, N. (2022). Deep Learning in Human Activity Recognition with Wearable Sensors: A Review on Advances. arXiv:2111.00418. https://arxiv.org/abs/2111.00418

**Linked concepts:** [[Human_Activity_Recognition]], [[Quantization]], [[Compression]]

## Abstract summary

The authors present a comprehensive, systematic review of deep learning methods applied to human activity recognition (HAR) using mobile and wearable sensor data, categorizing existing architectures (CNNs, RNNs, LSTMs, hybrid models) and discussing the practical constraints of deploying them on resource-limited mobile and wearable devices for applications such as activity tracking, wellness monitoring, and human-computer interaction.

## Research problem

Wearable and mobile devices provide a rich stream of low-power sensor data (accelerometer, gyroscope, and similar), but turning this raw sensor data into reliable activity recognition has historically relied on hand-engineered features and classical machine learning; deep learning has improved recognition accuracy substantially, but the resulting models must still operate within the tight compute, memory, and power budgets of mobile and wearable hardware, and the field lacked a systematic categorization of how different deep learning approaches address this trade-off.

## Key idea

Systematically organize the wearables-based HAR literature by deep learning architecture family and by how each approach handles the sensor-data-to-activity-label pipeline (feature learning, temporal modeling, multi-sensor fusion), making explicit the accuracy-versus-resource-constraint trade-offs relevant to on-device deployment.

## Technical contribution

A structured taxonomy and critical comparison of CNN-based, RNN/LSTM-based, and hybrid deep learning architectures for HAR, alongside a discussion of public benchmark datasets, common preprocessing pipelines, and the specific deployment constraints of mobile/wearable hardware.

## Experimental methodology

As a review paper, the methodology is a systematic literature survey: collecting, categorizing, and critically comparing published HAR deep learning approaches across architecture type, sensor modality, dataset used, and reported accuracy, rather than running new experiments.

## Results

The review documents a clear architectural trend toward CNN and hybrid CNN-RNN models for wearable HAR, identifies the public datasets most commonly used for benchmarking, and highlights recurring open challenges: limited labeled data, sensor placement/orientation variability, and the gap between reported accuracy and what is achievable under real on-device resource constraints.

## Comparison with the state of the art

Complements broader EdgeAI surveys by focusing specifically on the wearable-sensor HAR sub-field, providing a more detailed architectural breakdown than general TinyML surveys, while remaining a synthesis paper rather than introducing a new model or hardware result itself.

## Strengths

Comprehensive, systematic coverage of a fast-moving sub-field; useful as an entry point and taxonomy for newcomers to wearable HAR; explicitly connects model architecture choices to deployment constraints relevant to this Observatory's Hardware taxonomy.

## Weaknesses

Being a 2021/2022 review, it does not cover more recent self-supervised and foundation-model approaches to HAR (e.g. large-scale pretraining on hundreds of thousands of person-days of wearable data); as a survey, it does not provide new quantitative benchmarks of its own.

## Limitations

Survey papers age quickly in a fast-moving field; specific architecture recommendations should be checked against more recent primary literature before being treated as current best practice.

## Open questions

How do the most accurate wearable HAR architectures identified in this review perform when actually deployed on Cortex-M-class hardware under realistic power budgets, rather than evaluated only for offline accuracy? How much does self-supervised pretraining on large-scale unlabeled wearable data (a direction emerging after this review) change the accuracy-versus-resource trade-off?

## Possible extensions

An updated review or benchmark incorporating self-supervised and foundation-model approaches to wearable HAR, explicitly measured for on-device latency and energy rather than only offline accuracy.

## Relevance to our research

Foundational survey reference for the [[Human_Activity_Recognition]] branch of our Applications taxonomy, providing the architectural landscape against which specific deployed/optimized HAR models can be compared.

## Possible thesis topics

Benchmarking the top architecture families identified in this review on real Cortex-M/Cortex-A hardware for energy-per-inference and latency, to ground the review's qualitative comparisons in deployment-realistic numbers; extending wearable HAR with self-supervised pretraining under embedded resource constraints.

## Possible collaborations

Wearable sensing and mobile health research groups; HAR benchmark dataset maintainers.

## Links to related papers

[[2023_Yang_BIOT]], [[2022_Lin_OnDeviceTraining256KB]] (on-device training constraints directly relevant to wearable HAR deployment)
