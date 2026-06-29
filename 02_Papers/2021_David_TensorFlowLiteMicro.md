# TensorFlow Lite Micro: Embedded Machine Learning on TinyML Systems

**Full citation:** David, R., Duke, J., Jain, A., Janapa Reddi, V., Jeffries, N., Li, J., Kreeger, N., Nappier, I., Natraj, M., Wang, T., Warden, P., Rhodes, R. (2021). TensorFlow Lite Micro: Embedded Machine Learning for TinyML Systems. *Proceedings of Machine Learning and Systems (MLSys)*, 3, pp. 800–811. arXiv:2010.08678. https://arxiv.org/abs/2010.08678

**Linked concepts:** [[TensorFlow Lite Micro]], [[On-device Learning]]

## Abstract summary

The authors present TensorFlow Lite Micro (TFLM), an open-source inference runtime designed for microcontrollers without an operating system, with extreme memory constraints (kilobytes, not megabytes) and no dynamic dependencies.

## Research problem

Existing inference frameworks (including "standard" TensorFlow Lite) assume an operating system, dynamic memory allocation, and relatively abundant resources — assumptions that do not hold on 32-bit microcontrollers with only a few tens/hundreds of KB of RAM typical of TinyML.

## Key idea

A minimal interpreter, with no dependency on operating-system standard libraries, with statically planned memory allocation, portable across a wide range of microcontroller architectures via swappable kernel layers (including CMSIS-NN for Cortex-M).

## Technical contribution

Runtime architecture with a static memory planner; a mechanism for platform-specific optimized kernels; interoperability with TensorFlow Lite's FlatBuffer format, so models are trained in the same TensorFlow ecosystem and then converted for embedded deployment.

## Experimental methodology

Benchmarks across several microcontroller families (Cortex-M and others) with reference TinyML models (keyword spotting, visual wake words, anomaly detection), measuring memory footprint, latency, and energy consumption.

## Results

TFLM runs on devices with only a few tens of KB of RAM while maintaining competitive performance when paired with optimized kernels such as CMSIS-NN; it is adopted as the reference runtime for the MLPerf Tiny benchmark.

## Comparison with the state of the art

Compared to vendor-specific ad-hoc solutions, TFLM offers cross-platform portability while keeping performance close to specialized implementations, thanks to the decoupling between interpreter and kernels.

## Strengths

Very wide industry and TinyML community adoption; training-to-deployment ecosystem integrated with TensorFlow; actively maintained open-source code.

## Weaknesses

The generic graph interpreter introduces overhead compared to ad-hoc generated code (the approach instead followed by microTVM/compiler-based methods); static memory planning can be conservative for models with dynamic shapes.

## Limitations

Designed primarily for inference, not for on-device training; support for complex operators or very recent architectures (Transformers) requires continuous kernel updates.

## Open questions

How much performance gap remains between a generic interpreter (TFLM) and ad-hoc compiled code (microTVM) as model complexity grows? How to extend the runtime to support incremental on-device training without violating memory constraints?

## Possible extensions

Tighter integration with compilers like microTVM to generate model-specific kernels; native support for lightweight on-device fine-tuning.

## Relevance to our research

A central reference for any experimental work on TinyML: it is likely the base runtime used in our microcontroller experiments.

## Possible thesis topics

Experimental comparison between TFLM and microTVM on a common set of TinyML models, measuring interpreter overhead; extension of TFLM to support a lightweight on-device learning mechanism.

## Possible collaborations

Groups involved in MLPerf Tiny and the TinyML Foundation community; microcontroller vendors maintaining CMSIS-NN or equivalent kernels.

## Links to related papers

[[2018_Lai_CMSIS-NN]], [[2018_Chen_TVM]], [[2018_Warden_SpeechCommands]]
