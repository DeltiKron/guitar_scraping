{{ config(materialized='view') }}


with listings_per_day as (
    select
        day,
        count(*) as n_listings
    from {{ ref('cleaned_sales_data') }}
    group by day
    order by n_listings asc
)

select * from listings_per_day
