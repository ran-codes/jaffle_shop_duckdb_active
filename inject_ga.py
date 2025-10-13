"""
Copy dbt docs from target/ to docs/ and inject Google Analytics tag
"""
import re
import shutil
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

def copy_dbt_docs(source_dir: Path, dest_dir: Path):
    """Copy necessary files from target/ to docs/"""
    required_files = ['index.html', 'catalog.json', 'manifest.json']
    required_dirs = ['compiled', 'run']

    print(f"Copying dbt docs from {source_dir} to {dest_dir}...")

    # Create destination directory if it doesn't exist
    dest_dir.mkdir(exist_ok=True)

    # Copy required files
    for filename in required_files:
        source_file = source_dir / filename
        if source_file.exists():
            shutil.copy2(source_file, dest_dir / filename)
            print(f"  Copied {filename}")
        else:
            print(f"  Warning: {filename} not found in {source_dir}")

    # Copy required directories
    for dirname in required_dirs:
        source_subdir = source_dir / dirname
        dest_subdir = dest_dir / dirname
        if source_subdir.exists():
            if dest_subdir.exists():
                shutil.rmtree(dest_subdir)
            shutil.copytree(source_subdir, dest_subdir)
            print(f"  Copied {dirname}/")

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
    # Define paths
    target_dir = Path("target")
    docs_dir = Path("docs")

    # Copy files from target/ to docs/
    copy_dbt_docs(target_dir, docs_dir)

    # Inject GA tag into docs/index.html
    docs_index = docs_dir / "index.html"
    inject_ga_tag(docs_index)

    print("\nDone! docs/ folder is ready for GitHub Pages deployment.")
