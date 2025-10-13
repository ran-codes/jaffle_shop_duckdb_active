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
if not exist docs (
    mkdir docs
)
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
echo Step 3: Copying all files from target/ to docs/...
xcopy /E /I /Y target\* docs\
echo   Copied all target/ contents to docs/

echo.
echo Step 4: Injecting Google Analytics tag...
python inject_ga.py
if errorlevel 1 (
    echo   Error: inject_ga.py failed!
    exit /b 1
)
 
echo.
echo ============================================
echo Deployment staged - you can now commit and push to deploy
echo ============================================
