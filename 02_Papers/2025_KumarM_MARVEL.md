# MARVEL: An End-to-End Framework for Generating Model-Class Aware Custom RISC-V Extensions for Lightweight AI

**Full citation:** Kumar M, A., O'Mahoney, C., Werle, P.K., Shanker, S., Nikolopoulos, D.S., Ji, B., Vandierendonck, H., John, D. (2025). MARVEL: An End-to-End Framework for Generating Model-Class Aware Custom RISC-V Extensions for Lightweight AI. arXiv:2508.01800 (to appear in IEEE Open Journal of Circuits and Systems). https://arxiv.org/abs/2508.01800

**Linked concepts:** [[RISC-V]], [[NAS]]

## Abstract summary

The authors present MARVEL, an automated end-to-end framework that profiles a high-level DNN model representation (focusing primarily on CNNs) and, from that profile, generates a custom RISC-V ISA extension plus an ISA-extended core and matching compiler tooling tailored to that specific model class, rather than relying on a fixed, general-purpose instruction set.

## Research problem

Designing custom RISC-V ISA extensions for efficient DNN deployment is normally a manual, expert-driven hardware/compiler co-design effort, which does not scale as the variety of EdgeAI model classes (CNNs, transformers, etc.) and target devices grows.

## Key idea

Automate the path from a high-level, Python-described DNN model class to a working, model-class-aware RISC-V ISA extension and corresponding compiler support, treating the extension-design problem itself as something a framework can search and generate rather than something an architect must hand-craft.

## Technical contribution

An automated profiling stage that extracts model-class-relevant computational patterns; an ISA-extension generation stage producing a custom RISC-V core; integrated compiler tooling that exposes the generated extension to standard deployment flows.

## Experimental methodology

Evaluation of the generated model-class-aware extensions on representative CNN workloads, comparing efficiency of the automatically generated RISC-V core/extension against baseline RISC-V deployment without the custom extension.

## Results

The end-to-end automated framework produces custom RISC-V extensions for the evaluated CNN model classes without requiring manual ISA-extension design, reported (per the framework's stated goal) to bring efficiency benefits over generic RISC-V cores while removing most of the manual hardware/compiler co-design effort.

## Comparison with the state of the art

Distinct from fixed-function accelerators (GAP-8) and from general-purpose vector extensions (Spatz/RVV) by being a generation framework rather than a single fixed design — closer in spirit to hardware-aware NAS, but applied to ISA-extension design rather than network architecture.

## Strengths

Automates a traditionally manual and expertise-intensive hardware design step; integrates compiler support rather than stopping at the hardware-design stage alone.

## Weaknesses

Primary demonstrated focus is CNN model classes; the framework's generality to other architecture families (transformers, RNNs) relevant to current EdgeAI research is not yet broadly validated.

## Limitations

As a very recently published (2025), not-yet-widely-cited framework, independent third-party validation and adoption track record are not yet available.

## Open questions

How well does MARVEL's automated extension-generation approach scale to non-CNN model classes? How does a MARVEL-generated extension compare in efficiency to a hand-designed extension targeting the same model class and RISC-V baseline?

## Possible extensions

Extending MARVEL's profiling and generation pipeline to transformer-class EdgeAI models; combining MARVEL-style automated ISA-extension generation with hardware-aware NAS in a single joint search loop.

## Relevance to our research

Adds an automated-design-tooling perspective to the RISC-V hardware entry, complementing the fixed-function (GAP-8) and general vector-extension (Spatz) approaches already represented there.

## Possible thesis topics

Extending MARVEL-style automated RISC-V extension generation to a non-CNN EdgeAI model class; comparative study of automatically generated versus hand-designed RISC-V extensions for the same target workload.

## Possible collaborations

Groups working on hardware-aware NAS and on RISC-V compiler toolchains that could supply complementary search algorithms or lowering infrastructure.

## Links to related papers

[[2023_Perotti_Spatz]], [[2018_Flamand_GAP8]]
