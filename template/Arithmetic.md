{# Arithmetic.md #}
{# Mac Radigan #}

{#  Copyright 2017  Mac Radigan.                                                   #}
{#  Permission is granted to copy, distribute and/or modify this document          #}
{#  under the terms of the GNU Free Documentation License, Version 1.3             #}
{#  or any later version published by the Free Software Foundation;                #}
{#  with the Invariant Sections being Preface, Publication, Copying, and License,  #}
{#  with the Front-Cover Texts being "for Ashton, Lyla, Neomi, Ruth, and Malakai", #}
{#  and no Back-Cover Texts.                                                       #}
{#  A copy of the license is included in the section entitled "GNU Free            #}
{#  Documentation License".                                                        #}

{% include 'header.md' %}

\newpage

# Preface

\begin{center}
{{INVARIANT_PREFACE}}
\end{center}

\newpage

# Publication

\begin{center}
{{INVARIANT_PUBLICATION}}
\end{center}

\newpage

# Copying

{% include 'COPYING' %}

\newpage

# Multiplication

{% for n_k in dat.items() %}
## The Number {{n_k[0]}}

  {% for k_k in n_k[1].items() %}
### Product {{k_k[1]['factor_expression']}}

\resizebox{6in}{!}{\includegraphics{output/sections/figures/Number_{{n_k[0]}}_factors_{{k_k[1]['factors_string']}}}}

  {% endfor %}

{% endfor %}

\newpage

# LICENSE

{% include 'LICENSE' %}

{# *EOF* #}
