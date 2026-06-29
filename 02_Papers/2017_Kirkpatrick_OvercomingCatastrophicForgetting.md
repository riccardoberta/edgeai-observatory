# Overcoming Catastrophic Forgetting in Neural Networks

**Full citation:** Kirkpatrick, J., Pascanu, R., Rabinowitz, N., Veness, J., Desjardins, G., Rusu, A. A., Milan, K., Quan, J., Ramalho, T., Grabska-Barwinska, A., Hassabis, D., Clopath, C., Kumaran, D., Hadsell, R. (2017). Overcoming Catastrophic Forgetting in Neural Networks. *Proceedings of the National Academy of Sciences (PNAS)*, 114(13), 3521–3526. arXiv:1612.00796. https://arxiv.org/abs/1612.00796

**Linked concepts:** [[Continual_Learning]], [[On-device_Learning]]

## Abstract summary

The authors (DeepMind) introduce Elastic Weight Consolidation (EWC), a regularization technique inspired by synaptic consolidation in biological brains, that lets a neural network learn new tasks sequentially while retaining performance on previously learned tasks, by selectively slowing down learning on weights identified as important for earlier tasks.

## Research problem

Standard neural networks trained sequentially on new tasks suffer from catastrophic forgetting: gradient updates for a new task overwrite the weights that encoded knowledge from previous tasks, destroying earlier performance. This conflicts with any setting where a model must keep learning over its deployed lifetime without revisiting all past data (the basic premise of continual/lifelong learning, and a precondition for adaptive EdgeAI devices).

## Key idea

Estimate, via the diagonal of the Fisher Information Matrix, how important each weight was to performance on previous tasks, then add a quadratic penalty to the loss when training on a new task that discourages large changes to the weights with high estimated importance — allowing less important weights to adapt freely while protecting the ones that matter for earlier tasks.

## Technical contribution

Formalization of EWC's loss function combining the new-task loss with a Fisher-weighted quadratic penalty relative to the previous task's optimal parameters; empirical validation that this single mechanism, without storing or replaying old data, substantially mitigates catastrophic forgetting across multiple sequential-task settings.

## Experimental methodology

Evaluated on sequential supervised learning (permuted/sequential MNIST-style task sequences) and on sequential reinforcement learning across multiple Atari games, measuring retained performance on earlier tasks as new tasks are learned, compared against plain sequential fine-tuning (no protection) and other baselines.

## Results

EWC substantially reduces performance degradation on earlier tasks compared to naive sequential training, while still allowing the network to reach good performance on new tasks, demonstrated across both supervised and reinforcement learning sequential-task benchmarks.

## Comparison with the state of the art

At publication, EWC was one of the first practical, scalable answers to catastrophic forgetting that did not require storing raw data from previous tasks (unlike replay-based methods), making it attractive for memory- or privacy-constrained deployments — though later work (including more recent 2026 papers re-examining EWC, e.g. arXiv:2603.18596) shows its Fisher-based importance estimate can be inaccurate or prone to gradient vanishing in some regimes, motivating refinements.

## Strengths

No need to retain old training data (important where storage or privacy is a constraint, as in EdgeAI); simple to add on top of existing training pipelines; broad applicability across supervised and reinforcement learning settings; strong influence on the whole continual-learning subfield.

## Weaknesses

The Fisher Information estimate is a diagonal (factorized) approximation that can misjudge true parameter importance, especially over many sequential tasks ("EWC drift"); performance tends to degrade as the number of sequential tasks grows; the approach does not address the harder problem of detecting task boundaries when they are not explicitly given.

## Limitations

Assumes discrete, known task boundaries (a "task ID" or clear switch point), which doesn't match many real-world streaming-data scenarios; was not evaluated under the extreme memory and compute constraints typical of microcontroller-class EdgeAI hardware — its quadratic penalty still requires storing per-weight importance estimates, an extra memory cost not accounted for in the original paper.

## Open questions

How should importance-weighted regularization be adapted when memory itself (not just forgetting) is the binding constraint, as on MCUs? Can EWC-style protection be combined with the kind of sparse, memory-budgeted updates introduced in [[2022_Lin_OnDeviceTraining256KB]] without requiring full per-weight importance storage? How to handle task-boundary-free, continuously drifting data streams typical of always-on sensors?

## Possible extensions

Memory-efficient approximations of Fisher-based importance suitable for MCU-class on-device learning; combining EWC-style regularization with the Sparse Update mechanism of [[2022_Lin_OnDeviceTraining256KB]] so that "important" weights are both protected from forgetting and prioritized for limited training memory.

## Relevance to our research

Foundational paper for the [[Continual_Learning]] concept and a natural complement to [[On-device_Learning]]: any EdgeAI device that adapts over its lifetime (rather than being fine-tuned once) needs some mechanism like EWC to avoid forgetting earlier-learned behavior, especially since storing raw historical data on a constrained device is often infeasible.

## Possible thesis topics

A memory-budgeted variant of EWC designed for MCU-class on-device continual learning (combining importance-weighted regularization with a fixed memory budget for the importance estimates themselves); empirical study of catastrophic forgetting in a real always-on EdgeAI application (e.g. keyword spotting or HAR) as the operating environment drifts over weeks/months.

## Possible collaborations

Groups working on continual/lifelong learning theory; potential overlap with [[Federated_Learning]] research given that federated clients effectively face a sequential, non-stationary-data problem similar to continual learning.

## Links to related papers

[[2022_Lin_OnDeviceTraining256KB]] (memory-constrained on-device training, a natural pairing for memory-aware continual learning), [[2017_McMahan_FederatedAveraging]] (sequential, non-IID learning across clients shares structural similarities with continual learning across tasks)
