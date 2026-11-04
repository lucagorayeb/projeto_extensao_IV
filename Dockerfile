FROM --platform=$BUILDPLATFORM python:3.14.6-alpine3.24 AS base

WORKDIR /app/

COPY ./requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --upgrade pip && pip3 install -r requirements.txt

RUN apk add --no-cache \
    procps \
    git \
    unzip \
    icu-dev \
    zlib-dev \
    libxml2 \
    libxml2-dev \
    readline-dev \
    dcron \
    sudo \
    libzip-dev \
    postgresql-dev \
    xz  \
    tar \
    curl \
    nodejs \
    npm 


FROM base AS dev

COPY . /app
