# Pruning

Pruning removes weights, or whole structures (neurons, channels, layers), that contribute little to a network's accuracy, shrinking the model. *Unstructured* pruning removes individual weights and can achieve high theoretical compression, but usually needs specialized sparse-matrix hardware or software support to translate into a real speedup. *Structured* pruning removes entire channels or filters, producing a smaller dense network that runs faster on ordinary hardware without any special support.

## Evolution of the concept

Pruning's conceptual root goes back to LeCun, Denker, and Solla's "Optimal Brain Damage" (NeurIPS 1990), which used second-derivative (Hessian) information to decide which weights could be removed with minimal damage to the loss — the first formal saliency-based pruning criterion. The idea resurfaced for deep networks with Han et al.'s "Learning both Weights and Connections" (NeurIPS 2015), a three-step train/prune/retrain recipe, which Han et al. (2016) then folded into "Deep Compression" as the first stage of a three-stage pipeline (see [[Compression]]).

The main limitation of unstructured pruning is that it does not automatically translate into speedups on generic hardware, which pushed later research toward structured pruning at the channel or filter level. The 2023–2024 large-language-model era pushed this further still: SliceGPT (Ashkboos et al., ICLR 2024) exploits a computational-invariance property of transformer residual streams (a mathematical property that lets certain rotations be applied without changing the network's output) to physically delete rows and columns of weight matrices, yielding dense — not sparse — smaller matrices that run faster on standard hardware without any specialized sparse kernels.

Eccles et al. (2024) tackle the structured-versus-fast trade-off directly with "Reconvene", which applies structured (rather than unstructured) pruning at initialization — before training even begins — generating edge-ready pruned models within seconds: up to 16.21x smaller and 2x faster than an unstructured pruning-at-initialization counterpart at comparable accuracy.

A significant methodological caution for the whole field comes from Blalock et al.'s "What is the State of Neural Network Pruning?" (MLSys 2020) — not a new method, but a critical meta-analysis of 81 pruning papers finding that inconsistent evaluation practices (different baselines, metrics, and operating points) make most claimed improvements incomparable across papers. The paper introduces ShrinkBench, a standardized evaluation framework, and its finding is worth keeping in mind when reading any single paper's reported comparison in this concept, including Eccles et al.'s, which is evaluated only against an unstructured pruning-at-initialization baseline.

## Key papers

[[1990_LeCun_OptimalBrainDamage]] — original Hessian-based saliency criterion for removing unimportant weights; the conceptual ancestor of all later magnitude/saliency pruning.

[[2015_Han_LearningWeightsConnections]] — the original modern unstructured-pruning method (train, prune low-weight connections, retrain), which Deep Compression below builds on as its first stage.

[[2016_Han_DeepCompression]] — unstructured pruning as the first stage of a compression pipeline; shows that combined with quantization and Huffman coding it produces a multiplicative effect on compression.

[[2024_Ashkboos_SliceGPT]] — structured slicing of transformer weight matrices via a computational-invariance argument, producing dense matrices with real, hardware-realizable speedups for large language models.

[[2024_Eccles_StructuredPruningInitializationEdge]] — "Reconvene": structured pruning at initialization generating edge-ready pruned models within seconds, up to 16.21x smaller and 2x faster than unstructured pruning-at-initialization at comparable accuracy.

[[2020_Blalock_StateOfNeuralNetworkPruning]] — critical meta-analysis of 81 pruning papers finding widespread evaluation-methodology inconsistency; introduces ShrinkBench for standardized comparison.

## Open problems

Automating the compression ratio per layer as a function of the target hardware. Now that structured pruning at initialization has been shown to deliver real, hardware-realizable speedups at seconds-scale generation cost (Eccles et al.), how does it compare in final accuracy and speedup against post-training structured pruning (Deep-Compression-style) and NAS-guided pruning, not only against unstructured pruning-at-initialization as in its own evaluation? Does its seconds-scale generation advantage hold at the microcontroller (Cortex-M) tier, or only on the edge-server/mobile-class hardware it was likely evaluated on?

## Research ideas

NAS-guided pruning, to directly search for compressible architectures. Combining structured pruning with CMSIS-NN kernels to obtain measurable speedups on Cortex-M.

## Possible thesis topics

A comparison between classic unstructured pruning and modern structured pruning on models for microcontrollers, measuring real speedup rather than only parameter-count reduction.

## Links

[[Quantization]], [[Compression]], [[NAS]]
