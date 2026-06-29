# Predictive Maintenance

## Evolution of the concept

Predictive maintenance for industrial and mobile machinery has moved from fixed, single-tier inference deployments (always-on-device or always-cloud) toward hierarchical architectures that dynamically route inference across edge, gateway, and cloud tiers depending on accuracy, latency, and battery-life trade-offs. TinyML model optimization makes the on-device and on-gateway tiers viable in the first place, and empirical studies on real harsh-environment machinery (e.g. mining equipment) have begun quantifying the concrete accuracy-versus-power trade-off across this hierarchy, rather than only arguing qualitatively for edge inference. This connects directly to the [[Compression]] and [[On-device_Learning]] research directions, since narrowing the accuracy gap between edge-tier and cloud-tier inference is largely a model-compression and on-device-training problem.

## Key papers

[[2024_delaFuente_ESN-PdM]] — Edge Sensor Network for Predictive Maintenance (ESN-PdM), a TinyML-enabled hierarchical edge-gateway-cloud inference framework for mining mobile machinery, with quantified accuracy/latency/power trade-offs across tiers.

## Open problems

How does the hierarchical inference architecture's dynamic routing logic generalize to industrial domains with different failure-criticality profiles, where the accuracy gap between edge and cloud tiers may be unacceptable? Can the on-device tier's accuracy gap versus the cloud tier be narrowed using more advanced on-device training/compression techniques rather than a simpler optimized model?

## Research ideas

Applying advanced on-device training and compression techniques to the on-sensor tier of a hierarchical predictive maintenance system to attempt closing the accuracy gap with the cloud tier without sacrificing reported power savings.

## Possible thesis topics

Closing the accuracy gap between on-sensor and cloud inference tiers in a hierarchical predictive maintenance system using advanced on-device training/compression; porting a hierarchical-routing predictive maintenance architecture to a non-mining industrial domain and re-measuring the accuracy/latency/power trade-off.

## Links

[[Industrial_IoT]], [[On-device_Learning]], [[Compression]], [[Quantization]]
