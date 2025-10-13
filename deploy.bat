@echo off
echo ============================================
echo Deploying dbt docs to GitHub Pages
echo ============================================

echo.
echo Step 1: Cleaning docs folder...
if exist docs (
    rmdir /s /q docs
    echo   Deleted docs folder
)
mkdir docs
echo   Created clean docs folder

echo.
echo Step 2: Generating dbt documentation...
dbt docs generate
if errorlevel 1 (
    echo   Error: dbt docs generate failed!
    exit /b 1
)
echo   Documentation generated in target/

echo.
echo Step 3: Copying docs and injecting Google Analytics...
python inject_ga.py
if errorlevel 1 (
    echo   Error: inject_ga.py failed!
    exit /b 1
)


echo.
echo ============================================
echo Deployment staged - please commit and push the changes to Deploy
echo ============================================
