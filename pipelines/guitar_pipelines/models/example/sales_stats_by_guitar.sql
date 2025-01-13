{{ config(materialized='view') }}


with sales_stats_per_guitar as (SELECT artikelnummer, count(*) AS n_listings 
FROM {{ ref('cleaned_sales_data')}} GROUP BY artikelnummer order by n_listings desc)

select * from sales_stats_per_guitar
