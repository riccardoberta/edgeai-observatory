# LOPdM: A Low-Power On-Device Predictive Maintenance System Based on Self-Powered Sensing and TinyML

**Full citation:** Chen, Z., Gao, Y., Liang, J. (2023). LOPdM: A Low-Power On-Device Predictive Maintenance System Based on Self-Powered Sensing and TinyML. IEEE Transactions on Instrumentation and Measurement, 72, Article 3508211.

**PDF:** [IEEE Xplore](https://ieeexplore.ieee.org/document/10229236/)

**Linked concepts:** [[Predictive_Maintenance]]

## Abstract summary

A predictive maintenance system combining self-powered sensors (harvesting energy from the monitored machine's own vibration) with TinyML inference (random forest and DNN models) directly on the sensor node, using ultra-short, low-sampling-rate data to reach up to 99% precision.

## Research problem

Battery-powered wireless sensor nodes for predictive maintenance require periodic maintenance/replacement themselves, and typical deep-learning pipelines assume more data and power budget than a truly maintenance-free sensor node can provide.

## Key idea

Pair a self-powered sensor (no battery, harvesting energy from machine vibration) with a TinyML inference pipeline specifically designed for ultra-short data length, small sample count, and low sampling rate.

## Technical contribution

A full self-powered-sensing-plus-TinyML system architecture (star-topology BLE network of inference nodes) demonstrating that predictive maintenance inference can run entirely on harvested energy.

## Experimental methodology

Random forest and DNN models trained and deployed on the self-powered sensor nodes, evaluated for precision under ultra-short/low-sampling-rate data constraints against standard fault-detection baselines.

## Results

Up to 99% precision despite the extreme data constraints imposed by self-powered operation.

## Comparison with the state of the art

Pushes the resource-constraint envelope further than this concept's other on-device anchors (Gao et al.'s ESP32-S3 transfer learning, Asutkar et al.'s Raspberry Pi/ESP32 work) by removing the battery entirely, a genuinely maintenance-free deployment model.

## Strengths

Novel self-powered-sensing angle rarely combined with TinyML in this literature; demonstrates a genuinely battery-free predictive maintenance node; strong reported precision despite extreme constraints.

## Weaknesses

Single application domain validated; star-topology BLE network scalability not stress-tested at the scale of, e.g., [[2025_LujanMora_EdgeAIFaultDetectionIoT]]'s 500-device study.

## Limitations

Energy-harvesting availability is machine/vibration-profile dependent, limiting applicability to machines with insufficient ambient vibration.

## Open questions

How does LOPdM's battery-free approach combine with this concept's hierarchical edge/gateway/cloud routing architecture — could a self-powered tier reduce the routing framework's own power budget further?

## Possible extensions

Combining self-powered sensing with the hierarchical inference routing architecture this concept already tracks, to build a fully maintenance-free multi-tier predictive maintenance system.

## Relevance to our research

Extends this concept's resource-constraint frontier to genuinely battery-free operation, a deployment model none of the concept's other anchors address.

## Possible thesis topics

Integrating self-powered sensing with hierarchical edge-gateway-cloud predictive maintenance routing, characterizing the combined system's energy budget.

## Possible collaborations

Groups working on energy harvesting and self-powered sensing for industrial IoT (ShanghaiTech).

## Links to related papers

[[2025_Gao_TinyMLBearingFaultDiagnosis]], [[2025_LujanMora_EdgeAIFaultDetectionIoT]]
