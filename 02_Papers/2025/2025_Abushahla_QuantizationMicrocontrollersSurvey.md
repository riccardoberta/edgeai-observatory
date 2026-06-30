# Neural Network Quantization for Microcontrollers: A Comprehensive Survey of Methods, Platforms, and Applications

**Full citation:** Abushahla, H.A., Varam, D., Panopio, A.J.N., AlHajri, M.I. (2025). Neural Network Quantization for Microcontrollers: A Comprehensive Survey of Methods, Platforms, and Applications. arXiv:2508.15008. https://arxiv.org/abs/2508.15008

**Linked concepts:** [[CMSIS-NN]], [[Quantization]]

## Abstract summary

The authors survey quantized neural network deployment on microcontrollers, covering quantization methods, the hardware platforms that support them (ARM-based, RISC-V-based, and hybrid/NPU-enabled MCUs), and the software frameworks and runtime libraries — including CMSIS-NN-class kernel libraries — that enable quantized inference on these constrained devices.

## Research problem

Deploying quantized neural networks on microcontrollers involves balancing model accuracy, computational complexity, and tight memory constraints across a fragmented landscape of hardware platforms and supporting software toolchains, and a unified, up-to-date overview connecting quantization methods to the specific platforms and frameworks that support them was needed.

## Key idea

Provide a hardware-aware view of microcontroller quantization that explicitly connects quantization methods to the runtime libraries and hardware platforms that execute them, rather than treating quantization as a purely algorithmic topic decoupled from deployment infrastructure.

## Technical contribution

A structured survey connecting quantization methods to MCU hardware families (ARM Cortex-M, RISC-V, hybrid/NPU-enabled) and to the software frameworks/runtime libraries (including CMSIS-NN-class kernel libraries) that support quantized inference on each; a comparative discussion of deployment strategies and platform suitability across real-world application scenarios.

## Experimental methodology

As a survey, the paper does not run new experiments but systematically reviews and organizes existing quantization methods, hardware platforms, and software frameworks, drawing comparative conclusions about platform suitability for different application scenarios.

## Results

The survey documents that the choice of quantization method interacts strongly with the target MCU platform and its software stack (e.g. CMSIS-NN-optimized Cortex-M kernels behave differently than RISC-V or hybrid NPU-enabled targets), and that platform-aware quantization choices materially affect deployment outcomes.

## Comparison with the state of the art

Complements earlier, more algorithm-centric quantization surveys (and the original CMSIS-NN paper, which focuses on kernel implementation rather than surveying the broader quantization-method landscape) by explicitly bridging the algorithmic and platform/framework dimensions of MCU-class quantized deployment.

## Strengths

Up-to-date (2025) and broad coverage spanning methods, hardware, and frameworks; directly relevant to practical MCU deployment decisions; useful as a current reference for the state of the CMSIS-NN-centric Cortex-M software ecosystem alongside RISC-V and NPU-enabled alternatives.

## Weaknesses

As a survey, provides no new empirical validation of its own; breadth across methods/hardware/frameworks necessarily limits depth on any single framework (e.g. CMSIS-NN internals) compared to a dedicated technical paper.

## Limitations

Coverage of CMSIS-NN itself is contextual (as one of several supporting frameworks) rather than a deep technical update on CMSIS-NN's own kernel design since its original 2018 publication.

## Open questions

Has the CMSIS-NN kernel library itself made significant low-level algorithmic advances since 2018, or has the field's quantization progress been driven primarily by method-side (algorithmic) innovation layered on top of a relatively stable kernel library? How does CMSIS-NN compare to newer NPU-enabled MCU software stacks for the same quantized model?

## Possible extensions

A focused technical deep-dive specifically updating CMSIS-NN's kernel-level design against newer Cortex-M cores (M55/M85 with Helium) referenced elsewhere in our Hardware taxonomy.

## Relevance to our research

Useful as a current platform-aware reference connecting [[CMSIS-NN]] to the broader microcontroller quantization landscape, relevant when situating CMSIS-NN-based deployment decisions against RISC-V or NPU-enabled alternatives.

## Possible thesis topics

A platform-suitability study replicating this survey's comparative framework on real hardware, contrasting CMSIS-NN-based Cortex-M deployment against a RISC-V or NPU-enabled MCU for the same quantized model and task.

## Possible collaborations

Groups maintaining MCU quantization benchmarks and cross-platform embedded ML toolchains.

## Links to related papers

[[2018_Lai_CMSIS-NN]], [[2017_Jacob_QuantizationIntegerOnlyInference]]
