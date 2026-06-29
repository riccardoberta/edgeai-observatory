# microTVM / TVM

## Evolution of the concept

TVM (Chen et al., 2018) was created to overcome the limits of hand-written libraries for every model/hardware combination (such as CMSIS-NN): it separates the representation of the computational graph from low-level code generation and uses auto-tuning guided by learnable cost models to automatically find the most efficient implementation for each operator and hardware target. microTVM is its evolution designed for microcontrollers.

## Key papers

[[2018_Chen_TVM]] — end-to-end compiler with auto-tuning, performance comparable to hand-written libraries on CPU/GPU/FPGA without manual effort.

## Open problems

How well TVM's auto-tuning scales to microcontrollers with limited profiling resources. Reducing the cost of auto-tuning search to make it practical without large compute clusters.

## Research ideas

microTVM as a "compiler-based" alternative to hand-written kernels (CMSIS-NN) for Cortex-M/RISC-V; more efficient auto-tuning for scenarios with limited compute resources for the search itself.

## Possible thesis topics

Systematic comparison between microTVM and CMSIS-NN/TFLM on a common set of models and Cortex-M targets, in terms of performance, memory footprint, and development time.

## Links

[[CMSIS-NN]], [[TensorFlow Lite Micro]], [[Cortex-M]], [[RISC-V]]
