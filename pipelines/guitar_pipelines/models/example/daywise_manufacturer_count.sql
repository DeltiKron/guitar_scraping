{{ config(materialized='table') }}


with date_records as (
SELECT date(s.date) AS date_1,
    m.name as manufacturer_name,
    m.id
 
FROM sales as s
left join guitars as g on g.artikelnummer == s.artikelnummer
left join manufacturers as m on g.hersteller_id == m.id
),
 daywise_manufacturer_count as (
 select count(*) as n_listings, date_1 as date, manufacturer_name, id as manufacturer_id from date_records
 group by date, manufacturer_name 
 order by n_listings desc 
 )

select * from daywise_manufacturer_count