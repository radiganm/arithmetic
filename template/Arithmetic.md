{# Mac Radigan #}
{% include 'header.md' %}

# Multiplication

{% for n_k in dat.items() %}
## The Number {{n_k[0]}}

  {% for k_k in n_k[1].items() %}
### Factor {{k_k[1]['factor_expression']}} , factors {{k_k[1]['factors_string']}}

\resizebox{6in}{!}{\includegraphics{output/sections/figures/Number_{{n_k[0]}}_factors_{{k_k[1]['factors_string']}}}}

  {% endfor %}

{% endfor %}

{# *EOF* #}
