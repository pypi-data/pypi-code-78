"""
Django settings for website project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os, syst3m
from fil3s import *

# Environment.
SOURCE = Directory(gfp.base(__file__, back=3))
DATABASE = Directory(syst3m.env.get("DATABASE", default=str(SOURCE)))
PRODUCTION = syst3m.env.get("PRODUCTION", default=True, format=bool)
DOMAIN = syst3m.env.get("DOMAIN", default=None)
SECRET_KEY = syst3m.env.get("DJANGO_SECRET_KEY", default=String().generate(length=128, capitalize=True, digits=True, special=True))
WEBSITE_BASE = syst3m.env.get("WEBSITE_BASE", default=None)
if WEBSITE_BASE == None:
    raise ValueError("Improperly configured run, env variable [WEBSITE_BASE] is None.")
    
# Match production,
if PRODUCTION:

    # disable logs.
    DEBUG = False

    # security settings.
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SESSION_COOKIE_HTTPONLY = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_HSTS_PRELOAD = True
    X_FRAME_OPTIONS = 'DENY'

else:
    SECURE_SSL_REDIRECT = False
    DEBUG = True


# Add allowed hosts.
ALLOWED_HOSTS = []
if DOMAIN not in [None, ""]:
    for url in [
        DOMAIN,
    ]:
        if url != None:
            ALLOWED_HOSTS.append(url)
            ALLOWED_HOSTS.append("www."+url)
            ALLOWED_HOSTS.append("http://"+url)
            ALLOWED_HOSTS.append("https://"+"www."+url)
if PRODUCTION == False:
    ALLOWED_HOSTS.append("*")

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
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

ROOT_URLCONF = '__defaults__.django.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            SOURCE.join("apps"),
            WEBSITE_BASE,
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

WSGI_APPLICATION = '__defaults__.django.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATABASE.join("data/db.sqlite3"),
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_ROOT = '/www-data/static/'
STATIC_URL = '/static/'
STATICFILES_DIRS = [
    SOURCE.join('__defaults__/static'),
]
