#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'grapeot'
SITENAME = u'Computing Life'
SITEURL = 'https://yage.ai'

TIMEZONE = 'America/Los_Angeles'

GITHUB_URL = 'https://github.com/grapeot/blog/'
DEFAULT_LANG = u'en'
FAVICON_URL = 'static/images/favicon.ico'

SHOW_PAGES_IN_SIDEBAR = False

# Feed generation (enabled for local testing; publishconf overrides for production)
FEED_DOMAIN = SITEURL
FEED_ALL_ATOM = 'feeds/atom.xml'
CATEGORY_FEED_ATOM = 'feeds/{slug}.atom.xml'
FEED_ALL_RSS = 'feeds/rss.xml'
CATEGORY_FEED_RSS = 'feeds/{slug}.rss.xml'
FEED_MAX_ITEMS = 10
TRANSLATION_FEED_ATOM = None

# Blogroll
#LINKS =  (('Pelican', 'http://getpelican.com/'),
#          ('Python.org', 'http://python.org/'),
#          ('Jinja2', 'http://jinja.pocoo.org/'),
#          ('You can modify those links in your config file', '#'),)

# Social widget
# SOCIAL = (('https://www.facebook.com/YansReaderShareItems', 'FB Shared Items (Chinese)'),
#         ('http://weibo.com/grapeot/', 'Weibo (Chinese)'),
#         ('https://github.com/grapeot/', 'Github'),)

STATIC_PATHS = [ 'extra/robots.txt', 'images' ]
EXTRA_PATH_METADATA = { 'extra/robots.txt': {'path': 'robots.txt'}, }
MENUITEMS = (('Archives', '/archives.html'),
        ('Subscribe', '/pages/feed.html'),
        ('Services', '/pages/services.html'),
        #('Lab', 'http://lab.grapeot.me/'),)
        ('Duck Sky Survey', 'dssv2/'),
        ('🔍Search', '/search/'),
        )
THEME = './themes/gum'
DIRECT_TEMPLATES = (('index', 'tags', 'categories', 'archives'))

# plug-ins
PLUGIN_PATHS = [ './pelican-plugins' ]
PLUGINS = ['render_math', 'sitemap', 'gravatar', 'render_math']
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
RELATIVE_URLS = True

# Analytics and Comments (also used in development for testing)
GOOGLE_ANALYTICS_ID = "G-03MXLX12W1"
DISQUS_SITENAME = "computinglife"
