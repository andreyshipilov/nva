# -*- coding: utf-8 -*-
from os.path import splitext
from os import urandom

######################
# MEZZANINE SETTINGS #
######################
ADMIN_MENU_ORDER = (
    ("Content", ("pages.Page", (u"Загруженные файлы", "fb_browse"),
                 "setup.Setup")),
    ("Site", ("sites.Site", "redirects.Redirect", "conf.Setting")),
    ("Users", ("auth.User", "auth.Group",)),

    (u"Компания", ("news.NewsItem", "reviews.Review", "people.Human",
                   "legal.License", "legal.Patent", "banners.Banner",)),
    (u"Продукты и Услуги", ("people.Manager", "work.Product",
                            "work.ProductType", "work.Service",
                            "work.ServiceType",)),
    (u"Проекты", ("projects.Project", "projects.Client", "projects.Field",)),
)

PAGE_MENU_TEMPLATES = (
    (1, u"Верхнее левое", "pages/menus/top-left.html"),
    (2, u"Верхнее правое", "pages/menus/top-right.html"),
    (3, u"Верхнее правое (кнопками)", "pages/menus/top-right-buttons.html"),
    (4, u"Основное левое дерево", "pages/menus/left-tree.html"),
    (5, u"Нижнее (футер)", "pages/menus/footer.html"),
)

# A sequence of fields that will be injected into Mezzanine's (or any
# library's) models. Each item in the sequence is a four item sequence.
# The first two items are the dotted path to the model and its field
# name to be added, and the dotted path to the field class to use for
# the field. The third and fourth items are a sequence of positional
# args and a dictionary of keyword args, to use when creating the
# field instance. When specifying the field class, the path
# ``django.models.db.`` can be omitted for regular Django model fields.
#
EXTRA_MODEL_FIELDS = (
    (
        "mezzanine.pages.models.RichTextPage.image",
        "sorl.thumbnail.ImageField",
        (u"фоновое изображение для заголовка",),
        {
            "blank": True,
            "upload_to": lambda i, f: 'title_backgrounds/%s%s' % \
                (urandom(16).encode('hex'), splitext(f)[1].lower()),
            #"verbose_name": u"фоновое изображение для заголовка",
         },
    ),
    (
        "mezzanine.pages.models.RichTextPage.pre_text",
        "mezzanine.core.fields.RichTextField",
        (u"Текст перед основным содержимым",),
        {"blank": True,},
    ),
)

USE_SOUTH = True


########################
# MAIN DJANGO SETTINGS #
########################
ADMINS = (
    ('Andrey', 'a@andreyshipilov.com'),
)
MANAGERS = ADMINS
TIME_ZONE = None
USE_TZ = True
LANGUAGE_CODE = "ru"
DEBUG = False
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SITE_ID = 1
USE_I18N = True
SECRET_KEY = "6ef10b86-249c-4961-a509-2219d569b3c0d8b6fb54-fae5-48c2-a402-390c072610bf51ce6d5e-acae-4037-abeb-b1f8b7a41c44"
INTERNAL_IPS = ("127.0.0.1",)
ALLOWED_HOSTS = ['*',]
TEMPLATE_LOADERS = (
    "django.template.loaders.filesystem.Loader",
    "django.template.loaders.app_directories.Loader",
)
AUTHENTICATION_BACKENDS = ("mezzanine.core.auth_backends.MezzanineBackend",)
STATICFILES_FINDERS = (
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
#    'django.contrib.staticfiles.finders.DefaultStorageFinder',
)
SLUGIFY = "pytils.translit.slugify"
INLINE_EDITING_ENABLED = False


#############
# DATABASES #
#############
DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.",
        "NAME": "",
        "USER": "",
        "PASSWORD": "",
        "HOST": "",
        "PORT": "",
    }
}


#########
# PATHS #
#########

import os
import sys

PROJECT_ROOT = os.path.dirname(os.path.abspath(__file__))
PROJECT_DIRNAME = PROJECT_ROOT.split(os.sep)[-1]
CACHE_MIDDLEWARE_KEY_PREFIX = PROJECT_DIRNAME
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(PROJECT_ROOT, STATIC_URL.strip("/"))
MEDIA_URL = STATIC_URL + "media/"
MEDIA_ROOT = os.path.join(PROJECT_ROOT, *MEDIA_URL.strip("/").split("/"))
ADMIN_MEDIA_PREFIX = STATIC_URL + "grappelli/"
ROOT_URLCONF = "%s.urls" % PROJECT_DIRNAME
TEMPLATE_DIRS = (os.path.join(PROJECT_ROOT, "templates"),)
TINYMCE_SETUP_JS = "%sjs/custom_tinymce_setup.js" % STATIC_URL


################
# APPLICATIONS #
################
PATHS = (
    os.path.abspath(os.path.join(PROJECT_ROOT, 'apps')),
)
[sys.path.insert(0, i) if i not in sys.path else None for i in PATHS]

INSTALLED_APPS = (
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.redirects",
    "django.contrib.sessions",
    "django.contrib.sites",
    "django.contrib.sitemaps",
    "django.contrib.staticfiles",
    "mezzanine.boot",
    "mezzanine.conf",
    "mezzanine.core",
    "mezzanine.generic",
    #"mezzanine.blog",
    #"mezzanine.forms",
    "mezzanine.pages",
    #"mezzanine.galleries",
    #"mezzanine.twitter",
    #"mezzanine.accounts",
    #"mezzanine.mobile",

    "typogrify",
    "sorl.thumbnail",
    "supercaptcha",
    "django_reset",

    "setup",
    "news",
    "people",
    "projects",
    "reviews",
    "legal",
    "work",
    "banners",
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.contrib.messages.context_processors.messages",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    "django.core.context_processors.media",
    "django.core.context_processors.request",
    "django.core.context_processors.tz",
    "mezzanine.conf.context_processors.settings",
    "people.context_processors.add_random_human",
    "setup.context_processors.add_setup",
)

MIDDLEWARE_CLASSES = (
    "mezzanine.core.middleware.UpdateCacheMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.redirects.middleware.RedirectFallbackMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "mezzanine.core.request.CurrentRequestMiddleware",
    "mezzanine.core.middleware.TemplateForDeviceMiddleware",
    "mezzanine.core.middleware.TemplateForHostMiddleware",
    "mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware",
    # Uncomment the following if using any of the SSL settings:
    # "mezzanine.core.middleware.SSLRedirectMiddleware",
    "mezzanine.pages.middleware.PageMiddleware",
    "mezzanine.core.middleware.FetchFromCacheMiddleware",
)

PACKAGE_NAME_FILEBROWSER = "filebrowser_safe"
PACKAGE_NAME_GRAPPELLI = "grappelli_safe"


#########################
# OPTIONAL APPLICATIONS #
#########################
OPTIONAL_APPS = (
    "debug_toolbar",
    "django_extensions",
    "compressor",
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

DEBUG_TOOLBAR_CONFIG = {"INTERCEPT_REDIRECTS": False}

CAPTCHA_SYMBOLS = u'123456789'
CAPTCHA_LENGTH = 3
CAPTCHA_SIZE = (100, 50)
CAPTCHA_FOREGROUND_COLORS = ((150, 150, 150),)
CAPTCHA_BACKGROUND_COLOR = (255, 255, 255)
CAPTCHA_DEFAULT_ERROR_MESSAGE = u'Вы ввели неправильные символы'
CAPTCHA_HTML_TEMPLATE = """
<div>
<img src="%(src)s?%(rnd)s" alt="%(alt)s" width="%(width)s" height="%(height)s" />
</div>
<input%(input_attrs)s maxlength="%(length)s" />
"""

###################
# DEPLOY SETTINGS #
###################

# These settings are used by the default fabfile.py provided.
# Check fabfile.py for defaults.

# FABRIC = {
#     "SSH_USER": "", # SSH username
#     "SSH_PASS":  "", # SSH password (consider key-based authentication)
#     "SSH_KEY_PATH":  "", # Local path to SSH key file, for key-based auth
#     "HOSTS": [], # List of hosts to deploy to
#     "VIRTUALENV_HOME":  "", # Absolute remote path for virtualenvs
#     "PROJECT_NAME": "", # Unique identifier for project
#     "REQUIREMENTS_PATH": "", # Path to pip requirements, relative to project
#     "GUNICORN_PORT": 8000, # Port gunicorn will listen on
#     "LOCALE": "en_US.UTF-8", # Should end with ".UTF-8"
#     "LIVE_HOSTNAME": "www.example.com", # Host for public site.
#     "REPO_URL": "", # Git or Mercurial remote repo URL for the project
#     "DB_PASS": "", # Live database password
#     "ADMIN_PASS": "", # Live admin user password
# }


##################
# LOCAL SETTINGS #
##################

# Allow any settings to be defined in local_settings.py which should be
# ignored in your version control system allowing for settings to be
# defined per machine.
try:
    from local_settings import *
except ImportError:
    pass


####################
# DYNAMIC SETTINGS #
####################

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
