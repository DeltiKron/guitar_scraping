{{ config(materialized='view') }}


with listings_per_day as (SELECT day, count(*) AS n_listings 
FROM {{ ref('cleaned_sales_data')}} GROUP BY day order by n_listings asc)

select * from listings_per_day