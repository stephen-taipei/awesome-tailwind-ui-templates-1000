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
    print(f"Total templates to generate: {len(ALL_TEMPLATES)}")

    if len(ALL_TEMPLATES) > 0:
        print(f"First template: {ALL_TEMPLATES[0]['id']}")
        print(f"Last template: {ALL_TEMPLATES[-1]['id']}")

    for tmpl in ALL_TEMPLATES:
        print(f"Processing {tmpl['id']} in {tmpl['dir']}")
        # Create directory if not exists
        os.makedirs(tmpl['dir'], exist_ok=True)

        # File path
        file_path = os.path.join(tmpl['dir'], f"{tmpl['id']}.html")

        # Generate content
        html_content = BASE_HTML.format(
            title=tmpl['title'],
            description=tmpl['description'],
            content=tmpl['content']
        )

        # Write file
        with open(file_path, 'w') as f:
            f.write(html_content)

        print(f"Generated {file_path}")

        # Git operations: Add and Commit
        try:
            subprocess.run(['git', 'add', file_path], check=True)
            # Check if there are changes to commit
            status = subprocess.run(['git', 'status', '--porcelain'], capture_output=True, text=True)
            if status.stdout.strip():
                subprocess.run(['git', 'commit', '-m', f"feat: implement {tmpl['id']} template"], check=True)
                print(f"Committed {tmpl['id']}")
            else:
                print(f"No changes for {tmpl['id']}, skipping commit.")
        except subprocess.CalledProcessError as e:
            print(f"Error processing {tmpl['id']}: {e}")

    # Push all at once at the end
    try:
         print("Pushing all changes to origin dev...")
         subprocess.run(['git', 'push', 'origin', 'dev'], check=True)
         print("All changes pushed successfully.")
    except subprocess.CalledProcessError as e:
         print(f"Error pushing changes: {e}")

if __name__ == "__main__":
    generate_and_push()
