### Dockerfile for notebooks
###
### Copyright 2016 Mac Radigan
### All Rights Reserved

  FROM ubuntu:latest

  MAINTAINER Mac Radigan

  ENV LANG=C.UTF-8 LC_ALL=C.UTF-8

  ## update APT
  RUN ulimit -n 1024
  RUN apt-get update --fix-missing

  ## IPython Notebook
  RUN apt-get update &&      \
      apt-get install -y     \
        curl                 \
        sudo                 \
        build-essential      \
        autoconf             \
        automake             \
        git                  \
        rxvt-unicode         \
        xterm                \
        zsh                  \
        tmux                 \
        screen               \
        vim                  \
        emacs                \
        ack-grep             \
        firefox              \
        python-pygments      \
        ipython              \
        python-numpy         \
        python-matplotlib    \
        ipython-notebook     \
        python-pip           \
        python3-pip          \
        cython 

# # clean up APT
# RUN apt-get clean && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/*

  RUN python  -m pip install sympy
  RUN python3 -m pip install sympy

  RUN mkdir -p /opt
  RUN mkdir -p /notebooks
  COPY ./home /root

  EXPOSE 8888

  # entry point
  ADD ./ctl /usr/bin
  RUN chmod 775 /usr/bin/ctl
  ENTRYPOINT ["/usr/bin/ctl"]

### *EOF*
