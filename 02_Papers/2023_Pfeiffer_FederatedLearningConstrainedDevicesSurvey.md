# Federated Learning for Computationally-Constrained Heterogeneous Devices: A Survey

**Full citation:** Pfeiffer, K., Rapp, M., Khalili, R., Henkel, J. (2023). Federated Learning for Computationally-Constrained Heterogeneous Devices: A Survey. ACM Computing Surveys, 55(14s), Article 334. https://doi.org/10.1145/3596907

**Linked concepts:** [[Federated_Learning]]

## Abstract summary

The authors (Bosch, Karlsruhe Institute of Technology) survey federated learning approaches specifically designed for computationally-constrained and heterogeneous client devices, organizing the literature around techniques that allow resource-limited edge devices to participate meaningfully in federated training despite hardware heterogeneity and tight compute/memory/communication budgets.

## Research problem

Most foundational federated learning work assumes clients capable of training a full copy of the global model; in practice, federated deployments increasingly involve highly heterogeneous, resource-constrained devices (from smartphones down to IoT/embedded devices) that cannot all afford the same training cost, and a systematic understanding of techniques addressing this heterogeneity was lacking.

## Key idea

Organize and compare the growing body of techniques that adapt federated learning to constrained, heterogeneous clients — including model compression for federated rounds, partial/sub-model training, client selection and scheduling strategies, and communication-efficient aggregation — within a structured taxonomy tied to the specific resource constraint each technique targets.

## Technical contribution

A structured taxonomy of resource-constrained federated learning techniques, organized by which constraint (compute, memory, communication, energy) each technique primarily addresses; identification of gaps in the literature regarding combined/heterogeneous constraints.

## Experimental methodology

As a survey, the paper systematically reviews and categorizes existing federated learning methods for constrained devices, comparing their assumptions, targeted constraints, and reported trade-offs, rather than running new experiments.

## Results

The survey documents that while individual constraint dimensions (compute, communication) are relatively well addressed by dedicated techniques, jointly handling multiple simultaneous constraints under realistic device heterogeneity (some clients much weaker than others in the same federation) remains comparatively underexplored as of 2023.

## Comparison with the state of the art

Complements general federated learning surveys (which tend to focus on privacy, communication efficiency, or convergence theory broadly) by specifically centering the survey on the EdgeAI-relevant dimension of device-level resource constraints and heterogeneity.

## Strengths

EdgeAI-relevant framing directly applicable to federated learning across heterogeneous IoT/embedded fleets; structured taxonomy useful as a reference map of the sub-field; published in a high-impact, peer-reviewed venue (ACM Computing Surveys).

## Weaknesses

As a survey, does not propose or validate a new method; the pace of federated learning research means some specific technique comparisons may already be dated relative to 2024-2025 developments.

## Limitations

Focuses on the systems/resource-constraint angle of federated learning rather than deeply covering the privacy/security angle (differential privacy, secure aggregation), which is treated elsewhere in the broader federated learning literature.

## Open questions

How should federated learning systems handle simultaneous heterogeneity in compute, memory, AND communication budget across the same client fleet, rather than addressing each dimension in isolation? How do resource-constrained federated techniques interact with on-device continual/incremental learning?

## Possible extensions

A focused empirical study combining the taxonomy's compute-constraint and communication-constraint technique families on a real heterogeneous fleet of microcontroller-class and mobile-class devices for a shared EdgeAI task.

## Relevance to our research

A useful structured reference for navigating the [[Federated_Learning]] sub-field specifically from the device-resource-constraint angle relevant to our Hardware taxonomy's heterogeneous targets (Cortex-M, Cortex-A, NPU).

## Possible thesis topics

Designing and evaluating a federated learning scheme across a genuinely heterogeneous device fleet (e.g. mixing Cortex-M and Cortex-A class devices) for a shared sensor-classification task, using this survey's taxonomy to select complementary compute- and communication-efficient techniques.

## Possible collaborations

Groups working on federated learning systems and on heterogeneous-hardware edge deployment.

## Links to related papers

[[2016_Konecny_FederatedLearningCommunicationEfficiency]]
