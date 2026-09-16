#!/usr/bin/env python3
"""
Build the single-file HTML for the "Edge AI: Principles and Practice" artifact
(https://claude.ai/code/artifact/205a5250-397c-4073-b9fe-a23e28b4aca9) directly
from the Observatory's source markdown: 00_Taxonomy/taxonomy.md and every
01_Knowledge_Base/**/*.md concept file, with [[wikilinks]] resolved to either
an in-book chapter anchor or an external PDF/publisher link (via the matching
02_Papers/**/*.md record's **PDF:** field).

Why generated rather than hand-edited: the book must always be traceable to
source (no hallucinated content) and the KB grows/changes independently of
the book, so re-running this script is the only way to keep the book in
sync. Per Ricky's 2026-09-16 rule, this script should only be run as the
final step of an EdgeAI Observatory Knowledge Base Consolidation cycle
(see tools/README or the consolidation task's own SKILL.md) -- NOT after
every Weekly/Monthly cycle, since only Consolidation is allowed to modify
01_Knowledge_Base/ and 00_Taxonomy/taxonomy.md, the two things this book is
built from.

Usage:
    python3 tools/build_book.py > /path/to/book_body.html
    # then publish that file with the Artifact tool to the book's URL.

The "knowledge current through" date shown on the book's cover is computed
automatically as the most recent git commit date touching 00_Taxonomy/ or
01_Knowledge_Base/ -- not today's date, and not the date of the latest
03_Digests/Consolidation/ report file (history shows KB edits have
sometimes landed outside a formal Consolidation cycle; this script reports
when the content genuinely last changed, not when a report was filed).
"""
import os, re, html, json, subprocess, sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
KB = os.path.join(ROOT, "01_Knowledge_Base")
PAPERS = os.path.join(ROOT, "02_Papers")
TAX = os.path.join(ROOT, "00_Taxonomy", "taxonomy.md")


def slugify(s):
    return re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


def git_last_touched_date():
    try:
        out = subprocess.check_output(
            ["git", "log", "-1", "--format=%ad", "--date=short", "--",
             "00_Taxonomy/taxonomy.md", "01_Knowledge_Base/"],
            cwd=ROOT, text=True,
        ).strip()
        return out or None
    except Exception:
        return None


def parse_taxonomy():
    tax_text = open(TAX, encoding="utf-8").read()
    branch_blocks = re.split(r"^## ", tax_text, flags=re.M)[1:]
    branches = []
    for block in branch_blocks:
        lines = block.split("\n")
        name = lines[0].strip()
        if name in ("Field notes", "Known gaps"):
            continue
        rest = "\n".join(lines[1:]).strip()
        parts = rest.split("\n- ", 1)
        intro = parts[0].strip()
        bullets = []
        if len(parts) > 1:
            bullet_text = "- " + parts[1]
            for m in re.finditer(r"^-\s+\*\*(.+?)\*\*\s+—", bullet_text, flags=re.M):
                bullets.append(m.group(1).strip())
        branches.append({"name": name, "intro": intro, "concepts": bullets})
    fn_m = re.search(r"^## Field notes\n(.*?)\n## Known gaps", tax_text, flags=re.S | re.M)
    field_notes = fn_m.group(1).strip() if fn_m else ""
    kg_m = re.search(r"^## Known gaps\n(.*)$", tax_text, flags=re.S | re.M)
    known_gaps = kg_m.group(1).strip() if kg_m else ""
    return branches, field_notes, known_gaps


def index_concepts():
    concept_files, concept_meta = {}, {}
    for dirpath, _, filenames in os.walk(KB):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            full = os.path.join(dirpath, fn)
            text = open(full, encoding="utf-8").read()
            title = text.split("\n", 1)[0].lstrip("# ").strip()
            stem = os.path.splitext(fn)[0]
            category = os.path.basename(dirpath).replace("_", " ")
            for key in (title, stem, stem.replace("-", " "), stem.replace("_", " ")):
                concept_files[key] = full
            concept_meta[full] = {"title": title, "category": category, "stem": stem}
    return concept_files, concept_meta


def index_papers():
    paper_index = {}
    for dirpath, _, filenames in os.walk(PAPERS):
        for fn in filenames:
            if not fn.endswith(".md"):
                continue
            pid = os.path.splitext(fn)[0]
            full = os.path.join(dirpath, fn)
            text = open(full, encoding="utf-8").read()
            title_m = re.match(r"#\s+(.+)", text)
            title = title_m.group(1).strip() if title_m else pid
            pdf_m = re.search(r"\*\*PDF:\*\*\s*\[.*?\]\((https?[^\)]+)\)", text)
            pdf = pdf_m.group(1) if pdf_m else None
            paper_index[pid] = {"title": title, "pdf": pdf}
    return paper_index


WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def build():
    branches, field_notes, known_gaps = parse_taxonomy()
    concept_files, concept_meta = index_concepts()
    paper_index = index_papers()
    concept_slug = {full: "ch-" + slugify(meta["stem"]) for full, meta in concept_meta.items()}

    def resolve_link(target, label):
        disp = html.escape(label)
        if target in concept_files:
            full = concept_files[target]
            return f'<a class="xlink" href="#{concept_slug[full]}">{disp}</a>'
        if target in paper_index:
            p = paper_index[target]
            text = html.escape(label if label != target else p["title"])
            if p["pdf"]:
                return f'<a class="plink" href="{html.escape(p["pdf"])}" target="_blank" rel="noopener">{text}</a>'
            return f'<span class="plink-nolink">{text}</span>'
        return disp

    def inline_md(text):
        text = html.escape(text)
        text = WIKILINK_RE.sub(
            lambda m: resolve_link(html.unescape(m.group(1)).strip(), html.unescape((m.group(2) or m.group(1)).strip())),
            text,
        )
        text = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", text)
        text = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", text)
        text = re.sub(r"`([^`]+?)`", r"<code>\1</code>", text)
        return text

    def paragraphs_html(block, cls="p"):
        paras = [p.strip() for p in re.split(r"\n\s*\n", block.strip()) if p.strip()]
        return "\n".join(f'<p class="{cls}">{inline_md(re.sub(chr(10)+"+", " ", p))}</p>' for p in paras)

    def key_papers_html(block):
        paras = [p.strip() for p in re.split(r"\n\s*\n", block.strip()) if p.strip()]
        items = "\n".join(f'<li>{inline_md(re.sub(chr(10)+"+", " ", p))}</li>' for p in paras)
        return f'<ul class="paper-list">\n{items}\n</ul>'

    SECTION_LABELS = {
        "Evolution of the concept": "Evolution of the concept", "Variants": "Variants",
        "Key papers": "Key papers", "Open problems": "Open problems",
        "Research ideas": "Research ideas", "Possible thesis topics": "Possible thesis topics",
        "Links": "Related concepts",
    }

    def parse_concept(full):
        text = open(full, encoding="utf-8").read()
        lines = text.split("\n")
        title = lines[0].lstrip("# ").strip()
        body = "\n".join(lines[1:])
        section_split = re.split(r"^## (.+)$", body, flags=re.M)
        intro = section_split[0].strip()
        sections = {}
        for i in range(1, len(section_split), 2):
            name = section_split[i].strip()
            sections[name] = section_split[i + 1].strip() if i + 1 < len(section_split) else ""
        return title, intro, sections

    chapter_html, toc_html, chapter_num = [], [], 0
    for b in branches:
        toc_html.append(f'<div class="toc-branch"><div class="toc-branch-name">{html.escape(b["name"])}</div><ul class="toc-list">')
        chapter_html.append(f'<section class="part" id="part-{slugify(b["name"])}">'
                             f'<div class="part-label">Part</div><h2 class="part-title">{html.escape(b["name"])}</h2>'
                             f'<p class="part-intro">{inline_md(b["intro"])}</p></section>')
        for cname in b["concepts"]:
            full = concept_files[cname]
            title, intro, sections = parse_concept(full)
            chapter_num += 1
            slug = concept_slug[full]
            toc_html.append(f'<li><a href="#{slug}"><span class="toc-num">{chapter_num:02d}</span> {html.escape(title)}</a></li>')
            parts = [f'<article class="chapter" id="{slug}">',
                     f'<div class="chapter-eyebrow">{html.escape(b["name"])} &middot; Chapter {chapter_num:02d}</div>',
                     f'<h3 class="chapter-title">{html.escape(title)}</h3>',
                     paragraphs_html(intro, cls="lede")]
            for key in ["Evolution of the concept", "Variants", "Key papers", "Open problems", "Research ideas", "Possible thesis topics", "Links"]:
                if key not in sections or not sections[key].strip():
                    continue
                parts.append(f'<h4 class="sec-h">{SECTION_LABELS[key]}</h4>')
                if key == "Key papers":
                    parts.append(key_papers_html(sections[key]))
                elif key == "Links":
                    parts.append(f'<p class="related">{inline_md(sections[key])}</p>')
                else:
                    parts.append(paragraphs_html(sections[key]))
            parts.append('</article>')
            chapter_html.append("\n".join(parts))
        toc_html.append('</ul></div>')

    def render_appendix_md(text):
        paras = [p.strip() for p in re.split(r"\n\s*\n", text.strip()) if p.strip()]
        out = []
        for p in paras:
            p = html.escape(p)
            p = re.sub(r"\*\*(.+?)\*\*", r"<strong>\1</strong>", p)
            p = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<em>\1</em>", p)
            p = re.sub(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]", lambda m: (m.group(2) or m.group(1)), p)
            p = re.sub(r"^- (.+)$", r"<li>\1</li>", p)
            out.append(p)
        html_out, in_list = [], False
        for p in out:
            is_li = p.startswith("<li>")
            if is_li and not in_list:
                html_out.append("<ul>"); in_list = True
            if not is_li and in_list:
                html_out.append("</ul>"); in_list = False
            html_out.append(p if is_li else f"<p>{p}</p>")
        if in_list:
            html_out.append("</ul>")
        return "\n".join(html_out)

    n_concepts, n_papers, n_branches = chapter_num, len(paper_index), len(branches)
    as_of = git_last_touched_date() or "unknown"

    return {
        "n_concepts": n_concepts, "n_papers": n_papers, "n_branches": n_branches, "as_of": as_of,
        "toc_html": "\n".join(toc_html),
        "chapters_html": "\n".join(chapter_html),
        "field_notes_html": render_appendix_md(field_notes),
        "known_gaps_html": render_appendix_md(known_gaps),
    }


def format_as_of(as_of):
    if as_of == "unknown":
        return "unknown"
    try:
        from datetime import datetime
        d = datetime.strptime(as_of, "%Y-%m-%d")
        return d.strftime("%-d %B %Y")
    except Exception:
        return as_of


PAGE_TEMPLATE = """<title>Edge AI: Principles and Practice</title>
<style>
:root {
  --bg: #f8f5ef;
  --surface: #ffffff;
  --surface-2: #f1ece1;
  --ink: #211d17;
  --ink-muted: #6f6656;
  --ink-faint: #a89d87;
  --accent: #2c5c53;
  --accent-ink: #ffffff;
  --accent-soft: #e4ece7;
  --rule: #ddd3bf;
  --link: #2c5c53;
  --shadow: 0 1px 2px rgba(33,29,23,0.06), 0 8px 24px -12px rgba(33,29,23,0.18);
  --radius: 3px;
}
@media (prefers-color-scheme: dark) {
  :root:not([data-theme="light"]) {
    --bg: #171c1a;
    --surface: #1e2422;
    --surface-2: #242b28;
    --ink: #eae5da;
    --ink-muted: #a7a091;
    --ink-faint: #6d6a5e;
    --accent: #7fc4b3;
    --accent-ink: #10201c;
    --accent-soft: #26332e;
    --rule: #333a36;
    --link: #8fd0bf;
    --shadow: 0 1px 2px rgba(0,0,0,0.3), 0 8px 24px -12px rgba(0,0,0,0.5);
  }
}
:root[data-theme="dark"] {
  --bg: #171c1a;
  --surface: #1e2422;
  --surface-2: #242b28;
  --ink: #eae5da;
  --ink-muted: #a7a091;
  --ink-faint: #6d6a5e;
  --accent: #7fc4b3;
  --accent-ink: #10201c;
  --accent-soft: #26332e;
  --rule: #333a36;
  --link: #8fd0bf;
  --shadow: 0 1px 2px rgba(0,0,0,0.3), 0 8px 24px -12px rgba(0,0,0,0.5);
}

* { box-sizing: border-box; }
body {
  background: var(--bg);
  color: var(--ink);
  font-family: "Source Serif 4", Georgia, "Times New Roman", serif;
  font-size: 16.5px;
  line-height: 1.65;
}
::selection { background: var(--accent-soft); }
a { color: var(--link); text-decoration-color: color-mix(in srgb, var(--link) 40%, transparent); text-underline-offset: 2px; }
a:hover { text-decoration-thickness: 2px; }
a:focus-visible, button:focus-visible { outline: 2px solid var(--accent); outline-offset: 2px; }

.eyebrow, .label, .chapter-eyebrow, .part-label, .toc-branch-name, .colophon-label {
  font-family: "IBM Plex Mono", ui-monospace, "SF Mono", Menlo, monospace;
  text-transform: uppercase;
  letter-spacing: 0.09em;
  font-size: 11.5px;
  color: var(--ink-muted);
}

h1, h2, h3, h4 { font-family: "Fraunces", Georgia, serif; font-weight: 600; text-wrap: balance; color: var(--ink); }

/* ---- Top bar ---- */
.topbar {
  position: sticky; top: 0; z-index: 40;
  display: flex; align-items: center; gap: 12px;
  padding: 10px 20px;
  background: color-mix(in srgb, var(--bg) 88%, transparent);
  backdrop-filter: blur(8px);
  border-bottom: 1px solid var(--rule);
}
.topbar-title { font-family: "Fraunces", serif; font-weight: 600; font-size: 15px; flex: 1; }
.topbar-stat { font-family: "IBM Plex Mono", monospace; font-size: 11px; color: var(--ink-muted); }
.toc-toggle {
  display: none;
  background: var(--surface-2); border: 1px solid var(--rule); border-radius: var(--radius);
  color: var(--ink); font-family: inherit; font-size: 13px; padding: 6px 10px; cursor: pointer;
}

/* ---- Shell layout ---- */
.shell { display: grid; grid-template-columns: 300px minmax(0,1fr); max-width: 1280px; margin: 0 auto; }
.sidebar {
  border-right: 1px solid var(--rule);
  padding: 28px 22px 60px;
  align-self: start;
  position: sticky; top: 49px;
  max-height: calc(100vh - 49px);
  overflow-y: auto;
}
.sidebar-cover { margin-bottom: 22px; padding-bottom: 18px; border-bottom: 1px solid var(--rule); }
.sidebar-cover .mark {
  width: 34px; height: 34px; border-radius: 8px; background: var(--accent); color: var(--accent-ink);
  display: flex; align-items: center; justify-content: center; font-family: "Fraunces", serif; font-weight: 700; font-size: 15px;
  margin-bottom: 10px;
}
.sidebar-cover h1 { font-size: 19px; line-height: 1.25; margin: 0 0 4px; }
.sidebar-cover .sub { font-family: "IBM Plex Mono", monospace; font-size: 10.5px; color: var(--ink-muted); letter-spacing: 0.04em; }

.toc-body { display: flex; flex-direction: column; gap: 20px; }
.toc-branch-name { margin-bottom: 6px; color: var(--accent); }
.toc-list { list-style: none; margin: 0; padding: 0; display: flex; flex-direction: column; }
.toc-list li a {
  display: flex; gap: 8px; align-items: baseline;
  padding: 4px 6px; margin: 0 -6px; border-radius: var(--radius);
  color: var(--ink); text-decoration: none; font-size: 13.5px; line-height: 1.4;
}
.toc-list li a:hover { background: var(--surface-2); }
.toc-list li a.active { background: var(--accent-soft); color: var(--accent); font-weight: 600; }
.toc-num { font-family: "IBM Plex Mono", monospace; font-size: 10.5px; color: var(--ink-faint); flex-shrink: 0; padding-top: 1px; }

main { min-width: 0; padding: 0 0 100px; }

/* ---- Cover / preface ---- */
.cover { padding: 64px 56px 40px; max-width: 780px; }
.cover .kicker { color: var(--accent); margin-bottom: 18px; }
.cover h1 { font-size: 44px; line-height: 1.08; margin: 0 0 20px; }
.cover .dek { font-size: 18px; color: var(--ink-muted); font-family: "Source Serif 4", serif; line-height: 1.5; margin: 0 0 28px; max-width: 62ch; }
.meta-grid { display: grid; grid-template-columns: repeat(auto-fit, minmax(150px,1fr)); gap: 18px 28px; padding-top: 24px; border-top: 1px solid var(--rule); }
.meta-grid dt { font-family: "IBM Plex Mono", monospace; font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.08em; color: var(--ink-faint); margin-bottom: 4px; }
.meta-grid dd { margin: 0; font-size: 14.5px; }

.stat-row { display: flex; gap: 28px; margin: 30px 0 6px; }
.stat-row .stat { }
.stat-row .stat b { font-family: "Fraunces", serif; font-size: 26px; display: block; color: var(--accent); font-variant-numeric: tabular-nums; }
.stat-row .stat span { font-family: "IBM Plex Mono", monospace; font-size: 10.5px; text-transform: uppercase; letter-spacing: 0.07em; color: var(--ink-muted); }

.asof-note { font-family: "IBM Plex Mono", monospace; font-size: 11.5px; color: var(--ink-muted); margin: 14px 0 0; }
.asof-note a { color: var(--ink-muted); }

.preface { padding: 8px 56px 40px; max-width: 780px; }
.preface h2 { font-size: 22px; margin: 34px 0 14px; }
.preface p { margin: 0 0 16px; max-width: 66ch; }
.preface p:first-of-type { margin-top: 0; }

/* ---- Parts & chapters ---- */
.part {
  padding: 46px 56px 18px; max-width: 780px;
  border-top: 1px solid var(--rule); margin-top: 12px;
}
.part:first-of-type { border-top: 1px solid var(--rule); }
.part-label { color: var(--accent); margin-bottom: 8px; }
.part-title { font-size: 30px; margin: 0 0 12px; }
.part-intro { color: var(--ink-muted); font-size: 15.5px; max-width: 68ch; margin: 0; }

.chapter { padding: 30px 56px 6px; max-width: 780px; scroll-margin-top: 62px; }
.chapter-eyebrow { margin-bottom: 8px; }
.chapter-title { font-size: 24px; margin: 0 0 14px; }
.chapter p, .chapter li { max-width: 68ch; }
.chapter p.lede { font-size: 16px; margin: 0 0 14px; }
.chapter p.p { margin: 0 0 14px; }
.sec-h {
  font-family: "IBM Plex Mono", monospace; font-weight: 600; text-transform: uppercase;
  letter-spacing: 0.07em; font-size: 12px; color: var(--accent);
  margin: 26px 0 10px; padding-top: 14px; border-top: 1px solid var(--rule);
}
.paper-list { list-style: none; margin: 0 0 14px; padding: 0; display: flex; flex-direction: column; gap: 10px; }
.paper-list li {
  padding-left: 16px; border-left: 2px solid var(--rule); font-size: 15px; line-height: 1.55;
}
.plink { font-weight: 600; text-decoration-line: none; border-bottom: 1px solid color-mix(in srgb, var(--link) 45%, transparent); }
.plink:hover { border-bottom-width: 2px; }
.plink-nolink { font-weight: 600; font-style: italic; }
p.related { font-size: 14.5px; color: var(--ink-muted); }
p.related a { color: var(--ink); font-weight: 600; }
code { font-family: "IBM Plex Mono", monospace; font-size: 0.9em; background: var(--surface-2); padding: 0.1em 0.35em; border-radius: 3px; }

/* ---- Appendix / colophon ---- */
.appendix { padding: 46px 56px; max-width: 780px; border-top: 1px solid var(--rule); margin-top: 12px; }
.appendix h2 { font-size: 22px; margin: 0 0 6px; }
.appendix .sub { color: var(--ink-muted); font-size: 14px; margin: 0 0 18px; }
.appendix h3 { font-size: 16px; margin: 30px 0 10px; }
.appendix p, .appendix li { max-width: 68ch; margin: 0 0 12px; }
.appendix ul { padding-left: 20px; }

.colophon { padding: 40px 56px 70px; max-width: 780px; border-top: 1px solid var(--rule); margin-top: 12px; }
.colophon p { margin: 0 0 8px; font-size: 13.5px; color: var(--ink-muted); font-family: "IBM Plex Mono", monospace; line-height: 1.7; }
.colophon a { color: var(--ink-muted); }

@media (max-width: 860px) {
  .shell { grid-template-columns: 1fr; }
  .toc-toggle { display: inline-block; }
  .sidebar {
    position: fixed; inset: 49px 0 0 0; z-index: 39; background: var(--bg);
    max-height: none; transform: translateX(-100%); transition: transform 0.2s ease;
  }
  .sidebar.open { transform: translateX(0); }
  .cover, .preface, .part, .chapter, .appendix, .colophon { padding-left: 24px; padding-right: 24px; }
  .cover h1 { font-size: 32px; }
}
@media (prefers-reduced-motion: reduce) { .sidebar { transition: none; } }
</style>

<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Fraunces:opsz,wght@9..144,500;9..144,600;9..144,700&family=Source+Serif+4:ital,wght@0,400;0,500;0,600;1,400&family=IBM+Plex+Mono:wght@400;500;600&display=swap">

<div class="topbar">
  <button class="toc-toggle" id="tocToggle" aria-label="Toggle contents">&#9776; Contents</button>
  <div class="topbar-title">Edge AI: Principles and Practice</div>
  <div class="topbar-stat">__N_CONCEPTS__ chapters &middot; knowledge current through __AS_OF_SHORT__</div>
</div>

<div class="shell">
  <aside class="sidebar" id="sidebar">
    <div class="sidebar-cover">
      <div class="mark">Oe</div>
      <h1>Edge AI: Principles and Practice</h1>
      <div class="sub">EDGEAI OBSERVATORY &middot; GRADUATE REFERENCE VOLUME</div>
    </div>
    <div class="toc-body">
      <div class="toc-branch"><div class="toc-branch-name">Front matter</div>
        <ul class="toc-list">
          <li><a href="#preface">Preface</a></li>
          <li><a href="#grounding">How this book is grounded</a></li>
        </ul>
      </div>
      __TOC__
      <div class="toc-branch"><div class="toc-branch-name">Back matter</div>
        <ul class="toc-list">
          <li><a href="#field-notes">Field notes</a></li>
          <li><a href="#known-gaps">Known gaps</a></li>
        </ul>
      </div>
    </div>
  </aside>

  <main>
    <section class="cover" id="top">
      <div class="eyebrow kicker">EdgeAI Observatory &mdash; Graduate Reference Volume</div>
      <h1>Edge AI: Principles and Practice</h1>
      <p class="dek">A thorough, citation-grounded account of how machine learning is made to run under the memory, power, and latency budgets of embedded and near-edge hardware &mdash; algorithms, compilers, silicon, and applications treated as one connected system rather than four separate literatures.</p>
      <dl class="meta-grid">
        <div><dt>Level</dt><dd>Master's / PhD</dd></div>
        <div><dt>Chapters</dt><dd>__N_CONCEPTS__, across __N_BRANCHES__ taxonomy branches</dd></div>
        <div><dt>Grounded in</dt><dd>the Observatory's knowledge base &amp; paper records</dd></div>
        <div><dt>Curated by</dt><dd><a href="https://www.elios.unige.it/" target="_blank" rel="noopener">EliosLab</a>, University of Genoa</dd></div>
      </dl>
      <div class="stat-row">
        <div class="stat"><b>__N_PAPERS__</b><span>papers cited</span></div>
        <div class="stat"><b>__N_CONCEPTS__</b><span>concepts</span></div>
        <div class="stat"><b>__N_BRANCHES__</b><span>branches</span></div>
      </div>
      <p class="asof-note">Knowledge current through __AS_OF_LONG__ &mdash; regenerated after each Knowledge Base Consolidation cycle. <a href="https://github.com/riccardoberta/edgeai-observatory/tree/main/03_Digests/Consolidation" target="_blank" rel="noopener">See consolidation history</a>.</p>
    </section>

    <section class="preface" id="preface">
      <h2>Preface</h2>
      <p>This book is generated from the EdgeAI Observatory's living knowledge base: a continuously maintained set of concept records, each tracking how one research direction in edge AI has evolved, which papers anchor it, and where the open problems and thesis-scale opportunities sit today. Rather than a fixed textbook that goes stale the day it is printed, this volume is a snapshot of that knowledge base, structured for continuous reading rather than lookup.</p>
      <p>The organization follows the Observatory's own taxonomy: six branches &mdash; Algorithms, Frameworks, Hardware, Applications, Benchmarks &amp; Datasets, and Security &mdash; each broken into the concepts that make it up. Algorithms and Frameworks concern how a model's computation is made cheaper and how that computation is compiled and executed; Hardware surveys the silicon it eventually runs on; Applications covers the end-user tasks edge AI is built to perform; Benchmarks &amp; Datasets and Security round out the picture with how the field measures itself and protects what it deploys. Read it start to finish as an introduction to the field, or use the sidebar to jump straight to the one concept a paper, a thesis proposal, or a review deadline requires.</p>
      <h2 id="grounding">How this book is grounded</h2>
      <p>Every paper this book cites is a real, individually verified record in the Observatory's <code>02_Papers/</code> archive &mdash; checked, where possible, against its primary arXiv or publisher page rather than taken on a secondary source's word; a handful of exceptions are flagged in their own chapter as abstract-level evidence pending full-text verification, exactly as the Observatory's own records flag them. Every paper title in this book links directly to its PDF or publisher page. Every chapter title corresponds to a live Knowledge Base concept page, which continues to accumulate evidence after this book's own text is written.</p>
      <p>Two conventions recur throughout. First, an <em>open problem</em> is a question a field has not yet answered &mdash; not a rhetorical one, but one a specific paper, or the absence of one, leaves genuinely open. Second, a <em>research idea</em> or <em>thesis topic</em> is not a suggestion invented for this book, but one formed while reading the underlying papers, of where a genuinely useful next contribution could come from: a Master's-scale topic is scoped to something one student can complete in a year; a PhD-scale topic is named where the underlying question is large enough to justify one.</p>
    </section>

    __CHAPTERS__

    <section class="appendix" id="field-notes">
      <h2>Field notes</h2>
      <p class="sub">Durable observations about how the field itself is moving &mdash; not a log of what changed in the knowledge base, but trends worth keeping in mind when reading this book or planning new research.</p>
      __FIELD_NOTES__
    </section>

    <section class="appendix" id="known-gaps">
      <h2>Known gaps</h2>
      <p class="sub">Candidate topics that have come up during monitoring but do not yet have a dedicated chapter, because they do not yet meet the Observatory's bar of at least two independently authored papers anchoring the topic.</p>
      __KNOWN_GAPS__
    </section>

    <footer class="colophon">
      <p class="colophon-label">Colophon</p>
      <p>Edge AI: Principles and Practice is generated, not hand-written: its text is assembled directly from the EdgeAI Observatory's knowledge base and paper records, so that it stays traceable to source and can be regenerated as the literature moves. A research project of <a href="https://www.elios.unige.it/" target="_blank" rel="noopener">EliosLab</a>, University of Genoa.</p>
      <p>Knowledge current through __AS_OF_LONG__. Companion tool: <a href="https://claude.ai/code/artifact/c054e12a-e683-4b5e-b233-a4317e7b1545" target="_blank" rel="noopener">Ask the EdgeAI Observatory</a> &mdash; query the same knowledge base directly.</p>
    </footer>
  </main>
</div>

<script>
(function(){
  var toggle = document.getElementById('tocToggle');
  var sidebar = document.getElementById('sidebar');
  if (toggle) {
    toggle.addEventListener('click', function(){ sidebar.classList.toggle('open'); });
  }
  document.querySelectorAll('.toc-list a').forEach(function(a){
    a.addEventListener('click', function(){ sidebar.classList.remove('open'); });
  });

  var links = Array.prototype.slice.call(document.querySelectorAll('.toc-list a[href^="#"]'));
  var targets = links.map(function(a){ return document.getElementById(a.getAttribute('href').slice(1)); }).filter(Boolean);
  function onScroll(){
    var pos = window.scrollY + 120;
    var current = null;
    for (var i = 0; i < targets.length; i++) {
      if (targets[i].offsetTop <= pos) current = targets[i];
    }
    links.forEach(function(a){ a.classList.remove('active'); });
    if (current) {
      var match = links.find(function(a){ return a.getAttribute('href') === '#' + current.id; });
      if (match) match.classList.add('active');
    }
  }
  document.addEventListener('scroll', onScroll, { passive: true });
  onScroll();
})();
</script>
"""


def assemble(parts):
    page = PAGE_TEMPLATE
    as_of_long = format_as_of(parts["as_of"])
    page = page.replace("__N_CONCEPTS__", str(parts["n_concepts"]))
    page = page.replace("__N_PAPERS__", str(parts["n_papers"]))
    page = page.replace("__N_BRANCHES__", str(parts["n_branches"]))
    page = page.replace("__AS_OF_SHORT__", parts["as_of"])
    page = page.replace("__AS_OF_LONG__", as_of_long)
    page = page.replace("__TOC__", parts["toc_html"])
    page = page.replace("__CHAPTERS__", '<div class="chapters">' + parts["chapters_html"] + "</div>")
    page = page.replace("__FIELD_NOTES__", parts["field_notes_html"])
    page = page.replace("__KNOWN_GAPS__", parts["known_gaps_html"])
    return page


if __name__ == "__main__":
    out_path = sys.argv[1] if len(sys.argv) > 1 else os.path.join(ROOT, "book_final.html")
    parts = build()
    page = assemble(parts)
    with open(out_path, "w", encoding="utf-8") as f:
        f.write(page)
    print(f"Wrote {out_path} ({len(page.encode('utf-8'))} bytes) — "
          f"{parts['n_concepts']} concepts, {parts['n_papers']} papers, "
          f"{parts['n_branches']} branches, as_of={parts['as_of']}")
