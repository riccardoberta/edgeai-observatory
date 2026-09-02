# Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks

**Full citation:** Chen, Y.-H., Krishna, T., Emer, J.S., Sze, V. (2017). Eyeriss: An Energy-Efficient Reconfigurable Accelerator for Deep Convolutional Neural Networks. *IEEE Journal of Solid-State Circuits*, 52(1), 127–138. DOI: 10.1109/JSSC.2016.2616357

**PDF:** [DOI](https://doi.org/10.1109/JSSC.2016.2616357) · project page: [eyeriss.mit.edu](http://eyeriss.mit.edu/energy.html)

**Verification note:** Bibliographic details (authors, venue, volume/pages, DOI) confirmed via WebSearch cross-referencing dblp and the MIT project page. IEEE Xplore itself returns a client-rendered, non-fetchable page, so this record is based on the paper's abstract and widely-cited technical summary rather than a full-text read — flagged here as abstract-level verified, not full-text-verified.

**Linked concepts:** [[NPU]]

## Abstract summary

Eyeriss is a 65 nm CNN accelerator chip from MIT that introduced the Row-Stationary (RS) dataflow, a data-movement scheme designed to minimize energy spent moving data across the memory hierarchy (DRAM, global buffer, and a spatial array of processing elements with local register files) rather than only minimizing arithmetic operations. It remains one of the most cited hardware-accelerator papers in the EdgeAI/NPU literature and established energy-per-MAC, driven by data movement rather than compute, as the central design metric for CNN accelerators.

## Research problem

Early CNN accelerators optimized primarily for throughput or peak compute utilization, but for battery-powered and embedded devices energy consumption is dominated by data movement (reading/writing activations and weights across the memory hierarchy), not by the multiply-accumulate operations themselves. No systematic dataflow taxonomy existed for reasoning about how a given dataflow affects energy consumption across the memory hierarchy.

## Key idea

Classify CNN accelerator dataflows (weight-stationary, output-stationary, no local reuse, row-stationary) by what they hold stationary in local storage, and introduce the Row-Stationary dataflow, which maximizes reuse of filter weights and partial sums within each processing element's row-based computation, exploiting all three forms of data reuse (convolutional, filter, and image reuse) simultaneously rather than optimizing for only one.

## Technical contribution

The Row-Stationary dataflow and its instantiation in a fabricated 65 nm test chip with a 12×14 spatial PE array, local register-file-based reuse, and an on-chip global buffer; a companion energy model and dataflow taxonomy that became a standard reference framework for comparing subsequent CNN accelerators (including later NPU designs in this KB, such as [[NPU]] entries built on systolic or spatial array architectures).

## Experimental methodology

Fabricated 65 nm CMOS test chip, evaluated on AlexNet convolutional layers; energy breakdown measured across ALU, register file, NoC, and DRAM access to demonstrate where the Row-Stationary dataflow reduces movement relative to alternative dataflows, plus analytical/simulated comparison of RS against weight-stationary, output-stationary, and no-local-reuse dataflows on the same workload.

## Results

The Row-Stationary dataflow was shown to reduce total energy consumption relative to competing dataflows primarily by increasing reuse at the lowest, cheapest level of the memory hierarchy (the register file), with reported energy efficiency substantially better than prior accelerator designs of the era; the chip demonstrated real-time AlexNet inference at low power suitable for mobile/embedded deployment.

## Comparison with the state of the art

Positioned against earlier accelerators (e.g. DianNao-family designs) that primarily targeted compute-array utilization; Eyeriss instead reframed the design problem around the memory hierarchy and data-movement energy, a framing that subsequent NPU literature (including systolic-array and dataflow-flexible designs) explicitly builds on or contrasts against.

## Strengths

Rigorous, quantitative energy-per-access accounting across the full memory hierarchy rather than only counting operations; a general dataflow taxonomy reusable well beyond this one chip; silicon-validated (not just simulated) results.

## Weaknesses

Evaluated only on early-2010s CNN workloads (AlexNet-era); does not address the quantization, sparsity, or transformer/attention workloads that dominate more recent NPU and on-device inference discussions.

## Limitations

65 nm technology node is far from modern edge-NPU process nodes; the chip's spatial array size and buffer capacity reflect mid-2010s silicon budgets and are not directly comparable to current commercial edge NPUs (e.g. Arm Ethos, Qualcomm/Apple NPUs).

## Open questions

How does the Row-Stationary dataflow's energy advantage change under structured/unstructured sparsity and low-bit quantization, both now standard in edge deployment? Does RS remain optimal for non-convolutional workloads (attention, depthwise-separable convolutions) common in modern efficient architectures?

## Possible extensions

Re-deriving the RS dataflow's energy analysis for modern efficient architectures (MobileNet-style depthwise-separable convolutions, transformer blocks) and for sparse/quantized weights, to assess whether the same reuse principles still dominate the energy budget on current workloads.

## Relevance to our research

Foundational reference for [[NPU]]: establishes the vocabulary (dataflow taxonomy, data-movement-centric energy accounting) used throughout the Observatory's Hardware branch when comparing accelerator designs, and is a natural anchor citation whenever a new NPU paper claims an energy or dataflow innovation.

## Possible thesis topics

A quantitative comparison of Row-Stationary-style dataflows against flexible/reconfigurable dataflows (e.g. as used in more recent RISC-V-integrated NPUs such as [[2026_Tanase_DualCoreRISCVEdgeAI]]) on modern quantized, sparse workloads, measuring whether the mid-2010s reuse principles still hold.

## Possible collaborations

Hardware-architecture groups working on accelerator dataflow design and energy modeling (successors to the MIT Eyeriss line, e.g. Sze/Emer's continued work on accelerator design-space exploration tools such as Timeloop/Accelergy).

## Links to related papers

[[2026_Tanase_DualCoreRISCVEdgeAI]]
