# Deploying Machine Learning Models to Ahead-of-Time Runtime on Edge Using MicroTVM

**Full citation:** Liu, C., Jobst, M., Guo, L., Shi, X., Partzsch, J., Mayr, C. (2023). Deploying Machine Learning Models to Ahead-of-Time Runtime on Edge Using MicroTVM. Proceedings of the 2023 Workshop on Compilers, Deployment, and Tooling for Edge AI (CODAI '23). https://arxiv.org/abs/2304.04842

**Linked concepts:** [[microTVM_TVM]]

## Abstract summary

The authors (TU Dresden) present an end-to-end code generator that parses a pre-trained model and produces C source libraries for bare-metal edge devices using microTVM, the embedded-targeting extension of the Apache TVM compiler stack, with a focus on offloading compute-intensive operators to dedicated accelerators via TVM's Universal Modular Accelerator (UMA) interface.

## Research problem

Deploying machine learning models on bare-metal embedded devices via an ahead-of-time (AOT) compilation flow — rather than a traditional interpreter-based runtime — requires generating efficient, statically-scheduled C code, and effectively distributing operators between general-purpose CPU cores and dedicated hardware accelerators present on the target device is non-trivial to automate.

## Key idea

Use microTVM's AOT executor to compile a trained model directly into C source code for bare-metal deployment, and leverage the UMA interface to identify and offload compute-intensive operators to a dedicated accelerator while keeping the remaining operators on the CPU, automating what would otherwise be a manual hardware/software partitioning decision.

## Technical contribution

A complete, demonstrated AOT deployment pipeline using microTVM targeting bare-metal devices (e.g. STM32, ESP32-class targets); a concrete demonstration of UMA-based operator offloading to a dedicated accelerator within this pipeline.

## Experimental methodology

Deployment of representative ML models through the microTVM AOT pipeline onto bare-metal embedded hardware, measuring which operators are successfully offloaded to the dedicated accelerator via UMA versus processed on CPU cores, and characterizing the resulting deployment workflow.

## Results

The microTVM AOT pipeline successfully compiles and deploys models to bare-metal hardware, with the UMA interface enabling specific compute-intensive operators to be offloaded to a dedicated accelerator while the CPU handles the remainder, demonstrating the practicality of this automated CPU/accelerator partitioning approach.

## Comparison with the state of the art

Distinguishes itself from interpreter-based embedded runtimes (such as TensorFlow Lite Micro) by using an ahead-of-time compilation approach native to the TVM compiler stack, and from earlier microTVM usage by concretely exercising the UMA interface for accelerator offloading rather than targeting CPU-only deployment.

## Strengths

Concrete, demonstrated end-to-end pipeline rather than a purely theoretical proposal; directly addresses the practical CPU/accelerator operator-partitioning problem; published at a dedicated edge-AI compiler workshop.

## Weaknesses

As a workshop paper, the evaluation scope (model diversity, hardware diversity) is narrower than a full conference paper would typically provide.

## Limitations

Demonstrated on a specific set of bare-metal targets and accelerators; generalization of the UMA-offloading approach to a broader range of dedicated accelerators is not exhaustively evaluated.

## Open questions

How well does the UMA-based offloading approach generalize across a wider diversity of dedicated accelerators beyond those tested? How does the AOT-compiled microTVM pipeline compare in code size and latency to a hand-tuned CMSIS-NN-based deployment for the same model?

## Possible extensions

A head-to-head comparison between microTVM's AOT/UMA pipeline and a CMSIS-NN-based deployment for the same model on the same Cortex-M hardware, measuring code size, latency, and engineering effort.

## Relevance to our research

A concrete, practical reference for the [[microTVM_TVM]] AOT deployment path and its accelerator-offloading capability via UMA, relevant when comparing microTVM against TFLM/CMSIS-NN as a deployment route.

## Possible thesis topics

Benchmarking microTVM's AOT/UMA-based deployment pipeline against TFLM/CMSIS-NN for the same model and target hardware, evaluating both performance and developer effort.

## Possible collaborations

Groups working on TVM/UMA accelerator integration and on bare-metal embedded compiler toolchains.

## Links to related papers

[[2018_Chen_AutoTVM]], [[2024_Hamdi_MATCH]]
