FROM ubuntu:16.04
MAINTAINER Andrianarivo RAKOTOARIJAONA

ENV PYTHONUNBUFFERED 1

RUN apt-get update && \
        apt-get install -y software-properties-common && \
        add-apt-repository ppa:deadsnakes/ppa && \
        apt-get update -y  && \
        apt-get install -y build-essential python3.6 python3.6-dev python3-pip && \
        python3.6 -m pip install pip --upgrade && \
        python3.6 -m pip install wheel

COPY ./requirements.txt /requirements.txt

RUN pip3 install -r /requirements.txt

RUN mkdir /app
WORKDIR /app

COPY . /app
