#!/usr/bin/make -f
### boostrap.mk (for notebooks)
### Copyright 2016 Mac Radigan
### All Rights Reserved

.PHONY: bootstrap update
.DEFAULT_GOAL := bootstrap

bootstrap: update

update:
	$(MAKE) -C ./submodules update

### *EOF*
