# MATCH: Model-Aware TVM-based Compilation for Heterogeneous Edge Devices

**Full citation:** Hamdi, M.A., Daghero, F., Sarda, G.M., Van Delm, J., Symons, A., Benini, L., Verhelst, M., Jahier Pagliari, D., Burrello, A. (2024). MATCH: Model-Aware TVM-based Compilation for Heterogeneous Edge Devices. arXiv:2410.08855. https://arxiv.org/abs/2410.08855

**Linked concepts:** [[microTVM_TVM]]

## Abstract summary

The authors (Politecnico di Torino, KU Leuven, IMEC, University of Bologna) present MATCH, a TVM-based deep neural network deployment framework designed for agile retargeting across different microcontroller processors and accelerators, focusing specifically on automating the tiling and loop-ordering decisions that strongly depend on the target hardware's architecture.

## Research problem

Retargeting a TVM-based deployment pipeline to a new MCU processor or accelerator typically requires substantial manual engineering effort to re-derive hardware-specific tiling and loop-ordering schedules, since these decisions are strongly hardware-dependent and TVM's existing automated scheduling does not generalize easily across heterogeneous MCU/accelerator combinations.

## Key idea

Introduce a customizable, model-based hardware abstraction layer within the TVM compilation flow that captures the key architectural parameters relevant to tiling and loop-ordering decisions, so that retargeting to a new MCU or accelerator becomes a matter of specifying the abstraction's parameters rather than re-engineering the scheduling logic from scratch.

## Technical contribution

The MATCH hardware-abstraction layer and its integration into the TVM compilation flow; an automated tiling/loop-ordering optimization procedure that uses this abstraction to maximize throughput and energy efficiency across heterogeneous MCU/accelerator targets.

## Experimental methodology

Deployment of representative DNN models across multiple distinct MCU processors and accelerators using the MATCH framework, measuring throughput and energy efficiency against both hand-tuned, hardware-specific baselines and against generic (non-model-aware) TVM scheduling.

## Results

MATCH achieves throughput and energy efficiency competitive with hand-tuned, hardware-specific deployment pipelines while requiring substantially less manual re-engineering effort to retarget across different MCU/accelerator combinations, demonstrating the practicality of the model-based hardware abstraction.

## Comparison with the state of the art

Extends the microTVM/TVM compilation line (including UMA-based accelerator offloading) by specifically targeting the agile-retargeting problem across heterogeneous MCU/accelerator combinations, an engineering bottleneck not directly addressed by earlier microTVM deployment demonstrations.

## Strengths

Directly addresses a genuine engineering pain point (retargeting cost) in deploying TVM-based pipelines across diverse MCU hardware; validated across multiple real MCU/accelerator targets; collaboration across multiple groups with strong compiler/hardware co-design expertise.

## Weaknesses

The abstraction layer's parameters must still be correctly specified for each new target, meaning some hardware-specific expertise remains necessary even if the engineering burden is reduced.

## Limitations

Evaluated on a specific set of MCU processors and accelerators; generalization of the abstraction to architecturally very different future accelerators is not guaranteed.

## Open questions

Can the model-based hardware abstraction be extended to automatically infer its own parameters from a hardware description, removing the remaining manual specification step? How does MATCH's retargeting agility compare to CMSIS-NN's more hardware-specific, hand-tuned kernel approach in terms of total engineering cost over multiple target platforms?

## Possible extensions

Automating the inference of MATCH's hardware-abstraction parameters from existing hardware description languages or datasheets, further reducing the manual retargeting burden.

## Relevance to our research

Directly relevant to the [[microTVM_TVM]] line of research on compiler-based, hardware-aware deployment, addressing the practical retargeting-cost problem across our Hardware taxonomy's heterogeneous targets (Cortex-M, RISC-V, NPU).

## Possible thesis topics

Using MATCH to retarget a single trained model across multiple distinct hardware platforms in our Hardware taxonomy, measuring both the engineering effort saved and the resulting throughput/energy trade-offs compared to hand-tuned deployment.

## Possible collaborations

Groups working on compiler-based hardware abstraction and on heterogeneous accelerator co-design.

## Links to related papers

[[2018_Chen_AutoTVM]], [[2023_Liu_MicroTVMAheadOfTime]]
