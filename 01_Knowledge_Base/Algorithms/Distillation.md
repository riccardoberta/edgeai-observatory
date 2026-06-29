# Distillation

## Evolution of the concept

Hinton, Vinyals, and Dean (2015) introduce the idea that the "soft" probabilities produced by a large model (teacher) carry more information than hard labels alone, and that this information ("dark knowledge") can be transferred to a small model (student) via a temperature-scaled softmax loss. Unlike pruning and quantization, distillation does not compress an existing model but transfers knowledge to a new architecture, making it complementary to the other compression techniques.

## Key papers

[[2015_Hinton_DistillingKnowledge]] — original formulation of the distillation loss and the dark-knowledge concept.

## Open problems

Effectiveness of distillation when the capacity gap between teacher and student is very large. Automatic choice of temperature and weight between hard and soft loss, still largely empirical today.

## Research ideas

Progressive self-distillation through multiple students of decreasing size, down to a size compatible with Cortex-M; combining distillation and quantization-aware training in the same training pipeline.

## Possible thesis topics

Distillation from large Transformer models to compact CNNs/RNNs for inference on a microcontroller; study of the interaction between distillation and QAT.

## Links

[[Quantization]], [[Pruning]], [[NAS]]
