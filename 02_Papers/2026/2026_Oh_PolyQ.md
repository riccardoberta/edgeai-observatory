# PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference

**Full citation:** Oh, H., Jang, S., Chen, H., Nam, K., Yun, S., Masukawa, R., Imani, M. (2026). PolyQ: Codesigning End-to-End Quantization Framework for Scalable Edge CPU LLM Inference. arXiv:2607.14618 [cs.LG, cs.AR, cs.OS]. Submitted 16 Jul 2026. Accepted to ICCAD 2026. DOI: 10.48550/arXiv.2607.14618.

**Linked concepts:** [[Quantization]]; also part of [[Mixture-of-Experts (MoE) & Edge LLM Serving]] — PolyQ targets dense-model CPU inference specifically rather than MoE routing, but shares the cluster's edge-LLM-deployment framing.

## Abstract summary

CPUs are the most universal on-device LLM inference target, but existing low-bit quantization offers either coarse operating points or fine-grained mixed precision that is hard to execute efficiently on CPUs. PolyQ is a CPU-oriented compiler/quantization co-design for activation-aware, channel-wise bit allocation under a user-specified average-bit budget: per-channel bit-widths from {2,3,4,8,16} are assigned, then a compile-time model compiler permutes and clusters channels into bit-homogeneous blocks, generates SIMD- and LUT-compatible kernels, and merges compatible permutations across operators so layout regularization stays off the runtime path. Across Falcon-H1-3B, Llama2-13B, and Qwen3-32B on WikiText-2, PolyQ gives stable quality scaling from 3–6 bits and improves perplexity by 2.4–32.1% over prior methods at a 3-bit target. On three representative CPUs (workstation, laptop, mobile), compiler layout regularization cuts activation-reorder traffic by up to 70.8%, prefill latency and decode throughput scale nearly proportionally with the configured bit budget, and energy/token overhead stays below 2% relative to an optimized LUT back-end.

## Research problem

Fine-grained mixed-precision quantization (assigning different bit-widths to different channels based on their sensitivity) is known to give better accuracy-per-bit than uniform quantization, but it has been hard to execute *efficiently* on CPUs — the irregular per-channel bit-widths create a runtime layout-regularization tax that erodes the accuracy gains. Practitioners have therefore been stuck choosing between coarse, uniform operating points (easy to run fast, worse accuracy) or fine-grained mixed precision (better accuracy, hard to run fast) — with CPUs, the most universally available on-device inference target, caught on the wrong side of that trade-off.

## Key idea

Push the hard work of making mixed-precision layouts CPU-friendly to compile time rather than runtime: after assigning activation-aware, per-channel bit-widths under a user-specified average-bit budget, a compile-time model compiler permutes and clusters channels into bit-homogeneous blocks, generates SIMD- and LUT-compatible kernels for those blocks, and merges compatible permutations across operators — so that by the time the model actually runs, there is no layout-regularization cost left to pay at runtime.

## Technical contribution

An activation-aware channel-wise bit-allocation scheme choosing from {2,3,4,8,16}-bit per-channel widths under a global average-bit budget; a compile-time channel permutation/clustering algorithm that turns irregular mixed-precision layouts into bit-homogeneous, SIMD/LUT-friendly blocks; cross-operator permutation merging to avoid redundant reorder cost; the empirical property that prefill latency and decode throughput scale nearly proportionally with the configured average-bit budget — making deployment planning tractable ("if I want X bits, I get roughly Y latency") rather than trial-and-error.

## Experimental methodology

Perplexity evaluated on WikiText-2 across three model scales: Falcon-H1-3B, Llama2-13B, and Qwen3-32B, comparing PolyQ's 3–6-bit operating points against prior quantization methods at a matched 3-bit target. End-to-end latency/throughput/energy measured on three representative CPU classes: workstation, laptop, and mobile.

## Results

Stable quality scaling from 3–6 bits across all three model scales; 2.4–32.1% perplexity improvement over prior methods at a 3-bit target (a wide range suggesting model-dependent gains, likely largest for the models prior methods handle worst at 3 bits). On the CPU measurements: up to 70.8% reduction in activation-reorder traffic from compiler layout regularization; prefill latency and decode throughput scale nearly proportionally with the configured bit budget; energy-per-token overhead stays below 2% relative to an optimized LUT-based back-end — meaning the fractional-bit flexibility is nearly free in energy terms once the compile-time work is done.

## Comparison with the state of the art

Directly benchmarked against prior quantization methods at a matched 3-bit target on perplexity, and against "an optimized LUT-based back-end" on energy overhead — a genuine head-to-head rather than only self-comparison. Activation-aware and mixed-precision quantization are individually established (the Observatory already tracks AWQ and integer-only quantization in this space); PolyQ's specific contribution is making fine-grained per-channel budgets deployable on CPUs specifically, which prior mixed-precision work largely did not address.

## Strengths

Targets the most universal on-device inference substrate (every phone, laptop, and many MCUs have a CPU) rather than assuming specialized accelerator hardware; the "predictable scaling with configured average bits" property is unusually practitioner-friendly — it turns quantization-budget selection into a planning exercise rather than requiring re-benchmarking for every target bit-width; validated across three genuinely different model scales (3B to 32B) and three CPU classes (workstation to mobile), not a single point measurement; ICCAD 2026 acceptance signals peer review at a top hardware-systems venue.

## Weaknesses

The abstract does not specify how far down the "mobile CPU" target actually goes — application-class mobile CPU (e.g., a phone SoC's CPU cluster) versus true MCU-class hardware are very different regimes, and the 2026-07-19 digest explicitly held the paper below a 5/5 score pending this clarification; perplexity is the only accuracy metric reported at the abstract level — no downstream task accuracy (e.g., instruction-following, reasoning benchmarks) is given, which matters for whether the perplexity gains translate to real task quality.

## Limitations

The bit-homogeneous-block compilation strategy is specifically tuned for CPU SIMD/LUT execution; whether the same compile-time approach transfers to genuinely different execution substrates (GPU, NPU, or true MCU cores without wide SIMD) is untested and likely requires a different block-homogenization strategy given different hardware constraints.

## Open questions

How far down the CPU capability spectrum does PolyQ's near-linear latency/bit-budget scaling survive — does it hold on a true Cortex-M/RISC-V core without wide SIMD/LUT units, or does the compile-time strategy assume application-class CPU features? Do the perplexity gains reported translate proportionally to downstream task accuracy, or does 3-bit quantization disproportionately hurt specific capabilities?

## Possible extensions

Port PolyQ-style compile-time bit-homogeneous blocking from application-class CPUs down to Cortex-M/RISC-V with CMSIS-NN/microTVM back-ends, and measure whether the near-linear latency-vs-bit-budget scaling survives without wide SIMD/LUT units (the explicit 2026-07-19 digest hook); extend the perplexity-only evaluation with downstream task accuracy benchmarks to test whether the reported gains hold for actual model quality, not just language-modeling loss.

## Relevance to our research

A strong fit for the Observatory's [[Quantization]] branch, with a compile-time block-homogenization idea that is directly transferable in spirit to the group's own MCU/edge-CPU toolchains even if the specific mobile-CPU target in the paper sits above true MCU-class hardware. Also part of the broader "Mixture-of-Experts (MoE) & Edge LLM Serving" taxonomy cluster formalized 2026-08-25, as one of the earliest (July 2026) entries in that thread, alongside HeteroMosaic.

## Possible thesis topics

Fractional-bit quantization on true MCUs: port PolyQ-style compile-time bit-homogeneous blocking from application-class CPUs down to Cortex-M/RISC-V (with CMSIS-NN/microTVM back-ends) and measure whether the near-linear latency-vs-bit-budget scaling survives without wide SIMD/LUT units (Master's/PhD, per the 2026-07-19 digest's explicit hook; bridges [[Quantization]] and [[Cortex-M]]/[[RISC-V]]).

## Possible collaborations

Mohsen Imani's group (UC Irvine), whose PolyQ authorship the July 2026 monthly report flagged as worth tracking across future submissions given their ICCAD-2026-accepted quantization-compiler track record — a plausible collaboration target for CPU-oriented quantization compiler work.

## Links to related papers

Extends the Observatory's existing [[Quantization]] records ([[2017_Jacob_QuantizationIntegerOnlyInference]], AWQ) into the CPU-specific, compile-time-regularized fractional-bit regime. Part of the same emerging "edge LLM/MoE serving" cluster as HeteroMosaic (arXiv:2607.12839), APEX, EdgeXpert, and UnionSparse.
