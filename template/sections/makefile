#!/usr/bin/make -f
## makefile (for Elements)
## Mac Radigan

##  Copyright (C)  2017  Mac Radigan.
##  Permission is granted to copy, distribute and/or modify this document
##  under the terms of the GNU Free Documentation License, Version 1.3
##  or any later version published by the Free Software Foundation;
##  with the Invariant Sections being Preface, Publication, Copying, and License, 
##  with the Front-Cover Texts being "for Ashton, Lyla, Neomi, Ruth, and Malakai", 
##  and no Back-Cover Texts.
##  A copy of the license is included in the section entitled "GNU Free 
##  Documentation License".


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
