"""
Django settings for untitled project.

Generated by 'django-admin startproject' using Django 1.8.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'c(ri*s_b&7ogijq3$kp8l863kxhc9a=%$w4id00p+hx49dp%p('

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True


# Application definition

INSTALLED_APPS = (
    'ModelTracker',
    'TestApp',
)

# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'ModelTrackerTest',
        'USER': 'root',
        'PASSWORD': 'password',
        'HOST':'127.0.0.1', #127.0.0.1
        'port':'3306',
                }
            }



# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/
