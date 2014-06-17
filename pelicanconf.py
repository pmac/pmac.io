#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

import sys

from pathlib import Path


BASE_PATH = Path(__file__).resolve().parent
PLUGINS_PATH = BASE_PATH / 'pelican-plugins'
sys.path.append(str(PLUGINS_PATH))

AUTHOR = u'Paul McLanahan'
SITENAME = u'Paul McLanahan'
SITESUBTITLE = u'on webdev, mozilla, and stuff'
SITEURL = ''
STATIC_URL = '/static'

MD_EXTENSIONS = ['codehilite', 'extra']
THEME = 'theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PLUGINS = [
    'pelican_alias',
    'pelican_bugs',
    'assets',
]

FEED_ATOM = 'feed.xml'
CATEGORY_FEED_ATOM = 'category/%s/feed.xml'
TAG_FEED_ATOM = 'tag/%s/feed.xml'
FEED_ALL_ATOM = TRANSLATION_FEED_ATOM = None

TWITTER_USERNAME = 'pmclanahan'
GITHUB_URL = 'https://github.com/pmclanahan'
SOCIAL = (
    ('github', GITHUB_URL),
    ('twitter', 'https://twitter.com/pmclanahan'),
)

TEMPLATE_PAGES = {
    'extra/404.html': '404.html',
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = False
FILENAME_METADATA = '(?P<date>\d{4}-\d{2}-\d{2})-(?P<slug>.*)'
ARTICLE_URL = '{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = '{date:%Y}/{date:%m}/{slug}/index.html'
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
AUTHOR_URL = 'author/{slug}/'
AUTHOR_SAVE_AS = 'author/{slug}/index.html'
CATEGORY_URL = 'category/{slug}/'
CATEGORY_SAVE_AS = 'category/{slug}/index.html'
TAG_URL = 'tag/{slug}/'
TAG_SAVE_AS = 'tag/{slug}/index.html'
ARCHIVES_SAVE_AS = 'archives/index.html'
ARTICLE_EXCLUDES = ('pages', 'extra')
