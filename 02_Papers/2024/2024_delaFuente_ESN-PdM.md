# Enhancing Predictive Maintenance in Mining Mobile Machinery through a TinyML-enabled Hierarchical Inference Network

**Full citation:** de la Fuente, R., Radrigan, L., Morales, A. S. (2024). Enhancing Predictive Maintenance in Mining Mobile Machinery through a TinyML-enabled Hierarchical Inference Network. arXiv:2411.07168. https://arxiv.org/abs/2411.07168 (submitted to IEEE)

**Linked concepts:** [[Predictive_Maintenance]], [[Compression]], [[Industrial_IoT]]

## Abstract summary

The authors introduce ESN-PdM (Edge Sensor Network for Predictive Maintenance), a hierarchical inference framework spanning edge devices, gateways, and cloud services for real-time condition monitoring of mining mobile machinery, which dynamically chooses the inference location (on-device, on-gateway, or on-cloud) based on trade-offs among accuracy, latency, and battery life, using TinyML techniques for model optimization on resource-constrained devices.

## Research problem

Mining machinery operates in highly variable, harsh environments with unpredictable mechanical stress, making predictive maintenance both especially valuable (failures are costly and disruptive) and especially challenging; a single fixed inference location (always-on-device, or always-cloud) forces a poor compromise between accuracy, latency, and the battery life of the sensing nodes attached to the machinery.

## Key idea

Build a hierarchical inference architecture that does not commit to one fixed deployment location, but instead dynamically routes each inference decision to on-device, on-gateway, or on-cloud execution depending on the current trade-off needs (accuracy required, latency tolerance, remaining battery), using TinyML model optimization to make the on-device and on-gateway tiers viable in the first place.

## Technical contribution

ESN-PdM: a three-tier (edge-gateway-cloud) hierarchical inference system architecture for predictive maintenance, combined with TinyML-optimized models at the edge/gateway tiers, plus an empirical characterization of the accuracy/latency/power trade-offs across all three inference tiers for a real mining-machinery condition-monitoring task.

## Experimental methodology

Deployed and evaluated on real mining mobile machinery condition-monitoring data, comparing classification accuracy, latency, and power consumption across the three inference tiers (on-sensor, on-gateway, on-cloud), measuring operational battery life under the on-sensor inference mode.

## Results

On-sensor and on-gateway inference modes achieved over 90% classification accuracy, while cloud-based inference reached 99%; on-sensor inference reduced power consumption by approximately 44%, extending operation to up to 104 hours, demonstrating a concrete, quantified accuracy-versus-power trade-off across the hierarchy rather than a purely qualitative argument for edge inference.

## Comparison with the state of the art

Most predictive maintenance systems commit to a single fixed inference location; ESN-PdM's contribution is the dynamic, trade-off-aware hierarchical routing itself, which is a more general architectural pattern than typical fixed-edge-inference TinyML predictive maintenance papers (such as bearing fault diagnosis on a single microcontroller), and could in principle generalize beyond mining to other industrial predictive maintenance settings.

## Strengths

Validated on a real, harsh-environment industrial use case (mining mobile machinery) rather than a lab benchmark; provides quantified, multi-tier accuracy/latency/power trade-off data rather than a single deployment point; the dynamic routing architecture is reusable across other predictive maintenance domains.

## Weaknesses

The 9-percentage-point accuracy gap between edge/gateway tiers (over 90%) and cloud tier (99%) means the system trades meaningful accuracy for power savings, a trade-off whose acceptability is highly application-dependent and not deeply explored across other failure-criticality scenarios; the dynamic routing decision logic itself (how it decides for the moment to favor accuracy vs. battery life) is not detailed as thoroughly as the resulting empirical trade-off numbers.

## Limitations

Validated specifically on mining mobile machinery; generalization to other industrial predictive maintenance domains (e.g. manufacturing line equipment, building HVAC) with different failure modes and sensor modalities is not directly demonstrated.

## Open questions

How does the hierarchical inference architecture's dynamic routing logic generalize to industrial domains with different failure criticality profiles, where the 90%-vs-99% accuracy trade-off may be unacceptable? Can the on-device tier's accuracy gap versus the cloud tier be narrowed using more advanced on-device training/compression techniques (e.g. sparse update, quantization-aware scaling) rather than a simpler optimized model?

## Possible extensions

Applying more advanced on-device training and compression techniques (as in [[2022_Lin_OnDeviceTraining256KB]]) to the on-sensor tier of ESN-PdM to attempt closing the accuracy gap with the cloud tier without sacrificing the reported power savings; extending the hierarchical-routing architecture to a different industrial predictive maintenance domain.

## Relevance to our research

Foundational reference for the [[Predictive_Maintenance]] branch of our Applications taxonomy, and a concrete example of accuracy-latency-power trade-off engineering directly relevant to this Observatory's broader interest in [[Compression]] and [[On-device_Learning]].

## Possible thesis topics

Closing the accuracy gap between on-sensor and cloud inference tiers in a hierarchical predictive maintenance system using advanced on-device training/compression; porting the ESN-PdM hierarchical-routing architecture to a non-mining industrial predictive maintenance domain and re-measuring the accuracy/latency/power trade-off.

## Possible collaborations

Mining and heavy-machinery operators; groups working on hierarchical edge-gateway-cloud inference architectures for industrial IoT.

## Links to related papers

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] (industrial anomaly detection counterpart in the same TinyML/edge space), [[2022_Lin_OnDeviceTraining256KB]] (on-device training/compression techniques relevant to narrowing the edge-tier accuracy gap)
