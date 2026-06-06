#!/usr/bin/env python3
"""Business Insight renderer — HTML → PDF (headless Chrome).

Usage:
    python3 render_bi.py input.html output.pdf
    python3 render_bi.py input.html              # opens HTML in browser
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
    if len(sys.argv) < 2:
        print("Usage: python3 render_bi.py <input.html> [output.pdf]")
        sys.exit(1)

    html_path = Path(sys.argv[1])
    if not html_path.exists():
        sys.exit(f"File not found: {html_path}")

    if len(sys.argv) >= 3:
        pdf_path = Path(sys.argv[2])
        render_pdf(html_path, pdf_path)
        print(f"PDF: {pdf_path}")
    else:
        print(f"HTML: {html_path}")


if __name__ == "__main__":
    main()
