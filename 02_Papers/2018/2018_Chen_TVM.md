# TVM: An Automated End-to-End Optimizing Compiler for Deep Learning

**Full citation:** Chen, T., Moreau, T., Jiang, Z., Zheng, L., Yan, E., Shen, H., Cowan, M., Wang, L., Hu, Y., Ceze, L., Guestrin, C., Krishnamurthy, A. (2018). TVM: An Automated End-to-End Optimizing Compiler for Deep Learning. *13th USENIX Symposium on Operating Systems Design and Implementation (OSDI 18)*, pp. 578–594. arXiv:1802.04799. https://arxiv.org/abs/1802.04799

**Linked concepts:** [[microTVM_TVM]]

## Abstract summary

The authors present TVM, an end-to-end compiler that takes a deep learning model expressed in different frameworks (TensorFlow, PyTorch, etc.) and generates optimized code for a wide range of hardware backends (CPU, GPU, dedicated accelerators), automating optimizations that previously required hand-written libraries for each model/hardware combination.

## Research problem

Every new combination of model and hardware traditionally required hand-optimized kernel libraries (like CMSIS-NN for Cortex-M), an approach that does not scale as the variety of model architectures and target hardware grows.

## Key idea

Separate the representation of the computational graph from low-level code generation, using an explorable scheduling space (with machine-learning-guided search) to find, for each operator and each hardware target, the most efficient implementation automatically, without hand-writing kernels.

## Technical contribution

An intermediate representation of the computational graph (graph-level IR) and of the tensor (tensor-level IR, Halide-like); an auto-tuning mechanism based on learnable cost models to automatically explore the scheduling space (tiling, vectorization, parallelization).

## Experimental methodology

Benchmarks on several standard CNN models and several backends (server CPU, GPU, FPGA, and a custom accelerator), comparing the performance of TVM-generated code against hand-optimized libraries (e.g. cuDNN) and against other compilation frameworks.

## Results

TVM achieves performance comparable to or better than hand-written libraries on several backends, and above all allows obtaining this performance on new hardware (e.g. FPGA, custom accelerators) without the manual effort required by approaches like CMSIS-NN.

## Comparison with the state of the art

Compared to hand-written hardware-specific libraries (cuDNN, CMSIS-NN), TVM automates the optimization process, trading a bit of peak performance for portability and speed of adaptation to new hardware.

## Strengths

General and portable approach, very active open-source community, basis for microTVM (a variant specific to microcontrollers) and for many subsequent ML compiler projects.

## Weaknesses

Auto-tuning can require significant search time for each new model/hardware combination; peak performance on highly specialized hardware can remain slightly below hand-written libraries built by experts in that specific hardware.

## Limitations

The original paper focuses on "medium-sized" CPU/GPU/FPGA; extension to microcontrollers with extreme memory constraints requires the subsequent evolution (microTVM), not covered in detail here.

## Open questions

How well does TVM's auto-tuning scale to microcontrollers with limited profiling resources? How to reduce the cost of auto-tuning search to make it practical even for researchers without large compute clusters?

## Possible extensions

microTVM to generate optimized code directly for Cortex-M/RISC-V, as a "compiler-based" alternative to hand-written kernels like CMSIS-NN.

## Relevance to our research

Relevant for comparing the "automatic compiler" approach (TVM/microTVM) with the "hand-written kernel" approach (CMSIS-NN, TensorFlow Lite Micro) when choosing the deployment stack for TinyML experiments.

## Possible thesis topics

Systematic comparison between microTVM and CMSIS-NN/TFLM on a common set of models and Cortex-M targets, in terms of performance, memory footprint, and development time needed to support a new model.

## Possible collaborations

The Apache TVM community, groups working on compilers for dedicated NPU/FPGA edge accelerators.

## Links to related papers

[[2021_David_TensorFlowLiteMicro]], [[2018_Lai_CMSIS-NN]]
