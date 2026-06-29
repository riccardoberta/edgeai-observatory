# Compression

## Evolution of the concept

Model compression emerges as a problem in its own right with Han et al. (2016), who show that pruning, quantization, and entropy coding (Huffman) combine in a three-stage pipeline with a multiplicative effect on the compression ratio (35-49x on AlexNet/VGG with no accuracy loss). This work is the conceptual reference that ties together the other entries in the knowledge base (Quantization, Pruning, Distillation) as components of a broader compression strategy.

## Key papers

[[2016_Han_DeepCompression]] — three-stage pipeline: pruning + trained quantization + Huffman coding.

## Open problems

Transferring the pipeline to modern architectures (Transformers, already-compact networks like MobileNet) where the margins for "free" compression are smaller than on AlexNet/VGG.

## Research ideas

An "optimal" compression pipeline that automatically combines structured pruning, mixed-precision quantization, and distillation as a function of the target device's memory budget.

## Possible thesis topics

Replicating the Deep Compression pipeline on modern architectures for TinyML, measuring whether the multiplicative effect holds when starting from already-efficient models like MobileNet.

## Links

[[Quantization]], [[Pruning]], [[Distillation]], [[NAS]]
