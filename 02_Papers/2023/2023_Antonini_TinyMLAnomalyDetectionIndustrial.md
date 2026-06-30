# An Adaptable and Unsupervised TinyML Anomaly Detection System for Extreme Industrial Environments

**Full citation:** Antonini, M., Pincheira, M., Vecchio, M., Antonelli, F. (2023). An Adaptable and Unsupervised TinyML Anomaly Detection System for Extreme Industrial Environments. *Sensors*, 23(4), 2344. DOI: 10.3390/s23042344

**Linked concepts:** [[Industrial_IoT]], [[Compression]]

## Abstract summary

The authors propose an end-to-end, adaptable and configurable anomaly detection system for extreme industrial environments (such as submersible pumps), using IoT, edge computing, and Tiny-MLOps methodologies. The system runs entirely on an ESP32-based IoT sensing kit with MicroPython firmware, collects sensor data, trains an unsupervised isolation-forest anomaly detection model on-device, and alerts an external gateway when an anomaly is detected.

## Research problem

Industrial assets operating in extreme environments (high vibration, heat, limited connectivity, restricted physical access) cannot rely on continuous cloud connectivity for anomaly detection, and most existing ML-based industrial monitoring approaches assume labeled failure data and reliable communication links that are often unavailable in these extreme settings.

## Key idea

Move the entire anomaly-detection pipeline — data collection, model training, and inference — onto the constrained edge device itself using an unsupervised algorithm (isolation forest) that does not require labeled failure examples, so the system can adapt to a specific asset's normal operating signature without needing curated failure data or a persistent connection to the cloud.

## Technical contribution

A complete Tiny-MLOps pipeline (not just an inference-only deployment) that performs unsupervised model training directly on an ESP32 microcontroller, demonstrating that even the training phase of an anomaly detection model can be pushed to extremely resource-constrained edge hardware, with measured training times of 1.2-6.4 seconds and anomaly detection latency under 16 milliseconds.

## Experimental methodology

Deployed and evaluated on an IoT sensing kit based on an ESP32 microcontroller running MicroPython, applied to a real extreme-industrial-environment use case (submersible pumps), measuring on-device training time, inference latency, and anomaly detection effectiveness using the isolation forest algorithm.

## Results

The system trains an unsupervised anomaly detection model entirely on-device in 1.2 to 6.4 seconds and detects anomalies in under 16 milliseconds, demonstrating that both training and inference for industrial anomaly detection can run within the resource envelope of a low-cost microcontroller, without cloud dependency.

## Comparison with the state of the art

Most prior industrial anomaly detection systems perform training in the cloud or on a gateway and only push inference to the edge; this work is distinctive in pushing the unsupervised training step itself onto the constrained device, directly relevant to the broader [[On-device_Learning]] research direction in this Observatory.

## Strengths

Fully unsupervised approach removes the dependency on labeled failure data, which is often unavailable for industrial assets; demonstrates genuinely on-device training (not just inference) on extremely low-cost, widely available hardware (ESP32); validated on a realistic extreme-environment industrial use case.

## Weaknesses

Isolation forest is a relatively simple, classical ML algorithm rather than a deep learning model, so the paper's techniques may not directly transfer to more complex anomaly patterns that benefit from deep feature learning; evaluated on a single asset type (submersible pumps), so generalization to other industrial equipment is not directly demonstrated.

## Limitations

Unsupervised anomaly detection without labeled failures can struggle to distinguish genuinely novel failure modes from benign distribution shift in normal operating conditions; the system's adaptability is demonstrated for one extreme-environment scenario and would need validation across a wider range of industrial settings.

## Open questions

How does this on-device unsupervised training approach compare, in detection accuracy, to deep-learning-based anomaly detection methods deployed via inference-only edge pipelines? Can the Tiny-MLOps on-device training methodology be combined with the [[On-device_Learning]] techniques (e.g. sparse update, quantization-aware scaling) developed for more general embedded training?

## Possible extensions

Combining this unsupervised on-device training approach with sparse-update or quantization-aware on-device training techniques (as in [[2022_Lin_OnDeviceTraining256KB]]) to extend it from classical ML (isolation forest) to lightweight deep anomaly-detection models trainable on the same hardware class.

## Relevance to our research

Foundational reference for the [[Industrial_IoT]] branch of our Applications taxonomy, and a concrete bridge to [[On-device_Learning]], since it demonstrates genuine on-device training (not just inference) for a real industrial use case on extremely low-cost hardware.

## Possible thesis topics

Extending the on-device unsupervised training approach from isolation forest to a lightweight deep anomaly-detection model trainable within the same ESP32-class resource envelope; comparative study of on-device-trained versus cloud-trained anomaly detection for the same industrial asset class.

## Possible collaborations

Industrial IoT vendors and integrators; groups working on Tiny-MLOps and on-device training methodologies.

## Links to related papers

[[2024_delaFuente_ESN-PdM]] (predictive maintenance counterpart in the same TinyML/edge-hierarchy space), [[2022_Lin_OnDeviceTraining256KB]] (on-device training techniques that could extend this work beyond classical ML)
