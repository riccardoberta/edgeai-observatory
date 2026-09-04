# Taxonomy

This is the map of the EdgeAI Observatory's Knowledge Base: the set of concepts (research topics) the KB is organized around, grouped into six branches. A paper can belong to more than one concept — for example, a paper that prunes a model and then deploys it on a Cortex-M microcontroller belongs to both [[Pruning]] and [[Cortex-M]]. Each concept named below has its own page under `01_Knowledge_Base/`, which explains the concept itself, lists its key papers, and tracks open research questions and thesis ideas.

The taxonomy is a living structure: as new research directions emerge, new concepts are added, and existing ones are occasionally split or merged when the literature outgrows the current grouping. "Field notes" and "Known gaps" at the end of this document record observations of that kind that are still relevant today.

## Algorithms

Techniques for making a neural network's *computation* cheaper — smaller, faster, or less power-hungry — independent of what hardware it eventually runs on.

- **Quantization** — representing a model's weights and activations with fewer bits (e.g. 8-bit integers instead of 32-bit floats) to shrink memory and speed up inference. Includes post-training quantization, quantization-aware training, mixed precision, and binary/ternary networks.
- **Pruning** — removing weights or whole structures (neurons, channels, layers) that contribute little to accuracy, to shrink the model. Includes structured pruning (removes whole channels/filters, so the result is directly faster on ordinary hardware), unstructured pruning (removes individual weights, needs sparse-matrix support to actually speed up), and dynamic pruning (decided at inference time, per input).
- **Distillation** — training a small "student" model to reproduce the outputs of a larger, more accurate "teacher" model, so the student inherits some of the teacher's accuracy at a fraction of its size. Includes self-distillation, where a model distills from an earlier or larger version of itself.
- **NAS (Neural Architecture Search)** — automatically searching for a network architecture rather than hand-designing one, often optimized jointly for accuracy and for a specific hardware target ("hardware-aware NAS"). "Once-for-all" networks are a NAS variant that trains one large network from which many differently-sized sub-networks can be extracted without retraining, one for each hardware budget.
- **Compression** — techniques for shrinking a model's stored representation beyond quantization and pruning alone, such as low-rank factorization (approximating a weight matrix as the product of two smaller matrices) and weight sharing (forcing multiple weights to reuse the same stored value).
- **Continual Learning** — training a model on a sequence of tasks or data distributions over time without forgetting what it learned earlier ("catastrophic forgetting"), relevant when an edge device keeps learning after deployment rather than being trained once and frozen.
- **On-device Learning** — training or fine-tuning a model directly on the edge device itself, instead of training in the cloud and only deploying the finished model. Shares motivation with Continual Learning but focuses on making the training computation itself feasible under edge memory/compute budgets.
- **Federated Learning** — training one shared model across many devices that each keep their own data local and only exchange model updates, so raw data never leaves the device. Relevant to EdgeAI both for privacy and because it distributes the training cost across many constrained devices instead of one central server.
- **Mixture-of-Experts (MoE) & Edge LLM Serving** — running large language models (LLMs) on constrained hardware, covering both the MoE architecture itself (a network made of many "expert" sub-networks where only a few are activated per input, keeping compute low despite a huge total parameter count) and the broader infrastructure problem of serving any LLM under tight memory/bandwidth budgets: expert routing, caching and prefetching, and scheduling work across a device's CPU, GPU, and NPU.

## Frameworks

Software toolchains that turn a trained model into code that actually runs on edge hardware.

- **TensorFlow Lite Micro** — Google's inference runtime for microcontrollers (no operating system, kilobytes of RAM), the most widely used runtime at the very low end of the hardware spectrum.
- **CMSIS-NN** — Arm's library of hand-optimized neural-network kernels (convolution, matrix multiplication, etc.) for Cortex-M microcontrollers, often used underneath TensorFlow Lite Micro to accelerate the actual math.
- **microTVM / TVM** — Apache TVM is a compiler that takes a trained model and generates optimized code for a wide range of hardware backends; microTVM is its variant targeting microcontroller-class devices specifically.
- **MLIR (Multi-Level Intermediate Representation)** — a compiler infrastructure (originating at Google, now part of the LLVM project) for building custom compiler passes and representations; increasingly used as shared low-level plumbing underneath higher-level frameworks like TVM and vendor-specific NPU compilers.
- **ONNX Runtime** — a cross-framework inference engine for models exported in the ONNX (Open Neural Network Exchange) format, letting a model trained in one framework (e.g. PyTorch) run through a common runtime regardless of which framework produced it.
- **ExecuTorch** — Meta's PyTorch-native deployment runtime, designed to take a PyTorch model from a full microcontroller up to a phone-class SoC without converting to a different framework first.
- **Edge Impulse** — a commercial MLOps (machine-learning-operations) platform that sits above the runtimes listed here, handling data collection, training, and deployment through one workflow rather than being a runtime itself.

## Hardware

The physical processor classes edge models are deployed on, each with different constraints on power, memory, and the kinds of computation they accelerate well.

- **Cortex-M** — Arm's microcontroller-class CPU core family: no operating system, kilobytes to low megabytes of RAM, the low-power floor of the hardware spectrum and the primary target of CMSIS-NN and TensorFlow Lite Micro.
- **Cortex-A** — Arm's application-processor CPU core family: runs a full operating system (Linux, Android), found in smartphones and single-board computers, several orders of magnitude more capable than Cortex-M.
- **RISC-V** — an open, royalty-free instruction-set architecture (as opposed to Arm's proprietary one), increasingly used as the basis for custom edge AI silicon because vendors can extend it freely with their own instructions.
- **DSP (Digital Signal Processor)** — a processor core optimized for the repetitive multiply-accumulate math common in signal processing and neural-network inference, often included as a co-processor alongside a general-purpose CPU.
- **FPGA (Field-Programmable Gate Array)** — a chip whose hardware logic can be reconfigured after manufacturing, used to build custom, application-specific accelerators without designing a fixed chip.
- **NPU (Neural Processing Unit)** — a chip or chip block purpose-built to accelerate neural-network inference (matrix multiplication at high throughput and low power), increasingly included alongside the CPU in modern edge SoCs.
- **Event-Driven / Neuromorphic Accelerators** — hardware built around event-graph-neural-network processing: instead of processing a full frame or sample window at fixed intervals, it responds only to changes in the input stream (e.g. a pixel that changed brightness), which suits sparse, asynchronous sensor data such as event cameras or always-on audio.

## Applications

The end-user tasks EdgeAI systems are built to perform, each with its own accuracy/latency/power trade-offs and typical model types.

- **Keyword Spotting** — detecting one or a few specific spoken words or phrases (e.g. a wake word like "Hey Siri") using a small, always-on model, rather than full speech recognition.
- **Vision** — image classification, object detection, and related visual tasks running on constrained hardware, typically built on efficient CNN or hybrid CNN/transformer architectures.
- **Human Activity Recognition (HAR)** — classifying a person's physical activity (walking, running, falling, etc.) from wearable sensor data, typically accelerometer/gyroscope streams.
- **Biosignals** — processing physiological signals (EEG, ECG, EMG, and similar) on wearable or implantable devices, usually for health monitoring or human-machine interfaces.
- **Industrial IoT** — sensing and inference embedded in industrial equipment and environments, such as quality control or anomaly detection on a factory line.
- **Predictive Maintenance** — predicting equipment failure before it happens from sensor data (vibration, temperature, etc.), so maintenance can be scheduled proactively instead of reactively.
- **Generative EdgeAI (Gen EdgeAI)** — deploying *generative* and *multimodal* models (as opposed to the classification/detection models the other Applications concepts above are built around) on constrained edge hardware: visual question answering, conversational pipelines combining speech-to-text, a small language model, and text-to-speech, and similar. A newer, less mature niche than the others, distinct from the Algorithms branch's Mixture-of-Experts (MoE) & Edge LLM Serving concept, which covers the *serving infrastructure* (memory management, scheduling) for LLMs rather than the end-user application built on top of it.

## Benchmarks & Datasets

Standardized ways to measure and compare EdgeAI systems, and the data used to train and evaluate them.

- **MLPerf Tiny** — the industry-standard benchmark suite for microcontroller-class ("TinyML") inference, run by the MLCommons consortium, giving vendors and researchers a common yardstick for latency, accuracy, and energy on the smallest hardware tier.
- **TinyML Reference Datasets** — the small, standardized datasets the field commonly trains and benchmarks against, such as Speech Commands (short spoken-word audio clips, used for keyword spotting) and Visual Wake Words (a binary "is a person present in this image" dataset, used for tiny vision models).

## Security

Protecting an edge AI system's data, model weights, and computation from attackers, a concern distinct from the accuracy/efficiency trade-offs the other branches focus on.

- **Hardware / Physical Security of Edge AI Accelerators** — attacks and defenses at the hardware level: extracting a model's architecture or weights by observing power consumption, electromagnetic emissions, or other physical side channels; and defenses such as extending a Trusted Execution Environment's (TEE's) protection boundary beyond the CPU into memory or accelerator-adjacent hardware.

## Field notes

These are durable observations about how the field itself is moving — not a log of Observatory activity, but trends worth keeping in mind when reading the KB or planning new research.

**Quantization and Compression have shifted from the CNN era to the LLM era.** Older work in both areas targeted compressing CNNs (the AlexNet/VGG/MobileNet generation of models). Since roughly 2023–2024, new work has shifted toward post-training, calibration-light compression of large language models for edge/on-device deployment. Calibration cost and structured-vs-unstructured trade-offs differ meaningfully between the two eras, so it is worth watching whether "LLM edge compression" becomes its own sub-category rather than remaining a variant of the older CNN-era techniques.

**Vision is moving from pure CNNs to hybrid CNN/transformer architectures.** Standard self-attention (the core mechanism in transformers) is memory-bound in a way that doesn't suit TinyML-scale budgets; recent architectures pair a memory-efficient attention variant with a CNN-style macro design, extending MobileNet-style "efficient by design" thinking to transformers.

**NPU vendors are building their compilation stacks directly on MLIR.** Rather than building a bespoke compiler toolchain, at least one major NPU vendor (Qualcomm, for its Hexagon NPU) now lowers standard front-ends (PyTorch, Triton) through MLIR's dialect infrastructure. Combined with academic work on learned MLIR-level cost models, this suggests MLIR is consolidating as shared compiler infrastructure across NPU vendors, not just an academic substrate.

**General-purpose compiler toolchains are retreating from MCU-class targets, while hardware pushes AI processing further into the sensor.** Apache TVM's recent releases have trimmed microTVM-specific code, and there are open questions in the TVM community about microTVM's future, even as hardware vendors (e.g. STMicroelectronics' in-sensor ISPU line) push AI processing further down into the sensor itself. This is not proof that microTVM is being abandoned, but it is a real signal that MCU-native libraries (CMSIS-NN, TensorFlow Lite Micro) may be consolidating their position as the practical default for ultra-low-power deployment, while TVM's center of gravity drifts toward GPU/accelerator-class hardware.

**"How edge is edge?" is a recurring, unresolved tension in LLM-serving research.** A cluster of recent systems papers on serving LLMs at the edge (see [[MoE_Edge_LLM_Serving]]) apply genuinely novel ideas to laptop, workstation, or edge-GPU-class hardware rather than the microcontroller/RISC-V/NPU tier this Observatory otherwise treats as "edge." No paper in that cluster has yet proposed a quantitative criterion (a memory budget, power envelope, or cost tier) for where "edge-native" LLM serving stops and genuine TinyML begins; anchoring such a definition to MLPerf Tiny's device classes versus MLPerf Inference's edge category is one plausible starting point, but nothing has validated it yet. The same boundary question resurfaces in [[Generative_EdgeAI]].

## Known gaps

Candidate topics that have come up in monitoring but do not yet have a dedicated concept page, because they don't yet meet this Observatory's bar of at least two independently-authored papers anchoring the topic. Listed here so they aren't rediscovered from scratch each time; a second independent paper on any of these should prompt formalizing it as a proper concept.

- **In-memory computing with emerging non-volatile memory** (e.g. Magnetic Tunnel Junction or ReRAM-based in-memory computation) — one active research program identified so far, not yet independently corroborated.
- **Standardized measurement infrastructure for MCU/NPU-class inference** — solid open measurement frameworks exist for Jetson-class and Apple-silicon-class hardware, but nothing equivalent has been found yet at the microcontroller/Ethos-U/RISC-V-NPU tier.
- **Edge GPU / Jetson-class hardware as its own Hardware concept** — a real, well-established hardware category (NVIDIA Jetson and similar), but only one dedicated characterization paper found so far; the existing Hardware branch (Cortex-M, Cortex-A, RISC-V, DSP, FPGA, NPU) has no GPU-tier entry.
- **Explainability / interpretability for edge AI systems** — one paper found proposing "explainability as a service" for edge deployments; not yet corroborated by independent work.
- **Robotics / autonomous-systems applications of EdgeAI** — a plausible Applications gap, but no credible anchor paper identified yet.
