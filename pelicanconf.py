#!/usr/bin/env python
from __future__ import unicode_literals

''' Content '''
AUTHOR = 'Transparência Hackday Portugal'
SITENAME = 'Date With Data'
SITEURL = ''
SITE_DESCRIPTION = "A lançar dados desde 2010"

TIMEZONE = 'Europe/Lisbon'
DEFAULT_LANG = 'pt'

PATH = 'content'
THEME = 'theme/datewithdata'

# Pagination
DEFAULT_ORPHANS = 0
DEFAULT_PAGINATION = True
PAGINATED_TEMPLATES = {'tag': 12, 'category': 12}
# limitar palavras no resumo do índice de posts
SUMMARY_MAX_LENGTH = 30

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

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

STATIC_PATHS = ['extra/htaccess']
EXTRA_PATH_METADATA = {'extra/htaccess': {'path': '.htaccess'}}

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
