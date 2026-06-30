# GAP-8: A RISC-V SoC for AI at the Edge of the IoT

**Full citation:** Flamand, E., Rossi, D., Conti, F., Loi, I., Pullini, A., Rotenberg, F., Benini, L. (2018). GAP-8: A RISC-V SoC for AI at the Edge of the IoT. *2018 IEEE 29th International Conference on Application-specific Systems, Architectures and Processors (ASAP)*, Milano, Italy. DOI/IEEE Xplore: https://ieeexplore.ieee.org/document/8445101

**Linked concepts:** [[RISC-V]], [[Vision]], [[Keyword_Spotting]]

## Abstract summary

The authors (GreenWaves Technologies / University of Bologna / ETH Zürich) present GAP-8, a multi-GOPS fully programmable RISC-V IoT-edge computing engine combining an 8-core RISC-V cluster with a CNN accelerator and an ultra-low-power MCU featuring 30 µW state-retentive sleep power, designed to let always-on, battery-powered IoT end-nodes process richer sensor data (image, video, audio, multi-axis motion) within a mW-range power envelope.

## Research problem

Always-on, battery-powered edge devices were largely confined to low-bandwidth sensors because the computational requirements of modern near-sensor data analysis (especially CNN-based) vastly exceed what a traditional ultra-low-power MCU can deliver within a milliwatt-range power budget, while general-purpose application processors are far too power-hungry for battery-constrained IoT end-nodes.

## Key idea

Combine a fully programmable RISC-V multi-core cluster (so the device is not locked to a fixed-function accelerator and can run varied workloads) with a dedicated hardware convolution engine and an extremely low sleep-power always-on domain, so the device can stay mostly asleep and only wake the compute cluster when richer processing (e.g. a CNN inference) is actually needed.

## Technical contribution

A complete, fabricated RISC-V system-on-chip architecture: an 8-core compute cluster built on the open RISC-V ISA, a hardware CNN accelerator tightly coupled to that cluster, and a separate always-on MCU domain with state-retentive sleep at 30 µW, demonstrating that an open instruction set architecture can support a commercially viable edge-AI SoC rather than only proprietary cores.

## Experimental methodology

Architectural description and on-chip measurements of the fabricated GAP-8 SoC, characterizing power consumption across operating modes (deep sleep, active compute) and computational throughput (multi-GOPS) on representative CNN-based edge workloads (image/audio near-sensor analysis), in the context of the IEEE ASAP conference's focus on application-specific architectures.

## Results

GAP-8 demonstrates that a fully programmable, open-ISA multi-core architecture with an integrated CNN accelerator can operate within the power envelope required by battery-powered, always-on IoT end-nodes, while remaining flexible enough (being RISC-V-programmable rather than fixed-function) to support a range of sensor modalities beyond a single hardwired application.

## Comparison with the state of the art

At publication, most ultra-low-power edge AI chips were either fixed-function ASICs (efficient but inflexible) or based on proprietary microcontroller cores; GAP-8 was among the first commercially-oriented RISC-V SoCs to combine general programmability with a dedicated CNN accelerator specifically for IoT-edge AI, contributing to RISC-V's broader adoption in the EdgeAI hardware space alongside platforms covered by our [[Cortex-M]] entry.

## Strengths

Open ISA (avoiding vendor lock-in, encouraging an open software/tooling ecosystem); genuine silicon implementation with measured power figures, not only simulation; a sleep/active architecture explicitly designed around the always-on, battery-constrained reality of IoT edge nodes.

## Weaknesses

As an architecture/SoC paper rather than a benchmark study, it reports relatively limited standardized accuracy/throughput comparisons against contemporaneous alternatives (e.g. ARM Cortex-M plus CMSIS-NN, or early NPU designs); software ecosystem maturity for RISC-V-based accelerators lagged behind the more established ARM tooling for several years after publication.

## Limitations

The paper predates the broader maturation of RISC-V vector extensions and the wider EdgeAI compiler ecosystem (TVM, MLIR-based tooling); GAP-8's fixed hardware convolution engine, while efficient for CNNs, is less flexible for other architectures (e.g. transformers, RNNs) that became more relevant for edge AI later.

## Open questions

How does GAP-8-style fixed CNN-accelerator-plus-RISC-V-cluster architecture compare, on equal workloads, to more recent flexible RISC-V vector-extension accelerators (e.g. Arrow, arXiv:2107.07169) or to Cortex-M-plus-CMSIS-NN solutions in terms of energy-per-inference for the same task? How well does the broader RISC-V compiler/toolchain ecosystem now (TVM, MLIR) support GAP-8-class hardware compared to when it launched?

## Possible extensions

A benchmark comparing GAP-8-class fixed-function CNN acceleration against more recent flexible RISC-V vector accelerators for both CNN and non-CNN (e.g. attention-based tiny models) workloads, to assess whether fixed-function efficiency still wins or whether flexible vector units have closed the gap.

## Relevance to our research

Foundational reference for the [[RISC-V]] branch of our Hardware taxonomy and for the GreenWaves Technologies vendor entry in `00_Config/sources.yaml`; relevant to any work targeting open-ISA, always-on EdgeAI hardware as an alternative to ARM Cortex-M.

## Possible thesis topics

Energy-per-inference benchmark of GAP-8-class RISC-V + CNN-accelerator hardware versus Cortex-M + CMSIS-NN for a fixed EdgeAI task (e.g. keyword spotting or simple vision); evaluation of current RISC-V toolchain (TVM/microTVM, MLIR) maturity for deploying non-CNN models on GAP-class hardware.

## Possible collaborations

GreenWaves Technologies; University of Bologna / ETH Zürich groups (PULP platform), already a monitored hardware vendor in `00_Config/sources.yaml`.

## Links to related papers

[[2018_Lai_CMSIS-NN]] (comparable ARM Cortex-M deployment stack), [[2018_Chen_TVM]] (compiler-based alternative for cross-hardware deployment, increasingly relevant to RISC-V targets)
