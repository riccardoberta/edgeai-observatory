# Rapid Deployment of DNNs for Edge Computing via Structured Pruning at Initialization

**Full citation:** Eccles, B.J., Wong, L., Varghese, B. (2024). Rapid Deployment of DNNs for Edge Computing via Structured Pruning at Initialization. 2024 IEEE/ACM 24th International Symposium on Cluster, Cloud and Internet Computing (CCGrid).

**PDF:** [IEEE Xplore](https://ieeexplore.ieee.org/iel8/10701311/10701314/10701394.pdf) · [arXiv preprint](https://arxiv.org/abs/2404.16877)

**Verification note:** Bibliographic details confirmed via WebSearch (University of St Andrews research portal, IEEE Xplore listing). Abstract-level verified; full IEEE-formatted text not fetched directly.

**Linked concepts:** [[Pruning]]

## Abstract summary

Introduces Reconvene, a system for rapidly generating structurally pruned DNNs suited to edge deployment using Pruning-at-Initialization (PaI) with structured (not unstructured) pruning. Reconvene creates pruned models within seconds that are up to 16.21x smaller and 2x faster than an unstructured-PaI counterpart while maintaining comparable accuracy, directly targeting the practical need for fast, repeatable model generation across many edge-deployment targets.

## Research problem

Existing pruning approaches trade off poorly for edge deployment: unstructured pruning removes individual weights but yields limited real runtime speedup on generic hardware (as this Observatory's own [[Pruning]] concept already notes), structured pruning can better translate to real speedups but is typically applied after training (train-prune-retrain) which is slow, and neural architecture search is accurate but computationally expensive — leaving a gap for a method that is both structured (hardware-realizable) and fast enough for rapid, repeated edge-model generation.

## Key idea

Apply Pruning-at-Initialization — deciding which structures to prune before training rather than after — using structured (channel/filter-level) criteria instead of unstructured single-weight criteria, so the resulting pruned network is both hardware-realizable and generated in seconds rather than requiring a full train-prune-retrain cycle.

## Technical contribution

Reconvene, a system implementing structured Pruning-at-Initialization for rapid, repeatable edge-DNN generation, reporting up to 16.21x model-size reduction and 2x speedup over an unstructured-PaI baseline at comparable accuracy, generated within seconds per model.

## Experimental methodology

Structured-PaI pruned models generated via Reconvene and compared against an unstructured-PaI baseline across model size, real-hardware-realizable inference speedup, and accuracy, with generation time measured to demonstrate the "rapid" claim (per the CCGrid paper; specific model/dataset/hardware combinations not independently re-derived in this abstract-level record).

## Results

Reconvene-generated structured-PaI models were up to 16.21x smaller and 2x faster than the unstructured-PaI counterpart while maintaining comparable accuracy, with pruned models generated within seconds — directly addressing both the speedup-realizability gap of unstructured pruning and the speed gap of post-training structured pruning or NAS.

## Comparison with the state of the art

Distinguishes itself from post-training structured pruning (train-prune-retrain, as in [[2016_Han_DeepCompression]]'s pruning stage) by pruning at initialization instead, and from unstructured Pruning-at-Initialization approaches by using structured criteria that translate into real hardware speedups — directly addressing this Observatory's own [[Pruning]] open problem about obtaining structured pruning with real (not just theoretical) speedups.

## Strengths

Directly targets the "real speedup on commodity hardware" open problem already flagged in this Observatory's [[Pruning]] concept; rapid (seconds-scale) generation makes it practical for exploring many edge-deployment configurations, unlike NAS-scale search costs; IEEE/ACM-published, peer-reviewed venue.

## Weaknesses

Abstract-level record; specific benchmark models, datasets, and target edge hardware are not detailed here beyond the headline size/speed figures.

## Limitations

As a Pruning-at-Initialization method, it forgoes the potential accuracy advantages of post-training pruning approaches that can use trained-weight information to guide pruning decisions; comparison is against an unstructured-PaI baseline rather than against post-training structured pruning or NAS-based approaches.

## Open questions

How does structured-PaI (Reconvene) compare in final accuracy and real speedup against post-training structured pruning and NAS-guided pruning, not just against unstructured PaI? Does the "seconds-scale generation" advantage hold at the same magnitude on microcontroller-class (Cortex-M) targets, or only on the edge-server/mobile-class hardware likely evaluated?

## Possible extensions

A three-way comparison of structured-PaI (Reconvene), post-training structured pruning, and NAS-guided pruning under a fixed edge-deployment time-and-accuracy budget, extending this Observatory's [[Pruning]] open problem about automating per-layer compression ratios.

## Relevance to our research

Directly closes this Observatory's own flagged [[Pruning]] gap — "obtaining structured pruning that gives real speedups on commodity hardware" — with a peer-reviewed, IEEE/ACM-published method achieving that goal at rapid (seconds-scale) generation cost.

## Possible thesis topics

Benchmarking Reconvene-style structured-PaI pruning against CMSIS-NN-optimized post-training structured pruning on Cortex-M hardware, to test whether the reported size/speed gains hold at the microcontroller tier.

## Possible collaborations

Systems/edge-computing research groups working on rapid DNN deployment tooling (University of St Andrews Systems Research Group, per the paper's institutional affiliation).

## Links to related papers

[[2016_Han_DeepCompression]]
