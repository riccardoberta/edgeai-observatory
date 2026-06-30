# Optimal Brain Damage

**Full citation:** LeCun, Y., Denker, J.S., Solla, S.A. (1990). Optimal Brain Damage. *Advances in Neural Information Processing Systems 2 (NeurIPS 1989/1990)*. https://proceedings.neurips.cc/paper/1989/file/6c9882bbac1c7093bd25041881277658-Paper.pdf

**Linked concepts:** [[Pruning]], [[Compression]]

## Abstract summary

The authors propose using second-order derivative information (an approximation of the Hessian of the loss with respect to the weights) to estimate the increase in training error caused by removing each weight, and use this "saliency" measure to decide which weights to prune from a trained network.

## Research problem

Naively removing weights from a trained network (e.g. by magnitude alone) can damage accuracy unpredictably, and retraining a smaller architecture from scratch is expensive; a principled way is needed to decide which weights matter least to the network's function.

## Key idea

Use a local quadratic (second-order Taylor) approximation of the loss surface around the trained weights to estimate, for each weight, how much training error would increase if that weight were set to zero — its "saliency" — and prune the lowest-saliency weights first.

## Technical contribution

A diagonal approximation of the Hessian (ignoring cross-terms between weights) that makes the saliency calculation tractable for networks of the era; an iterative prune-and-retrain procedure; the general framing of pruning as a constrained optimization problem (minimize parameter count subject to bounded error increase) that all later saliency-based pruning methods inherit.

## Experimental methodology

Applied to small fully-connected and convolutional networks for digit recognition tasks, comparing generalization performance of networks pruned with the saliency criterion against networks pruned by raw weight magnitude and against smaller networks trained from scratch.

## Results

Saliency-based pruning removes a substantial fraction of weights with smaller accuracy degradation than magnitude-based pruning at the same compression level, and in some cases the pruned network generalizes better than the original due to reduced overfitting.

## Comparison with the state of the art

At the time, this was a clear improvement over naive magnitude-based weight removal, which the paper shows is a comparatively poor proxy for a weight's actual importance to the loss.

## Strengths

Mathematically principled, conceptually simple, and equally applicable regardless of the specific architecture — the saliency criterion does not depend on any property unique to the small networks tested.

## Weaknesses

The diagonal-Hessian approximation ignores correlations between weights, which can misestimate saliency when weights interact; the second-order computation is also more expensive than simple magnitude thresholding, a cost that becomes significant at the scale of modern deep networks.

## Limitations

Evaluated only on very small networks by modern standards; it does not address structured (channel/filter-level) pruning, hardware speedups, or quantization — these are all later extensions building on the same saliency-pruning idea.

## Open questions

How well does a second-order saliency criterion scale computationally to networks with millions or billions of parameters? Can structured (group-level) saliency be defined so that pruning produces real speedups on commodity hardware, rather than only reducing the parameter count?

## Possible extensions

Group/structured saliency for channel or filter pruning compatible with dense hardware; cheaper Hessian approximations (e.g. via Fisher information or empirical Fisher) that scale to large modern networks, the approach modern saliency-based pruning methods (e.g. SNIP, Fisher pruning) actually adopt.

## Relevance to our research

The conceptual ancestor of essentially all later saliency/importance-based pruning work, including the magnitude-based pruning used in [[2015_Han_LearningWeightsConnections]] and [[2016_Han_DeepCompression]]; useful as the historical and mathematical baseline when motivating why pruning criteria matter.

## Possible thesis topics

Reproducing Optimal Brain Damage's diagonal-Hessian saliency criterion on a small modern CNN and comparing it against magnitude pruning at matched compression ratios, to quantify how much the original argument still holds with today's architectures and optimizers.

## Possible collaborations

Groups working on second-order optimization methods and on modern saliency/Fisher-information-based pruning criteria.

## Links to related papers

[[2015_Han_LearningWeightsConnections]], [[2016_Han_DeepCompression]]
