# Keyword Spotting

## Evolution of the concept

Keyword spotting (recognizing short keywords on "always-on" low-power devices) long suffered from the lack of a standard dataset for reproducibly comparing models. Warden (2018) solves the problem with Speech Commands, a public crowd-sourced dataset that became the de facto standard, also used in benchmarks like MLPerf Tiny, typically paired with runtimes like TensorFlow Lite Micro and kernels like CMSIS-NN.

## Key papers

[[2018_Warden_SpeechCommands]] — public dataset and collection methodology for reproducible keyword spotting benchmarks.

## Open problems

Extending equivalent benchmarks to languages other than English with limited data-collection resources. Robustness of models under real acoustic conditions (background noise, distance from microphone), not fully represented by the dataset's recording conditions.

## Research ideas

A dataset version with realistic background noise added synthetically; multilingual keyword spotting using few-shot techniques for low-resource languages, including Italian.

## Possible thesis topics

Evaluating the robustness of keyword spotting models trained on Speech Commands when deployed on a microcontroller with real microphones in noisy environments; extension to an Italian vocabulary.

## Links

[[TensorFlow Lite Micro]], [[CMSIS-NN]], [[Cortex-M]]
