#!/usr/bin/make -f
## makefile (for Elements)
## Mac Radigan

.PHONY: default init null

.DEFAULT_GOAL := default

figures  = ./figures

vpath %.mp .
VPATH = .

MP_FILES = \
{% for k_n in dat.items() %}{% for factors in k_n[1]['factor_list'] %}  Number_{{k_n[0]}}_factors_{{k_n[1]['factor_string']}}.pdf \
{% endfor %} {% endfor %}  null

PDF_FILES = $(MP_FILES:.mp=.pdf)

default: $(PDF_FILES)

null:

%.mps: %.mp
	mpost $(basename $<)

%.pdf: %.mps init
	epstopdf --outfile=$(figures)/$@ $(figures)/$<

init:
	mkdir -p $(figures)

## *EOF*
