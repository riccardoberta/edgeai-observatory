# Distilling the Knowledge in a Neural Network

**Full citation:** Hinton, G., Vinyals, O., Dean, J. (2015). Distilling the Knowledge in a Neural Network. arXiv:1503.02531. https://arxiv.org/abs/1503.02531

**Linked concepts:** [[Distillation]]

## Abstract summary

The authors show how to transfer the knowledge of a large model ("teacher", possibly an ensemble) to a small model ("student") by training the student to mimic the soft probability distributions produced by the teacher, instead of just hard labels, obtaining compact models that are nearly as accurate.

## Research problem

The most accurate models are often large ensembles or very deep networks, too costly to be deployed in production or on devices with limited resources. A way is needed to transfer their predictive capability to smaller models.

## Key idea

Use the teacher's "soft" probabilities (softened by a temperature parameter) as the training signal for the student, because they carry information about which classes are "almost correct" and not just about the right one — a much richer signal than hard labels.

## Technical contribution

Formulation of the distillation loss based on temperature-scaled softmax; demonstration that a single small model can approximate the performance of an ensemble; introduction of the concept of "dark knowledge" contained in soft probabilities.

## Experimental methodology

Experiments on MNIST and on an internal Google speech recognition task, comparing the student trained with distillation against the same student trained only on hard labels, and against the original teacher/ensemble.

## Results

The distilled student recovers most of the accuracy gap relative to the teacher, despite having a fraction of the parameters; in one case the student achieves performance nearly indistinguishable from an ensemble of many models.

## Comparison with the state of the art

At the time, it represented a more effective alternative to simply training the small model directly on the original data, and is conceptually different from pruning/quantization because it does not compress an existing model but transfers knowledge to a new architecture.

## Strengths

Simple, general idea, independent of teacher and student architecture; it has become a standard tool combinable with quantization and pruning.

## Weaknesses

Requires access to the teacher during student training (additional computational cost); choosing the temperature and the weight between hard and soft loss requires tuning.

## Limitations

The original experiments are on relatively small tasks (MNIST, speech); effectiveness on very heterogeneous teacher-student architecture pairs (e.g. Transformer-to-CNN) is not covered.

## Open questions

How well does distillation work when the capacity gap between teacher and student is very large? How to automatically choose temperature and loss weight?

## Possible extensions

Self-distillation (a model distilling itself); progressive distillation through multiple students of decreasing size; combination with quantization-aware training for models to be deployed on microcontrollers.

## Relevance to our research

A technique complementary to quantization and pruning in the edge compression pipeline: useful when redesigning the architecture, not just compressing the existing one.

## Possible thesis topics

Distillation from large Transformer models to compact CNNs/RNNs for inference on Cortex-M; study of the interaction between distillation and quantization-aware training.

## Possible collaborations

Groups working on compact language models for edge and on NAS, where distillation is often used to guide the search for the student architecture.

## Links to related papers

[[2016_Han_DeepCompression]], [[2017_Jacob_QuantizationIntegerOnlyInference]]
