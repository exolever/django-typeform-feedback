# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import

import os
import django

from celery import current_app


DEBUG = True
USE_TZ = True
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3d#8x9iy+b#1f1g&12^6lf&u*mzqik$d_1m0-i^x2jg(y6pi#*'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME', 'travis_ci_test'),
        'USER': os.environ.get('DB_USER', 'exolever'),
        'PASSWORD': os.environ.get('DB_PASS', 'exolever'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', '5432'),
    }
}

ROOT_URLCONF = 'tests.urls'

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sites',
    'typeform_feedback',
    'rest_framework',
    'foo',
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
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

# Celery configuration

REDIS_HOST = os.environ.get('REDIS_HOST', 'localhost')
REDIS_PORT = os.environ.get('REDIS_PORT', 6379)
REDIS_CELERY_DB = 1

CELERY_SERVICE_BROKER_URL = os.environ.get(
    'BROKER_URL',
    'redis://{}:{}/{}'.format(
        REDIS_HOST,
        REDIS_PORT,
        REDIS_CELERY_DB
    )
)

current_app.conf.task_always_eager = True
current_app.conf.task_eager_propagates = True
