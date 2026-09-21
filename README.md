# EdgeAI Observatory

A research project of [EliosLab](https://www.elios.unige.it/), University of Genoa.

[Browse the site](https://riccardoberta.github.io/edgeai-observatory/) · [Ask the Observatory](https://riccardoberta.github.io/edgeai-observatory/ask/) · [Read the Textbook](https://riccardoberta.github.io/edgeai-observatory/book/)

A long-term research knowledge system for the EdgeAI / TinyML literature, built to behave like a research analyst for the lab rather than a folder of PDFs. It is not a literature-review tool: a review summarizes papers, while the Observatory is built to identify patterns, connect ideas across papers, track how the field evolves, and help generate new research directions.

It organizes knowledge around **concepts** rather than documents — the concept graph, not the paper list, is what the Observatory grows and queries over time. Papers feed the concepts: each one is processed into structured knowledge and routed into the ideas it advances, the open problems it touches, and the research directions it opens.

Beyond tracking what individual papers say, the Observatory surfaces patterns across the field: which research directions are emerging, which problems remain unsolved, which ideas contradict each other, which topics are becoming saturated, and which represent good thesis opportunities. It supports research, teaching, thesis supervision, and scientific writing, with the goal of becoming, over one or two years, a genuine, evolving scientific memory for anyone working on EdgeAI.

## Interact with the Observatory

There are three ways to use the Observatory, all reading from the same corpus:

**[Browse the site](https://riccardoberta.github.io/edgeai-observatory/)** — the full taxonomy, knowledge base, paper records, and digests as a searchable static site, rebuilt on every push to `main`.

**[Ask the Observatory](https://riccardoberta.github.io/edgeai-observatory/ask/)** — a Claude-powered page for natural-language questions ("what's emerging in on-device learning for Cortex-M?", "which papers contradict each other on X?"). It retrieves the concept pages, paper records and digests most relevant to the question from a live database that mirrors this repository (`tools/sync_db.py` regenerates that mirror, full text, whenever the source files change), answers only from that retrieved context, and lists the concept pages and paper records it drew on, each linked to the corresponding page on the site above. Anyone with the link can open the page and browse the knowledge base; the live AI answers use Claude capabilities that are available only to signed-in members of the Observatory's Claude workspace — other visitors get the matching concept excerpts without AI editing, plus links to the book and the repository.

**[Read the Textbook](https://riccardoberta.github.io/edgeai-observatory/book/)** — "Edge AI: Principles and Practice," a Master's/PhD-level reference volume generated from the Knowledge Base, organized as chapters mirroring the taxonomy (Algorithms, Frameworks, Hardware, Applications, Benchmarks & Datasets, Security). It is generated, never hand-edited: `tools/build_book.py` renders the taxonomy and every concept page verbatim into one HTML page, resolving wikilinks to in-book chapters or to the papers' PDF links, so the text is always traceable to source. Its cover states the date of the last change to the Knowledge Base it was built from; it is rebuilt and republished as the final step of every pass that changes the Knowledge Base (see below).

## Structure

`00_Taxonomy/taxonomy.md` holds the map of the field's concepts in six branches (Algorithms, Frameworks, Hardware, Applications, Benchmarks & Datasets, Security), plus durable field notes and the list of known gaps — topics under observation that do not yet have a concept page. It's a living document: it gets refined continuously as new sub-areas or connections emerge, and every bullet in it corresponds to exactly one page in `01_Knowledge_Base/`.

`00_Config/` holds the configuration and the editorial rules. `sources.yaml` lists every monitored source (digital libraries, conferences, software projects, hardware vendors, benchmarks, datasets); edit it directly to add, remove, or pause a source — monitoring cycles read from this file instead of a hardcoded list. `consolidation_candidates.yaml` and `consolidation_history.yaml` track the evidence-accumulation layer described below. `editorial_guidelines.md` is the writing standard every file must follow (English, EliosLab attribution, no process narration, traceability and reciprocity rules, digest fields and relevance rubric), `paper_record_template.md` is the template for `02_Papers/` records, and `kb_review_prompt.md` is the prompt for an on-demand research-analyst review of the Knowledge Base.

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
    explicit consolidation request
            |
            v
      CONSOLIDATION
      /     |       \
   merge  promote   reject/watch
     |       |
     v       v
     KNOWLEDGE BASE (01_Knowledge_Base/)
```

**Weekly** (`edgeai-observatory-weekly-digest`, scheduled) monitors every active source in `00_Config/sources.yaml` — arXiv listings, IEEE Xplore, ACM DL, MDPI, ScienceDirect and SpringerLink through `site:`-filtered web search, and a bounded set of Google Scholar keyword searches — ranks new papers, records which sources contributed (`last_checked`), and writes `03_Digests/Weekly/`. It may also append evidence to `00_Config/consolidation_candidates.yaml`, open a new `watching` candidate for a genuinely reusable signal, or mark a candidate `ready_for_review` — conservatively, not for every paper.

**Monthly** (`edgeai-observatory-monthly-report`, scheduled) reads a month of weeklies plus ecosystem sources and writes `03_Digests/Monthly/`, adding a layer of synthesis the weeklies can't see individually. It has the same candidate-queue permissions as Weekly, plus merging duplicate/synonymous candidates and — occasionally — creating a candidate visible only through cross-week synthesis.

**Knowledge Base Consolidation** (`edgeai-observatory-knowledge-base-consolidation`, on-demand only — never scheduled) is the only layer allowed to touch `01_Knowledge_Base/`. Run it explicitly whenever you want accumulated monitoring evidence turned into curated persistent knowledge. It reviews `ready_for_review` candidates (and recent digests, as a backstop), decides for each one whether to merge it into an existing concept, promote it as a new concept, keep watching, or reject it, verifies claims against primary sources before writing anything, and closes each decision into `00_Config/consolidation_history.yaml` with a dated rationale. Every cycle is logged in `03_Digests/Consolidation/YYYY-MM-DD_kb_consolidation.md` — a durable record of not just *what* changed in the Knowledge Base, but *why*, and what was deliberately left as an open signal instead.

**Manual editorial passes** are the one other way the Knowledge Base changes: an explicit, human-run review such as `00_Config/kb_review_prompt.md`, a coverage audit against Google Scholar, or a targeted correction. They carry the same authority and the same duties as a Consolidation cycle — every concept created, merged or rejected is recorded in `00_Config/consolidation_history.yaml` (marked `via: manual editorial pass`), the taxonomy's known gaps stay in step with the candidate queue, and the derived surfaces below are regenerated.

In short: monitoring and synthesis (Weekly, Monthly) are about *noticing* — they can accumulate and organize evidence, but never decide on their own that something belongs in the Knowledge Base. Promotion is a separate, explicit, human-triggered editorial act, reserved for the Consolidation layer and for manual editorial passes.

**Derived surfaces.** Three things are generated from the source files and must be regenerated whenever those files change. The live database behind [Ask the Observatory](https://riccardoberta.github.io/edgeai-observatory/ask/) mirrors every concept page, paper record and digest in full text plus a `meta/stats` document with the counts shown in the page header: `tools/sync_db.py` produces the documents, and the layer that changed the files writes them with the Artifact database tool (Weekly and Monthly runs do this for the digests and stats they add; Consolidation and manual passes do it for everything they touch). The [Textbook](https://riccardoberta.github.io/edgeai-observatory/book/) is rebuilt with `tools/build_book.py` and republished. The Ask page carries an embedded static snapshot of the concept pages (its fallback for visitors without live database access), regenerated with `tools/build_concepts_snapshot.py` and republished. The last two only depend on `01_Knowledge_Base/` and `00_Taxonomy/`, so only Consolidation cycles and manual editorial passes need to run them; Weekly and Monthly runs never rebuild or republish either page.

## Static site

The Observatory is also published as a browsable static site (MkDocs Material), auto-deployed to GitHub Pages on every push to `main` via `.github/workflows/docs.yml`. The Obsidian-style wikilink syntax used throughout the source files stays untouched — `tools/build_docs.py` renders it into plain relative links into a generated `docs/` folder right before `mkdocs build` runs (both locally and in CI); neither `docs/` nor `site/` are committed.

The deploy workflow first runs `tools/check_consistency.py`, which fails the build on any unresolved wikilink, paper record missing a required field, orphan paper record (one no concept page links to), or mismatch between the taxonomy and the Knowledge Base, and warns about stale `sources.yaml` entries or process narration; run it locally before committing.

To preview locally:

```
pip install -r requirements-docs.txt
python3 tools/check_consistency.py
python3 tools/build_docs.py --strict
mkdocs serve
```

## Tools

| Script | What it does | When to run it |
|---|---|---|
| `tools/check_consistency.py` | Repository-wide consistency checks (links, record fields, orphans, taxonomy parity, style warnings) | Before every commit; runs in CI |
| `tools/build_docs.py` | Renders the source tree into `docs/` with wikilinks resolved for MkDocs | Before `mkdocs build`/`serve`; runs in CI |
| `tools/sync_db.py` | Generates the full-text documents mirroring the repository into the Ask page's database (`db_sync/`) | After any change to concepts, papers or digests |
| `tools/build_book.py` | Generates the Textbook HTML from the taxonomy and the concept pages | After any change to `01_Knowledge_Base/` or `00_Taxonomy/` |
| `tools/build_concepts_snapshot.py` | Builds the Ask page HTML from `00_Config/ask_page.template.html` plus a fresh snapshot of the concept pages and corpus counts | After any change to `01_Knowledge_Base/` |
| `tools/export_pdf.py` | Builds an offline PDF of the whole corpus | On demand |

## PDF export

To create a polished offline PDF containing the full Observatory corpus
(taxonomy, knowledge base, paper records, and the weekly, monthly, and
consolidation digests):

```
python -m pip install -r requirements-docs.txt
python tools/export_pdf.py
```

The default output is `output/pdf/edgeai-observatory-export.pdf`. Use
`python tools/export_pdf.py -o path/to/export.pdf` to choose another
location.

## Principles

Every claim must be traceable to its original source. No hallucinated information. Quality over quantity: a few well-curated concepts are worth more than a long list of disconnected papers. Over time, the goal is to answer questions like "which groups lead a given area," "which algorithms are becoming obsolete," "which topics are good thesis material" — not just "what does this paper say."
