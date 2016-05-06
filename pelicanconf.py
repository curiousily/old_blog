#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Venelin Valkov'
SITENAME = 'Curiousily'
SITESUBTITLE = 'The curious quest of one fooled by randomness'
SITEURL = 'http://curiousily.com'

TWITTER_USERNAME = 'curiousily'

PATH = 'content'

TIMEZONE = 'Europe/Sofia'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
# LINKS = (('Pelican', 'http://getpelican.com/'),
         # ('Python.org', 'http://python.org/'),
         # ('Jinja2', 'http://jinja.pocoo.org/'),
         # ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('twitter', 'https://twitter.com/curiousily'),
          ('github', 'https://github.com/curiousily'),)

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

THEME = "./themes/pelican-bootstrap3"
BOOTSTRAP_THEME = "readable"

EXTRA_HEADER = open('_nb_header.html').read()

PLUGIN_PATHS = ['./plugins']
PLUGINS = ['liquid_tags', 'liquid_tags.notebook']

NOTEBOOK_DIR = 'notebooks'

PYGMENTS_STYLE = "default"

STATIC_PATHS = ['images', 'extra/CNAME']
EXTRA_PATH_METADATA = {'extra/CNAME': {'path': 'CNAME'},}

DELETE_OUTPUT_DIRECTORY = True

ARTICLE_URL = 'posts/{date:%Y}/{date:%m}/{slug}/'
ARTICLE_SAVE_AS = 'posts/{date:%Y}/{date:%m}/{slug}/index.html'

GOOGLE_ANALYTICS = 'UA-63986975-1'

ADDTHIS_PROFILE = 'ra-572a213e4c4ede2a'

DISQUS_SITENAME = 'curiousily'
