# TinyML Reference Datasets

## Evolution of the concept

Created 2026-09-02 alongside [[MLPerf_Tiny]], formalizing the Benchmarks & Datasets taxonomy branch. Groups the standard, widely-reused reference datasets that underpin reproducible comparison across this Observatory's Applications concepts — datasets are monitored sources in `00_Config/sources.yaml` in their own right, but previously had no Knowledge Base concept distinct from the Application concept (e.g. [[Keyword_Spotting]]) that happens to use them. [[2018_Warden_SpeechCommands]] is the anchor: a public, crowd-sourced dataset that became the de facto standard for keyword-spotting research and is also one of MLPerf Tiny's four representative tasks, directly connecting this concept to [[MLPerf_Tiny]]. Visual Wake Words (Chowdhery et al., 2019, arXiv:1906.05721) is the other actively-monitored dataset in `00_Config/sources.yaml` and MLPerf Tiny's other vision-side representative task. A 2026-09-03 exhaustive Scholar audit closed this concept's own previously self-flagged gap by giving it a full deep-analysis record: a binary person-presence-detection dataset derived from COCO, sized specifically to represent realistic always-on microcontroller vision (85-90% accuracy achievable within a 250 KB memory footprint using contemporary mobile architectures). The same audit added the concept's first dedicated survey-level anchor: Quadar, Chehri, and Debaque's "TinyML Datasets as Enablers of 6G Edge Intelligence: Key Insights and Research Gaps" (IEEE Wireless Communications, 2026) treats TinyML datasets as a first-class research object, arguing dataset scarcity/quality is a genuine constraint on TinyML's role in emerging 6G-scale distributed edge intelligence and identifying specific coverage gaps.

## Key papers

[[2018_Warden_SpeechCommands]] — public, crowd-sourced dataset and collection methodology for reproducible keyword-spotting benchmarks; the de facto standard dataset for [[Keyword_Spotting]] and one of [[MLPerf_Tiny]]'s four representative tasks.

[[2019_Chowdhery_VisualWakeWordsDataset]] — binary person-presence-detection dataset, [[MLPerf_Tiny]]'s vision-side representative task; 85-90% accuracy achievable within a 250 KB memory footprint using contemporary mobile architectures.

[[2026_Quadar_TinyMLDatasets6GEdgeIntelligence]] — first dedicated survey of the TinyML dataset landscape as its own topic, identifying coverage gaps relevant to emerging 6G-scale edge intelligence deployments.

## Open problems

Are there more recent successor/extension datasets in the vision-wake-word space worth tracking alongside Visual Wake Words, per the gaps the 2026 Quadar et al. survey identifies? Do Speech Commands and Visual Wake Words remain representative of current edge-AI deployment workloads as the field's center of gravity shifts toward LLM/MoE serving (per [[Mixture-of-Experts (MoE) & Edge LLM Serving]]), or is the field due for a next-generation reference dataset closer to that workload profile?

## Research ideas

A survey of whether Speech Commands- and Visual-Wake-Words-trained models' reported accuracy gains have saturated — i.e., whether these benchmarks are becoming solved/saturated tasks (echoing the taxonomy's general "detect saturated topics" design principle).

## Possible thesis topics

Assessing whether Speech Commands and Visual Wake Words remain discriminative benchmarks for current architectures, or have saturated to the point of needing a harder successor (Master's; bridges this concept and [[Keyword_Spotting]] / [[Vision]]).

## Links

[[Keyword_Spotting]], [[Vision]], [[MLPerf_Tiny]]
