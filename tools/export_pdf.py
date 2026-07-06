#!/usr/bin/env python3
"""
Export the full EdgeAI Observatory knowledge base to a polished PDF.

The exporter reads the same source directories as the MkDocs build, rewrites
Obsidian-style wikilinks, and lays the content out with ReportLab.
"""
from __future__ import annotations

import argparse
import os
import re
import sys
from dataclasses import dataclass
from datetime import datetime
from html import escape
from pathlib import Path
from typing import Iterable

try:
    from reportlab.lib import colors
    from reportlab.lib.enums import TA_CENTER, TA_RIGHT
    from reportlab.lib.pagesizes import A4
    from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
    from reportlab.lib.units import mm
    from reportlab.pdfbase import pdfmetrics
    from reportlab.pdfbase.ttfonts import TTFont
    from reportlab.platypus import (
        BaseDocTemplate,
        Frame,
        HRFlowable,
        ListFlowable,
        ListItem,
        PageBreak,
        PageTemplate,
        Paragraph,
        Preformatted,
        Spacer,
        Table,
        TableStyle,
    )
    from reportlab.platypus.tableofcontents import TableOfContents
except ImportError as exc:
    raise SystemExit(
        "Missing PDF dependency. Install it in your active Python environment with:\n"
        "  python -m pip install -r requirements-docs.txt\n"
        f"\nOriginal error: {exc}"
    )

SCRIPT_DIR = Path(__file__).resolve().parent
ROOT = SCRIPT_DIR.parent
sys.path.insert(0, str(SCRIPT_DIR))

import build_docs  # noqa: E402

DEFAULT_OUTPUT = ROOT / "output" / "pdf" / "edgeai-observatory-export.pdf"

INDIGO = colors.HexColor("#2f3a8f")
AMBER = colors.HexColor("#c4820e")
INK = colors.HexColor("#1f2937")
MUTED = colors.HexColor("#6b7280")
RULE = colors.HexColor("#d9dee8")
SOFT_BG = colors.HexColor("#f4f6fb")

FONT_REGULAR = "Helvetica"
FONT_BOLD = "Helvetica-Bold"
FONT_ITALIC = "Helvetica-Oblique"
FONT_BOLD_ITALIC = "Helvetica-BoldOblique"
FONT_MONO = "Courier"

HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
BULLET_RE = re.compile(r"^\s*[-*]\s+(.+)$")
NUMBER_RE = re.compile(r"^\s*\d+[.)]\s+(.+)$")
LINK_RE = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
BARE_URL_RE = re.compile(r"(?<![\"'=])(https?://[^\s<>()]+)")
CODE_RE = re.compile(r"`([^`]+)`")
BOLD_RE = re.compile(r"\*\*(.+?)\*\*")
CONTROL_RE = re.compile(r"[\x00-\x08\x0b\x0c\x0e-\x1f]")


@dataclass(frozen=True)
class SourceDocument:
    rel_path: str
    title: str
    section: str
    order_key: tuple
    text: str


class ObservatoryDocTemplate(BaseDocTemplate):
    def __init__(self, filename: str, **kwargs):
        super().__init__(filename, **kwargs)
        frame = Frame(
            self.leftMargin,
            self.bottomMargin,
            self.width,
            self.height,
            id="normal",
        )
        self.addPageTemplates(
            [PageTemplate(id="main", frames=[frame], onPage=draw_page_frame)]
        )

    def afterFlowable(self, flowable):
        level = getattr(flowable, "_toc_level", None)
        bookmark = getattr(flowable, "_bookmark_name", None)
        if level is None or bookmark is None:
            return

        text = flowable.getPlainText()
        self.canv.bookmarkPage(bookmark)
        self.notify("TOCEntry", (level, text, self.page))
        self.canv.addOutlineEntry(text, bookmark, level=level, closed=level == 0)


def draw_page_frame(canvas, doc):
    canvas.saveState()
    width, height = A4

    if doc.page > 1:
        canvas.setStrokeColor(RULE)
        canvas.setLineWidth(0.4)
        canvas.line(doc.leftMargin, height - 15 * mm, width - doc.rightMargin, height - 15 * mm)
        canvas.setFont(FONT_REGULAR, 8)
        canvas.setFillColor(MUTED)
        canvas.drawString(doc.leftMargin, height - 11 * mm, "EdgeAI Observatory Export")
        canvas.drawRightString(width - doc.rightMargin, height - 11 * mm, f"Page {doc.page}")

    canvas.setStrokeColor(RULE)
    canvas.setLineWidth(0.4)
    canvas.line(doc.leftMargin, 14 * mm, width - doc.rightMargin, 14 * mm)
    canvas.setFont(FONT_REGULAR, 7.5)
    canvas.setFillColor(MUTED)
    canvas.drawCentredString(width / 2, 9 * mm, "Generated from the repository Markdown sources")
    canvas.restoreState()


def first_existing(paths: Iterable[str]) -> str | None:
    for path in paths:
        if os.path.isfile(path):
            return path
    return None


def register_fonts():
    global FONT_REGULAR, FONT_BOLD, FONT_ITALIC, FONT_BOLD_ITALIC

    regular = first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial Unicode.ttf",
            "/Library/Fonts/Arial Unicode.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans.ttf",
        ]
    )
    bold = first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial Bold.ttf",
            "/Library/Fonts/Arial Bold.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Bold.ttf",
        ]
    )
    italic = first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial Italic.ttf",
            "/Library/Fonts/Arial Italic.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-Oblique.ttf",
        ]
    )
    bold_italic = first_existing(
        [
            "/System/Library/Fonts/Supplemental/Arial Bold Italic.ttf",
            "/Library/Fonts/Arial Bold Italic.ttf",
            "/usr/share/fonts/truetype/dejavu/DejaVuSans-BoldOblique.ttf",
        ]
    )

    if not regular:
        return

    FONT_REGULAR = "ObservatorySans"
    FONT_BOLD = "ObservatorySans-Bold" if bold else FONT_REGULAR
    FONT_ITALIC = "ObservatorySans-Italic" if italic else FONT_REGULAR
    FONT_BOLD_ITALIC = "ObservatorySans-BoldItalic" if bold_italic else FONT_BOLD

    pdfmetrics.registerFont(TTFont(FONT_REGULAR, regular))
    if bold:
        pdfmetrics.registerFont(TTFont(FONT_BOLD, bold))
    if italic:
        pdfmetrics.registerFont(TTFont(FONT_ITALIC, italic))
    if bold_italic:
        pdfmetrics.registerFont(TTFont(FONT_BOLD_ITALIC, bold_italic))

    pdfmetrics.registerFontFamily(
        FONT_REGULAR,
        normal=FONT_REGULAR,
        bold=FONT_BOLD,
        italic=FONT_ITALIC,
        boldItalic=FONT_BOLD_ITALIC,
    )


def build_styles():
    base = getSampleStyleSheet()
    styles = {}

    def add(name, parent="Normal", **kwargs):
        styles[name] = ParagraphStyle(name, parent=base[parent], **kwargs)

    add(
        "CoverTitle",
        fontName=FONT_BOLD,
        fontSize=31,
        leading=36,
        textColor=INDIGO,
        alignment=TA_CENTER,
        spaceAfter=8,
    )
    add(
        "CoverSubtitle",
        fontName=FONT_REGULAR,
        fontSize=12,
        leading=17,
        textColor=INK,
        alignment=TA_CENTER,
        spaceAfter=20,
    )
    add(
        "Generated",
        fontName=FONT_REGULAR,
        fontSize=8.5,
        leading=12,
        textColor=MUTED,
        alignment=TA_CENTER,
        spaceAfter=16,
    )
    add(
        "TocTitle",
        fontName=FONT_BOLD,
        fontSize=21,
        leading=26,
        textColor=INDIGO,
        spaceAfter=14,
    )
    add(
        "SectionTitle",
        fontName=FONT_BOLD,
        fontSize=22,
        leading=27,
        textColor=INDIGO,
        spaceAfter=8,
        keepWithNext=True,
    )
    add(
        "SectionIntro",
        fontName=FONT_REGULAR,
        fontSize=10,
        leading=14,
        textColor=MUTED,
        spaceAfter=14,
    )
    add(
        "DocTitle",
        fontName=FONT_BOLD,
        fontSize=16,
        leading=20,
        textColor=INK,
        spaceAfter=4,
        keepWithNext=True,
    )
    add(
        "SourcePath",
        fontName=FONT_REGULAR,
        fontSize=7.5,
        leading=10,
        textColor=MUTED,
        spaceAfter=9,
    )
    add(
        "Body",
        fontName=FONT_REGULAR,
        fontSize=9.4,
        leading=13.3,
        textColor=INK,
        spaceAfter=7,
    )
    add(
        "Bullet",
        fontName=FONT_REGULAR,
        fontSize=9.2,
        leading=12.6,
        textColor=INK,
        leftIndent=4,
        spaceAfter=3,
    )
    add(
        "Quote",
        fontName=FONT_ITALIC,
        fontSize=9.2,
        leading=12.8,
        textColor=MUTED,
        leftIndent=12,
        borderColor=RULE,
        borderWidth=0,
        borderPadding=6,
        spaceAfter=7,
    )
    add(
        "Code",
        fontName=FONT_MONO,
        fontSize=7.4,
        leading=9.6,
        textColor=colors.HexColor("#111827"),
        backColor=colors.HexColor("#eef1f7"),
        borderPadding=6,
        spaceAfter=8,
    )
    add(
        "H1",
        fontName=FONT_BOLD,
        fontSize=15,
        leading=19,
        textColor=INDIGO,
        spaceBefore=8,
        spaceAfter=6,
        keepWithNext=True,
    )
    add(
        "H2",
        fontName=FONT_BOLD,
        fontSize=12.2,
        leading=15,
        textColor=INDIGO,
        spaceBefore=7,
        spaceAfter=5,
        keepWithNext=True,
    )
    add(
        "H3",
        fontName=FONT_BOLD,
        fontSize=10.8,
        leading=13.6,
        textColor=INK,
        spaceBefore=6,
        spaceAfter=4,
        keepWithNext=True,
    )
    add(
        "H4",
        fontName=FONT_BOLD,
        fontSize=9.7,
        leading=12.5,
        textColor=INK,
        spaceBefore=5,
        spaceAfter=3,
        keepWithNext=True,
    )

    return styles


def classify_section(rel_path: str) -> tuple[str, tuple]:
    parts = rel_path.split("/")
    if rel_path == "README.md":
        return "Overview", (0, rel_path)
    if parts[0] == "00_Taxonomy":
        return "Taxonomy", (1, rel_path)
    if parts[0] == "01_Knowledge_Base":
        subsection_order = {
            "Algorithms": 0,
            "Frameworks": 1,
            "Hardware": 2,
            "Applications": 3,
        }
        subsection = parts[1] if len(parts) > 1 else "General"
        return (
            f"Knowledge Base - {subsection}",
            (2, subsection_order.get(subsection, 99), rel_path.lower()),
        )
    if parts[0] == "02_Papers":
        year = parts[1] if len(parts) > 1 else "Unknown"
        return f"Paper Records - {year}", (3, year, rel_path.lower())
    if parts[0] == "03_Digests":
        subsection_order = {"Monthly": 0, "Weekly": 1}
        subsection = parts[1] if len(parts) > 1 else "General"
        return (
            f"Digests - {subsection}",
            (4, subsection_order.get(subsection, 99), rel_path.lower()),
        )
    return "Other", (99, rel_path.lower())


def read_title(path: Path) -> str:
    with path.open(encoding="utf-8") as handle:
        for line in handle:
            match = HEADING_RE.match(line.strip())
            if match:
                return strip_markdown(match.group(2))
    return path.stem.replace("_", " ")


def strip_markdown(text: str) -> str:
    text = text.strip().strip("#").strip()
    text = re.sub(r"\*\*(.+?)\*\*", r"\1", text)
    text = re.sub(r"`([^`]+)`", r"\1", text)
    text = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r"\1", text)
    return text


def load_documents() -> tuple[list[SourceDocument], list[tuple[str, str]]]:
    source_files = [
        (Path(abs_path), rel_path)
        for abs_path, rel_path in build_docs.find_markdown_files()
    ]
    index = build_docs.build_index(
        [(str(abs_path), rel_path) for abs_path, rel_path in source_files]
    )
    unresolved: list[tuple[str, str]] = []
    documents: list[SourceDocument] = []

    readme = ROOT / "README.md"
    if readme.is_file():
        source_files.insert(0, (readme, "README.md"))

    for abs_path, rel_path in source_files:
        text = abs_path.read_text(encoding="utf-8")
        rewritten = build_docs.rewrite_links(text, rel_path, index, unresolved)
        rewritten = CONTROL_RE.sub("", rewritten)
        section, order_key = classify_section(rel_path)
        documents.append(
            SourceDocument(
                rel_path=rel_path,
                title=read_title(abs_path),
                section=section,
                order_key=order_key,
                text=rewritten,
            )
        )

    documents.sort(key=lambda doc: doc.order_key)
    return documents, unresolved


def format_inline(text: str) -> str:
    placeholders: list[str] = []

    def stash(html: str) -> str:
        placeholders.append(html)
        return f"\u0000{len(placeholders) - 1}\u0000"

    def link_repl(match):
        label = strip_markdown(match.group(1))
        href = match.group(2).strip()
        safe_label = escape(label, quote=False)
        safe_href = escape(href, quote=True)
        if href.startswith(("http://", "https://", "mailto:")):
            return stash(f'<a href="{safe_href}" color="#2f3a8f">{safe_label}</a>')
        return stash(f'<font color="#2f3a8f">{safe_label}</font>')

    text = LINK_RE.sub(link_repl, text)
    text = escape(text, quote=False)
    text = CODE_RE.sub(
        lambda m: f'<font name="{FONT_MONO}" backColor="#eef1f7">{m.group(1)}</font>',
        text,
    )
    text = BOLD_RE.sub(r"<b>\1</b>", text)
    text = BARE_URL_RE.sub(
        lambda m: f'<a href="{m.group(1)}" color="#2f3a8f">{m.group(1)}</a>',
        text,
    )

    for idx, html in enumerate(placeholders):
        text = text.replace(f"\u0000{idx}\u0000", html)
    return text


def toc_paragraph(text: str, style, level: int, bookmark: str) -> Paragraph:
    paragraph = Paragraph(format_inline(text), style)
    paragraph._toc_level = level
    paragraph._bookmark_name = bookmark
    return paragraph


def markdown_to_flowables(text: str, styles, skip_initial_h1: bool = True):
    story = []
    lines = text.splitlines()
    paragraph_lines: list[str] = []
    list_items: list[str] = []
    list_kind: str | None = None
    code_lines: list[str] = []
    in_code = False
    skipped_h1 = False

    def flush_paragraph():
        nonlocal paragraph_lines
        if not paragraph_lines:
            return
        html = "<br/>".join(format_inline(line.strip()) for line in paragraph_lines)
        story.append(Paragraph(html, styles["Body"]))
        paragraph_lines = []

    def flush_list():
        nonlocal list_items, list_kind
        if not list_items:
            return
        bullet_type = "1" if list_kind == "number" else "bullet"
        flowable_items = [
            ListItem(Paragraph(format_inline(item), styles["Bullet"]), leftIndent=11)
            for item in list_items
        ]
        story.append(
            ListFlowable(
                flowable_items,
                bulletType=bullet_type,
                leftIndent=14,
                bulletFontName=FONT_REGULAR,
                bulletFontSize=8.4,
                bulletColor=AMBER,
                spaceAfter=7,
            )
        )
        list_items = []
        list_kind = None

    def flush_code():
        nonlocal code_lines
        if not code_lines:
            return
        story.append(Preformatted("\n".join(code_lines), styles["Code"]))
        code_lines = []

    for line in lines:
        stripped = line.rstrip()

        if stripped.startswith("```"):
            flush_paragraph()
            flush_list()
            if in_code:
                flush_code()
                in_code = False
            else:
                in_code = True
            continue

        if in_code:
            code_lines.append(stripped)
            continue

        if not stripped:
            flush_paragraph()
            flush_list()
            continue

        heading = HEADING_RE.match(stripped)
        if heading:
            flush_paragraph()
            flush_list()
            level = len(heading.group(1))
            heading_text = strip_markdown(heading.group(2))
            if skip_initial_h1 and level == 1 and not skipped_h1:
                skipped_h1 = True
                continue
            style_name = "H1" if level == 1 else "H2" if level == 2 else "H3" if level == 3 else "H4"
            story.append(Paragraph(format_inline(heading_text), styles[style_name]))
            continue

        if stripped in {"---", "***", "___"}:
            flush_paragraph()
            flush_list()
            story.append(
                HRFlowable(width="100%", color=RULE, thickness=0.7, spaceBefore=4, spaceAfter=10)
            )
            continue

        bullet = BULLET_RE.match(stripped)
        if bullet:
            flush_paragraph()
            if list_kind not in (None, "bullet"):
                flush_list()
            list_kind = "bullet"
            list_items.append(bullet.group(1).strip())
            continue

        number = NUMBER_RE.match(stripped)
        if number:
            flush_paragraph()
            if list_kind not in (None, "number"):
                flush_list()
            list_kind = "number"
            list_items.append(number.group(1).strip())
            continue

        if stripped.startswith(">"):
            flush_paragraph()
            flush_list()
            quote = stripped.lstrip("> ").strip()
            story.append(Paragraph(format_inline(quote), styles["Quote"]))
            continue

        flush_list()
        paragraph_lines.append(stripped)

    flush_paragraph()
    flush_list()
    flush_code()
    return story


def section_intro(section: str, docs: list[SourceDocument]) -> str:
    if section == "Overview":
        return "Repository orientation and operating principles."
    if section == "Taxonomy":
        return "The living concept map used to organize the Observatory."
    if section.startswith("Knowledge Base"):
        return f"{len(docs)} concept note(s), grouped by the Observatory taxonomy."
    if section.startswith("Paper Records"):
        return f"{len(docs)} structured paper analysis record(s)."
    if section.startswith("Digests"):
        return f"{len(docs)} time-based research intelligence report(s)."
    return f"{len(docs)} source document(s)."


def build_cover(styles, documents: list[SourceDocument], unresolved_count: int):
    counts = {
        "Total source files": len(documents),
        "Knowledge base notes": sum(doc.rel_path.startswith("01_Knowledge_Base/") for doc in documents),
        "Paper records": sum(doc.rel_path.startswith("02_Papers/") for doc in documents),
        "Digests and reports": sum(doc.rel_path.startswith("03_Digests/") for doc in documents),
    }
    generated = datetime.now().astimezone().strftime("%Y-%m-%d %H:%M %Z")
    data = [[Paragraph(f"<b>{escape(label)}</b>", styles["Body"]), str(value)] for label, value in counts.items()]
    if unresolved_count:
        data.append([Paragraph("<b>Unresolved wikilinks</b>", styles["Body"]), str(unresolved_count)])

    table = Table(data, colWidths=[72 * mm, 28 * mm], hAlign="CENTER")
    table.setStyle(
        TableStyle(
            [
                ("BACKGROUND", (0, 0), (-1, -1), SOFT_BG),
                ("BOX", (0, 0), (-1, -1), 0.6, RULE),
                ("INNERGRID", (0, 0), (-1, -1), 0.35, colors.white),
                ("TEXTCOLOR", (0, 0), (-1, -1), INK),
                ("FONTNAME", (0, 0), (-1, -1), FONT_REGULAR),
                ("FONTSIZE", (0, 0), (-1, -1), 9),
                ("ALIGN", (1, 0), (1, -1), "RIGHT"),
                ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
                ("LEFTPADDING", (0, 0), (-1, -1), 8),
                ("RIGHTPADDING", (0, 0), (-1, -1), 8),
                ("TOPPADDING", (0, 0), (-1, -1), 7),
                ("BOTTOMPADDING", (0, 0), (-1, -1), 7),
            ]
        )
    )

    return [
        Spacer(1, 45 * mm),
        Paragraph("EdgeAI Observatory", styles["CoverTitle"]),
        Paragraph(
            "Complete research memory export: taxonomy, knowledge base, paper records, weekly digests, and monthly reports.",
            styles["CoverSubtitle"],
        ),
        Paragraph(f"Generated {escape(generated)}", styles["Generated"]),
        table,
        Spacer(1, 22 * mm),
        HRFlowable(width="42%", color=AMBER, thickness=1.2, spaceBefore=4, spaceAfter=8),
        Paragraph(
            "Built from the repository Markdown sources. Wikilinks are resolved into readable PDF references.",
            styles["Generated"],
        ),
    ]


def group_documents(documents: list[SourceDocument]) -> list[tuple[str, list[SourceDocument]]]:
    grouped: list[tuple[str, list[SourceDocument]]] = []
    current_section = None
    current_docs: list[SourceDocument] = []

    for doc in documents:
        if doc.section != current_section:
            if current_section is not None:
                grouped.append((current_section, current_docs))
            current_section = doc.section
            current_docs = []
        current_docs.append(doc)

    if current_section is not None:
        grouped.append((current_section, current_docs))
    return grouped


def build_story(documents: list[SourceDocument], unresolved: list[tuple[str, str]], styles):
    story = []
    story.extend(build_cover(styles, documents, len(unresolved)))
    story.append(PageBreak())

    toc = TableOfContents()
    toc.levelStyles = [
        ParagraphStyle(
            "TOCLevel0",
            fontName=FONT_BOLD,
            fontSize=10.5,
            leading=14,
            leftIndent=0,
            firstLineIndent=0,
            textColor=INDIGO,
            spaceBefore=4,
        ),
        ParagraphStyle(
            "TOCLevel1",
            fontName=FONT_REGULAR,
            fontSize=8.8,
            leading=11.5,
            leftIndent=11,
            firstLineIndent=-11,
            textColor=INK,
        ),
    ]
    story.append(Paragraph("Contents", styles["TocTitle"]))
    story.append(toc)
    story.append(PageBreak())

    bookmark_index = 0
    for section, docs in group_documents(documents):
        section_bookmark = f"section-{bookmark_index}"
        bookmark_index += 1
        story.append(toc_paragraph(section, styles["SectionTitle"], 0, section_bookmark))
        story.append(Paragraph(format_inline(section_intro(section, docs)), styles["SectionIntro"]))

        for doc in docs:
            doc_bookmark = f"doc-{bookmark_index}"
            bookmark_index += 1
            story.append(toc_paragraph(doc.title, styles["DocTitle"], 1, doc_bookmark))
            story.append(Paragraph(escape(doc.rel_path), styles["SourcePath"]))
            story.extend(markdown_to_flowables(doc.text, styles))
            story.append(PageBreak())

    if story and isinstance(story[-1], PageBreak):
        story.pop()
    return story


def export_pdf(output_path: Path):
    register_fonts()
    styles = build_styles()
    documents, unresolved = load_documents()

    output_path = output_path.resolve()
    output_path.parent.mkdir(parents=True, exist_ok=True)

    doc = ObservatoryDocTemplate(
        str(output_path),
        pagesize=A4,
        leftMargin=18 * mm,
        rightMargin=18 * mm,
        topMargin=20 * mm,
        bottomMargin=20 * mm,
        title="EdgeAI Observatory Export",
        author="EdgeAI Observatory",
        subject="Complete Markdown knowledge base export",
    )
    story = build_story(documents, unresolved, styles)
    doc.multiBuild(story)
    return output_path, documents, unresolved


def display_path(path: Path) -> str:
    try:
        return str(path.relative_to(ROOT))
    except ValueError:
        return str(path)


def parse_args():
    parser = argparse.ArgumentParser(
        description="Export the full EdgeAI Observatory Markdown corpus to PDF."
    )
    parser.add_argument(
        "-o",
        "--output",
        type=Path,
        default=DEFAULT_OUTPUT,
        help=f"PDF output path. Default: {DEFAULT_OUTPUT.relative_to(ROOT)}",
    )
    return parser.parse_args()


def main():
    args = parse_args()
    output_path, documents, unresolved = export_pdf(args.output)
    print(f"Wrote {display_path(output_path)}")
    print(f"Included {len(documents)} source files.")
    if unresolved:
        print(f"WARNING: {len(unresolved)} unresolved wikilink(s).")


if __name__ == "__main__":
    main()
