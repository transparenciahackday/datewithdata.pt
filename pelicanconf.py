#!/usr/bin/env python
from __future__ import unicode_literals

''' Content '''
AUTHOR = 'Transparência Hackday Portugal'
SITENAME = 'Date With Data'
SITEURL = 'http://datewithdata.pt'
SITE_DESCRIPTION = "A lançar dados desde 2010"

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'pt'

PATH = 'content'
THEME = 'theme/datewithdata'


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

# Set up clean URLs
ARTICLE_URL = '{category}/{slug}/'
ARTICLE_SAVE_AS = '{category}/{slug}/index.html'
PAGE_URL = '{slug}/'
PAGE_SAVE_AS = '{slug}/index.html'
CATEGORY_URL = '{slug}/'
CATEGORY_SAVE_AS = '{slug}/index.html'
DRAFT_URL = 'private/{slug}/'
DRAFT_SAVE_AS = 'private/{slug}/index.html'
DRAFT_LANG_URL = 'private/{slug}-{lang}/'
DRAFT_LANG_SAVE_AS = 'private/{slug}-{lang}/index.html'

