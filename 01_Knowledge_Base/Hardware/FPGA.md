# FPGA (Field-Programmable Gate Array)

An FPGA is a chip whose hardware logic can be reconfigured after manufacturing, used to build custom, application-specific accelerators without designing a fixed chip. FPGA-based EdgeAI acceleration grew out of the observation that reconfigurable hardware can instantiate many small, fully parallel, per-layer compute structures, rather than relying on a single reused generic processing unit as GPUs and CPUs do.

## Evolution of the concept

Zhang et al.'s "Optimizing FPGA-based Accelerator Design for Deep Convolutional Neural Networks" (2015) was an early, influential formalization of this idea: it applies a roofline-model-based analysis (a way of predicting whether a computation is limited by compute speed or by memory bandwidth) to systematically navigate the loop-tiling and loop-unrolling design space of a CNN accelerator, rather than relying on ad hoc design choices — directly anticipating the more aggressive, precision-driven design-space exploration FINN later builds on.

FINN (Umuroğlu et al., 2017) was a pioneering framework demonstrating that pairing aggressive network quantization (down to binary precision) with a streaming, per-layer-customized dataflow architecture could yield extremely high throughput-per-watt for image classification, directly linking [[Quantization]] to a concrete, automated hardware-generation pipeline. The framework has since evolved (FINN-R) to support a wider range of quantization levels and target platforms, from embedded devices up to cloud FPGAs.

Two more recent works update the picture from different angles. Zhan et al. (2023) systematically review and experimentally compare the fragmented landscape of FPGA-based binary-neural-network accelerator designs, rather than proposing a single new framework, giving the binary-precision corner of this space a structured reference point. Shawahna, Sait, and El-Maleh (2018) review the field's design-technique landscape more broadly, spanning both training and inference; Yan, Koch, and Sinnen's later quantitative survey (2024) of 287 papers across the field's leading FPGA conferences finds inference acceleration dominating over training (81% versus 13%) and CNNs still dominant but with clear growth in graph-neural-network-targeted accelerator research — the two surveys together give roughly a six-year trend comparison for the field.

## Key papers

[[2015_Zhang_FPGAAcceleratorDesign]] — roofline-model-guided design-space exploration for CNN accelerator loop tiling/unrolling on FPGA, an early systematic alternative to ad hoc accelerator design.

[[2017_Umuroglu_FINN]] — framework for generating fast, scalable, per-layer streaming FPGA accelerators for binarized/quantized neural networks.

[[2023_Zhan_FPGABinaryNN]] — structured review and experimental comparison of FPGA-based binary neural network accelerator designs for edge computing.

[[2024_Yan_FPGASurvey]] — quantitative survey of 287 FPGA accelerator papers, finding inference/training imbalance (81%/13%) and CNN dominance with rising graph-neural-network-targeted research.

[[2018_Shawahna_FPGAAcceleratorsReview]] — comprehensive, highly-cited review of FPGA deep-learning accelerator design techniques spanning training and inference, an earlier and broader baseline than the 2024 Yan et al. survey.

## Open problems

How does FINN-style per-layer dataflow customization compare to NPU/ASIC fixed-function accelerators on modern EdgeAI benchmarks, in throughput-per-watt and resource cost? Can the design-space-exploration approach extend efficiently to non-CNN architectures, such as small transformers, relevant to current TinyML research?

## Research ideas

A throughput-per-watt benchmark comparing a FINN-generated FPGA accelerator against an NPU and a Cortex-M+CMSIS-NN deployment for the same quantized EdgeAI model.

## Possible thesis topics

Extending FINN's per-layer dataflow methodology to a non-vision EdgeAI task, such as Keyword Spotting or Human Activity Recognition. A reconfigurability-versus-efficiency study comparing FPGA, NPU, and RISC-V accelerator substrates for the same task.

## Links

[[Quantization]], [[NPU]], [[RISC-V]], [[Cortex-M]]
