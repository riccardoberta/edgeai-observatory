# What is the State of Neural Network Pruning?

**Full citation:** Blalock, D., Gonzalez Ortiz, J.J., Frankle, J., Guttag, J. (2020). What is the State of Neural Network Pruning? Proceedings of Machine Learning and Systems (MLSys 2020).

**PDF:** [MLSys proceedings](https://proceedings.mlsys.org/paper_files/paper/2020/hash/6c44dc73014d66ba49b28d483a8f8b0d-Abstract.html)

**Verification note:** Bibliographic details confirmed via WebSearch (DBLP, MLSys proceedings). Abstract-level verified. MLSys is one of this Observatory's explicitly tracked conferences (00_Config/sources.yaml).

**Linked concepts:** [[Pruning]]

## Abstract summary

A critical meta-analysis of the pruning literature: after surveying 81 pruning papers, the authors find the field lacks standardized benchmarks, comparable evaluation metrics, and consistent baselines, making it nearly impossible to determine which pruning methods actually outperform others; they introduce ShrinkBench, an open-source framework for standardized pruning evaluation, and re-evaluate several methods under it.

## Research problem

Despite decades of pruning research and hundreds of published methods, no standardized way existed to compare them — papers use different baselines, different accuracy-vs-compression operating points, and inconsistent metrics, making claimed improvements largely incomparable across papers.

## Key idea

Systematically audit the pruning literature's evaluation practices, quantify the resulting incomparability, and provide a standardized open-source benchmarking framework (ShrinkBench) to fix it going forward.

## Technical contribution

ShrinkBench, an open-source framework standardizing pruning evaluation (consistent baselines, consistent metrics, consistent accuracy-compression operating points), plus a re-evaluation of several established pruning methods under it that surfaces cases where the field's received wisdom does not hold up.

## Experimental methodology

Surveyed 81 pruning papers for evaluation-methodology inconsistencies, then re-implemented and re-evaluated several representative pruning methods under the standardized ShrinkBench framework to enable direct, fair comparison.

## Results

Finds that many pruning papers cannot be fairly compared to each other due to inconsistent evaluation practices, and that under standardized evaluation, some methods' claimed superiority does not hold up; ShrinkBench is released to remedy this going forward.

## Comparison with the state of the art

A meta-level critique directly relevant to every empirical pruning result this KB tracks ([[2015_Han_LearningWeightsConnections]], [[2016_Han_DeepCompression]], [[2024_Eccles_StructuredPruningInitializationEdge]]) — a methodological check on how much weight to place on any single paper's reported numbers without knowing its evaluation protocol.

## Strengths

Extremely influential (1900+ citations) as a rare critical/meta-analysis paper in a field usually dominated by proposing new methods; published at MLSys, a venue this Observatory explicitly tracks; the ShrinkBench framework remains a usable, concrete tool.

## Weaknesses

As a critique-and-tooling paper, it proposes no new pruning method of its own; its findings are about evaluation methodology, not about which specific technique is best.

## Limitations

ShrinkBench standardizes evaluation but does not itself resolve the field's disagreement about which pruning criterion (magnitude, saliency, structured vs. unstructured) is fundamentally superior — it only makes existing methods more fairly comparable.

## Open questions

Has the field's evaluation-methodology problem improved since 2020, or do more recent pruning papers this KB tracks (like [[2024_Eccles_StructuredPruningInitializationEdge]]) still suffer from the same baseline/metric inconsistencies this paper identified?

## Possible extensions

Auditing this KB's own Pruning key papers against ShrinkBench's standardized evaluation criteria, to assess whether their reported comparisons (e.g. against unstructured PaI baselines) meet this paper's fairness bar.

## Relevance to our research

A crucial methodological caution for how this KB should read and compare any pruning paper's reported numbers — directly relevant to the Observatory's own stated principle of scientific rigor and no hallucinated claims.

## Possible thesis topics

Re-evaluating a subset of this KB's own Pruning key papers under the ShrinkBench framework to verify whether their claimed improvements hold up under standardized comparison.

## Possible collaborations

Groups working on ML evaluation methodology and reproducibility (MIT).

## Links to related papers

[[2015_Han_LearningWeightsConnections]], [[2016_Han_DeepCompression]], [[2024_Eccles_StructuredPruningInitializationEdge]]
