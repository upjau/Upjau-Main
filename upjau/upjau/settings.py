"""
Django settings for upjau project.

Generated by 'django-admin startproject' using Django 1.11.17.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '89ur5-@$n_qbc8wogftm*8++e52gclz+)m@s*$_$*@_jzn(f=$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Self-defined
    'accounts',
    'farmer',
    'logistics',
    'industry',

    # Required
    'bootstrap_modal_forms',
]

AUTH_USER_MODEL = 'accounts.Profile'

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'upjau.urls'

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

WSGI_APPLICATION = 'upjau.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'Upjau_Main',
        'USER': 'anway',
        'PASSWORD': 'anway123',
        'HOST': 'localhost',
        'PORT': '',
    },
    #'farmer': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'Upjau_Farmer',
    #    'USER': 'anway',
    #    'PASSWORD': 'anway123',
    #    'HOST': 'localhost',
    #    'PORT': '',
    #},
    #'admin': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'Upjau_Admin',
    #    'USER': 'anway',
    #    'PASSWORD': 'anway123',
    #    'HOST': 'localhost',
    #    'PORT': '',
    #},
    #'logistics': {
    #    'ENGINE': 'django.db.backends.mysql',
    #    'NAME': 'Upjau_Logistics',
    #    'USER': 'anway',
    #    'PASSWORD': 'anway123',
    #    'HOST': 'localhost',
    #    'PORT': '',
    #}
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

MEDIA_URL = '/media/'
iMEDIA_ROOT = os.path.join(BASE_DIR, 'media')

