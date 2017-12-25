#!/usr/bin/make -f
### makefile (for modularity)
### Copyright 2017 Mac Radigan
### SPDX-License-Identifier: GFDL-1.3

##  Copyright (C)  2017  Mac Radigan.
##  Permission is granted to copy, distribute and/or modify this document
##  under the terms of the GNU Free Documentation License, Version 1.3
##  or any later version published by the Free Software Foundation;
##  with no Invariant Sections, and with no restrictions on the Front-Cover 
##  and no Back-Cover Texts.
##  A copy of the license is included in the section entitled "GNU Free 
##  Documentation License".

.PHONY: convert convert-intro convert-examples dox

.DEFAULT_GOAL := default

target          = modularity
pyconvert       = ../scripts/py-convert
pyconvert_batch = ../scripts/py-convert-batch
notebook        = $(target).py
date            = $(shell date +%F)
include         = ./dox-data/include
template        = ./dox-data/template
template-intro  = ./dox-data/template-intro
generator       = ./dox-data/generator/pi.py
output          = ./examples

default: convert

convert: convert-intro convert-examples

convert-intro: dox-intro
	$(pyconvert) $(target).py $(target).ipynb

convert-examples: dox
	$(pyconvert_batch) $(output)

dox: $(source)
	rm -rf $(output)
	env PYTHONPATH=../dox/library   \
	  python3 ../dox/dox.py         \
	    -v -r                       \
	    -g $(generator)             \
	    -I $(include)               \
	    -t $(template)              \
	    -o $(output)

dox-intro:
	rm -f README.org
	env PYTHONPATH=../dox/library   \
	  python3 ../dox/dox.py         \
	    -r                          \
	    -g $(generator)             \
	    -I $(include)               \
	    -t $(template-intro)        \
	    -o .

### *EOF*
