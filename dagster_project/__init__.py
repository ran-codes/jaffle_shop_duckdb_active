from dagster import AssetExecutionContext, Definitions
from dagster_dbt import DbtCliResource, DbtProject, dbt_assets
from pathlib import Path

DBT_PROJECT_DIR = Path(__file__).parent.parent

dbt_project = DbtProject(
    project_dir=DBT_PROJECT_DIR,
    target="dev",
)

@dbt_assets(
    manifest=dbt_project.manifest_path,
    project=dbt_project,
)
def jaffle_shop_dbt_assets(context: AssetExecutionContext, dbt: DbtCliResource):
    yield from dbt.cli(["build"], context=context).stream()

defs = Definitions(
    assets=[jaffle_shop_dbt_assets],
    resources={"dbt": DbtCliResource(project_dir=DBT_PROJECT_DIR)},
)