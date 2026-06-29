# FPGA

## Evolution of the concept

FPGA-based EdgeAI acceleration grew out of the observation that reconfigurable hardware could instantiate many small, fully-parallel, per-layer compute structures rather than relying on a single reused generic processing unit as GPUs and CPUs do. FINN was a pioneering framework demonstrating that pairing aggressive network quantization (down to binary precision) with a streaming, per-layer-customized dataflow architecture could yield extremely high throughput-per-watt for image classification, directly linking the [[Quantization]] research direction to a concrete, automated hardware-generation pipeline. The framework has since evolved (FINN-R) to support a wider range of quantization levels and target platforms, from embedded devices up to cloud FPGAs.

## Key papers

[[2017_Umuroglu_FINN]] — framework for generating fast, scalable, per-layer streaming FPGA accelerators for binarized/quantized neural networks.

## Open problems

How does FINN-style per-layer dataflow customization compare to NPU/ASIC fixed-function accelerators on modern EdgeAI benchmarks, in throughput-per-watt and resource cost? Can the design-space exploration approach extend efficiently to non-CNN architectures (e.g. small transformers) relevant to current TinyML research?

## Research ideas

A throughput-per-watt benchmark comparing a FINN-generated FPGA accelerator against an NPU and a Cortex-M+CMSIS-NN deployment for the same quantized EdgeAI model.

## Possible thesis topics

Extending FINN's per-layer dataflow methodology to a non-vision EdgeAI task in our [[Applications]] taxonomy (Keyword Spotting, HAR); reconfigurability-versus-efficiency study comparing FPGA, NPU, and RISC-V accelerator substrates for the same task.

## Links

[[Quantization]], [[NPU]], [[RISC-V]], [[Cortex-M]]
