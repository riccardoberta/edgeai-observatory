# Optimized Edge-Cloud System for Activity Monitoring Using Knowledge Distillation

**Full citation:** Barranco, F. (2024). Optimized Edge-Cloud System for Activity Monitoring Using Knowledge Distillation. Electronics, 13(23), 4786. DOI: 10.3390/electronics13234786

**PDF:** [MDPI (open access)](https://www.mdpi.com/2079-9292/13/23/4786)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[Distillation]], [[Human_Activity_Recognition]]

## Abstract summary

Proposes an edge-cloud system for indoor activity monitoring in long-term care facilities, where video-based action recognition runs via deep learning at edge nodes. Complex networks are first distilled to fit resource-limited edge hardware, improving recognition performance by up to 8% without added resource cost. A central Quality and Resource Management (QRM) tool monitors hardware/recognition quality, load-balances across edge nodes, and dynamically reconfigures which distilled network variant runs, particularly around critical events such as falls. The paper also releases a manually curated Indoor Action Dataset.

## Research problem

Ambient Assisted Living video-based activity monitoring needs accurate action recognition running locally at resource-limited edge nodes (for power efficiency, bandwidth reduction, and resident privacy), but complex, accurate deep networks generally exceed what such edge hardware can run, and static model deployment cannot adapt to changing resource availability or the criticality of specific events (e.g. a fall).

## Key idea

Distill complex activity-recognition networks into more efficient variants deployable at the edge, and pair this with a central resource-management layer that dynamically reconfigures which distilled model variant runs on each edge node based on real-time hardware load and recognition-quality requirements, treating distillation and runtime orchestration as a joint system rather than a one-off offline compression step.

## Technical contribution

An edge-cloud activity-monitoring architecture combining knowledge distillation for on-edge deployability with a runtime Quality and Resource Management tool that load-balances and reconfigures which network variant executes per node; a released, manually curated Indoor Action Dataset for ambient-assisted-living research.

## Experimental methodology

Deployment and evaluation of distilled activity-recognition networks on resource-limited edge nodes for indoor video-based action recognition, measured for recognition performance gain and resource usage, plus system-level evaluation of the QRM tool's load-balancing and dynamic reconfiguration behavior including for critical fall-detection scenarios.

## Results

Knowledge distillation improved recognition performance by up to 8% without increasing resource usage on the edge nodes; the QRM tool's runtime reconfiguration and load balancing maintained real-time operation and optimized energy consumption while prioritizing recognition quality for critical situations like falls.

## Comparison with the state of the art

Distinguishes itself from static, offline-distilled edge deployment by making the distillation/deployment choice itself dynamic and resource-aware at runtime, and extends the ambient-assisted-living literature with a released dataset (Indoor Action Dataset) rather than relying solely on existing benchmarks.

## Strengths

Combines algorithmic compression (distillation) with system-level orchestration (QRM) rather than treating them separately; targets a genuinely resource- and privacy-sensitive real-world deployment (long-term care facilities); releases a new dataset as an additional contribution; fully open-access.

## Weaknesses

Single-domain validation (indoor activity monitoring for care facilities); the 8% recognition improvement and resource-neutrality claims are specific to the evaluated network/dataset combination and may not generalize to other distillation targets or edge hardware tiers.

## Limitations

Video-based sensing raises different privacy/resource trade-offs than the wearable-sensor-based HAR line of work (accelerometer/gyroscope) covered elsewhere in this Observatory; the QRM tool's runtime reconfiguration logic has not been tested against adversarial or highly dynamic multi-tenant edge-node conditions.

## Open questions

How does the QRM tool's dynamic reconfiguration strategy generalize to non-video HAR settings (wearable IMU-based recognition, as in [[2024_Moreira_HighPerformanceHAR]] or [[2016_Ordonez_DeepConvLSTM]])? Would combining distillation with quantization further improve the resource/accuracy trade-off for this deployment scenario?

## Possible extensions

Applying the joint distillation-plus-runtime-orchestration architecture to wearable-sensor-based HAR rather than video, to test whether the same resource/quality gains generalize across sensing modalities.

## Relevance to our research

A system-level demonstration for [[Distillation]] and [[Human_Activity_Recognition]] that distillation gains are not purely a static, offline compression story — pairing distillation with dynamic runtime resource management can extract additional recognition-quality headroom under a fixed resource budget, directly relevant to the Applications branch's [[Human_Activity_Recognition]] concept and its own open question about deployment-realistic benchmarking.

## Possible thesis topics

Porting the QRM-style dynamic distilled-model reconfiguration architecture to wearable IMU-based HAR (bridging [[Distillation]] and [[Human_Activity_Recognition]]); combining distillation and quantization within the same edge-cloud activity-monitoring system to further reduce resource usage.

## Possible collaborations

Ambient assisted living / healthcare-monitoring research groups working on edge-cloud video analytics for care facilities.

## Links to related papers

[[2024_Moreira_HighPerformanceHAR]]
