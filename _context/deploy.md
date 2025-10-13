# Deployment

This project uses GitHub Pages to host dbt documentation.

## How It Works

1. **Clean**: Delete everything in `docs/` folder to ensure a fresh deployment
2. **Generate docs**: `dbt docs generate` creates documentation files in the `target/` folder
3. **Copy**: Copy all files from `target/` to `docs/` using xcopy
4. **Inject GA**: `inject_ga.py` adds Google Analytics tracking to `docs/index.html`
5. **Commit**: Changes to the `docs/` folder are committed to the repository
6. **Push**: Push to GitHub
7. **GitHub Pages**: Configured to build and serve from the `docs/` folder on the `main` branch

## Quick Deployment

Simply run the batch file:

```bash
deploy.bat
```

This automated script will:
- Clean the `docs/` folder
- Generate fresh dbt documentation in `target/`
- Copy all files from `target/` to `docs/`
- Inject Google Analytics tag into `docs/index.html`
- Commit and push to GitHub

## Manual Deployment Steps

If you prefer to run commands individually:

```bash
rmdir /s /q docs
mkdir docs
dbt docs generate
xcopy /E /I /Y target\* docs\
python inject_ga.py
git add docs/
git commit -m "update docs"
git push
```

## Accessing Documentation

Once deployed, documentation is available at your GitHub Pages URL (typically: `https://[username].github.io/[repository-name]/`)

## Google Analytics

The documentation includes Google Analytics tracking (ID: G-XXKMP3JBB6) to monitor usage.

**Separation of Concerns:**
- **`deploy.bat`** (Step 3): Handles copying all files from `target/` to `docs/` using `xcopy`
- **`inject_ga.py`** (Step 4): Only responsible for injecting the GA tag into `docs/index.html`

The GA tag is automatically added during the deployment process, so you never need to manually edit the HTML.
