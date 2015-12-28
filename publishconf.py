#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

sys.path.append(os.curdir)
from pelicanconf import *


PLUGINS.append('gzip_cache')
SITEURL = 'https://{}'.format(os.getenv('PELICAN_DOMAIN', 'pmac.io'))
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-170744-4"

# load extra config if available
try:
    from pelicanlocal import *
except ImportError:
    pass
