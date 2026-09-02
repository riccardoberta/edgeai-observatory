# Predictive Maintenance

## Evolution of the concept

A foundational shared benchmark for the field is Saxena and Goebel's NASA "PHM08 Challenge Data Set" (2008, NASA Prognostics Center of Excellence), a simulated turbofan-engine degradation dataset (via the C-MAPSS tool) used to train and evaluate remaining-useful-life prediction algorithms — one of the first standardized, public datasets that let prognostics-and-health-management methods be compared on common ground rather than on private, non-reproducible industrial data. Predictive maintenance for industrial and mobile machinery has moved from fixed, single-tier inference deployments (always-on-device or always-cloud) toward hierarchical architectures that dynamically route inference across edge, gateway, and cloud tiers depending on accuracy, latency, and battery-life trade-offs. TinyML model optimization makes the on-device and on-gateway tiers viable in the first place, and empirical studies on real harsh-environment machinery (e.g. mining equipment) have begun quantifying the concrete accuracy-versus-power trade-off across this hierarchy, rather than only arguing qualitatively for edge inference. This connects directly to the [[Compression]] and [[On-device_Learning]] research directions, since narrowing the accuracy gap between edge-tier and cloud-tier inference is largely a model-compression and on-device-training problem. A complementary 2025 study (Gao et al.) tackles the data-scarcity side of the same problem for bearing fault diagnosis specifically: using transfer learning to adapt a model under limited labeled fault data and deploying it on an ESP32-S3 microcontroller, reaching 88.28% accuracy at 45 ms latency and 17.7 mJ per decision — a concrete demonstration that the on-sensor tier can handle both the resource-constraint and data-scarcity problems jointly. Two earlier Elsevier papers establish the two main strategies later work like Gao et al.'s draws on for getting a fault-diagnosis model onto constrained edge hardware in the first place. Asutkar et al. (2022, *Expert Systems with Applications*) address domain generalization directly: a lightweight 1D-CNN transfer-learning framework for machine fault diagnosis that fine-tunes convolutional layers while transferring dense layers, plus a memory-efficient bias-only retraining mode, validated on Raspberry Pi and ESP32, letting a model trained on one machine adapt cheaply to a related one without a full retrain. Ma et al. (2023, *Engineering Applications of Artificial Intelligence*) instead attack the architecture side: a multi-objective neural architecture search over a variable-layer search space that optimizes jointly for real-time inference speed, edge-deployment feasibility, and diagnostic accuracy under compound faults and strong noise, rather than searching for accuracy first and compressing afterward. Together these two papers frame a still-open design choice for on-sensor predictive maintenance: adapt a fixed lightweight architecture across domains (Asutkar et al.) versus search for a new deployment-aware architecture per task (Ma et al.), a choice whose relative cost/benefit has not yet been benchmarked head-to-head on the same fault-diagnosis task.

## Key papers

[[2008_Saxena_PHM08ChallengeDataSet]] — simulated turbofan-engine degradation dataset (C-MAPSS) and challenge that standardized remaining-useful-life benchmarking for prognostics and health management.

[[2024_delaFuente_ESN-PdM]] — Edge Sensor Network for Predictive Maintenance (ESN-PdM), a TinyML-enabled hierarchical edge-gateway-cloud inference framework for mining mobile machinery, with quantified accuracy/latency/power trade-offs across tiers.

[[2025_Gao_TinyMLBearingFaultDiagnosis]] — transfer-learning-enhanced TinyML pipeline for bearing fault diagnosis deployed on ESP32-S3, jointly addressing data scarcity and resource constraints.

[[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]] — lightweight 1D-CNN transfer-learning framework for domain generalization in machine fault diagnosis, with a memory-efficient bias-only retraining mode validated on Raspberry Pi and ESP32.

[[2023_Ma_LightweightFaultDiagnosisNAS]] — multi-objective neural architecture search for real-time mechanical fault diagnosis, jointly optimizing accuracy, inference speed, and edge-deployment feasibility under compound faults and strong noise.

## Open problems

How does the hierarchical inference architecture's dynamic routing logic generalize to industrial domains with different failure-criticality profiles, where the accuracy gap between edge and cloud tiers may be unacceptable? Can the on-device tier's accuracy gap versus the cloud tier be narrowed using more advanced on-device training/compression techniques rather than a simpler optimized model? Which strategy is more cost-effective for adapting a fault-diagnosis model to a new machine or fault type: transfer-learning-based domain adaptation of a fixed architecture (Asutkar et al.) or re-running multi-objective architecture search per deployment (Ma et al.)? No head-to-head comparison of the two on the same task and hardware exists yet.

## Research ideas

Applying advanced on-device training and compression techniques to the on-sensor tier of a hierarchical predictive maintenance system to attempt closing the accuracy gap with the cloud tier without sacrificing reported power savings.

## Possible thesis topics

Closing the accuracy gap between on-sensor and cloud inference tiers in a hierarchical predictive maintenance system using advanced on-device training/compression; porting a hierarchical-routing predictive maintenance architecture to a non-mining industrial domain and re-measuring the accuracy/latency/power trade-off.

## Links

[[Industrial_IoT]], [[On-device_Learning]], [[Compression]], [[Quantization]], [[NAS]]
