# Remaining Useful Life Prediction Using Deep Learning Approaches: A Review

**Full citation:** Wang, Y., Zhao, Y., Addepalli, S. (2020). Remaining Useful Life Prediction Using Deep Learning Approaches: A Review. Procedia Manufacturing, 49, 81-88. DOI: 10.1016/j.promfg.2020.06.015

**PDF:** [ScienceDirect](https://www.sciencedirect.com/science/article/pii/S2351978920316528)

**Linked concepts:** [[Predictive_Maintenance]]

## Abstract summary

Reviews deep-learning approaches to Remaining Useful Life (RUL) prediction, organizing the literature around four representative architecture families: Auto-encoders, Deep Belief Networks, CNNs, and RNNs.

## Research problem

RUL prediction research using deep learning had grown across disparate architecture families with no unified review connecting them, despite RUL prediction's central role in reducing unplanned downtime and maintenance cost.

## Key idea

Organize the deep-learning RUL literature by architecture family, comparing how each represents and models degradation trajectories.

## Technical contribution

A structured, architecture-family-based taxonomy of deep-learning RUL prediction methods.

## Experimental methodology

Literature review and synthesis, not new empirical results.

## Results

A widely-cited (350+) reference organizing the RUL prediction literature, showing deep learning's growing role in machine health monitoring.

## Comparison with the state of the art

Complements this concept's PHM08/C-MAPSS benchmark anchor ([[2008_Saxena_PHM08ChallengeDataSet]]) with a structured view of the modeling approaches evaluated on it and similar datasets.

## Strengths

Widely cited, clear architecture-family organization, directly relevant to this concept's central prediction task.

## Weaknesses

Review only, no new empirical results; predates the TinyML/edge-deployment-focused RUL work this concept otherwise tracks.

## Limitations

Does not address resource-constrained deployment; a pre-edge-computing-era literature snapshot.

## Open questions

Which of the four reviewed architecture families compresses most gracefully for on-device RUL prediction under this concept's edge/gateway/cloud hierarchical routing framework?

## Possible extensions

An updated version of this taxonomy incorporating edge-deployment feasibility as a further comparison axis.

## Relevance to our research

A structured entry point connecting this concept's PHM08/C-MAPSS benchmark to the broader deep-learning RUL literature, useful context for the edge-deployment-focused papers already tracked.

## Possible thesis topics

Benchmarking representative RUL architectures from each of the four reviewed families for on-device feasibility under a fixed microcontroller memory budget.

## Possible collaborations

None specific.

## Links to related papers

[[2008_Saxena_PHM08ChallengeDataSet]], [[2024_delaFuente_ESN-PdM]]
