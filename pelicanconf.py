#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yan Wang'
SITENAME = u'Computing Life'
SITEURL = ''

TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/grapeot/blog/'
DEFAULT_LANG = u'en'
FAVICON_URL = 'static/images/favicon.ico'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('https://www.facebook.com/YansReaderShareItems', 'FB Shared Items (Chinese)'),
        ('http://weibo.com/grapeot/', 'Weibo (Chinese)'),
        ('https://github.com/grapeot/', 'Github'),)

FILES_TO_COPY = (('extra/robots.txt', 'robots.txt'),)
MENUITEMS = (('Archives', '/archives.html'),
        ('Subscribe', '/pages/feed.html'),
        ('Lab', 'http://lab.grapeot.me/'),)
THEME = './themes/gum'
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))

# plug-ins
PLUGIN_PATH = 'plugins'
PLUGINS = ['pelican.latex', 'sitemap', 'gravatar']
SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'monthly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
LATEX = 'article'

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
