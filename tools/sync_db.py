#!/usr/bin/env python3
"""
Generate the documents that mirror the Observatory's source files into the
live database behind the "EdgeAI Observatory" Ask page
(https://claude.ai/code/artifact/c054e12a-e683-4b5e-b233-a4317e7b1545).

The database is the Ask page's only view of the corpus, so every document
must be a faithful, FULL-TEXT mirror of its source file — never a summary
or an abridged rewrite. This script is the single place that defines the
mapping file -> document; the Weekly / Monthly / Consolidation tasks and any
manual editorial pass should run it and write its output with the Artifact
database tool (`write_db` / ArtifactData, op "set", batched), rather than
composing documents by hand.

Output (default directory: db_sync/, gitignored):
    db_sync/concepts/<id>.json     one per 01_Knowledge_Base/**/*.md
    db_sync/papers/<id>.json       one per 02_Papers/**/*.md
    db_sync/digests/<id>.json      one per 03_Digests/**/*.md
    db_sync/meta/stats.json        counts + asOf, read live by the page header
    db_sync/bundle.json            all of the above in one file (for transfer)
    db_sync/manifest.json          {collection/doc_id: sha1 of the document}

Use --only-changed with a previous manifest to emit just the documents whose
content differs (`python3 tools/sync_db.py --only-changed old_manifest.json`).

Document schemas (must stay in sync with the page code):
    concepts: {category, path, sections{Overview + each ## heading}, title, url}
    papers:   {citation, pdf_url, concepts[], path, sections{each ## heading}, title, url, year}
    digests:  {content (full markdown), path, subtype weekly|monthly|consolidation, title, url}
    meta/stats: {papers, concepts, digests, branches, asOf, updatedAt, note}
`url` is the page on the public site: https://riccardoberta.github.io/edgeai-observatory/<path-without-.md>/
"""
import glob
import hashlib
import json
import os
import re
import sys
from datetime import datetime, timezone

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SITE = "https://riccardoberta.github.io/edgeai-observatory/"
WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def split_sections(body):
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    sections = {}
    intro = parts[0].strip()
    for i in range(1, len(parts), 2):
        sections[parts[i].strip()] = parts[i + 1].strip() if i + 1 < len(parts) else ""
    return intro, sections


def site_url(rel):
    return SITE + os.path.splitext(rel)[0].replace(os.sep, "/") + "/"


def kb_ids():
    return {os.path.splitext(os.path.basename(p))[0] for p in glob.glob(os.path.join(ROOT, "01_Knowledge_Base", "*", "*.md"))}


def concept_docs():
    docs = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "01_Knowledge_Base", "*", "*.md"))):
        rel = os.path.relpath(p, ROOT)
        text = read(p)
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        intro, sections = split_sections(text.split("\n", 1)[1] if "\n" in text else "")
        sections = {"Overview": intro, **sections}
        docs[os.path.splitext(os.path.basename(p))[0]] = {
            "category": os.path.basename(os.path.dirname(p)).replace("_", " "),
            "path": rel, "sections": sections, "title": title, "url": site_url(rel),
        }
    return docs


def paper_docs():
    kb = kb_ids()
    docs = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "02_Papers", "*", "*.md"))):
        rel = os.path.relpath(p, ROOT)
        text = read(p)
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        header, sections = split_sections(text.split("\n", 1)[1] if "\n" in text else "")
        cit = re.search(r"\*\*Full citation:\*\*\s*(.+)", header)
        pdf = re.search(r"\*\*PDF(?:/HTML)?:\*\*\s*\[.*?\]\((https?[^\)]+)\)", header)
        linked = re.search(r"\*\*Linked concepts:\*\*\s*(.+)", header)
        concepts = []
        for m in WIKILINK_RE.finditer(linked.group(1) if linked else header):
            cid = m.group(1).strip().replace(" ", "_")
            if cid in kb and cid not in concepts:
                concepts.append(cid)
        docs[os.path.splitext(os.path.basename(p))[0]] = {
            "citation": cit.group(1).strip() if cit else "",
            "pdf_url": pdf.group(1) if pdf else "",
            "concepts": concepts, "path": rel, "sections": sections, "title": title,
            "url": site_url(rel), "year": rel.split(os.sep)[1],
        }
    return docs


def digest_docs():
    docs = {}
    for p in sorted(glob.glob(os.path.join(ROOT, "03_Digests", "*", "*.md"))):
        rel = os.path.relpath(p, ROOT)
        text = read(p)
        title = text.split("\n", 1)[0].lstrip("# ").strip()
        subtype = {"Weekly": "weekly", "Monthly": "monthly", "Consolidation": "consolidation"}[rel.split(os.sep)[1]]
        docs[os.path.splitext(os.path.basename(p))[0]] = {
            "content": text, "path": rel, "subtype": subtype, "title": title, "url": site_url(rel),
        }
    return docs


def stats(concepts, papers, digests):
    tax = read(os.path.join(ROOT, "00_Taxonomy", "taxonomy.md"))
    branches = [b for b in re.findall(r"^## (.+)$", tax, flags=re.M) if b not in ("Field notes", "Known gaps")]
    as_of = max(d["path"][len("03_Digests/"):].split("/")[1][:10] for d in digests.values()
                if d["subtype"] == "weekly")
    return {
        "papers": len(papers), "concepts": len(concepts), "digests": len(digests), "branches": len(branches),
        "asOf": as_of,
        "updatedAt": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
        "note": "asOf = date of the most recent weekly digest. Counts are taken from the papers/concepts/digests "
                "collections; regenerate with tools/sync_db.py whenever those collections change.",
    }


def sha(doc):
    return hashlib.sha1(json.dumps(doc, sort_keys=True, ensure_ascii=False).encode("utf-8")).hexdigest()


def main():
    args = sys.argv[1:]
    out_dir = os.path.join(ROOT, "db_sync")
    old_manifest = {}
    if "--only-changed" in args:
        old_manifest = json.load(open(args[args.index("--only-changed") + 1], encoding="utf-8"))
    if "--out" in args:
        out_dir = args[args.index("--out") + 1]

    concepts, papers, digests = concept_docs(), paper_docs(), digest_docs()
    bundle = {"concepts": concepts, "papers": papers, "digests": digests, "meta": {"stats": stats(concepts, papers, digests)}}
    manifest = {f"{coll}/{doc_id}": sha(doc) for coll, docs in bundle.items() for doc_id, doc in docs.items() if coll != "meta"}

    written = 0
    for coll, docs in bundle.items():
        os.makedirs(os.path.join(out_dir, coll), exist_ok=True)
        for doc_id, doc in docs.items():
            key = f"{coll}/{doc_id}"
            if coll != "meta" and old_manifest and old_manifest.get(key) == manifest[key]:
                continue
            with open(os.path.join(out_dir, coll, doc_id + ".json"), "w", encoding="utf-8") as f:
                json.dump(doc, f, ensure_ascii=False, indent=1)
            written += 1
    with open(os.path.join(out_dir, "bundle.json"), "w", encoding="utf-8") as f:
        json.dump(bundle, f, ensure_ascii=False)
    with open(os.path.join(out_dir, "manifest.json"), "w", encoding="utf-8") as f:
        json.dump(manifest, f, indent=1, sort_keys=True)
    print(f"{len(concepts)} concepts, {len(papers)} papers, {len(digests)} digests -> {written} documents written to {out_dir}/ "
          f"(asOf {bundle['meta']['stats']['asOf']})")


if __name__ == "__main__":
    main()
