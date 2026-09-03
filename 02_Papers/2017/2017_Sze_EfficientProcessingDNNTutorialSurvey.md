# Efficient Processing of Deep Neural Networks: A Tutorial and Survey

**Full citation:** Sze, V., Chen, Y.H., Yang, T.J., Emer, J.S. (2017). Efficient Processing of Deep Neural Networks: A Tutorial and Survey. Proceedings of the IEEE, 105(12), 2295-2329.

**PDF:** [arXiv](https://arxiv.org/abs/1703.09039)

**Linked concepts:** [[NPU]]

## Abstract summary

The field's most-cited tutorial and survey on efficient DNN processing, covering DNN fundamentals, hardware platforms and architectures, and key trends for reducing computation cost via hardware design changes alone or joint hardware/algorithm co-design.

## Research problem

By 2017, DNN efficient-processing research spanned algorithms, architectures, and circuits with no single, systematically organized reference connecting these layers for newcomers or practitioners choosing an approach.

## Key idea

Provide a comprehensive, layered tutorial spanning DNN computation fundamentals through hardware architecture choices (dataflow taxonomy) to joint hardware/algorithm co-design trends, written by the same MIT group (Sze, Chen) responsible for the Eyeriss accelerator and its Row-Stationary dataflow.

## Technical contribution

A structured, tutorial-level organization of the entire efficient-DNN-processing design space, including the dataflow taxonomy (weight-stationary, output-stationary, no-local-reuse, row-stationary) this concept's Eyeriss anchor introduces in research-paper form.

## Experimental methodology

Tutorial/survey synthesis, not new empirical results, though it draws on the authors' own Eyeriss silicon results as a running example.

## Results

Became the single most-cited reference in the entire efficient-DNN-hardware field (6000+ citations), still the standard starting point/teaching reference.

## Comparison with the state of the art

The tutorial-form companion to [[2017_Chen_Eyeriss]] (same lead authors), presenting the dataflow taxonomy and design-space framework at teaching depth rather than as one research contribution — the two papers should be read together as this concept's foundational pair.

## Strengths

Extraordinarily widely cited and adopted as the field's standard teaching reference; written by the same team behind Eyeriss, giving direct continuity between tutorial framework and research contribution; comprehensive layered coverage (algorithm through circuit).

## Weaknesses

A 2017 snapshot — predates the mobile/edge NPU commercialization wave (Edge TPU, Samsung's multi-precision NPU, Hexagon) this concept now tracks in depth.

## Limitations

Tutorial-level treatment necessarily sacrifices some depth versus dedicated research papers on each sub-topic; no new empirical results of its own beyond citing the authors' prior work.

## Open questions

How would this tutorial's dataflow taxonomy and design-space framework need to be extended to cover the LLM/MoE-serving-era NPU workloads this concept's more recent anchors ([[2025_Chen_HeteroInfer]], [[2026_Bryngelson_AppleNeuralEngine]]) address?

## Possible extensions

An updated version of this tutorial's dataflow taxonomy incorporating the heterogeneous GPU/NPU phase-split patterns (prefill vs. decode) this concept's recent LLM-serving anchors identify.

## Relevance to our research

The single most foundational, most-cited teaching reference in the entire NPU/accelerator field — a significant gap given this concept already anchors on the same authors' Eyeriss research paper.

## Possible thesis topics

Extending this tutorial's classical dataflow taxonomy to explicitly cover LLM-serving-era heterogeneous accelerator patterns (phase-split GPU/NPU execution).

## Possible collaborations

MIT (Sze/Emer group), the same lineage behind Eyeriss.

## Links to related papers

[[2017_Chen_Eyeriss]], [[2014_Chen_DianNao]]
