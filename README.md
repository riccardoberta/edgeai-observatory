# EdgeAI Observatory

[riccardoberta.github.io/edgeai-observatory](https://riccardoberta.github.io/edgeai-observatory/)

A long-term research memory and scientific intelligence layer for the EdgeAI literature. It is not a literature-review tool: a review summarizes papers, while the Observatory is built to identify patterns, connect ideas across papers, track how the field evolves, and help generate new research directions.

It organizes knowledge around **concepts** rather than documents — the concept graph, not the paper list, is what the Observatory grows and queries over time. Papers feed the concepts: each one is processed into structured knowledge and routed into the ideas it advances, the open problems it touches, and the research directions it opens.

Beyond tracking what individual papers say, the Observatory surfaces patterns across the field: which research directions are emerging, which problems remain unsolved, which ideas contradict each other, which topics are becoming saturated, and which represent good thesis opportunities. It supports research, teaching, thesis supervision, and scientific writing, with the goal of becoming, over one or two years, a genuine, evolving scientific memory for anyone working on EdgeAI.

## Structure

`00_Taxonomy/` holds the map of the field's concepts (algorithms, frameworks, hardware, applications). It's a living document: it gets refined continuously as new sub-areas or connections emerge.

`00_Config/sources.yaml` is the configuration file listing every monitored source (digital libraries, conferences, software projects, hardware vendors, benchmarks, datasets). Edit it directly to add, remove, or pause a source — monitoring cycles read from this file instead of a hardcoded list. `00_Config/consolidation_candidates.yaml` and `00_Config/consolidation_history.yaml` track the evidence-accumulation layer described below.

`01_Knowledge_Base/` is the heart of the system. Each file represents a concept (e.g. Quantization, Pruning, NAS) and collects: how the idea evolved, which papers define or advance it, which problems remain open, which research or thesis directions it suggests.

`02_Papers/` contains the deep-analysis records of individual selected papers, grouped into per-year subfolders, with all the required fields (problem, contribution, methodology, validation, strengths and weaknesses, reproducibility, code, datasets, impact). Each record links to the corresponding concepts in `01_Knowledge_Base/`.

`03_Digests/` contains the weekly digests (`Weekly/`), monthly reports (`Monthly/`), and Knowledge Base Consolidation reports (`Consolidation/`), archived over time so the evolution of the field — and of the Observatory's own editorial decisions — can be reconstructed.

## Monitoring pipeline

The Observatory runs three layers, each with a different, deliberately narrow authority. Weekly and Monthly *accumulate evidence*; only the Consolidation layer *promotes* it into the persistent Knowledge Base — that separation is the architectural point, not a detail:

```
literature / ecosystem signals
            |
            v
         WEEKLY
   discovery + filtering
            |
            +------> active candidate queue (00_Config/consolidation_candidates.yaml)
            |                |
            v                |
         MONTHLY ------------+
      trend synthesis
            |
            v
     ready_for_review
            |
    explicit Ricky request
            |
            v
      CONSOLIDATION
      /     |       \
   merge  promote   reject/watch
     |       |
     v       v
     KNOWLEDGE BASE (01_Knowledge_Base/)
```

**Weekly** (`edgeai-observatory-weekly-digest`, scheduled) monitors arXiv and optionally IEEE Xplore/ACM/Scholar, ranks new papers, and writes `03_Digests/Weekly/`. It may also append evidence to `00_Config/consolidation_candidates.yaml`, open a new `watching` candidate for a genuinely reusable signal, or mark a candidate `ready_for_review` — conservatively, not for every paper.

**Monthly** (`edgeai-observatory-monthly-report`, scheduled) reads a month of weeklies plus ecosystem sources and writes `03_Digests/Monthly/`, adding a layer of synthesis the weeklies can't see individually. It has the same candidate-queue permissions as Weekly, plus merging duplicate/synonymous candidates and — occasionally — creating a candidate visible only through cross-week synthesis.

**Knowledge Base Consolidation** (`edgeai-observatory-knowledge-base-consolidation`, on-demand only — never scheduled) is the only layer allowed to touch `01_Knowledge_Base/`. Run it explicitly whenever you want accumulated monitoring evidence turned into curated persistent knowledge. It reviews `ready_for_review` candidates (and recent digests, as a backstop), decides for each one whether to merge it into an existing concept, promote it as a new concept, keep watching, or reject it, verifies claims against primary sources before writing anything, and closes each decision into `00_Config/consolidation_history.yaml` with a dated rationale. Every cycle is logged in `03_Digests/Consolidation/YYYY-MM-DD_kb_consolidation.md` — a durable record of not just *what* changed in the Knowledge Base, but *why*, and what was deliberately left as an open signal instead.

In short: monitoring and synthesis (Weekly, Monthly) are about *noticing* — they can accumulate and organize evidence, but never decide on their own that something belongs in the Knowledge Base. Promotion is a separate, explicit, human-triggered editorial act, reserved for the Consolidation layer.

## Static site

The Observatory is also published as a browsable static site (MkDocs Material), auto-deployed to GitHub Pages on every push to `main` via `.github/workflows/docs.yml`. The Obsidian-style wikilink syntax used throughout the source files stays untouched — `tools/build_docs.py` renders it into plain relative links into a generated `docs/` folder right before `mkdocs build` runs (both locally and in CI); neither `docs/` nor `site/` are committed.

To preview locally:

```
pip install -r requirements-docs.txt
python3 tools/build_docs.py
mkdocs serve
```

## PDF export

To create a polished offline PDF containing the full Observatory corpus
(taxonomy, knowledge base, paper records, weekly digests, and monthly
reports):

```
python -m pip install -r requirements-docs.txt
python tools/export_pdf.py
```

The default output is `output/pdf/edgeai-observatory-export.pdf`. Use
`python tools/export_pdf.py -o path/to/export.pdf` to choose another
location.

## Principles

Every claim must be traceable to its original source. No hallucinated information. Quality over quantity: a few well-curated concepts are worth more than a long list of disconnected papers. Over time, the goal is to answer questions like "which groups lead a given area," "which algorithms are becoming obsolete," "which topics are good thesis material" — not just "what does this paper say."
