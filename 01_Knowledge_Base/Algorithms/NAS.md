# NAS (Neural Architecture Search)

## Evolution of the concept

The field takes its name from Zoph and Le's "Neural Architecture Search with Reinforcement Learning" (ICLR 2017), which trains a recurrent-network controller with reinforcement learning to generate architecture descriptions, optimizing the controller against the validation accuracy of the architectures it proposes. In parallel, before automated search became affordable for resource-constrained targets, efficiency was achieved through manual design: MobileNet (Howard et al., 2017) introduces depthwise-separable convolutions and two global multipliers (width, resolution) as manual "knobs" for the accuracy/cost trade-off. The next step is to automate this search for efficient models specifically: Once-for-All (Cai et al., 2019) decouples training (done only once) from the search for the architecture specific to each hardware target, drastically reducing the cost of multi-platform hardware-aware NAS.

## Key papers

[[2017_Zoph_NeuralArchitectureSearchRL]] — the founding NAS paper; an RNN controller trained with reinforcement learning to generate and optimize network architectures.

[[2017_Howard_MobileNets]] — efficient-by-design architecture with manual hyperparameters, basis for much subsequent research.

[[2019_Cai_OnceForAll]] — "train once, deploy everywhere" paradigm for multi-platform hardware-aware NAS.

## Open problems

Extending the once-for-all paradigm to microcontrollers with extreme memory constraints, not just latency. Generalizing latency/accuracy predictors to hardware never seen during the predictors' own training.

## Research ideas

NAS with an explicit static memory-footprint constraint for Cortex-M; combining NAS with mixed-precision quantization to obtain already-quantized sub-networks ready for TinyML deployment.

## Possible thesis topics

Extension of Once-for-All with a memory constraint for microcontrollers; study of latency predictors on Cortex-M/RISC-V, underrepresented in the existing NAS literature.

## Links

[[Quantization]], [[Pruning]], [[Compression]]
