# BIOT: Cross-data Biosignal Learning in the Wild

**Full citation:** Yang, C., Westover, M. B., Sun, J. (2023). BIOT: Cross-data Biosignal Learning in the Wild. arXiv:2305.10351. https://arxiv.org/abs/2305.10351

**Linked concepts:** [[Biosignals]], [[Compression]]

## Abstract summary

The authors propose BIOT (Biosignal Transformer), a foundation-model approach to biosignal analysis that tokenizes diverse biosignals (EEG, ECG, human activity sensory signals) into unified "biosignal sentences," enabling a single model to be pretrained across multiple datasets with mismatched channels, variable sample lengths, and missing values, and then fine-tuned for different downstream clinical tasks.

## Research problem

Deep learning models for biosignals are typically specialized for one specific dataset and clinical setting, because different biosignal sources (and even different recordings of the same signal type) vary in channel count, sampling length, and missing-value patterns; this fragmentation limits the broader applicability of any single trained model and prevents the field from benefiting from cross-dataset pretraining the way text and vision foundation models do.

## Key idea

Convert heterogeneous biosignals into a unified tokenized representation ("biosignal sentences") so that a single transformer-based model can be pretrained across multiple, structurally different biosignal datasets and then fine-tuned for specific downstream tasks, rather than training a bespoke model per dataset.

## Technical contribution

The Biosignal Transformer (BIOT) architecture and its tokenization scheme for handling mismatched channels, variable sample lengths, and missing values across biosignal types, plus a cross-data pretraining and fine-tuning methodology validated across EEG, ECG, and human activity sensory signals.

## Experimental methodology

Comprehensive evaluations across EEG, ECG, and human activity sensory signal datasets, comparing BIOT's cross-data pretraining-then-fine-tuning approach against robust baselines trained in the conventional single-dataset setting, measuring downstream task performance and the model's ability to learn jointly across datasets with different formats.

## Results

BIOT outperforms robust single-dataset baselines in common settings and demonstrates that cross-dataset learning across structurally different biosignal types (EEG, ECG, activity sensors) is feasible and beneficial, supporting the broader foundation-model thesis for biosignal analysis.

## Comparison with the state of the art

Prior biosignal deep learning models were largely dataset- and task-specific; BIOT is among the first to demonstrate a transformer-based, cross-data foundation-model approach spanning multiple biosignal modalities (not just EEG or just ECG), positioning it alongside the broader trend toward pretrained foundation models being applied to biosignals (e.g. later EEG-specific foundation models such as "Large Cognition Model").

## Strengths

Addresses a genuine, widely-felt pain point (dataset fragmentation) in biosignal deep learning; spans three distinct signal modalities in one evaluation, demonstrating real cross-modal transfer rather than a single narrow case study; openly available implementation (GitHub) supports reproducibility.

## Weaknesses

As a transformer-based foundation model, BIOT's compute and memory footprint is substantially larger than what most embedded biosignal-sensing hardware (Cortex-M-class) can support directly, so the paper does not itself address on-device deployment or quantization/compression for edge use.

## Limitations

The cross-data pretraining approach assumes access to multiple diverse biosignal datasets, which may not be available in narrower clinical or research settings; the paper evaluates fine-tuned downstream performance but does not benchmark inference cost on constrained edge hardware relevant to this Observatory's [[Hardware]] taxonomy.

## Open questions

How much can BIOT-style foundation models be compressed (quantization, pruning, distillation) while retaining cross-dataset transfer benefits, to make them viable for on-device biosignal monitoring? Does cross-modal pretraining (EEG+ECG+activity) generalize to other biosignals relevant to edge health monitoring, such as PPG or EMG?

## Possible extensions

Applying [[Quantization]] and [[Distillation]] to a BIOT-style biosignal foundation model to evaluate how much of its cross-dataset benefit survives compression to a footprint suitable for embedded health-monitoring hardware.

## Relevance to our research

Foundational reference for the [[Biosignals]] branch of our [[Applications]] taxonomy, and a natural test case for whether large-model compression techniques developed elsewhere in this Observatory ([[Quantization]], [[Distillation]], [[Compression]]) can bring foundation-model-level biosignal performance to constrained edge hardware.

## Possible thesis topics

Compressing a BIOT-style cross-modal biosignal foundation model for deployment on Cortex-M/Cortex-A-class wearable hardware, measuring how much cross-dataset transfer benefit survives quantization/pruning/distillation; extending the BIOT tokenization approach to additional biosignal modalities (PPG, EMG) relevant to wearable health monitoring.

## Possible collaborations

Clinical biosignal research groups; wearable health-monitoring hardware vendors.

## Links to related papers

[[2022_Zhang_DeepLearningHARWearableSensors]] (shares the human activity sensory signal modality), [[2022_Lin_OnDeviceTraining256KB]] (relevant for any on-device fine-tuning of a compressed biosignal model)
