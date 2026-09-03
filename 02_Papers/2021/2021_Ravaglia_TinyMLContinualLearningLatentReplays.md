# A TinyML Platform for On-Device Continual Learning with Quantized Latent Replays

**Full citation:** Ravaglia, L., Rusci, M., Nadalini, D., Capotondi, A., Conti, F., Benini, L. (2021). A TinyML Platform for On-Device Continual Learning with Quantized Latent Replays. IEEE Journal on Emerging and Selected Topics in Circuits and Systems, 11(4), 789-802. DOI: 10.1109/JETCAS.2021.3121554. arXiv:2110.10486.

**PDF:** [arXiv](https://arxiv.org/abs/2110.10486)

**Verification note:** Bibliographic details confirmed via WebSearch (arXiv, IEEE Xplore listing, IRIS UniBo). Abstract-level verified.

**Linked concepts:** [[Continual_Learning]], [[On-device_Learning]]

## Abstract summary

A TinyML continual-learning platform combining a quantized latent-replay mechanism (storing compact, low-bitwidth intermediate activations rather than raw input data) with a memory-driven training scheme, demonstrated to fit continual learning into under 64 MB of memory on real embedded hardware.

## Research problem

Standard replay-based continual learning stores raw exemplar data, which is both a privacy risk and memory-infeasible on TinyML-class devices; existing latent-replay approaches had not been made to fit within genuinely embeddable memory budgets.

## Key idea

Store replay exemplars as quantized latent (intermediate-layer) representations instead of raw input data, drastically cutting both the memory footprint and the privacy exposure of the replay buffer.

## Technical contribution

A full TinyML continual-learning system integrating quantized latent replay with a memory-aware training pipeline, validated end-to-end on embedded hardware rather than only simulated.

## Experimental methodology

Deployed and evaluated on real embedded hardware (GAP8-class platform), measuring memory footprint, accuracy retention across sequential learning tasks, and comparing against full raw-data-replay baselines.

## Results

Achieves continual learning within under 64 MB of memory — compatible with genuine embedded/TinyML deployment — while retaining accuracy competitive with raw-data-replay methods that require far more memory.

## Comparison with the state of the art

Directly answers the memory-budget objection to exemplar-replay methods like [[2017_Rebuffi_iCaRL]] and [[2017_LopezPaz_GradientEpisodicMemory]] by replacing raw-data storage with quantized latent representations, and complements this KB's [[2024_Rub_ContinualIncrementalTinyML]] (dataset distillation) as an alternative memory-efficient replay strategy.

## Strengths

Real embedded-hardware validation, not simulation; directly connects [[Quantization]] and [[Continual_Learning]] as this KB's own Links section for Continual_Learning already anticipates; well-cited (150+) for a hardware-validated systems paper.

## Weaknesses

Validated on one hardware platform (GAP8-class RISC-V); latent-replay quality depends on how well the frozen early layers generalize to new tasks, a limitation not fully explored.

## Limitations

Does not address task-boundary detection — assumes task switches are known, a limitation shared with much of the classic continual-learning literature.

## Open questions

How does quantized latent replay compare directly, on the same hardware and task sequence, against dataset-distillation-based approaches like [[2024_Rub_ContinualIncrementalTinyML]]?

## Possible extensions

A head-to-head benchmark of quantized-latent-replay versus dataset-distillation continual learning under an identical embedded memory budget and task sequence.

## Relevance to our research

A concrete, hardware-validated bridge between [[Quantization]] and [[Continual_Learning]] for genuinely TinyML-class deployment, filling a gap this KB's Continual_Learning concept had before this audit (only EWC/iCaRL/GEM as general methods, no hardware-validated TinyML replay mechanism).

## Possible thesis topics

Benchmarking quantized-latent-replay against dataset-distillation-based continual learning on a common TinyML task and memory budget; extending latent replay to a task-boundary-free, drift-based setting.

## Possible collaborations

Groups working on TinyML continual learning and RISC-V/GAP-class embedded platforms (this KB already tracks the same lab's GAP-8/PULP hardware lineage under [[NPU]]/[[RISC-V]]).

## Links to related papers

[[2017_Rebuffi_iCaRL]], [[2017_LopezPaz_GradientEpisodicMemory]], [[2024_Rub_ContinualIncrementalTinyML]]
