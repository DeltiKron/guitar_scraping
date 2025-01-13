{% macro clean_wood(column_name) %}
    Replace(
    {% set patterns=[', Massiv', ' Massiv', 'Massiv', ',Massiv',', massiv', ' massiv', 'massiv', ',massiv'] %}
{% for _ in patterns %}
    Replace(
{% endfor %}{{ column_name }}{% for pattern in patterns %}
    ,'{{ pattern }}','')
{% endfor %},
    'RotFichte', 'Rotfichte')

{% endmacro %}
