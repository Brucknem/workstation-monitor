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
    python3-pip

# Bazel install
RUN echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | \
    tee /etc/apt/sources.list.d/bazel.list && \
    wget https://bazel.build/bazel-release.pub.gpg --no-check-certificate
RUN apt-key add bazel-release.pub.gpg
RUN apt-get update && apt-get install -y -qq --no-install-recommends bazel

RUN rm -rf /var/lib/apt/lists/*

# Python install
COPY requirements.txt .
RUN pip3 install --no-cache-dir --upgrade -r requirements.txt 
