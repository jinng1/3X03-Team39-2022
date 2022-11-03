"""
Django settings for healthcaretether project.

Generated by 'django-admin startproject' using Django 4.1.2.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.1/ref/settings/
"""

import os
from pathlib import Path
from dotenv import load_dotenv
from django.conf.global_settings import PASSWORD_HASHERS as DEFAULT_PASSWORD_HASHERS


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
load_dotenv(os.path.join(BASE_DIR, '.env'))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG = False
#DEBUG = int(os.environ.get("DEBUG", default=0))

ALLOWED_HOSTS =  ['healthcaretether.xyz']

CSRF_TRUSTED_ORIGINS = ['https://healthcaretether.xyz']
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")





# CSRF_TRUSTED_ORIGINS = ['http://localhost:1337']

# Application definition

INSTALLED_APPS = [
    #'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'crispy_forms',
    'crispy_bootstrap5',
    'main',
    'mfa',
    'sslserver',
    'axes',
]


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'axes.middleware.AxesMiddleware',
]

ROOT_URLCONF = 'healthcaretether.urls'

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

WSGI_APPLICATION = 'healthcaretether.wsgi.application'

AUTHENTICATION_BACKENDS = [
    # AxesBackend should be the first backend in the AUTHENTICATION_BACKENDS list.
    'axes.backends.AxesBackend',

    # Django ModelBackend is the default authentication backend.
    'django.contrib.auth.backends.ModelBackend',
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    "default": {
        "ENGINE": os.environ.get("SQL_ENGINE", "django.db.backends.sqlite3"),
        "NAME": os.environ.get("SQL_DATABASE", BASE_DIR / "db.sqlite3"),
        "USER": os.environ.get("SQL_USER", "user"),
        "PASSWORD": os.environ.get("SQL_PASSWORD", "password"),
        "HOST": os.environ.get("SQL_HOST", "localhost"),
        "PORT": os.environ.get("SQL_PORT", "5432"),
    }
}

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': BASE_DIR / 'db.sqlite3',
#     }
# }

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

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/home/app/web/static/'
#STATIC_ROOT = BASE_DIR / 'staticfiles/'
#STATICFILES_DIRS = [
#     os.path.join(BASE_DIR,'static'),
#    '/home/app/web/static/'
#]
#    os.path.join(BASE_DIR,'static')
#]

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
AUTH_USER_MODEL = 'main.CustomUser'
#LOGIN_REDIRECT_URL = "/"
CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"
CRISPY_TEMPLATE_PACK = 'bootstrap5'
LOGIN_URL="/auth/login"


# MFA Settings

MFA_UNALLOWED_METHODS=('U2F', 'TOTP', 'Trusted_Devices', 'Email', 'RECOVERY')   # Methods that shouldn't be allowed for the user e.g ('TOTP','U2F',)
MFA_LOGIN_CALLBACK="healthcaretether.auth.create_session"      # A function that should be called by username to login the user in session
MFA_RECHECK=True           # Allow random rechecking of the user
MFA_REDIRECT_AFTER_REGISTRATION="mfa_home"   # Allows Changing the page after successful registeration
MFA_SUCCESS_REGISTRATION_MSG = "Login" # The text of the link
MFA_RECHECK_MIN=10         # Minimum interval in seconds
MFA_RECHECK_MAX=30         # Maximum in seconds
MFA_QUICKLOGIN=False        # Allow quick login for returning users by provide only their 2FA
MFA_ALWAYS_GO_TO_LAST_METHOD = False # Always redirect the user to the last method used to save a click (Added in 2.6.0).
MFA_RENAME_METHODS={} #Rename the methods in a more user-friendly way e.g {"RECOVERY":"Backup Codes"} (Added in 2.6.0)
MFA_HIDE_DISABLE=('FIDO2',)     # Can the user disable his key (Added in 1.2.0).  
PASSWORD_HASHERS = DEFAULT_PASSWORD_HASHERS # Comment if PASSWORD_HASHER already set in your settings.py
PASSWORD_HASHERS += ['mfa.recovery.Hash'] 
RECOVERY_ITERATION = 350000 #Number of iteration for recovery code, higher is more secure, but uses more resources for generation and check...

TOKEN_ISSUER_NAME="healthcaretether"      #TOTP Issuer name


U2F_APPID="https://healthcaretether.xyz"    #URL For U2F
FIDO_SERVER_ID="healthcaretether.xyz"      # Server rp id for FIDO2, it is the full domain of your project
FIDO_SERVER_NAME="healthcaretether"


#Session settings
SESSION_ENGINE ='django.contrib.sessions.backends.db'
SESSION_COOKIE_AGE = 43200 #12 hours of active use
SESSION_EXPIRE_AT_BROWSER_CLOSE = True
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'
SESSION_COOKIE_HTTPONLY = True
SESSION_COOKIE_SAMESITE = 'Strict'
SESSION_COOKIE_SECURE = True

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    
    'formatters':{
        'main_formatter':{
            'format': "{asctime} - {levelname} - {module} - {message}",
            'style': '{',
        }
    },
    'handlers':{
        'console':{
            'class': "logging.StreamHandler",
            'formatter': "main_formatter",
        },
        'file':{
            'class': "logging.FileHandler",
            'filename': 'info.log',
            'formatter': "main_formatter",
        },
    },
    'loggers':{
        'main':{
            'handlers': ['file','console'],
            'propagate': True,
            'level': "INFO",
        },
    },

}


AXES_META_PRECEDENCE_ORDER = [
    'HTTP_X_FORWARDED_FOR',
    'REMOTE_ADDR',
]

#axes settings
AXES_LOCK_OUT_BY_USER_OR_IP=True
AXES_FAILURE_LIMIT=10


#testing webhook

