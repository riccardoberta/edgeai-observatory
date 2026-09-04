# Keyword Spotting

Keyword spotting (KWS) detects one or a few specific spoken words or phrases — a wake word like "Hey Siri", for example — using a small, always-on model, rather than running full speech recognition continuously. Because the model must run continuously on battery power, it is one of the most tightly resource-constrained EdgeAI applications.

## Evolution of the concept

The modern deep-learning era of keyword spotting starts with Sainath and Parada ("Convolutional Neural Networks for Small-footprint Keyword Spotting", 2015), which showed that a small CNN could outperform fully-connected networks for KWS with far fewer parameters — establishing the small-footprint CNN as the architecture family the rest of the field would standardize around.

Zhang, Suda, Lai, and Chandra ("Hello Edge: Keyword Spotting on Microcontrollers", 2017) provide the field's other foundational reference: a systematic architecture-exploration methodology comparing fully-connected, CNN, RNN, convolutional-recurrent, and depthwise-separable-CNN (DS-CNN) designs under microcontroller memory and compute constraints. The DS-CNN architecture it introduces reaches 95.4% accuracy and is the architecture and evaluation methodology later work in this concept implicitly builds on.

Keyword spotting long suffered from the lack of a standard dataset for reproducibly comparing models. Warden (2018) solves this with Speech Commands, a public, crowd-sourced dataset that became the de facto standard, also used in benchmarks like MLPerf Tiny, typically paired with runtimes like TensorFlow Lite Micro and kernels like CMSIS-NN.

Two more recent studies push the field toward a more system-level and more hardware-integrated view. Bartoli et al. (2025) show that the digital-signal-processing stage of the pipeline — extracting MFCC features (Mel-Frequency Cepstral Coefficients, a standard compact representation of audio for speech tasks), not just the neural network itself — is a significant contributor to total pipeline cost, measured across three STM32 microcontroller tiers. Liang et al. (2025) demonstrate a dedicated keyword-spotting accelerator co-designed with the algorithm into a complete audio system-on-chip, validated via a working FPGA-based prototype. A structurally different, neuromorphic-sensor-based approach (Jeziorek et al., 2026) uses an event-driven graph neural network running on an FPGA to spot keywords from an artificial-cochlea event stream rather than a conventional microphone-plus-MFCC pipeline, reaching 95% word-end detection accuracy at 10.53 microsecond latency and 1.18 W — no paper has yet directly compared this event-driven pipeline against the conventional MFCC/CNN pipeline on the same hardware.

## Key papers

[[2015_Sainath_CNNKeywordSpotting]] — shows a small CNN outperforming fully-connected networks for KWS with far fewer parameters, establishing the small-footprint CNN architecture family later standardized on via Speech Commands.

[[2018_Warden_SpeechCommands]] — public dataset and collection methodology for reproducible keyword-spotting benchmarks.

[[2017_Zhang_HelloEdgeKeywordSpottingMCU]] — systematic microcontroller-constrained architecture exploration introducing DS-CNN (95.4% accuracy), one of the two foundational KWS papers this concept's later work builds on.

[[2025_Bartoli_EndToEndKeywordSpotting]] — system-level pipeline benchmark across three STM32 tiers, showing MFCC feature extraction is a significant, often-overlooked contributor to total cost.

[[2025_Liang_IntelligentAudioSoC]] — dedicated keyword-spotting accelerator co-designed into an audio system-on-chip, validated via a working FPGA-based prototype.

[[2018_Flamand_GAP8]] — a RISC-V multi-core cluster with a dedicated convolution engine and an ultra-low-power always-on domain, a hardware platform well suited to always-on keyword spotting.

[[2022_Gerum_HANNAH]] — jointly searches network architecture and hardware accelerator configuration for always-on audio sensing, directly targeting keyword spotting as the motivating use case.

[[2026_Jeziorek_EventAudioGNNKWS]] — a structurally different, neuromorphic-sensor-based approach: event-driven graph neural network hardware (system-on-chip FPGA) for keyword spotting from an artificial-cochlea event stream rather than conventional microphone-plus-MFCC input, reaching 95% word-end detection accuracy at 10.53 microsecond latency and 1.18 W.

## Open problems

Extending equivalent benchmarks to languages other than English with limited data-collection resources. Robustness of models under real acoustic conditions (background noise, distance from microphone), not fully represented by the dataset's recording conditions. How the neuromorphic event-based pipeline compares in accuracy, latency, and energy to the conventional MFCC/CNN pipeline on equivalent hardware — an open cross-pipeline comparison neither side has run yet.

## Research ideas

A dataset version with realistic background noise added synthetically. Multilingual keyword spotting using few-shot techniques for low-resource languages, including Italian.

## Possible thesis topics

Evaluating the robustness of keyword-spotting models trained on Speech Commands when deployed on a microcontroller with real microphones in noisy environments. Extension to an Italian vocabulary.

## Links

[[TensorFlow_Lite_Micro]], [[CMSIS-NN]], [[Cortex-M]]
