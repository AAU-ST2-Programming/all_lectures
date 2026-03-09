from pathlib import Path
import textwrap

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "shared_overview.csv"
HTML_PATH = BASE_DIR / "shared_overview_table.html"
PNG_PATH = BASE_DIR / "shared_overview_table.png"
CURRENT_LECTURE = 10


def build_df() -> pd.DataFrame:
    return pd.read_csv(CSV_PATH, sep="|")


def build_html(df: pd.DataFrame) -> str:
    styled = df.style.set_uuid("shared_overview").apply(
        lambda row: ["font-weight: 1000"] * len(row)
        if row["#"] == CURRENT_LECTURE
        else [""] * len(row),
        axis=1,
    ).hide(axis="index")
    return styled.to_html()


def write_if_changed(output_path: Path, content: str) -> bool:
    if output_path.exists():
        existing = output_path.read_text(encoding="utf-8")
        if existing == content:
            return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    df = build_df()
    html_content = build_html(df)
    changed = write_if_changed(HTML_PATH, html_content)
    png_missing = not PNG_PATH.exists()
    png_stale = False
    if not png_missing:
        png_mtime = PNG_PATH.stat().st_mtime
        csv_mtime = CSV_PATH.stat().st_mtime
        script_mtime = Path(__file__).stat().st_mtime
        png_stale = png_mtime < max(csv_mtime, script_mtime)

    if changed:
        print(f"Updated {HTML_PATH}")
    else:
        print(f"No changes in {HTML_PATH}")

    if changed or png_missing or png_stale:
        if png_missing and not changed:
            print(f"Created {PNG_PATH}")
        elif png_stale and not changed:
            print(f"Refreshed {PNG_PATH}")
        else:
            print(f"Updated {PNG_PATH}")


if __name__ == "__main__":
    main()
