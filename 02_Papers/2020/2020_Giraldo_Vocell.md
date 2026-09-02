# Vocell: A 65-nm Speech-Triggered Wake-Up SoC for 10-μW Keyword Spotting and Speaker Verification

**Full citation:** Giraldo, J.S.P., Lauwereins, S., Badami, K., Verhelst, M. (2020). Vocell: A 65-nm Speech-Triggered Wake-Up SoC for 10-μW Keyword Spotting and Speaker Verification. *IEEE Journal of Solid-State Circuits*, 55(4), 868–878. DOI: 10.1109/JSSC.2020.2968875

**PDF:** [DOI](https://doi.org/10.1109/JSSC.2020.2968875)

**Verification note:** IEEE Xplore returns a client-rendered page (not directly fetchable); bibliographic details, page range, and full author list confirmed via WebSearch cross-referencing dblp, Semantic Scholar, and the ADS abstract service. This record is abstract-level verified, not full-text-verified.

**Linked concepts:** [[DSP]], [[Keyword_Spotting]]

## Abstract summary

Vocell is a complete mixed-signal 65 nm SoC that interfaces directly to an analog microphone and performs always-on keyword spotting (KWS) plus speaker verification (SV) entirely on-chip at 10 μW, without external accesses. A dedicated neural-network accelerator module stores compressed parameters and computes an x-vector-based speaker-verification embedding, while a RISC-V CPU handles the remaining pipeline (feature extraction and classification). Evaluated on the VoxCeleb dataset (1,251 test speakers), the system reports over 95% verification accuracy.

## Research problem

Always-on voice wake-up requires keyword spotting and speaker verification to run continuously at extremely low power (single-digit microwatts) on a battery-constrained edge device, while still delivering enough accuracy to reject false wake-ups and unauthorized speakers — a combination that generic low-power DSP or MCU designs, not co-designed with the specific KWS/SV neural pipeline, struggle to meet simultaneously.

## Key idea

Co-design a mixed-signal front end (direct analog microphone interface) with a small, dedicated neural accelerator specialized for x-vector speaker-embedding computation, offloading only the SV neural workload to hardware while keeping the more flexible parts of the pipeline (feature extraction, final classification) on a general-purpose RISC-V core — splitting the "always-on, fixed workload" part from the "occasionally-needed, flexible" part of the KWS/SV pipeline onto the hardware type best suited to each.

## Technical contribution

A fabricated, silicon-validated 65 nm SoC combining an analog-microphone-direct mixed-signal front end, a compressed-parameter neural accelerator for x-vector speaker verification, and a RISC-V CPU for feature extraction/classification, achieving full KWS+SV functionality at 10 μW system power.

## Experimental methodology

Silicon test-chip measurements of system-level power consumption during always-on operation; speaker-verification accuracy evaluated on the VoxCeleb dataset (1,251 test speakers) using the on-chip x-vector accelerator pipeline.

## Results

10 μW total system power for combined always-on KWS and speaker verification; over 95% speaker-verification accuracy on VoxCeleb — demonstrating that microwatt-power budgets are compatible with dataset-validated (not just toy-benchmark) speaker-verification accuracy.

## Comparison with the state of the art

Distinguishes itself from KWS-only always-on chips by adding on-chip speaker verification (not just wake-word detection) within the same microwatt power envelope, and from software-only SV pipelines by moving the x-vector computation into dedicated low-power silicon rather than relying on a always-on general-purpose DSP/MCU running compressed neural inference in software.

## Strengths

Full mixed-signal, silicon-validated system (not simulation); validated on a real, sizeable speaker-verification dataset (VoxCeleb) rather than a small custom set; demonstrates a practical split between fixed-function accelerator and general-purpose RISC-V core that is broadly reusable pattern for other always-on audio pipelines.

## Weaknesses

65 nm process node is dated relative to current commercial always-on audio SoCs; the record here is abstract-level (page range and headline results only), so architectural details of the RISC-V/accelerator interface and the exact compression scheme for x-vector parameters are not captured in this summary.

## Limitations

Single application domain (audio/speech); does not address multi-modal always-on sensing (e.g. combined audio+motion wake triggers) or more recent transformer-based speaker-verification approaches.

## Open questions

How does the fixed-function x-vector accelerator + RISC-V split generalize to other always-on biosignal or sensor pipelines (cf. [[Biosignals]])? Would a similar mixed-signal, dedicated-accelerator approach scale to keep pace with more accurate but more compute-heavy modern speaker-verification models?

## Possible extensions

Applying the same "fixed neural workload to dedicated accelerator, flexible logic to general-purpose core" architectural split to other always-on edge sensing pipelines beyond audio, and updating the accelerator for more recent, more accurate SV embedding models under the same microwatt power budget.

## Relevance to our research

A concrete silicon example for [[DSP]] and [[Keyword_Spotting]] of how mixed-signal front ends and dedicated small accelerators combine with a general-purpose RISC-V core to hit microwatt-level always-on power budgets — a useful comparison point against later, MDPI-published KWS ICs such as [[2023_Wu_KeywordSpottingIC]].

## Possible thesis topics

A comparative power/accuracy study of Vocell-style dedicated-accelerator KWS/SV architectures against more recent subband-energy-feature or learned-feature always-on KWS ICs, isolating how much of the power/accuracy trade-off comes from the feature-extraction stage versus the classification stage.

## Possible collaborations

Mixed-signal SoC design groups working on always-on audio front ends (KU Leuven MICAS group and similar low-power SoC design labs).

## Links to related papers

[[2023_Wu_KeywordSpottingIC]]
