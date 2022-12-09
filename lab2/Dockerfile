# syntax=docker/dockerfile:1

FROM ubuntu:focal

RUN apt-get update -y
RUN apt-get install -y python3
RUN apt-get install -y iputils-ping

WORKDIR /lab2/

COPY . /lab2/