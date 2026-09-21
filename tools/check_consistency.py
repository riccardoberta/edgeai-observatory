#!/usr/bin/env python3
"""
Consistency checks for the EdgeAI Observatory repository.

Run locally (`python3 tools/check_consistency.py`) or in CI (the GitHub
Actions workflow runs it before building the site). Exit status 1 on any
ERROR; WARNINGs are printed but do not fail the build.

ERRORS (block the deploy):
  - unresolved [[wikilinks]] anywhere in the source tree
  - a 02_Papers/ record missing a required header field
    (**Full citation:**, **PDF:**, **Linked concepts:**)
  - a 02_Papers/ record that no 01_Knowledge_Base/ page links to
    ("orphan paper": every record must appear in at least one concept's
    Key papers, otherwise it is not part of the concept graph)
  - a 02_Papers/ record whose year folder does not match its filename prefix
  - a taxonomy bullet without a Knowledge Base page, or a Knowledge Base page
    not named in 00_Taxonomy/taxonomy.md
  - a 01_Knowledge_Base/ page missing one of the standard sections

WARNINGS (reported only):
  - taxonomy "Known gaps" bullets and 00_Config/consolidation_candidates.yaml
    describe different sets of open gaps
  - a 00_Config/sources.yaml digital library with status active whose
    last_checked is older than the newest weekly digest by more than 21 days
  - Observatory-voice process narration in KB pages, taxonomy or digests
    (see 00_Config/editorial_guidelines.md)
  - a personal name used in Observatory-voice prose (outside citations)
"""
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
os.chdir(ROOT)

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")
KB_SECTIONS = ["## Evolution of the concept", "## Key papers", "## Open problems",
               "## Research ideas", "## Possible thesis topics"]
REQUIRED_PAPER_FIELDS = ["**Full citation:**", "**PDF:**", "**Linked concepts:**"]
NARRATION_RE = re.compile(
    r"this cycle|this pass|this week's run|sources checked this week|candidates for deep analysis|"
    r"sourcing note|notes on this cycle|the observatory's consolidation queue|"
    r"we've tracked|we have tracked|in the \d{4}-\d{2}-\d{2} digest|covered in the \d{4}-\d{2}-\d{2}",
    re.I)
PERSONAL_NAME_RE = re.compile(r"\bRicky\b|Riccardo Berta|this Observatory's own")

errors, warnings = [], []


def read(path):
    with open(path, encoding="utf-8") as f:
        return f.read()


def title_of(path):
    first = read(path).split("\n", 1)[0].strip()
    return first[2:].strip() if first.startswith("# ") else os.path.splitext(os.path.basename(path))[0]


def md_files(*dirs):
    out = []
    for d in dirs:
        out += sorted(glob.glob(os.path.join(d, "**", "*.md"), recursive=True))
    return out


kb = md_files("01_Knowledge_Base")
papers = md_files("02_Papers")
digests = md_files("03_Digests")
taxonomy = "00_Taxonomy/taxonomy.md"
all_md = kb + papers + digests + [taxonomy, "README.md"]

# ---- wikilink resolution ------------------------------------------------
index = {}
for p in kb + papers + [taxonomy]:
    stem = os.path.splitext(os.path.basename(p))[0]
    for form in (stem, stem.replace("_", " "), title_of(p)):
        index[form] = p
        index[form.lower()] = p


def resolve(target):
    for cand in (target, target.replace(" ", "_"), target.lower(), target.replace(" ", "_").lower()):
        if cand in index:
            return index[cand]
    return None


inbound_from_kb = {p: 0 for p in papers}
for p in all_md:
    text = read(p)
    for m in WIKILINK_RE.finditer(text):
        target = m.group(1).strip()
        r = resolve(target)
        if r is None:
            errors.append(f"{p}: unresolved wikilink [[{target}]]")
        elif r in inbound_from_kb and p.startswith("01_Knowledge_Base/"):
            inbound_from_kb[r] += 1

# ---- paper records -------------------------------------------------------
for p in papers:
    text = read(p)
    for field in REQUIRED_PAPER_FIELDS:
        if field not in text:
            errors.append(f"{p}: missing required field {field}")
    year = p.split(os.sep)[1]
    if not os.path.basename(p).startswith(year + "_"):
        errors.append(f"{p}: filename does not start with its year folder ({year})")
    if inbound_from_kb[p] == 0:
        errors.append(f"{p}: orphan record — no 01_Knowledge_Base/ page links to it")

# ---- taxonomy <-> knowledge base ---------------------------------------
tax_text = read(taxonomy)
tax_bullets = re.findall(r"^-\s+\*\*(.+?)\*\*\s+—", tax_text, flags=re.M)
kb_titles = {title_of(p): p for p in kb}
kb_stems = {os.path.splitext(os.path.basename(p))[0]: p for p in kb}
known_gaps_start = tax_text.find("## Known gaps")
concept_bullets = [b for b in tax_bullets if tax_text.find("**" + b + "**") < known_gaps_start]
for b in concept_bullets:
    if b not in kb_titles and b.replace(" ", "_") not in kb_stems:
        errors.append(f"taxonomy bullet '{b}' has no 01_Knowledge_Base/ page")
for t, p in kb_titles.items():
    if t not in concept_bullets:
        errors.append(f"{p}: title '{t}' is not a concept bullet in {taxonomy}")

for p in kb:
    text = read(p)
    missing = [s for s in KB_SECTIONS if s not in text]
    if missing:
        errors.append(f"{p}: missing sections {missing}")

# ---- known gaps vs candidate queue (warning) ---------------------------
gaps = re.findall(r"^-\s+\*\*(.+?)\*\*", tax_text[known_gaps_start:], flags=re.M) if known_gaps_start != -1 else []
cand_path = "00_Config/consolidation_candidates.yaml"
if os.path.exists(cand_path):
    cand_ids = re.findall(r"^\s*-\s+id:\s*(\S+)", read(cand_path), flags=re.M)
    if len(gaps) != len(cand_ids):
        warnings.append(f"{taxonomy} lists {len(gaps)} known gaps but {cand_path} has {len(cand_ids)} candidates — "
                        f"the two lists should describe the same open signals")

# ---- sources.yaml freshness (warning) ----------------------------------
weekly = sorted(glob.glob("03_Digests/Weekly/*_weekly_digest.md"))
if weekly:
    newest = os.path.basename(weekly[-1])[:10]
    src = read("00_Config/sources.yaml")
    lib_block = src.split("\nconferences:")[0]
    for name, last in re.findall(r"- name: (.+?)\n(?:.*?\n)*?\s+last_checked: (\S+)", lib_block):
        if last == "null":
            warnings.append(f"sources.yaml: digital library '{name}' has never been checked (last_checked: null)")
            continue
        from datetime import date
        try:
            d_last = date.fromisoformat(last)
            d_new = date.fromisoformat(newest)
            if (d_new - d_last).days > 21:
                warnings.append(f"sources.yaml: '{name}' last_checked {last} is stale versus newest digest {newest}")
        except ValueError:
            warnings.append(f"sources.yaml: '{name}' has an unparseable last_checked '{last}'")

# ---- style (warnings) ----------------------------------------------------
for p in kb + digests + [taxonomy]:
    for i, line in enumerate(read(p).split("\n"), 1):
        if NARRATION_RE.search(line):
            warnings.append(f"{p}:{i}: Observatory process narration — see 00_Config/editorial_guidelines.md")
for p in kb + digests + [taxonomy, "README.md"]:
    for i, line in enumerate(read(p).split("\n"), 1):
        if PERSONAL_NAME_RE.search(line):
            warnings.append(f"{p}:{i}: personal-name attribution in Observatory voice")

# ---- report --------------------------------------------------------------
for w in warnings:
    print("WARNING:", w)
for e in errors:
    print("ERROR:", e)
print(f"\n{len(kb)} concepts, {len(papers)} paper records, {len(digests)} digests checked — "
      f"{len(errors)} errors, {len(warnings)} warnings")
sys.exit(1 if errors else 0)
