# On-Device Training of Machine Learning Models on Microcontrollers with Federated Learning

**Full citation:** Freitag, F. (2022). On-Device Training of Machine Learning Models on Microcontrollers with Federated Learning. Electronics, 11(4), 573. DOI: 10.3390/electronics11040573

**PDF:** [MDPI (open access)](https://www.mdpi.com/2079-9292/11/4/573)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[On-device_Learning]], [[Federated_Learning]]

## Abstract summary

Explores training a machine learning model directly on a microcontroller (rather than only performing inference there) and extending this on-device training process with federated learning, implemented for a keyword-spotting task. Real-device experiments characterize learning behavior and resource consumption under different hyperparameter and federated-learning-round configurations, finding that training locally with less data and more frequent federated rounds reduces training loss faster but at the cost of higher bandwidth usage and longer training time.

## Research problem

Machine learning model training for microcontroller-class devices has traditionally happened entirely offline on powerful computers, with only inference deployed to the device; whether training itself — and specifically federated training across a fleet of microcontrollers — is practical given MCU compute/memory/bandwidth constraints had not been characterized with real hardware experiments.

## Key idea

Implement the full training loop directly on microcontroller hardware for a keyword-spotting task, and extend it with federated learning (local training plus periodic aggregation across devices), then empirically characterize the resulting trade-off between federated-round frequency, local data quantity, training-loss reduction speed, bandwidth usage, and training time.

## Technical contribution

A real-hardware (not simulated) implementation and empirical characterization of on-device training combined with federated learning specifically at the microcontroller tier, for a concrete application (keyword spotting), quantifying the resource/convergence trade-offs of different federated configurations.

## Experimental methodology

Experiments on real microcontroller devices implementing on-device training extended with federated learning for keyword spotting, varying hyperparameters and federated-learning-round frequency/configuration, measuring training-loss reduction, bandwidth usage, and training time.

## Results

More frequent federated learning rounds with less local data reduced training loss more quickly, but at the cost of higher bandwidth usage and longer overall training time; the results indicate the appropriate trade-off point depends on the specific application's requirements and resource constraints rather than a single universally optimal configuration.

## Comparison with the state of the art

Complements algorithm-focused federated-learning-for-constrained-devices work such as [[2023_Pfeiffer_FederatedLearningConstrainedDevicesSurvey]] and [[2026_Jain_TinyFed6G]] with real, physical-microcontroller-hardware measurements of the federated-training resource trade-off, rather than simulation — directly addressing an open problem already flagged in this Observatory's [[Federated_Learning]] concept about validating simulated FL-on-MCU claims on physical hardware.

## Strengths

Real hardware experiments (not NS-3/Python simulation), directly relevant to the physical-hardware-validation gap this Observatory's [[Federated_Learning]] concept already flags; concrete, reproducible application (keyword spotting) rather than a purely synthetic benchmark; fully open-access.

## Weaknesses

Single application (keyword spotting) and a specific microcontroller platform; the reported trade-offs may not generalize directly to other tasks or MCU tiers with different memory/compute/radio characteristics.

## Limitations

Does not address more advanced memory-efficient on-device training techniques (sparse update, quantization-aware scaling) alongside federated learning; the bandwidth/time trade-off characterization is empirical rather than accompanied by a general theoretical model.

## Open questions

How do the reported bandwidth/convergence trade-offs change when combined with update compression techniques such as those in [[2016_Konecny_FederatedLearningCommunicationEfficiency]] or [[2026_Jain_TinyFed6G]]'s semantic compression? Do the same trade-off patterns hold for other TinyML tasks beyond keyword spotting (HAR, biosignals)?

## Possible extensions

Combining this paper's real-hardware federated-training characterization with update-compression techniques from [[2016_Konecny_FederatedLearningCommunicationEfficiency]] to see whether the bandwidth cost of frequent rounds can be reduced without losing the faster convergence.

## Relevance to our research

Directly answers a physical-hardware-validation gap already named in this Observatory's [[Federated_Learning]] concept (validating simulated energy/latency claims on real MCU hardware) and provides a concrete, measured resource/convergence trade-off for [[On-device_Learning]] combined with federated aggregation.

## Possible thesis topics

Extending this real-hardware federated-training-on-MCU characterization to a non-keyword-spotting TinyML task, and combining it with update-compression techniques to reduce the reported bandwidth cost of frequent federated rounds.

## Possible collaborations

Groups working on federated learning for resource-constrained IoT/TinyML devices and real-hardware TinyML benchmarking.

## Links to related papers

[[2023_Pfeiffer_FederatedLearningConstrainedDevicesSurvey]], [[2026_Jain_TinyFed6G]]
