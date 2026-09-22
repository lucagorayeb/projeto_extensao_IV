FROM --platform=$BUILDPLATFORM python:3.14.6-alpine3.24 AS base

WORKDIR /app/

COPY ./requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install -r requirements.txt

FROM base AS dev

COPY . /app
