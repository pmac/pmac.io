FROM nginx:latest

WORKDIR /app

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python python-pip \
        python-dev optipng libjpeg-progs gettext-base

RUN rm /etc/nginx/nginx.conf
ENV PELICAN_DOMAIN pmac.io

COPY ./etc/nginx.conf /app/etc/nginx.conf
RUN cat /app/etc/nginx.conf | envsubst '$PELICAN_DOMAIN' > /etc/nginx/nginx.conf

# install python requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
RUN make publish

# Cleanup
RUN apt-get purge -y build-essential python python-pip \
        python-dev optipng libjpeg-progs gettext-base
RUN apt-get autoremove -y
RUN rm -rf /var/lib/{apt,dpkg,cache,log} /usr/share/doc /usr/share/man /tmp/*
