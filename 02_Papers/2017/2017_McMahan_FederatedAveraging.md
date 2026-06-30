# Communication-Efficient Learning of Deep Networks from Decentralized Data

**Full citation:** McMahan, B., Moore, E., Ramage, D., Hampson, S., Agüera y Arcas, B. (2017). Communication-Efficient Learning of Deep Networks from Decentralized Data. *Proceedings of the 20th International Conference on Artificial Intelligence and Statistics (AISTATS)*, PMLR 54, pp. 1273–1282. arXiv:1602.05629. https://arxiv.org/abs/1602.05629

**Linked concepts:** [[Federated Learning]]

## Abstract summary

The authors (Google) introduce Federated Averaging (FedAvg), an algorithm for training a shared model on data distributed across many devices (e.g. smartphones) without the data ever leaving the device, aggregating only locally computed weight updates.

## Research problem

Much useful training data (e.g. typed text, user behavior) resides on users' devices and cannot or should not be centralized for privacy, bandwidth, or cost reasons; a way is needed to train models on this data without centralizing it.

## Key idea

Each device runs a few steps of local gradient descent on its own data, then sends only the weight update (not the data) to a central server that aggregates the updates, weighted by the amount of local data, drastically reducing communication traffic compared to sending a gradient for every single step.

## Technical contribution

Formulation of the FedAvg algorithm; empirical analysis of its convergence as a function of the number of local steps per communication round and the non-IID-ness of data across devices.

## Experimental methodology

Experiments on reference datasets (e.g. MNIST, CIFAR, a next-word-prediction dataset) artificially partitioned across many simulated clients, in both IID and non-IID scenarios, measuring the number of communication rounds needed to reach a given accuracy.

## Results

FedAvg reduces the number of communication rounds needed by one or two orders of magnitude compared to the baseline (a single local step per round), even with non-IID data across clients, though with greater variability.

## Comparison with the state of the art

Compared to classic synchronous distributed training (which assumes centralized, balanced data), FedAvg is the first practical algorithm explicitly designed for decentralized, unbalanced, and non-IID data across a large number of devices.

## Strengths

Implementation simplicity, validation on realistic data heterogeneity scenarios, immediate industry adoption (e.g. mobile predictive keyboards) shortly after publication.

## Weaknesses

Convergence analysis is mainly empirical, not a strong theoretical guarantee for all non-IID regimes; it does not explicitly address privacy attacks (e.g. gradient inversion), only the absence of raw-data centralization.

## Limitations

Assumes devices are available and connected to participate in rounds; it does not discuss in depth the energy/compute costs on the device side, which are relevant in the EdgeAI context with very limited resources.

## Open questions

How to guarantee robust convergence under extreme heterogeneity across clients (data, compute capability, availability)? How to integrate formal privacy guarantees (differential privacy, secure aggregation) without losing too much accuracy?

## Possible extensions

Personalized federated learning (local models that specialize); combination with communication compression (quantizing the updates) for clients with very limited bandwidth, relevant to edge devices.

## Relevance to our research

Foundational paper for any work on privacy-preserving distributed training on resource-constrained edge devices; a starting point for exploring federated learning on microcontrollers or IoT sensors.

## Possible thesis topics

Federated learning with quantized/compressed updates for bandwidth- and battery-constrained devices; study of the effect of hardware heterogeneity (not just data heterogeneity) on FedAvg convergence.

## Possible collaborations

Groups working on privacy-preserving ML and on efficient communication for IoT.

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]] (for compressing the updates)
