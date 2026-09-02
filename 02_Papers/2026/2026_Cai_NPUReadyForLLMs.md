# Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference

**Full citation:** Cai, G., Tian, R., Yang, L., Ren, Z., Yuan, J., Li, L., Wang, J. (2026). Is Your NPU Ready for LLMs? Dissecting the Hidden Efficiency Bottlenecks in Mobile LLM Inference. arXiv:2607.05475 [cs.AR, cs.AI]. Submitted 6 Jul 2026. DOI: 10.48550/arXiv.2607.05475.

**Linked concepts:** [[NPU]], [[Quantization]] — also part of [[Mixture-of-Experts (MoE) & Edge LLM Serving]]; this paper is the diagnostic foundation HeteroMosaic explicitly builds on.

## Abstract summary

Deploying LLMs on mobile devices improves privacy and latency but is severely bottlenecked by hardware inefficiency. The paper presents the first comprehensive, cross-layer measurement study of mobile LLM inference, spanning five mainstream frameworks (e.g., llama.cpp, GENIE) and three hardware backends (CPU, GPU, NPU). PowerBench, a fine-grained profiling tool, provides the first backend-specific energy attribution beyond device-level measurement. Three findings: (1) framework-induced performance gaps are amplified up to 10× on NPUs via custom operators; (2) a phase split where NPUs excel at compute-bound prefilling while CPUs win at memory-bound decoding, driven by the NPU's preference for large fixed-shape workloads clashing with decode's small, dynamic kernels; (3) suboptimal thread configs, uncoordinated NPU sleep latencies, and CPU polling intervals waste up to 40% of energy. An energy-oriented best-practice configuration is estimated to cut NPU-backend energy by up to 54.8% across three datasets.

## Research problem

On-device LLM inference is the fastest-moving edge deployment frontier, but almost all published work is optimization-first (a new kernel, a new quantization scheme) rather than measurement-first — meaning the field has been optimizing without a clear, backend-specific picture of where energy and latency actually go across the CPU/GPU/NPU stack that real mobile SoCs expose. The paper asks: where exactly does mobile LLM inference waste energy, and does that waste differ systematically across serving frameworks and hardware backends?

## Key idea

Build a profiling tool (PowerBench) capable of backend-specific energy attribution — not just device-level power draw — and use it to run the first comprehensive cross-layer measurement study spanning five serving frameworks and three hardware backends. The premise is diagnostic, not prescriptive: characterize the bottlenecks precisely enough that the field's optimization efforts can be targeted rather than guessed at.

## Technical contribution

PowerBench, a fine-grained profiler giving the first backend-specific (not just device-level) energy attribution for mobile LLM inference; the empirical discovery of a prefill/decode phase split across NPU and CPU backends, tied to a specific hardware-preference explanation (NPUs prefer large fixed-shape workloads; decode's small, dynamic kernels clash with that); quantification of framework-induced NPU performance variance (up to 10×) driven by divergent offloading and quantization strategies; identification of a concrete, previously undercounted energy-waste source (thread configuration, NPU sleep latency coordination, CPU polling) worth up to 40% of energy.

## Experimental methodology

Cross-layer measurement across five mainstream serving frameworks (including llama.cpp and GENIE, named explicitly in the abstract) and three hardware backends (CPU, GPU, NPU) on mobile hardware, using the custom PowerBench profiler for backend-specific energy attribution. Evaluated across three datasets to validate the derived best-practice configuration.

## Results

Framework-induced performance gaps reach up to 10× on NPUs when custom operators are used, driven by divergent offloading and quantization strategies across frameworks. A clear phase split: NPUs excel at compute-bound prefilling, CPUs outperform all other backends at memory-bound decoding. Scheduling inefficiencies (suboptimal thread configuration, uncoordinated NPU sleep latencies, CPU polling intervals) waste up to 40% of energy — headroom missed by prior optimization work. An energy-oriented best-practice configuration derived from these findings is estimated to reduce NPU-backend energy consumption by up to 54.8% across three datasets.

## Comparison with the state of the art

Explicitly positioned as the first comprehensive, cross-layer measurement study of its kind — its point of comparison is prior work's absence of backend-specific energy attribution (device-level measurement being the norm) rather than a competing optimization technique. The 2026-07-19 digest treats HeteroMosaic as the direct constructive follow-on: where this paper diagnoses where the waste is, HeteroMosaic's heterogeneous iGPU+NPU scheduler is built to recover it.

## Strengths

Low algorithmic novelty but high diagnostic novelty — the prefill-on-NPU/decode-on-CPU characterization and backend-specific energy attribution are immediately reusable insights for anyone deploying LLMs on mobile hardware, independent of which optimization technique they eventually apply; the "40% wasted on scheduling" finding reshapes how practitioners should think about deployment (configuration matters as much as algorithm choice); PowerBench itself is a reusable measurement asset, not just a one-off result.

## Weaknesses

As a measurement/diagnostic paper, it proposes no new model, kernel, or training technique — its value is entirely in characterization, so a lab wanting to act on it needs to pair it with an optimization technique (as HeteroMosaic does); the abstract does not specify which mobile SoCs/NPUs were profiled, which matters for how directly the 40%-waste and 54.8%-energy-reduction figures transfer to different hardware.

## Limitations

Findings are specific to the mobile LLM inference regime studied (unspecified SoCs/NPUs at the abstract level) and to the five frameworks profiled; whether the phase-split characterization (NPU-prefill/CPU-decode) and the 40% scheduling-waste figure generalize to other NPU architectures or to genuinely embedded (sub-mobile, MCU-class) NPUs is untested.

## Open questions

Does the prefill-on-NPU/decode-on-CPU phase split hold on non-mobile edge NPUs (e.g., Cortex-M-class NPU companions), or is it specific to the mobile SoC NPU designs profiled here? How much of the 40% scheduling waste is recoverable in an open framework (microTVM, ONNX Runtime) versus requiring vendor-specific low-level access?

## Possible extensions

Reproduce the prefill-on-NPU/decode-on-CPU phase split on the group's own devices and quantify how much of the 40% scheduling waste is recoverable in an open framework such as microTVM or ONNX Runtime (the explicit 2026-07-13 digest hook); extend PowerBench-style backend-specific energy attribution to genuinely embedded NPU targets outside the mobile-SoC class this paper studies.

## Relevance to our research

Strong reference and methodology value for [[NPU]] deployment and on-device LLM work generally; PowerBench and the phase-split insight are directly reusable for the Observatory's own benchmarking work. Also the diagnostic anchor for the broader "Mixture-of-Experts (MoE) & Edge LLM Serving" cluster now formalized in the taxonomy (2026-08-25 Evolution note) — HeteroMosaic, PolyQ, APEX, EdgeXpert, and UnionSparse all build on or extend the problem space this paper first measured.

## Possible thesis topics

Backend-aware scheduling for on-device LLM inference: reproduce the prefill-on-NPU/decode-on-CPU phase split from this paper and quantify how much of the 40% scheduling waste is recoverable in an open framework, e.g. microTVM or ONNX Runtime (Master's, per the 2026-07-13 digest's explicit hook).

## Possible collaborations

No specific group flagged in prior digests; the released PowerBench methodology (if the tool itself is open) would be a natural starting point for any lab benchmarking effort rather than requiring formal collaboration with the authors.

## Links to related papers

The diagnostic foundation for HeteroMosaic (arXiv:2607.12839) — the 2026-07-19 digest explicitly frames the pair as "diagnose → schedule." Also part of the same emerging "edge LLM/MoE serving" cluster as PolyQ, APEX, EdgeXpert, and UnionSparse (none of which has a `02_Papers/` record predating this backlog-clearing pass).
