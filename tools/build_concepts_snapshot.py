#!/usr/bin/env python3
"""
Build the "EdgeAI Observatory" Ask page
(https://claude.ai/code/artifact/c054e12a-e683-4b5e-b233-a4317e7b1545) from
its tracked template, 00_Config/ask_page.template.html, by embedding a static
JSON snapshot of every 01_Knowledge_Base/**/*.md concept (id, title, category,
url, Overview and Evolution excerpts) together with the corpus counts.

Why the snapshot exists: the page's live features (`db` queries, `sample` AI
answers) are runtime capabilities available only to signed-in members of the
Observatory's Claude workspace. Any other visitor gets neither, so the page's
knowledge-base browsing and its extractive "what does the KB say" fallback
read from this embedded snapshot instead; live data still takes priority
whenever `db` is available. The counts in the snapshot's `stats` block are the
page's fallback for the header numbers, so nothing is hardcoded in the page.

Usage:
    python3 tools/build_concepts_snapshot.py                 # writes ./ask_page.html (gitignored)
    python3 tools/build_concepts_snapshot.py --json           # prints the snapshot JSON only
    python3 tools/build_concepts_snapshot.py --out path.html  # custom output path

Then publish the output with the Artifact tool to the Ask page's URL. Run it
(with tools/build_book.py) after every pass that changes 01_Knowledge_Base/;
Weekly and Monthly runs never need it.
"""
import glob
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "01_Knowledge_Base")
TEMPLATE = os.path.join(ROOT, "00_Config", "ask_page.template.html")
PLACEHOLDER = "__STATIC_SNAPSHOT__"
SITE = "https://riccardoberta.github.io/edgeai-observatory/"
EXCERPT_CHARS = 900


def build_concepts():
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
            sections = {"Overview": first_split[0].strip()}
            for chunk in first_split[1:]:
                nl = chunk.find("\n")
                name = chunk[:nl].strip() if nl != -1 else chunk.strip()
                sections[name] = chunk[nl + 1:].strip() if nl != -1 else ""
            out.append({
                "id": os.path.splitext(fn)[0],
                "data": {
                    "title": title,
                    "category": os.path.basename(dirpath).replace("_", " "),
                    "url": SITE + os.path.splitext(rel)[0].replace(os.sep, "/") + "/",
                    "sections": {
                        "Overview": sections.get("Overview", "")[:EXCERPT_CHARS],
                        "Evolution of the concept": sections.get("Evolution of the concept", "")[:EXCERPT_CHARS],
                    },
                },
            })
    return sorted(out, key=lambda c: c["id"].lower())


def build_stats(n_concepts):
    papers = glob.glob(os.path.join(ROOT, "02_Papers", "*", "*.md"))
    digests = glob.glob(os.path.join(ROOT, "03_Digests", "*", "*.md"))
    weekly = sorted(glob.glob(os.path.join(ROOT, "03_Digests", "Weekly", "*_weekly_digest.md")))
    as_of = os.path.basename(weekly[-1])[:10] if weekly else None
    return {"papers": len(papers), "concepts": n_concepts, "digests": len(digests), "asOf": as_of}


def main():
    args = sys.argv[1:]
    concepts = build_concepts()
    snapshot = {"concepts": concepts, "stats": build_stats(len(concepts))}
    payload = json.dumps(snapshot, ensure_ascii=False).replace("</", "<\\/")
    if "--json" in args:
        sys.stdout.write(payload)
        return
    out_path = args[args.index("--out") + 1] if "--out" in args else os.path.join(ROOT, "ask_page.html")
    template = open(TEMPLATE, encoding="utf-8").read()
    if PLACEHOLDER not in template:
        sys.exit(f"ERROR: {TEMPLATE} has no {PLACEHOLDER} marker")
    page = template.replace(PLACEHOLDER, payload)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {out_path} ({len(page.encode('utf-8'))} bytes) — {len(concepts)} concepts, "
          f"stats {snapshot['stats']}")


if __name__ == "__main__":
    main()
