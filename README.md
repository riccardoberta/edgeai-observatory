# EdgeAI Observatory

This is not a paper archive. It is the lab's long-term research memory on EdgeAI: it organizes knowledge around **concepts**, not documents, and supports research, teaching, thesis supervision, and scientific writing.

## Structure

`00_Taxonomy/` holds the map of the field's concepts (algorithms, frameworks, hardware, applications). It's a living document: it gets refined continuously as new sub-areas or connections emerge.

`00_Config/sources.yaml` is the configuration file listing every monitored source (digital libraries, conferences, software projects, hardware vendors, benchmarks, datasets). Edit it directly to add, remove, or pause a source — monitoring cycles read from this file instead of a hardcoded list.

`01_Knowledge_Base/` is the heart of the system. Each file represents a concept (e.g. Quantization, Pruning, NAS) and collects: how the idea evolved, which papers define or advance it, which problems remain open, which research or thesis directions it suggests. Papers are not the center: they are references that feed the concepts.

`02_Papers/` contains the deep-analysis records of individual selected papers, with all the required fields (problem, contribution, methodology, validation, strengths and weaknesses, reproducibility, code, datasets, impact). Each record links to the corresponding concepts in `01_Knowledge_Base/`.

`03_Digests/` contains the weekly digests and monthly reports, archived over time so the evolution of the field can be reconstructed.

## Principles

Every claim must be traceable to its original source. No hallucinated information. Quality over quantity: a few well-curated concepts are worth more than a long list of disconnected papers. Over time, the goal is to answer questions like "which groups lead a given area," "which algorithms are becoming obsolete," "which topics are good thesis material" — not just "what does this paper say."
