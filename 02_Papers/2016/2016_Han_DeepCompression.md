# Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding

**Full citation:** Han, S., Mao, H., Dally, W.J. (2016). Deep Compression: Compressing Deep Neural Networks with Pruning, Trained Quantization and Huffman Coding. *4th International Conference on Learning Representations (ICLR 2016)*. arXiv:1510.00149. https://arxiv.org/abs/1510.00149

**Linked concepts:** [[Pruning]], [[Quantization]], [[Compression]]

## Abstract summary

The authors propose a three-stage pipeline — pruning, trained quantization, and Huffman coding — that reduces the size of deep neural networks by 35-49x without loss of accuracy, making it possible to run them on devices with limited memory.

## Research problem

The deep neural networks of the time (AlexNet, VGG) were too large to be stored and run on mobile and embedded devices with limited memory resources.

## Key idea

Compress the model in three sequential stages that reinforce each other: first remove the least important connections (pruning), then quantize the remaining weights by sharing them across a few clusters (trained quantization), and finally compress further with entropy coding (Huffman).

## Technical contribution

An integrated pruning + quantization + Huffman coding pipeline, with retraining between stages to recover accuracy; a demonstration that the three techniques are complementary rather than redundant.

## Experimental methodology

Application of the pipeline on AlexNet and VGG-16 on ImageNet, measuring the compression ratio and top-1/top-5 accuracy relative to the original model.

## Results

35x reduction for AlexNet and 49x for VGG-16 with no measurable accuracy loss; also reduces the energy needed for inference thanks to the smaller amount of data to be moved from memory.

## Comparison with the state of the art

Outperforms pruning or quantization applied individually, showing that the combination produces a multiplicative effect on the compression ratio.

## Strengths

Highly cited and reproducible results (code released by the authors), a clear conceptual framework that inspired much of the subsequent research on model compression.

## Weaknesses

The unstructured pruning produced does not automatically translate into speedups on generic hardware without support for sparse matrices; dedicated hardware or libraries are needed to actually exploit it.

## Limitations

Validated mainly on CNNs for vision on ImageNet with architectures that are now dated (AlexNet, VGG); it is unclear how well the pipeline transfers to Transformers or to already-compact networks like MobileNet.

## Open questions

How to obtain structured pruning that gives real speedups on commodity hardware? How to automate the choice of compression ratio per stage as a function of the target hardware?

## Possible extensions

Structured pruning (at the channel/filter level) compatible with hardware acceleration; combination with NAS to directly search for compressible architectures.

## Relevance to our research

An essential historical reference for any work on model compression for edge/embedded; useful as a conceptual baseline even though modern architectures require structured pruning techniques.

## Possible thesis topics

Comparison between classic unstructured pruning (Deep Compression) and modern structured pruning on models for microcontrollers; study of the effect of entropy coding on NPU accelerators.

## Possible collaborations

Research groups on hardware for sparse matrices and on compilers that support structured pruning (TVM, MLIR).

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]], [[2015_Hinton_DistillingKnowledge]]
