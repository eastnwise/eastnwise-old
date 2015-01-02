#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'eastnwise'
SITENAME = 'EAST&WISE (beta)'
SITEURL = 'http://www.eastnwise.com'

PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
# FEED_DOMAIN = 'http://feeds.feedburner.com/eastnwise/'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('You can add links in your config file', '#'),
#           ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True

THEME = 'pelican-theme'

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'}}

SLUGIFY_SOURCE = 'basename'

ARTICLE_URL = 'posts/{slug}.html'
ARTICLE_SAVE_AS = 'posts/{slug}.html'

SLUG_SUBSTITUTIONS = ('투자', 'investment')

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ko': '%Y-%m-%d(%a)',
}
