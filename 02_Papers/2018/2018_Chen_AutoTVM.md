# Learning to Optimize Tensor Programs

**Full citation:** Chen, T., Zheng, L., Yan, E., Jiang, Z., Moreau, T., Ceze, L., Guestrin, C., Krishnamurthy, A. (2018). Learning to Optimize Tensor Programs. *Advances in Neural Information Processing Systems 31 (NeurIPS 2018)*. https://proceedings.neurips.cc/paper_files/paper/2018/file/8b5700012be65c9da25f49408d959ca0-Paper.pdf

**Linked concepts:** [[microTVM_TVM]]

## Abstract summary

The authors present AutoTVM, a learned, statistical cost-model-guided auto-tuning system that automatically searches a tensor compiler's space of possible low-level implementations (loop tilings, orderings, vectorization choices) for a given operator and hardware target, replacing the need for hand-written, hardware-specific kernel libraries.

## Research problem

High-performance deep learning inference traditionally relies on hand-tuned kernel libraries (e.g. vendor BLAS/DNN libraries) written separately for each hardware target; this does not scale to the rapidly growing diversity of hardware backends (CPUs, GPUs, accelerators, microcontrollers) that a general tensor compiler like TVM needs to support.

## Key idea

Instead of hand-tuning each operator implementation for each hardware target, define a large space of candidate low-level schedules (loop transformations) for a given tensor operation, train a statistical machine learning cost model to predict which candidate schedules will run fast on the target hardware without having to execute all of them, and use this learned model to guide a search toward near-optimal schedules.

## Technical contribution

A machine-learning-based cost model (rather than a hand-built analytical performance model) that learns from actual hardware measurements to predict schedule performance; an efficient search/exploration strategy over the schedule space guided by this learned model; demonstrated automatic generation of kernels competitive with hand-tuned vendor libraries across CPU, GPU, and accelerator targets.

## Experimental methodology

Evaluates AutoTVM-generated operator implementations against hand-optimized vendor libraries (e.g. cuDNN, MKL-DNN) and other compiler-based approaches on standard deep learning operators (convolutions, matrix multiplications) across multiple hardware backends, measuring achieved throughput/latency and tuning time required.

## Results

AutoTVM-tuned kernels match or exceed the performance of hand-tuned vendor libraries on several hardware backends, demonstrating that a learned cost model can replace expert hand-tuning for generating high-performance tensor program implementations, while generalizing across very different hardware targets without per-target manual engineering.

## Comparison with the state of the art

A clear advance over both purely hand-tuned kernel libraries (which require per-hardware expert engineering effort) and purely analytical/heuristic auto-tuning approaches that predate the use of learned cost models, which typically achieved lower performance or required much larger search budgets.

## Strengths

Removes the need for hardware-specific hand-tuned kernels, making it practical for TVM to target a much wider and faster-growing range of hardware backends, including novel and embedded accelerators; the learned cost model approach generalizes better than fixed analytical models as hardware diversity grows.

## Weaknesses

The schedule search and cost-model training/data-collection process can be time-consuming, especially for new hardware targets without an existing trained cost model to start from; tuning quality depends on the quality and coverage of the search space definition for each operator.

## Limitations

Evaluated primarily on relatively powerful hardware backends (CPU/GPU/accelerators) of the time; applying the same auto-tuning methodology to extremely resource-constrained microcontroller targets (as in microTVM) introduces additional practical constraints (compile-time and on-device measurement cost) not fully explored in the original paper.

## Open questions

How can auto-tuning be made fast and practical for one-off or rapidly-iterating microcontroller targets, where collecting large amounts of on-device timing data for cost-model training is itself costly? Can cost models be transferred across similar hardware targets to reduce per-target tuning cost?

## Possible extensions

Cross-device transfer of learned cost models to new but similar hardware targets, reducing the tuning cost for each new microcontroller variant; tighter integration of auto-tuning with quantization-aware kernel generation for ultra-low-power targets.

## Relevance to our research

The specific learned-auto-tuning mechanism underlying TVM's (and microTVM's) ability to generate competitive kernels for the wide variety of EdgeAI hardware targets the Observatory tracks, without requiring hand-written kernels for each one.

## Possible thesis topics

Studying the practical cost and quality of AutoTVM-style auto-tuning specifically on a microcontroller target via microTVM, including how much tuning budget is needed to match a hand-written CMSIS-NN kernel.

## Possible collaborations

The TVM/microTVM compiler community and groups working on learned cost models for compiler auto-tuning.

## Links to related papers

[[2017_Howard_MobileNets]]
