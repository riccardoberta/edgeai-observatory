# Predicting Parameters in Deep Learning

**Full citation:** Denil, M., Shakibi, B., Dinh, L., Ranzato, M., de Freitas, N. (2013). Predicting Parameters in Deep Learning. *Advances in Neural Information Processing Systems 26 (NeurIPS 2013)*. https://proceedings.neurips.cc/paper_files/paper/2013/file/7fec306d1e665bc9c748b5d2b99a6e97-Paper.pdf

**Linked concepts:** [[Compression]]

## Abstract summary

The authors show that the weight matrices of trained neural networks are highly redundant: a small subset of the weights, or a low-rank factorization, is often sufficient to predict (reconstruct) the remaining weights with little loss in accuracy, suggesting that large weight matrices can be replaced by much smaller parameterizations.

## Research problem

Deep networks of the time used very large, densely parameterized weight matrices, but it was unclear how much of that parameterization was actually necessary to represent the function the network had learned, as opposed to simply redundant capacity.

## Key idea

If a small number of weights in a layer can be used to accurately predict the values of the rest of the weights in that layer (e.g. via a low-rank factorization or a learned dictionary), then the layer's effective parameter count can be reduced dramatically without retraining from scratch or losing the learned function.

## Technical contribution

Empirical evidence, across several network architectures and tasks, that weight matrices contain substantial structure/redundancy; low-rank and dictionary-based parameterizations that exploit this redundancy to reduce the number of free parameters that must be learned or stored per layer.

## Experimental methodology

Trains networks with a fraction of weights treated as "free" parameters and the rest predicted from them via the chosen parameterization, then measures task accuracy relative to a fully-parameterized baseline, across vision and other benchmark tasks.

## Results

Substantial parameter reduction is achievable with only a small accuracy cost in several settings, providing some of the earliest quantitative evidence for the weight redundancy that motivates the broader model-compression research direction (pruning, quantization, low-rank methods alike).

## Comparison with the state of the art

A precursor and complement to pruning-based compression: rather than removing individual weights, this line of work compresses by exploiting the predictability/structure across weights, an approach later echoed in low-rank factorization and tensor-decomposition compression methods.

## Strengths

Provides a different, structurally motivated lens on why neural networks can be compressed, distinct from and complementary to magnitude-based pruning; broadly applicable across architectures.

## Weaknesses

The low-rank/dictionary parameterizations explored are relatively simple compared to later structured compression methods, and the paper does not address how the resulting structured parameterizations map onto real hardware speedups.

## Limitations

Evaluated on networks and tasks considered small by current standards; does not directly address quantization, structured channel pruning, or deployment on memory-constrained edge hardware.

## Open questions

How does weight predictability/redundancy scale with network depth and width in modern large architectures? Can structured low-rank compression be combined effectively with quantization and pruning for compounding compression gains, similar to the pruning + quantization + coding pipeline of [[2016_Han_DeepCompression]]?

## Possible extensions

Combining low-rank/dictionary weight parameterizations with pruning and quantization in an integrated compression pipeline; extending the redundancy analysis to modern Transformer and efficient-CNN architectures, which are already much more compact than the networks studied here.

## Relevance to our research

Early, foundational evidence for weight redundancy that motivates the entire model-compression research direction; useful as a conceptual complement to the pruning- and quantization-focused papers more commonly cited in the [[Compression]] literature.

## Possible thesis topics

Quantifying weight redundancy (via low-rank approximation error) across layers of a modern efficient CNN (e.g. MobileNet) to test whether the redundancy this paper documents in older, larger architectures still holds in already-compact modern designs.

## Possible collaborations

Groups working on low-rank/tensor-decomposition compression methods and on theoretical analyses of neural network overparameterization.

## Links to related papers

[[2016_Han_DeepCompression]]
