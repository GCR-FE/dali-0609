#!/usr/bin/env python3
"""
EP Renderer — fills the Jinja2 template with structured data and outputs HTML or PDF.

Usage:
    python render_ep.py input.json output.html
    python render_ep.py input.json output.pdf

Input: JSON file with the EP data structure (see sample_data.json).
Output: Rendered HTML or PDF file (determined by extension).

PDF generation uses headless Chrome/Chromium for stable output.
"""

import json
import os
import platform
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

try:
    from jinja2 import Environment, FileSystemLoader
except ImportError:
    print("ERROR: jinja2 not installed. Run: pip install jinja2", file=sys.stderr)
    sys.exit(1)


def render_ep(data: dict, template_dir: str = None) -> str:
    """Render EP data into HTML string."""
    if template_dir is None:
        template_dir = str(Path(__file__).parent)

    env = Environment(
        loader=FileSystemLoader(template_dir),
        autoescape=True
    )
    template = env.get_template("engagement-plan.html.j2")
    return template.render(**data)


def find_chrome():
    """Find Chrome/Chromium executable on the system."""
    system = platform.system()

    if system == "Darwin":
        candidates = [
            "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
            "/Applications/Chromium.app/Contents/MacOS/Chromium",
            "/Applications/Google Chrome Canary.app/Contents/MacOS/Google Chrome Canary",
        ]
    elif system == "Linux":
        candidates = [
            "google-chrome",
            "google-chrome-stable",
            "chromium",
            "chromium-browser",
        ]
    elif system == "Windows":
        candidates = [
            os.path.expandvars(r"%ProgramFiles%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%ProgramFiles(x86)%\Google\Chrome\Application\chrome.exe"),
            os.path.expandvars(r"%LocalAppData%\Google\Chrome\Application\chrome.exe"),
        ]
    else:
        candidates = []

    for candidate in candidates:
        if os.path.isfile(candidate):
            return candidate
        found = shutil.which(candidate)
        if found:
            return found

    return None


def html_to_pdf(html_content: str, output_path: str) -> None:
    """Convert HTML to PDF using headless Chrome."""
    chrome = find_chrome()
    if not chrome:
        print("ERROR: Chrome/Chromium not found. Install Chrome or use .html output.", file=sys.stderr)
        sys.exit(1)

    tmp_html = tempfile.NamedTemporaryFile(suffix=".html", delete=False, mode="w", encoding="utf-8")
    try:
        tmp_html.write(html_content)
        tmp_html.close()

        cmd = [
            chrome,
            "--headless",
            "--disable-gpu",
            "--no-sandbox",
            "--disable-software-rasterizer",
            "--run-all-compositor-stages-before-draw",
            "--virtual-time-budget=5000",
            "--window-size=1280,900",
            f"--print-to-pdf={output_path}",
            "--print-to-pdf-no-header",
            "--no-pdf-header-footer",
            tmp_html.name,
        ]

        result = subprocess.run(cmd, capture_output=True, text=True, timeout=30)
        if result.returncode != 0:
            stderr = result.stderr.strip()
            if not os.path.exists(output_path):
                print(f"ERROR: Chrome PDF generation failed.\n{stderr}", file=sys.stderr)
                sys.exit(1)
    finally:
        os.unlink(tmp_html.name)


def main():
    if len(sys.argv) < 3:
        print(f"Usage: {sys.argv[0]} input.json output.html|pdf", file=sys.stderr)
        sys.exit(1)

    input_path = sys.argv[1]
    output_path = sys.argv[2]
    ext = Path(output_path).suffix.lower()

    with open(input_path, 'r', encoding='utf-8') as f:
        data = json.load(f)

    html = render_ep(data)

    if ext == ".pdf":
        html_to_pdf(html, output_path)
    else:
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(html)

    print(f"✅ Rendered: {output_path}")


if __name__ == "__main__":
    main()
