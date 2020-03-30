#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals
# https://github.com/getpelican/pelican/blob/master/docs/settings.rst


# GENERAL
PATH = "content"
AUTHOR = "Wojtek Zubera"
SITENAME = "wojtek_zubera.log"
SITETITLE = SITENAME
SITESUBTITLE = "I write about the things I learn."
SITEURL = "https://affectionate-nobel-2a09ac.netlify.com"
TIMEZONE = "Europe/Warsaw"
DEFAULT_LANG = "en"
STATIC_PATHS = ["extra"]
SITELOGO = "/wz-deepart.jpg"
FAVICON = "/favicon.ico"

# DELETE_OUTPUT_DIRECTORY = True
DISPLAY_PAGES_ON_MENU = True
RELATED_POSTS_SKIP_SAME_CATEGORY = True

# IGNORE_FILES = ['*.html', '*.rst']

USE_TIPUE_SEARCH = True

# can be useful in development, but set to False when you're ready to publish
RELATIVE_URLS = True

# TIME AND DATES
DEFAULT_DATE_FORMAT = '%d %B %Y'

# THEME VARIABLES
THEME = "./themes/Flex"

EXTRA_PATH_METADATA = {
    'extra/favicon.ico': {'path': 'favicon.ico'},
    'extra/wz-deepart.jpg': {'path': 'wz-deepart.jpg'},
    'extra/robots.txt': {'path': 'robots.txt'},
}

# ARCHIVES
YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
ARCHIVES_SAVE_AS = 'articles/index.html'
ARCHIVES_URL = 'articles'

# AUTHORS
AUTHORS_SAVE_AS = 'authors/index.html'
AUTHOR_URL = 'author/{slug}'

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
LINKS = (("You can modify those links in your config file", "#"),)

# Social widget
GITHUB = "luiggi629"
LINKEDIN = "wojtek-zubera-18895415b"

SOCIAL = (
    ("github", "https://github.com/" + GITHUB),
    ("linkedin", "https://www.linkedin.com/in/" + LINKEDIN),
)

GITHUB_URL = "http://github.com/" + GITHUB

GITHUB_CORNER_URL = "https://github.com/" + GITHUB + "/wojtekzubera.dev"

# PAGINATION
DEFAULT_PAGINATION = 4
DEFAULT_ORPHANS = 0
PAGINATION_PATTERNS = (
    (1, '{name}{extension}', '{name}{extension}'),
    (2, 'latest-{number}/', 'latest-{number}/index.html'),
)
PAGINATED_TEMPLATES = {'period_archives': None}

# DISABLE CACHING
LOAD_CONTENT_CACHE = False

# Uncomment following line if you want document-relative URLs when developing
# RELATIVE_URLS = True
