{% macro clean_guitar_name(column_name) %}
{% set manufacturer_names = dbt_utils.get_column_values(table=source('main','manufacturers'), column='name') %}
{% for _ in manufacturer_names %}Replace({% endfor %}{{ column_name }}{% for pattern in manufacturer_names %},'{{ pattern }}',''){% endfor %}
{% endmacro %}