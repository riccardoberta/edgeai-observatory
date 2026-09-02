# Edge-AI Enabled Wearable Device for Non-Invasive Type 1 Diabetes Detection Using ECG Signals

**Full citation:** Gragnaniello, M., Marrazzo, V.R., Borghese, A., Maresca, L., Breglio, G., Riccio, M. (2025). Edge-AI Enabled Wearable Device for Non-Invasive Type 1 Diabetes Detection Using ECG Signals. *Bioengineering*, 12(1), 4. DOI: 10.3390/bioengineering12010004

**PDF:** [MDPI (open access)](https://www.mdpi.com/2306-5354/12/1/4)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed via WebSearch (Google Scholar record) cross-referenced with the MDPI journal listing.

**Linked concepts:** [[Biosignals]], [[Quantization]]

## Abstract summary

Proposes a wearable, microcontroller-based Edge-AI system that performs real-time ECG acquisition and non-invasively flags the likely presence of (Type 1) diabetes on-device, using a spectrogram-based preprocessing step feeding a 1-Dimensional Convolutional Neural Network (1D-CNN). The quantized model achieves close to 90% accuracy while fitting in 347 kB of flash and 23 kB of RAM, validated on a custom PCB prototype for low-power, real-world wearable deployment.

## Research problem

Diabetes screening conventionally requires invasive blood-glucose testing; recent evidence links glycaemic state to detectable ECG signal changes, but turning that link into a real-time, non-invasive, wearable screening tool requires a model small enough to run on-device (for privacy and continuous/offline operation) while remaining accurate enough to be clinically useful, which had not been demonstrated end-to-end on real wearable hardware.

## Key idea

Convert ECG signals to spectrograms as a preprocessing step, feeding a compact 1D-CNN sized and quantized to fit a microcontroller's memory budget, so that diabetes-relevant ECG pattern detection runs entirely on a wearable device rather than requiring cloud offload of continuous ECG data.

## Technical contribution

A validated, quantized Edge-AI pipeline (spectrogram preprocessing + 1D-CNN) for non-invasive diabetes detection from ECG, fitting within 347 kB flash / 23 kB RAM, plus a custom PCB wearable prototype demonstrating real-world feasibility rather than only an offline model benchmark.

## Experimental methodology

Model development and quantization targeting the 347 kB flash / 23 kB RAM budget; accuracy evaluated on ECG data for diabetes detection (near-90% reported); functional validation on a custom-built PCB wearable prototype (per the MDPI abstract; dataset size, patient cohort, and detailed accuracy breakdown not captured in this record beyond the headline figures).

## Results

Approximately 90% classification accuracy for non-invasive diabetes detection from ECG, with the quantized model fitting comfortably within typical Cortex-M-class microcontroller memory budgets (347 kB flash, 23 kB RAM), and a working custom PCB prototype validating real-world wearable feasibility.

## Comparison with the state of the art

Extends the broader trend of ECG-based Edge-AI screening (paralleling arrhythmia-focused work such as [[2026_CuevasRodriguez_TinyMLArrhythmiaMCU]]) to a new application, metabolic/glycaemic screening, rather than rhythm classification, and targets a more capable microcontroller tier (347 kB flash) than the 8-bit feasibility study in that companion record.

## Strengths

Genuinely novel application angle (non-invasive diabetes screening from ECG, not just arrhythmia classification) within the Biosignals space; end-to-end validation including a physical wearable prototype, not just a simulated model; fully open-access, full-text-verifiable publication.

## Weaknesses

Near-90% accuracy, while promising for a screening tool, would need substantially higher sensitivity/specificity validation before any clinical screening claim; this record captures headline results only, not the full clinical validation methodology, cohort size, or class-balance details.

## Limitations

Type 1 diabetes specifically (not Type 2, which is far more prevalent and often the more clinically pressing screening target); non-invasive ECG-based diabetes detection is a relatively young evidentiary area, so the underlying physiological link merits independent replication beyond this single study.

## Open questions

Does the same spectrogram+1D-CNN approach generalize to Type 2 diabetes detection, and how does accuracy hold up across a larger, more diverse patient cohort? How does the model's memory footprint and accuracy compare directly against arrhythmia-classification models on the same or similar hardware tier, e.g. [[2026_CuevasRodriguez_TinyMLArrhythmiaMCU]]?

## Possible extensions

Extending the pipeline to Type 2 diabetes and to larger, demographically diverse validation cohorts; combining diabetes screening and arrhythmia detection into a single multi-task on-device model sharing the same ECG front end.

## Relevance to our research

A recent (2025), fully open-access example for [[Biosignals]] and [[Quantization]] of Edge-AI extending beyond cardiac-rhythm classification into metabolic screening from the same ECG modality — broadens the Observatory's Biosignals coverage beyond the arrhythmia-classification cluster represented by [[2026_CuevasRodriguez_TinyMLArrhythmiaMCU]].

## Possible thesis topics

Extending non-invasive ECG-based diabetes screening to Type 2 diabetes with a larger validation cohort, or building a unified multi-task on-device ECG model that jointly screens for arrhythmia and glycaemic abnormality on shared wearable hardware.

## Possible collaborations

Wearable biosignal hardware groups and clinical partners with access to ECG/glycaemic-state paired datasets for screening-model validation.

## Links to related papers

[[2026_CuevasRodriguez_TinyMLArrhythmiaMCU]]
