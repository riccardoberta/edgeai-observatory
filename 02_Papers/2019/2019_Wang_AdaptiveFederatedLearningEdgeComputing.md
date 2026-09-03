# Adaptive Federated Learning in Resource Constrained Edge Computing Systems

**Full citation:** Wang, S., Tuor, T., Salonidis, T., Leung, K.K., Makaya, C., He, T., Chan, K. (2019). Adaptive Federated Learning in Resource Constrained Edge Computing Systems. IEEE Journal on Selected Areas in Communications, 37(6), 1205-1221. DOI: 10.1109/JSAC.2019.2904348.

**PDF:** [arXiv](https://arxiv.org/abs/1804.05271) — [Code](https://github.com/IBM/adaptive-federated-learning)

**Verification note:** Bibliographic details confirmed via WebSearch (IBM Research, IEEE Xplore listing, GitHub). Abstract-level verified.

**Linked concepts:** [[Federated_Learning]]

## Abstract summary

Derives a convergence bound for gradient-descent-based federated learning under a fixed resource budget, and uses it to design a control algorithm that adaptively decides the optimal frequency of global model aggregation given available communication and computation resources.

## Research problem

Federated learning at the edge must balance the frequency of global aggregation (more frequent = better convergence but more communication cost) against a fixed resource budget, but no principled way existed to set this trade-off given real, limited edge resources.

## Key idea

Derive a theoretical convergence bound as a function of aggregation frequency and use it to compute, in real time, the aggregation frequency that minimizes loss under a fixed resource (communication + computation) budget.

## Technical contribution

A convergence-bound-driven adaptive aggregation-frequency control algorithm for federated learning under resource constraints, validated with both theoretical analysis and real-testbed experiments.

## Experimental methodology

Evaluated via a hardware testbed and simulations under varying resource budgets, comparing the adaptive-frequency algorithm against fixed-frequency baselines for convergence speed and resource usage.

## Results

The adaptive algorithm consistently outperforms fixed-frequency baselines for a given resource budget, and the paper's convergence bound accurately predicts the empirically optimal aggregation frequency.

## Comparison with the state of the art

Provides the theoretical convergence-bound foundation that later resource-aware federated learning surveys, including this KB's [[2021_Imteaj_FederatedLearningResourceConstrainedIoTSurvey]], build on; complements this KB's real-hardware [[2022_Freitag_OnDeviceTrainingMCUFederated]] finding (more frequent rounds with less local data reduce loss faster but cost more bandwidth/time) with a principled way to set that trade-off rather than only characterizing it empirically.

## Strengths

Rigorous theoretical grounding backed by real testbed validation; extremely high impact (2800+ citations); directly actionable for anyone deploying federated learning under a real resource budget.

## Weaknesses

Testbed validation predates genuinely microcontroller-class devices; the convergence bound assumes gradient-descent-based FL specifically, not all federated learning variants.

## Limitations

Assumes resource budget and network conditions are known or estimable in advance; does not address non-IID data distribution as a primary focus.

## Open questions

Does the adaptive-aggregation-frequency approach extend cleanly to genuinely MCU-class devices where computation, not just communication, is the binding constraint — the setting this KB's [[2022_Freitag_OnDeviceTrainingMCUFederated]] empirically explores?

## Possible extensions

Extending the adaptive-frequency control algorithm to jointly optimize for computation-bound MCU-class devices, not only communication-bound edge devices as originally validated.

## Relevance to our research

Provides the theoretical foundation underlying the resource/convergence trade-off this KB's own [[2022_Freitag_OnDeviceTrainingMCUFederated]] characterizes empirically on real MCU hardware — a striking gap given how directly these two papers connect.

## Possible thesis topics

Validating whether this paper's convergence-bound-derived optimal aggregation frequency matches what [[2022_Freitag_OnDeviceTrainingMCUFederated]] found empirically on real microcontroller hardware.

## Possible collaborations

Groups working on federated learning theory and resource-aware distributed optimization (IBM Research, Penn State).

## Links to related papers

[[2019_Yang_FederatedMachineLearningConceptApplications]], [[2021_Imteaj_FederatedLearningResourceConstrainedIoTSurvey]], [[2022_Freitag_OnDeviceTrainingMCUFederated]]
