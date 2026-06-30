# Compression

## Evolution of the concept

Before pruning/quantization pipelines, Denil et al.'s "Predicting Parameters in Deep Learning" (NeurIPS 2013) gave an early, distinct demonstration that compression is possible at all: it showed that most weights in a trained network are redundant and that a large fraction (over 95% in the best case) can be predicted from a small learned subset via low-rank factorization, without retraining the full set of parameters. Model compression as an end-to-end engineering problem in its own right is established by Han et al. (2016), who show that pruning, quantization, and entropy coding (Huffman) combine in a three-stage pipeline with a multiplicative effect on the compression ratio (35-49x on AlexNet/VGG with no accuracy loss). This work is the conceptual reference that ties together the other entries in the knowledge base (Quantization, Pruning, Distillation) as components of a broader compression strategy. A 2025 survey (Liu et al., Frontiers in Robotics and AI) updates this synthesis for the LLM era, bridging the classic CNN-era compression literature with the 2023-2024 wave of LLM-focused methods (AWQ, SliceGPT, MiniLLM) and noting that applying mature pruning/quantization/distillation techniques at LLM scale surfaces new challenges (calibration cost, structured-vs-unstructured trade-offs) not present in the AlexNet/VGG era.

## Key papers

[[2013_Denil_PredictingParametersDeepLearning]] — early evidence of massive weight redundancy via low-rank factorization, a precursor line of research distinct from pruning/quantization.

[[2016_Han_DeepCompression]] — three-stage pipeline: pruning + trained quantization + Huffman coding.

[[2025_Liu_ModelCompressionSurvey]] — survey bridging classic CNN-era compression techniques with 2023-2024 LLM-scale compression methods, useful as an up-to-date reference point for the field.

[[1990_LeCun_OptimalBrainDamage]] — saliency-based weight removal via a second-order Taylor approximation of the loss, the foundational precursor to the magnitude-based pruning that later compression pipelines build on.

[[2006_Bucila_ModelCompression]] — uses a trained ensemble as a labeling oracle to transfer its learned decision function into a single compact model, the precursor to modern knowledge distillation as a compression technique.

[[2015_Han_LearningWeightsConnections]] — shows that removing low-magnitude weights and retraining the surviving sparse network recovers most or all original accuracy, the pruning stage that Deep Compression later combines with quantization and entropy coding.

[[2016_Hubara_BinarizedNeuralNetworks]] — binary weights/activations as the most extreme point on the compression spectrum, with a straight-through-estimator training recipe still referenced by later binary/ternary compression work.

[[2020_Cai_TinyTL]] — reframes compression for the training (not just inference) memory budget, freezing weights and training only a small bias/lite-residual module to cut activation memory.

[[2021_Banbury_MLPerfTiny]] — standardized benchmark methodology used to compare the practical effect of different compression techniques on a level playing field.

[[2022_Zhang_DeepLearningHARWearableSensors]] — survey connecting compression choices explicitly to deployment constraints for wearable HAR models.

[[2023_Antonini_TinyMLAnomalyDetectionIndustrial]] — full anomaly-detection pipeline (training and inference) compressed onto a constrained edge device using an unsupervised algorithm that avoids the need for labeled failure data.

[[2023_Yang_BIOT]] — a natural test case for whether large-model compression techniques can bring foundation-model-level biosignal performance to constrained edge hardware.

[[2024_Lattanzi_TransformersTinyHAR]] — benchmarks transformer-based HAR models against CNN/RNN baselines under the actual memory constraints of tiny wearable devices, surfacing where compression is most needed.

[[2024_delaFuente_ESN-PdM]] — uses TinyML model optimization to make on-device and on-gateway inference tiers viable within a dynamic accuracy/latency/battery routing architecture.

[[2025_Zeng_TinyNeXt]] — redesigns self-attention to cut memory-bound operations directly, rather than only reducing parameter count or FLOPs, paired with a hybrid CNN/transformer macro architecture.

[[2026_Sen_NVFP4QuantizationEdgeAI]] — reports consistent ~4× static model-size and ~7× runtime activation-storage reduction from NVFP4 across six CNN backbones, with the trade-off explicitly characterized against accuracy.

[[2026_Garavagno_HWNASUltraLowPower]] — bounds RAM/Flash/MAC of the searched CNN directly in the NAS objective, producing architectures sized for 20-40 KiB RAM targets rather than compressing a pre-existing model post hoc.

## Open problems

Transferring the pipeline to modern architectures (Transformers, already-compact networks like MobileNet) where the margins for "free" compression are smaller than on AlexNet/VGG.

## Research ideas

An "optimal" compression pipeline that automatically combines structured pruning, mixed-precision quantization, and distillation as a function of the target device's memory budget.

## Possible thesis topics

Replicating the Deep Compression pipeline on modern architectures for TinyML, measuring whether the multiplicative effect holds when starting from already-efficient models like MobileNet.

## Links

[[Quantization]], [[Pruning]], [[Distillation]], [[NAS]]
