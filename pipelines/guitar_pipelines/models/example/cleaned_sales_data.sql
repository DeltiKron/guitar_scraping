{{ config(materialized='table') }}

with average_prices as (select AVG(preis) as preis, AVG(verkaufsrang) as verkaufsrang, date(date) as day, sales.artikelnummer from {{ source('main','sales')}} group by day, artikelnummer
 order by date asc, artikelnummer asc), 

distinct_sales as (
SELECT distinct date(date) as day, artikelnummer from {{ source('main','sales')}} order by date asc, artikelnummer asc),

cleaned_sales_data as (
select s.day, CAST(s.artikelnummer as bigint) as artikelnummer, preis, verkaufsrang from distinct_sales s left join average_prices a on a.artikelnummer = s.artikelnummer and a.day = s.day
)


select * from cleaned_sales_data