# A Real-Time Mechanical Fault Diagnosis Approach Based on Lightweight Architecture Search Considering Industrial Edge Deployments

**Full citation:** Ma, S., Sun, H., Gao, S., Zhou, G. (2023). A real-time mechanical fault diagnosis approach based on lightweight architecture search considering industrial edge deployments. *Engineering Applications of Artificial Intelligence*, 123, 106433. DOI: 10.1016/j.engappai.2023.106433

**PDF:** [DOI](https://doi.org/10.1016/j.engappai.2023.106433) · [ScienceDirect](https://www.sciencedirect.com/science/article/abs/pii/S0952197623006176)

**Verification note:** ScienceDirect returns a client-rendered, non-fetchable abstract page; bibliographic details and technical summary confirmed via WebSearch. This record is abstract-level verified, not full-text-verified.

**Linked concepts:** [[Predictive_Maintenance]], [[NAS]], [[Industrial_IoT]]

## Abstract summary

Proposes a mechanical fault-diagnosis strategy built on multi-objective automatic architecture search, combining a variable-layer search space, an efficient search-space design, and a real-time search strategy to construct a lightweight diagnostic network that jointly optimizes for edge-deployment feasibility, real-time inference speed, and diagnostic accuracy, explicitly considering compound faults and strong noise conditions typical of rotating industrial machinery.

## Research problem

Neural architecture search for fault diagnosis typically optimizes for accuracy alone, or treats edge deployability as a post-hoc constraint applied after search, rather than as a first-class search objective, resulting in architectures that perform well in benchmarks but are not necessarily well-suited to real-time inference under the noise and compound-fault conditions typical of industrial edge deployment.

## Key idea

Formulate lightweight architecture search for fault diagnosis as a multi-objective problem from the outset, jointly searching over a variable-layer search space for architectures that satisfy real-time inference-speed constraints and edge-deployment feasibility simultaneously with diagnostic accuracy, rather than optimizing accuracy first and compressing afterward.

## Technical contribution

A multi-objective NAS framework specifically targeting real-time mechanical fault diagnosis under industrial edge constraints, incorporating a variable-layer search space, an efficient search-space design intended to keep search cost tractable, and explicit handling of compound faults and strong noise as part of the evaluation criteria rather than as an afterthought.

## Experimental methodology

Multi-objective architecture search over the proposed variable-layer search space, evaluated for real-time inference speed and diagnostic accuracy under noisy and compound-fault rotating-machinery conditions; compared against baseline fault-diagnosis architectures for accuracy/speed/robustness trade-offs (per the abstract; specific bearing/rotating-machinery dataset and quantitative accuracy figures not captured in this record beyond the general framing).

## Results

The searched lightweight architectures achieved a favorable trade-off between real-time inference speed, edge-deployment feasibility, and diagnostic accuracy under compound-fault and high-noise conditions, outperforming architectures not explicitly co-optimized for these industrial-edge constraints (per the published abstract).

## Comparison with the state of the art

Distinguishes itself from post-hoc compression approaches (prune/quantize a large accurate model afterward) and from single-objective NAS (search for accuracy, then check if it fits the edge budget) by making real-time and edge-deployment constraints first-class search objectives; complements the transfer-learning-based domain-generalization approach of [[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]], which instead assumes a fixed lightweight architecture and focuses on adapting it across domains.

## Strengths

Explicitly incorporates compound faults and strong noise, conditions closer to real industrial environments than clean single-fault benchmarks, into both the search objective and evaluation; multi-objective framing (accuracy + speed + deployability) is more representative of actual industrial edge-deployment requirements than accuracy-only NAS.

## Weaknesses

As an abstract-level record (ScienceDirect full text not fetchable), this summary lacks the specific search-space size, search-cost/compute-budget figures, and the exact rotating-machinery dataset(s) and fault taxonomy used for evaluation.

## Limitations

NAS search cost, even with an "efficient" search space, is typically higher than either post-hoc compression or the transfer-learning approach of [[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]]; unclear from the abstract how the search cost compares, or whether the searched architecture needs to be re-searched for meaningfully different machine types.

## Open questions

How does the search cost (compute-time, energy) of this multi-objective NAS approach compare to the retraining cost of the transfer-learning approach in [[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]] for adapting to a new machine or fault type? Does the searched architecture family generalize across different rotating-machinery types, or is search-space design specific to the evaluated equipment?

## Possible extensions

A direct empirical comparison of NAS-based lightweight architecture search (this paper) versus transfer-learning-based domain adaptation of a fixed architecture ([[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]]) on the same fault-diagnosis benchmark, measuring total cost (search/retraining time and energy) versus accuracy for both new-domain and new-machine-type scenarios.

## Relevance to our research

Anchors the [[NAS]] concept node's connection into [[Predictive_Maintenance]] and [[Industrial_IoT]], demonstrating multi-objective, deployment-aware architecture search as a distinct strategy from the transfer-learning approach represented by [[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]] within the same application area.

## Possible thesis topics

Benchmarking multi-objective NAS against transfer-learning-based domain adaptation for industrial fault diagnosis under a unified cost model (search/retraining compute + energy + accuracy), to give practitioners a concrete decision framework for which strategy to use when deploying across heterogeneous industrial equipment.

## Possible collaborations

Groups working on NAS for resource-constrained/edge deployment and industrial fault-diagnosis / predictive-maintenance research applying deep learning to rotating machinery.

## Links to related papers

[[2022_Asutkar_TinyMLTransferLearningFaultDiagnosis]]
