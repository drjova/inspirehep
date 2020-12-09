FROM node:lts-jessie as build-stage

WORKDIR /usr/src/app

ENV PORT 4000
ENV PATH /usr/src/app/node_modules/.bin:$PATH

COPY . /usr/src/app

RUN npm i -g npm@latest \
  && npm i

EXPOSE ${PORT}

ARG VERSION
ENV VERSION="${VERSION}"
