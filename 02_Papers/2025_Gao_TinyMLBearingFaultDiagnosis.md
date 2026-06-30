# An edge-deployable TinyML approach enhanced by transfer learning for efficient bearing fault diagnosis

**Full citation:** Gao, Z., Jiang, Z., Dong, Z., et al. (2025). An edge-deployable TinyML approach enhanced by transfer learning for efficient bearing fault diagnosis. Science China Technological Sciences, 68, Article 2220401. https://doi.org/10.1007/s11431-025-3072-9

*(Note: the full author list beyond the first three names could not be independently confirmed from publicly available sources at time of writing; cited here as "et al." accordingly.)*

**Linked concepts:** [[Predictive_Maintenance]], [[On-device_Learning]]

## Abstract summary

The authors present a TinyML approach for bearing fault diagnosis that uses transfer learning to adapt a model under limited labeled training data, deploying the resulting classifier on an ESP32-S3 microcontroller and reporting 88.28% fault-classification accuracy across four fault types, with inference completing in 45 ms at 17.7 mJ of energy per decision.

## Research problem

Industrial bearing fault diagnosis via machine learning typically assumes abundant labeled fault data and capable compute hardware; real deployments face both scarce labeled fault examples (faults are rare events) and the tight memory/energy budget of low-cost microcontroller-class edge hardware, making the standard ML pipeline impractical without adaptation.

## Key idea

Use transfer learning to adapt a fault-diagnosis model with limited target-domain labeled data, then optimize and deploy the resulting compact model directly on an ESP32-S3 microcontroller, jointly addressing the data-scarcity and resource-constraint problems rather than solving each independently.

## Technical contribution

A transfer-learning-enhanced TinyML pipeline specifically tailored to bearing fault diagnosis; an end-to-end deployment on ESP32-S3 hardware with measured accuracy, latency, and per-decision energy figures.

## Experimental methodology

Evaluation on a proprietary bearing dataset covering four distinct fault types, measuring classification accuracy, per-inference latency, and per-decision energy consumption on the deployed ESP32-S3 hardware.

## Results

The deployed system achieves 88.28% fault-classification accuracy with 45 ms inference latency and 17.7 mJ energy per decision, demonstrating that transfer-learning-adapted models can deliver practical bearing-fault diagnosis directly on low-cost microcontroller hardware.

## Comparison with the state of the art

Extends the hierarchical edge-gateway-cloud predictive-maintenance direction (ESN-PdM) with a fully on-sensor-tier deployment specifically addressing the data-scarcity problem via transfer learning, rather than assuming abundant labeled fault data is already available at the edge tier.

## Strengths

Addresses both core practical obstacles (data scarcity and resource constraints) in a single pipeline rather than treating them separately; reports concrete, hardware-measured latency and energy figures rather than only offline accuracy.

## Weaknesses

Evaluated on a proprietary dataset, limiting independent reproducibility and direct comparison against other published bearing-fault-diagnosis methods on common ground.

## Limitations

Restricted to four specific bearing fault types and to the ESP32-S3 platform; generalization to other industrial asset classes or fault modes is not directly demonstrated.

## Open questions

How does this transfer-learning-based approach compare in accuracy and resource cost to the unsupervised on-device training approach used for industrial acoustic anomaly detection (Tiny-MLOps)? Would adopting a public, shared bearing-fault benchmark (rather than a proprietary dataset) change the comparative picture against other TinyML fault-diagnosis methods?

## Possible extensions

Replicating the approach on a public bearing-fault dataset to enable direct comparison with other published methods; combining transfer learning with the hierarchical edge-gateway-cloud routing architecture (ESN-PdM) to handle cases where the edge-tier model's confidence is low.

## Relevance to our research

Adds a second concrete, hardware-validated 2023-2026 data point to the Predictive Maintenance entry, specifically addressing the data-scarcity dimension that the existing hierarchical-routing paper (ESN-PdM) does not focus on.

## Possible thesis topics

Comparative study of transfer-learning-based versus unsupervised on-device training approaches for industrial fault/anomaly detection under the same microcontroller resource budget; combining this transfer-learning pipeline with hierarchical edge-gateway-cloud routing for low-confidence cases.

## Possible collaborations

Groups maintaining public bearing-fault and industrial-vibration datasets that could supply a shared benchmark for reproducible comparison.

## Links to related papers

[[2024_delaFuente_ESN-PdM]], [[2023_Antonini_TinyMLAnomalyDetectionIndustrial]]
