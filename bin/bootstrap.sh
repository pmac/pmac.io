#!/bin/bash

make publish
cat etc/nginx-tmpl.conf | envsubst '$PELICAN_DOMAIN' > etc/nginx.conf
exec nginx -c /app/etc/nginx.conf
