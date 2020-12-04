"""
Django settings for tock.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

from django.utils.crypto import get_random_string
from pathlib import Path

from .env import env

BASE_DIR = os.path.dirname(os.path.dirname(__file__))
DATABASES = {}
ROOT_URLCONF = 'tock.urls'
WSGI_APPLICATION = 'tock.wsgi.application'
SECRET_KEY = env.get_credential('DJANGO_SECRET_KEY', get_random_string(50))
LOGIN_URL = '/auth/login'
LOGIN_REDIRECT_URL = '/'

CSRF_FAILURE_VIEW = 'tock.views.csrf_failure'

INSTALLED_APPS = (
    'django.contrib.contenttypes',  # may be okay to remove
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'tock.apps.TockAppConfig',
    'projects.apps.ProjectsAppConfig',
    'hours.apps.HoursAppConfig',
    'employees.apps.EmployeesAppConfig',
    'organizations.apps.OrganizationsAppConfig',
    'api.apps.ApiAppConfig',
    'utilization.apps.UtilizationAppConfig',
    'rest_framework.authtoken',
)

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            '/templates/'
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.media',
                'django.template.context_processors.static',
                'django.template.context_processors.tz',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.request',
                'tock.context_processors.version_url',
                'tock.context_processors.tock_request_form_url',
            ],
        },
    },
]


MIDDLEWARE = (
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'tock.middleware.AutoLogout',
)

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
)

ACCOUNT_USER_MODEL_USERNAME_FIELD = 'username'
ACCOUNT_EMAIL_REQUIRED = True
ACCOUNT_AUTHENTICATION_METHOD = 'email'
ACCOUNT_LOGOUT_REDIRECT_URL = '/'
ACCOUNT_EMAIL_VERIFICATION = 'optional'
ACCOUNT_EMAIL_SUBJECT_PREFIX = ''
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 1
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = True

SITE_ID = 1

LANGUAGE_CODE = 'en-us'
TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = True
USE_TZ = True

STATIC_ROOT = os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'

REST_FRAMEWORK = {
    'UNICODE_JSON': False,
    'DEFAULT_RENDERER_CLASSES': (
        'rest_framework.renderers.JSONRenderer',
        # use our CSV renderer instead of rest_framework_csv's
        'api.renderers.PaginatedCSVRenderer',
    ),
    'DEFAULT_PERMISSION_CLASSES': (
        'rest_framework.permissions.IsAuthenticated',
    ),
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework.authentication.TokenAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
}

try:
    VERSION = (Path(BASE_DIR) / '..' / 'VERSION').read_text().strip()
except IOError:
    VERSION = 'main'

AUTO_LOGOUT_DELAY_MINUTES = 60

TOCK_CHANGE_REQUEST_FORM = '#'

# enable HSTS according to https://cyber.dhs.gov/bod/18-01/
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True

# UTILIZATION
RECENT_TOCKS_TO_REPORT = 5
STARTING_FY_FOR_REPORTS_PAGE = 2019
RECENT_TIMECARDS_FOR_BILLABILITY = 4
HOURS_IN_A_REGULAR_WORK_WEEK = 40
DEFAULT_BILLABLE_EXPECTATION = 0.80
DEFAULT_EXPECTED_BILLABLE_HOURS = round(HOURS_IN_A_REGULAR_WORK_WEEK * DEFAULT_BILLABLE_EXPECTATION)
