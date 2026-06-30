# A Multi-Mode 8K-MAC HW-Utilization-Aware Neural Processing Unit With a Unified Multi-Precision Datapath in 4-nm Flagship Mobile SoC

**Full citation:** Park, J.-S., Park, C., Kwon, S., Jeon, T., Kang, Y., Lee, H., Lee, D., Kim, J., Kim, H.-S., Lee, Y., et al. (2023). A Multi-Mode 8K-MAC HW-Utilization-Aware Neural Processing Unit With a Unified Multi-Precision Datapath in 4-nm Flagship Mobile SoC. IEEE Journal of Solid-State Circuits, 58(1), 189-202. https://ieeexplore.ieee.org/document/9916240

**Linked concepts:** [[NPU]], [[Cortex-A]]

## Abstract summary

The authors (Samsung) describe an NPU implemented in a 4-nm flagship mobile SoC featuring an 8K-MAC datapath, a unified multi-precision arithmetic design supporting several numeric formats within a single datapath, and hardware-utilization-aware scheduling to keep the large MAC array efficiently fed across varied real-world neural network workloads.

## Research problem

Mobile NPUs deployed across a wide range of model architectures and precisions (from highly quantized to higher-precision layers) typically lose efficiency when the MAC array's hardware utilization drops for certain layer shapes or precision combinations, since a fixed datapath optimized for one configuration underperforms on others.

## Key idea

Design a single, unified datapath that can flexibly support multiple precision modes without datapath duplication, and pair it with hardware-utilization-aware control logic that adapts scheduling to keep the 8K-MAC array busy across the full diversity of layer shapes and precisions found in real mobile AI workloads.

## Technical contribution

A unified multi-precision MAC datapath design avoiding the area overhead of separate fixed-precision datapaths; hardware-utilization-aware scheduling logic that adapts to per-layer characteristics to sustain high MAC-array utilization across diverse workloads.

## Experimental methodology

Silicon-level characterization of the fabricated 4-nm NPU integrated in a flagship mobile SoC, measuring throughput, hardware utilization, and energy efficiency across representative real-world mobile AI inference workloads with varying layer shapes and precision requirements.

## Results

The design sustains high hardware utilization of its 8K-MAC array across diverse precision modes and workload shapes, demonstrating that a unified multi-precision datapath with utilization-aware scheduling can avoid the efficiency losses typical of fixed-precision NPU datapaths.

## Comparison with the state of the art

Extends the DianNao-lineage fixed-function NPU design philosophy with an explicit multi-precision flexibility dimension, addressing a real-world deployment gap (workload precision diversity) that earlier, more narrowly fixed-precision NPU designs did not target.

## Strengths

Silicon-validated in an actual shipping flagship mobile SoC rather than only simulated; explicitly measures hardware utilization as a first-class metric rather than only raw peak TOPS.

## Weaknesses

As an industrial silicon design paper, architectural and scheduling details are reported at a level that may be less reproducible for academic follow-up work than an open-source accelerator design.

## Limitations

Evaluated within the specific 4-nm flagship SoC context; how the same unified-datapath approach scales down to lower-power, lower-cost mobile/edge tiers is not directly addressed.

## Open questions

How does this unified multi-precision datapath approach compare, in efficiency, to NXP's compiler-co-designed eIQ Neutron NPU approach to the same utilization problem? Could the utilization-aware scheduling principle be applied to NPUs paired with Cortex-M (rather than Cortex-A) class hosts?

## Possible extensions

Adapting the unified multi-precision datapath and utilization-aware scheduling principles to a lower-power edge/microcontroller-class NPU design; a comparative efficiency study against compiler-driven utilization optimization (eIQ Neutron-style) for the same workload diversity problem.

## Relevance to our research

Brings the NPU entry's mobile/Cortex-A-class accelerator coverage into the 2023-2026 window with a concrete, silicon-validated industrial design addressing the practical multi-precision utilization problem.

## Possible thesis topics

Comparing hardware-level utilization-aware scheduling (this paper) against compiler-level utilization optimization (eIQ Neutron) for the same NPU workload diversity challenge; evaluating whether mobile-NPU utilization-aware design principles transfer to edge/MCU-class NPUs.

## Possible collaborations

Groups working on mobile SoC NPU benchmarking and on cross-vendor NPU characterization (in the spirit of the Edge TPU evaluation already in this entry).

## Links to related papers

[[2014_Chen_DianNao]], [[2021_Yazdanbakhsh_EdgeTPUEvaluation]], [[2025_Bamberg_eIQNeutron]]
