# Distillation

Knowledge distillation trains a small "student" model to reproduce the behavior of a larger, more accurate "teacher" model, so the student inherits some of the teacher's accuracy at a fraction of its size. Unlike [[Pruning]] or [[Quantization]], distillation does not shrink an existing model directly — it transfers what a large model has learned into a new, smaller architecture — which makes it complementary to those other compression techniques rather than a substitute for them.

## Evolution of the concept

The core idea predates the current wave of deep learning: Bucilă, Caruana, and Niculescu-Mizil's "Model Compression" (KDD 2006) already showed that a large, complex ensemble's predictions could train a single, much smaller and faster model that approximates the ensemble's behavior. Hinton, Vinyals, and Dean (2015) reframe and popularize this idea for deep networks specifically, introducing a temperature-scaled softmax loss that transfers the "soft" probabilities of a large teacher model — which carry more information than hard labels alone, sometimes called "dark knowledge" — to a small student model.

For generative large language models, the standard distillation objective (minimizing forward KL divergence, a measure of how one probability distribution differs from another) tends to make the student over-estimate low-probability regions of the teacher's output distribution. MiniLLM (Gu et al., ICLR 2024) addresses this by minimizing *reverse* KL divergence instead, optimized via policy-gradient reinforcement learning, producing higher-quality open-ended text generation than forward-KL-distilled students of the same size.

Distillation's benefits are not limited to a one-off offline compression step. Barranco (2024) shows this in an edge-cloud activity-monitoring system for long-term care facilities: distilling the recognition network for edge deployment is paired with a runtime resource-management layer that dynamically reconfigures which distilled variant runs on which node, boosting recognition performance by up to 8% with no added resource cost — evidence that distillation's gains compound with system-level orchestration, not just with the distillation method itself.

Two further techniques extend distillation's reach. Lopes et al. (2017) address a genuine deployment constraint — compressing a model when the original training data is unavailable — by reconstructing synthetic training data from lightweight activation statistics recorded during the teacher's original training, a technique known as data-free distillation. Suwannaphong et al. (2025) combine distillation with quantization across both Transformer and the newer Mamba/state-space-model architecture family (an alternative to attention-based transformers, built around a recurrent-style sequence model) for an indoor-localization task.

## Key papers

[[2006_Bucila_ModelCompression]] — original demonstration that a large ensemble's predictions can train a single compact model that mimics its behavior, predating and foreshadowing modern knowledge distillation.

[[2015_Hinton_DistillingKnowledge]] — original formulation of the distillation loss and the "dark knowledge" concept.

[[2024_Gu_MiniLLM]] — reverse-KL, policy-gradient-based distillation objective tailored to generative LLMs, addressing a mismatch in standard forward-KL distillation.

[[2024_Barranco_EdgeCloudActivityDistillation]] — edge-cloud video activity-monitoring system pairing knowledge distillation with a runtime resource-management tool that dynamically reconfigures which distilled model variant runs per edge node.

[[2017_Lopes_DataFreeKnowledgeDistillation]] — distills without access to the original training data, using activation statistics recorded during the teacher's original training to synthesize replacement training data.

[[2025_Suwannaphong_TinyMLQuantizationDistillationIndoorLocalisation]] — joint quantization-plus-distillation compression compared across Transformer and Mamba (state-space-model) architectures for edge indoor localization.

## Open problems

How effective distillation remains when the capacity gap between teacher and student is very large. Automatic choice of the temperature parameter and the weighting between hard-label and soft-label loss, both still largely set by trial and error today.

## Research ideas

Progressive self-distillation through multiple students of decreasing size, down to a size compatible with a Cortex-M microcontroller. Combining distillation and quantization-aware training within the same training pipeline rather than as two separate stages.

## Possible thesis topics

Distillation from large Transformer models to compact CNNs/RNNs for inference on a microcontroller. A study of the interaction between distillation and quantization-aware training.

## Links

[[Quantization]], [[Pruning]], [[NAS]]
