# Scaling Wearable Foundation Models

**Full citation:** Narayanswamy, G., Liu, X., Ayush, K., et al. (2025). Scaling Wearable Foundation Models. International Conference on Learning Representations (ICLR 2025). arXiv:2410.13638

**PDF:** [arXiv](https://arxiv.org/abs/2410.13638)

**Linked concepts:** [[Biosignals]]

## Abstract summary

Studies the scaling properties (compute, data, model size) of LSM, a multimodal wearable-sensor foundation model trained on up to 40 million hours of heart rate, heart rate variability, electrodermal activity, accelerometer, skin temperature, and altimeter data from over 165,000 people, establishing scaling laws and sample-efficient downstream transfer for tasks such as imputation and activity recognition.

## Research problem

Whether the scaling-law behavior observed for language and vision foundation models also holds for multimodal physiological/wearable sensor data, and how such scaling should inform the design of a practical wearable foundation model.

## Key idea

Train one multimodal foundation model (LSM) across the largest assembled wearable-signal dataset and range of sensor modalities to date, and systematically measure how performance scales with compute, data, and model size.

## Technical contribution

Empirically established scaling laws for wearable-sensor foundation models across six modalities; a sample-efficient downstream transfer method for imputation, interpolation, extrapolation, and activity/exercise recognition.

## Experimental methodology

Pretraining LSM on up to 40M hours of data from 165,000+ people, then evaluating scaling curves and downstream task transfer (few-shot and full fine-tuning) against smaller and single-modality baselines.

## Results

Performance improves predictably with scale across all measured axes; the resulting model enables markedly more sample-efficient downstream learning than training task-specific models from scratch.

## Comparison with the state of the art

Directly extends the cross-modal biosignal foundation-model direction this KB already tracks via [[2023_Yang_BIOT]], at far larger scale (40M hours vs. BIOT's more modest pretraining corpora) and explicitly raises the on-device deployment question this concept's open problems already name.

## Strengths

Industrial-scale dataset and compute; rigorous scaling-law methodology; directly relevant to this concept's central open question about foundation-model compression for edge deployment.

## Weaknesses

The paper itself does not attempt compression or on-device deployment; scale (40M hours, Google-internal data) is not reproducible outside a well-resourced industry lab.

## Limitations

Scaling laws characterized only up to the model sizes/compute budgets tested; edge/embedded deployment left as future work rather than demonstrated.

## Open questions

At what point does the accuracy gain from further scaling stop justifying the resulting on-device compression cost? Does the sample-efficiency benefit survive aggressive quantization/pruning/distillation to a footprint suitable for wearable hardware?

## Possible extensions

A compression study applying this KB's Quantization/Distillation/Pruning techniques to a scaled-down LSM-style checkpoint, measuring how much of the scaling-law benefit survives compression to a wearable-deployable footprint.

## Relevance to our research

The most direct, large-scale evidence yet for this concept's central open problem (compressing biosignal foundation models for on-device deployment) — establishes the accuracy ceiling any future compression work would need to preserve.

## Possible thesis topics

Empirically characterizing how much of LSM's (or a similar wearable foundation model's) scaling-law benefit survives quantization and distillation to a Cortex-M/Cortex-A wearable deployment budget.

## Possible collaborations

Groups working on large-scale wearable sensor foundation models (Google Research) and on-device model compression.

## Links to related papers

[[2023_Yang_BIOT]], [[2019_Biswas_CorNET]]
