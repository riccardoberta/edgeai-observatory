# Keyword Spotting

## Evolution of the concept

Keyword spotting's modern deep-learning era starts with Sainath and Parada's "Convolutional Neural Networks for Small-footprint Keyword Spotting" (Interspeech 2015), which showed that a small CNN could outperform fully-connected DNNs for KWS with far fewer parameters — establishing the small-footprint CNN as the architecture family the rest of the field, and the benchmark below, would standardize around. Keyword spotting (recognizing short keywords on "always-on" low-power devices) long suffered from the lack of a standard dataset for reproducibly comparing models. Warden (2018) solves the problem with Speech Commands, a public crowd-sourced dataset that became the de facto standard, also used in benchmarks like MLPerf Tiny, typically paired with runtimes like TensorFlow Lite Micro and kernels like CMSIS-NN. Two 2025 studies push the field toward a more system-level and more hardware-integrated view: Bartoli et al. show that the DSP-domain MFCC feature-extraction stage, not just the neural network, is a significant contributor to total pipeline cost across three STM32 platform tiers; and Liang et al. demonstrate a dedicated keyword-spotting accelerator co-designed with the algorithm into a complete audio SoC, validated via a working FPGA-based prototype.

## Key papers

[[2015_Sainath_CNNKeywordSpotting]] — shows a small CNN outperforming fully-connected DNNs for KWS with far fewer parameters, establishing the small-footprint CNN architecture family later standardized on via Speech Commands.

[[2018_Warden_SpeechCommands]] — public dataset and collection methodology for reproducible keyword spotting benchmarks.

[[2025_Bartoli_EndToEndKeywordSpotting]] — system-level pipeline benchmark across three STM32 tiers, showing MFCC feature extraction is a significant, often-overlooked contributor to total cost.

[[2025_Liang_IntelligentAudioSoC]] — dedicated keyword-spotting accelerator co-designed into an audio SoC, validated via a working FPGA-based prototype.

## Open problems

Extending equivalent benchmarks to languages other than English with limited data-collection resources. Robustness of models under real acoustic conditions (background noise, distance from microphone), not fully represented by the dataset's recording conditions.

## Research ideas

A dataset version with realistic background noise added synthetically; multilingual keyword spotting using few-shot techniques for low-resource languages, including Italian.

## Possible thesis topics

Evaluating the robustness of keyword spotting models trained on Speech Commands when deployed on a microcontroller with real microphones in noisy environments; extension to an Italian vocabulary.

## Links

[[TensorFlow Lite Micro]], [[CMSIS-NN]], [[Cortex-M]]
