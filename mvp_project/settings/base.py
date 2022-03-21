"""
Django settings for mvp_project project.

Generated by 'django-admin startproject' using Django 3.0.2.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
from secrets import *
from django.contrib.messages import constants as messages

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(os.path.join(__file__, os.pardir))))

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/


# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = ''

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',  # new

    # 3-rd part
    # 'debug_toolbar',
    'bootstrap4',
    'rest_framework',
    'rest_framework_swagger',
    'rest_framework_simplejwt.token_blacklist',
    'corsheaders',
    'social_django',
    'analytical',
    'django_nose',

    # local
    'crispy_forms',
    'users.apps.UsersConfig',
    'pages.apps.PagesConfig',
    'api.apps.ApiConfig',
    'cms.apps.CmsConfig',
    'shop.apps.ShopConfig',
    'payment.apps.PaymentConfig',
    'drf_yasg',
    'fullurl',

]

# Use nose to run all tests
# TEST_RUNNER = 'django_nose.NoseTestSuiteRunner'
#
# NOSE_ARGS = [
#     '--with-coverage',
#     '--cover-package=users, api, cms, pages',
#     # '--cover-html',
# ]

CRISPY_TEMPLATE_PACK = 'bootstrap4'

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware',  # new for cors-headers
    'django.middleware.common.CommonMiddleware',  # new for cors-headers
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  # new (for translate)
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # new (for debugger tool)
    # 'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'mvp_project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            'templates/',
            'users/templates/',
            'pages/templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.i18n',  # new for lang
                'social_django.context_processors.backends',  # python social
                'social_django.context_processors.login_redirect',  # python social
                'cms.context_processors.health_data_and_result_not_empty',
            ],
        },
    },
]

WSGI_APPLICATION = 'mvp_project.wsgi.application'

MESSAGE_TAGS = {
    messages.DEBUG: 'alert-info',
    messages.INFO: 'alert-info',
    messages.SUCCESS: 'alert-success',
    messages.WARNING: 'alert-warning',
    messages.ERROR: 'alert-danger',
}

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
        'OPTIONS': {
            'min_length': 6,
        }
    },
    # {
    #     'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    # },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
    # {
    #     'NAME': 'users.validators.SpecialCharValidator',
    #     'OPTIONS': {
    #         'special_chars': (
    #             '!', ';', ':', ')', '(', '_', '+', '/', '-', '.', ',', '|', '`', '~',
    #             '<', '>', '{', '}', '№', '@', '#', '$', '%', '^', '&', '*', '?'
    #         )
    #     },
    # },
  ]

# new to strong-secure hash passwords
PASSWORD_HASHERS = [
    'django.contrib.auth.hashers.Argon2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2PasswordHasher',
    'django.contrib.auth.hashers.PBKDF2SHA1PasswordHasher',
    'django.contrib.auth.hashers.BCryptSHA256PasswordHasher',
]

# UserModel
AUTH_USER_MODEL = 'users.CustomUser'

# Internationalization
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en'

LANGUAGES = (
    ('en', 'English'),
    ('ru', 'Russian'),
)

PREFIX_DEFAULT_LANGUAGE = False

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)


SHORT_DATE_FORMAT = 'j.m.Y'
SHORT_DATETIME_FORMAT = 'j.m.Y H:i:s'
DATE_FORMAT = 'j E Y'
DATETIME_FORMAT = 'j E Y H:i:s'
TIME_FORMAT = 'H:i:s'
MONTH_DAY_FORMAT = 'F, j'
YEAR_MONTH_FORMAT = 'F Y'

DATE_INPUT_FORMATS = [
    '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y',  # '2006-10-25', '10/25/2006', '10/25/06'
    '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
    '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
    '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
    '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
    '%d.%m.%Y',                         # 25.10.2006
]

DATETIME_INPUT_FORMATS = [
    '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
    '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
    '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
    '%Y-%m-%d',              # '2006-10-25'
    '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
    '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
    '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
    '%m/%d/%Y',              # '10/25/2006'
    '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
    '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
    '%m/%d/%y %H:%M',        # '10/25/06 14:30'
    '%m/%d/%y',              # '10/25/06'
    '%d.%m.%Y %H:%M:%S',     # '25.10.2006 14:30:59'
    '%d.%m.%Y %H:%M',        # '25.10.2006 14:30'
]

TIME_INPUT_FORMATS = [
    '%H:%M:%S',     # '14:30:59'
    '%H:%M:%S.%f',  # '14:30:59.000200'
    '%H:%M',        # '14:30'
]

FIRST_DAY_OF_WEEK = 1  # Monday


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static/'),]
STATIC_ROOT = os.path.join(BASE_DIR, 'static/')
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'mvp_project/static/'), ]
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

LOGIN_URL = "users:login"
LOGIN_REDIRECT_URL = 'users:profile'
LOGOUT_REDIRECT_URL = "pages:index"
PASSWORD_RESET_TIMEOUT_DAYS = 1


SITE_ID = 1

AUTHENTICATION_BACKENDS = {
    # 'django.contrib.auth.backends.ModelBackend',
    'users.authenticate.CustomModelBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.google.GoogleOAuth2',
}

# python social
SOCIAL_AUTH_POSTGRES_JSONFIELD = True

SOCIAL_AUTH_URL_NAMESPACE = 'social'
SOCIAL_AUTH_ADMIN_USER_SEARCH_FIELDS = ['email']

SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']
SOCIAL_AUTH_FACEBOOK_PROFILE_EXTRA_PARAMS = {
    'fields': 'id,name,email',
}

# debug-toolbar
INTERNAL_IPS = '127.0.0.1'

DEFAULT_FROM_EMAIL = 'noreply@intime.digital'

# django-rest-framework
REST_FRAMEWORK = {
    # Use Django's standard `django.contrib.auth` permissions,
    # or allow read-only access for unauthenticated users.
    'DEFAULT_PERMISSION_CLASSES': [
        "rest_framework.permissions.IsAuthenticated",
    ],
    "DEFAULT_PARSER_CLASSES": [
        "rest_framework.parsers.JSONParser",
        'rest_framework.parsers.FormParser',
        'rest_framework.parsers.MultiPartParser',
    ],
    "DEFAULT_SCHEMA_CLASS": "rest_framework.schemas.coreapi.AutoSchema",
    'DEFAULT_AUTHENTICATION_CLASSES': [
        "rest_framework.authentication.SessionAuthentication",
        "api.authentication.CustomJWTAuthentication",
    ],
    'DEFAULT_VERSIONING_CLASS': 'rest_framework.versioning.NamespaceVersioning',
    "EXCEPTION_HANDLER": ("api.exception_handler.custom_exception_handler"),
    "DATE_INPUT_FORMATS": [
        '%Y-%m-%d', '%m/%d/%Y', '%m/%d/%y',  # '2006-10-25', '10/25/2006', '10/25/06'
        '%b %d %Y', '%b %d, %Y',            # 'Oct 25 2006', 'Oct 25, 2006'
        '%d %b %Y', '%d %b, %Y',            # '25 Oct 2006', '25 Oct, 2006'
        '%B %d %Y', '%B %d, %Y',            # 'October 25 2006', 'October 25, 2006'
        '%d %B %Y', '%d %B, %Y',            # '25 October 2006', '25 October, 2006'
        '%d.%m.%Y',                         # 25.10.2006
    ],
    "DATE_FORMAT": "%d.%m.%Y",
    "DATETIME_FORMAT": '%d.%m.%Y %H:%M',
    "DATETIME_INPUT_FORMATS": [
        '%Y-%m-%d %H:%M:%S',     # '2006-10-25 14:30:59'
        '%Y-%m-%d %H:%M:%S.%f',  # '2006-10-25 14:30:59.000200'
        '%Y-%m-%d %H:%M',        # '2006-10-25 14:30'
        '%Y-%m-%d',              # '2006-10-25'
        '%m/%d/%Y %H:%M:%S',     # '10/25/2006 14:30:59'
        '%m/%d/%Y %H:%M:%S.%f',  # '10/25/2006 14:30:59.000200'
        '%m/%d/%Y %H:%M',        # '10/25/2006 14:30'
        '%m/%d/%Y',              # '10/25/2006'
        '%m/%d/%y %H:%M:%S',     # '10/25/06 14:30:59'
        '%m/%d/%y %H:%M:%S.%f',  # '10/25/06 14:30:59.000200'
        '%m/%d/%y %H:%M',        # '10/25/06 14:30'
        '%m/%d/%y',              # '10/25/06'
        '%d.%m.%Y %H:%M:%S',     # '25.10.2006 14:30:59'
        '%d.%m.%Y %H:%M',        # '25.10.2006 14:30'
    ],
    "TIME_INPUT_FORMATS": [
        '%H:%M:%S',     # '14:30:59'
        '%H:%M:%S.%f',  # '14:30:59.000200'
        '%H:%M',        # '14:30'
    ],
    "TIME_FORMAT": '%H:%M:%S',
}

# cors-headers allowed_domains
# CORS_ORIGIN_WHITELIST = (
# 'localhost:3000'
# )

# for tests
CORS_ORIGIN_ALLOW_ALL = True

SWAGGER_SETTINGS = {
    'api_version': '1',
    'is_authenticated': False,
    'is_superuser': False,
    'unauthenticated_user': None,
    'LOGIN_URL': 'rest_framework:login',
    'LOGOUT_URL': 'rest_framework:logout',
    'SECURITY_DEFINITIONS': {
        'api_key': {
            'type': 'apiKey',
            'in': 'header',
            'name': 'Authorization'
        }
    }
}

# celery
CELERY_ACCEPT_CONTENT = ['json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'
CELERY_ENABLE_UTC = True
CELERY_BROKER_URL = 'amqp://guest@localhost:5672//'


# password change config
OLD_PASSWORD_FIELD_ENABLED = True
LOGOUT_ON_PASSWORD_CHANGE = False

# admins
ADMINS = [('Intime Admin', 'support@intime.digital.com')]

# config for logger
LOGGING_CONFIG = 'logging.config.dictConfig'
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'default': {
            'format': "[%(asctime)s] %(levelname)s [%(name)s:%(lineno)s] %(message)s",
            'datefmt': "%Y-%m-%d %H:%M:%S",
        },
    },
    'handlers': {
        'file': {
            'level': 'INFO',
            'class': 'logging.FileHandler',
            'formatter': 'default',
            'filename': os.path.join(BASE_DIR, 'logs/django/debug.log'),
        },
    },
    'loggers': {
        'django': {
            'handlers': ['file'],
            'propagate': True,
            'level': 'INFO',
        },
    }
}

# FIREBASE_ORM_CERTIFICATE = os.path.join(BASE_DIR, 'articles/intime-267309-9501628539c3.json')
# FIREBASE_ORM_BUCKET_NAME = 'intime-267309.appspot.com'

# PUSHTABLE_ENDPOINT = "https://www.pushtable.com/api/firestore/intime-267309/"
