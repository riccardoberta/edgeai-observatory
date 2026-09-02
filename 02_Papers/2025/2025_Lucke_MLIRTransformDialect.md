# The MLIR Transform Dialect: Your Compiler Is More Powerful Than You Think

**Full citation:** Lücke, M.P., Zinenko, O., Moses, W.S., Steuwer, M., Cohen, A. (2025). The MLIR Transform Dialect. Proceedings of the 23rd ACM/IEEE International Symposium on Code Generation and Optimization (CGO 2025). DOI: 10.1145/3696443.3708922

**PDF:** [ACM Digital Library](https://dl.acm.org/doi/10.1145/3696443.3708922) · [arXiv preprint](https://arxiv.org/abs/2409.03864)

**Verification note:** ACM/IEEE CGO 2025 conference proceedings; bibliographic details confirmed via WebSearch (CGO 2025 program, ACM DL listing).

**Linked concepts:** [[MLIR]]

## Abstract summary

Introduces the MLIR Transform Dialect, an infrastructure within MLIR that lets compiler transformations and optimization strategies themselves be expressed, composed, and controlled as first-class, schedulable IR — rather than being hard-coded into fixed compiler passes — giving users direct, fine-grained control over how and when transformations are applied. The paper argues and demonstrates that this makes MLIR-based compilers substantially more flexible and powerful for custom optimization strategies than typically assumed.

## Research problem

Traditional compiler infrastructures apply optimization passes in a fixed, largely opaque sequence, giving users (including EdgeAI-specific compiler/toolchain developers) little direct control over exactly how and when specific transformations are applied to their code, limiting the ability to build custom, domain-specific optimization strategies on top of a shared compiler infrastructure like MLIR.

## Key idea

Represent compiler transformations themselves as composable, schedulable operations within MLIR's own IR (the "Transform Dialect"), so that a user can express a custom transformation strategy — which passes to apply, in what order, to which parts of the program — as data/IR that the compiler interprets, rather than as fixed, hard-coded compiler-pass logic.

## Technical contribution

The Transform Dialect itself: an MLIR-native mechanism for expressing, composing, and scheduling compiler transformations as first-class IR, giving fine-grained programmatic control over optimization strategy construction within the shared MLIR infrastructure this Observatory's [[MLIR]] concept already tracks.

## Experimental methodology

Design and implementation of the Transform Dialect within MLIR, demonstrated through case studies showing custom transformation strategies expressed and applied via the dialect, illustrating the flexibility gain over fixed-pass-sequence compilation (per the CGO 2025 paper; specific case-study benchmarks not independently re-derived in this abstract-level record).

## Results

The Transform Dialect demonstrates that MLIR-based compilation can support substantially more flexible, user-controlled optimization strategies than the traditional fixed-pass-pipeline model, without requiring changes to MLIR's core infrastructure — the transformation-scheduling capability is built as a dialect on top of the existing system.

## Comparison with the state of the art

Extends this Observatory's [[MLIR]] concept's existing narrative — MLIR as shared, extensible infrastructure via dialects (as in [[2020_Lattner_MLIR]] and the industrial-scale validation in [[2026_Absar_HexagonMLIR]]) — with a mechanism specifically for controlling how transformations are composed and scheduled, a capability orthogonal to defining new dialects for new abstraction levels.

## Strengths

Peer-reviewed at a top compiler-systems venue (CGO, co-sponsored by ACM and IEEE); directly extends the core MLIR infrastructure this Observatory already tracks with a capability (transformation scheduling as first-class IR) rather than yet another point-solution compiler; multi-institutional authorship spanning academia and industry (Google, Meta-affiliated authors visible in related MLIR work).

## Weaknesses

Abstract-level record; concrete EdgeAI-specific use cases (e.g. applied to a Cortex-M or NPU compilation target) are not detailed here, since the paper's own case studies are likely general-purpose rather than EdgeAI-specific.

## Limitations

Building custom transformation strategies via the Transform Dialect still requires meaningful compiler expertise, echoing this Observatory's existing [[MLIR]] open problem that "building a new dialect still requires significant compiler expertise, limiting how broadly the infrastructure-level benefits translate into easy wins for EdgeAI practitioners without compiler backgrounds" — the Transform Dialect adds power, not necessarily accessibility.

## Open questions

Could the Transform Dialect's programmatic transformation-scheduling capability be used to build an EdgeAI-specific, hardware-aware optimization strategy (e.g. for NPU or Cortex-M targets) more easily than hand-writing new compiler passes? Does it reduce or increase the compiler expertise barrier this Observatory's [[MLIR]] concept already flags as a limitation?

## Possible extensions

Building a concrete EdgeAI-hardware-targeted (NPU or Cortex-M) optimization strategy using the Transform Dialect and comparing the engineering effort and resulting performance against a hand-written custom MLIR pass for the same target.

## Relevance to our research

Extends this Observatory's [[MLIR]] concept with a mechanism for controlling how optimizations are composed and scheduled within MLIR's shared infrastructure, complementing the existing narrative about MLIR as extensible, dialect-based infrastructure (see [[2020_Lattner_MLIR]], [[2026_Absar_HexagonMLIR]]).

## Possible thesis topics

Evaluating whether the MLIR Transform Dialect lowers or raises the practical barrier to building a custom, EdgeAI-hardware-targeted optimization strategy compared to hand-written compiler passes, directly testing this Observatory's existing [[MLIR]] open problem about compiler-expertise barriers.

## Possible collaborations

Compiler-infrastructure research groups working on MLIR and its ecosystem (the paper's authors span multiple MLIR-core-contributing institutions).

## Links to related papers

[[2020_Lattner_MLIR]], [[2026_Absar_HexagonMLIR]]
