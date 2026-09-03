# CorNET: Deep Learning Framework for PPG-Based Heart Rate Estimation and Biometric Identification in Ambulant Environment

**Full citation:** Biswas, D., Everson, L., Liu, M., Panwar, M., Verhoef, B.E., Patki, S., Kim, C.H., Acharyya, A., Van Hoof, C., Konijnenburg, M., Van Helleputte, N. (2019). CorNET: Deep Learning Framework for PPG-Based Heart Rate Estimation and Biometric Identification in Ambulant Environment. IEEE Transactions on Biomedical Circuits and Systems, 13(2), 282-291.

**PDF:** [PubMed](https://pubmed.ncbi.nlm.nih.gov/30629514/)

**Linked concepts:** [[Biosignals]]

## Abstract summary

Introduces CorNET, a four-layer CNN+LSTM deep network that estimates heart rate and performs biometric identification from a single wrist-worn PPG channel collected during real ambulant (motion-affected) conditions, without hand-engineered motion-artifact-removal preprocessing.

## Research problem

Wrist-worn PPG is a popular, non-invasive alternative to ECG for continuous cardiovascular monitoring, but motion artifacts from daily activity severely degrade classical signal-processing-based heart rate estimation.

## Key idea

Let a personalized CNN+LSTM network learn to estimate heart rate directly from raw single-channel PPG despite motion artifacts, rather than first removing artifacts with a separate signal-processing stage; the same learned representation also supports biometric identification.

## Technical contribution

A compact four-layer deep network combining two convolutional layers with two LSTM layers, personalized per subject, jointly addressing heart rate estimation and biometric identification from one wrist-worn PPG signal.

## Experimental methodology

Evaluated on PPG data collected during physical activity (ambulant, motion-affected conditions) against classical HR-estimation baselines and prior biometric-identification methods.

## Results

Improved heart rate estimation accuracy under motion compared to classical baselines, plus competitive biometric identification accuracy from the same signal and network.

## Comparison with the state of the art

Predates and is a direct precursor to the cross-modal biosignal foundation-model direction now tracked in this KB ([[2023_Yang_BIOT]], scaling-law wearable foundation models); demonstrates the single-modality, task-specific deep learning baseline that foundation-model approaches now aim to generalize beyond.

## Strengths

Widely cited early deep-learning result for wearable PPG; addresses a real deployment obstacle (motion artifacts) rather than only clean-signal benchmarks; dual-task design from one signal.

## Weaknesses

Personalization requirement (per-subject tuning) limits out-of-the-box generalization; single modality (PPG only); no on-device deployment or embedded hardware validation in the paper itself.

## Limitations

Does not address model compression or embedded deployment; validated only on relatively small research cohorts of the era.

## Open questions

Can a single-modality architecture like CorNET's CNN+LSTM be compressed enough for on-wrist microcontroller deployment, avoiding cloud offload of raw PPG?

## Possible extensions

Combining CorNET-style motion-robust PPG processing with quantization/distillation for on-device wearable deployment; extending to multimodal PPG+accelerometer fusion.

## Relevance to our research

A foundational, widely-cited deep-learning-for-wearable-PPG result that predates and contextualizes this KB's cross-modal biosignal foundation-model direction (BIOT, LSM/Scaling Wearable Foundation Models).

## Possible thesis topics

Benchmarking CorNET-style motion-robust PPG heart rate estimation against a compressed cross-modal foundation model on the same on-wrist hardware target.

## Possible collaborations

Groups working on wearable PPG and low-power biosignal ASIC/SoC design (imec, KU Leuven).

## Links to related papers

[[2019_Hannun_CardiologistLevelArrhythmiaDetection]], [[2023_Yang_BIOT]]
