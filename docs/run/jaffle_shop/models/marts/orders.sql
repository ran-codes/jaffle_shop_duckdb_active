
      create or replace view "dev"."external"."orders__dbt_int" as (
        select * from read_parquet('_server\dev/orders.parquet', union_by_name=False)
        -- if relation is empty, filter by all columns having null values
        
      );
    