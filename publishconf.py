#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

# This file is only used if you use `make publish` or
# explicitly specify it as your config file.

import os
import sys
sys.path.append(os.curdir)
from pelicanconf import *

SITEURL = 'http://grapeot.me'
RELATIVE_URLS = False

FEED_ATOM = 'feeds/atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = 'feeds/%s.atom.xml'
FEED_RSS = 'feeds/rss.xml'
FEED_ALL_RSS = None
CATEGORY_FEED_RSS = 'feeds/%s.rss.xml'
FEED_MAX_ITEMS = 10

DELETE_OUTPUT_DIRECTORY = True

# Following items are often useful when publishing

DISQUS_SITENAME = "computinglife"
#GOOGLE_ANALYTICS = ""
