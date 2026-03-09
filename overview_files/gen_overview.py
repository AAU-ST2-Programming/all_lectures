from pathlib import Path

import pandas as pd

BASE_DIR = Path(__file__).resolve().parent
CSV_PATH = BASE_DIR / "shared_overview.csv"
HTML_PATH_TEMPLATE = "shared_overview_table{table_name}.html"

def build_df() -> pd.DataFrame:
    return pd.read_csv(CSV_PATH, sep="|")


def build_html(df: pd.DataFrame) -> dict[int, str]:
    html_by_index: dict[int, str] = {}
    for i in range(1, len(df) + 1):
        styled = df.style.set_uuid("shared_overview").apply(
            lambda row: ["font-weight: 1000"] * len(row)
            if row["#"] == i
            else [""] * len(row),
            axis=1,
        ).hide(axis="index")
        html_by_index[i] = styled.to_html()
    return html_by_index


def path_from_template(table_name: str) -> Path:
    return BASE_DIR / HTML_PATH_TEMPLATE.format(table_name=table_name)


def write_if_changed(output_path: Path, content: dict[str,str]) -> bool:
    if output_path.exists():
        existing = output_path.read_text(encoding="utf-8")
        if existing == content:
            return False

    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return True


def main() -> None:
    df = build_df()
    html_by_index = build_html(df)

    for i, html_content in html_by_index.items():
        table_name = str(i)
        html_path = path_from_template(table_name)
        changed = write_if_changed(html_path, html_content)

        if changed:
            print(f"Updated {html_path}")
        else:
            print(f"No changes in {html_path}")



if __name__ == "__main__":
    main()
