# -*- coding: utf-8 -*-
"""
Django settings for renefernandezcom project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
import sys


BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '<GENERATE A SECRET KEY>'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

TEMPLATE_DEBUG = False

ADMINS = (
    ('<YOUR NAME>', '<YOUR EMAIL>'),
)

MANAGERS = ADMINS

ALLOWED_HOSTS = ['<DOMAIN 1>','<DOMAIN 2>']

STATIC_ROOT = '/home/to/your/project/'

# URL prefix for static files.
# Example: "http://media.lawrence.com/static/"
STATIC_URL = 'http://yourdomain.com/static/'

# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'captcha',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.core.context_processors.i18n',
    'django.contrib.auth.context_processors.auth',
	'django.contrib.messages.context_processors.messages',
)

ROOT_URLCONF = 'renefernandezcom.urls'

WSGI_APPLICATION = 'renefernandezcom.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
        'NAME': '<PGSQL DB>',                      # Or path to database file if using sqlite3.
        'USER': '<PGSQL USER>',                      # Not used with sqlite3.
        'PASSWORD': '<PGSQL PASSWORD>',                  # Not used with sqlite3.
        'HOST': '',                      # Set to empty string for localhost. Not used with sqlite3.
        'PORT': '<PGSQL PORT>',                      # Set to empty string for default. Not used with sqlite3.
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static"),
    '/renefernandezcom/static/',
)

LOCALE_PATHS = (
    os.path.join(BASE_DIR, "locale"),
)

#Añadido para cargar las plantillas
TEMPLATE_DIRS = (
    # Put strings here, like "/home/html/django_templates" or "C:/www/django/templates".
    # Always use forward slashes, even on Windows.
    # Don't forget to use absolute paths, not relative paths.
    os.path.join(os.path.dirname(__file__), 'templates').replace('\\','/'),
)

CAPTCHA_CHALLENGE_FUNCT = 'captcha.helpers.math_challenge'
CAPTCHA_NOISE_FUNCTIONS = ()
CAPTCHA_LETTER_ROTATION = (0, 1)

EMAIL_HOST = '<SMTP.YOURHOST.COM>'
EMAIL_HOST_USER = '<YOUR EMAIL USERNAME>'
EMAIL_HOST_PASSWORD = '<YOUR EMAIL PASSWORD>'
DEFAULT_FROM_EMAIL = '<YOUR EMAIL FROM>'
SERVER_EMAIL = '<YOUR EMAIL TO>'

if 'test' in sys.argv:
    CAPTCHA_TEST_MODE = True