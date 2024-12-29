
/*
    Welcome to your first dbt model!
    Did you know that you can also configure models directly within SQL files?
    This will override configurations stated in dbt_project.yml

    Try changing "table" to "view" below
*/

{{ config(materialized='table') }}

with sales_stats as (
select count(*) as n_listings, max(date) as max_date, min(date) as min_date, timediff(max(date), min(date)) as time_covered, artikelnummer from sales group by artikelnummer),


data_availability as (
    select g.artikelnummer, s.n_listings,  s.min_date, s.max_date, time_covered
    from gitarren as g
)

select *
from data_availability

/*
    Uncomment the line below to remove records with null `id` values
*/

-- where id is not null
