#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Paul McLanahan'
SITENAME = u'Paul McLanahan'
SITESUBTITLE = u'a mozillian on a mission'
SITEURL = ''

MD_EXTENSIONS = ['codehilite', 'extra']
THEME = 'themes/sundown'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PLUGINS = ['content_aliases', 'assets']

FEED_ALL_ATOM = 'feed/all.xml'
CATEGORY_FEED_ATOM = 'feed/category/%s.xml'
TAG_FEED_ATOM = 'feed/tag/%s.xml'

TWITTER_USERNAME = 'pmclanahan'
GITHUB_URL = 'https://github.com/pmclanahan/'
SOCIAL = (
    ('github', GITHUB_URL),
    ('twitter', 'https://twitter.com/pmclanahan'),
)
FILES_TO_COPY = (
    ('extra/CNAME', 'CNAME'),
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
