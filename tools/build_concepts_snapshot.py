#!/usr/bin/env python3
"""
Generate a static JSON snapshot of every 01_Knowledge_Base/**/*.md concept
(id, title, category, url, and the Overview/Evolution excerpts), for embedding
directly into the "EdgeAI Observatory" Ask-tool artifact
(https://claude.ai/code/artifact/c054e12a-e683-4b5e-b233-a4317e7b1545).

Why this exists: the Ask-tool page's live features (`db` query, `sample`
AI answers) are runtime capabilities granted by the claude.ai viewer shell,
and — as of 2026-09-16 — appear to be scoped to signed-in members of the
Observatory's own Claude workspace. A genuinely external viewer (outside
that workspace) gets `null` for both capabilities no matter which link is
used to open the page, so the page's knowledge-base browsing and its
extractive "what does the KB say" fallback must not depend on `db` at all.
This script produces the fallback's data source: embed its JSON output
into the page as `<script id="staticConceptsData" type="application/json">`,
and have the page's `loadConcepts()` fall back to it whenever `db` is
unavailable or empty (live `db` data, when available, still takes priority
so registered viewers see the current KB, not a stale snapshot).

Usage:
    python3 tools/build_concepts_snapshot.py > concepts_snapshot.json
    # then splice the output into ask_page.html in place of the
    # <script id="staticConceptsData" type="application/json">...</script>
    # block's content, and republish the artifact.

Regenerate this snapshot (and republish the Ask-tool page) whenever
01_Knowledge_Base/ changes materially — in practice, that means after each
Knowledge Base Consolidation cycle, the same trigger tools/build_book.py
uses for the companion book.
"""
import os
import re
import json
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "01_Knowledge_Base")

EXCERPT_CHARS = 900


def build_snapshot():
    out = []
    for dirpath, _, filenames in os.walk(KB):
        for fn in sorted(filenames):
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            rel = os.path.relpath(full, ROOT)
            text = open(full, encoding="utf-8").read()
            lines = text.split("\n")
            title = lines[0].lstrip("# ").strip()
            body = "\n".join(lines[1:])
            first_split = re.split(r"^## ", body, flags=re.M)
            intro = first_split[0].strip()
            sections = {"Overview": intro}
            for i in range(1, len(first_split)):
                chunk = first_split[i]
                nl = chunk.find("\n")
                name = chunk[:nl].strip() if nl != -1 else chunk.strip()
                sec_body = chunk[nl + 1:].strip() if nl != -1 else ""
                sections[name] = sec_body
            category = os.path.basename(dirpath).replace("_", " ")
            stem = os.path.splitext(fn)[0]
            path_no_ext = os.path.splitext(rel)[0]
            out.append({
                "id": stem,
                "data": {
                    "title": title,
                    "category": category,
                    "url": "https://riccardoberta.github.io/edgeai-observatory/" + path_no_ext + "/",
                    "sections": {
                        "Overview": sections.get("Overview", "")[:EXCERPT_CHARS],
                        "Evolution of the concept": sections.get("Evolution of the concept", "")[:EXCERPT_CHARS],
                    },
                },
            })
    return out


if __name__ == "__main__":
    snapshot = build_snapshot()
    json.dump(snapshot, sys.stdout, ensure_ascii=False)
    sys.stderr.write(f"Wrote {len(snapshot)} concepts to stdout\n")
