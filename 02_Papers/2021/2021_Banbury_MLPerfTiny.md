# MLPerf Tiny Benchmark

**Full citation:** Banbury, C., Reddi, V.J., Torelli, P., Holleman, J., Jeffries, N., et al. (2021). MLPerf Tiny Benchmark. *Advances in Neural Information Processing Systems 34 (NeurIPS 2021), Datasets and Benchmarks Track*. https://datasets-benchmarks-proceedings.neurips.cc/paper/2021/file/da4fb5c6e93e74d3df8527599fa62642-Paper-round1.pdf

**Linked concepts:** [[TensorFlow_Lite_Micro]], [[Quantization]], [[Compression]]

## Abstract summary

The authors, on behalf of the MLCommons/MLPerf consortium, present MLPerf Tiny, a standardized benchmark suite for evaluating machine learning inference performance on extremely resource-constrained, ultra-low-power devices (microcontrollers and similar hardware), covering representative tasks (e.g. keyword spotting, visual wake words, image classification, anomaly detection) together with a defined methodology for measuring latency, energy, and accuracy.

## Research problem

Before this benchmark, performance claims for TinyML hardware and software stacks (MCUs, runtimes, compilers) were largely incomparable across vendors and papers, since there was no standardized set of tasks, reference models, and measurement methodology specific to the extreme low-power, low-memory regime that general MLPerf benchmarks (targeting servers and mobile/edge GPUs) did not address.

## Key idea

Define a small set of representative TinyML reference tasks and reference models, together with a rigorous, standardized measurement methodology (including energy measurement protocols) and a public submission/results process, so that different hardware platforms, runtimes, and optimization techniques can be compared on a level playing field.

## Technical contribution

The benchmark task suite itself (keyword spotting, visual wake words, image classification, anomaly detection) with reference models sized for microcontroller deployment; a measurement methodology specification covering both latency and energy consumption; an open submission and results infrastructure that the broader TinyML community (vendors, runtime developers) can submit results to.

## Experimental methodology

Defines reference implementations of each task (including a TensorFlow Lite Micro reference runtime) and establishes the rules under which any hardware/software combination can be benchmarked and have results submitted and published, with both closed (fixed model) and open (any model achieving a quality target) submission divisions.

## Results

Establishes a working, adopted benchmark with submissions from multiple hardware vendors and software stacks, enabling for the first time apples-to-apples comparison of TinyML inference latency and energy efficiency across different microcontroller platforms and optimization approaches.

## Comparison with the state of the art

Extends the established MLPerf methodology (already standard for server/datacenter and mobile inference benchmarking) down into the extreme low-power MCU regime, which prior MLPerf divisions did not cover, filling a real gap in standardized TinyML evaluation.

## Strengths

Backed by a broad industry/academic consortium, giving it wide adoption and credibility; the standardized energy-measurement methodology in particular addresses a previously inconsistent and hard-to-compare aspect of TinyML evaluation.

## Weaknesses

The benchmark tasks and reference models, by necessity, represent only a subset of real-world TinyML use cases, and results can still be sensitive to vendor-specific compiler/runtime optimizations that may not generalize to other workloads.

## Limitations

As a benchmark suite rather than a research method, it does not itself propose new algorithms or hardware; its value is entirely as shared infrastructure that the rest of the field measures itself against, which means its relevance depends on continued community adoption and task-set evolution.

## Open questions

How should the benchmark task suite evolve to keep pace with emerging TinyML application areas (e.g. on-device learning, federated learning) that are not yet represented? How comparable are energy measurements across very different measurement setups and hardware power-delivery characteristics in practice?

## Possible extensions

Extending the benchmark suite to cover on-device training/federated learning workloads, not just inference; adding standardized model-compression-ratio reporting alongside latency/energy/accuracy.

## Relevance to our research

The standard reference benchmark and evaluation methodology for nearly all TinyML inference work the Observatory tracks; results reported against MLPerf Tiny should be treated as the most directly comparable cross-platform evidence available.

## Possible thesis topics

Benchmarking a novel compression or quantization technique against the MLPerf Tiny task suite on a specific microcontroller target, to produce results directly comparable to published submissions.

## Possible collaborations

Groups and vendors actively submitting to MLPerf Tiny, and the broader MLCommons benchmarking community.

## Links to related papers

[[2017_Jacob_QuantizationIntegerOnlyInference]]
