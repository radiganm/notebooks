#!/usr/bin/make
## makefile (for notebooks)
##
## Copyright 2016 Mac Radigan
## All Rights Reserved

.PHONY: build clean run ui shell

absroot   = $(shell pwd)

name = radiganm/notebooks

port = 8888

build: 
	docker build -t $(name) .

run: 
	docker run -it             \
	  -p $(port):$(port)       \
	  -v /tmp:/tmp             \
	  -v $(absroot):/notebooks \
	  $(name) notebook

ui:
	docker run -it                       \
	  -p $(port):$(port)                 \
	  -v /tmp:/tmp                       \
	  -e DISPLAY                         \
	  -v /tmp/.X11-unix:/tmp.X11-unix:ro \
	  -v $(absroot):/notebooks           \
	  $(name) notebook-ui

shell: 
	docker run -it                       \
	  -e DISPLAY                         \
	  -v /tmp/.X11-unix:/tmp.X11-unix:ro \
	  -v $(absroot):/notebooks           \
	  $(name) util shell

clean: 
	docker ps -a --no-trunc | grep $(name) | awk '{print$$1}' | xargs -I{} docker stop {}
	docker images -a --no-trunc | grep $(name) | awk '{print$$3}' | xargs -I{} docker rmi -f {}

## *EOF*
