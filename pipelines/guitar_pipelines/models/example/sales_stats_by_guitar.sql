{{ config(materialized='view') }}


with sales_stats_per_guitar as (
    select
        artikelnummer,
        count(*) as n_listings
    from {{ ref('cleaned_sales_data') }}
    group by artikelnummer
    order by n_listings desc
)

select * from sales_stats_per_guitar
