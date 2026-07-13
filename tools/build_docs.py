#!/usr/bin/env python3
"""
Render the Observatory's source markdown (with Obsidian-style [[wikilinks]])
into docs/, with wikilinks rewritten to plain relative markdown links that
MkDocs can resolve natively.

Why this exists instead of a wikilink MkDocs plugin: the most maintained
candidate (mkdocs-ezlinks-plugin 0.1.14) resolves the *target* correctly but
emits a broken, lowercased, extension-less href — every cross-link in the
site ends up dead. Our linking scheme is simple (exact filename match, same
logic already used by kb_build/parse.py for the KB Explorer artifact), so a
~100-line preprocessing script is more reliable than a third-party plugin,
and avoids adding a dependency to an MkDocs plugin ecosystem that is
currently in flux (MkDocs 2.0 dropping plugin support entirely).

Run before `mkdocs build` / `mkdocs serve` (also wired into
.github/workflows/docs.yml for the GitHub Pages deploy).
"""
import os
import re
import shutil

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DOCS = os.path.join(ROOT, "docs")
STATIC_SITE = os.path.join(ROOT, "00_Config", "site")

SOURCE_DIRS = ["00_Taxonomy", "01_Knowledge_Base", "02_Papers", "03_Digests"]

WIKILINK_RE = re.compile(r"\[\[([^\]|]+)(?:\|([^\]]+))?\]\]")


def find_markdown_files():
    """Return list of (abs_path, rel_path) for every .md file under SOURCE_DIRS."""
    files = []
    for sub in SOURCE_DIRS:
        base = os.path.join(ROOT, sub)
        if not os.path.isdir(base):
            continue
        for dirpath, _, filenames in os.walk(base):
            for fname in filenames:
                if fname.endswith(".md"):
                    abs_path = os.path.join(dirpath, fname)
                    rel_path = os.path.relpath(abs_path, ROOT)
                    files.append((abs_path, rel_path))
    return files


def build_index(files):
    """Map every plausible reference form (id, title, spaced/hyphenated id) -> rel_path."""
    index = {}
    for abs_path, rel_path in files:
        stem = os.path.splitext(os.path.basename(rel_path))[0]
        forms = {stem, stem.replace("_", " "), stem.replace("-", " ")}
        try:
            with open(abs_path, encoding="utf-8") as f:
                first_line = f.readline().strip()
            if first_line.startswith("# "):
                title = first_line[2:].strip()
                forms.add(title)
        except OSError:
            pass
        for form in forms:
            index[form] = rel_path
            index[form.lower()] = rel_path
    return index


def resolve(link_target, index):
    if link_target in index:
        return index[link_target]
    if link_target.lower() in index:
        return index[link_target.lower()]
    norm = link_target.replace(" ", "_")
    if norm in index:
        return index[norm]
    if norm.lower() in index:
        return index[norm.lower()]
    return None


def rewrite_links(text, current_rel_path, index, unresolved):
    current_dir = os.path.dirname(current_rel_path)

    def repl(m):
        target, label = m.group(1).strip(), m.group(2)
        display = (label or target).strip()
        resolved_rel = resolve(target, index)
        if resolved_rel is None:
            unresolved.append((current_rel_path, target))
            return display
        link_path = os.path.relpath(resolved_rel, current_dir)
        link_path = link_path.replace(os.sep, "/")
        return f"[{display}]({link_path})"

    return WIKILINK_RE.sub(repl, text)


def copy_static_site_files():
    """Copy tracked MkDocs static files into the generated docs/ tree."""
    if not os.path.isdir(STATIC_SITE):
        return 0

    copied = 0
    for dirpath, _, filenames in os.walk(STATIC_SITE):
        rel_dir = os.path.relpath(dirpath, STATIC_SITE)
        out_dir = DOCS if rel_dir == "." else os.path.join(DOCS, rel_dir)
        os.makedirs(out_dir, exist_ok=True)
        for fname in filenames:
            src = os.path.join(dirpath, fname)
            dst = os.path.join(out_dir, fname)
            shutil.copy2(src, dst)
            copied += 1
    return copied


def main():
    # Note: deliberately not removing an existing docs/ tree first. The
    # rendered output is deterministic given the same sources (file set is
    # stable run to run), so overwriting in place is sufficient and avoids
    # rmtree/rmdir, which can fail with EPERM on some mounted filesystems.
    os.makedirs(DOCS, exist_ok=True)

    files = find_markdown_files()
    index = build_index(files)
    unresolved = []

    for abs_path, rel_path in files:
        with open(abs_path, encoding="utf-8") as f:
            text = f.read()
        rewritten = rewrite_links(text, rel_path, index, unresolved)
        out_path = os.path.join(DOCS, rel_path)
        os.makedirs(os.path.dirname(out_path), exist_ok=True)
        with open(out_path, "w", encoding="utf-8") as f:
            f.write(rewritten)

    # Homepage
    readme_path = os.path.join(ROOT, "README.md")
    if os.path.isfile(readme_path):
        with open(readme_path, encoding="utf-8") as f:
            text = f.read()
        rewritten = rewrite_links(text, "index.md", index, unresolved)
        with open(os.path.join(DOCS, "index.md"), "w", encoding="utf-8") as f:
            f.write(rewritten)

    static_count = copy_static_site_files()

    print(f"Rendered {len(files)} files into docs/.")
    if static_count:
        print(f"Copied {static_count} static site files into docs/.")
    if unresolved:
        print(f"WARNING: {len(unresolved)} unresolved wikilinks:")
        for src, target in unresolved:
            print(f"  {src}: [[{target}]]")


if __name__ == "__main__":
    main()
