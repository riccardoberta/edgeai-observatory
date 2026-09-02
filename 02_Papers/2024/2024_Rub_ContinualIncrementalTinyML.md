# A Continual and Incremental Learning Approach for TinyML On-device Training Using Dataset Distillation and Model Size Adaption

**Full citation:** Rüb, M., Tuchel, P., Sikora, A., Mueller-Gritschneder, D. (2024). A Continual and Incremental Learning Approach for TinyML On-device Training Using Dataset Distillation and Model Size Adaption. 2024 IEEE 7th International Conference on Industrial Cyber-Physical Systems (ICPS). DOI: 10.1109/ICPS59941.2024.10639989

**PDF:** [IEEE Xplore](https://ieeexplore.ieee.org/document/10639989/) · [arXiv preprint](https://arxiv.org/abs/2409.07114)

**Verification note:** Bibliographic details confirmed via WebSearch (dblp, TUM research portal, IEEE Xplore listing). Abstract-level verified; full IEEE-formatted text not fetched directly.

**Linked concepts:** [[Continual_Learning]], [[On-device_Learning]]

## Abstract summary

Proposes an incremental-learning algorithm for TinyML devices that addresses catastrophic forgetting through dataset distillation — compressing prior task data into a small, synthetic distilled dataset that is retained and replayed alongside new data — combined with a model-size adaptation mechanism that grows the network as new classes/tasks are added, targeting low-performance, energy-constrained embedded devices (voice recognition, anomaly detection, predictive maintenance, sensor processing).

## Research problem

TinyML devices deployed for classification tasks (voice, sensor anomaly, predictive maintenance) often need to learn new classes/tasks over their operational lifetime, but standard incremental learning either requires storing growing amounts of raw historical data (infeasible on MCU-class memory) or suffers catastrophic forgetting when fine-tuned only on new data.

## Key idea

Distill prior-task data into a compact synthetic dataset (dataset distillation) that is cheap to retain in constrained memory, and adapt model size incrementally as new classes are learned, jointly addressing the memory-budget and forgetting problems that a naive incremental fine-tuning approach would face on embedded hardware.

## Technical contribution

A combined dataset-distillation-plus-model-size-adaptation algorithm for continual/incremental learning specifically targeting TinyML-class embedded deployment, rather than adapting a general-purpose continual-learning method (e.g. EWC-style regularization or exemplar replay) without regard to the memory constraints of the target hardware.

## Experimental methodology

Incremental learning experiments across multiple task/class-addition scenarios relevant to TinyML applications (voice recognition, anomaly detection, sensor data classification), comparing the dataset-distillation-based approach against baseline incremental-learning strategies in terms of forgetting and memory footprint (per the IEEE ICPS paper; detailed dataset/accuracy tables not independently re-derived in this record).

## Results

The combined dataset-distillation and model-size-adaptation approach mitigates catastrophic forgetting while keeping the memory footprint of retained historical information small enough for embedded deployment, outperforming naive fine-tuning baselines on the incremental-learning task set evaluated.

## Comparison with the state of the art

Distinguishes itself from exemplar-replay approaches like [[2017_Rebuffi_iCaRL]] (which retain raw or lightly-processed exemplars) by compressing retained history into a distilled synthetic dataset, and from purely regularization-based approaches like EWC ([[2017_Kirkpatrick_OvercomingCatastrophicForgetting]]) by directly addressing the memory-growth problem of TinyML deployment rather than only weight-importance protection.

## Strengths

Directly targets the TinyML/MCU-class deployment constraints that most general continual-learning literature does not consider; combines two complementary mechanisms (distillation for memory, size adaptation for capacity) rather than a single-technique fix.

## Weaknesses

Abstract-level record; specific memory footprint numbers, hardware targets, and accuracy-retention figures relative to full-history replay are not captured here in full detail.

## Limitations

Dataset distillation quality may degrade for more complex sensor modalities or class boundaries than the tasks evaluated; model-size growth still bounds how many tasks can be added before exceeding a fixed device's memory ceiling.

## Open questions

How does the dataset-distillation approach's forgetting/memory trade-off compare quantitatively to EWC-style regularization ([[2017_Kirkpatrick_OvercomingCatastrophicForgetting]]) or exemplar replay ([[2017_Rebuffi_iCaRL]]) under an identical fixed memory budget? How many incremental tasks can the model-size-adaptation mechanism absorb before exceeding typical Cortex-M memory ceilings?

## Possible extensions

A head-to-head comparison of dataset-distillation-based continual learning against EWC-style and exemplar-replay approaches under a fixed TinyML memory budget, extending the Continual_Learning concept's existing open problem about memory-budgeted continual learning.

## Relevance to our research

A concrete, TinyML-specific continual-learning mechanism for [[Continual_Learning]] and [[On-device_Learning]], complementing the more general-purpose EWC and iCaRL approaches already in this Observatory's KB with a method co-designed for embedded memory constraints from the outset.

## Possible thesis topics

Benchmarking dataset-distillation-based continual learning against EWC and exemplar-replay methods under a fixed MCU memory budget for a real always-on EdgeAI task (keyword spotting or HAR personalization).

## Possible collaborations

Groups working on TinyML on-device training and continual learning for embedded/industrial cyber-physical systems.

## Links to related papers

[[2017_Kirkpatrick_OvercomingCatastrophicForgetting]], [[2017_Rebuffi_iCaRL]]
