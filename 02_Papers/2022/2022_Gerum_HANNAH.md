# Hardware Accelerator and Neural Network Co-Optimization for Ultra-Low-Power Audio Processing Devices

**Full citation:** Gerum, C., Frischknecht, A., Hald, T., Palomero Bernardo, P., Lübeck, K., Bringmann, O. (2022). Hardware Accelerator and Neural Network Co-Optimization for Ultra-Low-Power Audio Processing Devices. arXiv:2209.03807. https://arxiv.org/abs/2209.03807

**Linked concepts:** [[DSP]], [[Keyword_Spotting]], [[NAS]]

## Abstract summary

The authors present HANNAH (Hardware Accelerator and Neural Network seArcH), a framework for automated, joint hardware/software co-design of deep neural networks and their corresponding hardware accelerators, targeting resource- and power-constrained edge devices such as those used for always-on audio/signal processing.

## Research problem

Manually co-optimizing a neural network architecture together with the digital-signal-processing-class hardware accelerator that will run it is a slow, expert-driven process with a huge joint design space (network architecture choices × accelerator architecture choices); for ultra-low-power audio devices, where both compute and power budgets are extremely tight, this manual process becomes a major bottleneck to exploring good design points.

## Key idea

Automate the joint search over neural network architecture and hardware accelerator configuration simultaneously, rather than optimizing the network first and then designing or selecting hardware for it afterward (or vice versa), so the search can find combinations that neither a network-only NAS nor a hardware-only design-space exploration would discover separately.

## Technical contribution

An integrated co-design framework (HANNAH) that couples a neural-architecture-search-style exploration of network design choices with an accelerator-configuration search, specifically scoped to the constraints of ultra-low-power audio processing devices (the kind of workload typically run on DSP-class hardware in always-on sensing applications).

## Experimental methodology

Applied to audio-processing neural network and accelerator co-design tasks representative of ultra-low-power, always-on sensing devices, exploring the joint network/hardware design space and evaluating resulting solutions on accuracy versus resource/power metrics relative to non-co-optimized baselines.

## Results

Demonstrates that joint network/accelerator search can surface design points that satisfy ultra-low-power constraints while retaining task accuracy, illustrating the practical value of treating model and hardware design as one combined search problem rather than two sequential, separately-optimized steps.

## Comparison with the state of the art

Distinct from hardware-aware NAS approaches that search the network architecture against a fixed or coarsely-parameterized hardware cost model (as in [[2019_Cai_OnceForAll]]), HANNAH searches the accelerator configuration itself jointly with the network, which is a more general (and more expensive) version of the hardware-awareness idea, specifically scoped to DSP-class audio accelerators.

## Strengths

Directly addresses a real practical pain point (manual co-design effort) in a domain — ultra-low-power always-on audio sensing — that is central to several entries in our Applications taxonomy (Keyword Spotting); automation of the joint search reduces dependence on hard-to-find expert co-design skills.

## Weaknesses

Joint network/accelerator search is computationally expensive, likely requiring proxy models or surrogate evaluation to be tractable (similar to the broader challenge in hardware-aware NAS, see [[NAS]]); scoped specifically to audio/DSP-class accelerators, so generality to other modalities/hardware classes is unproven within the paper itself.

## Limitations

As with most automated co-design frameworks, the quality of the discovered solutions depends heavily on the design space definition (which network and hardware parameters are exposed to the search) and on the accuracy of whatever proxy/simulation is used to estimate power and latency without full hardware fabrication for every candidate.

## Open questions

How does HANNAH's joint search compare, in solution quality and search cost, to a two-stage approach (hardware-aware NAS over a fixed accelerator family, as in [[2019_Cai_OnceForAll]], followed by light accelerator tuning)? Can the same joint-search philosophy be applied beyond DSP-class audio accelerators to other Hardware categories (e.g. NPU, FPGA)?

## Possible extensions

Extending HANNAH's joint network/accelerator search methodology to a different modality relevant to our taxonomy (e.g. biosignals or HAR), or comparing it directly against hardware-aware NAS on a fixed accelerator for the same audio task to quantify the benefit of also searching the hardware.

## Relevance to our research

Primary reference for the [[DSP]] branch of our Hardware taxonomy, with a direct link to [[Keyword_Spotting]] and to the broader [[NAS]] research direction, since it generalizes hardware-aware NAS to jointly search the accelerator as well as the network.

## Possible thesis topics

Comparative study of joint network/accelerator co-search (HANNAH-style) versus sequential hardware-aware NAS for a fixed audio sensing task, measuring search cost versus final solution quality; applying the co-design philosophy to a non-audio EdgeAI application in our taxonomy.

## Possible collaborations

Groups working on hardware-aware NAS and DSP/accelerator co-design for always-on sensing.

## Links to related papers

[[2019_Cai_OnceForAll]] (hardware-aware NAS, the closest related research direction), [[2018_Warden_SpeechCommands]] (representative dataset for the audio sensing tasks this hardware targets)
