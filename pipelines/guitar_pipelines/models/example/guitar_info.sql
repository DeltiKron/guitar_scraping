{{
  config(materialized='table')
}}

with guitars as ( select * from {{ source('main','guitars') }} left join {{ source('main', 'manufacturers')}} m on hersteller_id = m.id) 
select 
    artikelnummer,
    {{ clean_guitar_name('modell') }} as guitar_name,
    bauweise as construction_style,
    CAST(cutaway as bool) as has_cutaway, 
    farbe as color, 
    griffbrett as wood_fretboard, 
    cast(koffer as bool) as has_case, 
    date(erhaeltlich_seit) as available_since, 
    cast(buende as int) as number_of_frets, 
    {{ clean_wood('holz_decke') }} as wood_top,
    {{ clean_wood('holz_boden_zargen') }} as wood_back_sides,
    name as manufacturer_name 
from guitars
