# Visual Wake Words Dataset

**Full citation:** Chowdhery, A., Warden, P., Shlens, J., Howard, A., Rhodes, R. (2019). Visual Wake Words Dataset. arXiv:1906.05721

**PDF:** [arXiv](https://arxiv.org/abs/1906.05721)

**Linked concepts:** [[TinyML_Reference_Datasets]]

## Abstract summary

Introduces Visual Wake Words, a binary person-presence-detection dataset representing a common microcontroller vision use case, providing a realistic benchmark for tiny vision models operating within a few hundred kilobytes of memory.

## Research problem

Standard vision benchmarks (ImageNet-scale classification) do not reflect the realistic, memory-constrained task profile of microcontroller-class always-on vision applications; no standard dataset existed for the specific "is a person present" use case central to many embedded vision products.

## Key idea

Curate a binary person-presence dataset derived from a larger source (COCO), sized and labeled specifically to represent the realistic always-on microcontroller vision task, rather than a scaled-down general classification benchmark.

## Technical contribution

The Visual Wake Words dataset itself, plus baseline results showing state-of-the-art mobile models reach 85-90% accuracy within a 250 KB memory footprint.

## Experimental methodology

Derived from COCO images, relabeled for binary person-presence; baseline mobile architectures (MobileNet-class) evaluated under a 250 KB memory constraint.

## Results

85-90% accuracy achievable within 250 KB using contemporary mobile architectures, establishing a realistic, achievable target for microcontroller-class vision.

## Comparison with the state of the art

MLPerf Tiny's vision-side representative task (per [[MLPerf_Tiny]] and this concept's own Evolution text), and this concept's own previously self-flagged gap — tracked by reference in `00_Config/sources.yaml` but lacking a full deep-analysis record until this pass.

## Strengths

Directly representative of a real, common embedded vision product use case; realistic memory-budget framing (250 KB) rather than an arbitrary scaled-down benchmark; adopted as an MLPerf Tiny representative task.

## Weaknesses

Single task (binary person presence); derived from COCO's image distribution which may not represent all embedded-camera deployment contexts (lighting, angle, sensor quality).

## Limitations

Binary classification only; does not address localization or multi-person counting.

## Open questions

Per this concept's own open problems: is Visual Wake Words still discriminative for current architectures, or has it saturated? Are there successor/extension datasets worth tracking alongside it (e.g. more recent large-scale TinyML vision datasets)?

## Possible extensions

A saturation study measuring whether current architectures' Visual Wake Words accuracy has plateaued, extending this concept's own flagged research idea.

## Relevance to our research

Closes this concept's own explicitly self-flagged gap: an actively-monitored, MLPerf-Tiny-representative dataset that lacked a deep-analysis record.

## Possible thesis topics

Assessing whether Visual Wake Words remains a discriminative benchmark or has saturated, and if a next-generation successor dataset is warranted (directly matches this concept's existing thesis topic).

## Possible collaborations

None specific (Google origin).

## Links to related papers

[[2021_Banbury_MLPerfTiny]], [[2018_Warden_SpeechCommands]]
