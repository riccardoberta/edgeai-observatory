# Predictive Maintenance

## Evolution of the concept

A foundational shared benchmark for the field is Saxena and Goebel's NASA "PHM08 Challenge Data Set" (2008, NASA Prognostics Center of Excellence), a simulated turbofan-engine degradation dataset (via the C-MAPSS tool) used to train and evaluate remaining-useful-life prediction algorithms — one of the first standardized, public datasets that let prognostics-and-health-management methods be compared on common ground rather than on private, non-reproducible industrial data. Predictive maintenance for industrial and mobile machinery has moved from fixed, single-tier inference deployments (always-on-device or always-cloud) toward hierarchical architectures that dynamically route inference across edge, gateway, and cloud tiers depending on accuracy, latency, and battery-life trade-offs. TinyML model optimization makes the on-device and on-gateway tiers viable in the first place, and empirical studies on real harsh-environment machinery (e.g. mining equipment) have begun quantifying the concrete accuracy-versus-power trade-off across this hierarchy, rather than only arguing qualitatively for edge inference. This connects directly to the [[Compression]] and [[On-device_Learning]] research directions, since narrowing the accuracy gap between edge-tier and cloud-tier inference is largely a model-compression and on-device-training problem. A complementary 2025 study (Gao et al.) tackles the data-scarcity side of the same problem for bearing fault diagnosis specifically: using transfer learning to adapt a model under limited labeled fault data and deploying it on an ESP32-S3 microcontroller, reaching 88.28% accuracy at 45 ms latency and 17.7 mJ per decision — a concrete demonstration that the on-sensor tier can handle both the resource-constraint and data-scarcity problems jointly.

## Key papers

[[2008_Saxena_PHM08ChallengeDataSet]] — simulated turbofan-engine degradation dataset (C-MAPSS) and challenge that standardized remaining-useful-life benchmarking for prognostics and health management.

[[2024_delaFuente_ESN-PdM]] — Edge Sensor Network for Predictive Maintenance (ESN-PdM), a TinyML-enabled hierarchical edge-gateway-cloud inference framework for mining mobile machinery, with quantified accuracy/latency/power trade-offs across tiers.

[[2025_Gao_TinyMLBearingFaultDiagnosis]] — transfer-learning-enhanced TinyML pipeline for bearing fault diagnosis deployed on ESP32-S3, jointly addressing data scarcity and resource constraints.

## Open problems

How does the hierarchical inference architecture's dynamic routing logic generalize to industrial domains with different failure-criticality profiles, where the accuracy gap between edge and cloud tiers may be unacceptable? Can the on-device tier's accuracy gap versus the cloud tier be narrowed using more advanced on-device training/compression techniques rather than a simpler optimized model?

## Research ideas

Applying advanced on-device training and compression techniques to the on-sensor tier of a hierarchical predictive maintenance system to attempt closing the accuracy gap with the cloud tier without sacrificing reported power savings.

## Possible thesis topics

Closing the accuracy gap between on-sensor and cloud inference tiers in a hierarchical predictive maintenance system using advanced on-device training/compression; porting a hierarchical-routing predictive maintenance architecture to a non-mining industrial domain and re-measuring the accuracy/latency/power trade-off.

## Links

[[Industrial_IoT]], [[On-device_Learning]], [[Compression]], [[Quantization]]
