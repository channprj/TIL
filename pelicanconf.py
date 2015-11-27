#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CHANN'
SITENAME = 'GIT TO GEEK'
SITEURL = ''
DISQUS_SITENAME = u'githubs'

# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'

### THEME SETTING
THEME = 'themes/pure-single'
# THEME = 'themes/pelican-bootstrap3'
COVER_IMG_URL = 'http://blog.chann.kr/content/images/2015/11/photo-1421757295538-9c80958e75b0-1.jpeg'


OUTPUT_PATH = 'output'
PATH = 'content'

TIMEZONE = 'Asia/Seoul'

DEFAULT_LANG = 'ko'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
)

# Social widget
SOCIAL = (('github', 'https://github.com/channprj'),
          ('twitter-square', 'https://twitter.com/chann_kr'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Remove html extension
ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL+'.html'

CATEGORY_URL = '{slug}/index'
CATEGORY_SAVE_AS = CATEGORY_URL+'.html'