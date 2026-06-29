# Federated Learning

## Evolution of the concept

McMahan et al. (2017) introduce Federated Averaging (FedAvg): each device runs a few steps of local training and sends only the weight update (not the data) to a server that aggregates it, drastically reducing the communication traffic needed to train a model on decentralized, non-IID data. It is the starting point for any privacy-preserving distributed training on resource-constrained devices. Jain et al. (2026) push this toward genuinely TinyML-scale hardware (≤256 KB RAM MCUs) by combining FedAvg with resource-aware dual-mode execution (train vs. infer), quantized/semantically-filtered updates, and last-layer personalization, within a 6G-aligned hierarchical architecture — showing FL is becoming viable on extreme-edge devices, not just smartphones.

## Key papers

[[2017_McMahan_FederatedAveraging]] — the FedAvg algorithm, the first practical solution for training on decentralized, heterogeneous data.

[[2026_Jain_TinyFed6G]] — hierarchical FL framework for MCU-class TinyML clients, combining device-profile-driven model assignment, dual-mode train/infer execution, and semantic compression of quantized updates; reports large communication and energy savings over FedAvg/FedPer/FedRep in simulation.

## Open problems

Robust convergence under extreme heterogeneity across clients (data, compute capability, availability). Integrating formal privacy guarantees (differential privacy, secure aggregation) without losing too much accuracy. Validating simulated energy/latency claims (as in TinyFed6G) on physical MCU hardware rather than NS-3/Python simulation.

## Research ideas

Federated learning with quantized/compressed updates for bandwidth- and battery-constrained edge devices; study of the effect of hardware heterogeneity (not just data heterogeneity) on convergence; physical-hardware validation of simulated FL-on-MCU frameworks.

## Possible thesis topics

Federated learning with compressed updates for IoT sensors/microcontrollers; evaluation of FedAvg in scenarios with devices that disconnect frequently (typical of low-power IoT networks); hardware testbed implementation of a dual-mode (train/infer) FL framework on Cortex-M boards to validate simulated energy and latency gains.

## Links

[[On-device Learning]], [[Quantization]]
