# Pruning

## Evolution of the concept

Pruning originates from the observation that many connections in a trained neural network contribute little to the output and can be removed without significant accuracy loss. Han et al. (2016) formalize it as the first stage of a three-stage compression pipeline (Deep Compression). The main limitation of unstructured pruning (at the single-connection level) is that it does not automatically translate into speedups on generic hardware: this pushed later research toward structured pruning, at the channel or filter level, compatible with real hardware acceleration.

## Key papers

[[2016_Han_DeepCompression]] — unstructured pruning as the first stage of the pipeline; shows that combined with quantization and Huffman coding it produces a multiplicative effect on compression.

## Open problems

Obtaining structured pruning that gives real speedups on commodity hardware (not just a theoretical reduction in parameters). Automating the compression ratio per layer as a function of the target hardware.

## Research ideas

NAS-guided pruning to directly search for compressible architectures; combining structured pruning with CMSIS-NN kernels to obtain measurable speedups on Cortex-M.

## Possible thesis topics

Comparison between classic unstructured pruning and modern structured pruning on models for microcontrollers, measuring real speedup and not just parameter reduction.

## Links

[[Quantization]], [[Compression]], [[NAS]]
