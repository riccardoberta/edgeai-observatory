# Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core

**Full citation:** Hubinet, B., Moellic, P.-A., Savry, O., Potin, O., Rigaud, J.-B. (2026). Hardware-Software Co-Design for Float16 On-Device Training on RISC-V Single-Core. arXiv:2607.21130 [cs.AR, cs.AI]. Submitted 23 Jul 2026. Accepted to IEEE PRIME 2026. Affiliations per the 2026-07 monthly report: CEA-Leti / Mines Saint-Étienne. DOI: 10.48550/arXiv.2607.21130.

**PDF:** [arXiv PDF](https://arxiv.org/pdf/2607.21130)

**Linked concepts:** [[RISC-V]], [[On-device_Learning]], [[Quantization]] (float16 as a precision-reduction technique for training, not inference)

**Verification note:** every web-fetch attempt to independently retrieve this paper's arXiv page (five attempts across this session) was blocked by an in-session rate limit that did not affect most other papers fetched in the same session. This record is therefore built entirely from the 2026-07-26 weekly digest's own full-text-verified summary (that digest's sourcing note states papers were read at the abstract level from arXiv, consistent with its stated methodology) and the 2026-07 monthly report's cross-references, rather than an independent re-verification in this pass. This arXiv fetch should be re-run (or the PDF opened directly) before citing the specific figures below in a survey or thesis.

## Abstract summary (as reported by the source digest)

The paper leverages the standard RISC-V `Zfh` (scalar float16) and `Zvfh` (vector float16) ISA extensions to enable end-to-end on-device training on a resource-constrained RISC-V single core — not an accelerator, not application-class silicon — contributing an open-source framework built on AIfES, an existing open-source embedded training framework. Using float16 instead of float32 cuts training memory footprint by roughly 50% with minimal model-quality degradation. Transfer-learning and fine-tuning scenarios are supported through layer-freezing (training only selected layers). The hardware cost of adding `Zfh` ISA support to an RV64GC superscalar out-of-order FPGA softcore is quantified at +1.15% LUT6 and +0.05% FF at 175MHz, with a `Zvfh` vector implementation outlined within the same core.

## Research problem

Complete on-device *training* (not just inference) on truly MCU-class, single-core RISC-V hardware has been aspirational rather than characterized: prior on-device training work either targets more capable application-class hardware, relies on dedicated accelerators, or hasn't quantified the actual silicon cost of adding the precision support (float16) that makes training memory-tractable on a constrained core in the first place.

## Key idea

Use RISC-V's standardized `Zfh`/`Zvfh` float16 ISA extensions — rather than a custom precision format requiring bespoke hardware — to enable end-to-end training directly on a single, resource-constrained RISC-V core, built on top of an existing open-source embedded training framework (AIfES) rather than a from-scratch training stack. Layer-freezing support lets transfer-learning/fine-tuning scenarios train only the layers that need updating, further reducing the memory and compute burden.

## Technical contribution

An open-source, standardized-ISA float16 on-device *training* framework (as distinct from inference) built on AIfES; end-to-end characterization spanning ISA hardware area overhead through to model training-quality outcomes — a full-stack accounting rare in this literature; layer-freezing support for transfer learning/fine-tuning; a quantified answer to "is it worth adding float16 ISA support to my RISC-V core?" via the +1.15% LUT6 / +0.05% FF area-overhead figures.

## Experimental methodology (as reported by the source digest)

Implemented on a resource-constrained RISC-V single core using the standard `Zfh` scalar float16 extension, with a `Zvfh` vector float16 implementation outlined within the same core. ISA area overhead measured on an RV64GC superscalar out-of-order FPGA softcore at 175MHz. Training memory footprint and model-quality degradation compared between float16 and float32 precision.

## Results (as reported by the source digest)

Float16 cuts training memory footprint by roughly 50% versus float32, with minimal model-quality degradation. Adding `Zfh` scalar float16 ISA support to an RV64GC superscalar out-of-order FPGA softcore costs only +1.15% LUT6 and +0.05% FF at 175MHz — a small, precisely quantified hardware cost for the memory-footprint benefit.

## Comparison with the state of the art

Low-precision training and layer-freezing are each individually established techniques (the Observatory already tracks TinyTL and TinyTrain in [[On-device_Learning]], and float16/low-precision formats generally in [[Quantization]]); the paper's specific contribution, per the 2026-07-26 digest, is "a fully open-source float16 *training* path riding on standardized RISC-V float16 extensions, characterized end-to-end from ISA area overhead up to model accuracy on a single MCU-class core" — genuinely reproducible because it uses standardized ISA extensions and an existing open framework rather than proprietary hardware or a closed training stack.

## Strengths

Standardized ISA extensions (not a custom format) mean the hardware cost/benefit analysis is directly transferable to any RISC-V core considering the same extensions, not locked to one vendor's silicon; built on an existing open-source framework (AIfES) rather than a closed, from-scratch training stack, materially lowering the barrier to reproduction; the ISA-to-accuracy full-stack characterization is unusually complete for this literature, turning "is float16 training worth it on my core?" into an answerable, data-driven question rather than a judgment call; true single-core, MCU-class target (not an accelerator or application-class chip) — directly in this Observatory's core hardware focus.

## Weaknesses

This entire record rests on secondhand (digest) reporting rather than this pass's own independent verification — the specific percentages (50% memory reduction, +1.15% LUT6, +0.05% FF) should be treated as provisional until directly re-checked from the paper; no information available at this remove about which models/tasks the "minimal model-quality degradation" claim covers, which matters enormously for how broadly the finding generalizes.

## Limitations

As reported, the `Zvfh` vector float16 implementation is only "outlined" (not fully measured) within the same core — meaning the hardware-cost quantification (+1.15% LUT6, +0.05% FF) applies specifically to the scalar `Zfh` extension, and the vector extension's cost/benefit is not yet characterized with the same rigor.

## Open questions

Which specific models and tasks does the "minimal model-quality degradation" claim cover, and does it hold for the kinds of workloads (keyword spotting, HAR, biosignals) this Observatory's lab typically works with? How does float16 training compare against integer/quantized training (cf. Deutel 2024, on-device training on quantized Cortex-M) on the *same* RISC-V core — which wins on the memory/accuracy/energy Pareto front for true MCU-class targets? What is the actual measured (not just outlined) cost and benefit of the `Zvfh` vector extension?

## Possible extensions

Directly re-verify this record's figures from the full PDF, given the fetch limitations in this pass; extend EliosLab's AIfES-based infrastructure (already open-source per this paper) to compare `Zfh`/`Zvfh` float16 training against int8/quantized training on the same RISC-V core (the explicit 2026-07-26 and July-2026-monthly-report hook); fully characterize the `Zvfh` vector extension's hardware cost and training-time benefit, not just the outlined scalar (`Zfh`) case.

## Relevance to our research

A direct, high-priority fit for the Observatory's [[RISC-V]] and [[On-device_Learning]] branches — open-source, MCU-class, and immediately actionable given the released AIfES-based infrastructure. Both the 2026-07-26 weekly digest and the July 2026 monthly report independently flagged this as the strongest deep-analysis candidate of its respective cycles; the monthly report specifically noted "open-source infrastructure already exists (AIfES-based), so this is unusually low-friction to start" for the Pareto-study thesis topic below.

## Possible thesis topics

Float16 vs int8 on-device training on RISC-V: extend this paper by comparing its `Zfh`/`Zvfh` float16 training path against integer/quantized training (cf. Deutel 2024) on the same RISC-V core — which wins on the memory/accuracy/energy Pareto front for true MCU-class targets? (Master's/PhD; bridges [[RISC-V]], [[On-device_Learning]], [[Quantization]] — explicitly flagged as the July 2026 monthly report's second-ranked research opportunity, "unusually low-friction to start" given the existing open AIfES infrastructure.)

## Possible collaborations

The paper's own author group (Hubinet, Moellic, Savry, Potin, Rigaud — CEA-Leti / Mines Saint-Étienne per the July 2026 monthly report) is building open, reproducible embedded-training infrastructure directly usable by this lab, making them a genuine collaboration candidate rather than merely a citation, per the monthly report's own assessment.

## Links to related papers

Extends the Observatory's existing [[On-device_Learning]] records (TinyTL, TinyTrain) and connects to [[2024_Deutel_OnDeviceTrainingQuantizedCortexM]] as the natural comparison point for the float16-vs-int8 thesis topic above. Pairs conceptually with the Hailo-8L on-device adaptation paper (arXiv:2607.18101, `02_Papers/2026/2026_Piechocki_Hailo8LAdaptation.md`) from the same 2026-07-26 digest cycle — both reduce on-device training cost, one via low-precision training on the core, the other via offloaded frozen-backbone inference.
