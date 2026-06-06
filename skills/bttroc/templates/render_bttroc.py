#!/usr/bin/env python3
"""BTTROC renderer — HTML → PDF (headless Chrome).

Usage:
    python3 render_bttroc.py input.html output.pdf
"""

import subprocess
import sys
from pathlib import Path


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
        print(f"Usage: {sys.argv[0]} input.html output.pdf", file=sys.stderr)
        sys.exit(1)

    html_path = Path(sys.argv[1])
    pdf_path = Path(sys.argv[2])

    if not html_path.exists():
        sys.exit(f"File not found: {html_path}")

    render_pdf(html_path, pdf_path)
    print(f"PDF: {pdf_path}")


if __name__ == "__main__":
    main()
