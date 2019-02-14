---
title: "Multi-Stage Dockerfiles and Python Virtualenvs"
date: 2019-02-12T22:22:20-05:00
draft: true
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
thing. Hooray Docker! But the multistage-dockerfile introduces a reason to use
them again. We can use a larger image with a lot of build tools and dependencies
to compile and install all of our dependencies in a virtualenv, and then
(as long as you keep it at the same path and on the same base distro) copy
it to a much more lean production image. The basic pattern is as follows:

```docker
########
# Python dependencies builder
#
FROM python:3-stretch AS builder

WORKDIR /app
ENV LANG=C.UTF-8
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PATH="/venv/bin:$PATH"

# do all of this in one RUN to limit final image size
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        gettext build-essential mariadb-client libmariadbclient-dev \
        libxml2-dev libxslt1-dev libxslt1.1 && \
    rm -rf /var/lib/apt/lists/*

RUN virtualenv /venv
COPY requirements.txt ./

# Install Python deps
RUN pip3 install --no-cache-dir -r requirements.txt
```

And then the production app image:

```docker
########
# django app container
#
FROM python:3-slim-stretch AS app-base

# Extra python env
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV PIP_DISABLE_PIP_VERSION_CHECK=1
ENV PATH="/venv/bin:$PATH"

# add non-priviledged user
RUN adduser --uid 1000 --disabled-password --gecos '' --no-create-home webdev

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

COPY ./ ./
```

The final Dockerfile is just these three sections concatinateed together.
This ensures that the final image has no extra build tools, language runtimes
(Node), or libraries required only during build, thus reducing the size and
security footprint of the running service.
