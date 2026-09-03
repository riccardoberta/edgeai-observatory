# Neural Architecture Search Survey: A Hardware Perspective

**Full citation:** Chitty-Venkata, K.T., Somani, A.K. (2022). Neural Architecture Search Survey: A Hardware Perspective. ACM Computing Surveys, 55(4), Article 78, 1-36. DOI: 10.1145/3524500.

**PDF:** [ACM DL (open HTML)](https://dl.acm.org/doi/full/10.1145/3524500)

**Verification note:** Bibliographic details confirmed via WebSearch (ACM DL, ResearchGate, DBLP). Full-text-adjacent verified — ACM DL provides an open full-HTML version.

**Linked concepts:** [[NAS]]

## Abstract summary

A survey specifically reviewing hardware-aware NAS: methods that automate the architectural design process of DNNs while explicitly accounting for target-hardware constraints (latency, energy, memory) rather than optimizing accuracy alone.

## Research problem

Standard NAS (as surveyed in [[2019_Elsken_NASSurvey]]) optimizes purely for validation accuracy, but deploying discovered architectures on real hardware — especially resource-constrained edge/embedded hardware — requires the search itself to account for hardware cost, a distinct and rapidly growing subfield with its own taxonomy needs.

## Key idea

Extend the standard NAS taxonomy with hardware-awareness as an explicit dimension: how hardware cost is estimated (proxy models, lookup tables, direct measurement) and how it is incorporated into the search objective (constraint vs. multi-objective).

## Technical contribution

A structured taxonomy specifically for hardware-aware NAS methods, covering hardware-cost estimation strategies and search-objective formulations, complementing but extending the general NAS taxonomy of [[2019_Elsken_NASSurvey]].

## Experimental methodology

Literature survey and synthesis of hardware-aware NAS methods through 2022, not a novel empirical study.

## Results

A widely-cited (169+) structured reference specifically for the hardware-aware NAS subfield, filling the hardware-cost gap that general NAS surveys like [[2019_Elsken_NASSurvey]] leave open.

## Comparison with the state of the art

Directly extends [[2019_Elsken_NASSurvey]]'s three-axis taxonomy with hardware-cost as an explicit consideration, and is the natural survey-level anchor for this KB's existing MCU-targeted hardware-aware NAS entry, [[2026_Garavagno_HWNASUltraLowPower]].

## Strengths

Recent (2022), open-access via ACM DL's full-HTML version, and specifically scoped to the hardware-aware subfield most relevant to this KB's EdgeAI focus.

## Weaknesses

As a survey, offers no new empirical results; published 2022, so it predates the most recent (2023-2026) zero-shot and proxy-based hardware-aware NAS methods.

## Limitations

Survey currency bounded by publication date; taxonomy is necessarily broader than any single hardware target class (covers everything from data-center accelerators to microcontrollers).

## Open questions

Where does this KB's own [[2026_Garavagno_HWNASUltraLowPower]] (bounding RAM/Flash/MAC directly in the NAS objective) fall within this survey's hardware-cost-estimation and search-objective taxonomy — direct measurement, constraint-based formulation, or something the survey's 2022-era taxonomy does not yet anticipate?

## Possible extensions

Positioning this KB's existing hardware-aware NAS entries explicitly on this survey's taxonomy, and identifying which hardware-cost-estimation strategies (proxy vs. direct measurement) are least represented for microcontroller-class targets specifically.

## Relevance to our research

The dedicated survey-level anchor for hardware-aware NAS, directly relevant to and complementing this KB's existing MCU-targeted NAS content — a clear gap this audit closes.

## Possible thesis topics

A systematic evaluation of hardware-cost-estimation strategies (proxy models vs. direct on-device measurement) specifically for Cortex-M-class NAS search spaces.

## Possible collaborations

Groups working on hardware-aware NAS methodology (Iowa State University).

## Links to related papers

[[2019_Elsken_NASSurvey]], [[2017_Zoph_NeuralArchitectureSearchRL]], [[2026_Garavagno_HWNASUltraLowPower]]
