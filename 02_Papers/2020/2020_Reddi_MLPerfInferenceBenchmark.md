# MLPerf Inference Benchmark

**Full citation:** Reddi, V.J., Cheng, C., Kanter, D., Mattson, P., et al. (2020). MLPerf Inference Benchmark. 2020 ACM/IEEE 47th Annual International Symposium on Computer Architecture (ISCA 2020), 446-459. DOI: 10.1109/ISCA45697.2020.00045

**PDF:** [arXiv](https://arxiv.org/abs/1911.02549)

**Linked concepts:** [[MLPerf_Tiny]]

## Abstract summary

Introduces MLPerf Inference, the MLCommons/MLPerf consortium's industry-standard benchmark suite for measuring ML inference performance across datacenter, edge, and mobile systems, establishing the methodology and governance model MLPerf Tiny later specializes for microcontroller-class hardware.

## Research problem

ML inference performance claims across hardware vendors and software stacks were largely incomparable, with no industry-standard, fair, and reproducible benchmark methodology — a problem MLPerf Training had already addressed for training but not inference.

## Key idea

Establish a standardized inference benchmark suite spanning representative tasks, quality targets, and scenarios (single-stream, multi-stream, server, offline), governed by a broad industry/academic consortium to ensure fairness and comparability.

## Technical contribution

The MLPerf Inference methodology: task selection criteria, quality-target definitions, submission/review process, and scenario taxonomy — later directly inherited and adapted by MLPerf Tiny for the microcontroller regime.

## Experimental methodology

Defines the benchmark suite and reports first-round submission results across a range of hardware from datacenter accelerators to mobile SoCs.

## Results

Established an industry-standard, cross-vendor-comparable inference benchmark now used across the ML hardware industry; nearly 1000 citations reflecting its foundational role.

## Comparison with the state of the art

The direct methodological parent of [[2021_Banbury_MLPerfTiny]], which this concept's own Evolution text notes explicitly excluded MCU-class devices — a gap MLPerf Tiny was created to fill using this paper's governance and methodology as a template.

## Strengths

Extremely widely cited and industry-adopted; rigorous, broad-consortium governance; directly explains why MLPerf Tiny needed to exist as a separate effort.

## Weaknesses

Explicitly excludes microcontroller-class devices (the regime MLPerf Tiny addresses), and datacenter/mobile-focused task selection does not capture TinyML-specific workloads.

## Limitations

Governance complexity (broad multi-company consortium) makes rapid iteration slower than a single-lab benchmark.

## Open questions

How much of MLPerf Inference's scenario taxonomy (single-stream, multi-stream, server, offline) is meaningful at MCU scale, versus needing simplification as MLPerf Tiny did?

## Possible extensions

A direct comparison of MLPerf Inference's and MLPerf Tiny's methodological choices, documenting exactly what had to change to make the benchmark meaningful at microcontroller scale.

## Relevance to our research

The methodological and governance parent of this concept's primary anchor, explaining why MCU-class inference needed its own dedicated benchmark suite rather than an extension of the general-purpose one.

## Possible thesis topics

A structured comparison of MLPerf Inference's and MLPerf Tiny's task-selection and scenario-taxonomy choices, as a case study in benchmark design for extremely resource-constrained hardware.

## Possible collaborations

MLCommons/MLPerf consortium.

## Links to related papers

[[2021_Banbury_MLPerfTiny]]
