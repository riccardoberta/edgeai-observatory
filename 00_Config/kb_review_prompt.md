# KB Review Prompt (periodic, on-demand)

Use this prompt whenever you want a research-analyst pass over the Knowledge Base, not tied to the weekly/monthly digest cycle.

## How to run it

Just paste the prompt below into chat. Run it whenever you feel the KB might be stale, after a burst of reading, or before a thesis-topic conversation — there's no fixed cadence, this is meant to be triggered manually.

## The prompt

```
Act as an expert EdgeAI researcher and review the Knowledge Base (01_Knowledge_Base/) end to end:

1. For each concept file, check whether the "Evolution of the concept," "Open problems," "Research ideas," and "Possible thesis topics" sections still reflect the current state of the field. Update entries that are outdated, vague, or now superseded, and add new concept files if a genuinely distinct, stable research area has emerged that doesn't fit the existing taxonomy.
2. Check whether there are important foundational or highly-cited papers relevant to any concept that are not yet cited in its "Key papers" section, and add them where genuinely warranted (quality over quantity — don't pad).
3. For every paper you newly cite in the KB, create its full deep-analysis record under 02_Papers/ (following the existing template) and link it from the KB via [[paper_id]] — never leave an inline citation without a corresponding record.
4. Do not hallucinate citations, dates, or results — every claim must be traceable to a real, verifiable source.
5. At the end, give me a short summary of what changed: which concepts were updated, which new papers/records were added, and any new concept files created.
```

## How to tweak it

- To narrow scope (e.g. only Hardware, or only one concept), add a line like "Limit this review to the Hardware category" or "Focus only on Quantization and NAS."
- To bias toward recent literature instead of foundational gaps, replace step 2 with: "Check whether any major paper from the last 12 months is missing from each concept's Key papers."
- To make it more conservative (fewer additions, just a health check), add: "Only flag candidate additions for my approval — do not write any new files yet."
- To also touch the taxonomy itself, add: "Also reconsider 00_Taxonomy/ — flag if any category needs restructuring."
```
