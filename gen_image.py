from __future__ import annotations

import os
from pathlib import Path
from urllib.request import urlopen
import re

import matplotlib.pyplot as plt

OVERVIEW_URL = "https://raw.githubusercontent.com/AAU-ST2-Programming/all_lectures/main/shared_overview.md"

LECTURE_MAP = {
    "oop_1": 1,
    "oop_2": 2,
    "oop_3": 3,
    "oop_4_workshop": 4,
    "signals_1": 5,
    "signals_2": 6,
    "signals_3": 7,
    "signals_4_workshop": 8,
    "populations_data_1": 9,
    "populations_data_2": 10,
    "populations_data_3": 11,
    "populations_data_4_workshop": 12,
}


def _parse_overview(markdown_text: str) -> tuple[str, str, list[str], list[list[str]]]:
    lines = [line.rstrip() for line in markdown_text.splitlines()]
    title = ""
    subtitle = ""
    table_rows: list[list[str]] = []

    for line in lines:
        if not title and line.startswith("# "):
            title = line[2:].strip()
            continue
        if not subtitle and line.startswith("## "):
            subtitle = line[3:].strip()
            continue

        stripped = line.strip()
        if not (stripped.startswith("|") and stripped.endswith("|")):
            continue

        parts = [part.strip() for part in stripped.split("|")[1:-1]]
        if not parts:
            continue

        if set("".join(parts)).issubset(set("-: ")):
            continue

        table_rows.append(parts)

    if not table_rows:
        raise ValueError("No markdown table found in shared_overview.md")

    header = table_rows[0]
    body = table_rows[1:]
    return title, subtitle, header, body


def _render_overview(title: str, subtitle: str, header: list[str], body: list[list[str]], current_lecture: int | None) -> None:
    fig, ax = plt.subplots(figsize=(16, 9), dpi=220)
    ax.axis("off")

    if title:
        fig.text(0.02, 0.97, title, fontsize=22, weight="bold", ha="left", va="top")
    if subtitle:
        fig.text(0.02, 0.92, subtitle, fontsize=14, ha="left", va="top")

    table = ax.table(
        cellText=body,
        colLabels=header,
        loc="center",
        cellLoc="left",
        colLoc="left",
        bbox=[0.02, 0.05, 0.96, 0.82],
    )
    table.auto_set_font_size(False)
    table.set_fontsize(10)
    table.scale(1, 1.4)

    for (row, col), cell in table.get_celld().items():
        if row == 0:
            cell.set_text_props(weight="bold")
            cell.set_facecolor("#EAEAEA")
        cell.set_edgecolor("#666666")
        cell.PAD = 0.03

    if current_lecture is not None:
        for row_idx, row_values in enumerate(body, start=1):
            first_col_num = re.sub(r"[^0-9]", "", row_values[0])
            if first_col_num and int(first_col_num) == current_lecture:
                for col_idx in range(len(header)):
                    highlight_cell = table[(row_idx, col_idx)]
                    highlight_cell.set_text_props(weight="bold")
                    highlight_cell.set_facecolor("#F5F5F5")
                break

    plt.show()


def _bold_current_lecture_row(header: list[str], body: list[list[str]], current_lecture: int | None) -> list[str]:
    lines = ["| " + " | ".join(header) + " |", "|" + "|".join(["---"] * len(header)) + "|"]

    for row_values in body:
        row_out = row_values[:]
        first_col_num = re.sub(r"[^0-9]", "", row_values[0])
        if current_lecture is not None and first_col_num and int(first_col_num) == current_lecture:
            row_out = [cell if (cell.startswith("**") and cell.endswith("**")) else f"**{cell}**" for cell in row_values]
        lines.append("| " + " | ".join(row_out) + " |")

    return lines


def build_overview_markdown() -> str:
    current_lecture = LECTURE_MAP.get(Path.cwd().name)

    with urlopen(OVERVIEW_URL, timeout=20) as response:
        markdown_text = response.read().decode("utf-8")

    title, subtitle, header, body = _parse_overview(markdown_text)
    table_lines = _bold_current_lecture_row(header, body, current_lecture)

    parts = []
    if title:
        parts.append(f"# {title}")
    if subtitle:
        parts.append("")
        parts.append(f"## {subtitle}")
    parts.append("")
    parts.extend(table_lines)
    return "\n".join(parts)


def show_overview_markdown() -> None:
    from IPython.display import Markdown, display

    display(Markdown(build_overview_markdown()))


def main() -> None:
    mode = os.getenv("OVERVIEW_RENDER_MODE", "markdown").strip().lower()

    if mode == "image":
        current_lecture = LECTURE_MAP.get(Path.cwd().name)
        with urlopen(OVERVIEW_URL, timeout=20) as response:
            markdown_text = response.read().decode("utf-8")
        title, subtitle, header, body = _parse_overview(markdown_text)
        _render_overview(title, subtitle, header, body, current_lecture)
        return

    show_overview_markdown()


if __name__ == "__main__":
    main()
