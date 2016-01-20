#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'CHANN'
SITENAME = 'Today I Learned'
SITESUBTITLE = 'Novice Programmer'
SITEURL = 'http://til.chann.kr'
# SITEURL = 'http://localhost:8000'
DISQUS_SITENAME = u'githubs'

# DISQUS_SECRET_KEY = u'YOUR_SECRET_KEY'
# DISQUS_PUBLIC_KEY = u'YOUR_PUBLIC_KEY'

### THEME SETTING
THEME = 'theme/pelican-svbhack'
# THEME = 'theme/replika'
# BOOTSTRAP_NAVBAR_INVERSE = True
# DISPLAY_CATEGORY_IN_BREADCRUMBS = True
# COVER_IMG_URL = 'http://blog.chann.kr/content/images/2015/11/photo-1421757295538-9c80958e75b0-1.jpeg'


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
LINKS = (
         ('Blog', 'http://blog.chann.kr'),
)

# Social widget
SOCIAL = (
	('Resume', 'https://chann.kr'),
	('Github', 'https://github.com/channprj'),
	('Twitter', 'https://twitter.com/chann_kr'),
	('Facebook', 'https://fb.com/channprj'),
)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Remove html extension
ARCHIVE_URL = '{archive}'

ARTICLE_URL = '{category}/{slug}'
ARTICLE_SAVE_AS = ARTICLE_URL+'.html'

PAGE_URL = '{slug}'
PAGE_SAVE_AS = PAGE_URL+'.html'

CATEGORY_URL = '{slug}/index'
CATEGORY_SAVE_AS = CATEGORY_URL+'.html'

TAG_URL = 'tag/{slug}'
TAG_SAVE_AS = TAG_URL+'.html'

AUTHOR_URL = 'author/{slug}'
AUTHOR_SAVE_AS = AUTHOR_URL+'.html'
