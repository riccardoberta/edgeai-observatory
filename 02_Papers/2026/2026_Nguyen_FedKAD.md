# FedKAD: Federated Low-Rank Koopman Learning for Multivariate Time-Series Anomaly Detection in IoT Systems

**Full citation:** Nguyen, T.-A., Bui, V.-P., Le, A. T., Ta, K. H., Le, M. T., Zhang, J. A., Huang, X. (2026). Federated Low-Rank Koopman Learning for Multivariate Time-Series Anomaly Detection in IoT Systems. arXiv:2607.08978 [cs.LG, eess.SP]. Submitted 9 Jul 2026. License CC BY 4.0. DOI: 10.48550/arXiv.2607.08978.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2607.08978)

**Linked concepts:** [[Federated Learning]], [[Industrial IoT]], [[Predictive Maintenance]]

## Abstract summary

Distributed IoT systems generate multivariate time-series streams for monitoring physical assets, servers, and embedded sensing platforms; detecting abnormal temporal behavior is critical for fault diagnosis, predictive maintenance, and security, but is hindered by decentralized non-IID data, limited bandwidth, and constrained edge compute/memory. FedKAD is a resource-efficient federated Koopman anomaly detection framework that learns normal temporal dynamics via lightweight sliding-window Koopman representations rather than large neural models. Federated training is cast as a low-rank consensus problem under orthonormality (Stiefel-manifold) constraints, solved via a federated Stiefel-ADMM algorithm with convergence guarantees under partial client participation. On four multivariate time-series anomaly-detection benchmarks, FedKAD matches or improves detection performance versus federated deep-learning baselines while providing up to 2.1×10³ faster training, 80× lower communication, and 79× lower inference latency.

## Research problem

Practical IoT anomaly detection needs to run on decentralized, non-IID sensor streams under tight bandwidth and constrained edge compute/memory — but deep-learning-based federated anomaly detectors require training and communicating large neural models, which is exactly what these constraints make expensive. The paper asks whether a much lighter-weight dynamical-systems representation (Koopman operator theory) can match deep-learning detection quality while being dramatically cheaper to train and communicate.

## Key idea

Replace the heavy neural sequence model with a linear-dynamics surrogate: learn each client's normal temporal behavior via lightweight sliding-window Koopman representations, and formulate federated training as a low-rank consensus problem where raw sensor streams and each client's local reduced dynamics stay on-device — only compact subspace variables are exchanged with the server. Optimizing the shared representation under Stiefel-manifold (orthonormality) constraints requires a purpose-built federated Stiefel-ADMM algorithm rather than standard federated averaging. At inference, each client detects anomalies locally from the residual between observed future trajectories and the learned Koopman dynamics — no server round-trip needed for detection itself.

## Technical contribution

A federated anomaly-detection framework that communicates only compact subspace variables rather than full model gradients/weights; a federated Stiefel-ADMM algorithm with convergence and stationarity analysis under partial client participation (not just the idealized full-participation case); a formal treatment of the accuracy/efficiency trade-off for a linear-dynamics surrogate versus deep-learning anomaly detectors in a genuinely federated, resource-constrained setting.

## Experimental methodology

Evaluated on four widely used multivariate time-series anomaly-detection benchmarks against federated deep-learning baselines. Metrics: detection performance (matched/improved vs. baselines), plus training time, communication volume, and inference latency, all reported as multiplicative improvements over the neural baselines.

## Results

FedKAD matches or improves detection performance relative to federated deep-learning baselines across the four benchmarks, while providing up to 2.1×10³ (~2,100×) faster training, 80× lower communication, and 79× lower inference latency than the neural baselines — efficiency deltas large enough to plausibly make on-device federated deployment practical rather than aspirational.

## Comparison with the state of the art

The individual ingredients — Koopman operator learning, federated ADMM, and Stiefel-manifold optimization — are each independently known techniques; the paper's contribution is combining them into a communication- and compute-frugal federated anomaly detector with a formal convergence result under partial client participation, which the 2026-07-13 weekly digest characterized as "a clean counterpoint to the deep-learning default" the Observatory otherwise tracks for [[Industrial IoT]] anomaly detection. It also complements the 2026-07-05 digest's embedded-anomaly-detection survey, which explicitly flagged weak on-device concept-drift handling and poor cross-platform portability as open gaps in the field — gaps FedKAD does not claim to close.

## Strengths

A well-motivated departure from the field's deep-learning default, directly addressing the bandwidth and compute constraints that make neural federated anomaly detection impractical at the edge; a genuine theoretical contribution (convergence and stationarity guarantees under partial participation), not just an empirical trick; efficiency deltas (orders of magnitude in training time and communication) large enough to change what's deployable, not just incrementally better.

## Weaknesses

The abstract does not specify what "edge device" concretely means in the experiments (true MCU-class hardware vs. edge-CPU/gateway-class), which matters enormously for whether the claimed efficiency numbers translate to this Observatory's typical hardware targets — this is exactly the caveat the 2026-07-13 digest flagged and held the paper below a 5/5 relevance score for; no discussion at the abstract level of how FedKAD handles concept drift, despite that being explicitly identified as an open gap for this application area by the prior week's survey.

## Limitations

As a linear-dynamics (Koopman) surrogate, FedKAD's detection quality is fundamentally bounded by how well linearizable dynamics approximate the true (possibly strongly nonlinear) sensor behavior — the paper reports it "matches or improves" versus neural baselines on four benchmarks, but does not claim to dominate them, suggesting there may be regimes (highly nonlinear anomaly signatures) where the neural approach still wins.

## Open questions

What concretely is "edge device" in the experimental setup — MCU, edge-CPU, or gateway-class hardware? Does FedKAD's detection quality hold up under real concept drift (sensor aging, seasonal/operational regime changes), which is exactly the gap the prior week's embedded-anomaly-detection survey flagged as unresolved across the field?

## Possible extensions

Validate FedKAD-style Koopman anomaly detection on real MCU/edge hardware (Cortex-M/RISC-V) against quantized neural baselines, and test its behavior specifically under concept drift (the explicit 2026-07-13 digest hook); characterize the boundary between linear-dynamics-approximable and genuinely nonlinear anomaly signatures to understand when FedKAD's efficiency advantage does or doesn't come at an accuracy cost.

## Relevance to our research

A strong fit for the Observatory's [[Federated Learning]], [[Industrial IoT]], and [[Predictive Maintenance]] branches — the leading candidate the 2026-07-13 digest flagged for the intersection of all three. Directly extends [[Predictive Maintenance]] work with a communication-frugal alternative to the deep-learning anomaly-detection default.

## Possible thesis topics

On-device federated anomaly detection with linear-dynamics surrogates: validate FedKAD-style Koopman anomaly detection on real MCU/edge hardware against quantized neural baselines, and test its behavior under concept drift — directly addressing the gap flagged in the 2026-07-05 digest's embedded-anomaly-detection survey (Master's/PhD, per the 2026-07-13 digest's explicit hook).

## Possible collaborations

No specific group flagged in prior digests, but the paper's combination of Koopman operator theory and federated optimization suggests dynamical-systems-adjacent or federated-optimization-theory groups as natural collaborators for the theoretical side, alongside embedded-systems groups for the on-device validation extension above.

## Links to related papers

Complements (without yet a `02_Papers/` record for) the 2026-07-05 weekly digest's "Real-Time Machine Learning for Embedded Anomaly Detection" survey (arXiv:2512.19383), which flagged weak on-device concept-drift handling and cross-platform portability as open gaps FedKAD's efficiency gains do not by themselves resolve.
