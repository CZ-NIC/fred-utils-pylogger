FROM ubuntu:bionic
# Requirements for the python test environment
RUN apt-get --yes update \
 && apt-get install --yes --no-install-recommends \
    git \
    python2.7 \
    python3-setuptools \
    ssh \
 && rm -rf /var/lib/apt/lists/*
# Install newest pip, tox and its plugins
RUN apt-get --yes update \
 && apt-get install --yes --no-install-recommends \
    python3-pip \
 && rm -rf /var/lib/apt/lists/* \
 && pip3 install --upgrade \
    pip \
    tox \
 && apt-get purge --yes python3-pip
