# MiniLLM: Knowledge Distillation of Large Language Models

**Full citation:** Gu, Y., Dong, L., Wei, F., Huang, M. (2024). MiniLLM: Knowledge Distillation of Large Language Models. Proceedings of ICLR 2024. https://arxiv.org/abs/2306.08543

**Linked concepts:** [[Distillation]]

## Abstract summary

The authors (Tsinghua University, Microsoft Research) propose MiniLLM, a knowledge-distillation method for compressing large generative language models into smaller student models by replacing the standard forward Kullback-Leibler divergence training objective with a reverse-KL objective optimized via policy-gradient reinforcement learning, better suited to the open-ended, generative nature of LLM outputs.

## Research problem

Standard knowledge-distillation objectives (forward KL divergence) were developed for classification-style teacher-student setups and tend to make the student over-estimate low-probability regions of the teacher's output distribution in open-ended text generation, producing students that hallucinate or generate low-quality long-form text.

## Key idea

Minimizing the reverse KL divergence (student-to-teacher direction) instead of the forward KL divergence better matches the mode-seeking behavior needed for high-quality generative text, but reverse KL cannot be optimized directly with standard supervised gradient descent for autoregressive generation, so the authors formulate it as a policy-gradient reinforcement-learning problem with techniques to stabilize training (single-step regularization, teacher-mixed sampling, length normalization).

## Technical contribution

The reverse-KL distillation objective for generative LLMs; a policy-gradient-based optimization procedure with specific stabilization techniques to make this objective trainable in practice at LLM scale.

## Experimental methodology

Distillation experiments from LLaMA/GPT-2-family teacher models (up to 13B parameters) into smaller student models (120M-1.3B+ parameters), evaluated on instruction-following and open-ended generation benchmarks using both automatic metrics and human/GPT-4-based evaluation, compared against standard forward-KL sequence-level distillation baselines.

## Results

MiniLLM-distilled students produce more precise, higher-quality, and more diverse responses than forward-KL-distilled baselines of the same size, with lower exposure bias and better generalization to held-out instruction-following tasks, while maintaining good scalability across teacher/student size combinations.

## Comparison with the state of the art

Distinguishes itself from classic distillation work (Hinton-style and sequence-level KD) by directly addressing the mismatch between distillation objective and the generative, open-ended nature of LLM outputs, rather than re-applying classification-era objectives to generation tasks.

## Strengths

Principled reformulation of the distillation objective grounded in the mode-seeking-versus-mode-covering distinction between reverse and forward KL; demonstrated at meaningful LLM scale; consistent gains across multiple teacher/student size pairs.

## Weaknesses

The policy-gradient training procedure is more complex and less stable to implement than standard supervised distillation losses, requiring several stabilization tricks.

## Limitations

Evaluated on server/GPU-class teacher and student models; the smallest students studied (~120M parameters) are still larger than what fits on microcontroller-class hardware, so direct applicability to the smallest EdgeAI targets requires further compression.

## Open questions

Can the reverse-KL objective be combined effectively with quantization or pruning of the student to reach microcontroller-class model sizes? How sensitive are the stabilization techniques to teacher/student architecture mismatch?

## Possible extensions

Combining MiniLLM-style reverse-KL distillation with post-training quantization (e.g. AWQ) to produce small, deployable instruction-following models for edge GPU/NPU targets.

## Relevance to our research

Representative of the 2023-2024 shift in [[Distillation]] research toward compressing generative large language models rather than only classification CNNs, relevant to on-device LLM deployment as an emerging EdgeAI direction.

## Possible thesis topics

Studying how far reverse-KL-style distillation can shrink a generative language model while retaining acceptable instruction-following quality on edge GPU/NPU hardware.

## Possible collaborations

Groups working on LLM compression and on RL-based training stabilization for sequence models.

## Links to related papers

[[2006_Bucila_ModelCompression]], [[2024_Lin_AWQ]]
