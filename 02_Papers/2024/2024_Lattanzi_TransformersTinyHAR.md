# Are Transformers a Useful Tool for Tiny devices in Human Activity Recognition?

**Full citation:** Lattanzi, E., Calisti, L., Contoli, C. (2024). Are Transformers a Useful Tool for Tiny devices in Human Activity Recognition? Proceedings of the 2024 8th International Conference on Advances in Artificial Intelligence (ICAAI '24). https://doi.org/10.1145/3704137.3704171

**Linked concepts:** [[Human_Activity_Recognition]], [[Compression]]

## Abstract summary

The authors empirically evaluate whether transformer-based architectures, despite their theoretical advantages for time-series classification, are actually practical for wearable Human Activity Recognition on tiny, resource-constrained devices, finding that the deepest transformer variant that fits on-device achieves up to 14% lower accuracy than convolutional and recurrent baselines under the same memory budget.

## Research problem

Transformers have become the dominant architecture for time-series and sequence tasks generally, including HAR, but their RAM requirements may make them impractical for tiny wearable HAR devices — a question the field had been answering mostly by analogy with non-tiny-device transformer results rather than direct on-device evaluation.

## Key idea

Directly benchmark transformer-based HAR models against CNN and RNN/LSTM baselines under the actual memory constraints of tiny wearable devices, rather than comparing architectures only on offline accuracy without a hardware-budget constraint.

## Technical contribution

A systematic, hardware-budget-constrained comparison of transformer, CNN, and RNN/LSTM HAR architectures across several benchmark datasets; an empirical characterization of how much accuracy a memory-constrained transformer must sacrifice relative to convolutional/recurrent alternatives.

## Experimental methodology

Evaluation across multiple benchmark wearable HAR datasets, constraining each architecture family to the RAM budget realistic for a tiny wearable device, and comparing the resulting accuracy of the best transformer variant that fits against CNN and LSTM baselines at the same budget.

## Results

Under a tiny-device memory budget, the most capable deployable transformer variant achieves up to 14% lower accuracy than CNN/RNN baselines, indicating that transformers' RAM requirements impose a real accuracy penalty once genuinely constrained to tiny-device budgets, rather than transformers being a strictly superior architecture choice regardless of hardware.

## Comparison with the state of the art

Provides a direct empirical counterpoint to the broader transformer-adoption trend in time-series/HAR research (e.g. cross-modal foundation models like BIOT), showing the trend's architectural assumptions do not transfer cleanly to the tiniest deployment tier.

## Strengths

Directly tests a widely-assumed but rarely hardware-validated claim (transformers being broadly superior for time-series); evaluates across several benchmark datasets rather than a single case.

## Weaknesses

Evaluates transformer variants compact enough to fit tiny-device RAM budgets, which may not represent the most architecturally advanced transformer designs being developed elsewhere in the literature.

## Limitations

Results are specific to the wearable HAR domain and the particular RAM budgets tested; conclusions may not generalize to other always-on sensing tasks with different sequence lengths or sensor modalities.

## Open questions

Would more memory-efficient transformer variants (e.g. linear-attention or state-space-based designs) close the accuracy gap found here under the same tiny-device budget? Does the same accuracy penalty appear for cross-modal foundation models like BIOT once compressed down to tiny-device size?

## Possible extensions

Repeating the same constrained comparison with linear-attention or Mamba-style state-space HAR architectures, which claim to avoid the RAM overhead of standard self-attention; testing whether a compressed BIOT-style foundation model suffers the same accuracy penalty under tiny-device budgets.

## Relevance to our research

Directly informs the open question already flagged in our [[Human_Activity_Recognition]] entry about how accurate architectures actually perform when deployed under real hardware constraints, providing a concrete, hardware-budget-constrained answer for the transformer-versus-CNN/RNN question specifically.

## Possible thesis topics

Benchmarking memory-efficient transformer variants (linear attention, state-space models) against this paper's CNN/LSTM baselines under the same tiny-device RAM budget; compressing a BIOT-style HAR foundation model to the same budget and measuring whether the same accuracy penalty appears.

## Possible collaborations

Groups working on cross-modal biosignal/activity foundation models ([[Biosignals]]) that could supply a foundation-model baseline for the same constrained-comparison methodology.

## Links to related papers

[[2016_Ordonez_DeepConvLSTM]], [[2022_Zhang_DeepLearningHARWearableSensors]]
