# NAS (Neural Architecture Search)

## Evolution of the concept

The field takes its name from Zoph and Le's "Neural Architecture Search with Reinforcement Learning" (ICLR 2017), which trains a recurrent-network controller with reinforcement learning to generate architecture descriptions, optimizing the controller against the validation accuracy of the architectures it proposes. In parallel, before automated search became affordable for resource-constrained targets, efficiency was achieved through manual design: MobileNet (Howard et al., 2017) introduces depthwise-separable convolutions and two global multipliers (width, resolution) as manual "knobs" for the accuracy/cost trade-off. The next step is to automate this search for efficient models specifically: Once-for-All (Cai et al., 2019) decouples training (done only once) from the search for the architecture specific to each hardware target, drastically reducing the cost of multi-platform hardware-aware NAS. More recently, hardware-aware NAS has begun extending beyond CNNs to other architecture families: HGNAS (Zhou et al., IEEE Transactions on Computers, 2024) adapts hardware-aware search to graph neural networks, a structurally different and largely unaddressed search space, by building a GNN-specific hardware-cost predictor and search space. A 2026-09-03 historical audit added the field's standard organizing reference, Elsken, Metzen, and Hutter's "Neural Architecture Search: A Survey" (JMLR 2019, 4900+ citations), which decomposes any NAS method into three axes — search space, search strategy, performance-estimation strategy — a framework hardware-aware NAS work (including this concept's own Garavagno anchor) implicitly extends with hardware cost as a further consideration; and Chitty-Venkata and Somani's "Neural Architecture Search Survey: A Hardware Perspective" (ACM Computing Surveys 2022, 169+ citations), the dedicated survey for exactly that hardware-aware extension.

## Key papers

[[2017_Zoph_NeuralArchitectureSearchRL]] — the founding NAS paper; an RNN controller trained with reinforcement learning to generate and optimize network architectures.

[[2019_Elsken_NASSurvey]] — the field's standard three-axis organizing taxonomy (search space, search strategy, performance estimation); the most-cited general NAS survey.

[[2022_ChittyVenkata_NASHardwarePerspectiveSurvey]] — dedicated survey for hardware-aware NAS specifically, extending Elsken et al.'s taxonomy with hardware-cost estimation and search-objective formulation.

[[2017_Howard_MobileNets]] — efficient-by-design architecture with manual hyperparameters, basis for much subsequent research.

[[2019_Cai_OnceForAll]] — "train once, deploy everywhere" paradigm for multi-platform hardware-aware NAS.

[[2024_Zhou_HGNAS]] — extends hardware-aware NAS to graph neural networks via a GNN-specific search space and hardware-cost predictor, addressing a structurally distinct and underexplored search domain.

[[2022_Gerum_HANNAH]] — jointly searches network architecture and hardware accelerator configuration together, rather than optimizing the network first and the hardware afterward, for always-on audio sensing.

[[2025_KumarM_MARVEL]] — automates the path from a high-level DNN model description to a model-class-aware RISC-V ISA extension and compiler support, treating accelerator-extension design itself as a searchable/generatable space rather than a hand-crafted one.

[[2026_Garavagno_HWNASUltraLowPower]] — derivative-free HW-NAS targeting the ultra-low-power tier (20-40 KiB RAM) below most prior HW-NAS work, with a search-host RAM constraint that makes the search itself runnable on constrained hardware (including a Raspberry Pi 4); directly addresses this entry's "extreme memory constraints" open problem.

[[2021_Banbury_MicroNets]] — differentiable NAS incorporating MCU SRAM/Flash/latency constraints directly into the search objective, deployed end-to-end via MicroTVM; highly cited (500+), added 2026-09-03 via the [[microTVM_TVM]] concept and cross-linked here.

## Open problems

Extending the once-for-all paradigm to microcontrollers with extreme memory constraints, not just latency. Generalizing latency/accuracy predictors to hardware never seen during the predictors' own training.

## Research ideas

NAS with an explicit static memory-footprint constraint for Cortex-M; combining NAS with mixed-precision quantization to obtain already-quantized sub-networks ready for TinyML deployment.

## Possible thesis topics

Extension of Once-for-All with a memory constraint for microcontrollers; study of latency predictors on Cortex-M/RISC-V, underrepresented in the existing NAS literature.

## Links

[[Quantization]], [[Pruning]], [[Compression]]
