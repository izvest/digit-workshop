import os

import environ

checkout_dir = environ.Path(__file__) - 2
assert os.path.exists(checkout_dir('manage.py'))

parent_dir = checkout_dir.path('..')
if parent_dir() != '/' and os.path.isdir(parent_dir('etc')):
    env_file = parent_dir('etc/env')
    default_var_root = parent_dir('var')
else:
    env_file = checkout_dir('.env')
    default_var_root = checkout_dir('var')

env = environ.Env(
    DEBUG=(bool, False),
    TIER=(str, 'dev'),  # one of: prod, qa, stage, test, dev
    SECRET_KEY=(str, 'foo'),
    VAR_ROOT=(str, default_var_root),
    ALLOWED_HOSTS=(list, []),
    DATABASE_URL=(str, 'sqlite:///var/db.sqlite3'),
    CACHE_URL=(str, 'locmemcache://'),
    EMAIL_URL=(str, 'consolemail://'),
    SENTRY_DSN=(str, ''),
)
if os.path.exists(env_file):
    env.read_env(env_file)


DEBUG = env.bool('DEBUG')
TIER = env.str('TIER')
SECRET_KEY = env.str('SECRET_KEY')
if DEBUG and not SECRET_KEY:
    SECRET_KEY = 'xxx'

ALLOWED_HOSTS = env.list('ALLOWED_HOSTS')

DATABASES = {'default': env.db()}
CACHES = {'default': env.cache()}
vars().update(env.email_url())  # EMAIL_BACKEND etc.

var_root = env.path('VAR_ROOT')
if not os.path.isdir(var_root()):
    os.makedirs(var_root())

MEDIA_ROOT = var_root('media')
STATIC_ROOT = var_root('static')
MEDIA_URL = "/media/"
STATIC_URL = "/static/"
STATICFILES_STORAGE = 'django.contrib.staticfiles.storage.ManifestStaticFilesStorage'

ROOT_URLCONF = 'digit_project.urls'
WSGI_APPLICATION = 'digit_project.wsgi.application'

LANGUAGE_CODE = 'fi'
TIME_ZONE = 'Europe/Helsinki'
USE_I18N = True
USE_L10N = True
USE_TZ = True


INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
