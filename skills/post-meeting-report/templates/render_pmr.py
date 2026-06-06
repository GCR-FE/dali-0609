#!/usr/bin/env python3
"""Post-Meeting Report renderer — HTML + PDF (headless Chrome)."""

import json
import subprocess
import sys
from pathlib import Path

from jinja2 import Environment, FileSystemLoader

TEMPLATE_DIR = Path(__file__).parent
TEMPLATE_FILE = "post-meeting-report.html.j2"


def render_html(data: dict, output_path: Path) -> Path:
    env = Environment(loader=FileSystemLoader(str(TEMPLATE_DIR)))
    template = env.get_template(TEMPLATE_FILE)
    html = template.render(**data)
    output_path.write_text(html, encoding="utf-8")
    return output_path


def render_pdf(html_path: Path, pdf_path: Path) -> Path:
    chrome = next(
        (p for p in [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/usr/bin/google-chrome",
            "/usr/bin/chromium-browser",
        ] if Path(p).exists()),
        None,
    )
    if not chrome:
        sys.exit("Chrome not found — install Google Chrome for PDF export.")

    subprocess.run(
        [chrome, "--headless", "--disable-gpu", "--no-pdf-header-footer",
         f"--print-to-pdf={pdf_path}", str(html_path)],
        check=True, capture_output=True,
    )
    return pdf_path


def main():
    if len(sys.argv) < 2:
        print("Usage: python3 render_pmr.py <output.[html|pdf]> [data.json]")
        sys.exit(1)

    output = Path(sys.argv[1])
    data_file = Path(sys.argv[2]) if len(sys.argv) > 2 else TEMPLATE_DIR / "sample_data.json"

    data = json.loads(data_file.read_text(encoding="utf-8"))

    if output.suffix == ".pdf":
        html_tmp = output.with_suffix(".html")
        render_html(data, html_tmp)
        render_pdf(html_tmp, output)
        print(f"PDF: {output}")
    else:
        render_html(data, output)
        print(f"HTML: {output}")


if __name__ == "__main__":
    main()
