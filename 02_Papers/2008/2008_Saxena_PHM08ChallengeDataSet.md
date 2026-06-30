# PHM08 Challenge Data Set

**Full citation:** Saxena, A., Goebel, K. (2008). PHM08 Challenge Data Set. *NASA Prognostics Data Repository, NASA Ames Research Center*. https://www.nasa.gov/intelligent-systems-division/discovery-and-systems-health/pcoe/pcoe-data-set-repository/

**Linked concepts:** [[Predictive_Maintenance]]

## Abstract summary

The authors release the PHM08 Challenge Data Set, a simulated turbofan-engine degradation dataset generated with the C-MAPSS (Commercial Modular Aero-Propulsion System Simulation) tool, providing run-to-failure sensor trajectories used as a standardized benchmark for developing and evaluating remaining-useful-life (RUL) prediction algorithms.

## Research problem

Predictive maintenance and prognostics-and-health-management (PHM) research on remaining-useful-life estimation lacked a standardized, public, realistic dataset, forcing different research groups to validate methods on private, non-reproducible industrial data that could not be used to fairly compare competing RUL-prediction algorithms.

## Key idea

Use a high-fidelity physics-based simulation of a turbofan engine (C-MAPSS) to generate multiple, varied run-to-failure degradation trajectories under different operating conditions and fault modes, producing a dataset realistic enough to support meaningful RUL-prediction research while being fully public and reproducible, unlike proprietary real-world industrial sensor logs.

## Technical contribution

The dataset itself: multiple sets of multivariate time-series sensor readings from simulated turbofan engines, run from a nominal condition to simulated failure, under varying initial wear states, operating conditions, and fault modes, packaged as a public PHM challenge with an associated leaderboard/evaluation methodology for RUL-prediction accuracy.

## Experimental methodology

Provides the simulated sensor trajectories together with a defined RUL-prediction task and scoring methodology (penalizing late predictions more heavily than early ones, reflecting the asymmetric cost of failing to predict maintenance needs in time), used as the basis for the original PHM08 challenge competition and all subsequent research using the dataset.

## Results

Establishes a shared, standardized benchmark that has been used by a very large number of subsequent predictive-maintenance and RUL-prediction papers, becoming the de facto standard dataset for the subfield and enabling direct, reproducible comparison across many different modeling approaches (from classical regression to deep learning).

## Comparison with the state of the art

Fills a clear gap relative to prior practice in the field, where RUL-prediction methods were validated on inconsistent, often private datasets; PHM08/C-MAPSS provided the realistic, public, and reproducible alternative that the field still relies on heavily.

## Strengths

Public, free, and widely adopted, enabling broad reproducibility and comparison; physics-simulation-based generation allows controlled variation of operating conditions and fault modes that would be difficult or impossible to obtain from real fleet sensor logs.

## Weaknesses

Being a simulation rather than real sensor data, it may not capture all the noise characteristics, sensor failure modes, and unmodeled degradation mechanisms present in real-world turbofan engine fleets, so strong results on this dataset do not guarantee equivalent real-world performance.

## Limitations

Specific to turbofan engine degradation; the dataset's particular sensor set, fault modes, and operating-condition envelope do not directly generalize to other industrial asset types (e.g. motors, pumps, bearings) without independent validation on asset-specific data.

## Open questions

How well do RUL-prediction methods that perform strongly on the simulated PHM08/C-MAPSS data transfer to real turbofan fleet sensor logs, and to other industrial asset classes with different degradation dynamics and sensor sets entirely?

## Possible extensions

Validating RUL-prediction methods developed on PHM08/C-MAPSS against real (even if smaller-scale) turbofan or other industrial asset sensor logs, to test simulation-to-reality transfer; extending the standardized-benchmark approach to other asset classes relevant to edge-deployed predictive maintenance.

## Relevance to our research

The foundational shared benchmark dataset for remaining-useful-life prediction referenced throughout the [[Predictive_Maintenance]] literature; essential reference whenever the Observatory evaluates a new RUL-prediction method against the field's standard comparison point.

## Possible thesis topics

Comparing a hierarchical edge-gateway-cloud RUL-prediction pipeline (as in [[2024_delaFuente_ESN-PdM]]) when trained/evaluated on PHM08/C-MAPSS versus on real sensor data from a non-aerospace industrial asset, to assess how much of its reported accuracy/efficiency trade-off is dataset-specific.

## Possible collaborations

The NASA Prognostics Center of Excellence and groups working on simulation-to-reality transfer for prognostics and health management.

## Links to related papers

[[2024_delaFuente_ESN-PdM]]
