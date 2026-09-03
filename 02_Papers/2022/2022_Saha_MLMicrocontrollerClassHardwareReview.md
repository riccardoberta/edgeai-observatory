# Machine Learning for Microcontroller-Class Hardware: A Review

**Full citation:** Saha, S.S., Sandha, S.S., Srivastava, M. (2022). Machine Learning for Microcontroller-Class Hardware: A Review. IEEE Sensors Journal, 22(22), 21362-21390. DOI: 10.1109/JSEN.2022.3210773. arXiv:2205.14550.

**PDF:** [arXiv](https://arxiv.org/abs/2205.14550)

**Verification note:** Bibliographic details confirmed via WebSearch (arXiv, PubMed, eScholarship UC). Abstract-level verified.

**Linked concepts:** [[On-device_Learning]]

## Abstract summary

A broad, systematic review of the entire machine-learning-on-microcontrollers landscape — covering model design, compression, runtime frameworks, hardware platforms, and including a dedicated treatment of on-device training/fine-tuning approaches — positioned as a general entry point to the field this KB organizes its Algorithms and Frameworks branches around.

## Research problem

By 2022 the MCU-class ML literature had grown across many independent threads (compression, runtime design, hardware co-design, on-device training) without a single review connecting them as one coherent deployment pipeline.

## Key idea

Review the full MCU-class ML pipeline end-to-end — algorithm, compression, runtime, hardware — as one connected system, with on-device learning/adaptation (fine-tuning and continual updates using online learning frameworks) as one first-class pipeline stage rather than an afterthought.

## Technical contribution

A structured, full-pipeline review of MCU-class ML, with explicit coverage of on-device training and federated learning as mechanisms for periodic model adaptation to account for data distribution shifts — directly relevant to this KB's On-device_Learning concept.

## Experimental methodology

Literature survey and synthesis, not a novel empirical study.

## Results

A widely-cited (360+) general reference for the entire MCU-class ML field, frequently used as an entry point by researchers new to TinyML deployment.

## Comparison with the state of the art

Complements this KB's more narrowly-scoped On-device_Learning anchors ([[2022_Lin_OnDeviceTraining256KB]], [[2024_Kwon_TinyTrain]]) by situating on-device training within the full deployment pipeline (compression, runtime, hardware) rather than treating it in isolation.

## Strengths

Broad, well-cited, recent enough (2022) to include the early on-device-training wave; explicitly connects on-device learning to the surrounding pipeline (compression choices affect what training is feasible, runtime choices affect what update mechanisms are possible).

## Weaknesses

As a broad review, treats on-device training relatively briefly compared to dedicated papers like [[2022_Lin_OnDeviceTraining256KB]]; published 2022, predates [[2024_Kwon_TinyTrain]] and more recent sparse-update training work.

## Limitations

No new empirical results of its own; broad scope means depth on any single sub-topic (including on-device learning) is necessarily limited.

## Open questions

How has the on-device-training slice of this review's full-pipeline framing evolved since 2022, given the subsequent TinyTrain (2024) and quantized full-training-loop (2024) work already in this KB?

## Possible extensions

An updated version of this review's on-device-training section specifically, incorporating TinyTrain-class meta-learning approaches and fully-quantized training loops published since 2022.

## Relevance to our research

The broad, high-citation entry-point review for the entire MCU-class ML field this KB's Algorithms and Frameworks branches organize around, with on-device learning as one explicit pipeline stage — a natural general anchor missing from this KB's On-device_Learning concept.

## Possible thesis topics

Updating this review's full-pipeline framing (algorithm/compression/runtime/hardware) with 2023-2026 developments already tracked individually across this KB, producing a single current synthesis.

## Possible collaborations

Groups working on the full TinyML deployment pipeline, not just individual pipeline stages (UCLA).

## Links to related papers

[[2022_Lin_OnDeviceTraining256KB]], [[2024_Kwon_TinyTrain]]
