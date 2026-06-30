# Optimizing FPGA-based Accelerator Design for Deep Convolutional Neural Networks

**Full citation:** Zhang, C., Li, P., Sun, G., Guan, Y., Xiao, B., Cong, J. (2015). Optimizing FPGA-based Accelerator Design for Deep Convolutional Neural Networks. *Proceedings of the 2015 ACM/SIGDA International Symposium on Field-Programmable Gate Arrays (FPGA 2015)*. https://dl.acm.org/doi/10.1145/2684746.2689060

**Linked concepts:** [[FPGA]]

## Abstract summary

The authors propose a systematic, roofline-model-guided design methodology for exploring the design space of FPGA-based CNN accelerators — choosing loop tiling and unrolling factors for convolution computation to maximize throughput under the FPGA's available compute and memory-bandwidth resources — replacing ad-hoc, manually tuned accelerator designs with a principled optimization procedure.

## Research problem

Designing an efficient FPGA accelerator for CNN inference requires choosing many interacting parameters (loop tiling sizes, loop unrolling factors, on-chip buffer sizes) that jointly determine compute utilization and memory-bandwidth usage; prior accelerator designs typically chose these parameters manually or heuristically, without a systematic way to identify the actual compute- or bandwidth-bound design point.

## Key idea

Apply the roofline performance model — which characterizes a design's achievable throughput as the minimum of its compute-bound and memory-bandwidth-bound limits — to the space of possible CNN accelerator loop-tiling/unrolling configurations, so that the design space can be systematically searched for the configuration that maximizes throughput given the target FPGA's actual compute and bandwidth resources.

## Technical contribution

A formal analytical framework that maps CNN accelerator design parameters (tiling, unrolling) onto roofline-model performance bounds; an automated design-space exploration procedure built on this framework that identifies near-optimal accelerator configurations without exhaustive manual tuning; a polyhedral-based loop transformation methodology to generate the corresponding accelerator hardware description.

## Experimental methodology

Applies the roofline-guided design-space exploration to generate FPGA accelerator implementations for standard CNN architectures (e.g. AlexNet-class networks) on real FPGA hardware, comparing achieved throughput and resource utilization against both a naive/manually-tuned baseline design and the roofline-predicted optimum.

## Results

The roofline-guided design achieves substantially higher throughput and better resource utilization than manually tuned baseline accelerator designs, and the actual measured performance closely matches the roofline model's predictions, validating the model as a reliable guide for accelerator design-space exploration.

## Comparison with the state of the art

An early systematic alternative to the largely ad-hoc accelerator design practices common at the time, establishing analytical, model-guided design-space exploration as a standard methodology for subsequent FPGA (and more broadly, hardware) CNN accelerator design work.

## Strengths

Provides a principled, reusable design methodology rather than a one-off accelerator instance, generalizable to different FPGA platforms and different CNN architectures with relatively modest re-analysis effort.

## Weaknesses

The roofline model is a relatively coarse abstraction that does not capture every architectural detail (e.g. fine-grained memory-access patterns, control overhead), so the predicted optimum is only an approximate guide and final designs typically still require some empirical tuning.

## Limitations

Evaluated on CNN architectures and FPGA generations from the mid-2010s; does not address more recent concerns such as quantized/mixed-precision arithmetic, sparsity, or the very different resource profile of newer CNN architectures (e.g. depthwise-separable convolutions).

## Open questions

How should the roofline-guided design methodology be extended to account for quantized and sparse computation, where the compute/bandwidth balance differs substantially from the dense, full-precision convolutions originally analyzed?

## Possible extensions

Extending the roofline-based design-space exploration to quantized and structured-sparse CNN accelerators, and to newer, more efficient architectures (e.g. MobileNet-style depthwise-separable convolutions) whose compute/bandwidth characteristics differ from the AlexNet-class networks originally studied.

## Relevance to our research

An early systematic alternative to ad-hoc accelerator design that remains a standard reference methodology for FPGA-based CNN acceleration; relevant whenever the Observatory considers FPGA deployment of EdgeAI models and needs a principled way to reason about achievable throughput.

## Possible thesis topics

Applying the roofline-guided design-space exploration methodology to a quantized, depthwise-separable CNN (e.g. a MobileNet variant) on a modern low-cost FPGA, to test whether the same analytical framework still predicts near-optimal designs for these newer, more efficient architectures.

## Possible collaborations

FPGA and reconfigurable computing research groups working on accelerator design-space exploration and high-level synthesis for deep learning workloads.

## Links to related papers

[[2014_Chen_DianNao]]
