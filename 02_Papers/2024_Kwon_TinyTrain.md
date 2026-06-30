# TinyTrain: Resource-Aware Task-Adaptive Sparse Training of DNNs at the Data-Scarce Edge

**Full citation:** Kwon, Y.D., Li, R., Venieris, S.I., Chauhan, J., Lane, N.D., Mascolo, C. (2024). TinyTrain: Resource-Aware Task-Adaptive Sparse Training of DNNs at the Data-Scarce Edge. Proceedings of ICML 2024. https://arxiv.org/abs/2307.09988

**Linked concepts:** [[On-device_Learning]]

## Abstract summary

The authors (Samsung AI Center Cambridge, University of Cambridge) propose TinyTrain, an on-device training method that reduces both the computational/memory cost of fine-tuning and the amount of labeled task-specific data needed, by combining a task-adaptive sparse-update mechanism with a pre-training/meta-learning phase designed to make subsequent on-device adaptation more data-efficient.

## Research problem

On-device training/fine-tuning of neural networks on resource-constrained edge devices is doubly constrained: by limited compute/memory for backpropagation, and by limited labeled data available at the edge for the target task, but most prior on-device learning work (e.g. TinyTL) addresses only the compute/memory dimension and assumes sufficient labeled data is available.

## Key idea

Jointly address both constraints by (1) selecting, at fine-tuning time, a task- and memory-aware sparse subset of layers/channels to update (rather than updating the whole network or a fixed subset chosen offline), and (2) using a meta-learning-style pre-training phase that makes the resulting model more amenable to fast, data-efficient adaptation once deployed.

## Technical contribution

A dynamic, task-adaptive sparse-update selection algorithm that accounts for both the importance of each layer/channel to the current task and the memory budget available on-device; integration of this selection mechanism with a meta-learning pre-training procedure for improved few-shot on-device adaptation.

## Experimental methodology

Evaluation on multiple vision and sensor-based benchmark datasets under few-shot / data-scarce settings, deployed on real microcontroller-class and mobile edge hardware, measuring task accuracy, memory footprint, and energy/latency of the on-device fine-tuning process, compared against TinyTL and full fine-tuning baselines.

## Results

TinyTrain achieves higher accuracy than prior on-device learning baselines under data-scarce conditions while reducing the memory footprint and energy cost of on-device training, with measured improvements on real edge hardware rather than only simulated estimates.

## Comparison with the state of the art

Extends the on-device learning line started by TinyTL by additionally tackling the data-scarcity dimension through task-adaptive sparse selection plus meta-learning-style pre-training, rather than assuming abundant labeled on-device data as TinyTL implicitly does.

## Strengths

Addresses both compute/memory and data-scarcity constraints jointly, which is closer to realistic edge deployment conditions; validated on real hardware, not only simulation; published at a top-tier ML venue (ICML).

## Weaknesses

The meta-learning pre-training phase adds complexity and requires access to representative pre-training data/tasks before deployment, which may not always be available for novel edge use cases.

## Limitations

Evaluated on a set of benchmark vision/sensor tasks; generalization to highly novel, out-of-distribution edge tasks not represented in the meta-learning pre-training phase is not deeply explored.

## Open questions

How does task-adaptive sparse-update selection interact with continual learning across a sequence of on-device adaptation episodes (catastrophic forgetting risk)? Can the meta-learning pre-training phase itself be made cheaper for resource-constrained model providers?

## Possible extensions

Combining TinyTrain-style task-adaptive sparse updates with closed-form/analytic continual learning updates (e.g. TS-ACL) to support a sequence of on-device adaptations without forgetting.

## Relevance to our research

Directly extends the [[On-device_Learning]] research line beyond TinyTL by tackling the realistic combination of compute, memory, and data scarcity, relevant to our Applications taxonomy's sensor-based on-device personalization use cases (HAR, biosignals).

## Possible thesis topics

Evaluating TinyTrain-style task-adaptive sparse on-device fine-tuning for a specific HAR or biosignal personalization task, measuring the accuracy/memory/energy trade-off against full fine-tuning and against TinyTL.

## Possible collaborations

Groups working on meta-learning for few-shot adaptation and on on-device training systems for mobile/embedded hardware.

## Links to related papers

[[2020_Cai_TinyTL]], [[2024_Li_TSACL]]
