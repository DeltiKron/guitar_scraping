{{
  config(materialized='table')
}}

with guitars as ( select * from {{ source('main','guitars') }} left join {{ source('main', 'manufacturers')}} m on hersteller_id = m.id) 
select artikelnummer, modell as guitar_name, bauweise as construction_style, CAST(cutaway as bool) as has_cutaway, farbe as color, griffbrett as fretboard_wood, cast(koffer as bool) as has_case, tonabnehmer as pickup, date(erhaeltlich_seit) as available_since, cast(buende as int) as number_of_frets, holz_decke as wood_top, holz_boden_zargen as wood_back_sides,  name as manufacturer_name from guitars
