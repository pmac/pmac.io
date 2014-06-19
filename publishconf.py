#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys

from webassets.filter import register_filter
sys.path.append(os.curdir)
from pelicanconf import *

from asset_filters import BetterGZip


register_filter(BetterGZip)

SITEURL = 'http://pmac.io'
RELATIVE_URLS = False

FEED_DOMAIN = SITEURL

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

#DISQUS_SITENAME = ""
GOOGLE_ANALYTICS = "UA-170744-4"

# add gzip
for bundle in ASSET_BUNDLES:
    bundle[2]['filters'].append('better_gzip')
