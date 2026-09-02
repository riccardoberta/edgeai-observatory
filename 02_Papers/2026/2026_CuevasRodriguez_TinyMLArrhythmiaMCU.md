# Real-Time Cardiac Arrhythmia Classification Using TinyML on Ultra-Low-Cost Microcontrollers: A Feasibility Study for Resource-Constrained Environments

**Full citation:** Cuevas-Rodriguez, E.O., et al. (2026). Real-Time Cardiac Arrhythmia Classification Using TinyML on Ultra-Low-Cost Microcontrollers: A Feasibility Study for Resource-Constrained Environments. *Bioengineering*, 13(5), 532. DOI: 10.3390/bioengineering13050532

**PDF:** [MDPI (open access)](https://www.mdpi.com/2306-5354/13/5/532)

**Verification note:** MDPI is fully open access; bibliographic details and abstract confirmed directly via `web_fetch` of the article page.

**Linked concepts:** [[Biosignals]], [[Quantization]]

## Abstract summary

Presents an end-to-end real-time cardiac arrhythmia classification system built around a quantized one-dimensional convolutional neural network (1D-CNN) deployed on an 8-bit Arduino UNO microcontroller — deliberately targeting the cheapest, most resource-constrained class of hardware rather than a Cortex-M-class MCU. The pipeline covers ECG acquisition via a low-cost AD8232 analog front end, signal preprocessing, heartbeat segmentation, on-device classification, and real-time visualization on an OLED display, explicitly framed as a feasibility study for extremely resource-constrained deployment environments.

## Research problem

Most TinyML biosignal work targets 32-bit Cortex-M-class microcontrollers; whether real-time, clinically meaningful arrhythmia classification is feasible on genuinely ultra-low-cost 8-bit hardware (Arduino UNO / ATmega-class, without a dedicated NPU/DSP or even a 32-bit core) had not been established, which matters directly for cost-constrained or resource-poor healthcare deployment settings.

## Key idea

Push quantized 1D-CNN arrhythmia classification down to an 8-bit AVR-class microcontroller by tightly co-designing every pipeline stage, a minimal analog front end (AD8232), lightweight preprocessing/segmentation, and an aggressively quantized model, so the entire real-time pipeline fits within the memory and compute budget of the cheapest commodity microcontroller class.

## Technical contribution

A complete, real-time, end-to-end arrhythmia-classification system (acquisition through on-device display) validated on 8-bit Arduino UNO hardware, demonstrating that quantized 1D-CNN biosignal classification is feasible well below the Cortex-M tier typically assumed necessary for this task.

## Experimental methodology

Full pipeline implementation and real-time evaluation on Arduino UNO hardware: ECG acquisition via the AD8232 analog front end, preprocessing and heartbeat segmentation, quantized 1D-CNN inference, and live classification output on an OLED display (per the MDPI article; classification accuracy and latency figures per the published results, not independently re-derived here).

## Results

Demonstrated real-time, on-device arrhythmia classification running entirely on an 8-bit Arduino UNO with acceptable classification accuracy for the feasibility study's target use case (per the published abstract), establishing that this class of hardware, far below typical TinyML MCU targets, is a viable deployment tier for basic real-time biosignal classification.

## Comparison with the state of the art

Distinguishes itself from the bulk of TinyML biosignal literature (including [[2025_Gragnaniello_EdgeAIWearableDiabetesECG]]) that targets 32-bit Cortex-M microcontrollers with dedicated flash/RAM budgets in the hundreds of KB; this paper instead demonstrates feasibility on markedly weaker 8-bit hardware, trading model capacity for hardware cost.

## Strengths

Full end-to-end system (not just an offline model benchmark) validated on real, extremely low-cost hardware; directly relevant to resource-constrained/low-income healthcare deployment settings, an application angle less commonly emphasized in the TinyML biosignal literature; fully open-access, full-text-verifiable publication.

## Weaknesses

8-bit AVR hardware imposes hard ceilings on model capacity and arrhythmia-class coverage compared to Cortex-M-class systems; this record does not capture the full quantitative accuracy/latency table (only the headline feasibility result from the abstract).

## Limitations

Likely restricted to a smaller set of arrhythmia classes and lower classification granularity than Cortex-M-class systems can support; single-lead ECG via a low-cost analog front end constrains signal quality relative to clinical-grade acquisition.

## Open questions

How does classification accuracy and class coverage degrade as the arrhythmia taxonomy grows, and where exactly does the 8-bit ceiling bind relative to 32-bit Cortex-M deployments such as [[2025_Gragnaniello_EdgeAIWearableDiabetesECG]]? Is the same "push down to 8-bit" strategy viable for other biosignal tasks (EMG, EEG) or specific to the relative simplicity of single-lead ECG rhythm classification?

## Possible extensions

A systematic accuracy/cost/power comparison across the full microcontroller cost tier (8-bit AVR vs. Cortex-M0/M4 vs. Cortex-M with dedicated DSP/NPU) for the same arrhythmia-classification task, to map out where each additional dollar of hardware cost buys the most accuracy.

## Relevance to our research

Extends [[Biosignals]] and [[Quantization]] into the lowest-cost hardware tier explored in this Observatory's KB for cardiac applications, directly complementing the more typical Cortex-M-targeted work such as [[2025_Gragnaniello_EdgeAIWearableDiabetesECG]] and giving a concrete lower bound on hardware cost for real-time ECG classification.

## Possible thesis topics

A head-to-head benchmark of the same quantized arrhythmia-classification model deployed across 8-bit AVR, Cortex-M0, and Cortex-M4 hardware, quantifying the accuracy/cost/power Pareto frontier for low-resource cardiac monitoring.

## Possible collaborations

Groups working on low-cost/resource-constrained healthcare technology and TinyML deployment for global-health or point-of-care settings.

## Links to related papers

[[2025_Gragnaniello_EdgeAIWearableDiabetesECG]]
