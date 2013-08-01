#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Yan Wang'
SITENAME = u'Computing Life'
SITEURL = 'http://grapeot.me'

TIMEZONE = 'America/New_York'

GITHUB_URL = 'https://github.com/grapeot/blog/'
DEFAULT_LANG = u'en'

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
        ('RSS', 'http://grapeot.me/feeds/all.atom.xml'),
        ('Lab', 'http://lab.grapeot.me/'),)
THEME = '/home/grapeot/pelican-themes/gum'
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
