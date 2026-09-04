# Federated Learning

Federated learning trains one shared model across many devices that each keep their own data local, exchanging only model updates (not raw data) with a coordinating server. For EdgeAI, this matters for two reasons at once: it preserves privacy (sensitive sensor data never leaves the device), and it distributes the cost of training across many constrained devices instead of requiring one central server to hold all the data.

## Evolution of the concept

Yang, Liu, Chen, and Tong's "Federated Machine Learning: Concept and Applications" (ACM TIST, 2019) is the field's most-cited paper and defines its modern conceptual vocabulary: a taxonomy of *horizontal* federated learning (clients share the same features but different data samples — the common case, and the one all other papers in this concept address), *vertical* federated learning (clients share the same data samples but different features), and *federated transfer learning* (neither samples nor features fully overlap).

McMahan et al. (2017) introduce Federated Averaging (FedAvg), the field's foundational algorithm: each device runs a few steps of local training and sends only its weight update — not its data — to a server that averages the updates across devices. This drastically cuts the communication traffic needed to train on decentralized, non-identically-distributed data, and remains the starting point for privacy-preserving distributed training on resource-constrained devices. Könecný et al. (2016) anticipate the bandwidth concern this raises: they propose structured and "sketched" updates (low-rank or randomly-masked restrictions, plus quantization, random rotation, and subsampling) to cut the uplink communication cost of FedAvg-style training.

Wang et al. (IEEE JSAC, 2019) derive a theoretical convergence bound as a function of how often devices synchronize ("aggregation frequency") under a fixed resource budget, together with an adaptive control algorithm that uses the bound to decide the right frequency automatically. Freitag et al. (2022) provide a real-hardware instance of that same trade-off: implementing the full training loop directly on microcontrollers for a keyword-spotting task, and characterizing — through physical-device experiments rather than simulation — how more frequent federated rounds with less local data per round reduce loss faster but cost more bandwidth and time.

Imteaj et al. (IEEE Internet of Things Journal, 2021/2022) provide the field's most-cited survey specifically on federated learning for resource-constrained IoT devices, organizing the literature around the compounding constraints these devices face together: communication, computation, storage, and heterogeneity across the fleet. Pfeiffer et al. (2023) take stock of the techniques developed since then to adapt federated learning to computationally-constrained, heterogeneous clients — compression, partial or sub-model training, and scheduling — organized by which resource constraint each technique addresses, and note that handling multiple constraints simultaneously (compute, memory, and communication together) across a genuinely heterogeneous device fleet remains comparatively underexplored.

Jain et al. (2026) push federated learning toward genuinely TinyML-scale hardware — microcontrollers with 256 KB of RAM or less — by combining FedAvg with resource-aware dual-mode execution (a device switches between training and inference depending on its current resource budget), quantized and semantically-filtered updates, and last-layer personalization, within a hierarchical architecture aligned with upcoming 6G network designs. This shows federated learning becoming viable on extreme-edge devices, not just smartphones.

## Key papers

[[2019_Yang_FederatedMachineLearningConceptApplications]] — founds the field's modern conceptual vocabulary (the horizontal/vertical/federated-transfer-learning taxonomy); the single most-cited federated learning paper.

[[2019_Wang_AdaptiveFederatedLearningEdgeComputing]] — derives a convergence bound as a function of aggregation frequency under a fixed resource budget, and an adaptive control algorithm using it; the theoretical foundation for the resource/convergence trade-off Freitag et al. characterize empirically below.

[[2021_Imteaj_FederatedLearningResourceConstrainedIoTSurvey]] — the most-cited survey specifically on federated learning for resource-constrained IoT devices, organizing the literature around compounding communication/computation/storage/heterogeneity constraints.

[[2017_McMahan_FederatedAveraging]] — the FedAvg algorithm, the first practical solution for training on decentralized, heterogeneous data.

[[2016_Konecny_FederatedLearningCommunicationEfficiency]] — proposes structured and sketched updates to cut the uplink communication cost of FedAvg-style training, directly anticipating the bandwidth concerns TinyFed6G's update compression (below) addresses.

[[2023_Pfeiffer_FederatedLearningConstrainedDevicesSurvey]] — survey and taxonomy of federated learning techniques for computationally-constrained, heterogeneous devices, organized by which resource constraint (compute, memory, communication) each technique targets.

[[2026_Jain_TinyFed6G]] — hierarchical federated-learning framework for MCU-class TinyML clients, combining device-profile-driven model assignment, dual-mode train/infer execution, and semantic compression of quantized updates; reports large communication and energy savings over prior methods in simulation.

## Open problems

Robust convergence under extreme heterogeneity across clients — in data, compute capability, and availability. Integrating formal privacy guarantees (differential privacy, secure aggregation) without losing too much accuracy. Validating simulated energy/latency claims, as in TinyFed6G, on physical microcontroller hardware rather than in simulation.

## Research ideas

Federated learning with quantized or compressed updates for bandwidth- and battery-constrained edge devices. A study of how hardware heterogeneity — not just data heterogeneity — affects convergence. Physical-hardware validation of simulated federated-learning-on-microcontroller frameworks.

## Possible thesis topics

Federated learning with compressed updates for IoT sensors and microcontrollers. Evaluation of FedAvg in scenarios with devices that disconnect frequently, typical of low-power IoT networks. A hardware testbed implementation of a dual-mode (train/infer) federated-learning framework on Cortex-M boards, to validate simulated energy and latency gains against real measurements.

## Links

[[On-device_Learning]], [[Quantization]]
