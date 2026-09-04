# Continual Learning

A network trained sequentially on new tasks tends to overwrite what it learned on earlier ones — a failure mode known as *catastrophic forgetting*. Continual (or "lifelong") learning is the study of how to keep learning from new data without losing old capability. For EdgeAI specifically, it is the natural counterpart to [[On-device_Learning]]: a device that keeps adapting from local data over its deployed lifetime needs some way to avoid forgetting earlier-learned behavior, especially since it usually cannot afford to store a full history of raw data to "remind" itself.

## Evolution of the concept

Two early approaches defined the field's main paradigms. Kirkpatrick et al. (2017) introduce Elastic Weight Consolidation (EWC): using the Fisher Information Matrix (a measure of how sensitive a model's output is to changes in each weight) to estimate how important each weight is to previously learned tasks, then penalizing large changes to important weights when learning something new — without needing to store any old training data. EWC became a reference point for the whole field, though later work has shown its importance estimate can become inaccurate over long sequences of tasks. Rebuffi et al.'s iCaRL (2017) takes a different, memory-based approach: it keeps a small set of stored examples ("exemplars") from earlier tasks and combines them with knowledge distillation, learning the data representation and the classifier jointly rather than assuming a fixed feature extractor.

Lopez-Paz and Ranzato's Gradient Episodic Memory (GEM, NeurIPS 2017) reformulates continual learning as a constrained optimization problem: new-task gradient updates are only allowed in directions that do not increase loss on a small stored sample of previous tasks' data. Notably, GEM demonstrates *positive backward transfer* — learning a new task can actually improve performance on earlier ones — an evaluation dimension that is now standard in the field.

A more recent direction, motivated by sensor-data privacy, replaces gradient-based incremental updates with closed-form analytic ones: TS-ACL (Li et al., 2024) reformulates class-incremental updates for time-series classification as a recursive least-squares computation over a frozen embedding, avoiding both raw-data replay and the forgetting that iterative fine-tuning is prone to.

Two lines of work bring continual learning specifically to TinyML-class hardware. Ravaglia et al. (IEEE JETCAS, 2021) validate *quantized latent replay* end to end on real embedded hardware (GAP8-class, see [[RISC-V]]) within under 64 MB of memory: instead of storing raw exemplars, the method stores compact, low-bitwidth intermediate activations — directly bridging this concept with [[Quantization]] and giving it its first hardware-validated (not simulated) anchor. Rüb et al. (2024) tackle the same memory-budget problem from a different angle, purpose-built for microcontroller-class deployment: rather than protecting weight importance (EWC) or replaying exemplars (iCaRL), they distill prior-task data into a compact synthetic dataset cheap enough to retain within microcontroller memory, paired with a mechanism that grows the network as new classes are added.

## Key papers

[[2017_Kirkpatrick_OvercomingCatastrophicForgetting]] — Elastic Weight Consolidation, a Fisher-Information-based regularization method that mitigates catastrophic forgetting without retaining old data.

[[2017_LopezPaz_GradientEpisodicMemory]] — GEM: constrained-optimization continual learning using a small stored exemplar sample, with positive backward transfer; one of the two foundational early paradigms alongside EWC.

[[2021_Ravaglia_TinyMLContinualLearningLatentReplays]] — quantized latent replay for TinyML continual learning, validated on real embedded hardware within under 64 MB of memory; this concept's first hardware-validated, replay-based anchor.

[[2017_Rebuffi_iCaRL]] — class-incremental learning combining a small exemplar memory with knowledge distillation; a memory-based approach complementary to EWC's regularization-based one.

[[2024_Li_TSACL]] — closed-form, recursive analytic-learning update for class-incremental time-series classification, avoiding raw-data replay.

[[2024_Rub_ContinualIncrementalTinyML]] — TinyML-specific incremental learning combining dataset distillation (a compact synthetic memory) with model-size adaptation, targeting genuinely memory-constrained embedded devices.

## Open problems

Detecting task boundaries automatically in continuous, drifting data streams, rather than assuming known task switches, as classic EWC does. Making importance-estimation methods (Fisher-based or otherwise) cheap enough to fit the memory budgets of MCU-class on-device learning. Avoiding degraded protection from EWC-style methods over very long sequences of tasks.

## Research ideas

A memory-budgeted continual-learning method designed jointly with the memory constraints of [[On-device_Learning]] — for example combining sparse weight updates with importance-weighted protection under one fixed memory envelope. Task-boundary-free continual learning for always-on sensors (audio, inertial-measurement-unit, biosignals) where drift is gradual rather than discrete.

## Possible thesis topics

An empirical study of catastrophic forgetting in a real always-on EdgeAI application as the deployment environment drifts over weeks or months — for example keyword spotting or Human Activity Recognition under changing acoustic or usage conditions. A lightweight, MCU-feasible approximation of Fisher-based importance estimation.

## Links

[[On-device_Learning]], [[Federated_Learning]]
