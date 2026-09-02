# Distillation

## Evolution of the concept

The core idea predates deep learning's current wave: Bucilă, Caruana, and Niculescu-Mizil's "Model Compression" (KDD 2006) already showed that a large, complex ensemble's predictions could be used to train a single, much smaller and faster model that approximates the ensemble's behavior. Hinton, Vinyals, and Dean (2015) reframe and popularize this idea for deep networks, introducing the temperature-scaled softmax loss to transfer the "soft" probabilities of a large model (teacher) — carrying more information than hard labels alone ("dark knowledge") — to a small model (student). Unlike pruning and quantization, distillation does not compress an existing model but transfers knowledge to a new architecture, making it complementary to the other compression techniques. For generative large language models, the standard forward-KL distillation objective tends to make the student over-estimate low-probability regions of the teacher's distribution; MiniLLM (Gu et al., ICLR 2024) addresses this by minimizing reverse KL divergence instead, optimized via policy-gradient reinforcement learning, producing higher-quality open-ended generation than forward-KL-distilled students of the same size. A 2024 MDPI Electronics paper (Barranco) shows distillation's role extending beyond a one-off offline compression step: in an edge-cloud activity-monitoring system for long-term care facilities, distilling the recognition network for edge deployment is paired with a runtime resource-management layer that dynamically reconfigures which distilled variant runs per node, boosting recognition performance by up to 8% without added resource cost — evidence that distillation gains compound with system-level orchestration, not just with the distillation method itself.

## Key papers

[[2006_Bucila_ModelCompression]] — original demonstration that a large ensemble's predictions can train a single compact model that mimics its behavior, predating and foreshadowing modern knowledge distillation.

[[2015_Hinton_DistillingKnowledge]] — original formulation of the distillation loss and the dark-knowledge concept.

[[2024_Gu_MiniLLM]] — reverse-KL, policy-gradient-based distillation objective tailored to generative LLMs, addressing the mode-covering/mode-seeking mismatch of standard forward-KL distillation.

[[2024_Barranco_EdgeCloudActivityDistillation]] — edge-cloud video activity-monitoring system pairing knowledge distillation with a runtime resource-management tool that dynamically reconfigures which distilled model variant runs per edge node.

## Open problems

Effectiveness of distillation when the capacity gap between teacher and student is very large. Automatic choice of temperature and weight between hard and soft loss, still largely empirical today.

## Research ideas

Progressive self-distillation through multiple students of decreasing size, down to a size compatible with Cortex-M; combining distillation and quantization-aware training in the same training pipeline.

## Possible thesis topics

Distillation from large Transformer models to compact CNNs/RNNs for inference on a microcontroller; study of the interaction between distillation and QAT.

## Links

[[Quantization]], [[Pruning]], [[NAS]]
