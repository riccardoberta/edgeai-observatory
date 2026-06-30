# microTVM / TVM

## Evolution of the concept

TVM (Chen et al., 2018) was created to overcome the limits of hand-written libraries for every model/hardware combination (such as CMSIS-NN): it separates the representation of the computational graph from low-level code generation and uses auto-tuning guided by learnable cost models to automatically find the most efficient implementation for each operator and hardware target. microTVM is its evolution designed for microcontrollers. Recent work has pushed microTVM toward more concrete, practical deployment: Liu et al. (CODAI 2023) demonstrate an ahead-of-time compilation pipeline that generates bare-metal C code and offloads compute-intensive operators to a dedicated accelerator via TVM's Universal Modular Accelerator (UMA) interface, while MATCH (Hamdi et al., 2024) tackles the engineering cost of retargeting TVM-based deployment to a new MCU/accelerator combination by introducing a customizable, model-based hardware abstraction for tiling and loop-ordering decisions, reducing what was previously substantial manual re-engineering effort.

## Key papers

[[2018_Chen_TVM]] — end-to-end compiler with auto-tuning, performance comparable to hand-written libraries on CPU/GPU/FPGA without manual effort.

[[2018_Chen_AutoTVM]] — the learned cost-model-guided auto-tuning method underlying TVM's per-operator code generation; the specific mechanism that lets TVM match hand-written kernels without manual tuning.

[[2023_Liu_MicroTVMAheadOfTime]] — ahead-of-time microTVM deployment pipeline for bare-metal devices with UMA-based accelerator offloading.

[[2024_Hamdi_MATCH]] — model-based hardware abstraction for agile retargeting of TVM-based tiling/loop-ordering optimization across heterogeneous MCU/accelerator combinations.

[[2020_Lattner_MLIR]] — the extensible compiler-infrastructure (dialects, progressive lowering) that TVM-adjacent toolchains, including ONNX-MLIR, build on or interoperate with.

## Open problems

How well TVM's auto-tuning scales to microcontrollers with limited profiling resources. Reducing the cost of auto-tuning search to make it practical without large compute clusters.

## Research ideas

microTVM as a "compiler-based" alternative to hand-written kernels (CMSIS-NN) for Cortex-M/RISC-V; more efficient auto-tuning for scenarios with limited compute resources for the search itself.

## Possible thesis topics

Systematic comparison between microTVM and CMSIS-NN/TFLM on a common set of models and Cortex-M targets, in terms of performance, memory footprint, and development time.

## Links

[[CMSIS-NN]], [[TensorFlow Lite Micro]], [[Cortex-M]], [[RISC-V]]
