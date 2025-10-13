"""
Inject Google Analytics tag into dbt docs index.html
"""
import re
from pathlib import Path

# Google Analytics tag
GA_TAG = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-XXKMP3JBB6"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());

  gtag('config', 'G-XXKMP3JBB6');
</script>"""

def inject_ga_tag(index_path: Path):
    """Inject GA tag into the <head> section of index.html"""
    if not index_path.exists():
        print(f"Error: {index_path} not found")
        return False

    # Read the file
    content = index_path.read_text(encoding='utf-8')

    # Check if GA tag already exists
    if 'gtag' in content and 'G-XXKMP3JBB6' in content:
        print("GA tag already present in index.html")
        return True

    # Inject GA tag right after <head>
    updated_content = re.sub(
        r'(<head>)',
        r'\1\n' + GA_TAG,
        content,
        count=1
    )

    if updated_content == content:
        print("Error: Could not find <head> tag in index.html")
        return False

    # Write the updated content
    index_path.write_text(updated_content, encoding='utf-8')
    print(f"Successfully injected GA tag into {index_path}")
    return True

if __name__ == "__main__":
    # Inject GA tag into docs/index.html
    docs_index = Path("docs/index.html")

    if inject_ga_tag(docs_index):
        print("Done! GA tag injected successfully.")
    else:
        print("Failed to inject GA tag.")
        exit(1)
