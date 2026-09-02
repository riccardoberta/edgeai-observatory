# Implementation of Edge AI for Early Fault Detection in IoT Networks: Evaluation of Performance and Scalability in Complex Applications

**Full citation:** Luján-Mora, S. (2025). Implementation of edge AI for early fault detection in IoT networks: evaluation of performance and scalability in complex applications. Discover Internet of Things, 5, 108. DOI: 10.1007/s43926-025-00196-4

**PDF:** [Springer (open access)](https://link.springer.com/article/10.1007/s43926-025-00196-4)

**Verification note:** Springer open-access article; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[Industrial_IoT]], [[Predictive_Maintenance]]

## Abstract summary

Introduces an edge-based AI architecture for early fault detection in heterogeneous IoT networks, using recurrent neural networks and autoencoders optimized for time-series anomaly detection with inference running locally on edge nodes. Evaluated under realistic laboratory conditions on Raspberry Pi and NVIDIA Jetson platforms, the system achieves a 92.0% fault detection rate with response times consistently under 150 ms, reduces energy consumption to 50 Wh under standard conditions, and scales to 500 IoT devices while maintaining detection accuracy above 88%.

## Research problem

Traditional cloud-based IoT fault-detection solutions suffer from excessive latency and energy overhead due to continuous data transmission and centralized analysis, which is particularly costly for early fault detection where response time directly affects how much damage or downtime can be avoided; a genuinely scalable, low-latency, energy-efficient edge-based alternative had not been validated across realistic device counts and heterogeneous hardware.

## Key idea

Run RNN- and autoencoder-based time-series anomaly detection directly on heterogeneous edge nodes (from Raspberry Pi to NVIDIA Jetson) rather than centralizing detection in the cloud, and explicitly evaluate the architecture's scalability (up to 500 devices) and energy profile alongside detection accuracy and latency, rather than validating fault-detection accuracy alone.

## Technical contribution

An edge-based fault-detection architecture combining RNN and autoencoder anomaly detection, validated for accuracy, latency, energy, and scalability together across heterogeneous real edge hardware (Raspberry Pi, Jetson) and up to 500 simulated/tested devices — a broader validation scope than most single-metric fault-detection papers.

## Experimental methodology

Laboratory evaluation on a range of IoT devices and edge computing platforms (Raspberry Pi, NVIDIA Jetson), measuring fault detection rate, response time, energy consumption, and scalability up to 500 IoT devices under realistic operating conditions.

## Results

92.0% fault detection rate with response time consistently under 150 ms; energy consumption reduced to 50 Wh under standard conditions; the architecture scaled to 500 IoT devices while maintaining detection accuracy above 88%, outperforming cloud-based approaches in both latency and energy metrics.

## Comparison with the state of the art

Extends this Observatory's existing industrial-IoT anomaly-detection literature (unsupervised on-device training in [[2023_Antonini_TinyMLAnomalyDetectionIndustrial]], hierarchical edge-gateway-cloud routing in [[2024_delaFuente_ESN-PdM]]) with an explicit multi-device scalability evaluation (500 devices) that neither of those papers directly reports, and validates across heterogeneous hardware tiers (Raspberry Pi through Jetson) rather than a single device class.

## Strengths

Evaluates accuracy, latency, energy, and scalability together rather than any single metric in isolation; genuinely heterogeneous hardware validation; open-access, full-text-verifiable Springer publication; scalability claim (500 devices, accuracy holding above 88%) is a distinctive contribution relative to this Observatory's existing Industrial_IoT key papers.

## Weaknesses

Single-author paper; laboratory conditions rather than a live industrial deployment; the specific fault types and IoT application domain evaluated are not fully detailed in this abstract-level record.

## Limitations

Laboratory validation, however realistic, is not the same as long-term deployment in an actual industrial environment with the extreme conditions (heat, vibration, dust) this Observatory's [[Industrial_IoT]] concept centers on; accuracy degradation from 92% to above-88% as device count scales to 500 suggests some accuracy/scalability trade-off worth quantifying further.

## Open questions

How does the accuracy/scalability trade-off (92% at presumably lower device counts, above 88% at 500 devices) behave beyond 500 devices — is there a scalability ceiling? How does this RNN/autoencoder architecture compare directly, on the same task, to the unsupervised on-device training approach of [[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] or the hierarchical routing of [[2024_delaFuente_ESN-PdM]]?

## Possible extensions

A direct, controlled comparison of this RNN/autoencoder edge-fault-detection architecture against [[2023_Antonini_TinyMLAnomalyDetectionIndustrial]]'s unsupervised on-device training approach and [[2024_delaFuente_ESN-PdM]]'s hierarchical routing architecture, on the same industrial fault-detection task and device fleet, to determine which scales and performs best under matched conditions.

## Relevance to our research

Adds a scalability dimension (up to 500 devices) to this Observatory's [[Industrial_IoT]] concept that its existing key papers do not directly address, complementing the on-device-training focus of [[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] and the hierarchical-tier focus of [[2024_delaFuente_ESN-PdM]].

## Possible thesis topics

Extending the reported 500-device scalability evaluation to identify where (if anywhere) detection accuracy or latency breaks down as device count grows further, and comparing this architecture head-to-head against the Observatory's existing on-device-training and hierarchical-routing industrial-IoT approaches.

## Possible collaborations

Groups working on scalable edge AI architectures for industrial IoT fault detection and smart infrastructure monitoring.

## Links to related papers

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]], [[2024_delaFuente_ESN-PdM]]
