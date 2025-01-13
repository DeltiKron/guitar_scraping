{{ config(materialized='view') }}


with listings_per_manufacturer as (
    select
        manufacturer_id,
        sum(n_listings) as n_listings
    from {{ ref('daywise_manufacturer_count') }}
    group by manufacturer_id
    order by n_listings desc
)

select * from listings_per_manufacturer
