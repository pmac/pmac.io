---
title: "Multi-Stage Dockerfiles and Python Virtualenvs"
date: 2019-02-12T22:22:20-05:00
draft: true
tags:
  - mozilla
  - docker
  - python
---

Using Docker's [multi-stage build][] feature and Python's virtualenv tool,
we can make smaller and more secure docker images for production.

<!--more-->

## The Problem

We want to have the smallest production Docker images for a number of reasons.
Having files unnecessary to the running app makes the image slower to move
to and from the Docker Hub, as well as potentially introducting security
vulnerabilities. So we'd really prefer not to have any of the build tools
or libraries required to build the app in the final image if we can help it.

To accomplish this we used to have several docker files and we'd build them
one at a time. We'd then either copy the built files out of them, or mount
a volume and run the process that produced the files we needed then. But this
was cumbersome and could potentially conflict with other builds on the same CI
box if we weren't careful, so a single build process was very intersting.

## Multi-stage Dockerfile

Enter a potential solution from Docker. A multi-stage Dockerfile is basically
more than one Dockerfile glued together, i.e. it has more than one `FROM` line.
The resulting image is the result of the last section in the file. So, for
example, you could base the first section of the file on a NodeJS base, and in
there have it build and process your static assets (CSS, JS, images), then in
a second section based on a Python image you build your app and copy the assets
from the first stage. Here's a simple example:

```docker
########
# assets builder and dev server
#
FROM node:8 AS assets

# Add node tools to path
ENV PATH=/app/node_modules/.bin:$PATH
WORKDIR /app

# copy dependency definitions
COPY package.json yarn.lock ./

# install dependencies
RUN yarn install --pure-lockfile
RUN yarn global add gulp-cli@2.0.1

# copy supporting files and media
COPY .eslintrc.js .stylelintrc gulpfile.js ./
COPY ./media ./media

# build production files
RUN gulp build --production
```

The above results in processed files in an `static_final` directory in
the image. Another section can get those files with a directive like
`COPY --from=assets /app/static_final /app/static_final`.

[multi-stage build]: https://docs.docker.com/develop/develop-images/multistage-build/

## Python Virtualenv

Normally in a Docker image a virtualenv is superfluous. You can just install
your Python dependencies globally in the image and it won't interfere with a
thing. Yay Docker! But the multistage-dockerfile (or just using multiple
dockerfiles before this feature) introduces a reason to use
them again. We can use a larger image with a lot of build tools and dependencies
to compile and install all of our dependencies in a virtualenv, and then
(as long as you keep it at the same path and on the same base distro) copy
it to a much leaner and more secure production image.

This is a technique I learned from my friend and colleague
[Giorgos](https://giorgos.sealabs.net/) in his work on
[SUMO](https://github.com/mozilla/kitsune/ "Mozilla's Support Site") at Mozilla.
He is awesome and you should check out his stuff.

The basic pattern is as follows:

```docker
########
# Python dependencies builder
#
# Full official Debian-based Python image
FROM python:3-stretch AS builder

# Always set a working directory
WORKDIR /app
# Sets utf-8 encoding for Python
ENV LANG=C.UTF-8
# Turns off writing .pyc files. Superfluous on an ephemeral container.
ENV PYTHONDONTWRITEBYTECODE=1
# Seems to speed things up
ENV PYTHONUNBUFFERED=1

# Ensures that the python and pip executables used
# in the image will be those from our virtualenv.
ENV PATH="/venv/bin:$PATH"

# Install OS package dependencies.
# Do all of this in one RUN to limit final image size.
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gettext build-essential mariadb-client libmariadbclient-dev \
        libxml2-dev libxslt1-dev libxslt1.1 && \
    rm -rf /var/lib/apt/lists/*

# Setup the virtualenv
RUN python -m venv /venv
# or "virtualenv /venv" for Python 2

# Install Python deps
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
```

And then the production app image:

```docker
########
# django app container
#
# Smaller official Debian-based Python image
FROM python:3-slim-stretch AS app

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/venv/bin:$PATH"

WORKDIR /app
EXPOSE 8000
CMD ["./bin/run.sh"]

# do all of this in one RUN to limit final image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gettext libxslt1.1 && \
    rm -rf /var/lib/apt/lists/*

# copy in Python environment
COPY --from=builder /venv /venv

# copy in static assets
COPY --from=assets /app/static_final /app/static_final

# copy in the rest of the app
COPY ./ ./
```

The final Dockerfile is just these three sections concatinateed together.
This ensures that the final image has no extra build tools, language runtimes
(Node in this case), or libraries required only during build. The end result is
a smaller and more secure container running your service.

See the [official Python docker image repository][docker-hub-py]
for descriptions of the image types if you're curious. I highly recommend
the official Python images. They are well maintained and always have the latest
Python versions.

## Wrapping up

I really like this technique. You get the benefit of a single Dockerfile with
the full build encapsulated into one file and happening in one command, wile
also producting a much smaller and more secure image. I've thrown together a
quick [demo Responder app repo][responder-demo] so that you can see how it all really works
and fits together, and because I wanted an excuse to play with [Responder][] :)

I also included in the demo, simple as it is, an [example Dockerfile][dockerfile-full]
of the same commands but just using one build stage. The results of building these are:

```bash
$ docker images | grep multi-stage
multi-stage-docker-venv-demo_app         latest  a6106f3a4c59  195MB
multi-stage-docker-venv-demo_app-pipenv  latest  e945e860ec24  216MB
multi-stage-docker-venv-demo_app-full    latest  e945e860ec24  979MB
```

I hope you found this helpful. Thanks for reading!

[docker-hub-py]: https://hub.docker.com/_/python/#image-variants
[responder-demo]: https://github.com/pmac/multi-stage-docker-venv-demo
[Responder]: https://python-responder.org/
[dockerfile-full]: https://github.com/pmac/multi-stage-docker-venv-demo/blob/master/Dockerfile-full
