{{ config(materialized='table') }}

with average_prices as (
    select
        sales.artikelnummer,
        AVG(preis) as preis,
        AVG(verkaufsrang) as verkaufsrang,
        DATE(date) as day
    from {{ source('main','sales') }}
    group by day, artikelnummer
    order by date asc, artikelnummer asc
),

distinct_sales as (
    select distinct
        artikelnummer,
        DATE(date) as day
    from {{ source('main','sales') }}
    order by date asc, artikelnummer asc
),

cleaned_sales_data as (
    select
        s.day,
        preis,
        verkaufsrang,
        CAST(s.artikelnummer as bigint) as artikelnummer
    from distinct_sales as s
    left join
        average_prices as a
        on s.artikelnummer = a.artikelnummer and s.day = a.day
)


select * from cleaned_sales_data
