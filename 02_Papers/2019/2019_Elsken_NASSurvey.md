# Neural Architecture Search: A Survey

**Full citation:** Elsken, T., Metzen, J.H., Hutter, F. (2019). Neural Architecture Search: A Survey. Journal of Machine Learning Research, 20(55), 1-21.

**PDF:** [JMLR](https://jmlr.org/papers/v20/18-598.html)

**Verification note:** Bibliographic details confirmed via WebSearch (JMLR official listing, ACM DL, DBLP). Abstract-level verified.

**Linked concepts:** [[NAS]]

## Abstract summary

The canonical NAS survey, organizing the field along three orthogonal dimensions: search space (what architectures can be represented), search strategy (how the space is explored — RL, evolution, gradient-based), and performance estimation strategy (how candidate architectures are evaluated without full training).

## Research problem

By 2018-2019 NAS methods had proliferated rapidly (RL-based, evolutionary, gradient-based, Bayesian) with no shared framework for comparing them, making it hard to see which design choices (search space vs. search strategy vs. performance estimation) actually drove reported improvements.

## Key idea

Decompose any NAS method into three independent, comparable design axes — search space, search strategy, performance estimation strategy — so different methods can be compared component-by-component rather than as monolithic systems.

## Technical contribution

The three-axis NAS taxonomy that became the field's standard organizing framework, plus a systematic survey of methods within each axis as of 2018-2019.

## Experimental methodology

Literature survey and synthesis, not a novel empirical study.

## Results

Became the most-cited NAS survey (4900+ citations) and the standard reference framework subsequent NAS papers (including hardware-aware variants) use to position their own contributions.

## Comparison with the state of the art

Directly frames [[2017_Zoph_NeuralArchitectureSearchRL]] (an RL-based search strategy) within the broader design space, and is extended by hardware-aware surveys like this KB's [[2022_ChittyVenkata_NASHardwarePerspectiveSurvey]] which adds hardware cost as a fourth consideration layered on top of this taxonomy.

## Strengths

Extremely widely cited and adopted as the field's standard reference taxonomy; the three-axis decomposition remains useful for understanding any NAS method, including hardware-aware ones, seven years later.

## Weaknesses

Published in 2019, predates essentially all hardware-aware and TinyML-targeted NAS work, including this KB's own [[2026_Garavagno_HWNASUltraLowPower]].

## Limitations

No new empirical results; the taxonomy does not explicitly include hardware-cost as a first-class axis, an omission later hardware-aware NAS surveys had to address separately.

## Open questions

Does the three-axis (search space / search strategy / performance estimation) taxonomy need a fourth axis for hardware-cost modeling, or does hardware-awareness cleanly fold into "performance estimation" as later surveys suggest?

## Possible extensions

Positioning this KB's existing NAS anchor ([[2026_Garavagno_HWNASUltraLowPower]]) explicitly on this survey's three-axis taxonomy, to make explicit which axis its hardware-awareness modifies.

## Relevance to our research

The field's standard organizing framework for NAS, foundational to understanding and comparing this KB's existing hardware-aware NAS content — a clear gap this audit closes.

## Possible thesis topics

A systematic mapping of every NAS-adjacent paper in this KB onto this survey's three-axis taxonomy plus a hardware-cost axis, to identify which combinations remain underexplored for TinyML deployment.

## Possible collaborations

None specific — a foundational survey reference rather than an active research group.

## Links to related papers

[[2017_Zoph_NeuralArchitectureSearchRL]], [[2022_ChittyVenkata_NASHardwarePerspectiveSurvey]], [[2026_Garavagno_HWNASUltraLowPower]]
