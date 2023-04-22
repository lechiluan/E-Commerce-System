"""
Django settings for ecommerce project.

Generated by 'django-admin startproject' using Django 4.1.7.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

from pathlib import Path
import os
import cloudinary
import dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# SECURITY WARNING: keep the secret key used in production secret!
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIl_FROM = os.environ.get('EMAIL_FROM')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
EMAIL_USE_TLS = True
PASSWORD_RESET_TIMEOUT = 259200

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
# Add .env variables anywhere before SECRET_KEY
dotenv_file = os.path.join(BASE_DIR, ".env")
if os.path.isfile(dotenv_file):
    dotenv.load_dotenv(dotenv_file)

# UPDATE secret key
SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY TO USE HTTPS
# SESSION_COOKIE_SECURE = True  # for https only, it uses to secure session
# CSRF_COOKIE_SECURE = True  # for https only, it uses to secure csrf token
# SECURE_SSL_REDIRECT = True  # for https only, it uses to redirect http to https

# SECURITY WARNING: don't run with debug turned on in production!
# DEBUG = True
DEBUG = False

# ALLOWED_HOSTS is a list of strings representing the host/domain names that this Django site can server
ALLOWED_HOSTS = ['127.0.0.1', 'localhost', 'lclshop.herokuapp.com', 'lclshop.up.railway.app']
CSRF_TRUSTED_ORIGINS = ['https://lclshop.up.railway.app', 'https://lclshop.herokuapp.com']

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',  # for admin
    'django.contrib.auth',  # for authentication
    'django.contrib.contenttypes',  # for content types
    'django.contrib.sessions',  # for sessions
    'django.contrib.messages',  # for messages
    'django.contrib.staticfiles',  # for static files
    'main.apps.MainConfig',  # for main app
    'dashboard.apps.DashboardConfig',  # for dashboard app
    'customer.apps.CustomerConfig',  # for customer app
    'crispy_forms',  # for crispy forms
    'tinymce',  # for tinymce editor
    'captcha',  # for google captcha
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',  # for security
    'django.contrib.sessions.middleware.SessionMiddleware',  # for sessions
    'django.middleware.common.CommonMiddleware',  # for common middleware
    'django.middleware.csrf.CsrfViewMiddleware',  # for csrf token
    'django.contrib.auth.middleware.AuthenticationMiddleware',  # for authentication
    'django.contrib.messages.middleware.MessageMiddleware',  # for messages middleware
    'django.middleware.clickjacking.XFrameOptionsMiddleware',  # for clickjacking
    'whitenoise.middleware.WhiteNoiseMiddleware',  # for whitenoise
]
ROOT_URLCONF = 'ecommerce.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(BASE_DIR / 'templates'),
                 (BASE_DIR / 'main/templates'),
                 (BASE_DIR / 'dashboard/templates'),
                 (BASE_DIR / 'customer/templates')],  # for templates folder
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',  # for debug context processor
                'django.template.context_processors.request',  # for request context processor
                'django.contrib.auth.context_processors.auth',  # for auth context processor
                'django.contrib.messages.context_processors.messages',  # for messages context processor
                'main.context_processors.categories',  # for categories context processor
                'main.context_processors.brands',  # for brands context processor
            ],
        },
    },
]

WSGI_APPLICATION = 'ecommerce.wsgi.application'  # for wsgi application

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('DB_USER'),
        'PASSWORD': os.environ.get('DB_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Ho_Chi_Minh'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = [(BASE_DIR / 'static'),
                    (BASE_DIR / 'main/static'),
                    (BASE_DIR / 'dashboard/static'),
                    (BASE_DIR / 'customer/static')]  # use to find static files
STATIC_ROOT = BASE_DIR / 'staticfiles'  # use to collect static files use when use public hosting
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

CLOUDINARY = {
  'cloud_name': os.environ.get('CLOUDINARY_CLOUD_NAME'),
  'api_key': os.environ.get('CLOUDINARY_API_KEY'),
  'api_secret': os.environ.get('CLOUDINARY_API_SECRET'),
}
MEDIA_URL = 'https://res.cloudinary.com/hsflo3cmj/image/upload/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

# Connect to bootstrap4 for crispy forms
CRISPY_TEMPLATE_PACK = 'bootstrap4'
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap4"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'  # for big auto field

LOGIN_REDIRECT_URL = "/"  # for login redirect url after login
LOGOUT_REDIRECT_URL = "/"  # for logout redirect url after logout

# Configure tinymce editor for django
TINYMCE_DEFAULT_CONFIG = {
    'selector': 'textarea',
    'plugins': 'print preview fullpage powerpaste searchreplace autolink directionality advcode visualblocks visualchars fullscreen image link media template codesample table charmap hr pagebreak nonbreaking anchor toc insertdatetime advlist lists wordcount imagetools textpattern noneditable help quickbars emoticons code legacyoutput ltr rtl spellchecker',
    'toolbar': 'undo redo | formatselect | bold italic strikethrough forecolor backcolor | link image media | alignleft aligncenter alignright alignjustify fullscreen | numlist bullist outdent indent | removeformat | help | codesample code | emoticons hr image link media nonbreaking pagebreak preview print save searchreplace table template toc charmap fullscreen insertdatetime media noneditable powerpaste advcode advlist anchor autolink codesample code directionality fullpage help image insertdatetime link lists media nonbreaking pagebreak paste print quickbars save searchreplace table template textpattern toc visualblocks visualchars wordcount | fullscreen | cut copy paste | selectall | searchreplace | charmap | spellchecker | pagebreak | nonbreaking | template | print | preview | save | insertdatetime | anchor | image | media | codesample | help | code | emoticons | hr | link | table | toc',
    'menubar': 'file edit view insert format tools table help',
    'toolbar_mode': 'sliding',
    'toolbar_sticky': True,
}
TINYMCE_UPLOAD_DIR = 'uploads/'
TINYMCE_UPLOAD_NAME = 'tinymce_upload'

# Config for Google Captcha
RECAPTCHA_PUBLIC_KEY = os.environ.get('RECAPTCHA_PUBLIC_KEY')
RECAPTCHA_PRIVATE_KEY = os.environ.get('RECAPTCHA_PRIVATE_KEY')
SILENCED_SYSTEM_CHECKS = ['captcha.recaptcha_test_key_error']
