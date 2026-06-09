#!/usr/bin/env python3
"""Solutions Search renderer — JSON → HTML (Jinja2) → PDF (headless Chrome).

Usage:
    python3 render_ss.py input.json output.html
    python3 render_ss.py input.json output.html output.pdf
"""

import json
import subprocess
import sys
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)


def render_html(data: dict, template_dir: str = None) -> str:
    if template_dir is None:
        template_dir = str(Path(__file__).parent)
    env = Environment(loader=FileSystemLoader(template_dir), autoescape=True)
    template = env.get_template("solutions-search.html.j2")
    return template.render(**data)


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
         f"--print-to-pdf={pdf_path}", str(html_path.resolve())],
        check=True, capture_output=True,
    )
    return pdf_path


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html [output.pdf]", file=sys.stderr)
        sys.exit(1)

    input_path = Path(sys.argv[1])
    output_html = Path(sys.argv[2])

    if not input_path.exists():
        sys.exit(f"File not found: {input_path}")

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = render_html(data)
    with open(output_html, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"HTML: {output_html}")

    if len(sys.argv) >= 4:
        pdf_path = Path(sys.argv[3])
        render_pdf(output_html, pdf_path)
        print(f"PDF: {pdf_path}")


if __name__ == "__main__":
    main()
