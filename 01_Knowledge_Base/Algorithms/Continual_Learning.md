# Continual Learning

## Evolution of the concept

Neural networks trained sequentially on new tasks tend to overwrite what they learned before — catastrophic forgetting. Kirkpatrick et al. (2017) introduce Elastic Weight Consolidation (EWC), which estimates the importance of each weight to previously learned tasks (via the Fisher Information Matrix) and penalizes large changes to important weights when learning something new, without needing to store old training data. EWC became a reference point for the whole continual/lifelong-learning subfield, though later work has shown its Fisher-based importance estimate can be inaccurate over long task sequences, motivating refinements. For EdgeAI specifically, continual learning is the natural counterpart to [[On-device_Learning]]: a device that adapts from local data over its deployed lifetime needs some mechanism to avoid forgetting earlier-learned behavior, especially since it usually cannot afford to store a full history of raw data.

## Key papers

[[2017_Kirkpatrick_OvercomingCatastrophicForgetting]] — Elastic Weight Consolidation, a Fisher-Information-based regularization method that mitigates catastrophic forgetting without retaining old data.

## Open problems

Detecting task boundaries automatically in continuous, drifting data streams (rather than assuming known task switches, as classic EWC does). Making importance-estimation methods (Fisher-based or otherwise) cheap enough to fit the memory budgets of MCU-class on-device learning. Avoiding "EWC drift" / degraded protection over very long sequences of tasks.

## Research ideas

A memory-budgeted continual-learning method designed jointly with the memory constraints of [[On-device_Learning]] (e.g. combining Sparse Update with importance-weighted protection under one fixed memory envelope); task-boundary-free continual learning for always-on sensors (audio, IMU, biosignals) where drift is gradual rather than discrete.

## Possible thesis topics

Empirical study of catastrophic forgetting in a real always-on EdgeAI application as the deployment environment drifts over weeks or months (e.g. keyword spotting or HAR under changing acoustic/usage conditions); a lightweight, MCU-feasible approximation of Fisher-based importance estimation.

## Links

[[On-device_Learning]], [[Federated_Learning]]
