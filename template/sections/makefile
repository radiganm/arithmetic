#!/usr/bin/make -f
## makefile (for Elements)
## Mac Radigan

.PHONY: default init null

.DEFAULT_GOAL := default

figures  = ./figures

vpath %.mp .
VPATH = .

MP_FILES = \
{% for n_k in dat.items() %}{% for k_k in n_k[1].items() %}  Number_{{n_k[0]}}_factors_{{k_k[1]['factors_string']}}.pdf \
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
