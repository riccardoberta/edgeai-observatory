# An Evaluation of Edge TPU Accelerators for Convolutional Neural Networks

**Full citation:** Yazdanbakhsh, A., Seshadri, K., Akin, B., Laudon, J., Narayanaswami, R. (2021). An Evaluation of Edge TPU Accelerators for Convolutional Neural Networks. arXiv:2102.10423. https://arxiv.org/abs/2102.10423

**Linked concepts:** [[NPU]], [[Vision]]

## Abstract summary

The authors (Google) characterize the microarchitecture of Edge TPUs — a family of NPU accelerators used in products such as Coral and Pixel devices — and extensively evaluate three classes of Edge TPU across roughly 423,000 unique convolutional neural networks, deriving interpretable microarchitectural insights and building learned models to estimate accelerator latency and energy consumption.

## Research problem

NPU/accelerator vendors typically report headline performance numbers (peak TOPS, example benchmark latency), but practitioners need a much finer-grained understanding of how an NPU's specific microarchitectural choices (memory hierarchy, datapath, compiler behavior) affect real performance and energy across a wide diversity of CNN architectures, not just one or two reference models.

## Key idea

Run a very large, systematic sweep of CNN architectures (hundreds of thousands of variants) across multiple generations/classes of Edge TPU hardware, then use the resulting performance data both to extract human-interpretable microarchitectural insights and to train machine-learned performance/energy prediction models that could substitute for exhaustive hardware measurement in future design or deployment decisions.

## Technical contribution

A large-scale empirical characterization methodology for NPU accelerators (rather than a new accelerator design itself): detailed microarchitectural description of Edge TPU classes, a massive CNN-variant benchmark suite, and learned estimators for latency/energy that generalize across the architecture search space.

## Experimental methodology

Evaluation across three classes of Edge TPU (covering different deployment contexts — currently shipped products and product-pipeline designs) and approximately 423,000 unique CNN architectures, measuring latency and energy, then fitting machine-learning models to predict these metrics from architectural descriptors, validated against held-out measured data.

## Results

The study surfaces concrete, interpretable microarchitectural bottlenecks and trade-offs specific to Edge TPU's design (e.g. how certain layer shapes or operator choices interact with the accelerator's datapath and memory hierarchy) and demonstrates that learned models can estimate latency/energy accurately enough to be useful for fast, hardware-aware neural architecture search without needing to run every candidate on real silicon.

## Comparison with the state of the art

Compared to typical vendor-reported single-model benchmarks, this is a substantially larger and more systematic empirical study; it complements (and could feed into) hardware-aware NAS approaches like the work covered in our [[NAS]] concept, by providing accurate, cheap-to-query performance proxies instead of requiring on-device measurement for every candidate architecture.

## Strengths

Very large, systematic benchmark scale (423K CNN variants) gives statistically robust insights rather than anecdotal comparisons; produced from within Google with direct access to Edge TPU microarchitectural details and multiple hardware generations; directly useful as a performance-proxy tool for downstream hardware-aware design work.

## Weaknesses

Focused specifically on CNNs and on Edge TPU hardware, so the learned performance models and microarchitectural insights may not transfer to other NPU vendors' architectures or to non-CNN model families (transformers, RNNs) increasingly relevant to EdgeAI; being an industry characterization study rather than an open accelerator design, the underlying hardware details remain partly proprietary.

## Limitations

Edge TPU is a fixed, non-reconfigurable ASIC-class NPU — the insights here may not generalize to reconfigurable accelerators like FPGAs (see [[FPGA]]) or to programmable RISC-V-based accelerators (see [[RISC-V]]); the learned performance-prediction models would need retraining for any new hardware generation or non-CNN model family.

## Open questions

How well do the learned latency/energy estimators generalize to non-CNN architectures (small transformers, RNNs) now common in TinyML research? How do Edge TPU's microarchitectural bottlenecks compare to other NPU families (e.g. ARM Ethos, CEVA NeuPro) on the same model set — is there a generalizable theory of NPU bottlenecks, or is it largely vendor-specific?

## Possible extensions

Extending the same large-scale empirical characterization methodology to non-CNN architectures and to other commercial NPU families, to test whether the learned performance-prediction approach generalizes beyond Edge TPU and CNNs.

## Relevance to our research

Foundational empirical reference for the [[NPU]] branch of our Hardware taxonomy; directly useful for any [[NAS]] work that wants a fast, hardware-aware performance proxy instead of exhaustive on-device benchmarking.

## Possible thesis topics

Building an analogous large-scale performance-characterization study for a different NPU family (e.g. ARM Ethos-U, used with Cortex-M) or for non-CNN model families, to test the generality of the learned-estimator approach introduced here.

## Possible collaborations

Hardware-aware NAS research groups; NPU vendors (Arm, Qualcomm, CEVA) listed in `00_Config/sources.yaml`, who could provide architectural access analogous to what this Google-internal study had for Edge TPU.

## Links to related papers

[[2019_Cai_OnceForAll]] (hardware-aware NAS that could directly use this kind of performance proxy), [[2018_Flamand_GAP8]], [[2017_Umuroglu_FINN]] (alternative accelerator substrates for the same deployment problem)
