# Federated Learning: Strategies for Improving Communication Efficiency

**Full citation:** Konečný, J., McMahan, H.B., Yu, F.X., Richtárik, P., Suresh, A.T., Bacon, D. (2016). Federated Learning: Strategies for Improving Communication Efficiency. *NeurIPS 2016 Workshop on Private Multi-Party Machine Learning*. https://research.google/pubs/federated-learning-strategies-for-improving-communication-efficiency/

**Linked concepts:** [[Federated_Learning]]

## Abstract summary

The authors propose two families of techniques — structured updates (restricting client updates to a low-rank or random-mask subspace) and sketched updates (compressing a full update via quantization, random rotation, and subsampling before sending it) — to drastically reduce the uplink communication cost of federated learning, the direction in which bandwidth is most constrained.

## Research problem

Federated learning (training a shared model across many distributed devices without centralizing their data) is bottlenecked by the cost of repeatedly sending model updates from devices to the server, particularly over the slow, often metered uplink connections typical of mobile and edge devices; naively sending full-precision updates every round does not scale.

## Key idea

A client's update does not need to be communicated at full fidelity to be useful: restricting the update itself to a compact structured form (low-rank or sparse), or compressing an unrestricted update through quantization, random rotation (to make quantization error more uniform), and random subsampling, can cut communication volume by large factors while still allowing the aggregated model to converge.

## Technical contribution

A systematic comparison of structured-update and sketched-update strategies for client-to-server communication compression in the FedAvg setting; an analysis of the trade-off between compression aggressiveness and convergence/accuracy, and of how the two families of techniques can be combined.

## Experimental methodology

Simulated federated training across the families of compression strategies, measuring achieved model accuracy as a function of the per-round communication budget, compared against uncompressed FedAvg updates as the baseline.

## Results

Both structured and sketched update strategies achieve substantial reductions in uplink communication (reported in the original work as on the order of two orders of magnitude in some settings) while reaching comparable final accuracy to uncompressed federated averaging, demonstrating that aggressive communication compression is compatible with federated convergence.

## Comparison with the state of the art

One of the earliest systematic treatments of communication efficiency specifically for the federated setting, as opposed to general gradient compression for distributed/data-center training, anticipating the bandwidth concerns that motivate later communication-efficient federated learning systems for cellular and other constrained edge networks.

## Strengths

Directly targets the practical bottleneck (uplink bandwidth) that most limits federated learning's deployability on real mobile/edge networks; the two technique families are complementary and can be tuned independently of model architecture.

## Weaknesses

Compression introduces additional hyperparameters (sketch size, subsampling rate, rotation choice) that must be tuned per task/model, and aggressive compression can slow convergence in wall-clock rounds even if it saves bandwidth per round.

## Limitations

Evaluated in simulation on benchmark federated learning tasks of the era rather than on real heterogeneous mobile/edge hardware with realistic, variable network conditions; does not address downlink (server-to-client) communication cost, on-device compute constraints, or non-IID data heterogeneity in depth.

## Open questions

How do these compression strategies interact with the system-level and network-condition constraints of real-world deployments (e.g. cellular networks, as later studied by frameworks like TinyFed6G)? Can compression be made adaptive to per-client bandwidth and battery conditions rather than fixed?

## Possible extensions

Adaptive, per-client compression rates based on observed network/battery conditions; combining update compression with on-device model compression (quantization/pruning) for a fully resource-aware federated pipeline.

## Relevance to our research

The foundational reference for communication-efficient federated learning, directly anticipating the bandwidth concerns that motivate later cellular/edge-targeted federated systems; essential background whenever the Observatory discusses federated learning's deployability on constrained networks.

## Possible thesis topics

Benchmarking structured versus sketched update compression on a real federated learning testbed of resource-constrained edge devices over realistic (e.g. simulated cellular) network conditions, measuring the true wall-clock convergence trade-off rather than only per-round communication volume.

## Possible collaborations

Groups working on communication-efficient distributed optimization and on federated learning systems for cellular/IoT network conditions.

## Links to related papers

[[2017_Kirkpatrick_OvercomingCatastrophicForgetting]]
