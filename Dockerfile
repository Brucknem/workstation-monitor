FROM ubuntu:20.04

LABEL Marcel Bruckner "mbruckner94@gmail.com"

WORKDIR /usr/workstation-monitor

RUN apt-get update \
  && apt-get install -y -qq --no-install-recommends \
    apt-utils \
    gnupg \
    wget \
    xauth \
    python3 \
    python3-pip \
    python3-dev \
    build-essential \
    libsystemd-dev

# Bazel install
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | \
    tee /etc/apt/sources.list.d/bazel.list && \
    wget https://bazel.build/bazel-release.pub.gpg --no-check-certificate
RUN apt-key add bazel-release.pub.gpg
RUN apt-get update && apt-get install -y -qq --no-install-recommends bazel

RUN rm -rf /var/lib/apt/lists/*

# Python install
RUN ln -s /usr/bin/python3 /usr/bin/python & \
    ln -s /usr/bin/pip3 /usr/bin/pip

# COPY utils/geckodriver /usr/bin/geckodriver
# COPY requirements.txt .