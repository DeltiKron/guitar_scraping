{{ config(materialized='view') }}


with listings_per_manufacturer as (SELECT manufacturer_id, sum(n_listings) AS n_listings 
FROM {{ ref('daywise_manufacturer_count')}} GROUP BY manufacturer_id order by n_listings desc)

select * from listings_per_manufacturer