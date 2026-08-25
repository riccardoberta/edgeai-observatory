# Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator

**Full citation:** Piechocki, M., Capotondi, A., Kraft, M. (2026). Empowering On-Device Model Adaptation with an Edge AI Inference Accelerator. arXiv:2607.18101 [cs.LG, cs.AR, cs.CV]. Submitted 20 Jul 2026. Accepted at the ITEM Workshop, ECML-PKDD 2026 (to appear in the joint post-workshop proceedings). ACM classes I.2.5, C.4. License CC BY 4.0. Code: https://github.com/MatPiech/accelerator-training. DOI: 10.48550/arXiv.2607.18101.

**Linked concepts:** [[On-device Learning]], [[Quantization]]

## Abstract summary

On-device model adaptation is essential for lifelong personalization on resource-constrained hardware, but compute/power/memory limits make end-to-end backpropagation impractical for modern DNNs. The paper proposes a heterogeneous adaptation pipeline that repurposes a commercial edge AI inference accelerator, Hailo-8L, for frozen-backbone feature extraction during on-device training: the computational graph is partitioned so the pre-trained backbone is quantized to INT8 and run on the accelerator, while only a lightweight FP32 classification head is fine-tuned on the host CPU. Across multiple architectures and datasets, this achieves up to 15.4× faster wall-clock training versus a Raspberry Pi 5 CPU baseline, competitive throughput in favorable settings, and consistently lower energy per sample. Post-training quantization restoration is shown to be crucial for preserving accelerator-generated feature quality and mitigating accuracy loss in quantization-sensitive architectures. Code released.

## Research problem

Lifelong, in-field personalization requires on-device model adaptation, but full end-to-end backpropagation is too compute/power/memory-expensive for resource-constrained hardware running modern DNNs. Existing inference accelerators (like Hailo-8L) are built purely for forward-pass inference and are not designed to support training at all — so the compute they offer is stranded for adaptation purposes unless something bridges that gap.

## Key idea

Don't build training support into new hardware — instead, repurpose an existing, commercially available, inference-only accelerator to do the expensive part of adaptation it's actually good at: forward-pass feature extraction. Partition the computational graph so the pre-trained backbone (quantized to INT8) runs entirely on the Hailo-8L accelerator as a frozen feature extractor, while only a small, lightweight FP32 classification head is trained (via backpropagation) on the host CPU. Because the backbone never needs gradients, this sidesteps the need for training support in the accelerator entirely.

## Technical contribution

A heterogeneous adaptation pipeline architecture partitioning pre-trained-backbone (frozen, INT8, accelerator-resident) from trainable-head (FP32, host CPU); the empirical finding that post-training quantization restoration is crucial for preserving the quality of accelerator-generated features and mitigating accuracy loss specifically in quantization-sensitive architectures — a concrete, reusable detail about what makes this repurposing pattern work versus fail; a released, reproducible implementation (GitHub) validated across multiple architectures and datasets.

## Experimental methodology

Multiple model architectures and datasets, comparing wall-clock training time and energy per sample of the Hailo-8L-accelerated frozen-backbone pipeline against a Raspberry Pi 5 CPU baseline running standard on-device fine-tuning. Also evaluates accuracy with and without a post-training quantization restoration step, isolating its effect on quantization-sensitive architectures specifically.

## Results

Up to 15.4× faster wall-clock training time versus the Raspberry Pi 5 CPU baseline; competitive throughput in favorable settings (implying not universally faster — some configurations trade off less favorably); consistently lower energy per sample across the tested architectures/datasets. Post-training quantization restoration is shown to be necessary to preserve accelerator-generated feature quality, with its absence causing accuracy loss specifically in quantization-sensitive architectures.

## Comparison with the state of the art

Frozen-backbone / head-only fine-tuning is an established pattern in [[On-device Learning]] (the Observatory already tracks TinyTL in this space); this paper's specific contribution is repurposing a strictly inference-oriented commercial accelerator (rather than a general-purpose or training-capable chip) as the feature-extraction engine, and characterizing the INT8 quantization-restoration step needed to keep the resulting features usable for downstream classification. Compared directly against a standard CPU-only training baseline (Raspberry Pi 5) rather than against other accelerator-based adaptation schemes, since — per the 2026-07-26 digest — this appears to be a first-of-its-kind demonstration for this specific accelerator-repurposing pattern.

## Strengths

A pragmatic, immediately reproducible pattern using commercially available hardware (Hailo-8L, Raspberry Pi 5) rather than custom silicon — genuinely accessible to a lab wanting to replicate it; code is released, materially raising reproduction value beyond what the abstract alone provides; the quantization-restoration finding is a specific, actionable, and non-obvious detail (not just "quantize and hope") that other groups repurposing inference accelerators for training would need to discover independently otherwise; validated across multiple architectures and datasets rather than a single case study.

## Weaknesses

"Competitive throughput in favorable settings" (rather than "faster throughput" universally) suggests the approach's advantage is wall-clock-training-time and energy specifically, not raw throughput in all configurations — the abstract does not clarify which settings are unfavorable or why; the hardware (Hailo-8L accelerator + Raspberry Pi 5 host) is a notch above the group's most constrained MCU targets, similar to several other papers in this backlog.

## Limitations

The approach fundamentally depends on the adaptation task being expressible as frozen-backbone-feature-extraction plus a small trainable head — tasks requiring adaptation of earlier/backbone layers (rather than just the final classifier) are not addressed by this architecture, since the whole point is that the backbone never needs gradients.

## Open questions

How far does the "repurpose an inference-only accelerator, freeze the backbone" pattern generalize beyond Hailo-8L — does it work equally well on other inference-only edge accelerators (Ethos-U, Coral), and does the quantization-restoration step transfer directly or need re-tuning per accelerator? What determines whether a given setting falls into the "competitive throughput" or a less favorable regime?

## Possible extensions

Generalize the "frozen backbone on the accelerator, head on the CPU" pattern beyond Hailo-8L to other inference-only edge accelerators (Ethos-U, Coral) and quantify how far the frozen-feature-extraction trick scales before quantization-restoration can no longer recover accuracy (the explicit 2026-07-26 digest hook); characterize which task/architecture combinations fall into the "competitive throughput" regime versus the less favorable ones the abstract hints at.

## Relevance to our research

A strong, practically reproducible fit for the Observatory's [[On-device Learning]] and [[Quantization]] branches, and directly relevant to heterogeneous edge personalization work given its use of commercially available, accessible hardware. Part of the July 2026 monthly report's "freeze most of the network, cheaply update a small part" thread alongside the RISC-V float16 training paper and CLASP (ECRAM continual learning) — three papers sharing a common on-device-training design pattern despite differing implementation substrates.

## Possible thesis topics

Repurposing inference-only NPUs for training: generalize this paper's pattern beyond Hailo-8L to other inference-only edge accelerators (Ethos-U, Coral) and quantify how far the frozen-feature-extraction trick scales before quantization-restoration can no longer recover accuracy (Master's, per the 2026-07-26 digest's explicit hook; bridges [[On-device Learning]] × [[Quantization]]).

## Possible collaborations

The paper's own group (Piechocki, Capotondi, Kraft) given the released, reproducible codebase — a natural starting point for direct extension work without needing to reimplement the pipeline from scratch.

## Links to related papers

Pairs conceptually with the RISC-V float16 on-device training paper (arXiv:2607.21130) from the same 2026-07-26 digest cycle — both freeze most of the network and differ only in *where* the cheap-to-train part runs (accelerator-offloaded frozen backbone here; low-precision training on the core there). Extends the Observatory's existing [[On-device Learning]] entry TinyTL with a commercial-accelerator-repurposing variant of the frozen-backbone pattern.
