# Theme-specific settings
SITENAME = 'Oleg Kmechak'
DOMAIN = 'doweneedmath.ua'
BIO_TEXT = 'Developer and musician from Sokal.'
FOOTER_TEXT = 'Powered by <a href="http://getpelican.com">Pelican</a> and <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.'

SITE_AUTHOR = 'Oleg Kmechak'
#TWITTER_USERNAME = '@none'
GOOGLE_PLUS_URL = 'https://plus.google.com/+OlegFedyna'
INDEX_DESCRIPTION = 'Website and blog of Oleg Kmechak, a developer and musician from Sokal, BC.'

SIDEBAR_LINKS = [
    '<a href="category/about.html">About</a>',
    '<a href="categories.html">Categories</a>',
    '<a href="archives.html">Archive</a>'
]

ICONS_PATH = 'images/icons'

SOCIAL_ICONS = [
    ('mailto:oleg.kmechak@gmail.com', 'Email (oleg.kmechak@gmail.com)', 'fa-envelope'),
    #('http://twitter.com/None', 'Twitter', 'fa-twitter'),
    ('https://github.com/ofcrashbash', 'GitHub', 'fa-github'),
    ('https://soundcloud.com/rain_must_fall', 'SoundCloud', 'fa-soundcloud'),
    ('https://www.facebook.com/profile.php?id=100005110871470', 'Facebook', 'fa-facebook'),
    #('https://vk.com/rain_must_fall', 'Vkontakte', 'fa-vk'),
    #('https://plus.google.com/+OlegFedyna', 'Google+', 'fa-google-plus'),
    ('http://www.youtube.com/c/OlegFedyna ','Youtube', 'fa-youtube')
    #('/atom.xml', 'Atom Feed', 'fa-rss')
]

THEME_COLOR = '#FF8000'

# Pelican settings
RELATIVE_URLS = True
SITEURL = 'http://doweneedmath.pp.ua'
TIMEZONE = 'Europe/Kiev'
DEFAULT_DATE = 'fs'
DEFAULT_DATE_FORMAT = '%B %d, %Y'
DEFAULT_PAGINATION = False
SUMMARY_MAX_LENGTH = 70


THEME = 'pneumatic_upd'

#ARTICLE_URL = '/{category}/{slug}/'
#ARTICLE_SAVE_AS = 'category/{slug}/' + 'index.html'

#PAGE_URL = '{slug}/'
#PAGE_SAVE_AS = PAGE_URL + 'index.html'

#TODO resolve this: do i need this archives?
#ARCHIVES_SAVE_AS = 'blog/index.html'
#YEAR_ARCHIVE_SAVE_AS = '{date:%Y}/index.html'
#MONTH_ARCHIVE_SAVE_AS = '{date:%Y}/{date:%m}/index.html'

# Disable authors, categories, tags, and category pages
#DIRECT_TEMPLATES = ['index', 'blogs']
#CATEGORY_SAVE_AS = ''

# Disable Atom feed generation
FEED_ATOM = 'atom.xml'
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

TYPOGRIFY = True

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.admonition': {},
        'markdown.extensions.codehilite': {'linenums': None},
        'markdown.extensions.extra': {},
    },
    'output_format': 'html5',
}

CACHE_CONTENT = False
DELETE_OUTPUT_DIRECTORY = True
OUTPUT_PATH = 'develop'
PATH = 'content'

#templates = ['404.html']
#TEMPLATE_PAGES = {page: page for page in templates}

STATIC_PATHS = ['Images', 'uploads', 'extra', 'Images/hello_world']
IGNORE_FILES = ['.DS_Store', 'pneumatic.scss', 'pygments.css']

PLUGIN_PATHS = ['C:/Users/ofcra/Programming_Files_And_Scripts/Pelican/pelican-plugins']
PLUGINS = ['assets', 'neighbors', 'render_math', 'i18n_subsites']
ASSET_SOURCE_PATHS = ['static']
ASSET_CONFIG = [
    ('cache', False),
    ('manifest', False),
    ('url_expire', False),
    ('versions', False),
]

#multilanguage setup
I18N_SUBSITES = {
    'ua': {'SITENAME': 'Олег Кмечак',
           'BIO_TEXT': 'Програміст і музикант зі Сокаля',
           'FOOTER_TEXT': 'Побудоване на <a href="http://getpelican.com">Pelican</a> і <a href="http://pages.github.com">GitHub&nbsp;Pages</a>.',
           'SITE_AUTHOR': 'Oleg Kmechak',
           'INDEX_DESCRIPTION': 'Мій вебсайт і блог, програміст і музикант зі Cокаля.',
           'SIDEBAR_LINKS': [
                '<a href="category/about.html">Про</a>',
                '<a href="categories.html">Блог</a>',
                '<a href="archives.html">Архів</a>'
                ]
            }
    }

DEFAULT_LANG = 'en'
I18N_UNTRANSLATED_ARTICLES = 'keep'
I18N_UNTRANSLATED_PAGES = 'keep'

UA_LINK_NAME = 'Укр'
EN_LINK_NAME = 'En'

languages_lookup = {
    'ua': 'Укр',
    'en': 'En',
    }

def lookup_lang_name(lang_code):
    return languages_lookup[lang_code]

JINJA_FILTERS = {
    'lookup_lang_name': lookup_lang_name
    }