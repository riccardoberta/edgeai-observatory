# NAS (Neural Architecture Search)

Neural Architecture Search automates the design of a network's architecture — how many layers, what type, how wide — instead of a human hand-designing it. "Hardware-aware" NAS additionally optimizes the search for a specific hardware target's accuracy/cost trade-off, rather than treating architecture design and deployment hardware as separate concerns.

## Evolution of the concept

The field takes its name from Zoph and Le's "Neural Architecture Search with Reinforcement Learning" (ICLR 2017), which trains a recurrent-network "controller" using reinforcement learning to generate architecture descriptions, optimizing the controller against the validation accuracy of the architectures it proposes. Elsken, Metzen, and Hutter's survey (JMLR 2019) became the field's standard organizing reference, decomposing any NAS method into three axes: the search space (which architectures are considered at all), the search strategy (how the space is explored), and the performance-estimation strategy (how a candidate architecture's quality is judged without fully training it). Chitty-Venkata and Somani's survey (ACM Computing Surveys, 2022) extends that same taxonomy specifically to hardware-aware NAS, adding hardware-cost estimation and search-objective formulation as further considerations.

Before automated search became affordable for resource-constrained targets, efficiency was achieved through manual design: MobileNet (Howard et al., 2017) introduces depthwise-separable convolutions (a cheaper alternative to standard convolution that factors it into two simpler steps) and two global multipliers — width and resolution — as manual "knobs" for trading accuracy against computational cost. The next step was to automate this search for efficient models specifically. Once-for-All (Cai et al., 2019) decouples training, done only once, from the search for the architecture specific to each hardware target, drastically reducing the cost of hardware-aware NAS across multiple platforms.

Hardware-aware NAS has since extended beyond CNNs to other architecture families: HGNAS (Zhou et al., 2024) adapts hardware-aware search to graph neural networks — a structurally different and largely unaddressed search space — by building a GNN-specific hardware-cost predictor and search space. Gerum et al. (2022) jointly search network architecture and hardware accelerator configuration together, rather than optimizing the network first and the hardware afterward, for always-on audio sensing. Kumar M et al. (2025) push automation further still, generating a model-class-aware RISC-V instruction-set-architecture extension and its compiler support directly from a high-level neural-network description — treating accelerator-extension design itself as a searchable, generatable space rather than a hand-crafted one.

At the extreme low-power end, Garavagno et al. (2026) run a derivative-free hardware-aware NAS that bounds the searched CNN's RAM, Flash, and multiply-accumulate operations directly in the search objective, producing architectures sized for 20–40 KiB RAM targets — below most prior hardware-aware NAS work — with a search process light enough to run on constrained search-host hardware itself (including a Raspberry Pi 4). Banbury et al.'s MicroNets (2021) take a related approach a tier up: a differentiable NAS that incorporates microcontroller SRAM/Flash/latency constraints directly into the search objective and deploys the result end to end via microTVM (see [[microTVM_TVM]]).

## Key papers

[[2017_Zoph_NeuralArchitectureSearchRL]] — the founding NAS paper; an RNN controller trained with reinforcement learning to generate and optimize network architectures.

[[2019_Elsken_NASSurvey]] — the field's standard three-axis organizing taxonomy (search space, search strategy, performance estimation); the most-cited general NAS survey.

[[2022_ChittyVenkata_NASHardwarePerspectiveSurvey]] — dedicated survey for hardware-aware NAS specifically, extending Elsken et al.'s taxonomy with hardware-cost estimation and search-objective formulation.

[[2017_Howard_MobileNets]] — efficient-by-design architecture with manually chosen hyperparameters, the basis for much subsequent research.

[[2019_Cai_OnceForAll]] — "train once, deploy everywhere" paradigm for multi-platform hardware-aware NAS.

[[2024_Zhou_HGNAS]] — extends hardware-aware NAS to graph neural networks via a GNN-specific search space and hardware-cost predictor, addressing a structurally distinct and underexplored search domain.

[[2022_Gerum_HANNAH]] — jointly searches network architecture and hardware accelerator configuration together, rather than optimizing the network first and the hardware afterward, for always-on audio sensing.

[[2025_KumarM_MARVEL]] — automates the path from a high-level neural-network description to a model-class-aware RISC-V instruction-set-architecture extension and compiler support, treating accelerator-extension design itself as a searchable space.

[[2026_Garavagno_HWNASUltraLowPower]] — derivative-free hardware-aware NAS targeting the ultra-low-power tier (20–40 KiB RAM), below most prior work, with a search process light enough to run on a Raspberry Pi 4.

[[2021_Banbury_MicroNets]] — differentiable NAS incorporating microcontroller SRAM/Flash/latency constraints directly into the search objective, deployed end to end via microTVM.

## Open problems

Extending the once-for-all paradigm to microcontrollers with extreme memory constraints, not just latency constraints. Generalizing latency/accuracy predictors to hardware never seen during the predictors' own training.

## Research ideas

NAS with an explicit static memory-footprint constraint for Cortex-M. Combining NAS with mixed-precision quantization to obtain already-quantized sub-networks ready for TinyML deployment.

## Possible thesis topics

An extension of Once-for-All with a memory constraint for microcontrollers. A study of latency predictors on Cortex-M/RISC-V, currently underrepresented in the NAS literature.

## Links

[[Quantization]], [[Pruning]], [[Compression]]
