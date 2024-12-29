{{ config(materialized='table') }}


with listings_per_day as (SELECT date(sales.date) AS date_1, count(*) AS count_1 
FROM sales GROUP BY date(sales.date))

select * from listings_per_day