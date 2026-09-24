import os
import subprocess
from definitions_batch_10 import TEMPLATES_BATCH_10

BASE_HTML = """<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>{title}</title>
    <meta name="description" content="{description}">
    <script src="https://cdn.tailwindcss.com"></script>
    <script>
        tailwind.config = {{
            theme: {{
                extend: {{
                    colors: {{
                        clifford: '#da373d',
                    }}
                }}
            }}
        }}
    </script>
</head>
<body class="bg-gray-50">
    {content}
</body>
</html>"""

def generate_and_push_batch_10():
    """Generate into an explicit output directory; never stage, commit, or push."""
    from scripts.legacy import generate_templates
    generate_templates(TEMPLATES_BATCH_10, BASE_HTML)


if __name__ == "__main__":
    generate_and_push_batch_10()
