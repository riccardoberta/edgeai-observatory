# Biosignals

This concept covers processing physiological signals — EEG (brain electrical activity), ECG (heart electrical activity), PPG (blood volume changes, measured optically, as in a smartwatch), EMG (muscle electrical activity), and similar — on wearable or implantable devices, usually for health monitoring or human-machine interfaces.

## Evolution of the concept

Deep learning's clinical credibility for biosignals was established early by Hannun et al. ("Cardiologist-level arrhythmia detection and classification in ambulatory electrocardiograms using a deep neural network", Nature Medicine, 2019), trained on over 91,000 single-lead ECGs and shown to match or exceed practicing cardiologists across 12 heart-rhythm classes — the result that gave single-signal deep ECG classification clinical legitimacy. Biswas et al.'s CorNET (2019) is an early, widely-cited result in the same single-modality vein: a compact CNN+LSTM network that estimates heart rate and performs biometric identification from a single wrist-worn PPG channel despite motion artifacts.

Biosignal analysis has historically relied on models trained and specialized for one specific dataset and clinical setting, which limits how well a model generalizes across studies and devices. The field is now shifting toward foundation-model approaches that tokenize heterogeneous biosignals into one unified representation, so a single model can be pretrained across multiple structurally different datasets (different channel counts, sample lengths, missing-value patterns) and fine-tuned for varied downstream clinical tasks. Yang et al.'s Biosignal Transformer (BIOT, 2023) demonstrates exactly this: cross-data pretraining and fine-tuning across EEG, ECG, and activity-sensor signals via a unified tokenization scheme. Narayanswamy et al. ("Scaling Wearable Foundation Models", ICLR 2025) push the same direction to a much larger scale, training a multimodal foundation model (LSM) on up to 40 million hours of wearable data from over 165,000 people and establishing scaling laws across compute, data, and model size.

For EdgeAI specifically, the central tension is that these foundation models are far larger than what embedded biosignal-sensing hardware can run directly, making compression ([[Quantization]], [[Pruning]], [[Distillation]]) a critical open direction for bringing foundation-model-level performance to wearable health-monitoring devices. Two recent, fully open-access studies show this compression-for-deployment tension being addressed directly, at opposite ends of the hardware-cost spectrum and for two different clinical targets. Cuevas-Rodríguez et al. (2026) push real-time arrhythmia classification down to an 8-bit Arduino UNO microcontroller with a quantized 1D-CNN and a full acquisition-to-display pipeline, deliberately testing feasibility on hardware well below the Cortex-M tier the rest of this literature typically assumes. Gragnaniello, Riccio et al. (2025) target a more capable microcontroller tier (347 kB flash / 23 kB RAM) but extend the application itself: rather than rhythm classification, they use a spectrogram-plus-1D-CNN pipeline to non-invasively flag likely Type 1 diabetes from wearable ECG, reaching close to 90% accuracy in a validated custom-PCB prototype. Together the two studies map out a hardware-cost/clinical-task grid for on-device ECG analysis that complements the cross-modal foundation-model direction above.

## Key papers

[[2019_Hannun_CardiologistLevelArrhythmiaDetection]] — large-scale (91,232 ECG) single-lead deep classifier matching cardiologist-level performance across 12 rhythm classes, establishing clinical-grade credibility for single-modality biosignal deep learning that later cross-modal foundation-model work builds on.

[[2023_Yang_BIOT]] — Biosignal Transformer (BIOT) foundation model demonstrating cross-data pretraining and fine-tuning across EEG, ECG, and human-activity sensor signals via a unified tokenization scheme.

[[2026_CuevasRodriguez_TinyMLArrhythmiaMCU]] — real-time cardiac arrhythmia classification via a quantized 1D-CNN deployed on an 8-bit Arduino UNO, a full acquisition-to-display pipeline feasibility study for ultra-low-cost hardware.

[[2025_Gragnaniello_EdgeAIWearableDiabetesECG]] — spectrogram-plus-1D-CNN edge pipeline for non-invasive Type 1 diabetes detection from wearable ECG, quantized to 347 kB flash / 23 kB RAM and validated on a custom PCB prototype.

[[2019_Biswas_CorNET]] — compact CNN+LSTM network estimating heart rate and biometric identity from motion-affected wrist PPG; a widely-cited single-modality baseline predating the foundation-model direction.

[[2025_Narayanswamy_ScalingWearableFoundationModels]] — scaling laws for a multimodal wearable foundation model (LSM) trained on 40 million hours of data from over 165,000 people; the largest-scale evidence for this concept's edge-compression open question.

## Open problems

How much can biosignal foundation models be compressed (quantization, pruning, distillation) while retaining cross-dataset transfer benefits, to make them viable for on-device biosignal monitoring? Does cross-modal pretraining generalize to other biosignals relevant to edge health monitoring beyond EEG/ECG/activity, such as PPG or EMG?

## Research ideas

Applying quantization and distillation to a BIOT-style biosignal foundation model to evaluate how much cross-dataset benefit survives compression to a footprint suitable for embedded health-monitoring hardware.

## Possible thesis topics

Compressing a cross-modal biosignal foundation model for deployment on Cortex-M/Cortex-A-class wearable hardware. Extending unified biosignal tokenization to additional modalities (PPG, EMG) relevant to wearable health monitoring.

## Links

[[Human_Activity_Recognition]], [[Quantization]], [[Distillation]], [[Compression]], [[On-device_Learning]]
