# Deployment

This project uses GitHub Pages to host dbt documentation.

## How It Works

1. **Clean**: Delete everything in `docs/` folder to ensure a fresh deployment
2. **Generate docs**: `dbt docs generate` creates documentation files in the `target/` folder
3. **Copy & inject GA**: `inject_ga.py` copies files from `target/` to `docs/` and adds Google Analytics tracking
4. **Commit**: Changes to the `docs/` folder are committed to the repository
5. **GitHub Pages**: Configured to build and serve from the `docs/` folder on the `main` branch

## Quick Deployment

Simply run the batch file:

```bash
deploy.bat
```

This automated script will:
- Clean the `docs/` folder
- Generate fresh dbt documentation
- Copy files from `target/` to `docs/`
- Inject Google Analytics tag
- Commit and push to GitHub

## Manual Deployment Steps

If you prefer to run commands individually:

```bash
rmdir /s /q docs
mkdir docs
dbt docs generate
python inject_ga.py
git add docs/
git commit -m "update docs"
git push
```

## Accessing Documentation

Once deployed, documentation is available at your GitHub Pages URL (typically: `https://[username].github.io/[repository-name]/`)

## Google Analytics

The documentation includes Google Analytics tracking (ID: G-XXKMP3JBB6) to monitor usage. The `inject_ga.py` script:
1. Copies required files from `target/` to `docs/` (`index.html`, `catalog.json`, `manifest.json`, `compiled/`, `run/`)
2. Injects the GA tag into the `<head>` section of `docs/index.html`

The GA tag is automatically added during the deployment process, so you never need to manually edit the HTML.
