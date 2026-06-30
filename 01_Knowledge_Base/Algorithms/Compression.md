# Compression

## Evolution of the concept

Before pruning/quantization pipelines, Denil et al.'s "Predicting Parameters in Deep Learning" (NeurIPS 2013) gave an early, distinct demonstration that compression is possible at all: it showed that most weights in a trained network are redundant and that a large fraction (over 95% in the best case) can be predicted from a small learned subset via low-rank factorization, without retraining the full set of parameters. Model compression as an end-to-end engineering problem in its own right is established by Han et al. (2016), who show that pruning, quantization, and entropy coding (Huffman) combine in a three-stage pipeline with a multiplicative effect on the compression ratio (35-49x on AlexNet/VGG with no accuracy loss). This work is the conceptual reference that ties together the other entries in the knowledge base (Quantization, Pruning, Distillation) as components of a broader compression strategy. A 2025 survey (Liu et al., Frontiers in Robotics and AI) updates this synthesis for the LLM era, bridging the classic CNN-era compression literature with the 2023-2024 wave of LLM-focused methods (AWQ, SliceGPT, MiniLLM) and noting that applying mature pruning/quantization/distillation techniques at LLM scale surfaces new challenges (calibration cost, structured-vs-unstructured trade-offs) not present in the AlexNet/VGG era.

## Key papers

[[2013_Denil_PredictingParametersDeepLearning]] — early evidence of massive weight redundancy via low-rank factorization, a precursor line of research distinct from pruning/quantization.

[[2016_Han_DeepCompression]] — three-stage pipeline: pruning + trained quantization + Huffman coding.

[[2025_Liu_ModelCompressionSurvey]] — survey bridging classic CNN-era compression techniques with 2023-2024 LLM-scale compression methods, useful as an up-to-date reference point for the field.

## Open problems

Transferring the pipeline to modern architectures (Transformers, already-compact networks like MobileNet) where the margins for "free" compression are smaller than on AlexNet/VGG.

## Research ideas

An "optimal" compression pipeline that automatically combines structured pruning, mixed-precision quantization, and distillation as a function of the target device's memory budget.

## Possible thesis topics

Replicating the Deep Compression pipeline on modern architectures for TinyML, measuring whether the multiplicative effect holds when starting from already-efficient models like MobileNet.

## Links

[[Quantization]], [[Pruning]], [[Distillation]], [[NAS]]
