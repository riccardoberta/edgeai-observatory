# A Study on the Application of TensorFlow Compression Techniques to Human Activity Recognition

**Full citation:** Contoli, C., Lattanzi, E. (2023). A Study on the Application of TensorFlow Compression Techniques to Human Activity Recognition. IEEE Access, 11, 48046-48058. DOI: 10.1109/ACCESS.2023.3276286

**PDF:** [IEEE Xplore](https://ieeexplore.ieee.org/document/10124768/)

**Linked concepts:** [[Human_Activity_Recognition]]

## Abstract summary

A systematic study of TensorFlow Lite compression techniques (simple conversion, dynamic-range quantization, full-integer quantization) applied to CNN, LSTM, and combined CNN-LSTM HAR models on the UCI-HAR dataset, comparing cascading versus stand-alone compression strategies.

## Research problem

Deep HAR models (CNN, LSTM, CNN-LSTM) deliver strong accuracy but are too complex and resource-demanding to deploy directly on constrained wearable/edge devices; which compression technique and application strategy best preserves accuracy for each architecture family was not systematically established.

## Key idea

Apply and compare multiple standard TensorFlow Lite compression techniques across three common HAR architecture families, testing both single-technique and cascaded (combined) compression.

## Technical contribution

A systematic, architecture-by-architecture comparison of compression technique effectiveness for HAR models, including a cascading-compression evaluation strategy not typically reported in single-technique compression papers.

## Experimental methodology

CNN, LSTM, and CNN-LSTM models trained on the UCI-HAR dataset, compressed via simple conversion, dynamic-range quantization, and full-integer quantization individually and in combination, measured for accuracy retention and size/latency reduction.

## Results

Quantifies which architecture/compression-technique combinations best preserve accuracy while reducing model size, with cascading compression offering further gains in some configurations.

## Comparison with the state of the art

A direct empirical precursor to this KB's own [[2024_Lattanzi_TransformersTinyHAR]] (same lead author, Lattanzi), which later extends the same tiny-wearable-budget question to transformer architectures; grounds that later comparison's CNN/LSTM baselines in systematically measured compression behavior.

## Strengths

Systematic architecture-by-architecture comparison; open, reproducible dataset (UCI-HAR); directly actionable for practitioners choosing a compression strategy per architecture family.

## Weaknesses

Single dataset; does not include transformer architectures (addressed by the same group's later 2024 paper); no real hardware energy measurement, only model-level size/latency.

## Limitations

TensorFlow Lite-specific; findings may not transfer directly to other runtimes (CMSIS-NN, microTVM).

## Open questions

Do the same architecture-specific compression-technique rankings hold on real embedded hardware (not just simulated size/latency), and do they extend to the transformer architectures evaluated in the group's later work?

## Possible extensions

Extending the same cascading-compression methodology to transformer-based HAR models, connecting directly to [[2024_Lattanzi_TransformersTinyHAR]].

## Relevance to our research

Direct empirical precursor and methodological grounding for this KB's existing transformer-vs-CNN/LSTM tiny-HAR comparison; a practical reference for choosing a compression strategy per HAR architecture family.

## Possible thesis topics

Extending this cascading-compression methodology to real Cortex-M hardware energy measurements rather than model-level size/latency estimates.

## Possible collaborations

University of Urbino group (Contoli, Lattanzi) working on energy-efficient HAR compression.

## Links to related papers

[[2024_Lattanzi_TransformersTinyHAR]], [[2016_Ronao_HARSmartphoneSensorsDeepLearning]]
