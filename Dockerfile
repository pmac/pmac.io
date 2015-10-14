FROM nginx:latest

WORKDIR /app
EXPOSE 80
CMD ["/app/bin/bootstrap.sh"]

RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential python python-pip \
        python-dev optipng libjpeg-progs gettext-base

# install python requirements
COPY ./requirements.txt /app/requirements.txt
RUN pip install -r requirements.txt

COPY . /app
