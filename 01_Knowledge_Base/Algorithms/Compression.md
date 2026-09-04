# Compression

Model compression is the general problem of making a trained network smaller and cheaper to run. [[Quantization]], [[Pruning]], and [[Distillation]] are each one technique for doing this; this concept covers the broader problem of combining such techniques into a full pipeline, plus techniques that don't fit neatly into any of those three categories.

## Evolution of the concept

An early demonstration that heavy compression is even possible came from Denil et al. ("Predicting Parameters in Deep Learning", NeurIPS 2013): most of a trained network's weights turn out to be redundant, and in the best case over 95% of them can be predicted from a small learned subset using low-rank factorization (approximating a large weight matrix as the product of two much smaller ones), without retraining the full parameter set.

Model compression as an end-to-end engineering pipeline — rather than one isolated technique — was established by Han et al. (2016, "Deep Compression"): pruning, quantization, and Huffman entropy coding (a data-compression technique that assigns shorter codes to more frequent values) combine into a three-stage pipeline whose effects multiply, achieving 35–49x compression on AlexNet/VGG with no loss of accuracy. This pipeline is the reference point that ties [[Quantization]], [[Pruning]], and [[Distillation]] together as components of one broader compression strategy rather than three unrelated techniques.

The field's standard organizing taxonomy comes from Cheng et al.'s 2018 IEEE Signal Processing Magazine survey, which groups compression techniques into four categories — parameter pruning/sharing, low-rank factorization, transferred/compact filters, and distillation — a grouping later surveys still build on. Deng et al.'s 2020 Proceedings of the IEEE survey extends that taxonomy by treating compression and hardware acceleration jointly, directly relevant to this concept's own open problem below (which techniques yield real, not just theoretical, speedups). Shuvo et al.'s 2023 review brings that same joint view specifically to resource-constrained edge devices, covering the full pipeline from compression technique through to hardware execution.

The rise of large language models (LLMs) has pulled compression research toward a new regime: a 2025 survey (Liu et al.) bridges the classic CNN-era techniques above with the 2023–2024 wave of LLM-focused compression methods (AWQ, SliceGPT, MiniLLM — see [[Quantization]], [[Pruning]], and [[Distillation]] for each), and notes that applying pruning/quantization/distillation at LLM scale surfaces new challenges — calibration cost, and different trade-offs between structured and unstructured techniques — that were not present in the AlexNet/VGG era.

## Key papers

[[2013_Denil_PredictingParametersDeepLearning]] — early evidence of massive weight redundancy via low-rank factorization, a precursor line of research distinct from pruning/quantization.

[[2018_Cheng_ModelCompressionAccelerationSurvey]] — established the four-category compression taxonomy (pruning/sharing, low-rank factorization, compact filters, distillation) that later surveys still build on; one of the most-cited papers in the entire compression literature.

[[2020_Deng_ModelCompressionHardwareAccelerationSurvey]] — treats compression and hardware acceleration jointly, directly relevant to whether a technique yields real hardware speedup versus only a theoretical reduction in parameter count.

[[2023_Shuvo_EfficientAccelerationEdgeInferenceReview]] — full compression-through-hardware pipeline review specifically for resource-constrained edge devices, complementing the more general surveys above.

[[2016_Han_DeepCompression]] — the three-stage pipeline: pruning + trained quantization + Huffman coding.

[[2025_Liu_ModelCompressionSurvey]] — survey bridging classic CNN-era compression techniques with 2023–2024 LLM-scale compression methods.

[[1990_LeCun_OptimalBrainDamage]] — saliency-based weight removal via a second-order (Hessian) approximation of the loss; the foundational precursor to the magnitude-based pruning that later compression pipelines build on.

[[2006_Bucila_ModelCompression]] — uses a trained ensemble as a labeling oracle to transfer its learned decision function into a single compact model; the precursor to modern knowledge distillation as a compression technique.

[[2015_Han_LearningWeightsConnections]] — shows that removing low-magnitude weights and retraining the surviving sparse network recovers most or all original accuracy; the pruning stage Deep Compression later combines with quantization and entropy coding.

[[2016_Hubara_BinarizedNeuralNetworks]] — binary weights and activations as the most extreme point on the compression spectrum, with a "straight-through estimator" training trick (a way to approximate gradients through the non-differentiable binarization step) still referenced by later binary/ternary compression work.

[[2020_Cai_TinyTL]] — reframes compression for the *training* memory budget (not just inference), freezing weights and training only a small bias/lite-residual module to cut activation memory.

[[2021_Banbury_MLPerfTiny]] — standardized benchmark methodology used to compare the practical effect of different compression techniques on a level playing field.

[[2022_Zhang_DeepLearningHARWearableSensors]] — survey connecting compression choices explicitly to deployment constraints for wearable Human Activity Recognition models.

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] — full anomaly-detection pipeline (training and inference) compressed onto a constrained edge device using an unsupervised algorithm that avoids the need for labeled failure data.

[[2023_Yang_BIOT]] — a natural test case for whether large-model compression techniques can bring foundation-model-level biosignal performance to constrained edge hardware.

[[2024_Lattanzi_TransformersTinyHAR]] — benchmarks transformer-based Human Activity Recognition models against CNN/RNN baselines under the actual memory constraints of tiny wearable devices, surfacing where compression is most needed.

[[2024_delaFuente_ESN-PdM]] — uses TinyML model optimization to make on-device and on-gateway inference tiers viable within a dynamic accuracy/latency/battery routing architecture.

[[2025_Zeng_TinyNeXt]] — redesigns self-attention to cut memory-bound operations directly, rather than only reducing parameter count or FLOPs, paired with a hybrid CNN/transformer architecture.

[[2026_Sen_NVFP4QuantizationEdgeAI]] — reports consistent ~4x static model-size and ~7x runtime activation-storage reduction from a 4-bit floating-point format (NVFP4) across six CNN backbones, with the accuracy trade-off explicitly characterized.

[[2026_Garavagno_HWNASUltraLowPower]] — bounds RAM/Flash/multiply-accumulate operations of the searched CNN directly in the architecture-search objective, producing architectures sized for 20–40 KiB RAM targets rather than compressing a pre-existing model after the fact.

## Open problems

Transferring the Deep-Compression-style pipeline to modern architectures (transformers, already-compact networks like MobileNet), where the margins for "free" compression are smaller than they were on AlexNet/VGG.

## Research ideas

An "optimal" compression pipeline that automatically combines structured pruning, mixed-precision quantization, and distillation as a function of the target device's memory budget.

## Possible thesis topics

Replicating the Deep Compression pipeline on modern architectures for TinyML, measuring whether the multiplicative effect still holds when starting from an already-efficient model like MobileNet rather than AlexNet/VGG.

## Links

[[Quantization]], [[Pruning]], [[Distillation]], [[NAS]]
