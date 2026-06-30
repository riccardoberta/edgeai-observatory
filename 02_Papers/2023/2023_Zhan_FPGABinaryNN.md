# FPGA-based acceleration for binary neural networks in edge computing

**Full citation:** Zhan, J.-Y., Yu, A.-T., Jiang, W., Yang, Y.-J., Xie, X.-N., Chang, Z.-W., Yang, J.-H. (2023). FPGA-based acceleration for binary neural networks in edge computing. Journal of Electronic Science and Technology, 21(2), 100204. https://doi.org/10.1016/j.jnlest.2023.100204

**Linked concepts:** [[FPGA]], [[Quantization]]

## Abstract summary

The authors review binary neural network (BNN) design and the corresponding FPGA-based hardware accelerator landscape for edge computing, providing a structured comparison of representative BNN accelerator designs alongside experimental evaluation on typical BNN workloads.

## Research problem

Binary neural networks promise extreme efficiency gains for edge deployment, but the design space of FPGA accelerators tailored to binary (1-bit) precision is fragmented across many point designs, making it hard to compare approaches or identify which design choices actually drive efficiency.

## Key idea

Systematically organize and compare existing FPGA-based BNN accelerator designs along common axes (dataflow style, resource utilization, precision-specific optimizations), and validate the comparison experimentally on representative BNN models, rather than treating each accelerator as a one-off point design.

## Technical contribution

A structured taxonomy of FPGA-based BNN accelerator design choices; an experimental evaluation comparing representative designs on common BNN workloads, providing a reference point for the binary-precision corner of the FPGA/[[Quantization]] design space.

## Experimental methodology

Implementation and evaluation of representative BNN accelerator design patterns on FPGA, measuring throughput, resource utilization, and accuracy trade-offs across typical BNN benchmark models.

## Results

The review and accompanying experiments characterize how different FPGA-based BNN accelerator design choices trade off throughput, resource cost, and accuracy, giving edge-FPGA practitioners a comparative reference rather than a single isolated design report.

## Comparison with the state of the art

Extends the FINN-era binary/quantized FPGA accelerator line specifically toward a systematic, comparative review of the binary-precision design space, rather than introducing a single new framework.

## Strengths

Provides a structured comparison across multiple BNN accelerator designs rather than a single point solution; grounds the review in actual experimental evaluation rather than only a literature survey.

## Weaknesses

Focused specifically on binary (1-bit) precision; does not cover the broader mixed-precision quantization spectrum that much current EdgeAI quantization research (e.g. INT4/INT8, AWQ-style methods) now targets.

## Limitations

BNN accuracy remains a known limitation relative to higher-precision quantization on harder tasks, a trade-off the review documents but does not solve.

## Open questions

How does the binary-precision design space reviewed here compare, in throughput-per-watt, to the higher-precision streaming dataflow accelerators (FINN-R) covered elsewhere in the [[FPGA]] entry? Can binary-precision FPGA accelerator design patterns extend efficiently to non-CNN architectures?

## Possible extensions

Extending the comparative review methodology to mixed-precision (not purely binary) FPGA accelerator designs; benchmarking the surveyed BNN accelerator patterns against modern NPU/ASIC binary-precision support.

## Relevance to our research

Brings the FPGA entry's binary-precision corner into the 2023-2026 window with a structured, comparative reference, complementing FINN's framework-level contribution already covered there.

## Possible thesis topics

A throughput-per-watt comparison between the binary-precision FPGA designs surveyed here and FINN-R's mixed-precision streaming dataflow approach on a common quantized EdgeAI model.

## Possible collaborations

Groups maintaining FPGA-based BNN/quantized accelerator frameworks (e.g. the FINN ecosystem) that could supply comparison baselines.

## Links to related papers

[[2017_Umuroglu_FINN]], [[2015_Zhang_FPGAAcceleratorDesign]]
