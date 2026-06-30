# Learning both Weights and Connections for Efficient Neural Networks

**Full citation:** Han, S., Pool, J., Tran, J., Dally, W.J. (2015). Learning both Weights and Connections for Efficient Neural Networks. *Advances in Neural Information Processing Systems 28 (NeurIPS 2015)*. https://proceedings.neurips.cc/paper/2015/file/ae0eb3eed39d2bcef4622b2499a05fe6-Paper.pdf

**Linked concepts:** [[Pruning]], [[Compression]]

## Abstract summary

The authors propose a simple train → prune → retrain pipeline: train a dense network to convergence, remove connections whose weight magnitude falls below a threshold, then retrain the remaining (sparse) connections to recover accuracy, iterating as needed.

## Research problem

Modern deep CNNs (AlexNet, VGG) at the time had tens to hundreds of millions of parameters, far more than needed to represent the function they learn, making them costly to store, move, and run on memory- and energy-constrained hardware.

## Key idea

Many connections in a trained network are redundant once the network has converged; removing low-magnitude weights and retraining the surviving sparse network on the same task recovers most or all of the original accuracy, since the remaining connections can re-adapt to compensate.

## Technical contribution

A practical, scalable, iterative magnitude-pruning algorithm (prune → retrain → re-prune) applicable to large modern CNNs, in contrast to the more theoretically involved second-order saliency criterion of [[1990_LeCun_OptimalBrainDamage]]; demonstrates that simple magnitude thresholding, combined with retraining, is enough to achieve large compression ratios with no accuracy loss.

## Experimental methodology

Applied to AlexNet and VGG-16 on ImageNet classification, measuring the number of parameters removed and the resulting top-1/top-5 accuracy compared to the dense baseline, with retraining performed after each pruning round.

## Results

Reduces the number of parameters in AlexNet and VGG-16 by roughly 9x and 13x respectively with no loss in accuracy, establishing that the vast majority of connections in these networks are unnecessary once retraining is allowed.

## Comparison with the state of the art

A more practical and scalable alternative to second-order saliency pruning for networks of this size, and the first stage that [[2016_Han_DeepCompression]] builds its quantization and Huffman-coding stages on top of.

## Strengths

Simple to implement, scales to large networks, produces large, reproducible compression ratios; became the standard first stage of subsequent compression pipelines.

## Weaknesses

The resulting sparsity is unstructured (irregular, scattered individual connections), which does not translate into real speedups on commodity dense hardware (CPU/GPU) without specialized sparse-matrix support.

## Limitations

Validated only on CNNs for image classification with architectures now considered large and redundant by modern standards; does not address how the sparse network should be efficiently executed in practice.

## Open questions

How can pruning be made structured (at the level of channels, filters, or blocks) so that the resulting model is directly faster on standard hardware, rather than only smaller in parameter count?

## Possible extensions

Structured/channel pruning for hardware-friendly speedups; combination with quantization and entropy coding, as done immediately afterward in [[2016_Han_DeepCompression]].

## Relevance to our research

The original modern unstructured-pruning method and the direct precursor stage of Deep Compression; a standard baseline for any pruning study targeting edge/embedded deployment.

## Possible thesis topics

Comparing the iterative magnitude-pruning procedure introduced here against modern one-shot or structured pruning criteria on a model sized for microcontroller deployment, evaluating both compression ratio and real inference speedup.

## Possible collaborations

Groups working on sparse-matrix hardware/kernels and on structured pruning compilers (TVM, MLIR) that could realize speedups from this kind of sparsity.

## Links to related papers

[[1990_LeCun_OptimalBrainDamage]], [[2016_Han_DeepCompression]]
