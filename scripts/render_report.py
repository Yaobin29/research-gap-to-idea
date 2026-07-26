#!/usr/bin/env python3
"""Render a research-gap-to-idea Markdown report as a standalone HTML file.

The renderer intentionally uses only the Python standard library so the public
skill stays portable. It supports the Markdown constructs used by the report
template: headings, paragraphs, links, emphasis, code fences, blockquotes,
lists, and pipe tables. The Markdown file remains the single source of truth.
"""

from __future__ import annotations

import argparse
import html
import re
from pathlib import Path


HEADING_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$")
TABLE_SEPARATOR_RE = re.compile(r"^\|?\s*:?-{3,}:?\s*(\|\s*:?-{3,}:?\s*)+\|?$")
CARD_RE = re.compile(r"^(?:P\d+\b|Idea\s+\d+\b)")


def slugify(value: str) -> str:
    value = re.sub(r"[`*_]", "", value).strip().lower()
    value = re.sub(r"[^\w\-\u4e00-\u9fff ]+", "", value)
    return re.sub(r"\s+", "-", value) or "section"


def split_cells(line: str) -> list[str]:
    line = line.strip()
    if line.startswith("|"):
        line = line[1:]
    if line.endswith("|"):
        line = line[:-1]
    return [cell.strip() for cell in line.split("|")]


def inline(value: str) -> str:
    escaped = html.escape(value, quote=True)
    escaped = re.sub(r"\[([^\]]+)\]\(([^)]+)\)", r'<a href="\2">\1</a>', escaped)
    escaped = re.sub(r"`([^`]+)`", r"<code>\1</code>", escaped)
    escaped = re.sub(r"\*\*([^*]+)\*\*", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"__([^_]+)__", r"<strong>\1</strong>", escaped)
    escaped = re.sub(r"(?<!\*)\*([^*]+)\*(?!\*)", r"<em>\1</em>", escaped)
    escaped = re.sub(r"(?<!_)_([^_]+)_(?!_)", r"<em>\1</em>", escaped)
    for marker, css in (("D", "evidence-d"), ("C", "evidence-c"), ("L", "evidence-l"), ("U", "evidence-u")):
        escaped = escaped.replace(f"[{marker}]", f'<span class="evidence {css}">[{marker}]</span>')
    return escaped


def render_table(lines: list[str]) -> str:
    headers = split_cells(lines[0])
    rows = [split_cells(line) for line in lines[2:]]
    out = ['<div class="table-wrap"><table><thead><tr>']
    out.extend(f"<th>{inline(cell)}</th>" for cell in headers)
    out.append("</tr></thead><tbody>")
    for row in rows:
        out.append("<tr>")
        for index in range(len(headers)):
            cell = row[index] if index < len(row) else ""
            out.append(f"<td>{inline(cell)}</td>")
        out.append("</tr>")
    out.append("</tbody></table></div>")
    return "".join(out)


def render_markdown(source: str) -> tuple[str, str]:
    lines = source.splitlines()
    output: list[str] = []
    toc: list[str] = []
    paragraph: list[str] = []
    list_items: list[str] = []
    list_ordered = False
    in_code = False
    code_lines: list[str] = []
    active_card: str | None = None
    used_ids: dict[str, int] = {}

    def flush_paragraph() -> None:
        nonlocal paragraph
        if paragraph:
            output.append(f"<p>{inline(' '.join(line.strip() for line in paragraph))}</p>")
            paragraph = []

    def flush_list() -> None:
        nonlocal list_items
        if not list_items:
            return
        tag = "ol" if list_ordered else "ul"
        output.append(f"<{tag}>" + "".join(f"<li>{inline(item)}</li>" for item in list_items) + f"</{tag}>")
        list_items = []

    def close_card() -> None:
        nonlocal active_card
        if active_card:
            output.append("</div></details>")
            active_card = None

    index = 0
    while index < len(lines):
        line = lines[index]
        if in_code:
            if line.strip().startswith("```"):
                output.append(f'<pre><code>{html.escape("\n".join(code_lines))}</code></pre>')
                code_lines = []
                in_code = False
            else:
                code_lines.append(line)
            index += 1
            continue

        if line.strip().startswith("```"):
            flush_paragraph(); flush_list()
            in_code = True
            index += 1
            continue

        heading = HEADING_RE.match(line)
        if heading:
            flush_paragraph(); flush_list()
            level = len(heading.group(1))
            text = heading.group(2)
            if active_card and (level <= 2 or (level == 3 and not CARD_RE.match(text))):
                close_card()
            base_id = slugify(text)
            count = used_ids.get(base_id, 0)
            used_ids[base_id] = count + 1
            element_id = base_id if count == 0 else f"{base_id}-{count + 1}"
            if level == 1 and not output:
                title = inline(text)
            else:
                title = inline(text)
            if level in (2, 3):
                toc_class = "toc-h3" if level == 3 else "toc-h2"
                toc.append(f'<a class="{toc_class}" href="#{element_id}">{title}</a>')
            if level == 3 and CARD_RE.match(text):
                card_class = "idea-card" if text.startswith("Idea") else "paper-card"
                output.append(f'<details class="{card_class}" id="{element_id}" open><summary>{title}</summary><div>')
                active_card = card_class
            else:
                output.append(f'<h{level} id="{element_id}">{title}</h{level}>')
            index += 1
            continue

        if line.strip() == "":
            flush_paragraph(); flush_list(); index += 1; continue

        if line.lstrip().startswith(">"):
            flush_paragraph(); flush_list()
            quote_lines = []
            while index < len(lines) and lines[index].lstrip().startswith(">"):
                quote_lines.append(lines[index].lstrip()[1:].strip())
                index += 1
            output.append(f'<blockquote>{inline(" ".join(quote_lines))}</blockquote>')
            continue

        if line.lstrip().startswith("- ") or re.match(r"^\s*\d+\.\s+", line):
            flush_paragraph()
            current_ordered = bool(re.match(r"^\s*\d+\.\s+", line))
            if list_items and current_ordered != list_ordered:
                flush_list()
            list_ordered = current_ordered
            item = re.sub(r"^\s*(?:- |\d+\.\s+)", "", line)
            list_items.append(item)
            index += 1
            continue

        if line.lstrip().startswith("|") and index + 1 < len(lines) and TABLE_SEPARATOR_RE.match(lines[index + 1]):
            flush_paragraph(); flush_list()
            table_lines = [line, lines[index + 1]]
            index += 2
            while index < len(lines) and lines[index].lstrip().startswith("|") and lines[index].strip():
                table_lines.append(lines[index]); index += 1
            output.append(render_table(table_lines))
            continue

        paragraph.append(line)
        index += 1

    flush_paragraph(); flush_list()
    if in_code:
        output.append(f'<pre><code>{html.escape("\n".join(code_lines))}</code></pre>')
    close_card()
    title_match = re.search(r"^#\s+(.+?)\s*$", source, flags=re.MULTILINE)
    title = title_match.group(1).strip() if title_match else "Research Gap to Idea Report"
    return "\n".join(output), "\n".join(toc)


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("input", type=Path, help="Markdown report")
    parser.add_argument("output", type=Path, help="Standalone HTML output")
    parser.add_argument("--template", type=Path, help="Optional HTML template")
    args = parser.parse_args()

    script_dir = Path(__file__).resolve().parent
    template_path = args.template or script_dir.parent / "assets" / "report-template.html"
    source = args.input.read_text(encoding="utf-8")
    content, toc = render_markdown(source)
    title_match = re.search(r"^#\s+(.+?)\s*$", source, flags=re.MULTILINE)
    title = html.escape(title_match.group(1).strip() if title_match else "Research Gap to Idea Report", quote=True)
    template = template_path.read_text(encoding="utf-8")
    rendered = template.replace("{{TITLE}}", title).replace("{{TOC}}", toc).replace("{{CONTENT}}", content)
    args.output.parent.mkdir(parents=True, exist_ok=True)
    args.output.write_text(rendered, encoding="utf-8")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
