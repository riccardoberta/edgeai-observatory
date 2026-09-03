# Keyword Spotting

## Evolution of the concept

Keyword spotting's modern deep-learning era starts with Sainath and Parada's "Convolutional Neural Networks for Small-footprint Keyword Spotting" (Interspeech 2015), which showed that a small CNN could outperform fully-connected DNNs for KWS with far fewer parameters — establishing the small-footprint CNN as the architecture family the rest of the field, and the benchmark below, would standardize around. Keyword spotting (recognizing short keywords on "always-on" low-power devices) long suffered from the lack of a standard dataset for reproducibly comparing models. Warden (2018) solves the problem with Speech Commands, a public crowd-sourced dataset that became the de facto standard, also used in benchmarks like MLPerf Tiny, typically paired with runtimes like TensorFlow Lite Micro and kernels like CMSIS-NN. Zhang, Suda, Lai, and Chandra's "Hello Edge: Keyword Spotting on Microcontrollers" (arXiv 2017, 720+ citations) is the field's other foundational reference, missing from this concept until a 2026-09-03 exhaustive Scholar audit: a systematic architecture-exploration methodology comparing DNN/CNN/RNN/CRNN/DS-CNN under microcontroller memory and compute constraints, introducing the depthwise-separable CNN (DS-CNN) that reaches 95.4% accuracy — the architecture and evaluation methodology this concept's own STM32-tier and benchmark anchors implicitly build on. Two 2025 studies push the field toward a more system-level and more hardware-integrated view: Bartoli et al. show that the DSP-domain MFCC feature-extraction stage, not just the neural network, is a significant contributor to total pipeline cost across three STM32 platform tiers; and Liang et al. demonstrate a dedicated keyword-spotting accelerator co-designed with the algorithm into a complete audio SoC, validated via a working FPGA-based prototype.

## Key papers

[[2015_Sainath_CNNKeywordSpotting]] — shows a small CNN outperforming fully-connected DNNs for KWS with far fewer parameters, establishing the small-footprint CNN architecture family later standardized on via Speech Commands.

[[2018_Warden_SpeechCommands]] — public dataset and collection methodology for reproducible keyword spotting benchmarks.

[[2017_Zhang_HelloEdgeKeywordSpottingMCU]] — systematic microcontroller-constrained architecture exploration introducing DS-CNN (95.4% accuracy), one of the two foundational KWS papers this concept's later work builds on.

[[2025_Bartoli_EndToEndKeywordSpotting]] — system-level pipeline benchmark across three STM32 tiers, showing MFCC feature extraction is a significant, often-overlooked contributor to total cost.

[[2025_Liang_IntelligentAudioSoC]] — dedicated keyword-spotting accelerator co-designed into an audio SoC, validated via a working FPGA-based prototype.

[[2018_Flamand_GAP8]] — RISC-V multi-core cluster with a dedicated convolution engine and ultra-low-power always-on domain, a hardware platform well-suited to always-on keyword spotting.

[[2022_Gerum_HANNAH]] — jointly searches network architecture and hardware accelerator configuration for always-on audio sensing, directly targeting keyword spotting as the motivating use case.

[[2026_Jeziorek_EventAudioGNNKWS]] — a structurally different, neuromorphic-sensor-based approach: event-driven graph neural network hardware (SoC FPGA) for keyword spotting from an artificial-cochlea event stream rather than conventional microphone+MFCC input, reaching 95% word-end detection accuracy at 10.53µs latency and 1.18W.

## Open problems

Extending equivalent benchmarks to languages other than English with limited data-collection resources. Robustness of models under real acoustic conditions (background noise, distance from microphone), not fully represented by the dataset's recording conditions. How does the neuromorphic event-based pipeline ([[2026_Jeziorek_EventAudioGNNKWS]]) compare in accuracy, latency, and energy to the conventional MFCC/CNN pipeline on equivalent hardware — an open cross-pipeline comparison neither side has run yet.

## Research ideas

A dataset version with realistic background noise added synthetically; multilingual keyword spotting using few-shot techniques for low-resource languages, including Italian.

## Possible thesis topics

Evaluating the robustness of keyword spotting models trained on Speech Commands when deployed on a microcontroller with real microphones in noisy environments; extension to an Italian vocabulary.

## Links

[[TensorFlow Lite Micro]], [[CMSIS-NN]], [[Cortex-M]]
