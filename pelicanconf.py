#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# https://github.com/getpelican/pelican/blob/master/docs/settings.rst


# GENERAL
PATH = "content"
AUTHOR = "Wojtek Zubera"
SITENAME = "Wojtek Zubera"
SITETITLE = SITENAME
SITESUBTITLE = "I write about the things I learn."
SITEURL = "https://affectionate-nobel-2a09ac.netlify.com"
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"
STATIC_PATHS = ["extra"]
SITELOGO = "/wz-deepart.jpg"
FAVICON = "/favicon.ico"
RELATIVE_URLS = False
# DELETE_OUTPUT_DIRECTORY = True

# TIME AND DATES
DEFAULT_DATE_FORMAT = '%d %B %Y'

# THEME VARIABLES
THEME = "./themes/Flex"

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/wz-deepart.jpg': {'path': 'wz-deepart.jpg'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# PLUGIN_PATHS = ["./plugins/pelican-plugins"]

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
#     "show_source",
#     "tipue_search",
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
LINKS = (("Pelican", "http://getpelican.com/"),
         ("Python.org", "http://python.org/"),
         ("Jinja2", "http://jinja.pocoo.org/"),
         ("You can modify those links in your config file", "#"),)

# Social widget
GITHUB = "LuiGGi629"
LINKEDIN = "wojtek-zubera-18895415b"

SOCIAL = (("Github", "https://github.com/" + GITHUB, GITHUB, "fab fa-github"),
          ("LinkedIn", "https://www.linkedin.com/in/" + LINKEDIN, LINKEDIN, "fab fa-linkedin-in"),)

# PAGINATION
DEFAULT_PAGINATION = 5

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
