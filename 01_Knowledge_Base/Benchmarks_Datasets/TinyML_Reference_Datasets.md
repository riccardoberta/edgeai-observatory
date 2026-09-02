# TinyML Reference Datasets

## Evolution of the concept

Created 2026-09-02 alongside [[MLPerf_Tiny]], formalizing the Benchmarks & Datasets taxonomy branch. Groups the standard, widely-reused reference datasets that underpin reproducible comparison across this Observatory's Applications concepts — datasets are monitored sources in `00_Config/sources.yaml` in their own right, but previously had no Knowledge Base concept distinct from the Application concept (e.g. [[Keyword_Spotting]]) that happens to use them. [[2018_Warden_SpeechCommands]] is the anchor: a public, crowd-sourced dataset that became the de facto standard for keyword-spotting research and is also one of MLPerf Tiny's four representative tasks, directly connecting this concept to [[MLPerf_Tiny]]. Visual Wake Words (Chowdhery et al., 2019, arXiv:1906.05721) — the other actively-monitored dataset in `00_Config/sources.yaml` and MLPerf Tiny's other vision-side representative task — is tracked here by reference but does not yet have its own `02_Papers/` deep-analysis record; this is a known, explicitly flagged gap rather than an oversight.

## Key papers

[[2018_Warden_SpeechCommands]] — public, crowd-sourced dataset and collection methodology for reproducible keyword-spotting benchmarks; the de facto standard dataset for [[Keyword_Spotting]] and one of [[MLPerf_Tiny]]'s four representative tasks.

*Visual Wake Words* (Chowdhery et al., 2019, arXiv:1906.05721) — a binary person-presence-detection dataset, [[MLPerf_Tiny]]'s vision-side representative task and an actively-monitored source in `00_Config/sources.yaml`; not yet given a full `02_Papers/` deep-analysis record — a known gap, flagged rather than silently left uncited.

## Open problems

Visual Wake Words lacks a deep-analysis record despite being an actively-monitored, MLPerf-Tiny-representative dataset — should it be added, and are there more recent successor/extension datasets in the vision-wake-word space worth tracking alongside it? Do Speech Commands and Visual Wake Words remain representative of current edge-AI deployment workloads as the field's center of gravity shifts toward LLM/MoE serving (per [[Mixture-of-Experts (MoE) & Edge LLM Serving]]), or is the field due for a next-generation reference dataset closer to that workload profile?

## Research ideas

Creating the missing deep-analysis record for Visual Wake Words to close this concept's own flagged gap. A survey of whether Speech Commands- and Visual-Wake-Words-trained models' reported accuracy gains have saturated — i.e., whether these benchmarks are becoming solved/saturated tasks (echoing the taxonomy's general "detect saturated topics" design principle).

## Possible thesis topics

Assessing whether Speech Commands and Visual Wake Words remain discriminative benchmarks for current architectures, or have saturated to the point of needing a harder successor (Master's; bridges this concept and [[Keyword_Spotting]] / [[Vision]]).

## Links

[[Keyword_Spotting]], [[Vision]], [[MLPerf_Tiny]]
