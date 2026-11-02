FROM --platform=$BUILDPLATFORM python:3.14.6-alpine3.24 AS base

WORKDIR /app/

COPY ./requirements.txt /app

RUN --mount=type=cache,target=/root/.cache/pip \
    pip3 install --upgrade pip && pip3 install -r requirements.txt

RUN curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.8/install.sh | bash \
    \. "$HOME/.nvm/nvm.sh" \
    nvm install 26

FROM base AS dev

COPY . /app
