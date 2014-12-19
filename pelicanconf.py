#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = u'Paul McLanahan'
SITENAME = u'Paul McLanahan'
SITESUBTITLE = u'on webdev, mozilla, and stuff'
SITEURL = ''

MD_EXTENSIONS = ['codehilite', 'extra']
THEME = 'theme'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

PLUGIN_PATH = 'pelican-plugins'
PLUGINS = [
    'pelican_alias',
    'pelican_bugs',
    'pelican_edit_url',
    'optimize_images',
    'assets',
]

FEED_ATOM = 'feed.xml'
CATEGORY_FEED_ATOM = 'category/%s/feed.xml'
TAG_FEED_ATOM = 'tag/%s/feed.xml'
FEED_ALL_ATOM = TRANSLATION_FEED_ATOM = None

TWITTER_USERNAME = 'pmclanahan'
GITHUB_URL = 'https://github.com/pmclanahan'
GITHUB_REPO = 'pmac.io'
GITHUB_REPO_URL = '{}/{}'.format(GITHUB_URL, GITHUB_REPO)
EDIT_CONTENT_URL = GITHUB_REPO_URL + '/blob/master/{file_path}'
SOCIAL = (
    ('github', GITHUB_URL),
    ('twitter', 'https://twitter.com/pmclanahan'),
)

TEMPLATE_PAGES = {
    'extra/404.html': '404.html',
}

STATIC_PATHS = [
    'extra/keybase.txt',
]

EXTRA_PATH_METADATA = {
    'extra/keybase.txt': {'path': 'keybase.txt'},
}

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = False
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

# Static Media
ASSET_BUNDLES = (
    ('base-css',
     ['css/main.css',
      'css/pygment.css',
      'css/font-awesome.css',
      'css/gh-fork-ribbon.css',
      'css/responsive-nav.css'],
     {'output': 'CACHE/base-css.%(version)s.css',
      'filters': ['cssmin']}),
    ('base-js',
     ['js/jquery-2.1.1.js',
      'js/jquery.timeago.js',
      'js/responsive-nav.js',
      'js/site.js'],
     {'output': 'CACHE/base-js.%(version)s.js',
      'filters': ['rjsmin']})
)
