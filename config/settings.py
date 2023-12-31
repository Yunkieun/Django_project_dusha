"""
Django settings for config project.

Generated by 'django-admin startproject' using Django 4.2.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
import json
import sys
from datetime import timedelta

#카카오 로그인 설정 시작
BASE_DIR = Path(__file__).resolve().parent.parent



# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-^eetx2qpisue%x@8g7nxmtv(z+60repknyvymwp%-d^695h_22'

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
    'django.contrib.humanize',
    'item',
    'board',
    'common',
    'cart',
    'crispy_forms',
    'coupon',
    'widget_tweaks',
    'order',
    # 소셜로그인 설정 start
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'django.contrib.sites',
    'allauth.socialaccount.providers.naver',
    'allauth.socialaccount.providers.kakao',
    'allauth.socialaccount.providers.google',
    # 소셜로그인 설정 end

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
# 소셜로그인 설정 start
SITE_ID = 1
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend',
)

# 소셜로그인 설정 end




ROOT_URLCONF = 'config.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / 'templates'],
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

WSGI_APPLICATION = 'config.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.2/topics/i18n/

LANGUAGE_CODE = 'ko-kr'

TIME_ZONE = 'Asia/Seoul'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.2/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [BASE_DIR / 'static']

MEDIA_ROOT = os.path.join(BASE_DIR, '_media')
MEDIA_URL = '/media/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

CART_ID = 'cart_id'

LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'  #로그아웃 성공시 루트(인덱스)로 이동
ACCOUNT_SIGNUP_AUTO_LOGIN = True
ACCOUNT_SIGNUP_REDIRECT_URL = '/' #로그인후 이동경로
ACCOUNT_AUTHENTICATION_METHOD = 'email' #로그인시 email로 사용하게하는 기능
ACCOUNT_EMAIL_VERIFICATION = 'none'
ACCOUNT_EMAIL_REQUIRED = True           #이메일 필수 조건
ACCOUNT_USERNAME_REQUIRED = True       #username 사용여부
ACCOUNT_LOGIN_ATTEMPTS_LIMIT = 5        #5번실패시 지정한시간만큼 사용x
ACCOUNT_LOGIN_ATTEMPTS_TIMEOUT = 60 # 1분동안 사용못함

ACCOUNT_SESSION_REMEMBER = True #브라우저를 닫아도 세션기록 유지
SOCIALACCOUNT_LOGIN_ON_GET = True
ACCOUNT_LOGOUT_REDIRECT_URL ='/'
ACCOUNT_LOGOUT_ON_GET = True

# 기본 유저모델변경
AUTH_USER_MODEL = "common.User"

