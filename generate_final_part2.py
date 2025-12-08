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
    all_templates = TEMPLATES_BATCH_10
    total = len(all_templates)
    print(f"Total templates to generate: {total}")

    for index, tmpl in enumerate(all_templates):
        print(f"[{index+1}/{total}] Processing {tmpl['id']}...")

        # Create directory
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

        # Git operations (optional, can be done in batch at the end if desired, but here per file as requested)
        try:
            subprocess.run(['git', 'add', file_path], check=True)
            # Use specific commit message
            subprocess.run(['git', 'commit', '-m', f"feat: implement {tmpl['id']} template"], check=True)
            # Push every 10 commits to avoid too many push operations or push failures blocking everything
            if (index + 1) % 10 == 0:
                print("Pushing to remote...")
                subprocess.run(['git', 'push', 'origin', 'dev'], check=True)
        except subprocess.CalledProcessError as e:
            print(f"Error processing {tmpl['id']}: {e}")

    # Final push
    try:
        subprocess.run(['git', 'push', 'origin', 'dev'], check=True)
    except subprocess.CalledProcessError as e:
        print(f"Final push failed: {e}")

if __name__ == "__main__":
    generate_and_push_batch_10()
