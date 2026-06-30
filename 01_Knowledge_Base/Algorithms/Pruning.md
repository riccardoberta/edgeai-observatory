# Pruning

## Evolution of the concept

Pruning's conceptual root goes back to LeCun, Denker, and Solla's "Optimal Brain Damage" (NeurIPS 1990), which used second-derivative (Hessian) information to decide which weights could be removed with minimal damage to the loss — the first formal saliency-based pruning criterion. The idea resurfaced for deep networks with Han et al.'s "Learning both Weights and Connections" (NeurIPS 2015), a three-step train/prune/retrain recipe, which Han et al. (2016) then folded into Deep Compression as the first stage of a three-stage pipeline. The main limitation of unstructured pruning (at the single-connection level) is that it does not automatically translate into speedups on generic hardware: this pushed later research toward structured pruning, at the channel or filter level, compatible with real hardware acceleration.

## Key papers

[[1990_LeCun_OptimalBrainDamage]] — original Hessian-based saliency criterion for removing unimportant weights; the conceptual ancestor of all later magnitude/saliency pruning.

[[2015_Han_LearningWeightsConnections]] — the original modern unstructured-pruning method (train → prune low-weight connections → retrain), which Deep Compression below builds on as its first stage.

[[2016_Han_DeepCompression]] — unstructured pruning as the first stage of the pipeline; shows that combined with quantization and Huffman coding it produces a multiplicative effect on compression.

## Open problems

Obtaining structured pruning that gives real speedups on commodity hardware (not just a theoretical reduction in parameters). Automating the compression ratio per layer as a function of the target hardware.

## Research ideas

NAS-guided pruning to directly search for compressible architectures; combining structured pruning with CMSIS-NN kernels to obtain measurable speedups on Cortex-M.

## Possible thesis topics

Comparison between classic unstructured pruning and modern structured pruning on models for microcontrollers, measuring real speedup and not just parameter reduction.

## Links

[[Quantization]], [[Compression]], [[NAS]]
