
      create or replace view "dev"."external"."locations__dbt_int" as (
        select * from read_parquet('_server\dev/locations.parquet', union_by_name=False)
        -- if relation is empty, filter by all columns having null values
        
      );
    