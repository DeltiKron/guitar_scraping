
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with sales_stats as (
select count(*) as n_listings, max(day) as max_date, min(day) as min_date, timediff(max(day), min(day)) as time_covered, artikelnummer from {{ ref('cleaned_sales_data')}} group by artikelnummer),


data_availability as (
    select s.artikelnummer, s.n_listings,  s.min_date, s.max_date, time_covered
    from {{ source('main','guitars')}} as g
    left join sales_stats as s on g.artikelnummer == s.artikelnummer
)

select *
from data_availability

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
