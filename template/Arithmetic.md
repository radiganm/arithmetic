{# Mac Radigan #}
{% include 'header.md' %}

# Multiplication

{% for k_n in dat.items() %}
## The Number {{k_n[0]}}

  {% for factors in k_n[1]['factor_list'] %}
### Factor {{k_n[1]['factor_expression']}}
  {% endfor %}

{% endfor %}

{# *EOF* #}
