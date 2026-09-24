import os
import subprocess
import shutil

# Import definitions
from definitions_team import TEMPLATES_TEAM_NEW
from definitions_landing import TEMPLATES_LANDING_NEW

# Base HTML template
BASE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <title>{title} - Awesome Tailwind UI Templates</title>
  <meta name="description" content="{description}">
  <script src="https://stephen.taipei/tailwindcss-browser.js"></script>
  <style type="text/tailwindcss">
    @theme {{
      --color-primary-50: #eff6ff;
      --color-primary-100: #dbeafe;
      --color-primary-200: #bfdbfe;
      --color-primary-300: #93c5fd;
      --color-primary-400: #60a5fa;
      --color-primary-500: #3b82f6;
      --color-primary-600: #2563eb;
      --color-primary-700: #1d4ed8;
      --color-primary-800: #1e40af;
      --color-primary-900: #1e3a8a;
      --color-primary-950: #172554;
    }}
  </style>
</head>
<body class="bg-gray-50 text-slate-900">
  {content}
</body>
</html>"""

ALL_TEMPLATES = []
ALL_TEMPLATES.extend(TEMPLATES_TEAM_NEW)
ALL_TEMPLATES.extend(TEMPLATES_LANDING_NEW)

def generate_and_push():
    """Generate into an explicit output directory; never stage, commit, or push."""
    from scripts.legacy import generate_templates
    generate_templates(ALL_TEMPLATES, BASE_HTML)


if __name__ == "__main__":
    generate_and_push()
