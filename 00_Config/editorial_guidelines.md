# Editorial Guidelines

These rules apply to everything that ships as Observatory content: `00_Taxonomy/taxonomy.md`, every page in `01_Knowledge_Base/`, every record in `02_Papers/`, every file in `03_Digests/`, `README.md`, and the two published pages (Ask the Observatory, the Textbook). The Weekly, Monthly and Knowledge Base Consolidation tasks, the KB review prompt, and any manual editorial pass must follow them. `tools/check_consistency.py` enforces the mechanical parts.

## Language and attribution

All content is written in English, whatever language the editorial conversation happens in.

The Observatory belongs to [EliosLab](https://www.elios.unige.it/), University of Genoa. Observatory-voice prose never names an individual as the owner or curator of the project ("X should re-verify this", "X's own paper"): write "this should be re-verified", "co-authored within EliosLab (DITEN, University of Genoa)". Real author names in a `**Full citation:**` line, in a digest's `**Authors:**` line, or in a "Possible collaborations" field are bibliographic facts and are fine.

## No process narration

Content describes the field, not the Observatory's own activity. Do not write "this cycle found", "created on 2026-09-04", "as flagged in the 2026-09-13 digest", "the consolidation queue has been watching", "sources checked this week", "the first paper we've tracked", or similar. A digest's date and a consolidation report's date are part of the file name and title; nothing else in the text should refer to the Observatory's schedule, tasks, queue, or earlier digests as evidence. The only acceptable trace of process is a `[[wikilink]]` to a `02_Papers/` record, which is how a claim stays grounded in a source.

Exception: `02_Papers/` records may carry a `**Verification note:**` line stating how the bibliographic data was verified and whether the abstract or the full text was read — that is provenance, not narration. `00_Config/*.yaml` files are internal bookkeeping and may reference digests and dates freely.

## Traceability

Every claim about a paper must be traceable to a `02_Papers/` record, linked with `[[record_id]]`. In Knowledge Base "Evolution of the concept" prose, link the first mention of each paper inline (`[[2017_Jacob_QuantizationIntegerOnlyInference|Jacob et al. (2017)]]`); do not rely on the Key papers list alone. Never cite a paper inline without a record; never create a record without a `**PDF:**` link (arXiv PDF preferred, else DOI, else the best official page — never fabricated; say explicitly when none can be found).

Reciprocity: every `02_Papers/` record lists its concepts in `**Linked concepts:**`, and every concept it lists names the record in its "Key papers" section. A record no concept links to is an error (orphan).

## Concept pages (`01_Knowledge_Base/`)

Open with one or two plain-language paragraphs defining the concept and any acronym or jargon, written for someone meeting the term for the first time; then the fixed sections `## Evolution of the concept`, `## Variants` (optional), `## Key papers`, `## Open problems`, `## Research ideas`, `## Possible thesis topics`, `## Links`. Key papers entries are one paragraph each: `[[record_id]] — what the paper contributes to this concept.`

Every concept page must be named as a bullet in `00_Taxonomy/taxonomy.md`, and every taxonomy bullet must have a page. A new concept requires two independently-authored anchor papers; until then the topic stays in the taxonomy's "Known gaps" list, which must describe the same open signals as `00_Config/consolidation_candidates.yaml` (same set, same count).

## Paper records (`02_Papers/`)

Follow `00_Config/paper_record_template.md` exactly: file name `YYYY_FirstAuthor_ShortTitle.md` in the `YYYY/` folder, the header fields `**Full citation:**`, `**PDF:**`, optional `**Verification note:**`, `**Linked concepts:**`, then the seventeen `##` sections in the template's order.

## Digests (`03_Digests/`)

Weekly digest: title `# Weekly Digest — YYYY-MM-DD` (the run date), an opening paragraph that states the period covered (for example "Covers papers first listed between 14 and 20 September 2026") and the concepts touched, then one numbered `## N. Title` section per paper with exactly these fields: `**Source:**`, `**Authors:**`, `**Link:**` (or `**DOI:**`), `**Why it matters:**`, `**Technical summary:**`, `**Novelty assessment:**`, `**Relevance score:**`, and a closing `## Suggested thesis / research hooks`. Monthly report: `# Monthly Report — Month YYYY` with the sections emerging trends, open questions, new research directions, influential research groups, software releases, benchmarks, datasets, research and thesis opportunities. Consolidation report: `# Knowledge Base Consolidation — YYYY-MM-DD` recording, for each candidate reviewed, the decision and the rationale, plus any cross-concept questions the review surfaced.

Relevance score rubric (weekly digests), 1–5:

| Score | Meaning |
|---|---|
| 5 | Directly advances a core concept with real-hardware or measured-silicon validation, standard benchmark or open artifacts, and a clear thesis or research hook |
| 4 | Solid quantified result on real hardware or a standard benchmark, relevant to at least one concept, minor gaps in validation or openness |
| 3 | Relevant and credible but simulation-only, incremental, or on a hardware tier outside the Observatory's core (laptop/workstation GPU) |
| 2 | Tangential: relevant framing but weak validation, or mainly useful as a survey/entry point |
| 1 | Recorded for completeness only (for example a signal for a known gap) |

Novelty assessment uses the words High, Moderate-to-high, Moderate, Low, each followed by one sentence saying what is new relative to prior work named in the Knowledge Base.

## Authority of each layer

Weekly and Monthly runs write only `03_Digests/` and `00_Config/consolidation_candidates.yaml` (and update `last_checked` in `00_Config/sources.yaml`). The Knowledge Base Consolidation task and explicit manual editorial passes are the only ways `01_Knowledge_Base/`, `00_Taxonomy/taxonomy.md` and `02_Papers/` change; each such pass records every concept created, merged or rejected in `00_Config/consolidation_history.yaml` (a manual pass uses `outcome: promoted` / `merged` / `rejected` with `via: manual editorial pass`), then regenerates the database mirror (`tools/sync_db.py`), the Textbook (`tools/build_book.py`) and the Ask page's static snapshot (`tools/build_concepts_snapshot.py`).
