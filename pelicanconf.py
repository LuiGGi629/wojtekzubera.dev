#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Wojtek Zubera'
SITENAME = 'Wojtek Zubera'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Warsaw'

DEFAULT_LANG = 'en'

THEME = "./themes/Flex"

# PLUGIN_PATHS = ['./plugins/pelican-plugins']

# PLUGINS = [
#     "sitemap",
#     "better_codeblock_line_numbering",
#     # "better_code_samples",
#     "bootstrapify",
#     "deadlinks",
#     "more_categories",
#     "neighbors",
#     "pelican-ert",
#     "liquid_tags.notebook",
#     "liquid_tags.include_code",
#     "representative_image",
#     "share_post",
#     'show_source',
#     'tipue_search',
#     "dateish",
#     "post_stats",
#     "render_math",
#     "related_posts",
#     "autostatic",
#     "clean_summary"
# ]

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

DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True