# Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition

**Full citation:** Warden, P. (2018). Speech Commands: A Dataset for Limited-Vocabulary Speech Recognition. arXiv:1804.03209. https://arxiv.org/abs/1804.03209

**Linked concepts:** [[Keyword Spotting]]

## Abstract summary

The author (Google) presents Speech Commands, a public dataset of short spoken words (commands like "yes," "no," "stop," "go") designed specifically to train and evaluate limited-vocabulary keyword spotting systems, with a methodology for collecting and validating recordings in a reproducible way.

## Research problem

There was no standard, public dataset of adequate size for fairly comparing different keyword spotting models intended for "always-on" embedded devices (e.g. low-power voice assistants), making it hard to compare results across different papers.

## Key idea

Collect a very large number of short audio clips of single words spoken by thousands of different volunteers, using a crowd-sourced collection and validation procedure, organized so that standard reproducible benchmarks for limited-vocabulary recognition can be defined.

## Technical contribution

A public dataset with documented collection methodology; a standard split into training/validation/test that allows fair comparisons across different papers; baseline results reported in the paper.

## Experimental methodology

Description of the collection pipeline (recording via a web app, validation through cross-checking between annotators) and training of baseline models (small CNNs/RNNs) on the dataset, reporting accuracy as a reference for future comparisons.

## Results

The dataset, in its later versions, becomes the de facto standard benchmark for keyword spotting in the TinyML community, also used as one of the reference tasks in MLPerf Tiny.

## Comparison with the state of the art

Before this dataset, keyword spotting papers often used proprietary, non-comparable datasets; Speech Commands solves the reproducibility and comparability problem.

## Strengths

Wide adoption as a standard benchmark; size and speaker diversity adequate for training robust models; later updates (v2) expanded the vocabulary.

## Weaknesses

Limited, English-only vocabulary: generalization to multilingual keyword spotting or to different vocabularies requires additional datasets (indeed an open research area, "few-shot keyword spotting in any language").

## Limitations

Recording conditions (background noise, microphones) may not fully represent the real deployment conditions of an always-on embedded device in noisy environments.

## Open questions

How to extend equivalent benchmarks to languages other than English with limited data-collection resources? How well do models that perform well on this dataset behave under real acoustic conditions (noise, distance from microphone)?

## Possible extensions

Versions of the dataset with realistic background noise added synthetically; extension to multilingual keyword spotting using few-shot techniques.

## Relevance to our research

A reference dataset for any keyword spotting experiment on microcontrollers; used together with TensorFlow Lite Micro and CMSIS-NN in standard TinyML benchmarks.

## Possible thesis topics

Evaluating the robustness of keyword spotting models trained on Speech Commands when deployed on a microcontroller with real microphones in noisy environments; extension to an Italian vocabulary with limited collection resources.

## Possible collaborations

The MLPerf Tiny and TinyML Foundation communities that maintain benchmarks based on this dataset.

## Links to related papers

[[2021_David_TensorFlowLiteMicro]], [[2018_Lai_CMSIS-NN]]
