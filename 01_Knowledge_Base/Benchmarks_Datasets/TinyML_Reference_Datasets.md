# TinyML Reference Datasets

This concept groups the standard, widely-reused reference datasets that underpin reproducible comparison across this Observatory's Applications concepts.

## Evolution of the concept

Warden's Speech Commands (2018) is the anchor dataset: a public, crowd-sourced collection of short spoken-word audio clips that became the de facto standard for keyword-spotting research (see [[Keyword_Spotting]]) and is also one of MLPerf Tiny's four representative tasks (see [[MLPerf_Tiny]]).

Chowdhery et al.'s Visual Wake Words (2019) is the field's other standard reference dataset: a binary "is a person present in this image" dataset derived from COCO, sized specifically to represent realistic always-on microcontroller vision — 85–90% accuracy is achievable within a 250 KB memory footprint using contemporary mobile architectures. It is MLPerf Tiny's vision-side representative task.

Quadar, Chehri, and Debaque (2026) treat TinyML datasets as a research object in their own right, arguing that dataset scarcity and quality are a genuine constraint on TinyML's role in emerging, large-scale distributed edge intelligence (looking ahead to 6G-era networks), and identify specific coverage gaps in the current dataset landscape.

## Key papers

[[2018_Warden_SpeechCommands]] — public, crowd-sourced dataset and collection methodology for reproducible keyword-spotting benchmarks; the de facto standard dataset for [[Keyword_Spotting]] and one of [[MLPerf_Tiny]]'s four representative tasks.

[[2019_Chowdhery_VisualWakeWordsDataset]] — binary person-presence-detection dataset, [[MLPerf_Tiny]]'s vision-side representative task; 85–90% accuracy achievable within a 250 KB memory footprint using contemporary mobile architectures.

[[2026_Quadar_TinyMLDatasets6GEdgeIntelligence]] — first dedicated survey of the TinyML dataset landscape as its own topic, identifying coverage gaps relevant to emerging large-scale edge-intelligence deployments.

## Open problems

Are there more recent successor or extension datasets in the vision-wake-word space worth tracking alongside Visual Wake Words? Do Speech Commands and Visual Wake Words remain representative of current edge-AI deployment workloads as the field's center of gravity shifts toward LLM/MoE serving (see [[MoE_Edge_LLM_Serving]]), or is the field due for a next-generation reference dataset closer to that workload profile?

## Research ideas

A survey of whether Speech-Commands- and Visual-Wake-Words-trained models' reported accuracy gains have saturated — that is, whether these benchmarks are becoming "solved" tasks that no longer discriminate well between methods.

## Possible thesis topics

Assessing whether Speech Commands and Visual Wake Words remain discriminative benchmarks for current architectures, or have saturated to the point of needing a harder successor (Master's; bridges this concept with [[Keyword_Spotting]] and [[Vision]]).

## Links

[[Keyword_Spotting]], [[Vision]], [[MLPerf_Tiny]]
