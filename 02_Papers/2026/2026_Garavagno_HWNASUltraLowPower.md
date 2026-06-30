# An Affordable Hardware-Aware Neural Architecture Search for Deploying Convolutional Neural Networks on Ultra-Low-Power Computing Platforms

**Full citation:** Garavagno, A. M., Ragusa, E., Frisoli, A., Gastaldo, P. (2026). An affordable hardware-aware neural architecture search for deploying convolutional neural networks on ultra-low-power computing platforms. arXiv:2606.16290 [cs.LG]. Submitted 15 June 2026. Accepted for publication in *IEEE Sensors Letters*; final publication at https://doi.org/10.1109/LSENS.2024.3387056. Code: https://github.com/AndreaMattiaGaravagno/NanoNAS. Funded by the Italian PNRR project "LEARN."

**Linked concepts:** [[NAS]], [[Cortex-M]], [[Compression]]

## Abstract summary

The authors propose a lightweight, derivative-free hardware-aware NAS (HW-NAS) targeting ultra-low-power microcontrollers (20–40 KiB RAM class), explicitly distinct from prior HW-NAS work that targets higher-performance MCUs. The search itself can run on resource-constrained hardware, including a Raspberry Pi 4, by formulating an optimization problem that bounds not only the resulting CNN's RAM/Flash/MAC budget but also the RAM available on the device hosting the search.

## Research problem

Prior HW-NAS frameworks (µNAS, MCUNet, Micronets) target relatively high-performance MCUs (e.g., the paper's Table 1 reference point: STM32 F412ZG with 256 KiB RAM, 1024 KiB Flash, 608 CoreMark) and typically require GPU-based search infrastructure (MCUNet: >300 h on GPU). Neither the resulting architectures nor the search process itself are designed for the ultra-low-power tier (here as low as 20 KiB RAM, 75 CoreMark) common in always-on sensing applications.

## Key idea

Formulate the architecture search as an optimization problem P that maximizes validation accuracy f(x) subject to RAM, Flash, and MAC constraints on the resulting CNN (ξ_R, ξ_F, ξ_M) and an additional constraint θ(x) ≤ Θ_T on the RAM available on the device that hosts the search process itself. A derivative-free search strategy incrementally grows kernel count k and, for each k, cell count c until validation accuracy stops improving, scoring any training run that exceeds resource limits as f=0 so the search degrades gracefully rather than crashing on constrained hosts.

## Technical contribution

A cell-wise search space (preprocessing → conv layer with k kernels → c cells [maxpool + batchnorm + conv] → classifier with global-average-pool + dropout + softmax) with kernel count per cell following n_c = k if c=0, else ⌈(2 − Σ2^(-i))·n_(c-1)⌉; an early-stopping regularization strategy using only 3 training epochs during search (vs. 100 for final training), shown to select the same best CNN as 100-epoch search with >78% probability (Fig. 1); and explicit validation that the search itself runs on a Raspberry Pi 4 (4 GB RAM) without a GPU, not just that the resulting CNN runs on an MCU.

## Experimental methodology

Hardware-aware evaluation on three STM32 MCUs spanning the ultra-low-power tier: L010RBT6 (20 KiB RAM / 128 KiB Flash / 75 CoreMark), L151UCY6DTR (32 KiB / 256 KiB / 93 CoreMark), L412KBU3 (40 KiB / 128 KiB / 273 CoreMark). Three datasets: Visual Wake Words (50×50), CIFAR-10 (32×32), Melanoma Skin Cancer (50×50). For each (MCU, dataset) pair the search reports the selected (k,c) architecture, search wall-clock time, resulting RAM/Flash/MAC, test accuracy, and measured inference latency. The Visual Wake Words search on the L4-class target is additionally repeated on a Raspberry Pi 4 to confirm the search itself is embeddable.

## Results

Representative Table 2 results: on Visual Wake Words, the L0 target selects (k=3,c=3) in 1:39h, giving 20 KiB RAM / 10.7 KiB Flash / 0.41 MMAC, 71.7% accuracy, 56.2 ms latency; the L4 target selects (k=6,c=4) in 3:17h, giving 28.5 KiB RAM / 23.7 KiB Flash / 1.27 MMAC, 77% accuracy, 87.9 ms latency. The same L4/VWW search repeated on a Raspberry Pi 4 takes 34:29h, confirming feasibility without a GPU. Table 3 SOTA comparison on VWW: the proposed method (L4 target) reaches 77% accuracy at 28.5 KiB RAM / 23.7 KiB Flash / 1.3 MMAC with a 3:17h CPU (1:08h GPU) search; ColabNAS reaches 77.6% but needs 31.5 KiB RAM / 20.83 KiB Flash / 2 MMAC and a 7:09h CPU search; Micronets reaches 76.8% but needs 70.5 KiB RAM / 273.8 KiB Flash / 3.3 MMAC; MCUNet reaches the highest accuracy (87.4%) but requires 168.5 KiB RAM / 530.5 KiB Flash / 6 MMAC and >300h of GPU search — resource levels the paper notes cannot be hosted on the ultra-low-power MCUs targeted here (citing prior work showing MobileNetV2 needs ≥256 KB RAM for VWW).

## Comparison with the state of the art

Matches or approaches the accuracy of ColabNAS and Micronets on Visual Wake Words while using less RAM/Flash/MAC and a substantially cheaper search (no GPU required, runs even on a Raspberry Pi 4). Does not match MCUNet's accuracy, but MCUNet's resulting architecture is explicitly infeasible on the ultra-low-power devices this paper targets — the comparison is therefore an accuracy/resource trade-off across a different operating point, not a strict win.

## Strengths

Directly targets a genuinely underserved ultra-low-power tier (20–40 KiB RAM) rather than the already well-covered higher-performance MCU tier; the search-host RAM constraint is a distinctive and practically useful addition — it means the NAS itself, not just its output, is deployable on constrained infrastructure; public code repository; concrete latency measurements on real STM32 hardware, not just simulated figures; early-stopping ablation (Fig. 1) gives empirical justification for the 3-epoch search shortcut rather than asserting it.

## Weaknesses

Search space is restricted to a single cell-wise CNN template (conv + pool/batchnorm/conv cells), so the method does not explore the architectural diversity of more general NAS frameworks. Evaluated on only three datasets, all relatively small/simple by modern vision standards (50×50 or 32×32 images). The paper acknowledges it is not competitive for high-performance-MCU targets, where traditional NAS or hand-crafted architectures remain preferable — this is a deliberately narrow niche, which is a strength for the stated problem but limits general applicability.

## Limitations

Large training datasets may pose a problem for genuinely on-device search (the Raspberry Pi 4 run already takes over a day); no exploration of how the method scales to datasets larger than the three tested; no discussion of how training-time memory (not just final-model memory) is bounded during the search itself on the most constrained hosts.

## Open questions

How does the search-host RAM constraint scale to datasets an order of magnitude larger? Can the cell-wise search space be extended to other operator types (depthwise/separable convolutions, attention) without breaking the ultra-low-power host-RAM guarantee? How sensitive is the 3-epoch early-stopping shortcut to dataset difficulty — does it still hold >78% agreement on harder tasks than VWW/CIFAR-10/Melanoma?

## Possible extensions

Extending the search space to depthwise-separable or grouped convolutions while preserving the host-RAM-bounded search property; applying the same affordable-search philosophy to non-vision sensing tasks (audio keyword spotting, inertial HAR) on the same ultra-low-power MCU tier; combining with the NVFP4/quantization line ([[2026_Sen_NVFP4QuantizationEdgeAI]]) to see whether quantization-aware search further shrinks the Pareto frontier on these devices.

## Relevance to our research

A strong, directly relevant addition to the Observatory's [[NAS]] line, specifically filling the ultra-low-power [[Cortex-M]] niche that most HW-NAS literature skips. The search-affordability angle (running NAS itself on constrained hardware) is a distinct contribution worth tracking separately from accuracy/resource trade-offs of the resulting CNNs, and connects to [[Compression]] given the explicit RAM/Flash/MAC budgeting.

## Possible thesis topics

Extending NanoNAS's search space to non-vision sensing modalities (audio, inertial) on the same ultra-low-power MCU class; a systematic study of how the 3-epoch early-stopping shortcut's reliability varies with task difficulty; combining hardware-aware NAS with post-training or quantization-aware compression on the resulting architectures to push further into the ultra-low-power Pareto frontier.

## Possible collaborations

The authors (Garavagno, Ragusa) are at DITEN — the Department of Electrical, Electronic, Telecommunications Engineering and Naval Architecture at the **University of Genoa**, the same institution as this Observatory — making this a strong candidate for a direct, local collaboration rather than only a literature reference. The public NanoNAS repository (https://github.com/AndreaMattiaGaravagno/NanoNAS) is a concrete starting point for joint work or extension.

## Links to related papers

[[2026_Sen_NVFP4QuantizationEdgeAI]] (complementary compression angle — quantization vs. architecture search for the same ultra-low-power resource budget)
