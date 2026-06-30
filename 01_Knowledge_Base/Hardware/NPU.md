# NPU

## Evolution of the concept

Neural processing units (NPUs) emerged as fixed-function, ASIC-class accelerators specifically designed for neural network inference. The line starts with Chen et al.'s DianNao (ASPLOS 2014), the first widely-cited small-footprint ASIC accelerator design specifically for machine-learning workloads, which established the basic architectural recipe (dedicated on-chip buffers and a fixed-function arithmetic datapath to avoid the memory-bandwidth and energy cost of general-purpose CPU/GPU execution) that essentially all later NPU designs build on. NPUs now ship inside everything from mobile Cortex-A SoCs (as surveyed in [[Cortex-A]]) to dedicated edge devices such as Google's Coral/Edge TPU products. Early evaluation relied largely on vendor-reported peak performance figures; the field's understanding deepened substantially with large-scale empirical characterization studies that swept hundreds of thousands of CNN variants across real NPU hardware, surfacing interpretable microarchitectural bottlenecks and enabling learned performance/energy estimators that can substitute for exhaustive on-device measurement — a capability directly useful for hardware-aware neural architecture search.

## Key papers

[[2014_Chen_DianNao]] — the foundational fixed-function NN accelerator ASIC architecture, establishing the dedicated-buffer/fixed-datapath design pattern that essentially all subsequent NPUs (including mobile and edge NPUs) descend from.

[[2021_Yazdanbakhsh_EdgeTPUEvaluation]] — large-scale empirical characterization of Edge TPU accelerators across roughly 423,000 CNN variants, producing microarchitectural insights and learned latency/energy estimators.

## Open problems

How well do learned latency/energy estimators generalize to non-CNN architectures (small transformers, RNNs) now common in TinyML research? How do Edge TPU's microarchitectural bottlenecks compare to other NPU families (ARM Ethos, CEVA NeuPro) on the same model set — is there a generalizable theory of NPU bottlenecks, or is it largely vendor-specific?

## Research ideas

Building an analogous large-scale performance-characterization study for a different NPU family (e.g. ARM Ethos-U used alongside Cortex-M) to test the generality of the learned-estimator approach.

## Possible thesis topics

Extending Edge TPU-style empirical characterization to non-CNN model families; using learned NPU performance proxies as a fast hardware-aware fitness function inside a [[NAS]] search loop.

## Links

[[NAS]], [[Cortex-A]], [[FPGA]], [[RISC-V]]
