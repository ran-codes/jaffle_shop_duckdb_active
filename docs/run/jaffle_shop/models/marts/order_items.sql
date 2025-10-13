
      create or replace view "dev"."external"."order_items__dbt_int" as (
        select * from read_parquet('_server\dev/order_items.parquet', union_by_name=False)
        -- if relation is empty, filter by all columns having null values
        
      );
    