# A Survey on Federated Learning for Resource-Constrained IoT Devices

**Full citation:** Imteaj, A., Thakker, U., Wang, S., Li, J., Amini, M.H. (2022). A Survey on Federated Learning for Resource-Constrained IoT Devices. IEEE Internet of Things Journal, 9(1), 1-24. DOI: 10.1109/JIOT.2021.3095077. (Early access 2021; filed here under 2021 by initial publication.)

**PDF:** [Author copy](https://shiqiang.wang/papers/AI_IOTJ2021.pdf)

**Verification note:** Bibliographic details confirmed via WebSearch (IEEE Xplore, FIU institutional repository). Abstract-level verified.

**Linked concepts:** [[Federated_Learning]]

## Abstract summary

A comprehensive survey specifically on federated learning for resource-constrained IoT devices, systematically categorizing the challenges (communication, computation, storage, heterogeneity, statistical non-IID data) and surveying proposed solutions for each.

## Research problem

Federated learning research had grown rapidly, but resource-constrained IoT devices face compounding challenges (limited communication, computation, storage, plus device and data heterogeneity) that generic federated learning surveys do not systematically address together.

## Key idea

Organize the federated-learning-for-constrained-IoT literature around the specific compounding resource constraints these devices face, rather than treating federated learning generically.

## Technical contribution

A structured problem/solution taxonomy specifically for resource-constrained IoT federated learning, covering communication-efficiency techniques, computation-reduction techniques, and heterogeneity-handling approaches together.

## Experimental methodology

Literature survey and synthesis, not a novel empirical study.

## Results

Became the most-cited survey (1000+ citations) specifically scoped to resource-constrained IoT federated learning, widely used as the field's entry point.

## Comparison with the state of the art

Directly extends the general federated learning framework of [[2019_Yang_FederatedMachineLearningConceptApplications]] and the resource/convergence theory of [[2019_Wang_AdaptiveFederatedLearningEdgeComputing]] into a constrained-IoT-specific problem taxonomy, and is the natural survey-level anchor for this KB's real-hardware [[2022_Freitag_OnDeviceTrainingMCUFederated]] finding.

## Strengths

Extremely high citation count for its specific scope; systematically organizes a fragmented literature around the compounding constraints (not just one at a time) that TinyML-class devices actually face.

## Weaknesses

As a survey, offers no new empirical validation; published 2021-2022, so predates the most recent (2024-2026) TinyML federated learning work.

## Limitations

Survey currency is bounded by publication date; does not include quantitative benchmarking of the surveyed techniques against each other.

## Open questions

Which of the surveyed communication-efficiency and heterogeneity-handling techniques have actually been validated on genuine microcontroller-class hardware, versus only simulated?

## Possible extensions

An updated version of this survey's taxonomy specifically filtering for techniques validated on real MCU-class hardware (like this KB's [[2022_Freitag_OnDeviceTrainingMCUFederated]]) rather than simulation-only results.

## Relevance to our research

The primary, most-cited survey-level anchor for exactly the intersection ([[Federated_Learning]] + resource-constrained devices) this KB's own concept is built around — a clear gap this audit closes.

## Possible thesis topics

Auditing this survey's cited techniques for which have real-hardware (not simulation-only) validation, and identifying which resource-constraint category (communication, computation, storage, heterogeneity) remains least validated on genuine TinyML hardware.

## Possible collaborations

Groups working on federated learning for constrained IoT/edge devices (Florida International University).

## Links to related papers

[[2019_Yang_FederatedMachineLearningConceptApplications]], [[2019_Wang_AdaptiveFederatedLearningEdgeComputing]], [[2022_Freitag_OnDeviceTrainingMCUFederated]]
