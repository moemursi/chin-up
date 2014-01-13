import os
import sys

from os.path import abspath, join

ADMINS = ()

ALLOWED_HOSTS = ['*', ]
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
MANAGERS = ADMINS

# Environment variables
DATABASE_NAME = os.environ.get("DATABASE_NAME")
DATABASE_USERNAME = os.environ.get("DATABASE_USERNAME")
DATABASE_PASSWORD = os.environ.get("DATABASE_PASSWORD")
DATABASE_HOST = os.environ.get("DATABASE_HOST", '')
SENTRY_DSN = os.environ.get("SENTRY_DSN", '')
FACEBOOK_API_CLIENT_ID = os.environ.get("FACEBOOK_API_CLIENT_ID")
FACEBOOK_API_SECRET = os.environ.get("FACEBOOK_API_SECRET")

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': DATABASE_NAME,
        'USER': DATABASE_USERNAME,
        'PASSWORD': DATABASE_PASSWORD,
        'HOST': DATABASE_HOST,
        'PORT': '',
    }
}

# Include other apps
PROJECT_ROOT = join(abspath(os.path.curdir), "project")
sys.path.append(join(PROJECT_ROOT, 'apps'))

# Directories
PROJECT_DIR = abspath(join(PROJECT_ROOT, ".."))
MEDIA_ROOT = abspath(join(PROJECT_ROOT, 'mediafiles'))
MEDIA_URL = '/media/'
STATIC_ROOT = abspath(join(PROJECT_ROOT, 'staticfiles'))
STATIC_URL = '/static/'

STATICFILES_DIRS = (abspath(join(PROJECT_ROOT, 'static')),)

TEMPLATE_DIRS = (abspath(join(PROJECT_ROOT, 'templates')),)

TIME_ZONE = 'America/Chicago'
LANGUAGE_CODE = 'en-us'

SITE_ID = 1

USE_I18N = True
USE_L10N = True
USE_TZ = False

# List of finder classes that know how to find static files in
# various locations.
STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder'
)

# Make this unique, and don't share it with anybody.
SECRET_KEY = 'p*)lhh6km9=$*@3fikdh)-g3pyv2e4)ma$p5i6ri)vghh4rus7'

# List of callables that know how to import templates from various sources.
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    "django.core.context_processors.request",
    'django.contrib.auth.context_processors.auth',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

ROOT_URLCONF = 'chinup.urls'

# Python dotted path to the WSGI application used by Django's runserver.
WSGI_APPLICATION = 'chinup.wsgi.application'

BASE_AND_LIBRARY_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'south',
    #'debug_toolbar',
    'gunicorn',
)

CHIN_UP_APPS = (
    'chinup',
)

INSTALLED_APPS = BASE_AND_LIBRARY_APPS + CHIN_UP_APPS

# registration/login
LOGIN_REDIRECT_URL = '/'

# Nose
TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

# Logging
LOGGING = {
    'version': 1,
    'disable_existing_loggers': True,
    'root': {
        'level': 'WARNING',
    },
    'formatters': {
        'verbose': {
            'format': '%(levelname)s %(asctime)s %(module)s %(process)d %(thread)d %(message)s'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'verbose'
        }
    },
    'loggers': {
        'django.db.backends': {
            'level': 'ERROR',
            'handlers': ['console'],
            'propagate': False,
        },
    },
}
