# FINN: A Framework for Fast, Scalable Binarized Neural Network Inference

**Full citation:** Umuroglu, Y., Fraser, N. J., Gambardella, G., Blott, M., Leong, P., Jahre, M., Vissers, K. (2017). FINN: A Framework for Fast, Scalable Binarized Neural Network Inference. *Proceedings of the 2017 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays (FPGA '17)*. arXiv:1612.07119. https://arxiv.org/abs/1612.07119

**Linked concepts:** [[FPGA]], [[Quantization]]

## Abstract summary

The authors (Xilinx Research Labs and collaborators) present FINN, a framework for building fast and flexible FPGA accelerators for binarized (and more generally quantized) neural networks, using a heterogeneous streaming architecture where each network layer gets a dedicated, custom-sized compute engine tailored to a target throughput, rather than a single reused generic processing unit.

## Research problem

Deploying neural networks on FPGAs traditionally relies on generic, time-shared compute units (similar in spirit to a GPU's reused execution units), which underuses the FPGA's ability to instantiate many small, custom, fully-parallel compute structures; meanwhile, binarized/low-precision networks open the door to extremely resource-efficient hardware, but need an accelerator design methodology that can actually exploit that low precision at the hardware level.

## Key idea

Map each layer of a binarized neural network onto its own dedicated, per-layer hardware compute engine sized according to the throughput needed for that specific layer, forming a streaming dataflow architecture across the FPGA fabric, rather than time-multiplexing one generic compute array across all layers.

## Technical contribution

A full framework (synthesizable building blocks plus a design-space exploration tool) that takes a binarized neural network specification and generates a custom, per-layer streaming FPGA accelerator, with fully-connected, convolutional, and pooling layer building blocks designed for extremely low-precision (binary/few-bit) arithmetic.

## Experimental methodology

Implemented on Xilinx FPGA platforms (e.g. ZC706), evaluated on standard image-classification benchmarks of the era (e.g. MNIST, CIFAR-10, SVHN) with binarized network architectures, measuring achieved throughput (frames/second), latency, power, and resource utilization against the target design throughput specified at synthesis time.

## Results

FINN-generated accelerators achieve very high classification throughput (millions of classifications per second on simple benchmarks at the time) at sub-watt to few-watt power levels, demonstrating that per-layer-customized, fully streaming dataflow architectures could vastly outperform generic time-shared FPGA accelerator designs for binarized networks.

## Comparison with the state of the art

At publication, FINN offered substantially higher throughput-per-resource than prior generic, time-multiplexed FPGA CNN accelerators, by trading network precision (binarization) for hardware specialization; its second generation, FINN-R, extended this from purely binary to a wider range of quantization levels and target platforms (from embedded devices up to AWS F1 cloud FPGAs).

## Strengths

Pioneering, fully open-sourced framework (still maintained as the Xilinx/finn project) connecting the [[Quantization]] research direction directly to a concrete, automated hardware-generation pipeline; demonstrated extreme throughput-per-watt by aligning precision reduction with a hardware architecture designed specifically to exploit it.

## Weaknesses

Binarized networks suffer accuracy degradation on harder tasks compared to higher-precision models, a trade-off FINN's original paper does not deeply explore beyond the benchmarks tested; per-layer dataflow customization requires re-synthesizing hardware for each new network, which is a slower iteration cycle than software-only deployment on CPUs/MCUs.

## Limitations

Targets FPGA fabric specifically, which has different cost, power, and reconfigurability trade-offs than ASIC NPUs or MCU-class CPUs covered elsewhere in our [[Hardware]] taxonomy; the original 2017 evaluation used benchmarks that are small by current standards, so direct comparison to modern EdgeAI workloads requires care.

## Open questions

How does FINN-style per-layer dataflow customization compare to NPU/ASIC fixed-function accelerators (covered under our [[NPU]] entry) on the same modern EdgeAI benchmarks, in throughput-per-watt and resource cost? Can FINN's design-space exploration approach be extended efficiently to non-CNN architectures (e.g. small transformers) relevant to current TinyML research?

## Possible extensions

Applying FINN-style streaming dataflow generation to a modern EdgeAI benchmark (e.g. a quantized keyword-spotting or HAR model) and comparing throughput-per-watt against an NPU or Cortex-M+CMSIS-NN baseline for the same task.

## Relevance to our research

Foundational reference for the [[FPGA]] branch of our [[Hardware]] taxonomy, and a direct bridge to [[Quantization]]: it is one of the clearest demonstrations that aggressive quantization (down to binary) can be paired with a hardware design methodology that fully exploits it, rather than just reducing model size in isolation.

## Possible thesis topics

A throughput-per-watt benchmark comparing a FINN-generated FPGA accelerator against an NPU and a Cortex-M+CMSIS-NN deployment for the same quantized EdgeAI model; extending FINN's per-layer dataflow methodology to a non-vision EdgeAI task in our taxonomy (Keyword Spotting, HAR).

## Possible collaborations

Xilinx Research Labs / AMD (current maintainers of the open-source FINN project); FPGA-for-ML research groups.

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]] (the precision-reduction research direction FINN's hardware exploits), [[2018_Lai_CMSIS-NN]], [[2018_Flamand_GAP8]] (alternative hardware substrates for the same EdgeAI deployment problem)
