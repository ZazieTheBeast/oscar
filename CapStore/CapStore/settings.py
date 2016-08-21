#settings.py
from oscar import get_core_apps
from oscar import OSCAR_MAIN_TEMPLATE_DIR
from oscar.defaults import *
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))

location = lambda x: os.path.join(
   os.path.dirname(os.path.realpath(__file__)), x
)

SECRET_KEY = 'pa--blableitnhczk5ublsx%)*bla^sox86&*slbs&y'
DEBUG = True
TEMPLATE_DEBUG = True
ALLOWED_HOSTS = []

STATIC_FINDERS = (
    'django.contrib.staticfiles.finders.FilesystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django.contrib.flatpages',
    'south',
    'compressor',
] + get_core_apps()


SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    'django.template.loaders.eggs.Loader',
)
TEMPLATE_DIRS = (
    location('templates'),
    OSCAR_MAIN_TEMPLATE_DIR,
)
TEMPLATE_CONTEXT_PROCESSORS = (
    "django.contrib.auth.context_processors.auth",
    "django.core.context_processors.request",
    "django.core.context_processors.debug",
    "django.core.context_processors.i18n",
    "django.core.context_processors.media",
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages",
    'oscar.apps.search.context_processors.search_form',
    'oscar.apps.promotions.context_processors.promotions',
    'oscar.apps.checkout.context_processors.checkout',
    'oscar.apps.customer.notifications.context_processors.notifications',
    'oscar.apps.context_processors.metadata',
)   

AUTHENTICATION_BACKNDS = (
    'oscar.apps.customer.auth_backends.Emailbackend',
    'django.contrib.auth.backends.ModelBackend',
)

HAYSTACK_CONNECTIONS = {
    'default' : {
        'ENGINE' : 'haystack.backends.simple_backend.SimpleEngine',
    },
} 

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'oscar.apps.basket.middleware.BasketMiddleware',
    'django.middleware.transaction.TransctionMiddleware',
    'django.contrib.flatpages.middleware.FlatpageFallbackMiddleware'
)

ROOT_URLCONF = 'rdyact.urls'
WSGI_APPLICATION = 'rdyact.wsgi.application'
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
        'USER' : '',
        'PASSWORD' : '',
        'HOST' : '',
        'PORT' : '',
        'ATOMIC_REQUESTS' : True,
    }
}

LANGUAGE_CODE = 'en-us'
SITE_ID = 1
TIME_ZONE = 'UTC'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_URL = '/static/'
STATIC_ROOT = ''
STATIC_DIRS = (
)
MEDIA_ROOT = ''
MEDIA_URL = ''