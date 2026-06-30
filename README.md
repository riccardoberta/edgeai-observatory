# EdgeAI Observatory

A long-term research memory and scientific intelligence layer for the EdgeAI literature. It is not a literature-review tool: a review summarizes papers, while the Observatory is built to identify patterns, connect ideas across papers, track how the field evolves, and help generate new research directions.

It organizes knowledge around **concepts** rather than documents — the concept graph, not the paper list, is what the Observatory grows and queries over time. Papers feed the concepts: each one is processed into structured knowledge and routed into the ideas it advances, the open problems it touches, and the research directions it opens.

Beyond tracking what individual papers say, the Observatory surfaces patterns across the field: which research directions are emerging, which problems remain unsolved, which ideas contradict each other, which topics are becoming saturated, and which represent good thesis opportunities. It supports research, teaching, thesis supervision, and scientific writing, with the goal of becoming, over one or two years, a genuine, evolving scientific memory for anyone working on EdgeAI.

## Structure

`00_Taxonomy/` holds the map of the field's concepts (algorithms, frameworks, hardware, applications). It's a living document: it gets refined continuously as new sub-areas or connections emerge.

`00_Config/sources.yaml` is the configuration file listing every monitored source (digital libraries, conferences, software projects, hardware vendors, benchmarks, datasets). Edit it directly to add, remove, or pause a source — monitoring cycles read from this file instead of a hardcoded list.

`01_Knowledge_Base/` is the heart of the system. Each file represents a concept (e.g. Quantization, Pruning, NAS) and collects: how the idea evolved, which papers define or advance it, which problems remain open, which research or thesis directions it suggests.

`02_Papers/` contains the deep-analysis records of individual selected papers, grouped into per-year subfolders, with all the required fields (problem, contribution, methodology, validation, strengths and weaknesses, reproducibility, code, datasets, impact). Each record links to the corresponding concepts in `01_Knowledge_Base/`.

`03_Digests/` contains the weekly digests (`Weekly/`) and monthly reports (`Monthly/`), archived over time so the evolution of the field can be reconstructed.

## Static site

The Observatory is also published as a browsable static site (MkDocs Material), auto-deployed to GitHub Pages on every push to `main` via `.github/workflows/docs.yml`. The `[[wikilink]]` syntax used throughout the source files stays untouched — `tools/build_docs.py` renders it into plain relative links into a generated `docs/` folder right before `mkdocs build` runs (both locally and in CI); neither `docs/` nor `site/` are committed.

To preview locally:

```
pip install -r requirements-docs.txt
python3 tools/build_docs.py
mkdocs serve
```

## Principles

Every claim must be traceable to its original source. No hallucinated information. Quality over quantity: a few well-curated concepts are worth more than a long list of disconnected papers. Over time, the goal is to answer questions like "which groups lead a given area," "which algorithms are becoming obsolete," "which topics are good thesis material" — not just "what does this paper say."
