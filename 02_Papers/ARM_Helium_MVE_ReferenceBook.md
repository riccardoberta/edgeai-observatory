# Arm Helium Technology: M-Profile Vector Extension (MVE) for Arm Cortex-M Processors

**Full citation:** ARM. Arm Helium Technology: M-Profile Vector Extension (MVE) for Arm Cortex-M Processors. Reference Book, Arm Education. (Vendor source; no deep-analysis record previously existed.) https://armkeil.blob.core.windows.net/developer/Files/pdf/ebook/arm-helium-technology-mve.pdf

**Linked concepts:** [[Cortex-M]]

## Abstract summary

This is Arm's official technical reference book for Helium, the M-Profile Vector Extension (MVE) added to higher-end Cortex-M processors (such as Cortex-M55 and Cortex-M85), describing the vector instruction set, its programming model, and how it accelerates digital signal processing and machine learning workloads directly within the Cortex-M architecture rather than requiring a separate DSP or NPU.

## Research problem

Cortex-M microcontrollers historically relied on scalar instructions (or limited DSP extensions) for signal-processing and ML inference workloads, leaving substantial performance and energy efficiency on the table compared to what a wider, vector-style execution unit could achieve, without the cost, complexity, and board space of adding a separate DSP or NPU.

## Key idea

Add a vector instruction set extension (Helium/MVE) directly to the Cortex-M instruction-set architecture, so that a single, low-cost, low-power microcontroller core can execute the same kind of data-parallel multiply-accumulate operations that signal-processing and neural-network kernels are dominated by, without requiring a separate accelerator block.

## Technical contribution

The complete Helium/MVE instruction set architecture specification — vector register file, vector arithmetic and load/store instructions, predication for handling irregular loop trip counts — and the architectural integration approach that lets it coexist with the existing scalar Cortex-M pipeline; programming model guidance for compilers and libraries (such as CMSIS-NN) to target the new vector instructions.

## Experimental methodology

As a reference/specification document rather than an experimental research paper, this work documents the instruction set and its intended use rather than presenting novel benchmark results; performance characterization of Helium-accelerated kernels is published separately by Arm and by libraries (e.g. CMSIS-NN) that have added Helium-specific code paths.

## Results

Establishes the instruction set and programming model that subsequent CMSIS-NN and compiler work uses to deliver reported multi-fold speedups for signal-processing and ML-inference kernels on Helium-equipped Cortex-M55/M85 cores relative to scalar-only execution on earlier Cortex-M cores.

## Comparison with the state of the art

Positions Helium as a Cortex-M-native alternative to adding a separate DSP or NPU block for signal-processing/ML acceleration, trading some of the peak performance of a dedicated accelerator for tighter integration, lower system complexity, and a unified programming model within the existing Cortex-M software ecosystem.

## Strengths

Brings meaningful data-parallel acceleration to the same low-cost, low-power Cortex-M class of devices already widely deployed in TinyML, without requiring a new accelerator block or a separate toolchain; officially documented and supported by Arm's own compiler and library ecosystem (CMSIS-NN, CMSIS-DSP).

## Weaknesses

As a vendor reference document, it is necessarily Arm-specific and does not provide independent third-party benchmarking or a comparison against alternative vector-extension approaches (e.g. RISC-V vector extensions); actual achieved speedups depend heavily on how well a given kernel implementation (e.g. within CMSIS-NN) exploits the new instructions.

## Limitations

Only available on the subset of higher-end Cortex-M cores (M55, M85 and later) that implement Helium; many currently deployed TinyML devices use earlier Cortex-M cores (M4, M33) without this extension, limiting how broadly Helium-specific optimizations apply across the existing device fleet.

## Open questions

How much of CMSIS-NN's and TensorFlow Lite Micro's kernel coverage currently exploits Helium effectively, versus still running unoptimized scalar code paths on Helium-capable hardware? How does Helium's vector-instruction performance compare, in practice, to dedicated NPU offload for the same kernels on hardware that offers both options?

## Possible extensions

Extending CMSIS-NN/TFLM kernel coverage to fully exploit Helium across more operator types; a head-to-head comparison of Helium-vectorized execution versus dedicated low-power NPU offload for the same TinyML models on devices that support both.

## Relevance to our research

The official technical reference for the hardware capability that is currently named as an open problem in the [[Cortex-M]] knowledge-base entry, since CMSIS-NN/TFLM coverage of Helium remains limited; essential background for any thesis evaluating Helium-vectorized kernels.

## Possible thesis topics

Benchmarking the actual speedup obtained by Helium-vectorized CMSIS-NN kernels versus scalar Cortex-M execution across a representative set of TinyML model layers, to quantify how much of Helium's theoretical potential current library support actually realizes.

## Possible collaborations

Arm's own CMSIS-NN/CMSIS-DSP engineering teams and academic groups working on compiler auto-vectorization for M-Profile Vector Extension targets.

## Links to related papers

[[2006_Chellapilla_HighPerformanceCNNDocumentProcessing]]
