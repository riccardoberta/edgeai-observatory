# Monthly Report — June 2026

## Emerging trends

The clearest signal this month is not a single paper or chip but a quiet architectural argument happening across the toolchain layer: the industry is bifurcating between general-purpose ML compilers retreating from microcontroller-class targets, and hardware vendors pushing AI processing further down into the sensor itself. On the compiler side, Apache TVM's v0.25.0 release candidate (uploaded 9 June 2026) includes a runtime refactor explicitly described as removing "leftover microTVM/CRT crumbs," consistent with an open community discussion thread on the TVM forum questioning microTVM's future development. Read together, these are not proof that microTVM is being discontinued, but they are a real and verifiable signal that the project's bare-metal/CRT-specific code paths are being pared down rather than invested in. That matters directly for [[microTVM_TVM]]: if the trend continues, frameworks like [[CMSIS-NN]] and [[TensorFlow_Lite_Micro]] — which target the MCU tier directly rather than through a general compiler — may consolidate their position as the practical default for ultra-low-power deployment, while TVM's center of gravity drifts toward GPU/accelerator-class hardware.

At the opposite end of the stack, hardware vendors are pushing intelligence into the sensor, not just the MCU. STMicroelectronics' IIS3DWB10IS vibration sensor (announced 3 June 2026) embeds a second-generation "Intelligent Sensor Processing Unit" (ISPU 2.0, 40 MIPS/40 MFLOPS) directly on the MEMS die, explicitly positioned as a piezosensor alternative for industrial condition monitoring. This is a concrete data point for an "in-sensor AI" trend that sits below the taxonomy's current Hardware branch ([[Cortex-M]], [[Cortex-A]], [[RISC-V]], [[DSP]], [[FPGA]], [[NPU]]) — "computation inside the sensor package" is a distinct deployment target from "computation on an MCU fed by a sensor."

A third, broader trend visible in the wider edge AI discourse this month is the push to run small language and vision-language models directly on edge silicon, evidenced by NVIDIA's published Jetson Thor token-throughput benchmarks for Mistral and Qwen-family models. This is a different weight class from the Cortex-M-class deployments this taxonomy mostly tracks, but it converges on similar concerns (quantization, memory footprint, latency) — see [[MoE_Edge_LLM_Serving]].

## New research directions

Two directions look ready for deeper investment. First, on-device-runnable NAS search procedures (as in the ultra-low-power hardware-aware NAS paper, arXiv:2606.16290) point toward a broader question: which parts of the model-development pipeline can be moved onto the constrained device itself, not just inference? Second, the disentangled ablation methodology used in the NVFP4 quantization paper (arXiv:2606.06527) — separating the contribution of scaling from the contribution of bit width — is a template that could productively be applied to other compression techniques in [[Quantization]] and [[Compression]], many of which report end-to-end accuracy numbers without isolating which design choice actually drove the result.

## Influential research groups

Worth tracking across future submissions: the NVFP4 quantization paper's author list (Sen, Kamineni, Lobo, Bhunia, Ewetz, Chatterjee) spans groups with prior work in hardware-software co-design, and the hardware-aware NAS paper (Garavagno, Ragusa, Frisoli, Gastaldo) comes from a group with a track record in embedded/wearable robotics rather than pure ML.

## Software releases

Apache TVM published v0.25.0-rc0 on 9 June 2026, with the microTVM/CRT runtime cleanup noted above. CMSIS-NN's most recent tagged release remains v7.0.0, which added int8 Pad, Transpose, and Minimum/Maximum operators along with per-channel-quantized Fully Connected support. TensorFlow Lite Micro does not use GitHub's release-tag mechanism at all. Edge Impulse (now under Qualcomm) shipped full integration into the Arduino App Lab, bringing Edge Impulse Studio training/deployment directly into Arduino's UNO Q workflow — a meaningful reduction in friction for hobbyist and teaching use cases.

## Benchmarks

The latest published MLPerf Tiny results remain v1.3 (September 2025, which added a 1D depthwise-separable CNN wake-word test). MLCommons' broader-scale MLPerf Inference v6.0 and MLPerf Training v6.0 rounds landed in 2026 (April and June respectively) but target datacenter-class hardware, outside the MCU/edge focus this taxonomy tracks — their existence sometimes gets conflated with MLPerf Tiny in casual reporting.

## Datasets

No new dataset directly extending or replacing Speech Commands or Visual Wake Words was confirmed this month. An IEEE-published "Benchmark Dataset for Generative AI on Edge Devices" (BeDGED) surfaced in search results, covering throughput/latency/memory measurements for generative models on edge hardware, but its publication date could not be pinned down with confidence.

## Conference landscape note

As of 2026, IPSN and IoTDI have merged into SenSys, which now runs as a single unified ACM/IEEE event (SenSys 2026 was held 11–14 May 2026 in Saint-Malo, co-located with CPS-IoT Week). None of DAC (scheduled 25–29 July 2026), MLSys (held 18–22 May 2026), NeurIPS, ICML, or ICLR had events or proceedings releases falling inside the June window.

## Research and thesis opportunities

Three concrete directions, each tied to existing taxonomy branches. First, a systematic comparison of MCU-native inference libraries ([[CMSIS-NN]], [[TensorFlow_Lite_Micro|TFLite Micro]]) against general compiler-based toolchains ([[microTVM_TVM|TVM/microTVM]]) as the latter's bare-metal investment appears to soften — a thesis could measure whether this is already showing up as a performance or maintenance gap on real [[Cortex-M]] targets. Second, in-sensor AI processing (as in STMicroelectronics' ISPU 2.0) opens a question about where the optimal compute boundary sits for specific applications — a Master's-level study comparing energy and latency trade-offs of in-sensor versus on-MCU inference for a fixed task (e.g. vibration-based predictive maintenance, connecting to [[Predictive_Maintenance]]) would produce genuinely new comparative data rather than restating vendor claims. Third, the disentangled-ablation methodology from the NVFP4 paper could be formalized into a reusable evaluation protocol for compression-technique papers generally — a methodological contribution with real value for reproducibility in the [[Quantization]] and [[Compression]] literature, and a reasonable scope for an undergraduate or early Master's thesis.
