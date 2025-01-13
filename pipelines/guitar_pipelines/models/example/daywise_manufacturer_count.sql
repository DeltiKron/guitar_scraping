{{ config(materialized='table') }}


with date_records as (
SELECT day,
    m.name as manufacturer_name,
    m.id
 
FROM {{ ref("cleaned_sales_data") }} as s
left join {{ source('main','guitars')}} as g on g.artikelnummer == s.artikelnummer
left join {{ source('main','manufacturers')}} as m on g.hersteller_id == m.id
),
 daywise_manufacturer_count as (
 select count(*) as n_listings, day, manufacturer_name, id as manufacturer_id from date_records
 group by day, manufacturer_name 
 order by n_listings desc 
 )

select * from daywise_manufacturer_count