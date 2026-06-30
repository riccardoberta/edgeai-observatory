# ML-driven Hardware Cost Model for MLIR

**Full citation:** Das, D., Mannarswamy, S. (2023). ML-driven Hardware Cost Model for MLIR. Proceedings of ICLR 2023. https://arxiv.org/abs/2302.11405

**Linked concepts:** [[MLIR]]

## Abstract summary

The authors propose a machine-learning-based hardware cost model for high-level MLIR representations, treating the incoming MLIR code as a text input (analogous to NLP modeling) and applying NLP-style modeling techniques to predict hardware-relevant target variables such as CPU/GPU/xPU utilization, instructions executed, and register usage, intended to guide compiler optimization passes.

## Research problem

Deep learning compilers built on MLIR need accurate hardware-cost estimates to guide graph-level optimizations (operator fusion, memory allocation, kernel scheduling) and kernel-level optimizations (loop interchange, loop-invariant code motion, unrolling), but building accurate, generalizable hardware-cost models for arbitrary MLIR code traditionally requires hand-engineered, hardware-specific heuristics that do not transfer well across targets.

## Key idea

Treat MLIR code as a sequence-modeling problem analogous to natural language text, and apply modern NLP-style sequence models to learn a hardware-cost predictor directly from MLIR representations, replacing hand-engineered hardware-specific cost heuristics with a learned, potentially more generalizable model.

## Technical contribution

A learned, NLP-inspired hardware-cost model operating directly on MLIR text representations; demonstrated prediction of multiple hardware-relevant target variables (utilization, instruction counts, register usage) useful for guiding both graph-level and kernel-level compiler optimization decisions.

## Experimental methodology

Training and evaluation of the learned cost model on MLIR code samples, measuring prediction accuracy for the various hardware-cost target variables, and discussing how the resulting predictions could guide specific compiler optimization passes (operator fusion, memory allocation, loop transformations).

## Results

The learned, NLP-inspired cost model produces useful predictions for the studied hardware-cost variables directly from MLIR text, suggesting that sequence-modeling approaches developed for NLP can be repurposed effectively for compiler cost modeling without extensive hand-engineered hardware-specific features.

## Comparison with the state of the art

Distinguishes itself from traditional, hand-engineered hardware-cost heuristics used in compiler optimization passes by applying a learned, text-sequence-modeling approach directly to MLIR, following the same general philosophy as ML-driven compiler optimization research but applied specifically within the MLIR ecosystem.

## Strengths

Conceptually elegant reuse of mature NLP sequence-modeling techniques for a compiler-infrastructure problem; demonstrated within the actively-developed MLIR ecosystem at a top-tier venue (ICLR 2023).

## Weaknesses

As with most learned cost models, generalization to MLIR code substantially different from the training distribution (different hardware targets, very different code patterns) is not guaranteed and would need further validation.

## Limitations

The evaluation centers on cost-prediction accuracy rather than on demonstrating end-to-end compiler optimization gains (e.g. measured speedup) resulting from using the learned cost model in a real optimization pipeline.

## Open questions

Does using this learned cost model in an actual MLIR-based compiler optimization pipeline yield measurable end-to-end speedups on real EdgeAI hardware targets (Cortex-M, RISC-V, NPU)? How well does the model transfer to hardware targets not seen during training?

## Possible extensions

Integrating the learned cost model into an MLIR-based deployment pipeline targeting our Hardware taxonomy's MCU-class targets, and measuring real end-to-end optimization gains rather than only cost-prediction accuracy.

## Relevance to our research

Relevant to the [[MLIR]] compiler-infrastructure line of research as an example of applying learned models to compiler optimization decisions, complementary to hand-engineered approaches like Hexagon-MLIR's NPU-specific passes.

## Possible thesis topics

Evaluating whether a learned, MLIR-text-based cost model can guide real optimization decisions for a microcontroller-class deployment pipeline, measuring end-to-end latency/energy gains against a baseline without the learned cost model.

## Possible collaborations

Groups working on ML-for-compilers research and on MLIR-based deployment pipelines for edge hardware.

## Links to related papers

[[2004_Lattner_LLVM]], [[2026_Absar_HexagonMLIR]]
