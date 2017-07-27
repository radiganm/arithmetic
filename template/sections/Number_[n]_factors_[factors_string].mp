%% Number_{{n}}_factors_{{factors_string}}.mp
%% Mac Radigan
  
  outputtemplate := "figures/%j.mps";

  beginfig(1)

    %% unit
    M.0 = {{n}};
    f.0 = 1;
    u.0 = 1mm;
    s.0 = 2;
    h.0 = u.0*s.0*2*sqrt(1-1/4);
    w.0 = u.0*s.0*1;
    pair A,B,C;
    C = +1/2*h.0*up;
    A = C shifted (+1/2*w.0,-1/2*h.0);
    B = C shifted (-1/2*w.0,-1/2*h.0);
    picture picU ;
    picU:=nullpicture;
    addto picU doublepath A--B--C--cycle withpen currentpen;
    addto picU doublepath A withpen pencircle scaled 2bp;
    addto picU doublepath B withpen pencircle scaled 2bp;
    addto picU doublepath C withpen pencircle scaled 2bp;
    
    %% tesselation
    draw picU;
    for m=0 upto M.0-1:
      for n=-m upto -1:
        draw picU shifted(n*w.0+m*1/2*w.0, m*1/2*-h.0) withcolor {{colors[0]}};
      endfor;
      for n=1 upto +m:
        draw picU shifted(n*w.0-m*1/2*w.0, m*1/2*-h.0) withcolor {{colors[0]}};
      endfor;
    endfor;

{% set ko = 0 %}
{% for kx, factor in enumerate(factors) %}
  {% if factor != -1 %}
    {% set k = kx + 1 %}
    {% set symA = gensym_alpha(3) %}
    {% set symB = gensym_alpha(3) %}
    {% set symC = gensym_alpha(3) %}
    {% set symP = 'pic'+gensym_alpha(1) %}

    %% factor {{factor}} - {{k}}
    f.{{k}} = {{factor}};
    r.{{k}} = f.{{k-1}};
    M.{{k}} = M.{{k-1}}/(f.{{k}});
    s.{{k}} = s.{{k-1}} * f.{{k}};
    h.{{k}} = u.0*s.{{k}}*2*sqrt(1-1/4);
    w.{{k}} = u.0*s.{{k}}*1;
    pair {{symA}},{{symB}},{{symC}};
    {{symA}} = (1/2)*(h.0)*up;
    {{symB}} = C shifted (+1/2*w.{{k}},-1/2*h.{{k}});
    {{symC}} = C shifted (-1/2*w.{{k}},-1/2*h.{{k}});
    picture {{symP}};
    {{symP}}:=nullpicture;
    addto {{symP}} doublepath {{symA}}--{{symB}}--{{symC}}--cycle withpen currentpen;
    addto {{symP}} doublepath {{symA}} withpen pencircle scaled 2bp;
    addto {{symP}} doublepath {{symB}} withpen pencircle scaled 2bp;
    addto {{symP}} doublepath {{symC}} withpen pencircle scaled 2bp;

    %% factorization {{k}} using {{factor}}
    draw {{symP}} withcolor {{colors[k]}};
    for m=0 upto M.{{k}}-1:
      for n=-m upto -1:
        draw {{symP}} shifted(n*w.{{k}}+m*1/2*w.{{k}}, m*1/2*-h.{{k}}) withcolor {{colors[k]}};
      endfor;
      for n=1 upto +m:
        draw {{symP}} shifted(n*w.{{k}}-m*1/2*w.{{k}}, m*1/2*-h.{{k}}) withcolor {{colors[k]}};
      endfor;
    endfor;

  {% endif %}
{% endfor %}

    clip currentpicture to (-4cm,-4cm)--(4cm,-4cm)--(4cm,4cm)--(-4cm,4cm)--cycle;
  endfig;

  bye;

%% *EOF*

{# *EOF* #}
