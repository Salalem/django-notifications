# -*- coding: utf-8 -*-
"""
Django settings for salalem_notifications project.

Generated by 'django-admin startproject' using Django 2.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/2.1/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'qv=7zpi@(*^0c@=vch43sg=aac5%4nwha4rd=n)9%wr17%7wj+'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ["localhost"]


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'lms_events_handlers',
    'salalem_notifications',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


# Database
# https://docs.djangoproject.com/en/2.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/2.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.1/howto/static-files/

STATIC_URL = '/static/'

DJANGO_NOTIFICATIONS_CONFIG = {
    "PAGINATE_BY": 20,
    "USE_JSONFIELD": False,
    "SOFT_DELETE": False,
    "NUM_TO_FETCH": 10,
}

# django propaganda
QUEUE_PROTOCOL = os.environ.get("QUEUE_PROTOCOL", "amqp")
QUEUE_USER = os.environ.get("QUEUE_USER", "admin")
QUEUE_PASSWORD = os.environ.get("QUEUE_PASSWORD", "123")
QUEUE_HOST = os.environ.get("QUEUE_HOST", "localhost")
QUEUE_PORT = os.environ.get("QUEUE_PORT", "5672")
QUEUE_VHOST = os.environ.get("QUEUE_VHOST", "lms")

PROPAGANDA_BROKER_URL = (
    QUEUE_PROTOCOL
    + "://"
    + QUEUE_USER
    + ":"
    + QUEUE_PASSWORD
    + "@"
    + QUEUE_HOST
    + ":"
    + QUEUE_PORT
    + "/"
    + QUEUE_VHOST
)


# Email settings
EMAIL_BACKEND = "sendgrid_backend.SendgridBackend"
SENDGRID_API_KEY = os.environ.get("SENDGRID_API_KEY", "API_KEY")

SENDGRID_SANDBOX_MODE_IN_DEBUG = False
